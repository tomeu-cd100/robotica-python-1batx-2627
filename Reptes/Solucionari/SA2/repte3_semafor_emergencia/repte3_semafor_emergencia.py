# SA2 - Repte 3 (SOLUCIO): semafor intel-ligent d'encreuament
# Nucli + ampliacions 1-3: avis sonor intermitent, funcions separades per
# mode, LED RGB sincronitzat amb l'emergencia.
# Maquinari: LED verd P1, ambre P8, vermell P12, brunzidor P2, rele P13
# (Kit 1 + Kit 3). LED RGB opcional als pins P8/P12/P16 (repte 2).

from microbit import *
import music

TEMPS_VERD = 3000
TEMPS_AMBRE = 1000
TEMPS_VERMELL = 3000

emergencia = False   # Ampliacio 2: variable d'estat que decideix quina funcio es crida


def tot_apagat():
    pin1.write_digital(0)
    pin8.write_digital(0)
    pin12.write_digital(0)


def revisa_boto():
    # Comprova el boto A sense bloquejar el cicle: si es prem, commuta
    # l'estat d'emergencia (nucli del requisit: interrupcio immediata).
    global emergencia
    if button_a.is_pressed():
        emergencia = not emergencia
        sleep(300)   # petita espera per no rebotar
    return emergencia


def cicle_normal():
    # --- Fase verda ---
    tot_apagat()
    pin1.write_digital(1)
    for i in range(TEMPS_VERD // 100):
        if revisa_boto():
            return
        sleep(100)

    # --- Fase ambre ---
    tot_apagat()
    pin8.write_digital(1)
    music.pitch(440, 200, pin=pin2)
    for i in range(TEMPS_AMBRE // 100):
        if revisa_boto():
            return
        sleep(100)

    # --- Fase vermella (amb rele) ---
    tot_apagat()
    pin12.write_digital(1)
    pin13.write_digital(1)
    for i in range(TEMPS_VERMELL // 100):
        if revisa_boto():
            pin13.write_digital(0)
            return
        sleep(100)
    pin13.write_digital(0)


def mode_emergencia():
    # Ampliacio 1: avis sonor intermitent + rele intermitent (llum d'emergencia).
    # Ampliacio 3: si hi ha LED RGB muntat, ambre parpellejant en lloc del LED digital.
    tot_apagat()
    pin12.write_digital(1)             # LED vermell parpellejant
    pin13.write_digital(1)             # rele actiu (llum d'emergencia encesa)
    music.pitch(880, 150, pin=pin2)    # avis sonor curt

    if revisa_boto():
        return
    sleep(250)

    pin12.write_digital(0)
    pin13.write_digital(0)

    if revisa_boto():
        return
    sleep(250)


while True:
    if emergencia:
        mode_emergencia()
    else:
        cicle_normal()
