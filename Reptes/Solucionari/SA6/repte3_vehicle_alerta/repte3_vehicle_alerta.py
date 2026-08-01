# SA6 - Repte 3 (SOLUCIO): vehicle amb alerta per temperatura i registre de bord
# Nucli de vehicle_seguretat.py (protocol CMD/STOP prioritari intacte) +
# ampliacions 1-3: tercer estat ALERTA amb histeresi propia, registre amb
# log.add() de cada entrada/sortida d'ALERTA, comptador propi per REPL, i
# una comanda de radio "A" per provocar l'ALERTA manualment (proves).
# Maquinari: vehicle T2 (M1=P13/P14, M2=P15/P16), LED=P1, polsador=P12,
# temperature() interna per a l'ALERTA automatica.

from microbit import *
import radio
import log

GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

LED_ESTAT = pin1
POLSADOR_STOP = pin12

VELOCITAT = 400

RUN, STOP, ALERTA = range(3)
estat = STOP

LLINDAR_ALERTA_ALT = 30    # entra en ALERTA per sobre d'aixo
LLINDAR_ALERTA_BAIX = 27   # nomes pot tornar a RUN per sota d'aixo (histeresi)

log.set_labels('event', 'temp')
entrades_alerta = 0   # ampliacio 2: comptador propi, a mes del log


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
    if estat == RUN:
        LED_ESTAT.write_digital(1)
    elif estat == STOP:
        LED_ESTAT.write_digital(0)
    else:
        LED_ESTAT.write_digital(1 if running_time() % 400 < 200 else 0)


def actualitza_estat(nou):
    global estat, entrades_alerta
    if nou in (STOP, ALERTA):
        aturar()
        display.show(Image.NO if nou == STOP else Image.SAD)
    if nou == ALERTA and estat != ALERTA:
        entrades_alerta += 1
        log.add(event="entra_alerta", temp=temperature())
    elif estat == ALERTA and nou != ALERTA:
        log.add(event="surt_alerta", temp=temperature())
    estat = nou
    actualitza_led()


actualitza_estat(STOP)

while True:
    if not POLSADOR_STOP.read_digital():
        actualitza_estat(STOP)

    temp = temperature()
    if estat != STOP:
        if temp > LLINDAR_ALERTA_ALT:
            actualitza_estat(ALERTA)
        elif estat == ALERTA and temp < LLINDAR_ALERTA_BAIX:
            actualitza_estat(STOP)   # surt d'ALERTA, cal ordre nova per RUN

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ordre = missatge[len(PREFIX):]
        if ordre == "X":
            actualitza_estat(STOP)
        elif ordre == "A":
            # Ampliacio 3: provocar l'ALERTA manualment (proves de seguretat).
            actualitza_estat(ALERTA)
        elif ordre == "S":
            actualitza_estat(STOP)
        elif estat == STOP and ordre in ("F", "B", "L", "R"):
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

    if button_a.was_pressed() and button_b.was_pressed():
        print("Entrades en ALERTA aquesta sessio:", entrades_alerta)

    sleep(20)
