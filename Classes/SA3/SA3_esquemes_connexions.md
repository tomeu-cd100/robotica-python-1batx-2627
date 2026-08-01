# SA3 · Esquemes i connexions

> 🧑‍🎓 **Quan toca?** Tingues aquesta pàgina oberta durant les **Sessions 1-3**, cada cop que munts un sensor nou al Micro:shield. A partir d'avui la micro:bit **llegeix** el món exterior: aquí comença la sèrie de taules de connexió d'entrades que t'acompanyarà fins a la SA8.

> ⚠️ **Abans de connectar res:** micro:bit **desendollada** de l'USB. Comprova que cap component analògic va a un pin **sense ADC** (només P0, P1, P2, P3, P4 i P10 llegeixen valors analògics) i que l'HC-SR04 rep **5 V**, no 3,3 V.

---

## 1. Pins analògics (ADC) del micro:bit V2 — regla d'or de la SA3

Només els pins **P0, P1, P2, P3, P4 i P10** tenen conversor analògic-digital (ADC): són els únics on `read_analog()` dona un valor fiable (0-1023). A partir d'avui, **cap component que es llegeixi de manera analògica pot anar a un altre pin.** Els pins purament digitals (botons, PIR, HC-SR04...) no tenen aquesta restricció.

## 2. Taula de connexions d'aquesta SA (pràctiques `codi/`)

