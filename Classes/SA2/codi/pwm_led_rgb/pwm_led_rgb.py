# SA2 - pwm_led_rgb.py
# Sortides PWM: efecte de "respiracio" en un LED i colors combinats en un
# LED RGB. Maquinari: LED al pin P1 (respiracio) i LED RGB als pins
# P8 (vermell), P12 (verd) i P16 (blau). Veure SA2_esquemes_connexions.md.

from microbit import *

# --- Part 1: efecte de respiracio amb un sol LED (PWM 0-1023) ---
def respira(pin, pujades):
    for i in range(pujades):
        for valor in range(0, 1024, 32):     # puja la intensitat de mica en mica
            pin.write_analog(valor)
            sleep(10)
        for valor in range(1023, -1, -32):   # i despres la baixa
            pin.write_analog(valor)
            sleep(10)


# --- Part 2: LED RGB, un color propi combinant els tres canals ---
def mostra_color(vermell, verd, blau):
    # Cada valor va de 0 (apagat) a 1023 (maxima intensitat d'aquell canal).
    pin8.write_analog(vermell)
    pin12.write_analog(verd)
    pin16.write_analog(blau)


while True:
    respira(pin1, 2)          # el LED de P1 "respira" dues vegades

    mostra_color(1023, 0, 0)  # vermell pur
    sleep(800)
    mostra_color(0, 1023, 0)  # verd pur
    sleep(800)
    mostra_color(0, 0, 1023)  # blau pur
    sleep(800)
    mostra_color(600, 0, 600) # color combinat: lila
    sleep(800)
    mostra_color(0, 0, 0)     # apaga el LED RGB
    sleep(500)
