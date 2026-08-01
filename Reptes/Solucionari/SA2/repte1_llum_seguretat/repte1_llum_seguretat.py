# SA2 - Repte 1 (SOLUCIO): llum de seguretat per a motxilla
# Nucli + ampliacions 1-3: comptador cada 5, mode "aparcada", funcions per mode.
# Maquinari: LED extern al pin P1 del Micro:shield (Kit 1).

from microbit import *

comptador = 0          # acumulador: quants parpellejos portem
MODE_APARCADA = False  # ampliacio 2: estat "fix" fins que es torna a premer un boto


def mode_normal():
    pin1.write_digital(1)
    sleep(500)
    pin1.write_digital(0)
    sleep(500)


def mode_alerta():
    # Ampliacio 3: parpelleig mes rapid que el normal.
    pin1.write_digital(1)
    sleep(120)
    pin1.write_digital(0)
    sleep(120)


def mode_aparcada():
    # Ampliacio 2: LED fix, sense parpellejar.
    pin1.write_digital(1)


while True:
    if button_b.is_pressed():
        MODE_APARCADA = not MODE_APARCADA   # commuta el mode amb cada pulsacio
        sleep(300)                          # petita espera per no rebotar

    if MODE_APARCADA:
        mode_aparcada()
    else:
        if button_a.is_pressed():
            mode_alerta()
        else:
            mode_normal()
        comptador = comptador + 1

        # Ampliacio 1: mostra el comptador cada 5 parpellejos (no cada 10).
        if comptador % 5 == 0:
            display.scroll(str(comptador))
