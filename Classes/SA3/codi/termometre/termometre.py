# SA3 - termometre.py
# Entrada analogica: sensor de temperatura basic del Kit 1 (extern) comparat
# amb el sensor de temperatura INTERN de la micro:bit (temperature(), graus
# Celsius). Interpreta la temperatura amb if/elif/else i la mostra al display.
# Maquinari: sensor de temperatura basic del Kit 1 al pin P10 (ADC valid).
# Veure SA3_esquemes_connexions.md pel cablatge.

from microbit import *

FRED = 18       # graus C: per sota, "fred"
CALOR = 26      # graus C: per sobre, "calor"


def graus_del_sensor_extern(lectura_analogica):
    # Conversio orientativa lectura (0-1023) -> graus C per al sensor basic
    # del Kit 1 (calibra el pendent/offset reals amb el REPL i el full de
    # caracteristiques del component, vegeu SA3_esquemes_connexions.md).
    return mapa(lectura_analogica, 0, 1023, 0, 50)


def mapa(valor, entrada_min, entrada_max, sortida_min, sortida_max):
    rang_entrada = entrada_max - entrada_min
    rang_sortida = sortida_max - sortida_min
    proporcio = (valor - entrada_min) / rang_entrada
    return sortida_min + proporcio * rang_sortida


while True:
    temp_interna = temperature()                     # graus C, sensor intern
    temp_externa = graus_del_sensor_extern(pin10.read_analog())

    if temp_interna < FRED:
        display.show(Image.SAD)     # icona "fred"
    elif temp_interna > CALOR:
        display.show(Image.ANGRY)   # icona "calor"
    else:
        display.show(Image.HAPPY)   # temperatura agradable

    sleep(500)
