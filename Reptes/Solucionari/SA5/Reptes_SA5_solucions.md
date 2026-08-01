# SA5 · Solucionari dels reptes — Ràdio: robots que parlen

> **Material del docent.** Solucions completes dels tres reptes de [`Reptes_SA5.md`](../../Reptes_SA5.md), amb el nucli i les tres ampliacions graduades ja incorporades. **No es reparteix a l'alumnat abans que hagi entregat el seu propi repte**: com l'exemple resolt de la SA, serveix per corregir i, si cal, per mostrar *després* del primer intent.

> Cada solució és una còpia exacta del fitxer `.py` de la seva carpeta (`repte1_xat_classe/`, `repte2_comandament_gestos/`, `repte3_historic_comandes/`): si canvies un fitxer, actualitza també el bloc de codi d'aquí sota. El repte 2 té **dos** fitxers a la seva carpeta: `repte2_comandament_gestos.py` (costat emissor) i `repte2_comandament_gestos_receptor.py` (costat receptor, amb la interpretació de `"CMD:Vn"` que demana l'ampliació 1).

---

## ⭐ Repte 1 · Xat de classe amb identificació

**Idea de la solució:** `mostra_historial()` mostra tots els missatges de la llista `historic` (nucli), un comptador `total_rebuts` mostrat amb A+B (ampliació 1), `mostra_historial_amb_paraula()` que filtra per contingut (ampliació 2) i una comanda especial `"NETEJA"` que buida l'historial (ampliació 3).

```python
# SA5 - Repte 1 (SOLUCIO): xat de classe amb identificacio
# Nucli + ampliacions 1-3: comptador de missatges rebuts, filtre per
# paraula a l'historial, i comanda especial "NETEJA" que buida l'historial.
# Maquinari: cap de nou, nomes la radio interna (com radio_missatges.py).

from microbit import *
import radio

GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

MEU_NOM = "A1"
historic = []
MAX_HISTORIC = 5
total_rebuts = 0   # ampliacio 1: comptador de missatges rebuts


def envia(text):
    radio.send(MEU_NOM + ":" + text)


def desa_al_historic(missatge):
    historic.append(missatge)
    if len(historic) > MAX_HISTORIC:
        historic.pop(0)


def mostra_historial():
    # Requisit minim: mostra tots els missatges de l'historial, un darrere
    # l'altre, separats per un espai (concatenacio amb un for, sense join()).
    text = ""
    for missatge in historic:
        text = text + missatge + " "
    display.scroll(text)


def mostra_historial_amb_paraula(paraula):
    # Ampliacio 2: nomes mostra els missatges que continguin "paraula"
    # (un for que va afegint-los, sense comprensio de llistes).
    text = ""
    for missatge in historic:
        if paraula in missatge:
            text = text + missatge + " "
    display.scroll(text)


while True:
    if button_a.was_pressed():
        envia("Hola")
        display.show(Image.YES)
        sleep(200)
        display.clear()
    if button_b.was_pressed():
        mostra_historial()
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll(str(total_rebuts))

    missatge_rebut = radio.receive()
    if missatge_rebut is not None:
        if missatge_rebut == "NETEJA":
            historic.clear()
            display.show(Image.NO)
            sleep(150)
            display.clear()
        else:
            desa_al_historic(missatge_rebut)
            total_rebuts = total_rebuts + 1
            display.show(Image.HAPPY)
            sleep(150)
            display.clear()
    sleep(20)
```

---

## ⭐⭐ Repte 2 · Comandament amb gestos per a un joc

**Idea de la solució:** tot el comandament es controla amb gestos de l'acceleròmetre (`left`/`right`/`shake`, nucli), dues comandes de velocitat activades amb `face up`/`face down` (ampliació 1), una pausa després de cada gest per evitar enviaments descontrolats (ampliació 2) i una variable `darrera_ordre` que mostra al display local quina ha estat l'última comanda enviada (ampliació 3).

