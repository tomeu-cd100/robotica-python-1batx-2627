# SA7 - segueix_linia.py  (comportament autonom, Sessio 2)
# Sensor seguidor de linia KS0050 (Kit 2) a P0 (analogic, ADC valid: P0/P1/
# P2/P3/P4/P10). Llegeix amb read_analog() (0-1023) i corregeix la
# trajectoria cap al costat on es perd la linia: es un LLAC TANCAT (llegeix
# -> decideix -> actua), el mateix cicle de la SA6 aplicat al moviment.
# Reutilitza les funcions de moviment de la SA4 (avancar/girar/aturar,
# mateixos pins de M1/M2). El LLINDAR cal calibrar-lo sobre el circuit real:
# el valor de "linia negra" i "fons blanc" varia amb la llum de l'aula.
# Maquinari: veure SA7_esquemes_connexions.md (seguidor de linia a P0).
# Simulador: python.microbit.org NO simula el seguidor de linia ni els
# motors; aquesta practica es fa NOMES amb maquinari real, sobre un circuit
# de linia a terra.

from microbit import *

SEGUIDOR_LINIA = pin0

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

# Llindar de deteccio: per SOTA es considera "linia" (negre), per SOBRE es
# considera "fons" (blanc). Calibra'l tu amb el REPL sobre el teu circuit
# (imprimeix SEGUIDOR_LINIA.read_analog() sobre la linia i fora d'ella).
LLINDAR_LINIA = 500

VELOCITAT_AVANCAR = 350
VELOCITAT_GIR = 300


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def girar(costat, velocitat):
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


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


while True:
    lectura = SEGUIDOR_LINIA.read_analog()

    if lectura < LLINDAR_LINIA:
        # El sensor encara veu la linia (negre): segueix recte.
        avancar(VELOCITAT_AVANCAR)
        display.show(Image.ARROW_N)
    else:
        # La linia s'ha perdut (fons blanc): gira cap a un costat fins que
        # el sensor la torni a trobar. Amb un unic sensor cal triar un
        # costat fix (aqui, esquerra) com a estrategia de recerca.
        girar('esquerra', VELOCITAT_GIR)
        display.show(Image.ARROW_W)

    sleep(20)
