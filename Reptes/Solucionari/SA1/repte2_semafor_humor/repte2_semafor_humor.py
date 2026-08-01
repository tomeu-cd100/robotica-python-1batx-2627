# SA1 - Repte 2 (SOLUCIO): semafor d'humor amb tres estats
# Nucli + ampliacions 1-3: estat A+B, comptador amb logo, funcions propies.
# Maquinari: nomes la micro:bit sola.

from microbit import *


def cara_contenta():
    display.show(Image.HAPPY)


def cara_trista():
    display.show(Image.SAD)


def cara_repos():
    display.show(Image.ASLEEP)


def cara_sorpresa():
    display.show(Image.SURPRISED)


while True:
    # Ampliacio 2: mostra el comptador de pulsacions del boto A en tocar el logo.
    if pin_logo.is_touched():
        display.scroll(str(button_a.get_presses()))
    # Ampliacio 1: estat A+B alhora, abans de mirar-los per separat.
    elif button_a.is_pressed() and button_b.is_pressed():
        cara_sorpresa()
    elif button_a.is_pressed():
        cara_contenta()
    elif button_b.is_pressed():
        cara_trista()
    else:
        cara_repos()
    sleep(100)
