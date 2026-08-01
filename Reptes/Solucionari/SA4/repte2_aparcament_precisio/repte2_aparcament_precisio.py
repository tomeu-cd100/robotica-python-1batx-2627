# SA4 - Repte 2 (SOLUCIO): aparcament automatic de precisio
# Nucli + ampliacions 1-3: arrencada progressiva, funcio trajecte() que
# combina arrencada+avanc+frenada, i dues velocitats segons boto A o A+B.
# Maquinari: motoreductors M1 (pin13/pin14) i M2 (pin15/pin16), com a
# velocitat_pwm.py. Alimentacio externa (piles), mai per USB.

from microbit import *

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

PAS_PWM = 64   # salt de velocitat a cada iteracio de la rampa


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def arrencada(velocitat_final):
    # Ampliacio 1: puja la velocitat de mica en mica en lloc de saltar
    # directament al valor final.
    for v in range(0, velocitat_final + 1, PAS_PWM):
        avancar(v)
        sleep(30)


def frenada(velocitat_inicial):
    # Nucli: baixa la velocitat de mica en mica fins aturar-se del tot.
    for v in range(velocitat_inicial, -1, -PAS_PWM):
        avancar(v)
        sleep(30)
    aturar()


def trajecte(velocitat, temps_avancant):
    # Ampliacio 2: arrencada + avanc a velocitat constant + frenada.
    arrencada(velocitat)
    sleep(temps_avancant)
    frenada(velocitat)


while True:
    # Ampliacio 3: dues velocitats diferents segons quins botons es premen.
    if button_a.is_pressed() and button_b.is_pressed():
        trajecte(1023, 800)   # rapid
    elif button_a.was_pressed():
        trajecte(400, 800)    # lent
    sleep(20)
