# SA4 - funcions_moviments.py  (PRIMERES FUNCIONS del curs, Sessio 1)
# Ja has escrit funcions sense saber-ho (respira/mostra_color a la SA2,
# mapa/canvia_emocio a la SA3): avui poses NOM al concepte i n'aprens la
# sintaxi formal (def, parametres, valor de retorn) per moure el servo
# de la mascota amb ordres propies (saluda, escombra).
# Maquinari: micro servo de la mascota (Kit 2) al pin P0 (NOMES muntat des
# de la SA2, encara no programat fins avui). Veure SA4_esquemes_connexions.md.
# NOTA: el simulador python.microbit.org NO simula el servo (nomes es veu
# que el programa no peta, no que es mogui de veritat).

from microbit import *

pin0.set_analog_period(20)   # periode de 20 ms: el que espera un servo estandard


def graus_a_pwm(angle):
    # Converteix un angle (0-180 graus) al valor write_analog (26-128) que
    # enten el servo. Es una funcio AMB VALOR DE RETORN: no fa res visible,
    # nomes calcula i torna un numero (com mapa() a la SA3).
    return 26 + (angle * (128 - 26)) // 180


def mou_servo(angle):
    # Funcio AMB UN PARAMETRE (angle): mou el servo a la posicio demanada.
    # Reutilitza graus_a_pwm() en lloc de repetir el calcul cada cop.
    pin0.write_analog(graus_a_pwm(angle))


def saluda(vegades):
    # Funcio AMB UN PARAMETRE (vegades): repeteix el gest tantes vegades com
    # es demani. Abans de tenir funcions, hauries d'haver copiat aquest bloc
    # de 4 linies un cop per cada salutacio.
    for i in range(vegades):
        mou_servo(0)
        sleep(300)
        mou_servo(180)
        sleep(300)
    mou_servo(90)   # torna al centre en acabar


def escombra(angle_maxim):
    # Funcio AMB UN PARAMETRE (angle_maxim): escombra d'un costat a l'altre.
    # El MATEIX codi serveix per a un moviment curt (angle_maxim=60) o llarg
    # (angle_maxim=180) nomes canviant l'argument, sense reescriure res.
    for angle in range(0, angle_maxim + 1, 20):
        mou_servo(angle)
        sleep(80)
    for angle in range(angle_maxim, -1, -20):
        mou_servo(angle)
        sleep(80)


# --- Demostracio: la mateixa funcio, cridada amb arguments diferents ---
saluda(2)         # saluda 2 vegades
sleep(500)
escombra(60)       # escombrada curta
sleep(500)
escombra(180)      # escombrada llarga, MATEIXA funcio, MATEIX codi
