# Prova practica T3 - ITEM NOU (obligatori, 2 punts) - SOLUCIO ORIENTATIVA
# (docent, NO es lliura). Comportament NOU del rover, NO treballat a cap
# sessio del curs: "aparca quan detecta la linia DUES vegades seguides".
# Es redacta a la TAULA (mateix bloc horari que la Part B): no necessita
# temps addicional de pista de la rotacio continua. Es valora la logica i
# l'estructura de la funcio (parametre + retorn); si toca torn de pista
# abans d'acabar la sessio es pot provar amb el rover real, pero no cal
# per obtenir la puntuacio.
# Cablatge (00_Fil_conductor_construccions.md #1b, rover T3, igual que
# prova_t3_rover.py): M1=P13/P14, M2=P15/P16, seguidor de linia=P0.
# Simulador: aquest comportament necessita el rover real (motors i sensor
# de linia no es simulen); la funcio cal_aparcar() si es pot provar sola
# al REPL amb valors enters (0, 1, 2...).

from microbit import *

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16
SEGUIDOR_LINIA = pin0

VELOCITAT_AVANCAR = 400
LLINDAR_LINIA = 500


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def cal_aparcar(deteccions_consecutives):
    # FUNCIO NOVA (item obligatori): UN PARAMETRE i VALOR DE RETORN.
    # Comportament no vist a classe: cal aparcar quan la linia s'ha
    # detectat DUES vegades SEGUIDES (no nomes un cop, per evitar un fals
    # positiu d'un sol instant de lectura sorollosa).
    return deteccions_consecutives >= 2


deteccions = 0
aparcat = False

while not aparcat:
    lectura = SEGUIDOR_LINIA.read_analog()
    detecta_linia = lectura < LLINDAR_LINIA

    if detecta_linia:
        deteccions += 1
    else:
        deteccions = 0   # nomes compten deteccions SEGUIDES, sense talls

    if cal_aparcar(deteccions):
        aturar()
        display.show(Image.YES)
        aparcat = True
    else:
        avancar(VELOCITAT_AVANCAR)
        display.show(Image.ARROW_N)

    sleep(50)
