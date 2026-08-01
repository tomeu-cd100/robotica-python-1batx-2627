# SA3 - Repte 3 (SOLUCIO): estacio meteorologica de butxaca
# Nucli + ampliacions 1-3: cinque resum propi, estabilitat de 2 s i
# avis de "rafega" amb el PIR.
# Maquinari: sensor de llum extern P3, sensor de temperatura extern P10
# (Kit 1/2); PIR al pin P8 (Kit 2) per a l'ampliacio 3.

from microbit import *

LLINDAR_CLAR = 500
FRED = 18
CALOR = 26
TEMPS_ESTABLE = 2000   # ms, ampliacio 2


def mapa(valor, entrada_min, entrada_max, sortida_min, sortida_max):
    rang_entrada = entrada_max - entrada_min
    rang_sortida = sortida_max - sortida_min
    proporcio = (valor - entrada_min) / rang_entrada
    return sortida_min + proporcio * rang_sortida


def resum(llum, temp):
    if temp < FRED:
        return "fred"
    if llum > LLINDAR_CLAR and temp > CALOR:
        return "sol"
    if llum <= LLINDAR_CLAR and FRED <= temp <= CALOR:
        return "ennuvolat"
    if llum > LLINDAR_CLAR and temp <= CALOR:
        return "clar"          # ampliacio 1: cinque resum propi
    return "variable"


def mostra_resum(nom):
    if nom == "sol":
        display.show(Image.HAPPY)
    elif nom == "fred":
        display.show(Image.SAD)
    elif nom == "ennuvolat":
        display.show(Image.MEH)
    elif nom == "clar":
        display.show(Image.CONFUSED)
    else:
        display.show(Image.SURPRISED)


resum_actual = None
resum_candidat = None
t_candidat = running_time()

while True:
    llum = pin3.read_analog()
    temp = mapa(pin10.read_analog(), 0, 1023, 0, 50)
    nou = resum(llum, temp)

    # Ampliacio 3: rafega detectada pel PIR, avis curt per sobre del resum.
    if pin8.read_digital() == 1:
        display.show(Image.TARGET)
        sleep(500)

    # Ampliacio 2: nomes canvia el resum si es mante estable 2 s seguits.
    if nou != resum_candidat:
        resum_candidat = nou
        t_candidat = running_time()
    elif running_time() - t_candidat > TEMPS_ESTABLE and nou != resum_actual:
        resum_actual = nou
        mostra_resum(resum_actual)

    sleep(200)
