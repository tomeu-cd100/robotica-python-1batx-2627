# SA6 - registre_dades.py  (data logging natiu V2, Sessio 2)
# La micro:bit V2 pot desar dades ELLA MATEIXA a la seva memoria flash amb el
# modul "log", sense cap ordinador ni nuvol connectat mentre es registra.
# API real (MicroPython micro:bit V2):
#   import log
#   log.set_labels('temp', 'llum')   # noms de columna, un sol cop
#   log.add(temp=..., llum=...)      # una fila nova cada crida
# Per llegir-ho: connecta la placa per USB (com per programar-la) i, des de
# l'explorador de fitxers de l'ordinador, obre el fitxer MY_DATA.HTM que
# apareix dins la unitat MICROBIT: es un full HTML amb una taula i un grafic
# amb totes les files registrades (es pot obrir amb qualsevol navegador,
# sense instal·lar res mes).
# Maquinari: cap component nou, sensors interns (temperature(),
# read_light_level()).
# Simulador: python.microbit.org SIMULA el modul log (es pot descarregar el
# CSV/HTML de dades simulades des del propi simulador), pero les dades
# reals nomes es poden llegir per USB en una placa fisica.

from microbit import *
import log

log.set_labels('temp', 'llum')

INTERVAL_MS = 2000   # cada quant es desa una fila nova

while True:
    temp = temperature()
    llum = display.read_light_level()

    log.add(temp=temp, llum=llum)

    display.scroll(str(temp), delay=80, wait=False)
    sleep(INTERVAL_MS)
