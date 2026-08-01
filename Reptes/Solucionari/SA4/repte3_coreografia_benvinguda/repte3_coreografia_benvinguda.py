# SA4 - Repte 3 (SOLUCIO): coreografia de benvinguda amb servo, so i motors
# Nucli + ampliacions 1-3: funcio comiat() simetrica, seguencia per botons
# A/B (B atura sempre) i velocitat com a parametre de cada crida.
# Maquinari: servo P0 + brunzidor P2 (mascota, com coreografia.py) i
# motoreductors M1/M2 (vehicle, com velocitat_pwm.py).

from microbit import *
import music

pin0.set_analog_period(20)

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16


def graus_a_pwm(angle):
    return 26 + (angle * (128 - 26)) // 180


def mou_servo(angle):
    pin0.write_analog(graus_a_pwm(angle))


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


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def benvinguda(velocitat):
    # Nucli: primer la part de servo/so/display, despres un avanc breu.
    # Ampliacio 3: "velocitat" es parametre propi d'aquesta crida.
    display.show(Image.HAPPY)
    mou_servo(0)
    music.pitch(880, 150, pin=pin2)
    mou_servo(180)
    music.pitch(660, 150, pin=pin2)
    mou_servo(90)
    avancar(velocitat)
    sleep(600)
    aturar()


def comiat(velocitat):
    # Ampliacio 1: simetrica a benvinguda(), amb un recul en lloc d'avancar.
    display.show(Image.SAD)
    mou_servo(180)
    music.pitch(440, 200, pin=pin2)
    mou_servo(90)
    retrocedir(velocitat)
    sleep(600)
    aturar()


# --- Ampliacio 2: seguencia per botons, amb B aturant-ho tot sempre ---
PAS = 0

while True:
    if button_a.was_pressed():
        if PAS == 0:
            benvinguda(400)
            PAS = 1
        else:
            comiat(400)
            PAS = 0
    if button_b.was_pressed():
        aturar()
        display.show(Image.NO)
        PAS = 0
    sleep(20)
