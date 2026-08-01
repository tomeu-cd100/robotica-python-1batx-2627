# SA4 - control_per_botons.py  (PRODUCTE de la SA4, Sessio 3)
# Repte "control per botons": seqüencia de moviments encadenada amb les
# funcions propies de moviment (avancar/retrocedir/girar/aturar, com a
# velocitat_pwm.py), activada amb els botons A/B. Es la base del futur
# control remot per radio (SA5-SA6).
# Cablatge: els mateixos pins definitius del vehicle (M1/M2), vegeu
# SA4_esquemes_connexions.md i 00_Projecte_T2_Vehicle.md.
# NOTA: el simulador NO simula els motoreductors; prova la LOGICA de la
# seqüencia substituint temporalment cada funcio per un display.scroll().

from microbit import *

M1_ENDAVANT = pin8
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

VELOCITAT = 400


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


# --- Seqüencia propia: el boto A avança un pas cada cop que es prem; ---
# --- el boto B atura sempre, es processi on es processi el moviment.  ---
PAS = 0


def seguent_moviment():
    global PAS
    if PAS == 0:
        display.show(Image.ARROW_N)
        avancar(VELOCITAT)
    elif PAS == 1:
        display.show(Image.ARROW_W)
        girar('esquerra')
    elif PAS == 2:
        display.show(Image.ARROW_S)
        retrocedir(VELOCITAT)
    elif PAS == 3:
        display.show(Image.ARROW_E)
        girar('dreta')
    PAS = (PAS + 1) % 4


aturar()
display.show(Image.NO)

while True:
    if button_a.was_pressed():
        seguent_moviment()
    if button_b.was_pressed():
        aturar()
        display.show(Image.NO)
        PAS = 0
    sleep(20)
