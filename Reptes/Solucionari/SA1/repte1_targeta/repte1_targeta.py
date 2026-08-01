# SA1 - Repte 1 (SOLUCIO): targeta de benvinguda digital
# Nucli + ampliacions 1-3: segona imatge, repeticio amb while, imatge propia.
# Maquinari: nomes la micro:bit sola.

from microbit import *

NOM = "TOMEU"

# Imatge propia (ampliacio 3): una fletxa senzilla feta amb un patro de 5x5.
# Cada fila son 5 digits de 0 (apagat) a 9 (maxima brillantor), separades per ":".
FLETXA = Image("00900:09990:90909:00900:00900")

while True:
    # Ampliacio 2: repeteix el cicle nom -> imatges 3 vegades amb un while.
    for i in range(3):
        display.scroll(NOM)
        sleep(200)
        display.show(Image.HAPPY)     # Ampliacio 1: primera imatge
        sleep(600)
        display.show(FLETXA)          # Ampliacio 3: imatge propia
        sleep(600)
    sleep(2000)   # Pausa llarga abans de tornar a comencar el cicle sencer
