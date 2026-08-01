# SA8 - Repte 3 (SOLUCIO): missio telemetrada amb alerta d'emergencia per
# gest (ROVER, emissor). Nucli (FSM+sensors+radio de telemetria_radio.py)
# + ampliacions 1-3: registre de cada alerta amb log, i proteocol
# bidireccional (escolta "CMD:S" de l'estacio base a mes de la sacsejada
# propia i del polsador STOP).
# Maquinari: identic a telemetria_radio.py + accelerometer intern (ja
# integrat a la placa, cap cablatge nou).

from microbit import *
import radio
import machine
import utime
import math
import log

GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

PREFIX_TEL = "TEL:"
PREFIX_CMD = "CMD:"   # ampliacio 3: protocol bidireccional (mateix prefix SA5/SA6)

log.set_labels('event', 'instant_ms')

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

TRIGGER = pin1
ECHO = pin2
SEGUIDOR_LINIA = pin0

DHT_PIN = pin8
DHT_PIN.set_pull(DHT_PIN.PULL_UP)

POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)

MPU_ADR = 0x68
MPU_REG_PWR = 0x6B
MPU_REG_ACCEL = 0x3B

VELOCITAT_SO_CM_US = 0.0343
LLINDAR_OBSTACLE_CM = 15
LLINDAR_LINIA = 500
VELOCITAT_AVANCAR = 400
VELOCITAT_GIR = 300

SEGUIR, ESQUIVAR, RECUPERAR = range(3)
NOMS_ESTAT = {SEGUIR: "SEGUIR", ESQUIVAR: "ESQUIVAR", RECUPERAR: "RECUPERAR"}
estat = SEGUIR

INTERVAL_TELEMETRIA_MS = 500
ultim_enviament = running_time()

aturada_emergencia = False   # requisit minim: activada per sacsejada (o CMD:S)


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def girar(costat, velocitat=VELOCITAT_GIR):
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


def polsador_premut():
    return not POLSADOR_STOP.read_digital()


def mesura_distancia():
    TRIGGER.write_digital(0)
    utime.sleep_us(2)
    TRIGGER.write_digital(1)
    utime.sleep_us(10)
    TRIGGER.write_digital(0)
    durada_us = machine.time_pulse_us(ECHO, 1, 30000)
    if durada_us < 0:
        return None
    return (durada_us * VELOCITAT_SO_CM_US) / 2


def mpu_inicia():
    i2c.write(MPU_ADR, bytes([MPU_REG_PWR, 0x00]))


def _valor_16bits(alt, baix):
    valor = (alt << 8) | baix
    if valor > 32767:
        valor -= 65536
    return valor


def mpu_llegeix_accel():
    i2c.write(MPU_ADR, bytes([MPU_REG_ACCEL]), repeat=True)
    dades = i2c.read(MPU_ADR, 6)
    x = _valor_16bits(dades[0], dades[1]) / 16384.0
    y = _valor_16bits(dades[2], dades[3]) / 16384.0
    z = _valor_16bits(dades[4], dades[5]) / 16384.0
    return x, y, z


def mpu_orientacio():
    x, y, z = mpu_llegeix_accel()
    magnitud = math.sqrt(x * x + y * y + z * z)
    return "INCLINAT" if (magnitud < 0.85 or magnitud > 1.15) else "PLA"


def llegeix_dht11():
    DHT_PIN.write_digital(0)
    sleep(20)
    DHT_PIN.set_pull(DHT_PIN.PULL_UP)
    if machine.time_pulse_us(DHT_PIN, 0, 1000) < 0:
        return None
    if machine.time_pulse_us(DHT_PIN, 1, 1000) < 0:
        return None
    bits = []
    for _ in range(40):
        if machine.time_pulse_us(DHT_PIN, 0, 1000) < 0:
            return None
        durada = machine.time_pulse_us(DHT_PIN, 1, 1000)
        if durada < 0:
            return None
        bits.append(1 if durada > 40 else 0)
    bytes_dades = []
    for i in range(5):
        valor = 0
        for b in bits[i * 8:i * 8 + 8]:
            valor = (valor << 1) | b
        bytes_dades.append(valor)
    if (sum(bytes_dades[:4]) & 0xFF) != bytes_dades[4]:
        return None
    return bytes_dades[2], bytes_dades[0]


def actualitza_estat(nou):
    global estat
    estat = nou
    display.show(NOMS_ESTAT[estat][0])


def dispara_alerta_emergencia():
    # Requisit minim: mateixa prioritat que el polsador STOP fisic.
    # Ampliacio 1: registrada amb log (event + instant).
    global aturada_emergencia
    aturada_emergencia = True
    aturar()
    display.show(Image.SKULL)
    log.add(event="ALERTA_STOP", instant_ms=running_time())
    radio.send(PREFIX_TEL + "ALERTA_STOP")


mpu_inicia()
actualitza_estat(SEGUIR)

while True:
    if polsador_premut() or accelerometer.was_gesture("shake"):
        dispara_alerta_emergencia()

    # Ampliacio 3: protocol bidireccional, escolta ordres CMD: a mes de la
    # propia telemetria (nomes "S" fa alguna cosa: atura d'emergencia remota).
    missatge_rebut = radio.receive()
    if missatge_rebut is not None and missatge_rebut.startswith(PREFIX_CMD):
        ordre = missatge_rebut[len(PREFIX_CMD):]
        if ordre == "S":
            dispara_alerta_emergencia()

    if aturada_emergencia:
        sleep(20)
        continue

    distancia = mesura_distancia()
    lectura_linia = SEGUIDOR_LINIA.read_analog()

    if estat == SEGUIR:
        if distancia is not None and distancia < LLINDAR_OBSTACLE_CM:
            aturar()
            actualitza_estat(ESQUIVAR)
        elif lectura_linia < LLINDAR_LINIA:
            avancar(VELOCITAT_AVANCAR)
        else:
            girar('esquerra')
    elif estat == ESQUIVAR:
        girar('dreta')
        sleep(400)
        aturar()
        actualitza_estat(RECUPERAR)
    elif estat == RECUPERAR:
        if lectura_linia < LLINDAR_LINIA:
            actualitza_estat(SEGUIR)
        else:
            avancar(VELOCITAT_AVANCAR)
            sleep(150)
            aturar()

    ara = running_time()
    if ara - ultim_enviament >= INTERVAL_TELEMETRIA_MS:
        ultim_enviament = ara
        lectura_dht = llegeix_dht11()
        temp = lectura_dht[0] if lectura_dht is not None else -1
        humitat = lectura_dht[1] if lectura_dht is not None else -1
        orientacio = mpu_orientacio()
        dist_text = str(int(distancia)) if distancia is not None else "-1"
        missatge = (PREFIX_TEL + "D:" + dist_text +
                    ";S:" + str(lectura_linia) +
                    ";E:" + NOMS_ESTAT[estat] +
                    ";T:" + str(temp) +
                    ";H:" + str(humitat) +
                    ";O:" + orientacio)
        radio.send(missatge)

    sleep(20)
