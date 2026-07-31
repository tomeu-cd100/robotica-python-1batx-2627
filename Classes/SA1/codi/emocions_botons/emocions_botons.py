# SA1 - emocions_botons.py
# Els botons A i B canvien la cara que es mostra al display.
# Maquinari: nomes la micro:bit sola. No cal connectar res.

from microbit import *

while True:
    # while True: es repeteix per sempre, comprovant els botons continuament.
    if button_a.is_pressed():
        display.show(Image.HAPPY)   # Botó A premut -> cara contenta
    elif button_b.is_pressed():
        display.show(Image.SAD)     # Botó B premut -> cara trista
    else:
        display.show(Image.ASLEEP)  # Cap botó premut -> cara "en repos"
    sleep(100)                      # Petita pausa abans de tornar a mirar
