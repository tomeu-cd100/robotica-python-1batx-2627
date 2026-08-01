# SA6 - termostat_histeresi.py  (llac tancat amb histeresi, Sessio 1)
# Sistema de control de LLAC TANCAT: el sensor de temperatura (sortida)
# realimenta la decisio (entrada de control). NUCLI AVALUABLE: la histeresi,
# no el control proporcional.
# Sense histeresi, un termostat tot/res amb un unic llindar fa "clic-clic"
# sense parar quan la temperatura balla al voltant del llindar (contacte del
# rele desgastat en poc temps). Amb DOS llindars (baix i alt) nomes commuta
# quan la temperatura els travessa de veritat.
# Maquinari: temperature() interna de la micro:bit (Kit 2 en te un d'extern,
# pero aqui fem servir el sensor intern per no afegir cablatge nou) + rele al
# pin2 (Kit 3). Si no tens rele a ma, substitueix RELE per pin1 (LED): el
# comportament de la histeresi es identic, nomes canvia l'actuador.
# Simulador: python.microbit.org SIMULA temperature(), pero NO simula el
# rele/actuador extern -> nomes es pot provar la LOGICA (quan hauria
# d'encendre's o apagar-se), no l'efecte fisic.

from microbit import *

RELE = pin2

LLINDAR_BAIX = 24   # per sota d'aixo, activa (te fred)
LLINDAR_ALT = 26    # per sobre d'aixo, desactiva (ja no te fred)

actiu = False   # estat actual del rele (variable d'estat, no nomes la lectura)

RELE.write_digital(0)

while True:
    temp = temperature()

    if not actiu and temp < LLINDAR_BAIX:
        actiu = True
    elif actiu and temp > LLINDAR_ALT:
        actiu = False
    # Si temp esta ENTRE els dos llindars, NO es toca "actiu": aixo es la
    # histeresi. Un termostat sense histeresi nomes tindria un llindar i
    # canviaria d'estat cada volta que la lectura ballegés al seu voltant.

    RELE.write_digital(1 if actiu else 0)

    if actiu:
        display.show(Image.HEART)      # actuador engegat: "escalfant"
    else:
        display.show(Image.NO)         # actuador apagat

    sleep(500)
