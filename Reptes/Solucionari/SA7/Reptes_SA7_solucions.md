# SA7 · Solucionari dels reptes — Robòtica mòbil: el rover

> **Material del docent.** Solucions completes dels tres reptes de [`Reptes_SA7.md`](../../Reptes_SA7.md), amb el nucli i les tres ampliacions graduades ja incorporades. **No es reparteix a l'alumnat abans que hagi entregat el seu propi repte**: com l'exemple resolt de la SA, serveix per corregir i, si cal, per mostrar *després* del primer intent.

> Cada solució és una còpia exacta del fitxer `.py` de la seva carpeta (`repte1_seguidor_avancat/`, `repte2_evita_intelligent/`, `repte3_rover_autonom_complet/`): si canvies un fitxer, actualitza també el bloc de codi d'aquí sota.

---

## ⭐ Repte 1 · Carret de magatzem amb velocitat variable

**Idea de la solució:** manté `read_analog()` i el llindar del nucli, però distingeix **tres zones** (clarament línia, zona intermèdia, línia perduda) amb tres velocitats diferents: normal, intermèdia (ampliació 3) i de correcció (requisit mínim). Una icona diferent al display per a cada zona (ampliació 1) i un comptador de correccions mostrat per REPL amb A+B (ampliació 2), que només suma a l'**inici** de cada correcció, no a cada volta del bucle mentre dura.

```python
# SA7 - Repte 1 (SOLUCIO): carret de magatzem amb velocitat variable
# Nucli + ampliacions 1-3: icona segons la velocitat, comptador de
# correccions per REPL, i una zona intermedia de llindar amb velocitat
# encara mes reduida (aproximacio basica a un control mes suau).
# Maquinari: seguidor de linia KS0050 a P0, motors M1=P13/P14, M2=P15/P16.

from microbit import *

SEGUIDOR_LINIA = pin0

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

LLINDAR_LINIA = 500
MARGE_INTERMIG = 60   # ampliacio 3: zona "quasi al limit" al voltant del llindar

VELOCITAT_NORMAL = 400
VELOCITAT_CORRECCIO = 220     # requisit minim: mes lenta durant els girs
VELOCITAT_INTERMEDIA = 300    # ampliacio 3: zona intermedia

correccions = 0   # ampliacio 2: comptador de vegades que ha corregit


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def girar(costat, velocitat=300):
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat)
        M1_ENDAVANT.write_digital(0)
        M2_ENDAVANT.write_analog(velocitat)
        M2_ENRERE.write_digital(0)
    elif costat == 'dreta':
        M1_ENDAVANT.write_analog(velocitat)
        M1_ENRERE.write_digital(0)
        M2_ENRERE.write_analog(velocitat)
        M2_ENDAVANT.write_digital(0)


estava_corregint = False

while True:
    lectura = SEGUIDOR_LINIA.read_analog()

    if lectura < LLINDAR_LINIA - MARGE_INTERMIG:
        # Clarament sobre la linia: velocitat normal.
        avancar(VELOCITAT_NORMAL)
        display.show(Image.ARROW_N)
        estava_corregint = False
    elif lectura < LLINDAR_LINIA:
        # Ampliacio 3: zona intermedia, ni clarament linia ni clarament fons.
        avancar(VELOCITAT_INTERMEDIA)
        display.show(Image.CHESSBOARD)
        estava_corregint = False
    else:
        # Linia perduda: corregeix a velocitat reduida (requisit minim).
        if not estava_corregint:
            correccions += 1   # ampliacio 2: nomes compta l'inici de cada correccio
            estava_corregint = True
        girar('esquerra', VELOCITAT_CORRECCIO)
        display.show(Image.ARROW_W)

    if button_a.was_pressed() and button_b.was_pressed():
        print("Correccions de rumb aquesta sessio:", correccions)

    sleep(20)
```

---

## ⭐⭐ Repte 2 · Vehicle d'inspecció amb marge de seguretat variable

