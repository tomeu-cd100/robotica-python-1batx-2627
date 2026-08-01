# SA3 · Solucionari dels reptes — Entrades: el robot percep

> **Material del docent.** Solucions completes dels tres reptes de [`Reptes_SA3.md`](../../Reptes_SA3.md), amb el nucli i les tres ampliacions graduades ja incorporades. **No es reparteix a l'alumnat abans que hagi entregat el seu propi repte**: com l'exemple resolt de la SA, serveix per corregir i, si cal, per mostrar *després* del primer intent.

> Cada solució és una còpia exacta del fitxer `.py` de la seva carpeta (`repte1_llum_automatica/`, `repte2_aparcament/`, `repte3_estacio_meteo/`): si canvies un fitxer, actualitza també el bloc de codi d'aquí sota.

---

## ⭐ Repte 1 · Llum automàtica d'estudi

**Idea de la solució:** dos llindars (`LLINDAR_FOSCOR`/`LLINDAR_MOLT_FOSC`) que decideixen entre parpelleig ("molt fosc"), intensitat proporcional amb PWM ("fosc") i apagat amb temporitzador mínim (ampliació 3, evita parpellejos ràpids).

```python
# SA3 - Repte 1 (SOLUCIO): llum automatica d'estudi
# Nucli + ampliacions 1-3: segon llindar "molt fosc" amb parpelleig,
# intensitat proporcional (PWM) i temporitzador d'apagada.
# Maquinari: sensor de llum extern al pin P3 (Kit 2), LED extern al pin P1.

from microbit import *

LLINDAR_FOSCOR = 400      # calibrat al REPL
LLINDAR_MOLT_FOSC = 150   # ampliacio 1: per sota, "molt fosc"
TEMPS_MINIM_ENCES = 3000  # ms, ampliacio 3: no s'apaga de cop si torna la llum


def mapa(valor, entrada_min, entrada_max, sortida_min, sortida_max):
    rang_entrada = entrada_max - entrada_min
    rang_sortida = sortida_max - sortida_min
    proporcio = (valor - entrada_min) / rang_entrada
    return int(sortida_min + proporcio * rang_sortida)


t_ultima_encesa = 0


while True:
    llum = pin3.read_analog()

    if llum < LLINDAR_MOLT_FOSC:
        # Ampliacio 1: "molt fosc" -> parpelleig en lloc de fix.
        t_ultima_encesa = running_time()
        pin1.write_digital(1)
        sleep(150)
        pin1.write_digital(0)
        sleep(150)
    elif llum < LLINDAR_FOSCOR:
        # Ampliacio 2: intensitat proporcional a la foscor (PWM).
        t_ultima_encesa = running_time()
        intensitat = mapa(llum, 0, LLINDAR_FOSCOR, 1023, 200)
        pin1.write_analog(intensitat)
        sleep(100)
    else:
        # Ampliacio 3: es mante ences un temps minim encara que torni la llum.
        if running_time() - t_ultima_encesa > TEMPS_MINIM_ENCES:
            pin1.write_digital(0)
        sleep(100)
```

---

## ⭐⭐ Repte 2 · Aparcament amb sensor de distància

**Idea de la solució:** una funció `distancia_cm()` reutilitzada de `alarma_ultrasons.py`, i tres funcions (`zona_lluny`/`zona_atencio`/`zona_perill`, ampliació 3) cridades segons la distància, cadascuna amb el seu propi ritme d'avís (ampliació 2).

