# SA8 - Repte 1 (SOLUCIO): estacio meteorologica escolar amb alertes
# Nucli (telemetria IMU+DHT11 per radio) + ampliacions 1-3: icona segons
# alerta, comptador d'alertes per REPL (A+B), i histeresi (dos llindars,
# com termostat_histeresi.py de la SA6) perque l'alerta no "parpellegi".
# Maquinari: identic a telemetria_radio.py (motors M1/M2, HC-SR04, seguidor
# de linia, DHT11=P8, IMU MPU6050 I2C=P19/P20, polsador STOP=P12).

from microbit import *
import radio
import machine
import utime
import math

GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "TEL:"

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

# Requisit minim: llindar de temperatura per activar l'alerta.
# Ampliacio 3: histeresi amb DOS llindars, en lloc d'un de sol, perque
# l'alerta no canvii d'estat cada cop que la temperatura balla un grau.
LLINDAR_TEMP_BAIX = 26   # per sota d'aixo, desactiva l'alerta
LLINDAR_TEMP_ALT = 29    # per sobre d'aixo, activa l'alerta

SEGUIR, ESQUIVAR, RECUPERAR = range(3)
NOMS_ESTAT = {SEGUIR: "SEGUIR", ESQUIVAR: "ESQUIVAR", RECUPERAR: "RECUPERAR"}
estat = SEGUIR

alerta_activa = False    # variable d'estat propia de l'alerta (histeresi)
comptador_alertes = 0    # ampliacio 2: quantes vegades s'ha activat

INTERVAL_TELEMETRIA_MS = 500
ultim_enviament = running_time()


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


def actualitza_alerta(temp):
    # Histeresi (ampliacio 3): nomes canvia "alerta_activa" quan la
    # temperatura travessa DE VERITAT un dels dos llindars, no quan balla
    # entre ells.
    global alerta_activa, comptador_alertes
    if not alerta_activa and temp > LLINDAR_TEMP_ALT:
        alerta_activa = True
        comptador_alertes += 1
    elif alerta_activa and temp < LLINDAR_TEMP_BAIX:
        alerta_activa = False


def actualitza_estat(nou):
    global estat
    estat = nou
    display.show(NOMS_ESTAT[estat][0])


mpu_inicia()
actualitza_estat(SEGUIR)

while True:
    if polsador_premut():
        aturar()
        display.show(Image.NO)
        sleep(20)
        continue

    if button_a.is_pressed() and button_b.is_pressed():
        # Ampliacio 2: comptador d'alertes per REPL.
        print("Alertes des de l'engegada:", comptador_alertes)

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

        if lectura_dht is not None:
            actualitza_alerta(temp)

        # Ampliacio 1: icona segons l'alerta (nomes quan no hi ha cap altre
        # missatge mostrant-se al display per l'estat de la FSM).
        if alerta_activa:
            display.show(Image.SAD)

        dist_text = str(int(distancia)) if distancia is not None else "-1"
        missatge = (PREFIX + "D:" + dist_text +
                    ";S:" + str(lectura_linia) +
                    ";E:" + NOMS_ESTAT[estat] +
                    ";T:" + str(temp) +
                    ";H:" + str(humitat) +
                    ";O:" + orientacio +
                    ";AL:" + ("1" if alerta_activa else "0"))
        radio.send(missatge)

    sleep(20)
