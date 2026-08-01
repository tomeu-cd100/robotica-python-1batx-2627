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
