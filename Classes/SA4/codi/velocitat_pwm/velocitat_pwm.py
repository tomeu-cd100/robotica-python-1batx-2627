# SA4 - velocitat_pwm.py  (funcions de moviment del vehicle, Sessio 2)
# Motoreductors del Kit 2 (canals M1/M2 del driver del Micro:shield): sentit
# de gir i velocitat amb PWM (write_analog). Aquests son els PINS DEFINITIUS
# del vehicle T2 (es fixen avui i ja no es tornen a tocar a T2 ni a T3,
# vegeu 00_Projecte_T2_Vehicle.md i 00_Projecte_T3_Rover.md).
# Cada motor porta DOS pins (un per sentit): per avancar s'envia PWM al pin
# "endavant" i 0 al pin "enrere"; per recular, al reves.
#   Motor esquerre (M1): pin13 (endavant) i pin14 (enrere)
#   Motor dret     (M2): pin15 (endavant) i pin16 (enrere)
# Veure SA4_esquemes_connexions.md pel cablatge complet (alimentacio externa
# per piles, MAI des de l'USB, quan els motors giren).
# NOTA: el simulador python.microbit.org NO simula els motoreductors.

from microbit import *

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16


def avancar(velocitat):
    # Funcio amb UN parametre (velocitat, 0-1023): els dos motors giren
    # endavant a la mateixa velocitat.
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def retrocedir(velocitat):
    # Mateixa idea que avancar(), pero enviant el PWM al pin "enrere".
    M1_ENRERE.write_analog(velocitat)
    M1_ENDAVANT.write_digital(0)
    M2_ENRERE.write_analog(velocitat)
    M2_ENDAVANT.write_digital(0)


def girar(costat):
    # Funcio amb UN parametre (costat, 'esquerra' o 'dreta'): gir sobre el
    # propi eix, un motor endavant i l'altre enrere a velocitat moderada.
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
    # Funcio SENSE parametres: velocitat 0 als quatre pins dels dos motors.
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


# --- ACTIVITAT NUCLI (Sessio 2): funcio AMB VALOR DE RETORN ---------------
# Calibratge de referencia: a VELOCITAT_REFERENCIA el vehicle avanca
# aproximadament CM_PER_SEGON centimetres cada segon (ajusta aquest valor
# al TEU vehicle cronometrant-lo). Escriu-la TU mateix abans de mirar-la:
# ha de RETORNAR (amb "return") els mil.lisegons que cal mantenir el motor
# engegat per recorrer unes certes distancies, NO moure res per si sola
# (com graus_a_pwm() a la SA4-S1).
CM_PER_SEGON = 20


def temps_per_recorregut(cm):
    # Funcio AMB VALOR DE RETORN: nomes calcula, no mou el vehicle.
    return int((cm / CM_PER_SEGON) * 1000)


# --- Demostracio: sentit de gir i velocitat amb les funcions de moviment ---
avancar(300)     # lent
sleep(1000)
avancar(1023)    # a tota velocitat
sleep(1000)
retrocedir(500)
sleep(1000)
girar('esquerra')
sleep(600)
girar('dreta')
sleep(600)
aturar()

# --- Us de temps_per_recorregut(cm): la funcio es CRIDA i el resultat ------
# --- s'USA per decidir quant dura l'avanc, en lloc d'un sleep() fix. -------
avancar(400)
sleep(temps_per_recorregut(30))   # avanca uns 30 cm i para
aturar()
