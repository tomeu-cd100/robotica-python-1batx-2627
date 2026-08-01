# Telemetria per ràdio: el rover explica el que "sent" (Sessions 2-3)

**Quan es fa:** Sessions 2-3 (producte) · **Fitxer:** `telemetria_radio.py` · **Maquinari:** [esquemes de connexions](../../SA8_esquemes_connexions.md) — mateix cablatge de comportaments.py + DHT11 a **P8** + IMU MPU6050 per I2C a **P19 (SCL) / P20 (SDA)**

## 🎯 Per què fem aquesta pràctica

Aquest programa respon a la pregunta inicial de la SA: *"com sap algú, des d'una altra taula, què està 'sentint' el rover?"* Reutilitza **exactament** la FSM de [`comportaments.py`](../comportaments/EXPLICACIO.md) (SEGUIR/ESQUIVAR/RECUPERAR) i hi afegeix dues coses noves: llegir dos sensors del **Kit 3** (IMU MPU6050 per I2C i DHT11 per un pin digital) i enviar-ho tot per **ràdio** amb un protocol propi, amb el prefix `"TEL:"` (en lloc del `"CMD:"` de la SA5/SA6) perquè la placa receptora sàpiga que és **telemetria**, no una ordre.

## 🔮 Abans d'executar: prediu

Si envies un missatge de telemetria a cada volta del bucle principal (cada ~20 ms) en lloc de cada `INTERVAL_TELEMETRIA_MS` (500 ms), què li passaria a la ràdio i a qui llegeix les dades a l'altra banda?

## 🧠 El codi, per blocs

### Bloc 1 — Un prefix diferent, el mateix patró de protocol

```python
PREFIX = "TEL:"
...
radio.send(missatge)
```

Mateixa idea de `PREFIX` que `comandament.py`/`vehicle_seguretat.py` (SA5-SA6), però amb un prefix **diferent**: així `estacio_base.py` pot distingir un missatge de telemetria d'una futura ordre de control sense ambigüitat.

### Bloc 2 — Llegir l'IMU per I2C: despertar-lo i llegir registres

```python
def mpu_inicia():
    i2c.write(MPU_ADR, bytes([MPU_REG_PWR, 0x00]))

def mpu_llegeix_accel():
    i2c.write(MPU_ADR, bytes([MPU_REG_ACCEL]), repeat=True)
    dades = i2c.read(MPU_ADR, 6)
    ...
```

El MPU6050 es connecta pel bus **I2C** (P19 SCL / P20 SDA): en lloc d'un pin dedicat per component (com el seguidor de línia a P0), es "parla" amb el sensor escrivint i llegint **registres** a la seva adreça (`0x68`). Primer cal despertar-lo (surt de mode "sleep" de fàbrica); després es llegeixen 6 bytes (2 per eix) i es converteixen a unitats "g".

### Bloc 3 — Llegir el DHT11: el mateix time-of-flight de l'HC-SR04, repetit 40 cops

```python
if machine.time_pulse_us(DHT_PIN, 0, 1000) < 0:
    return None
...
bits.append(1 if durada > 40 else 0)
```

El DHT11 no és analògic ni I2C: envia les seves dades com una seqüència de 40 **polsos** de durada variable. Es mesuren amb `machine.time_pulse_us`, **exactament** la mateixa eina que `mesura_distancia()` (SA7) fa servir per l'HC-SR04, només que aquí cal repetir-la 40 vegades i muntar els bits en 5 bytes (humitat, temperatura i una suma de control). Si la suma de control no quadra, la lectura es descarta (`return None`): més val "no tinc dada aquest cop" que una dada incorrecta.

### Bloc 4 — Enviar telemetria NOMÉS cada cert temps

```python
ara = running_time()
if ara - ultim_enviament >= INTERVAL_TELEMETRIA_MS:
    ultim_enviament = ara
    ...
    radio.send(missatge)
```

El bucle de moviment corre cada ~20 ms (perquè el rover reaccioni de pressa), però la telemetria només s'envia cada `INTERVAL_TELEMETRIA_MS` (500 ms): enviar-ho tot a cada volta saturaria la ràdio i la pantalla de l'estació base amb missatges repetits sense cap informació nova.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| `mpu_llegeix_accel()` no respon o penja el programa | Cablatge I2C intercanviat (SCL↔SDA) o GND no comú entre les dues plaques del bus |
| `llegeix_dht11()` retorna sempre `None` | Cablatge al pin equivocat (ha de ser **P8**), o cal esperar-hi més entre lectures (el DHT11 no es pot llegir més sovint que cada ~1-2 s) |
| L'estació base no rep res | `GRUP` diferent entre `telemetria_radio.py` i `estacio_base.py`, o `PREFIX` escrit de manera diferent a cada banda |

## 🔗 On ho aplicaràs

- **Ara mateix:** és el **producte de la SA**, junt amb [`estacio_base`](../estacio_base/EXPLICACIO.md), que ha d'escriure **cada alumne**.
- **Sessió 3:** la reflexió sobre IA (Teachable Machine) parteix de la mateixa idea que `mpu_orientacio()` fa "a mà" (un llindar sobre la magnitud d'acceleració): un classificador entrenat faria el mateix, però après de dades enlloc de programat.
- **Simulador:** la **ràdio sí** es simula (2 instàncies obertes alhora, per assajar el format del missatge); **cap** sensor ni motor d'aquest programa es simula.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA8](../../../../Reptes/Reptes_SA8.md)**.
