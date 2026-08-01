# SA7 - Repte 1 (SOLUCIO): carret de magatzem amb velocitat variable
# Nucli + ampliacions 1-3: icona segons la velocitat, comptador de
# correccions per REPL, i una zona intermedia de llindar amb velocitat
# encara mes reduida (aproximacio basica a un control mes suau).
# Maquinari: seguidor de linia KS0050 a P0, motors M1=P13/P14, M2=P15/P16.

from microbit import *

SEGUIDOR_LINIA = pin0

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

LLINDAR_LINIA = 500
MARGE_INTERMIG = 60   # ampliacio 3: zona "quasi al limit" al voltant del llindar

VELOCITAT_NORMAL = 400
VELOCITAT_CORRECCIO = 220     # requisit minim: mes lenta durant els girs
VELOCITAT_INTERMEDIA = 300    # ampliacio 3: zona intermedia

correccions = 0   # ampliacio 2: comptador de vegades que ha corregit


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def girar(costat, velocitat=300):
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat)
        M1_ENDAVANT.write_digital(0)
        M2_ENDAVANT.write_analog(velocitat)
        M2_ENRERE.write_digital(0)
    elif costat == 'dreta':
        M1_ENDAVANT.write_analog(velocitat)
        M1_ENRERE.write_digital(0)
        M2_ENRERE.write_analog(velocitat)
        M2_ENDAVANT.write_digital(0)


estava_corregint = False

while True:
    lectura = SEGUIDOR_LINIA.read_analog()

    if lectura < LLINDAR_LINIA - MARGE_INTERMIG:
        # Clarament sobre la linia: velocitat normal.
        avancar(VELOCITAT_NORMAL)
        display.show(Image.ARROW_N)
        estava_corregint = False
    elif lectura < LLINDAR_LINIA:
        # Ampliacio 3: zona intermedia, ni clarament linia ni clarament fons.
        avancar(VELOCITAT_INTERMEDIA)
        display.show(Image.CHESSBOARD)
        estava_corregint = False
    else:
        # Linia perduda: corregeix a velocitat reduida (requisit minim).
        if not estava_corregint:
            correccions += 1   # ampliacio 2: nomes compta l'inici de cada correccio
            estava_corregint = True
        girar('esquerra', VELOCITAT_CORRECCIO)
        display.show(Image.ARROW_W)

    if button_a.was_pressed() and button_b.was_pressed():
        print("Correccions de rumb aquesta sessio:", correccions)

    sleep(20)
