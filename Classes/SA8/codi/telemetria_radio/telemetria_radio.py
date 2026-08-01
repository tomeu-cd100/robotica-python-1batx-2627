# SA8 - telemetria_radio.py  (PRODUCTE de la SA, Sessions 2-3)
# El rover es mou amb la MATEIXA arquitectura de prioritats de
# comportaments.py (SEGUIR linia -> ESQUIVAR obstacle -> RECUPERAR linia) i,
# a mes, envia per radio el seu estat i les lectures dels sensors avancats
# del Kit 3 cada INTERVAL_TELEMETRIA_MS. Prefix "TEL:" DIFERENT del "CMD:"
# de la SA5/SA6, perque la placa receptora (estacio_base.py) no confongui
# telemetria amb una ordre de control.
# NUCLI de telemetria (fitxa 17: "com a minim dos sensors del Kit 3"): IMU
# MPU6050 (orientacio, per I2C) + DHT11 (temperatura/humitat, digital). El
# BMP280 i el CCS811 tambe son I2C, al MATEIX bus (adreca diferent): queden
# com a +ampliacio (vegeu SA8_fitxa_ampliada.md), no calen per al nucli.
# Cablatge (00_Fil_conductor_construccions.md #1b, font unica): M1=P13/P14,
# M2=P15/P16, HC-SR04 trigger=P1 echo=P2, seguidor de linia=P0, DHT11=P8,
# IMU MPU6050 (I2C) = P19 SCL / P20 SDA, polsador STOP=P12 (pull-up).
# Simulador: la radio SI es simula (2 instancies obertes alhora), pero CAP
# sensor ni motor d'aquest programa es simula: la part de moviment i
# sensors nomes es prova amb el rover real; la part de protocol de radio
# (el format del missatge) es pot assajar amb dues pestanyes del simulador.

from microbit import *
import radio
import machine
import utime
import math

GRUP = 1   # ha de coincidir amb el GRUP d'estacio_base.py de la parella

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

# Adreca I2C i registres del MPU6050 (mateix bus P19/P20 que BMP280/CCS811,
# cadascun amb la seva propia adreca: no calen pins nous per afegir-ne mes).
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

INTERVAL_TELEMETRIA_MS = 500   # cada quant s'envia un missatge TEL:
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
    # Mateixa lectura robusta que evita_obstacles.py (SA7-S3): time_pulse_us
    # pot senyalar timeout amb un valor negatiu O amb una excepcio OSError
    # (depen de placa/versio); el try/except cobreix el segon cas.
    TRIGGER.write_digital(0)
    utime.sleep_us(2)
    TRIGGER.write_digital(1)
    utime.sleep_us(10)
    TRIGGER.write_digital(0)
    try:
        durada_us = machine.time_pulse_us(ECHO, 1, 30000)
    except OSError:
        return None
    if durada_us < 0:
        return None
    return (durada_us * VELOCITAT_SO_CM_US) / 2


def mpu_inicia():
    # El MPU6050 arrenca en mode "sleep": cal despertar-lo escrivint 0 al
    # registre de gestio d'energia abans de poder llegir cap dada.
    i2c.write(MPU_ADR, bytes([MPU_REG_PWR, 0x00]))


def _valor_16bits(alt, baix):
    valor = (alt << 8) | baix
    if valor > 32767:          # complement a 2 (el sensor dona valors amb signe)
        valor -= 65536
    return valor


def mpu_llegeix_accel():
    # Llegeix 6 bytes consecutius (X, Y, Z, 2 bytes cadascun) a partir del
    # registre ACCEL_XOUT_H. Retorna els tres eixos en unitats "g".
    i2c.write(MPU_ADR, bytes([MPU_REG_ACCEL]), repeat=True)
    dades = i2c.read(MPU_ADR, 6)
    x = _valor_16bits(dades[0], dades[1]) / 16384.0   # rang +-2g de fabrica
    y = _valor_16bits(dades[2], dades[3]) / 16384.0
    z = _valor_16bits(dades[4], dades[5]) / 16384.0
    return x, y, z


def mpu_orientacio():
    # Amb el rover quiet i pla, la magnitud del vector acceleracio hauria de
    # ser propera a 1.0 g (nomes la gravetat). Si s'allunya prou d'1.0, el
    # rover esta inclinat o rebent un gest/sacsejada: es el mateix principi
    # que fara servir Teachable Machine a la Sessio 3, aqui amb un llindar
    # fet a ma en lloc d'un model entrenat.
    x, y, z = mpu_llegeix_accel()
    magnitud = math.sqrt(x * x + y * y + z * z)
    return "INCLINAT" if (magnitud < 0.85 or magnitud > 1.15) else "PLA"


def llegeix_dht11():
    # Protocol DHT11: 40 bits mesurats amb machine.time_pulse_us, EXACTAMENT
    # el mateix mecanisme que mesura_distancia() (temps de vol de l'HC-SR04),
    # nomes que aqui es mesuren 40 polsos consecutius en lloc d'un de sol.
    # Mateixa lectura robusta que evita_obstacles.py (SA7-S3): un try/except
    # OSError embolica TOTS els time_pulse_us, perque un sol timeout aturat
    # com a excepcio (en lloc de valor negatiu) no faci petar el programa.
    # Retorna (temperatura, humitat) o None si la lectura/checksum falla
    # (pot passar per pauses del recol.lector d'escombraries: es normal,
    # simplement es descarta aquesta lectura i es reintenta a la seguent).
    DHT_PIN.write_digital(0)
    sleep(20)                       # senyal de start (minim 18 ms)
    DHT_PIN.set_pull(DHT_PIN.PULL_UP)
    try:
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
            bits.append(1 if durada > 40 else 0)   # >40us alt = bit '1'
    except OSError:
        return None
    bytes_dades = []
    for i in range(5):
        valor = 0
        for b in bits[i * 8:i * 8 + 8]:
            valor = (valor << 1) | b
        bytes_dades.append(valor)
    if (sum(bytes_dades[:4]) & 0xFF) != bytes_dades[4]:
        return None                 # checksum erroni: descarta la lectura
    return bytes_dades[2], bytes_dades[0]   # (temperatura, humitat)


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

    # Telemetria: NOMES cada INTERVAL_TELEMETRIA_MS (no a cada volta del
    # bucle, que aniria massa de pressa per a la radio i per a qui ho llegeix
    # a l'estacio base).
    ara = running_time()
    if ara - ultim_enviament >= INTERVAL_TELEMETRIA_MS:
        ultim_enviament = ara
        lectura_dht = llegeix_dht11()
        temp = lectura_dht[0] if lectura_dht is not None else -1
        humitat = lectura_dht[1] if lectura_dht is not None else -1
        orientacio = mpu_orientacio()
        dist_text = str(int(distancia)) if distancia is not None else "-1"
        missatge = (PREFIX + "D:" + dist_text +
                    ";S:" + str(lectura_linia) +
                    ";E:" + NOMS_ESTAT[estat] +
                    ";T:" + str(temp) +
                    ";H:" + str(humitat) +
                    ";O:" + orientacio)
        radio.send(missatge)

    sleep(20)
