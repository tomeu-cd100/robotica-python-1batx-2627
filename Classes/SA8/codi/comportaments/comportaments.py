# SA8 - comportaments.py  (arquitectura de prioritats, Sessio 1)
# Generalitza el que ja fan segueix_linia.py i evita_obstacles.py (SA7) en
# UNA sola arquitectura de prioritats amb tres estats (FSM, mateix patro que
# maquina_estats_semafor.py i vehicle_seguretat.py de la SA6): SEGUIR linia
# FINS QUE apareix un obstacle -> ESQUIVAR-lo -> RECUPERAR la linia perduda
# -> torna a SEGUIR. Sense classes: nomes funcions + una variable d'estat.
# Aquest programa es la base conceptual de telemetria_radio.py (Sessio 2-3):
# alla es reutilitza EXACTAMENT aquesta mateixa FSM, afegint-hi Kit 3 i
# radio, perque la telemetria tingui quelcom rellevant a explicar (l'estat).
# Cablatge (00_Fil_conductor_construccions.md #1b, font unica; sense canvis
# respecte SA7): M1=P13/P14, M2=P15/P16, HC-SR04 trigger=P1 echo=P2,
# seguidor de linia=P0, polsador STOP=P12 (pull-up intern).
# Simulador: python.microbit.org NO simula motors, HC-SR04 ni seguidor de
# linia; aquest programa es prova NOMES amb el rover real.

from microbit import *
import machine
import utime

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

TRIGGER = pin1
ECHO = pin2
SEGUIDOR_LINIA = pin0

POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)   # sense aixo la lectura flota

VELOCITAT_SO_CM_US = 0.0343
LLINDAR_OBSTACLE_CM = 15
LLINDAR_LINIA = 500

VELOCITAT_AVANCAR = 400
VELOCITAT_GIR = 300

# Tres estats possibles, nomes UN a la vegada (variable d'estat, com a SA6):
# SEGUIR es l'estat per defecte (prioritat normal), ESQUIVAR guanya sempre
# que hi ha un obstacle a prop (prioritat maxima), RECUPERAR nomes actua
# quan venim de ESQUIVAR i encara no hem retrobat la linia.
SEGUIR, ESQUIVAR, RECUPERAR = range(3)
NOMS_ESTAT = {SEGUIR: "SEGUIR", ESQUIVAR: "ESQUIVAR", RECUPERAR: "RECUPERAR"}

estat = SEGUIR


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


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
    # Prioritat maxima ABSOLUTA (per damunt de qualsevol estat de la FSM):
    # mateix patro que vehicle_seguretat.py (SA6) i rover_missions.py (SA7).
    return not POLSADOR_STOP.read_digital()


def actualitza_estat(nou):
    # Un unic lloc que canvia "estat", perque mostrar-lo (display) no es
    # repeteixi cada cop que canvia (mateixa idea que maquina_estats_semafor.py).
    global estat
    estat = nou
    display.show(NOMS_ESTAT[estat][0])


actualitza_estat(SEGUIR)

while True:
    # 1a comprovacio de cada volta, per damunt de la FSM de comportament:
    # el polsador d'emergencia.
    if polsador_premut():
        aturar()
        display.show(Image.NO)
        sleep(20)
        continue

    distancia = mesura_distancia()
    lectura_linia = SEGUIDOR_LINIA.read_analog()

    if estat == SEGUIR:
        # Prioritat: l'obstacle guanya SEMPRE al seguiment de linia, encara
        # que en aquell instant la linia es vegi be.
        if distancia is not None and distancia < LLINDAR_OBSTACLE_CM:
            aturar()
            actualitza_estat(ESQUIVAR)
        elif lectura_linia < LLINDAR_LINIA:
            avancar(VELOCITAT_AVANCAR)
        else:
            girar('esquerra')   # estrategia de cerca fixa (un unic sensor)
    elif estat == ESQUIVAR:
        # Gir fix per apartar-se de l'obstacle; en acabar, passa a RECUPERAR.
        girar('dreta')
        sleep(400)
        aturar()
        actualitza_estat(RECUPERAR)
    elif estat == RECUPERAR:
        # Cerca la linia altre cop: si la retroba, torna a SEGUIR; si no,
        # continua avancant a poc a poc mentre la busca.
        if lectura_linia < LLINDAR_LINIA:
            actualitza_estat(SEGUIR)
        else:
            avancar(VELOCITAT_AVANCAR)
            sleep(150)
            aturar()

    sleep(20)
