# SA6 - maquina_estats_semafor.py  (FSM autonoma, Sessio 1)
# Introdueix el concepte de MAQUINA D'ESTATS FINITS (FSM) abans d'aplicar-la
# al vehicle: una VARIABLE D'ESTAT (nomes pot valer una cosa de cada vegada)
# + TRANSICIONS clares d'un estat a un altre. Aquest programa NO depen del
# vehicle: es un semafor autonom, per practicar la idea abans de barrejar-la
# amb motors i radio.
# Maquinari: cap component nou, nomes el display de la micro:bit (cada
# estat es mostra amb una imatge/color diferent al display 5x5).
# Simulador: python.microbit.org simula el display sencer, es pot provar tot.

from microbit import *

VERD, GROC, VERMELL = range(3)

# Diccionari de transicions: estat actual -> (proxim estat, quant dura en ms)
# Alternativa valida a un if/elif encadenat; aqui es fa servir per mostrar
# que la FSM es pot representar com a DADES, no nomes com a codi.
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

NOMS = {VERD: "VERD", GROC: "GROC", VERMELL: "VERMELL"}

estat = VERMELL   # estat inicial (variable d'estat: nomes un valor possible)


def actualitza_estat(nou):
    # Funcio AMB UN PARAMETRE: centralitza el canvi d'estat en un unic lloc,
    # perque mostrar-lo (display) i registrar-lo (print) no es repeteixi
    # cada cop que el semafor canvia.
    global estat
    estat = nou
    display.show(IMATGES[estat])
    print("Semafor ->", NOMS[estat])


actualitza_estat(estat)

while True:
    proxim, durada = TRANSICIONS[estat]
    sleep(durada)
    actualitza_estat(proxim)