**Idea de la solució:** afegeix un segon llindar (`LLINDAR_ALT_CM`) que crea una **zona intermèdia** de velocitat reduïda entre "lluny" i "massa a prop" (requisit mínim), amb una icona diferent per zona (ampliació 1). Guarda les 5 últimes distàncies en una llista i en mostra la mitjana per REPL (ampliació 2). Un tercer llindar (`LLINDAR_RETROCES_CM`) fa retrocedir el rover una mica abans de girar quan l'obstacle és massa a prop per girar amb seguretat (ampliació 3).

```python
# SA7 - Repte 2 (SOLUCIO): vehicle d'inspeccio amb marge de seguretat variable
# Nucli + ampliacions 1-3: icona segons la zona de distancia, registre de les
# 5 ultimes distancies amb mitjana per REPL, i un tercer llindar que fa
# retrocedir el rover una mica abans de girar si l'obstacle es massa a prop.
# Maquinari: HC-SR04 trigger=P1, echo=P2; motors M1=P13/P14, M2=P15/P16.

from microbit import *
import machine
import utime

TRIGGER = pin1
ECHO = pin2

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

VELOCITAT_SO_CM_US = 0.0343

LLINDAR_ALT_CM = 40     # per sobre: velocitat normal
LLINDAR_BAIX_CM = 15    # entre baix i alt: velocitat reduida; per sota: atura't
LLINDAR_RETROCES_CM = 5  # ampliacio 3: massa a prop, cal retrocedir abans de girar

VELOCITAT_NORMAL = 400
VELOCITAT_REDUIDA = 220
VELOCITAT_GIR = 300

ultimes_distancies = []   # ampliacio 2: registre de les 5 ultimes lectures


def mesura_distancia():
    TRIGGER.write_digital(0)
    utime.sleep_us(2)
    TRIGGER.write_digital(1)
    utime.sleep_us(10)
    TRIGGER.write_digital(0)
    durada_us = machine.time_pulse_us(ECHO, 1, 30000)
    if durada_us < 0:
        return None
    return (durada_us * VELOCITAT_SO_CM_US) / 2


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


def girar(costat, velocitat=VELOCITAT_GIR):
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat)
        M1_ENDAVANT.write_digital(0)
        M2_ENDAVANT.write_analog(velocitat)
        M2_ENRERE.write_digital(0)
    elif costat == 'dreta':
        M1_ENDAVANT.write_analog(velocitat)
        M1_ENRERE.write_digital(0)
        M2_ENRERE.write_analog(velocitat)
        M2_ENDAVANT.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


while True:
    d = mesura_distancia()

    if d is not None:
        # Ampliacio 2: registre de les 5 ultimes lectures.
        ultimes_distancies.append(d)
        if len(ultimes_distancies) > 5:
            ultimes_distancies.pop(0)

    if d is None or d > LLINDAR_ALT_CM:
        avancar(VELOCITAT_NORMAL)
        display.show(Image.ARROW_N)
    elif d > LLINDAR_BAIX_CM:
        avancar(VELOCITAT_REDUIDA)
        display.show(Image.CHESSBOARD)
    elif d > LLINDAR_RETROCES_CM:
        aturar()
        display.show(Image.NO)
        girar('esquerra')
        sleep(400)
    else:
        # Ampliacio 3: massa a prop per girar amb seguretat, retrocedeix.
        aturar()
        display.show(Image.SAD)
        retrocedir(VELOCITAT_REDUIDA)
        sleep(300)
        aturar()
        girar('esquerra')
        sleep(400)

    if button_a.was_pressed() and button_b.was_pressed() and ultimes_distancies:
        mitjana = sum(ultimes_distancies) / len(ultimes_distancies)
        print("Mitjana ultimes distancies (cm):", mitjana)

    sleep(50)
```

---

## ⭐⭐⭐ Repte 3 · Rover de repartiment amb missió completa i registre de bord

**Idea de la solució:** manté la comprovació prioritària del polsador STOP de `rover_missions.py`, i hi afegeix `missio_lliurament()`: segueix la línia fins detectar un obstacle (zona de lliurament), s'atura 2 s (entrega simulada) i torna enrere aproximant la durada del retorn a la de l'anada. Cada missió completa es registra amb `log.add()` amb la seva durada (ampliació 1), amb un comptador propi mostrat per REPL amb A+B (ampliació 2), i el botó B pot encadenar una segona missió automàticament sense tornar-lo a prémer (ampliació 3).