```python
# SA5 - Repte 2 (SOLUCIO): comandament amb gestos per a un joc
# Nucli + ampliacions 1-3: comandes nomes amb gestos (left/right/shake),
# comanda de velocitat variable ("CMD:V3"), control de repeticio amb pausa,
# i confirmacio visual local de la darrera comanda enviada.
# Maquinari: cap de nou, nomes la radio interna (com comandament.py).

from microbit import *
import radio

GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"
darrera_ordre = ""   # ampliacio 3: confirmacio visual local


def envia_ordre(ordre):
    global darrera_ordre
    radio.send(PREFIX + ordre)
    darrera_ordre = ordre
    display.show(ordre)
    sleep(150)
    display.clear()


while True:
    if accelerometer.was_gesture("left"):
        envia_ordre("L")
        sleep(300)
    if accelerometer.was_gesture("right"):
        envia_ordre("R")
        sleep(300)
    if accelerometer.was_gesture("shake"):
        envia_ordre("S")
        sleep(300)
    if accelerometer.was_gesture("face up"):
        envia_ordre("V5")
        sleep(300)
    if accelerometer.was_gesture("face down"):
        envia_ordre("V2")
        sleep(300)
    if button_a.was_pressed():
        display.scroll(darrera_ordre)
    sleep(20)
```

**Costat receptor (ampliació 1):** l'enunciat demana explícitament que `receptor_vehicle.py` interpreti `"CMD:V3"`/`"CMD:V5"` canviant la variable `VELOCITAT`, no només que el comandament les enviï. La solució anterior és el costat **emissor**; aquesta és el costat **receptor** modificat, aparellat amb el mateix `GRUP` i `PREFIX`.

```python
# SA5 - Repte 2 (SOLUCIO, costat RECEPTOR): interpreta la comanda de
# velocitat de l'ampliacio 1 ("CMD:V3", "CMD:V5"...) i ajusta la variable
# VELOCITAT en lloc d'un valor fix, com demana Reptes_SA5.md.
# Parteix de receptor_vehicle.py (SA5, Sessio 3) i hi afegeix NOMES la
# interpretacio de les ordres que comencen per "V".
# Maquinari: vehicle T2 (M1=pin13/pin14, M2=pin15/pin16), com a
# receptor_vehicle.py. Es fa servir aparellat amb
# repte2_comandament_gestos.py (mateix GRUP i mateix PREFIX).

from microbit import *
import radio

GRUP = 1   # ha de coincidir amb el GRUP de repte2_comandament_gestos.py

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

VELOCITAT = 400   # ja no es una constant fixa: l'ordre "Vn" la pot canviar


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def retrocedir(velocitat):
    M1_ENRERE.write_analog(velocitat)
    M1_ENDAVANT.write_digital(0)
    M2_ENRERE.write_analog(velocitat)
    M2_ENDAVANT.write_digital(0)


def girar(costat):
    velocitat_gir = 300
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat_gir)
        M1_ENDAVANT.write_digital(0)
        M2_ENDAVANT.write_analog(velocitat_gir)
        M2_ENRERE.write_digital(0)
    elif costat == 'dreta':
        M1_ENDAVANT.write_analog(velocitat_gir)
        M1_ENRERE.write_digital(0)
        M2_ENRERE.write_analog(velocitat_gir)
        M2_ENDAVANT.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def canvia_velocitat(ordre):
    # Ampliacio 1: "V3" -> VELOCITAT = 3*100 = 300, "V5" -> 500, etc.
    # Nomes es crida si ordre comenca per "V" i la resta son digits.
    global VELOCITAT
    xifra = ordre[1:]
    if xifra.isdigit():
        VELOCITAT = int(xifra) * 100
        display.show(Image.ARROW_N)
        sleep(100)
        display.clear()


def actua(ordre):
    # Esdeveniment -> accio: igual que receptor_vehicle.py, pero ara "V..."
    # no mou el vehicle, nomes en canvia la velocitat de les properes ordres.
    if ordre == "F":
        display.show(Image.ARROW_N)
        avancar(VELOCITAT)
    elif ordre == "B":
        display.show(Image.ARROW_S)
        retrocedir(VELOCITAT)
    elif ordre == "L":
        display.show(Image.ARROW_W)
        girar('esquerra')
    elif ordre == "R":
        display.show(Image.ARROW_E)
        girar('dreta')
    elif ordre == "S":
        display.show(Image.NO)
        aturar()
    elif ordre.startswith("V"):
        canvia_velocitat(ordre)


aturar()
display.show(Image.NO)

while True:
    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ordre = missatge[len(PREFIX):]
        actua(ordre)
    sleep(20)
```