```python
# SA3 - Repte 2 (SOLUCIO): aparcament amb sensor de distancia
# Nucli + ampliacions 1-3: distancia al display, ritme progressiu i
# una funcio per zona.
# Maquinari: HC-SR04 (Kit 2), trigger P14, echo P15; brunzidor P2 (Kit 1).

from microbit import *
import machine
import utime
import music

ZONA_ATENCIO_CM = 30
ZONA_PERILL_CM = 15
VELOCITAT_SO_CM_US = 0.0343


def distancia_cm():
    pin14.write_digital(0)
    utime.sleep_us(2)
    pin14.write_digital(1)
    utime.sleep_us(10)
    pin14.write_digital(0)
    durada_us = machine.time_pulse_us(pin15, 1, 30000)
    if durada_us < 0:
        return None
    return (durada_us * VELOCITAT_SO_CM_US) / 2


def zona_lluny(d):
    display.show(str(min(int(d) // 10, 9)))


def zona_atencio(d):
    display.show(str(min(int(d) // 10, 9)))
    music.pitch(660, 80, pin=pin2)
    sleep(300)   # ampliacio 2: ritme mig


def zona_perill(d):
    display.show(str(min(int(d) // 10, 9)))
    music.pitch(880, 80, pin=pin2)
    sleep(100)   # ampliacio 2: ritme rapid, molt a prop


while True:
    d = distancia_cm()
    if d is None:
        display.show("?")
        sleep(200)
        continue

    if d < ZONA_PERILL_CM:
        zona_perill(d)
    elif d < ZONA_ATENCIO_CM:
        zona_atencio(d)
    else:
        zona_lluny(d)
        sleep(200)
```

---

## ⭐⭐⭐ Repte 3 · Estació meteorològica de butxaca

**Idea de la solució:** una funció `resum()` que combina llum i temperatura en una etiqueta de text, un segon "buffer" (`resum_candidat`) que exigeix 2 s d'estabilitat abans de canviar el resum mostrat (ampliació 2), i un avís curt de "ràfega" amb el PIR que no substitueix el resum de fons (ampliació 3).

```python
# SA3 - Repte 3 (SOLUCIO): estacio meteorologica de butxaca
# Nucli + ampliacions 1-3: cinque resum propi, estabilitat de 2 s i
# avis de "rafega" amb el PIR.
# Maquinari: sensor de llum extern P3, sensor de temperatura extern P10
# (Kit 1/2); PIR al pin P8 (Kit 2) per a l'ampliacio 3.

from microbit import *

LLINDAR_CLAR = 500
FRED = 18
CALOR = 26
TEMPS_ESTABLE = 2000   # ms, ampliacio 2


def mapa(valor, entrada_min, entrada_max, sortida_min, sortida_max):
    rang_entrada = entrada_max - entrada_min
    rang_sortida = sortida_max - sortida_min
    proporcio = (valor - entrada_min) / rang_entrada
    return sortida_min + proporcio * rang_sortida


def resum(llum, temp):
    if temp < FRED:
        return "fred"
    if llum > LLINDAR_CLAR and temp > CALOR:
        return "sol"
    if llum <= LLINDAR_CLAR and FRED <= temp <= CALOR:
        return "ennuvolat"
    if llum > LLINDAR_CLAR and temp <= CALOR:
        return "clar"          # ampliacio 1: cinque resum propi
    return "variable"


def mostra_resum(nom):
    if nom == "sol":
        display.show(Image.HAPPY)
    elif nom == "fred":
        display.show(Image.SAD)
    elif nom == "ennuvolat":
        display.show(Image.MEH)
    elif nom == "clar":
        display.show(Image.CONFUSED)
    else:
        display.show(Image.SURPRISED)


resum_actual = None
resum_candidat = None
t_candidat = running_time()

while True:
    llum = pin3.read_analog()
    temp = mapa(pin10.read_analog(), 0, 1023, 0, 50)
    nou = resum(llum, temp)

    # Ampliacio 3: rafega detectada pel PIR, avis curt per sobre del resum.
    if pin8.read_digital() == 1:
        display.show(Image.TARGET)
        sleep(500)

    # Ampliacio 2: nomes canvia el resum si es mante estable 2 s seguits.
    if nou != resum_candidat:
        resum_candidat = nou
        t_candidat = running_time()
    elif running_time() - t_candidat > TEMPS_ESTABLE and nou != resum_actual:
        resum_actual = nou
        mostra_resum(resum_actual)

    sleep(200)
```

---

*Solucionari de la SA3. Material del docent. Es recolza en `Classes/SA3/codi/`. Llicència CC BY-SA 4.0.*
