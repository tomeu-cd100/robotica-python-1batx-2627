# SA5 - comandament.py  (protocol de comandes, Sessio 2)
# Una micro:bit fa de COMANDAMENT: envia ordres per radio amb un protocol
# propi de text pla amb prefix ("CMD:ordre"), amb botons A/B/A+B i un gest
# (sacsejada) com a STOP d'emergencia. La placa RECEPTORA es programa a
# receptor_vehicle.py (mateix GRUP i mateix protocol).
# Prefix "CMD:" -> introdueix la idea de PROTOCOL: la placa receptora nomes
# actua si el missatge comenca exactament per aquest prefix, per no
# confondre'l amb un xat com el de radio_missatges.py.

from microbit import *
import radio

GRUP = 1   # ha de coincidir amb el GRUP de receptor_vehicle.py de la parella

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"


def envia_ordre(ordre):
    # Funcio AMB UN PARAMETRE: envia sempre el mateix prefix, nomes canvia
    # la lletra de l'ordre (F/B/L/R/S).
    radio.send(PREFIX + ordre)
    display.show(ordre)
    sleep(150)
    display.clear()


while True:
    if button_a.is_pressed() and button_b.is_pressed():
        envia_ordre("S")            # A+B: atura (prioritat maxima)
    elif button_a.was_pressed():
        envia_ordre("F")            # A sol: avant
    elif button_b.was_pressed():
        envia_ordre("B")            # B sol: enrere
    if accelerometer.was_gesture("left"):
        envia_ordre("L")            # gest: gira a l'esquerra
    if accelerometer.was_gesture("right"):
        envia_ordre("R")            # gest: gira a la dreta
    if accelerometer.was_gesture("shake"):
        envia_ordre("S")            # gest: sacsejada = atura d'emergencia
    sleep(20)