---

## ⭐⭐⭐ Repte 3 · Historial de comandes amb estadístiques

**Idea de la solució:** `comanda_mes_frequent()` recorre les tuples `(ordre, instant)` de `historic_comandes` sense diccionaris (nucli), es mostren per REPL el total i la comanda més freqüent en prémer A+B (ampliació 1), `temps_mitja_entre_comandes()` calcula la diferència mitjana entre instants consecutius (ampliació 2), i el vehicle s'atura automàticament si passen més de 3 s sense cap ordre nova (ampliació 3).

```python
# SA5 - Repte 3 (SOLUCIO): historial de comandes amb estadistiques
# Nucli + ampliacions 1-3: comanda_mes_frequent(), total de comandes i
# temps mitja entre comandes per REPL, i aturada automatica de seguretat
# si fa mes de 3 segons que no arriba cap comanda.
# Maquinari: vehicle T2 (M1=pin13/pin14, M2=pin15/pin16), com a
# receptor_vehicle.py.

from microbit import *
import radio

GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

VELOCITAT = 400
TEMPS_MAXIM_SENSE_ORDRE = 3000

historic_comandes = []
MAX_HISTORIC = 20
ultim_instant_rebut = running_time()


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def retrocedir(velocitat):
    M1_ENRERE.write_analog(velocitat)
    M1_ENDAVANT.write_digital(0)
    M2_ENRERE.write_analog(velocitat)
    M2_ENDAVANT.write_digital(0)


def girar(costat):
    velocitat_gir = 300
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat_gir)
        M1_ENDAVANT.write_digital(0)
        M2_ENDAVANT.write_analog(velocitat_gir)
        M2_ENRERE.write_digital(0)
    elif costat == 'dreta':
        M1_ENDAVANT.write_analog(velocitat_gir)
        M1_ENRERE.write_digital(0)
        M2_ENRERE.write_analog(velocitat_gir)
        M2_ENDAVANT.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def desa_al_historic(ordre):
    historic_comandes.append((ordre, running_time()))
    if len(historic_comandes) > MAX_HISTORIC:
        historic_comandes.pop(0)


def comanda_mes_frequent():
    ordres_vistes = []
    comptadors = []
    for ordre, instant in historic_comandes:
        if ordre in ordres_vistes:
            index = ordres_vistes.index(ordre)
            comptadors[index] = comptadors[index] + 1
        else:
            ordres_vistes.append(ordre)
            comptadors.append(1)
    if len(ordres_vistes) == 0:
        return None
    index_max = comptadors.index(max(comptadors))
    return ordres_vistes[index_max]


def temps_mitja_entre_comandes():
    if len(historic_comandes) < 2:
        return 0
    suma_diferencies = 0
    for i in range(1, len(historic_comandes)):
        instant_anterior = historic_comandes[i - 1][1]
        instant_actual = historic_comandes[i][1]
        suma_diferencies = suma_diferencies + (instant_actual - instant_anterior)
    return suma_diferencies // (len(historic_comandes) - 1)


def actua(ordre):
    if ordre == "F":
        display.show(Image.ARROW_N)
        avancar(VELOCITAT)
    elif ordre == "B":
        display.show(Image.ARROW_S)
        retrocedir(VELOCITAT)
    elif ordre == "L":
        display.show(Image.ARROW_W)
        girar('esquerra')
    elif ordre == "R":
        display.show(Image.ARROW_E)
        girar('dreta')
    elif ordre == "S":
        display.show(Image.NO)
        aturar()


aturar()
display.show(Image.NO)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        print("Total de comandes:", len(historic_comandes))
        print("Comanda mes frequent:", comanda_mes_frequent())
        print("Temps mitja entre comandes (ms):", temps_mitja_entre_comandes())

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ordre = missatge[len(PREFIX):]
        desa_al_historic(ordre)
        ultim_instant_rebut = running_time()
        actua(ordre)

    if running_time() - ultim_instant_rebut > TEMPS_MAXIM_SENSE_ORDRE:
        aturar()
        display.show(Image.SAD)

    sleep(20)
```

---

*Solucionari de la SA5. Material del docent. Es recolza en `Classes/SA5/codi/`. Llicència CC BY-SA 4.0.*
