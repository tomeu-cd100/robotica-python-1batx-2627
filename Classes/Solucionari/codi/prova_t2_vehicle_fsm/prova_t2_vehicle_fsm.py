# Prova practica T2 - PART A - SOLUCIO ORIENTATIVA (docent, NO es lliura)
# NUCLI (satisfactori): maquina d'estats RUN/STOP controlada per ordres de
# radio amb el protocol "CMD:" (F/B/L/R/S), reutilitzant EXACTAMENT les
# funcions de moviment de la SA4/SA5 (avancar/retrocedir/girar/aturar).
# Ampliacio (notable): polsador STOP (P12, pull-up) amb prioritat maxima,
# comprovat SEMPRE abans que la radio a cada volta del bucle (mateix patro
# que vehicle_seguretat.py, SA6).
# Ampliacio (excel-lent): LED indicador d'estat (P1): ences fix = RUN,
# apagat = STOP.
# Cablatge (00_Fil_conductor_construccions.md #1b, vehicle T2): M1=P13/P14,
# M2=P15/P16, LED indicador=P1, polsador STOP=P12 (pull-up intern).
# Simulador: python.microbit.org NO simula els motors; nomes es pot provar
# la LOGICA de la maquina d'estats i del protocol de radio (dues pestanyes).

from microbit import *
import radio

GRUP = 1   # ha de coincidir amb el GRUP de la placa que envia les ordres

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

LED_ESTAT = pin1
POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)   # repos = 1, premut = 0

VELOCITAT = 400

RUN, STOP = range(2)
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


def girar(costat, velocitat=300):
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat)
        M1_ENDAVANT.write_digital(0)
        M2_ENDAVANT.write_analog(velocitat)
        M2_ENRERE.write_digital(0)
    elif costat == 'dreta':
        M1_ENDAVANT.write_analog(velocitat)
        M1_ENRERE.write_digital(0)
        M2_ENRERE.write_analog(velocitat)
        M2_ENDAVANT.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def actualitza_led():
    # AMPLIACIO (excel-lent): un unic lloc que reflecteix l'estat al LED.
    LED_ESTAT.write_digital(1 if estat == RUN else 0)


def actualitza_estat(nou):
    # UNIC lloc que canvia "estat": perque cap altra part del programa
    # pugui "oblidar-se" d'aturar els motors en entrar a STOP.
    global estat
    if nou == STOP:
        aturar()
        display.show(Image.NO)
    estat = nou
    actualitza_led()


actualitza_estat(STOP)

while True:
    # AMPLIACIO (notable): prioritat maxima, comprovada SEMPRE la primera.
    if not POLSADOR_STOP.read_digital():
        actualitza_estat(STOP)

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ordre = missatge[len(PREFIX):]
        if ordre == "S":
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
