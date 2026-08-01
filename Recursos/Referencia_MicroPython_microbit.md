# Referència ràpida de MicroPython per a micro:bit

> **Per a qui és?** Docent i alumnat. **Xuleta d'una parell de pàgines**:
> només l'API de `microbit` (i mòduls relacionats) que **realment s'usa en
> algun punt del curs**, no tota la biblioteca. Per a qualsevol funció que
> no hi surti, consulta la referència completa a
> [`Enllacos_i_tutorials.md`](Enllacos_i_tutorials.md#2-documentacio-oficial-de-micropython-per-a-microbit)
> (docs oficials de MicroPython micro:bit).

Tot programa comença amb:
```python
from microbit import *
```
i, si cal, `import music`, `import radio`, `import log` o `import machine`
a banda (no formen part de `from microbit import *`).

## 1. Display (matriu de 5×5 LED)

| Crida | Què fa |
|---|---|
| `display.show(Image.HAPPY)` | Mostra una imatge predefinida o pròpia. |
| `display.scroll("HOLA")` | Fa desfilar un text lletra a lletra. |
| `display.clear()` | Apaga tots els LED. |
| `display.set_pixel(col, fila, brillantor)` | Encén 1 píxel (`0-4`, `0-4`, brillantor `0-9`). |
| `display.get_pixel(col, fila)` | Llegeix la brillantor d'1 píxel. |
| `display.read_light_level()` | Sensor de llum **intern** (0-255): reaprofita la matriu com a fotosensor. |

**`Image.*` predefinides usades al curs:** `HAPPY, SAD, ANGRY, ASLEEP,
CONFUSED, MEH, SURPRISED, NO, YES, HEART, SKULL, DIAMOND, TARGET,
CHESSBOARD, SQUARE, SQUARE_SMALL, ARROW_N/E/S/W` (i la resta de fletxes
cardinals: `ARROW_NE/SE/SW/NW`).

Imatge pròpia: `Image("90009:09090:00900:09090:90009")` (5 files de 5
dígits `0-9` de brillantor, separades per `:`).

## 2. Botons A i B

| Crida | Què fa |
|---|---|
| `button_a.is_pressed()` | `True` mentre el botó està premut (estat). |
| `button_a.was_pressed()` | `True` **un sol cop** des de l'última lectura (esdeveniment; consumeix el registre). |

Igual per a `button_b`. **`is_pressed()` és idempotent** (no cal
antirebot per programari); `was_pressed()` ja fa d'antirebot d'esdeveniment.

## 3. Pins d'entrada/sortida

Pins usats al curs: `pin0, pin1, pin2, pin3, pin8, pin10, pin12, pin13,
pin14, pin15, pin16, pin19, pin20` (assignació concreta per SA i per robot
a `Classes/00_General/00_Fil_conductor_construccions.md` §1b, «Mapa de
pins per trimestre», **font única**).

| Crida | Què fa |
|---|---|
| `pinN.read_digital()` | Llegeix 0/1 (polsadors, PIR, ECHO de l'HC-SR04...). |
| `pinN.write_digital(0\|1)` | Escriu 0/1 (LED, relé, TRIG de l'HC-SR04...). |
| `pinN.read_analog()` | Llegeix 0-1023 (**només** pins ADC vàlids: P0/P1/P2/P3/P4/P10). |
| `pinN.write_analog(0-1023)` | Escriu PWM (servos, velocitat de motor). |
| `pinN.set_analog_period(ms)` | Canvia el període del PWM (p. ex. `20` ms per a servos). |
| `pinN.set_pull(pinN.PULL_UP)` | Activa la resistència de *pull-up* interna (polsadors amb GND). |
| `pin_logo.is_touched()` | Sensor tàctil del logotip (contacte capacitiu). |

> ⚠️ Un `pinN.write_analog()`/`read_analog()` sobre un pin **no ADC**
> produeix un error o una lectura sense sentit; comprova sempre la
> llista de pins ADC vàlids abans de cablejar un sensor analògic.

## 4. So: `music` (i `pinN` com a sortida del brunzidor)

| Crida | Què fa |
|---|---|
| `music.play(['C4:2', 'E4:2', 'G4:2'], pin=pin2, wait=False)` | Reprodueix una llista de notes (`Nota+Octava:Durada`) pel pin indicat, sense bloquejar el programa (`wait=False`). |
| `music.pitch(freqüència, duració_ms, pin=pin2)` | Reprodueix un to pur d'una freqüència concreta. |

## 5. Ràdio: `radio`

```python
import radio
radio.on()
radio.config(group=10, power=6)   # mateix group a totes les plaques que es parlen
radio.send("F")                    # envia una cadena de text
missatge = radio.receive()         # None si no hi ha res de nou
```

Protocol propi del curs: prefixos de text (`"CMD:F"`, `"TEL:temp:23.5"`...);
vegeu `Programació didàctica/14_SA5_Radio_robots_que_parlen.md` i
`17_SA8_Autonomia_i_telemetria.md` per al detall del protocol de cada SA.

## 6. Acceleròmetre: `accelerometer`

| Crida | Què fa |
|---|---|
| `accelerometer.was_gesture("shake")` | `True` un sol cop en detectar el gest. |

Gestos usats al curs: `"shake"`, `"left"`, `"right"`, `"face up"`,
`"face down"`.

## 7. Micròfon: `microphone`

| Crida | Què fa |
|---|---|
| `microphone.sound_level()` | Nivell de so **intern** (0-255); alternativa al sensor de so del Kit 3 si no es vol cablejar res. |

## 8. Registre de dades: `log`

```python
import log
log.set_labels('temp', 'llum')     # capçalera del full (un sol cop)
log.add(temp=temperature(), llum=display.read_light_level())
```
El `log` **natiu** de la micro:bit V2 desa els registres a la memòria
interna de la placa (fitxer `MY_DATA.HTM`, es descarrega connectant-la per
USB com una unitat). Substitueix `print()` per a sèries de mesures llargues
(SA6, SA8).

## 9. Sensors interns i temps

| Crida | Què fa |
|---|---|
| `temperature()` | Temperatura interna del xip, en ºC (aprox., no és un termòmetre de precisió). |
| `running_time()` | Mil·lisegons des de l'engegada de la placa (per a temporitzadors i antirebot). |
| `sleep(ms)` | Pausa el programa `ms` mil·lisegons. |

## 10. Bus I2C (sensors del Kit 3: MPU6050, BMP280, CCS811 — SA8)

`i2c` **ja existeix** amb `from microbit import *` (bus fix a P19 SCL /
P20 SDA): **no cal** `machine.I2C()` ni cap `i2c.init()`.

| Crida | Què fa |
|---|---|
| `i2c.write(adreça, bytes([...]))` | Escriu una seqüència de bytes al dispositiu de l'`adreça` donada. |
| `i2c.write(adreça, bytes([registre]), repeat=True)` | Escriu **sense deixar anar el bus** (`repeat=True`): apunta a un registre abans de llegir-lo tot seguit, sense que un altre dispositiu I2C hi pugui interferir pel mig. |
| `i2c.read(adreça, n_bytes)` | Llegeix `n_bytes` consecutius del dispositiu. |

Exemple real (IMU MPU6050, adreça `0x68`, `Classes/SA8/codi/telemetria_radio/telemetria_radio.py`):
```python
MPU_ADR = 0x68
MPU_REG_PWR = 0x6B      # registre de gestió d'energia (el sensor arrenca en "sleep")
MPU_REG_ACCEL = 0x3B    # primer registre de l'acceleròmetre (X alt)

i2c.write(MPU_ADR, bytes([MPU_REG_PWR, 0x00]))          # el desperta
i2c.write(MPU_ADR, bytes([MPU_REG_ACCEL]), repeat=True)  # apunta al registre
dades = i2c.read(MPU_ADR, 6)                              # llegeix X, Y, Z (2 bytes cadascun)
```
Cada sensor I2C té la seva pròpia adreça i mapa de registres (datasheet del
fabricant); vegeu `Classes/SA8/codi/` per als drivers ja fets al curs
(MPU6050 al nucli; BMP280/CCS811 a l'ampliació, mateix bus, adreça diferent).

## 11. `machine.time_pulse_us` (mesura de polsos: HC-SR04, DHT11)

`machine` **sí** cal importar-lo (`import machine`), però al curs **només**
s'hi usa aquesta funció, per mesurar quant dura un pols digital (temps de
vol):

```python
import machine
durada_us = machine.time_pulse_us(pin, valor_pols, temps_maxim_us)
```
- **HC-SR04** (SA7-SA8): un sol pols a l'ECHO, per calcular la distància.
- **DHT11** (SA6-SA8): 40 polsos consecutius, per muntar els bits de
  temperatura/humitat (mateix mecanisme, repetit).

Retorna la durada en microsegons, o un valor negatiu si no arriba cap pols
dins del `temps_maxim_us` (llavors es descarta la lectura, `return None`).

---

⬅️ Torna a [`00_LLEGEIX-ME_Recursos.md`](00_LLEGEIX-ME_Recursos.md).