```python
# SA7 - Repte 3 (SOLUCIO): rover de repartiment amb missio completa i registre
# Nucli de rover_missions.py (polsador STOP prioritari intacte) + ampliacions
# 1-3: missio "lliurament" (segueix linia fins obstacle, s'atura 2s, torna),
# registre amb log.add() de cada missio completada (amb la seva durada),
# comptador propi mostrat per REPL, i encadenament automatic de dues missions
# seguides sense tornar a premer el boto B entremig.
# Maquinari: M1=P13/P14, M2=P15/P16, HC-SR04 trigger=P1/echo=P2, seguidor de
# linia=P0, polsador STOP=P12 (pull-up).

from microbit import *
import machine
import utime
import log

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

TRIGGER = pin1
ECHO = pin2
SEGUIDOR_LINIA = pin0

POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)

VELOCITAT_SO_CM_US = 0.0343
LLINDAR_OBSTACLE_CM = 15
LLINDAR_LINIA = 500

VELOCITAT_AVANCAR = 400
VELOCITAT_GIR = 300

log.set_labels('event', 'durada_ms')
missions_completades = 0   # ampliacio 2: comptador propi, a mes del log


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


def girar(costat, velocitat=VELOCITAT_GIR):
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat)
        M1_ENDAVANT.write_digital(0)
        M2_ENDAVANT.write_analog(velocitat)
        M2_ENRERE.write_digital(0)
    elif costat == 'dreta':
        M1_ENDAVANT.write_analog(velocitat)
        M1_ENRERE.write_digital(0)
        M2_ENRERE.write_analog(velocitat)
        M2_ENDAVANT.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def mesura_distancia():
    TRIGGER.write_digital(0)
    utime.sleep_us(2)
    TRIGGER.write_digital(1)
    utime.sleep_us(10)
    TRIGGER.write_digital(0)
    durada_us = machine.time_pulse_us(ECHO, 1, 30000)
    if durada_us < 0:
        return None
    return (durada_us * VELOCITAT_SO_CM_US) / 2


def polsador_premut():
    return not POLSADOR_STOP.read_digital()


def missio_lliurament():
    # Requisit minim: segueix la linia fins detectar un obstacle (zona de
    # lliurament), s'atura 2 s simulant l'entrega, i torna cap enrere.
    global missions_completades
    inici = running_time()

    # 1a part: anar fins la zona de lliurament.
    while not polsador_premut():
        d = mesura_distancia()
        if d is not None and d < LLINDAR_OBSTACLE_CM:
            aturar()
            break
        lectura = SEGUIDOR_LINIA.read_analog()
        if lectura < LLINDAR_LINIA:
            avancar(VELOCITAT_AVANCAR)
        else:
            girar('esquerra')
        sleep(20)

    if polsador_premut():
        return

    display.show(Image.YES)   # "entrega" simulada
    sleep(2000)

    # 2a part: tornar (mitja volta + el mateix temps que ha durat l'anada).
    if polsador_premut():
        return
    durada_anada = running_time() - inici
    girar('dreta')
    sleep(860)
    if polsador_premut():
        return
    avancar(VELOCITAT_AVANCAR)
    sleep(min(durada_anada, 4000))   # marge maxim per no allargar-se massa
    aturar()

    if not polsador_premut():
        durada_total = running_time() - inici
        missions_completades += 1   # ampliacio 2
        log.add(event="missio_completada", durada_ms=durada_total)   # ampliacio 1


display.show("R")

while True:
    if polsador_premut():
        aturar()
        display.show(Image.NO)

    if button_b.was_pressed() and not polsador_premut():
        missio_lliurament()
        display.show("R")

        # Ampliacio 3: encadenar una segona missio automaticament, sense
        # tornar a premer el boto B, si el polsador no s'ha premut.
        if not polsador_premut():
            sleep(500)
            missio_lliurament()
            display.show("R")

    if button_a.was_pressed() and button_b.was_pressed():
        print("Missions completades aquesta sessio:", missions_completades)

    sleep(20)
```

---

*Solucionari de la SA7. Material del docent, no es reparteix abans de l'entrega de l'alumnat. Llicència CC BY-SA 4.0.*
