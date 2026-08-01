# SA8 · Solucionari dels reptes — Autonomia i telemetria

> **Material del docent.** Solucions completes dels tres reptes de [`Reptes_SA8.md`](../../Reptes_SA8.md), amb el nucli i les tres ampliacions graduades ja incorporades. **No es reparteix a l'alumnat abans que hagi entregat el seu propi repte**: com l'exemple resolt de la SA, serveix per corregir i, si cal, per mostrar *després* del primer intent.

> Cada solució és una còpia exacta del/dels fitxer(s) `.py` de la seva carpeta (`repte1_estacio_alertes/`, `repte2_estacio_multisensor/`, `repte3_missio_telemetrada/`): si canvies un fitxer, actualitza també el bloc de codi d'aquí sota.

---

## ⭐ Repte 1 · Estació meteorològica escolar amb alertes

**Idea de la solució:** parteix de `telemetria_radio.py` i hi afegeix una **variable d'estat pròpia** (`alerta_activa`) amb **histèresi** (dos llindars, `LLINDAR_TEMP_BAIX`/`LLINDAR_TEMP_ALT`, mateixa idea que `termostat_histeresi.py` de la SA6), una icona al display quan l'alerta és activa (ampliació 1), i un comptador d'alertes mostrat per REPL en prémer A+B (ampliació 2). El nou camp `"AL:"` s'afegeix al mateix missatge de telemetria, sense trencar el format dels camps ja existents.

```python
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
```

---

## ⭐⭐ Repte 2 · Estació base multisensor amb registre avançat

**Idea de la solució:** parteix de `estacio_base.py` i hi afegeix el seguiment de `temp_maxima`/`temp_minima` (requisit mínim), una navegació de vistes amb els botons A/B (ampliació 1), un camp `record` al `log` (ampliació 2), i una detecció de "sense senyal" basada en `running_time()` (ampliació 3).

```python
# SA8 - Repte 2 (SOLUCIO): estacio base multisensor amb registre avancat
# Nucli (rebre, analitzar, registrar amb log) + ampliacions 1-3: navegacio
# de camps amb botons A/B, marca de "nou record" al log, i deteccio de
# "sense senyal" quan fa massa temps que no arriba cap missatge.
# Maquinari: identic a estacio_base.py (nomes radio interna + display).

from microbit import *
import radio
import log

GRUP = 1
radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "TEL:"

log.set_labels('dist', 'seguidor', 'estat', 'temp', 'humitat', 'orientacio', 'record')

MAX_HISTORIC = 10
historic_distancies = []

# Requisit minim: seguiment de maxim/minim de temperatura.
temp_maxima = None
temp_minima = None

# Ampliacio 1: navegacio entre vistes amb els botons.
VISTES = ["ULTIMA", "MITJANA", "MAXMIN"]
vista_actual = 0

# Ampliacio 3: deteccio de "sense senyal".
LLINDAR_SENSE_SENYAL_MS = 5000
ultim_missatge_rebut = running_time()
ultima_temp = None


def analitza(missatge):
    dades = {}
    cos = missatge[len(PREFIX):]
    for camp in cos.split(";"):
        if ":" not in camp:
            continue
        clau, valor = camp.split(":", 1)
        dades[clau] = valor
    return dades


def mitjana(llista):
    return sum(llista) / len(llista) if llista else 0


def mostra_vista():
    nom = VISTES[vista_actual]
    if nom == "ULTIMA" and ultima_temp is not None:
        display.scroll(str(ultima_temp), delay=80, wait=False)
    elif nom == "MITJANA":
        display.scroll(str(int(mitjana(historic_distancies))), delay=80, wait=False)
    elif nom == "MAXMIN" and temp_maxima is not None:
        display.scroll(str(temp_maxima) + "/" + str(temp_minima), delay=80, wait=False)


while True:
    if button_a.was_pressed():
        # Ampliacio 1: canvia de vista sense esperar cap missatge nou.
        vista_actual = (vista_actual + 1) % len(VISTES)
        mostra_vista()

    if button_b.was_pressed():
        mostra_vista()

    # Ampliacio 3: si fa massa temps que no arriba res, avisa'n.
    ara = running_time()
    if ara - ultim_missatge_rebut > LLINDAR_SENSE_SENYAL_MS:
        display.show(Image.CONFUSED)

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ultim_missatge_rebut = running_time()
        dades = analitza(missatge)

        try:
            distancia = int(dades.get("D", -1))
        except ValueError:
            distancia = -1
        historic_distancies.append(distancia)
        if len(historic_distancies) > MAX_HISTORIC:
            historic_distancies.pop(0)

        try:
            temp = int(dades.get("T", -1))
        except ValueError:
            temp = -1
        ultima_temp = temp

        es_record = False
        if temp != -1:
            if temp_maxima is None or temp > temp_maxima:
                temp_maxima = temp
                es_record = True
            if temp_minima is None or temp < temp_minima:
                temp_minima = temp
                es_record = True

        log.add(dist=dades.get("D", ""), seguidor=dades.get("S", ""),
                 estat=dades.get("E", ""), temp=dades.get("T", ""),
                 humitat=dades.get("H", ""), orientacio=dades.get("O", ""),
                 record="1" if es_record else "0")

        print(missatge, "| mitjana D:", mitjana(historic_distancies),
              "| max/min T:", temp_maxima, temp_minima)
        mostra_vista()

    sleep(50)
```

