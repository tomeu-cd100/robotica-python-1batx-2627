# SA3 - nivell_llum.py
# Entrada analogica: compara el sensor de llum INTERN de la micro:bit
# (display.read_light_level(), 0-255) amb el sensor de llum EXTERN del
# Kit 2 (analogic, 0-1023) i mapa la lectura a barres al display.
# Maquinari: sensor de llum extern del Kit 2 al pin P0 (ADC valid; P3/P4/P10
# tambe tenen ADC pero comparteixen circuit amb el display i no es poden
# llegir amb el display actiu, com aqui).
# Veure SA3_esquemes_connexions.md pel cablatge.

from microbit import *

LLINDAR_FOSCOR = 50   # 0-255: per sota d'aixo, l'entorn es "fosc"


def mapa(valor, entrada_min, entrada_max, sortida_min, sortida_max):
    # Passa un valor d'un rang d'entrada a un rang de sortida (regla de tres).
    # Exemple: mapa(512, 0, 1023, 0, 5) -> quantes barres (0-5) toca la meitat.
    rang_entrada = entrada_max - entrada_min
    rang_sortida = sortida_max - sortida_min
    proporcio = (valor - entrada_min) / rang_entrada
    return int(sortida_min + proporcio * rang_sortida)


def barres(n):
    # Dibuixa n columnes enceses (0-5) a la matriu, com un indicador de nivell.
    display.clear()
    for columna in range(min(n, 5)):
        for fila in range(5):
            display.set_pixel(columna, 4 - fila, 9)


while True:
    llum_interna = display.read_light_level()      # 0-255, sensor intern
    llum_externa = pin0.read_analog()               # 0-1023, sensor Kit 2

    n_barres = mapa(llum_externa, 0, 1023, 0, 5)
    barres(n_barres)

    if llum_interna < LLINDAR_FOSCOR:
        display.show(Image.ASLEEP, wait=False, loop=False, delay=200)
        sleep(400)

    sleep(200)
