# SA1 - dau_sacseig.py  (AMPLIACIO)
# Sacseja la placa i mostra un numero de dau (1-6) a l'atzar.
# Maquinari: nomes la micro:bit sola (usa l'accelerometre intern).

from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        # was_gesture() nomes retorna True UN COP per cada sacseig detectat.
        numero = random.randint(1, 6)   # Nombre enter a l'atzar, entre 1 i 6 (tots dos inclosos)
        display.show(str(numero))       # show() necessita un text, per aixo cal str(...)
        sleep(1000)                     # Deixa'l 1 segon a la vista
        display.clear()                 # Apaga el display, a punt per al seguent sacseig