---

## ⭐⭐⭐ Repte 3 · Missió telemetrada amb alerta d'emergència per gest

**Idea de la solució:** dos fitxers, com el parell `telemetria_radio.py`/`estacio_base.py` del nucli. Al **rover** (`repte3_missio_telemetrada.py`), `dispara_alerta_emergencia()` centralitza les tres vies d'aturada d'emergència (polsador STOP físic, sacsejada pròpia i, amb l'ampliació 3, la comanda `"CMD:S"` rebuda per ràdio), sempre amb la mateixa prioritat màxima, i la registra amb `log`. A l'**estació base** (`repte3_missio_telemetrada_estacio.py`), el botó A envia `"CMD:S"` (protocol bidireccional, ampliació 3) i es compta cada alerta rebuda (ampliació 2).

```python
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
```

```python
# SA8 - Repte 3 (SOLUCIO): missio telemetrada amb alerta d'emergencia per
# gest (ESTACIO BASE, receptor). Nucli (rebre, mostrar, registrar) +
# ampliacio 2 (comptador d'alertes per REPL) + ampliacio 3 (boto A envia
# "CMD:S" per aturar el rover a distancia, protocol bidireccional).
# Maquinari: identic a estacio_base.py (nomes radio interna + display).

from microbit import *
import radio
import log

GRUP = 1
radio.on()
radio.config(group=GRUP, power=6)

PREFIX_TEL = "TEL:"
PREFIX_CMD = "CMD:"

log.set_labels('dist', 'seguidor', 'estat', 'temp', 'humitat', 'orientacio')

MAX_HISTORIC = 10
historic_distancies = []
comptador_alertes = 0   # ampliacio 2


def analitza(missatge, prefix):
    dades = {}
    cos = missatge[len(prefix):]
    for camp in cos.split(";"):
        if ":" not in camp:
            continue
        clau, valor = camp.split(":", 1)
        dades[clau] = valor
    return dades


def mitjana(llista):
    return sum(llista) / len(llista) if llista else 0


while True:
    if button_a.was_pressed():
        # Ampliacio 3: protocol bidireccional, atura el rover a distancia.
        radio.send(PREFIX_CMD + "S")
        display.show(Image.NO)
        sleep(150)

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX_TEL):
        cos = missatge[len(PREFIX_TEL):]

        if cos == "ALERTA_STOP":
            comptador_alertes += 1
            print("ALERTA D'EMERGENCIA rebuda. Total:", comptador_alertes)
            display.show(Image.SKULL)
            sleep(300)
            continue

        dades = analitza(missatge, PREFIX_TEL)
        try:
            distancia = int(dades.get("D", -1))
        except ValueError:
            distancia = -1
        historic_distancies.append(distancia)
        if len(historic_distancies) > MAX_HISTORIC:
            historic_distancies.pop(0)

        log.add(dist=dades.get("D", ""), seguidor=dades.get("S", ""),
                 estat=dades.get("E", ""), temp=dades.get("T", ""),
                 humitat=dades.get("H", ""), orientacio=dades.get("O", ""))

        print(missatge, "| mitjana D:", mitjana(historic_distancies))
        display.show(Image.YES)

    sleep(50)
```
