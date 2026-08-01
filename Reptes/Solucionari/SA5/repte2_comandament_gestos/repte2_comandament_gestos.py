# SA5 - Repte 2 (SOLUCIO): comandament amb gestos per a un joc
# Nucli + ampliacions 1-3: comandes nomes amb gestos (left/right/shake),
# comanda de velocitat variable ("CMD:V3"), control de repeticio amb pausa,
# i confirmacio visual local de la darrera comanda enviada.
# Maquinari: cap de nou, nomes la radio interna (com comandament.py).

from microbit import *
import radio

GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"
darrera_ordre = ""   # ampliacio 3: confirmacio visual local


def envia_ordre(ordre):
    global darrera_ordre
    radio.send(PREFIX + ordre)
    darrera_ordre = ordre
    display.show(ordre)
    sleep(150)
    display.clear()


while True:
    # Requisit minim: nomes gestos, cap boto.
    if accelerometer.was_gesture("left"):
        envia_ordre("L")
        sleep(300)   # ampliacio 2: pausa per evitar enviaments descontrolats
    if accelerometer.was_gesture("right"):
        envia_ordre("R")
        sleep(300)
    if accelerometer.was_gesture("shake"):
        envia_ordre("S")
        sleep(300)
    if accelerometer.was_gesture("face up"):
        envia_ordre("V5")   # ampliacio 1: velocitat alta
        sleep(300)
    if accelerometer.was_gesture("face down"):
        envia_ordre("V2")   # ampliacio 1: velocitat baixa
        sleep(300)
    if button_a.was_pressed():
        # Ampliacio 3: mostra la darrera ordre enviada, sense tornar-la
        # a enviar.
        display.scroll(darrera_ordre)
    sleep(20)
