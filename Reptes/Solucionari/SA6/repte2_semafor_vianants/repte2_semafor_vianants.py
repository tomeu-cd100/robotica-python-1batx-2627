# SA6 - Repte 2 (SOLUCIO): semafor de vianants amb boto prioritari
# Nucli + ampliacions 1-3: icona de sol.licitud pendent, boto que nomes
# "compta" durant el VERD, i un segon semafor (vianants) sempre en l'estat
# contrari al de vehicles, sense duplicar la logica de transicions.
# Maquinari: cap de nou, nomes el display i el boto A de la micro:bit.

from microbit import *

VERD, GROC, VERMELL = range(3)

TRANSICIONS = {
    VERD: (GROC, 3000),
    GROC: (VERMELL, 1000),
    VERMELL: (VERD, 3000),
}

IMATGES = {
    VERD: Image.SQUARE,
    GROC: Image.DIAMOND,
    VERMELL: Image.SQUARE_SMALL,
}

estat = VERMELL
sollicitud_pendent = False   # ampliacio 1: boto premut, esperant efecte


def semafor_vianants(estat_vehicles):
    # Ampliacio 3: el semafor de vianants es SEMPRE el contrari del de
    # vehicles, sense cap variable d'estat propia (es dedueix, no es guarda).
    return VERMELL if estat_vehicles != VERMELL else VERD


def actualitza_estat(nou):
    global estat
    estat = nou
    display.show(IMATGES[estat])
    print("Vehicles ->", estat, " Vianants ->", semafor_vianants(estat))


actualitza_estat(estat)
temps_restant = TRANSICIONS[estat][1]

while True:
    # Ampliacio 2: el boto nomes "compta" durant el VERD.
    if button_a.was_pressed() and estat == VERD:
        sollicitud_pendent = True

    pas = 100
    sleep(pas)
    temps_restant -= pas

    if sollicitud_pendent and estat == VERD:
        # Ampliacio 1 + requisit minim: escurca el VERD a un maxim d'1s.
        temps_restant = min(temps_restant, 1000)
        display.show(Image.SQUARE)   # icona de sol.licitud (aqui, el propi verd)

    if temps_restant <= 0:
        proxim, durada = TRANSICIONS[estat]
        actualitza_estat(proxim)
        temps_restant = durada
        if estat != VERD:
            sollicitud_pendent = False
