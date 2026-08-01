# SA1 - Repte 3 (SOLUCIO): dau doble sense repeticions
# Nucli + ampliacions 1-3: suma de dos daus, evitar repetir resultat, comptador.
# Maquinari: nomes la micro:bit sola (accelerometre intern).

from microbit import *
import random

ultim_resultat = 0   # Encara no hi ha cap tirada
tirades = 0           # Ampliacio 3: comptador de tirades


def tira_dos_daus():
    # Ampliacio 1: suma de dos daus (2-12).
    dau1 = random.randint(1, 6)
    dau2 = random.randint(1, 6)
    return dau1 + dau2


while True:
    if accelerometer.was_gesture("shake"):
        resultat = tira_dos_daus()
        # Ampliacio 2: si surt el mateix resultat que l'ultima vegada, torna a tirar.
        while resultat == ultim_resultat:
            resultat = tira_dos_daus()

        ultim_resultat = resultat
        tirades += 1

        display.scroll(str(resultat))   # scroll (no show) perque hi ha resultats de 2 xifres (10, 11, 12)
        sleep(200)
        display.clear()

    if pin_logo.is_touched():
        # Ampliacio 3: mostra el comptador de tirades sense interrompre el joc.
        display.scroll(str(tirades))
        display.clear()
