# SA6 - vehicle_seguretat.py  (PRODUCTE del Projecte T2, es tanca a la Sessio 3)
# Programa INTEGRADOR: el vehicle deixa d'obeir ordres puntuals (SA5) i passa
# a un SISTEMA DE CONTROL amb MAQUINA D'ESTATS (RUN/STOP/ALERTA, esquelet de
# 00_Projecte_T2_Vehicle.md) i ATURADA D'EMERGENCIA PRIORITARIA: interromp
# QUALSEVOL moviment en curs, es dispari com es dispari (polsador a bord o
# comanda de radio dedicada "X"), sense excepcio.
# Reutilitza EXACTAMENT el mateix protocol de radio de la SA5
# (receptor_vehicle.py): prefix "CMD:" + ordres F/B/L/R/S. La comanda "X" es
# NOVA d'aquesta SA i te prioritat maxima (STOP d'emergencia per radio).
# Cablatge (definitiu del vehicle des de SA4, 00_Fil_conductor_construccions.md
# #1b): M1=P13/P14, M2=P15/P16, LED indicador=P1, polsador STOP=P12 (pull-up
# intern, prioritari). Rele/DHT11 (P2/P8) NOMES en el termostat_histeresi
# d'aquesta mateixa SA, no en aquest programa.
# Ampliacio (+, NO al nucli): aturada automatica per ultrasons (HC-SR04) com
# a variant de l'estat prioritari; vegeu SA6_fitxa_ampliada.md.
# Simulador: python.microbit.org NO simula motors ni el rele; nomes es pot
# provar la LOGICA de la maquina d'estats i del protocol de radio.

from microbit import *
import radio

GRUP = 1   # ha de coincidir amb el GRUP del comandament (SA5) de la parella

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

LED_ESTAT = pin1
POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)   # sense aixo la lectura flota
# amb pull-up intern: repos = 1, premut = 0 (LOW)

VELOCITAT = 400

RUN, STOP, ALERTA = range(3)   # ALERTA: reservat per a l'ampliacio (obstacle/temp)
estat = STOP


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


def actualitza_led():
    # LED indicador d'estat (esquema del vehicle): fix = RUN, apagat = STOP,
    # intermitent = ALERTA (nomes es fa servir si s'activa l'ampliacio).
    if estat == RUN:
        LED_ESTAT.write_digital(1)
    elif estat == STOP:
        LED_ESTAT.write_digital(0)
    else:
        LED_ESTAT.write_digital(1 if running_time() % 400 < 200 else 0)


def actualitza_estat(nou):
    # STOP SEMPRE guanya, es processi on es processi del bucle: aquesta
    # funcio es l'UNIC lloc que canvia "estat", perque cap altra part del
    # programa pugui "oblidar-se" d'aturar els motors en entrar a STOP.
    global estat
    if nou == STOP:
        aturar()
        display.show(Image.NO)
    estat = nou
    actualitza_led()


actualitza_estat(STOP)

while True:
    # 1a comprovacio de cada volta: el polsador d'emergencia, SEMPRE abans
    # de mirar cap altra cosa (prioritat maxima, com demana la fitxa 15).
    if not POLSADOR_STOP.read_digital():
        actualitza_estat(STOP)

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ordre = missatge[len(PREFIX):]
        if ordre == "X":
            # STOP d'emergencia per radio: mateixa prioritat que el
            # polsador fisic, per davant de qualsevol altra comanda.
            actualitza_estat(STOP)
        elif ordre == "S":
            actualitza_estat(STOP)
        elif estat == STOP and ordre in ("F", "B", "L", "R"):
            # Sortir de STOP nomes amb una ordre de moviment explicita.
            actualitza_estat(RUN)
        if estat == RUN:
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

    sleep(20)
