# SA4 - Repte 1 (SOLUCIO): salutacio programable per a un aparador
# Nucli + ampliacions 1-3: tercer estil "doble", cara al display segons
# l'estil, i seleccio de l'estil amb el boto A per torns.
# Maquinari: servo de la mascota al pin P0 (Kit 2, com funcions_moviments.py).

from microbit import *

pin0.set_analog_period(20)

index_estil = 0   # ampliacio 3: comptador 0/1/2 que cicla els tres estils


def graus_a_pwm(angle):
    return 26 + (angle * (128 - 26)) // 180


def mou_servo(angle):
    pin0.write_analog(graus_a_pwm(angle))


def saluda(vegades):
    for i in range(vegades):
        mou_servo(0)
        sleep(300)
        mou_servo(180)
        sleep(300)
    mou_servo(90)


def escombra(angle_maxim):
    for angle in range(0, angle_maxim + 1, 20):
        mou_servo(angle)
        sleep(80)
    for angle in range(angle_maxim, -1, -20):
        mou_servo(angle)
        sleep(80)


def salutacio(estil, vegades):
    # Funcio amb DOS parametres: "estil" tria quin moviment fer, "vegades"
    # quantes vegades es repeteix.
    if estil == 'curt':
        display.show(Image.HAPPY)          # ampliacio 2: cara segons l'estil
        saluda(vegades)
    elif estil == 'llarg':
        display.show(Image.SURPRISED)
        escombra(180)
    elif estil == 'doble':
        # Ampliacio 1: tercer estil que combina els dos anteriors.
        display.show(Image.HEART)
        saluda(vegades)
        escombra(120)


while True:
    if button_a.was_pressed():
        # Ampliacio 3: cada premuda tria el seguent estil, segons el comptador.
        if index_estil == 0:
            estil_actual = 'curt'
        elif index_estil == 1:
            estil_actual = 'llarg'
        else:
            estil_actual = 'doble'
        salutacio(estil_actual, 2)
        index_estil = index_estil + 1
        if index_estil == 3:
            index_estil = 0   # torna a comencar el cicle
    sleep(20)
