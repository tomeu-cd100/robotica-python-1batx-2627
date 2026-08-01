# SA5 - Repte 2 (SOLUCIO, costat RECEPTOR): interpreta la comanda de
# velocitat de l'ampliacio 1 ("CMD:V3", "CMD:V5"...) i ajusta la variable
# VELOCITAT en lloc d'un valor fix, com demana Reptes_SA5.md.
# Parteix de receptor_vehicle.py (SA5, Sessio 3) i hi afegeix NOMES la
# interpretacio de les ordres que comencen per "V".
# Maquinari: vehicle T2 (M1=pin13/pin14, M2=pin15/pin16), com a
# receptor_vehicle.py. Es fa servir aparellat amb
# repte2_comandament_gestos.py (mateix GRUP i mateix PREFIX).

from microbit import *
import radio

GRUP = 1   # ha de coincidir amb el GRUP de repte2_comandament_gestos.py

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

VELOCITAT = 400   # ja no es una constant fixa: l'ordre "Vn" la pot canviar


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def retrocedir(velocitat):
    M1_ENRERE.write_analog(velocitat)
    M1_ENDAVANT.write_digital(0)
    M2_ENRERE.write_analog(velocitat)
    M2_ENDAVANT.write_digital(0)


def girar(costat):
    velocitat_gir = 300
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat_gir)
        M1_ENDAVANT.write_digital(0)
        M2_ENDAVANT.write_analog(velocitat_gir)
        M2_ENRERE.write_digital(0)
    elif costat == 'dreta':
        M1_ENDAVANT.write_analog(velocitat_gir)
        M1_ENRERE.write_digital(0)
        M2_ENRERE.write_analog(velocitat_gir)
        M2_ENDAVANT.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def canvia_velocitat(ordre):
    # Ampliacio 1: "V3" -> VELOCITAT = 3*100 = 300, "V5" -> 500, etc.
    # Nomes es crida si ordre comenca per "V" i la resta son digits.
    global VELOCITAT
    xifra = ordre[1:]
    if xifra.isdigit():
        VELOCITAT = int(xifra) * 100
        display.show(Image.ARROW_N)
        sleep(100)
        display.clear()


def actua(ordre):
    # Esdeveniment -> accio: igual que receptor_vehicle.py, pero ara "V..."
    # no mou el vehicle, nomes en canvia la velocitat de les properes ordres.
    if ordre == "F":
        display.show(Image.ARROW_N)
        avancar(VELOCITAT)
    elif ordre == "B":
        display.show(Image.ARROW_S)
        retrocedir(VELOCITAT)
    elif ordre == "L":
        display.show(Image.ARROW_W)
        girar('esquerra')
    elif ordre == "R":
        display.show(Image.ARROW_E)
        girar('dreta')
    elif ordre == "S":
        display.show(Image.NO)
        aturar()
    elif ordre.startswith("V"):
        canvia_velocitat(ordre)


aturar()
display.show(Image.NO)

while True:
    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ordre = missatge[len(PREFIX):]
        actua(ordre)
    sleep(20)
