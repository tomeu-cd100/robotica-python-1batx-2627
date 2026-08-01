# SA9 - plantilla_projecte.py  (esquelet del repte final integrador)
# Aquest fitxer NO es un repte resolt: es la BASTIDA que fas servir per
# comencar el teu propi projecte. Segueix la mateixa arquitectura de tot
# el curs: PERCEP (llegeix sensors) -> DECIDEIX (FSM, com maquina_estats_
# semafor.py de SA6 i comportaments.py de SA8) -> ACTUA (mou motors o
# actuadors). Copia i enganxa aqui les funcions que ja tens fetes de
# SA1-SA8 (avancar/girar/aturar de SA4/SA7, mesura_distancia de SA3/SA7,
# radio.send/receive de SA5/SA8, etc.) i completa nomes els TODO.
# Cablatge: reutilitza el mapa de pins del rover (00_Fil_conductor_
# construccions.md #1b) i, si el teu repte hi afegeix maquinari nou
# (bomba+rele, PIR, tira NeoPixel...), fes-ho constar al teu esquema de
# connexions del dossier (SA9_dossier_plantilla.md), NO en aquest fitxer.

from microbit import *
import machine
import utime

# --- 1. PINS -----------------------------------------------------------
# TODO: declara aqui els pins heretats del rover (motors, HC-SR04,
# seguidor de linia, polsador STOP) i els pins NOUS que faci servir el
# teu repte (per exemple: rele de la bomba, sensor d'humitat del terra,
# sensor PIR...). Consulta els pins lliures al mapa de pins (#1b).
POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)   # pull-up, com a SA6-SA8

# --- 2. CONSTANTS DEL REPTE ---------------------------------------------
# TODO: llindars, velocitats, intervals de temps del TEU repte.
INTERVAL_MOSTREIG_MS = 500

# --- 3. ESTATS DE LA FSM -------------------------------------------------
# TODO: substitueix aquests noms pels estats reals del teu repte (per
# exemple, per al reg automatic: ESPERA, REGANT, REFRESCANT; per al
# sentinella: VIGILANT, ALERTA, RECUPERANT). Mateix patro que SA6-SA8:
# una unica variable d'estat, mai dues coses alhora.
ESTAT_A, ESTAT_B = range(2)
NOMS_ESTAT = {ESTAT_A: "A", ESTAT_B: "B"}

estat = ESTAT_A
ultim_mostreig = running_time()


def polsador_premut():
    # Prioritat maxima ABSOLUTA (per damunt de qualsevol estat de la FSM),
    # mateix patro que vehicle_seguretat.py (SA6) i rover_missions.py (SA7).
    return not POLSADOR_STOP.read_digital()


def actualitza_estat(nou):
    global estat
    estat = nou
    display.show(NOMS_ESTAT[estat][0])


# --- 4. PERCEP -----------------------------------------------------------
def percep():
    # TODO: llegeix aqui els sensors del teu repte i retorna'ls (per
    # exemple, un diccionari o una tupla). Reutilitza les funcions de
    # mesura ja provades (machine.time_pulse_us per a HC-SR04/DHT11,
    # read_analog() per a sensors analogics, i2c per a l'IMU/BMP280/CCS811).
    return {}


# --- 5. DECIDEIX (FSM) ---------------------------------------------------
def decideix(dades):
    # TODO: la teva maquina d'estats. Mateixa estructura que
    # maquina_estats_semafor.py (SA6) i comportaments.py (SA8): un
    # if/elif per estat, transicions clares, comentades.
    global estat
    if estat == ESTAT_A:
        pass  # TODO: condicio de transicio cap a ESTAT_B
    elif estat == ESTAT_B:
        pass  # TODO: condicio de transicio cap a ESTAT_A


# --- 6. ACTUA --------------------------------------------------------------
def actua():
    # TODO: activa aqui els actuadors del teu repte (motors, rele,
    # display, radio...) segons l'estat actual.
    pass


# --- 7. BUCLE PRINCIPAL -----------------------------------------------------
actualitza_estat(ESTAT_A)

while True:
    # 1a comprovacio de cada volta: el polsador d'emergencia, sempre
    # per damunt de la FSM (mateix patro que tot el curs des de SA6).
    if polsador_premut():
        display.show(Image.NO)
        sleep(20)
        continue

    ara = running_time()
    if ara - ultim_mostreig >= INTERVAL_MOSTREIG_MS:
        ultim_mostreig = ara
        dades = percep()
        decideix(dades)
        actua()

    sleep(20)
