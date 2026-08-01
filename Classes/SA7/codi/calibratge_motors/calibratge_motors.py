# SA7 - calibratge_motors.py  (el rover va recte, Sessio 1)
# Cinematica diferencial: el rover gira variant la velocitat/sentit relatiu
# de cada roda. Aquest programa reutilitza EXACTAMENT les funcions de
# moviment de la SA4 (avancar/retrocedir/girar/aturar, mateixos pins), pero
# hi afegeix la COMPENSACIO per motor: cap parell de motoreductors surt
# identic de fabrica, i sense compensar, el rover "es desvia" en avancar
# recte encara que els dos rebin la mateixa consigna de PWM.
# Maquinari: motoreductors del vehicle T2, ja cablejats (no es toquen).
#   Motor esquerre (M1): pin13 (endavant) i pin14 (enrere)
#   Motor dret     (M2): pin15 (endavant) i pin16 (enrere)
# Veure 00_Projecte_T3_Rover.md i SA7_esquemes_connexions.md pel cablatge.
# NOTA: el simulador python.microbit.org NO simula els motoreductors.

from microbit import *

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

# Factors de calibratge (0.0-1.0): ajusta'ls tu mateix provant el rover en
# una superficie plana. Si el rover es desvia cap a la dreta, el motor
# esquerre (M1) va relativament mes fort: baixa FACTOR_M1 (o puja FACTOR_M2).
FACTOR_M1 = 1.0   # motor esquerre
FACTOR_M2 = 0.92  # motor dret (exemple: compensa un motor una mica mes fluix)


def avancar_calibrat(velocitat):
    # Mateixa idea que avancar() de la SA4, pero cada motor rep la seva
    # propia velocitat compensada, no la mateixa consigna crua.
    M1_ENDAVANT.write_analog(int(velocitat * FACTOR_M1))
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(int(velocitat * FACTOR_M2))
    M2_ENRERE.write_digital(0)


def retrocedir_calibrat(velocitat):
    M1_ENRERE.write_analog(int(velocitat * FACTOR_M1))
    M1_ENDAVANT.write_digital(0)
    M2_ENRERE.write_analog(int(velocitat * FACTOR_M2))
    M2_ENDAVANT.write_digital(0)


def girar(costat):
    # Gir sobre el propi eix: un motor endavant i l'altre enrere. El gir NO
    # es calibra (la simetria del gir ja compensa prou per a proves curtes).
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


# --- Prova de calibratge: avanca 2 segons en linia recta i atura't ---
# Marca amb cinta el punt de sortida i el d'arribada: si el rover es desvia,
# ajusta FACTOR_M1/FACTOR_M2 (redueix el del costat que "guanya") i torna a
# provar fins que la trajectoria quedi prou recta.
avancar_calibrat(500)
sleep(2000)
aturar()