| Component | Pin | Tipus | Kit | Programa(es) | Notes |
|---|---|---|---|---|---|
| Botons **A**/**B** | interns | Digital | micro:bit | (S1, en viu al REPL) | `button_a.is_pressed()`/`button_b.is_pressed()`, sense cablatge. |
| Polsador extern | — | Digital, *pull-up* | Kit 1 | (S1, en viu al REPL) | Concepte d'antirebot (*debounce*); es reutilitza cablejat i programat a `mascota_reactiva` (P12). |
| Sensor de llum **intern** | — | Analògic (0-255) | micro:bit | `nivell_llum` | `display.read_light_level()`, sense cablatge (reaprofita la matriu de LED). |
| Sensor de llum **extern** | **P3** | Analògic (0-1023), ADC | Kit 2 | `nivell_llum` | Pin lliure durant aquesta SA (no forma part del cablatge final de la mascota). |
| Sensor de temperatura **intern** | — | (graus C directes) | micro:bit | `termometre` | `temperature()`, sense cablatge. |
| Sensor de temperatura **extern** (bàsic) | **P10** | Analògic (0-1023), ADC | Kit 1 | `termometre` | Calibra el pendent real amb el REPL abans de fixar `FRED`/`CALOR`. |
| Potenciòmetre | **P3** (temporal) | Analògic, ADC | Kit 1 | (S2, exercici curt al REPL) | Mateix pin que el sensor de llum extern (es desmunta un per muntar l'altre); mateix mètode `read_analog()` + `mapa()`. |
| HC-SR04 (ultrasons): **trigger** | **P14** | Digital (sortida) | Kit 2 | `alarma_ultrasons` | Pols de 10 µs (`utime.sleep_us`). |
| HC-SR04 (ultrasons): **echo** | **P15** | Digital (entrada, temporitzada) | Kit 2 | `alarma_ultrasons` | `machine.time_pulse_us(pin15, 1, timeout)`. |
| HC-SR04: alimentació | 5 V / GND | — | Kit 2 | `alarma_ultrasons` | **Necessita 5 V**, no 3,3 V: usa el connector d'alimentació externa del Micro:shield. |
| Brunzidor (alarma) | **P2** | PWM/digital | Kit 1 | `alarma_ultrasons` | Reaprofita el mateix pin que la SA2 (`musica_altaveu`); és normal muntar/desmuntar entre exercicis. |

> ⚠️ **HC-SR04, seguretat del pin echo:** l'HC-SR04 estàndard treballa a 5 V; alguns mòduls retornen l'eco també a 5 V, que pot excedir el que admet un pin de la micro:bit (3,3 V lògics). Si el teu mòdul concret ho fa, munta un **divisor de tensió** (dues resistències) abans de l'echo, tal com indiqui la fitxa del component Keyestudio; si el mòdul del Kit 2 ja porta l'adaptació feta al connector *block*, no cal res més. Consulta-ho amb el docent abans de connectar-ho la primera vegada.

## 3. Pins EXACTES de la mascota (Sessió 3 — producte, cablatge del dossier)

El [dossier del Projecte T1 · La mascota](../00_General/00_Projecte_T1_Mascota.md) defineix el cablatge **definitiu i vinculant**: el programa `mascota_reactiva.py` s'hi ha d'ajustar exactament, no als pins temporals de la taula anterior.

| Component de la mascota | Pin | Tipus | Es programa a `mascota_reactiva.py`? |
|---|---|---|---|
| Micro servo (orelles/cua) | **P0** | PWM | No (es programa a la **SA4**; avui només és a la caixa). |
| LED / LED RGB (indicador d'humor) | **P1** | Digital/PWM | Sí (canvia amb l'emoció). |
| Brunzidor | **P2** | PWM | Sí (so de cada emoció). |
| Sensor PIR | **P8** | Digital | Sí (detecta presència → CURIÓS). |
| Polsador (carícia) | **P12** | Digital, *pull-up* + antirebot | Sí (calma la mascota). |
| Sensor de so (micròfon) | **P4** analògic, o `microphone.sound_level()` intern | Analògic / intern | Sí (soroll fort → ESPANTAT); el codi model fa servir el **micròfon integrat** de la V2 (alternativa vàlida a cablejar el del Kit 3). |
| DHT11 *(extra opcional)* | **P13** | Digital 1-Wire | No al nucli (ampliació ⭐). |
| Sensor de llum | — | Analògic intern | Sí (`display.read_light_level()`, foscor → ADORMIT). |
| Acceleròmetre | — | Intern (I2C) | Sí (`accelerometer.was_gesture('shake')`). |

> 🔁 **Per què P3/P10/P14/P15 (pràctiques) no coincideixen amb els pins de la mascota:** `nivell_llum`, `termometre` i `alarma_ultrasons` es munten i desmunten com a **exercicis previs** (com a la SA2), amb sensors que **no** formen part del cablatge final de la caixa (l'ultrasò, per exemple, no hi és). Quan arribis a `mascota_reactiva`, torna a l'esquema del dossier: només P1, P2, P8, P12 i, opcionalment, P4/P13.

## 4. Concepte: *pull-up* i antirebot (*debounce*)

Un polsador sense circuit extra "flota" quan no es prem (llegeix valors indeterminats). El **pull-up** intern (`pin.set_pull(pin.PULL_UP)`) fixa la lectura a `1` en repòs i a `0` en prémer. El **rebot mecànic** (el contacte "tremola" microsegons abans d'estabilitzar-se) pot fer que una sola premuda es llegeixi com moltes: l'**antirebot per software** (comparar `running_time()` amb la darrera detecció i ignorar canvis massa seguits) ho corregeix sense maquinari addicional.

## 5. Comprovació ràpida (abans de transferir el codi)

- [ ] Micro:bit **desendollada** mentre es cableja.
- [ ] Cap component analògic fora de P0/P1/P2/P3/P4/P10.
- [ ] HC-SR04 alimentat a **5 V** (no 3,3 V) i echo protegit si el mòdul ho requereix.
- [ ] `mascota_reactiva.py` usa **exactament** els pins del dossier de la mascota (P1, P2, P8, P12).
- [ ] El programa comença amb `from microbit import *` (i `import machine`, `import utime`, `import music` segons el programa).

---

## Simulació al navegador

- ▶ [python.microbit.org](https://python.microbit.org) simula el sensor de llum **intern** (`display.read_light_level()`), la **temperatura interna** (`temperature()`), l'**acceleròmetre** i els **botons A/B**, però **NO** simula cap sensor extern: ni el sensor de llum/temperatura del Kit, ni el PIR, ni el polsador extern, ni l'HC-SR04, ni el micròfon del Kit 3.
- Per programes com `mascota_reactiva.py`, substitueix temporalment un sensor extern (per exemple, el PIR) per `button_a.is_pressed()` per validar la **lògica** al simulador, i recalibra els llindars amb el maquinari real quan en tinguis.
- `alarma_ultrasons.py` (temps de vol de l'HC-SR04) **no es pot simular de cap manera**: cal maquinari real des del primer moment.

> Detall del procediment de transferència i limitacions generals del simulador: [`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md) §2.
