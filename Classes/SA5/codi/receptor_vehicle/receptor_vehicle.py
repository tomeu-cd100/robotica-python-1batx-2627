# SA5 - receptor_vehicle.py  (PRODUCTE de la SA5, Sessio 3)
# Repte "control remot bassic": el vehicle T2 (muntat a la SA4) rep ordres
# per radio i les converteix en moviment, reutilitzant les MATEIXES funcions
# de moviment de velocitat_pwm.py/control_per_botons.py (SA4): nomes canvia
# l'ENTRADA (radio en lloc de botons). Ha d'anar aparellat, mateix GRUP i
# mateix protocol, amb la placa que porta comandament.py (banc de proves
# puntual amb un company; el codi que s'avalua es sempre el propi).
# Cablatge: pins DEFINITIUS del vehicle des de la SA4 (SA5_esquemes_connexions.md,
# 00_Fil_conductor_construccions.md #1b): M1=P13/P14, M2=P15/P16.

from microbit import *
import radio

GRUP = 1   # ha de coincidir amb el GRUP de comandament.py de la parella

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

VELOCITAT = 400

# Ampliacio (+): historic de comandes rebudes, com a llista de tuples
# (ordre, instant en ms). Es una introduccio a estructures de dades que la
# SA6 completara amb mes detall.
historic_comandes = []
MAX_HISTORIC = 10


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


def desa_al_historic(ordre):
    # Tupla (ordre, instant): una parella de valors que no es pot modificar
    # un cop creada, a diferencia d'una llista.
    historic_comandes.append((ordre, running_time()))
    if len(historic_comandes) > MAX_HISTORIC:
        historic_comandes.pop(0)


def actua(ordre):
    # Esdeveniment -> accio: relaciona cada ordre rebuda amb una funcio de
    # moviment ja creada a la SA4 (mateix esquema que els botons A/B, ara
    # amb una ordre de radio com a entrada).
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


aturar()
display.show(Image.NO)

while True:
    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ordre = missatge[len(PREFIX):]
        desa_al_historic(ordre)
        actua(ordre)
    sleep(20)
