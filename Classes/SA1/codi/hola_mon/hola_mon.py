# SA1 - hola_mon.py
# El primer programa: mostra un text i despres una imatge al display.
# Maquinari: nomes la micro:bit sola. No cal connectar res.

from microbit import *

display.scroll("HOLA")   # Mostra el text lletra a lletra, desplacant-se
sleep(500)                # Espera 500 ms (mig segon)
display.show(Image.HEART) # Mostra una imatge fixa: un cor
