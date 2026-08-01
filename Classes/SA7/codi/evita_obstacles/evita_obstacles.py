# SA7 - evita_obstacles.py  (comportament autonom, Sessio 3)
# Sensor d'ultrasons HC-SR04 (Kit 2): mesura la distancia amb el temps de
# vol de l'eco (time-of-flight), EXACTAMENT el mateix patro de
# alarma_ultrasons.py (SA3), pero amb els pins DEFINITIUS del rover:
# trigger P1, echo P2 (a la SA3 es practicava a P14/P15, banc de proves de
# la mascota; al rover P14/P15 son ara dels motors, per aixo l'HC-SR04
# canvia de pins, veure 00_Fil_conductor_construccions.md #1b).
# Reutilitza les funcions de moviment de la SA4 (avancar/girar/aturar).
# Maquinari: veure SA7_esquemes_connexions.md (HC-SR04 a 5 V, trigger P1,
# echo P2).
# Simulador: python.microbit.org NO simula l'HC-SR04 ni els motors; aquesta
# practica es fa NOMES amb maquinari real.

from microbit import *
import machine
import utime

TRIGGER = pin1
ECHO = pin2

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

VELOCITAT_SO_CM_US = 0.0343  # cm per microsegon (a temperatura ambient)
LLINDAR_OBSTACLE_CM = 15     # per sota d'aixo, es considera obstacle proper

VELOCITAT_AVANCAR = 400
VELOCITAT_GIR = 300


def mesura_distancia():
    # ACTIVITAT NUCLI (lectura robusta d'un sensor): time_pulse_us pot NO
    # trobar mai el pols esperat (obstacle massa lluny, eco perdut, sensor
    # mal cablejat). Segons la placa/versio de MicroPython aixo es manifesta
    # de DUES maneres possibles: retornant un valor negatiu (-1/-2, ja
    # comprovat sota) O BE llancant una excepcio OSError. Un "try/except"
    # cobreix aquesta segona possibilitat perque una lectura puntual dolenta
    # NO aturi tot el programa del rover.
    TRIGGER.write_digital(0)
    utime.sleep_us(2)
    TRIGGER.write_digital(1)
    utime.sleep_us(10)
    TRIGGER.write_digital(0)

    try:
        # Echo: machine.time_pulse_us mesura quant triga el pin en estar a 1.
        durada_us = machine.time_pulse_us(ECHO, 1, 30000)   # 30 ms (~5 m)
    except OSError:
        return None   # timeout llancat com a excepcio: cap eco rebut

    if durada_us < 0:
        return None   # timeout retornat com a valor negatiu: mateix cas
    # Anada i tornada: la distancia real es la meitat del recorregut total.
    return (durada_us * VELOCITAT_SO_CM_US) / 2


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


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


while True:
    # EXEMPLE RESOLT: cicle reactiu - llegir la distancia a CADA volta, no
    # un sol cop abans del bucle.
    distancia = mesura_distancia()

    if distancia is not None and distancia < LLINDAR_OBSTACLE_CM:
        aturar()
        display.show(Image.NO)
        girar('esquerra', VELOCITAT_GIR)
        sleep(400)
    else:
        avancar(VELOCITAT_AVANCAR)
        display.show(Image.ARROW_N)

    sleep(50)
