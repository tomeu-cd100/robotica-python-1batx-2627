# Prova practica T3 - PART B (taula) - SOLUCIO ORIENTATIVA (docent, NO es
# lliura). Programa de TAULA, sense rover: es fa amb la placa sola durant
# la primera part de la sessio (mentre la resta del grup fa la Part A per
# torns a la pista).
# NUCLI (satisfactori): telemetria per radio (prefix "TEL:", mateix format
# clau:valor separat per ";" que telemetria_radio.py/estacio_base.py, SA8).
# Ampliacio: integra la dada en una decisio -> accio: un boto envia una
# ordre "CMD:STOP" (protocol diferent del "TEL:", com exigeix la fitxa 17)
# que, en un rover real, aturaria els motors en rebre-la.
# Maquinari: cap component nou, nomes la radio interna i el display.
# Simulador: la radio SI es simula (dues pestanyes obertes alhora): es pot
# provar tot el protocol sense maquinari.

from microbit import *
import radio

GRUP = 10   # ha de coincidir amb el GRUP de la placa parella (banc de proves)

radio.on()
radio.config(group=GRUP)

PREFIX_TEL = "TEL:"
PREFIX_CMD = "CMD:"

LLINDAR_ALERTA = 28   # graus C
aturat = False

INTERVAL_MS = 2000
ultim_enviament = running_time()


def envia_lectura():
    # NUCLI: mesura i transmet una dada (telemetria) amb el prefix "TEL:".
    temp = temperature()
    alerta = "1" if temp > LLINDAR_ALERTA else "0"
    radio.send(PREFIX_TEL + "T:" + str(temp) + ";A:" + alerta)
    display.show(Image.NO if alerta == "1" else Image.YES)


while True:
    if button_a.was_pressed():
        # AMPLIACIO: una ordre per radio integrada en el comportament
        # (equivalent, en un rover real, a aturar els motors en rebre-la).
        radio.send(PREFIX_CMD + "STOP")

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX_CMD):
        ordre = missatge[len(PREFIX_CMD):]
        if ordre == "STOP":
            aturat = True
            display.show(Image.SKULL)

    if not aturat:
        ara = running_time()
        if ara - ultim_enviament >= INTERVAL_MS:
            ultim_enviament = ara
            envia_lectura()

    sleep(20)
