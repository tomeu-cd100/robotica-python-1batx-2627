# Prova practica T1 - SOLUCIO ORIENTATIVA (docent, NO es lliura a l'alumnat)
# Tema: "estacio personal d'alertes" amb la micro:bit sola (sense muntar la
# mascota: aquesta prova es individual i separada del producte, ja tancat a
# la Sessio 3 de SA3).
# NUCLI (satisfactori): botons A/B per triar mode amb is_pressed() (SA1-SA3;
# was_pressed() NO s'ensenya fins la SA4 i no es pot exigir al nucli) +
# sensors INTERNS de llum i temperatura amb condicionals if/elif/else +
# lectura continua pel REPL (print) per depurar abans de fixar els llindars.
# NOTA: canviar de mode amb is_pressed() no necessita antirebot perque
# l'assignacio es IDEMPOTENT (mentre el boto es manté premut, cada volta
# torna a fixar el MATEIX mode: no hi ha cap comptador ni commutacio que
# es pugui "disparar" de mes).
# Ampliacio (notable): sensor de llum EXTERN del Kit 2 (P3, ADC) comparat
# amb l'intern (entrada analogica basica, mapa() de la SA3).
# Ampliacio (excel-lent): accelerometre (sacsejada) per confirmar l'alerta
# i microfon intern per detectar un soroll fort com a via addicional
# d'alerta; codi organitzat amb funcions (una responsabilitat per funcio).
# Maquinari: micro:bit V2 + Micro:shield; sensor de llum extern Kit 2 a P3
# (vegeu SA3_esquemes_connexions.md #2). Cap altre cablatge necessari: la
# resta son sensors interns.

from microbit import *
import music

LLINDAR_FOSCOR = 50        # 0-255, display.read_light_level() (calibra amb REPL)
LLINDAR_FRED = 18          # graus C, temperature()
LLINDAR_CALOR = 26         # graus C, temperature()
LLINDAR_SO = 150           # nivell del microfon intern (calibra amb REPL)

MODE_LLUM, MODE_TEMP = range(2)
mode = MODE_LLUM


def mapa(valor, entrada_min, entrada_max, sortida_min, sortida_max):
    # Mateixa funcio que nivell_llum.py/termometre.py (SA3): passa un valor
    # d'un rang d'entrada a un rang de sortida amb una regla de tres.
    rang_entrada = entrada_max - entrada_min
    rang_sortida = sortida_max - sortida_min
    proporcio = (valor - entrada_min) / rang_entrada
    return sortida_min + proporcio * rang_sortida


def mostra_mode():
    display.show(Image.ARROW_W if mode == MODE_LLUM else Image.ARROW_E)
    sleep(300)


def avalua_llum():
    # NUCLI: llum interna amb condicional + lectura pel REPL.
    intern = display.read_light_level()             # 0-255
    extern = pin3.read_analog()                      # 0-1023, sensor Kit 2
    extern_equivalent = mapa(extern, 0, 1023, 0, 255)
    print("llum intern:", intern, "extern (0-255):", round(extern_equivalent))

    if intern < LLINDAR_FOSCOR:
        display.show(Image.ASLEEP, wait=False, loop=False, delay=200)
    else:
        display.show(Image.SURPRISED, wait=False, loop=False, delay=200)
    sleep(400)


def avalua_temperatura():
    # NUCLI: temperatura interna amb if/elif/else + lectura pel REPL.
    temp = temperature()
    print("temperatura:", temp)

    if temp < LLINDAR_FRED:
        display.show(Image.SAD)
    elif temp > LLINDAR_CALOR:
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)


def comprova_alertes_ampliacio():
    # AMPLIACIO (excel-lent): dues vies mes d'alerta, cadascuna en la seva
    # propia funcio perque es puguin provar (i depurar) per separat.
    if accelerometer.was_gesture('shake'):
        display.show(Image.YES)   # sacsejada: confirma que l'alumne l'ha vist
        sleep(300)
    if microphone.sound_level() > LLINDAR_SO:
        music.pitch(1500, 100)    # so fort: avis agut i curt


while True:
    # NUCLI: is_pressed() (SA1-SA3), no was_pressed() (SA4). Idempotent:
    # mentre el boto es manté premut, es torna a fixar el mateix mode.
    if button_a.is_pressed():
        mode = MODE_LLUM
    if button_b.is_pressed():
        mode = MODE_TEMP
    mostra_mode()

    if mode == MODE_LLUM:
        avalua_llum()
    else:
        avalua_temperatura()

    comprova_alertes_ampliacio()
    sleep(200)
