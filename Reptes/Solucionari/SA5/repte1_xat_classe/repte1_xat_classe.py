# SA5 - Repte 1 (SOLUCIO): xat de classe amb identificacio
# Nucli + ampliacions 1-3: comptador de missatges rebuts, filtre per
# paraula a l'historial, i comanda especial "NETEJA" que buida l'historial.
# Maquinari: cap de nou, nomes la radio interna (com radio_missatges.py).

from microbit import *
import radio

GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

MEU_NOM = "A1"
historic = []
MAX_HISTORIC = 5
total_rebuts = 0   # ampliacio 1: comptador de missatges rebuts


def envia(text):
    radio.send(MEU_NOM + ":" + text)


def desa_al_historic(missatge):
    historic.append(missatge)
    if len(historic) > MAX_HISTORIC:
        historic.pop(0)


def mostra_historial():
    # Requisit minim: mostra tots els missatges de l'historial, un darrere
    # l'altre, separats per un espai.
    text = " ".join(historic)
    display.scroll(text)


def mostra_historial_amb_paraula(paraula):
    # Ampliacio 2: nomes mostra els missatges que continguin "paraula".
    filtrats = [m for m in historic if paraula in m]
    display.scroll(" ".join(filtrats))


while True:
    if button_a.was_pressed():
        envia("Hola")
        display.show(Image.YES)
        sleep(200)
        display.clear()
    if button_b.was_pressed():
        mostra_historial()
    if button_a.is_pressed() and button_b.is_pressed():
        # Ampliacio 1: mostra el total de missatges rebuts.
        display.scroll(str(total_rebuts))

    missatge_rebut = radio.receive()
    if missatge_rebut is not None:
        if missatge_rebut == "NETEJA":
            # Ampliacio 3: comanda especial que buida l'historial.
            historic.clear()
            display.show(Image.NO)
            sleep(150)
            display.clear()
        else:
            desa_al_historic(missatge_rebut)
            total_rebuts = total_rebuts + 1
            display.show(Image.HAPPY)
            sleep(150)
            display.clear()
    sleep(20)
