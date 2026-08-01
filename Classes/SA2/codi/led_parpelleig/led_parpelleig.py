# SA2 - led_parpelleig.py
# Sortida digital amb bucles: un LED extern parpelleja i comptem els cops.
# Maquinari: LED extern al pin P1 del Micro:shield (Kit 1). Veure
# SA2_esquemes_connexions.md per al cablatge complet.

from microbit import *

comptador = 0   # acumulador: quantes vegades ha parpellejat el LED

while True:
    pin1.write_digital(1)   # LED ences (sortida digital: nomes 0 o 1)
    sleep(500)
    pin1.write_digital(0)   # LED apagat
    sleep(500)

    comptador = comptador + 1   # un parpelleig mes

    if comptador % 10 == 0:
        # Cada 10 parpellejos, mostra el comptador al display.
        display.scroll(str(comptador))
