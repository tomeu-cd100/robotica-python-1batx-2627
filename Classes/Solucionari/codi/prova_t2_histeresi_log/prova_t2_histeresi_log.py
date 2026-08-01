# Prova practica T2 - PART B - SOLUCIO ORIENTATIVA (docent, NO es lliura)
# NUCLI (satisfactori): control tot/res AMB HISTERESI (dos llindars) sobre
# la temperatura interna, exactament el mateix patro que
# termostat_histeresi.py (SA6): un unic llindar faria "clic-clic" quan la
# lectura balla al voltant seu.
# Ampliacio (notable/excel-lent): registre de les lectures amb el modul
# "log" natiu de la V2 (igual que registre_dades.py, SA6), per documentar
# el quadern amb dades reals sense cap ordinador connectat mentre es grava.
# Maquinari: temperature() interna (cap cablatge nou); rele/LED d'ampliacio
# al pin2 (00_Fil_conductor_construccions.md #1b: rele = P2 al vehicle T2).
# Simulador: python.microbit.org simula temperature() i el modul log, pero
# NO simula el rele/actuador extern: nomes se'n pot provar la logica.

from microbit import *
import log

ACTUADOR = pin2   # rele (o LED, si no hi ha rele a ma: mateix comportament)

LLINDAR_BAIX = 24   # per sota d'aixo, activa (te fred)
LLINDAR_ALT = 26     # per sobre d'aixo, desactiva (ja no te fred)

log.set_labels('temp', 'actiu')

actiu = False   # variable d'estat: no nomes la lectura instantania
ACTUADOR.write_digital(0)

while True:
    temp = temperature()

    if not actiu and temp < LLINDAR_BAIX:
        actiu = True
    elif actiu and temp > LLINDAR_ALT:
        actiu = False
    # Si temp esta ENTRE els dos llindars, NO es toca "actiu": aixo es la
    # histeresi (error tipic: un sol "if temp > LLINDAR" -> tot/res SENSE
    # histeresi, no assoliria el nucli sencer).

    ACTUADOR.write_digital(1 if actiu else 0)
    display.show(Image.HEART if actiu else Image.NO)

    log.add(temp=temp, actiu=int(actiu))

    sleep(500)
