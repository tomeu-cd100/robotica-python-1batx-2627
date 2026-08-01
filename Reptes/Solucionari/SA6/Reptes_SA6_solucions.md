# SA6 · Solucionari dels reptes — Control: el robot decideix

> **Material del docent.** Solucions completes dels tres reptes de [`Reptes_SA6.md`](../../Reptes_SA6.md), amb el nucli i les tres ampliacions graduades ja incorporades. **No es reparteix a l'alumnat abans que hagi entregat el seu propi repte**: com l'exemple resolt de la SA, serveix per corregir i, si cal, per mostrar *després* del primer intent.

> Cada solució és una còpia exacta del fitxer `.py` de la seva carpeta (`repte1_termostat_multizona/`, `repte2_semafor_vianants/`, `repte3_vehicle_alerta/`): si canvies un fitxer, actualitza també el bloc de codi d'aquí sota.

---

## ⭐ Repte 1 · Termòstat de dues zones

**Idea de la solució:** dues parelles de llindars (histèresi independent per zona), un actuador per zona (relé a P2, LED a P1), una lletra al display segons quina zona és activa (ampliació 1), un comptador de canvis d'estat per zona mostrat per REPL amb A+B (ampliació 2), i una alerta d'emergència per sobreescalfament que desactiva els dos actuadors per davant de qualsevol altra lògica (ampliació 3).

```python
# SA6 - Repte 1 (SOLUCIO): termostat de dues zones
# Nucli + ampliacions 1-3: display amb la zona activa, comptador de canvis
# d'estat per zona, i una alerta d'emergencia per sobreescalfament que
# desactiva els dos actuadors per davant de qualsevol altra logica.
# Maquinari: temperature() interna (simula les dues zones amb el mateix
# sensor, en un cas real serien dos sensors); actuador zona 1 = pin2 (rele),
# actuador zona 2 = pin1 (LED, substitut segur).

from microbit import *

ACTUADOR_1 = pin2
ACTUADOR_2 = pin1

LLINDAR_BAIX_1 = 24
LLINDAR_ALT_1 = 26
LLINDAR_BAIX_2 = 20
LLINDAR_ALT_2 = 22

LLINDAR_EMERGENCIA = 32   # ampliacio 3: sobreescalfament

actiu_1 = False
actiu_2 = False
alerta = False

canvis_1 = 0   # ampliacio 2: comptador de canvis d'estat per zona
canvis_2 = 0


def actualitza_zona(temp):
    global actiu_1, actiu_2, canvis_1, canvis_2

    if not actiu_1 and temp < LLINDAR_BAIX_1:
        actiu_1 = True
        canvis_1 += 1
    elif actiu_1 and temp > LLINDAR_ALT_1:
        actiu_1 = False
        canvis_1 += 1

    if not actiu_2 and temp < LLINDAR_BAIX_2:
        actiu_2 = True
        canvis_2 += 1
    elif actiu_2 and temp > LLINDAR_ALT_2:
        actiu_2 = False
        canvis_2 += 1


while True:
    temp = temperature()

    if temp > LLINDAR_EMERGENCIA:
        # Ampliacio 3: alerta d'emergencia, per davant de qualsevol zona.
        alerta = True
        actiu_1 = False
        actiu_2 = False
    elif alerta and temp < LLINDAR_ALT_1:
        alerta = False   # torna a control normal quan ja no fa tanta calor

    if alerta:
        ACTUADOR_1.write_digital(0)
        ACTUADOR_2.write_digital(0)
        display.show(Image.SKULL)
    else:
        actualitza_zona(temp)
        ACTUADOR_1.write_digital(1 if actiu_1 else 0)
        ACTUADOR_2.write_digital(1 if actiu_2 else 0)
        # Ampliacio 1: lletra segons quina zona esta activa.
        if actiu_1 and actiu_2:
            display.show("B")
        elif actiu_1:
            display.show("1")
        elif actiu_2:
            display.show("2")
        else:
            display.clear()

    if button_a.was_pressed() and button_b.was_pressed():
        print("Canvis zona 1:", canvis_1, "  Canvis zona 2:", canvis_2)

    sleep(500)
```

---

## ⭐⭐ Repte 2 · Semàfor de vianants amb botó prioritari

**Idea de la solució:** manté el diccionari `TRANSICIONS` del nucli i hi afegeix una variable `sollicitud_pendent` que, si el botó A es prem **durant el VERD** (ampliació 2), escurça el temps restant a un màxim d'1 segon (requisit mínim + ampliació 1, amb una icona de sol·licitud). El semàfor de vianants (ampliació 3) es calcula amb una funció pura `semafor_vianants()`, sense guardar cap variable d'estat pròpia: sempre és el contrari del de vehicles.

