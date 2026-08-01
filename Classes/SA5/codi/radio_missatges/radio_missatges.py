# SA5 - radio_missatges.py  (xat per radio, Sessio 1)
# Primer contacte amb el modul radio: enviar i rebre text curt entre dues
# plaques. Cada alumne porta el SEU propi programa a la SEVA propia placa;
# per provar-lo cal aparellar-se PUNTUALMENT amb la placa d'un company
# (grup de radio = numero de parella de la llista, vegeu SA5_guia_docent.md)
# nomes com a banc de proves, mai com a producte compartit.
# NOTA: el simulador python.microbit.org SI simula la radio, pero nomes
# entre instancies del simulador (no amb una placa fisica real).

from microbit import *
import radio

# GRUP: numero de la parella de la llista assignada pel docent (1-10 per a
# 20 alumnes). Canvia aquest numero pel grup que et toqui avui.
GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

MEU_NOM = "A1"          # identificatiu curt (per exemple, inicial+numero)
historic = []            # llista amb els darrers missatges rebuts
MAX_HISTORIC = 5          # xat "5x5": es guarden nomes els 5 darrers


def envia(text):
    # Un missatge de text pla amb el remitent al davant, per saber qui
    # l'ha enviat quan es rep.
    radio.send(MEU_NOM + ":" + text)


def desa_al_historic(missatge):
    # Funcio amb UN parametre: guarda el missatge nou i descarta el mes
    # antic si ja hi ha MAX_HISTORIC entrades (llista com a cua curta).
    historic.append(missatge)
    if len(historic) > MAX_HISTORIC:
        historic.pop(0)


def mostra_historic():
    # ACTIVITAT NUCLI (Sessio 1): un "for" que recorre els ELEMENTS de la
    # llista directament (for missatge in historic), no un index ni un
    # range(len(historic)). Mostra'ls TOTS, del mes antic al mes nou.
    for missatge in historic:
        display.scroll(missatge)


while True:
    if button_a.is_pressed() and button_b.is_pressed():
        mostra_historic()           # A+B: repassa TOT l'historic
    elif button_a.was_pressed():
        envia("Hola")
        display.show(Image.YES)
        sleep(200)
        display.clear()
    elif button_b.was_pressed():
        # Mostra el darrer missatge rebut, o una cara triste si encara no
        # n'ha arribat cap.
        if len(historic) > 0:
            display.scroll(historic[-1])
        else:
            display.show(Image.SAD)
    missatge_rebut = radio.receive()
    if missatge_rebut is not None:
        desa_al_historic(missatge_rebut)
        display.show(Image.HAPPY)
        sleep(150)
        display.clear()
    sleep(20)
