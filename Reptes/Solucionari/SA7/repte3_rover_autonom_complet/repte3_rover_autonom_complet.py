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
