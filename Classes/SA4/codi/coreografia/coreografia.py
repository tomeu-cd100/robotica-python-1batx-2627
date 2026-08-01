# SA4 - coreografia.py  (funcions amb arguments, Sessio 1-2)
# Combina servo + so + display en petits "moviments" encapsulats en funcions
# amb parametres: una coreografia es nomes una LLISTA D'ORDRES a la funcio
# principal, sense repetir mai el detall de cada moviment.
# Maquinari: servo de la mascota (P0), brunzidor (P2, com a SA2/SA3).
# Veure SA4_esquemes_connexions.md.
# NOTA: el simulador NO simula el servo; el so i el display si es simulen.

from microbit import *
import music

pin0.set_analog_period(20)


def graus_a_pwm(angle):
    return 26 + (angle * (128 - 26)) // 180


def mou_servo(angle):
    pin0.write_analog(graus_a_pwm(angle))


def gest(angle_inici, angle_final, pas):
    # Funcio amb TRES parametres: un sol "moviment" reutilitzable per a
    # qualsevol combinacio d'angles i velocitat de pas.
    for angle in range(angle_inici, angle_final + pas, pas):
        mou_servo(angle)
        sleep(60)


def nota_curta(freq):
    # Funcio amb UN parametre: sona una nota concreta pel brunzidor extern
    # (pin= explicit, com mana la convencio del curs).
    music.pitch(freq, 150, pin=pin2)


def salut_musical(vegades):
    # Coreografia curta: combina gest() i nota_curta() "vegades" cops.
    for i in range(vegades):
        gest(90, 20, -10)
        nota_curta(880)
        gest(20, 90, 10)
        nota_curta(660)


def ball_complet():
    # Coreografia mes llarga: crida les funcions anteriors en un altre ordre.
    # Cap d'aquestes crides repeteix el detall del moviment: nomes l'ORDRE
    # en que es criden les funcions ja fetes canvia la coreografia sencera.
    display.show(Image.HAPPY)
    salut_musical(2)
    gest(90, 180, 15)
    nota_curta(523)
    gest(180, 0, -15)
    nota_curta(392)
    mou_servo(90)
    display.show(Image.HEART)


ball_complet()