```python
# SA6 - Repte 2 (SOLUCIO): semafor de vianants amb boto prioritari
# Nucli + ampliacions 1-3: icona de sol.licitud pendent, boto que nomes
# "compta" durant el VERD, i un segon semafor (vianants) sempre en l'estat
# contrari al de vehicles, sense duplicar la logica de transicions.
# Maquinari: cap de nou, nomes el display i el boto A de la micro:bit.

from microbit import *

VERD, GROC, VERMELL = range(3)

TRANSICIONS = {
    VERD: (GROC, 3000),
    GROC: (VERMELL, 1000),
    VERMELL: (VERD, 3000),
}

IMATGES = {
    VERD: Image.SQUARE,
    GROC: Image.DIAMOND,
    VERMELL: Image.SQUARE_SMALL,
}

estat = VERMELL
sollicitud_pendent = False   # ampliacio 1: boto premut, esperant efecte


def semafor_vianants(estat_vehicles):
    # Ampliacio 3: el semafor de vianants es SEMPRE el contrari del de
    # vehicles, sense cap variable d'estat propia (es dedueix, no es guarda).
    return VERMELL if estat_vehicles != VERMELL else VERD


def actualitza_estat(nou):
    global estat
    estat = nou
    display.show(IMATGES[estat])
    print("Vehicles ->", estat, " Vianants ->", semafor_vianants(estat))


actualitza_estat(estat)
temps_restant = TRANSICIONS[estat][1]

while True:
    # Ampliacio 2: el boto nomes "compta" durant el VERD.
    if button_a.was_pressed() and estat == VERD:
        sollicitud_pendent = True

    pas = 100
    sleep(pas)
    temps_restant -= pas

    if sollicitud_pendent and estat == VERD:
        # Ampliacio 1 + requisit minim: escurca el VERD a un maxim d'1s.
        temps_restant = min(temps_restant, 1000)
        display.show(Image.SQUARE)   # icona de sol.licitud (aqui, el propi verd)

    if temps_restant <= 0:
        proxim, durada = TRANSICIONS[estat]
        actualitza_estat(proxim)
        temps_restant = durada
        if estat != VERD:
            sollicitud_pendent = False
```

---

## ⭐⭐⭐ Repte 3 · Vehicle amb alerta per temperatura i registre de bord

**Idea de la solució:** afegeix el tercer estat `ALERTA` a `vehicle_seguretat.py` sense tocar l'STOP prioritari (polsador i `"X"` continuen funcionant exactament igual). L'ALERTA s'activa amb histèresi (`LLINDAR_ALERTA_ALT`/`LLINDAR_ALERTA_BAIX`) i queda registrada amb `log.add()` cada vegada que s'hi entra o se'n surt (ampliació 1), amb un comptador propi mostrat per REPL amb A+B (ampliació 2) i una comanda de ràdio `"A"` per provocar-la manualment en proves (ampliació 3).

```python
# SA6 - Repte 3 (SOLUCIO): vehicle amb alerta per temperatura i registre de bord
# Nucli de vehicle_seguretat.py (protocol CMD/STOP prioritari intacte) +
# ampliacions 1-3: tercer estat ALERTA amb histeresi propia, registre amb
# log.add() de cada entrada/sortida d'ALERTA, comptador propi per REPL, i
# una comanda de radio "A" per provocar l'ALERTA manualment (proves).
# Maquinari: vehicle T2 (M1=P13/P14, M2=P15/P16), LED=P1, polsador=P12,
# temperature() interna per a l'ALERTA automatica.

from microbit import *
import radio
import log

GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

LED_ESTAT = pin1
POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)   # sense aixo la lectura flota
# amb pull-up intern: repos = 1, premut = 0 (LOW)

VELOCITAT = 400

RUN, STOP, ALERTA = range(3)
estat = STOP

LLINDAR_ALERTA_ALT = 30    # entra en ALERTA per sobre d'aixo
LLINDAR_ALERTA_BAIX = 27   # nomes pot tornar a RUN per sota d'aixo (histeresi)

log.set_labels('event', 'temp')
entrades_alerta = 0   # ampliacio 2: comptador propi, a mes del log


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


def actualitza_led():
    if estat == RUN:
        LED_ESTAT.write_digital(1)
    elif estat == STOP:
        LED_ESTAT.write_digital(0)
    else:
        LED_ESTAT.write_digital(1 if running_time() % 400 < 200 else 0)


def actualitza_estat(nou):
    global estat, entrades_alerta
    if nou in (STOP, ALERTA):
        aturar()
        display.show(Image.NO if nou == STOP else Image.SAD)
    if nou == ALERTA and estat != ALERTA:
        entrades_alerta += 1
        log.add(event="entra_alerta", temp=temperature())
    elif estat == ALERTA and nou != ALERTA:
        log.add(event="surt_alerta", temp=temperature())
    estat = nou
    actualitza_led()


actualitza_estat(STOP)

while True:
    if not POLSADOR_STOP.read_digital():
        actualitza_estat(STOP)

    temp = temperature()
    if estat != STOP:
        if temp > LLINDAR_ALERTA_ALT:
            actualitza_estat(ALERTA)
        elif estat == ALERTA and temp < LLINDAR_ALERTA_BAIX:
            actualitza_estat(STOP)   # surt d'ALERTA, cal ordre nova per RUN

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ordre = missatge[len(PREFIX):]
        if ordre == "X":
            actualitza_estat(STOP)
        elif ordre == "A":
            # Ampliacio 3: provocar l'ALERTA manualment (proves de seguretat).
            actualitza_estat(ALERTA)
        elif ordre == "S":
            actualitza_estat(STOP)
        elif estat == STOP and ordre in ("F", "B", "L", "R"):
            actualitza_estat(RUN)
        if estat == RUN:
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

    if button_a.was_pressed() and button_b.was_pressed():
        print("Entrades en ALERTA aquesta sessio:", entrades_alerta)

    sleep(20)
```

---

*Solucionari de la SA6. Material del docent, no es reparteix abans de l'entrega de l'alumnat. Llicència CC BY-SA 4.0.*
