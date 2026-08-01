# SA1 · Esquemes i connexions

> 🧑‍🎓 **Quan toca?** Tingues aquesta pàgina oberta durant la **Sessió 2** (Activitat 2, anatomia de la placa). A la SA1 **no hi ha cap muntatge extern**: treballem amb la micro:bit **sola**, sense Micro:shield ni sensors afegits. Aquest document, per tant, és **descriptiu** (anatomia de la placa i connexió mínima), no un esquema de circuit com el de les properes SA.

> A partir de la **SA2** la micro:bit s'encaixa al **Micro:shield** i s'hi connecten sensors i actuadors Keyestudio: aquell dia aquest document tornarà a tenir taules de connexió pin a pin. Per ara, l'única "connexió" del curs és el cable **USB** entre la micro:bit i l'ordinador.

---

## 1. Anatomia de la micro:bit V2 (Activitat 2)

Aquest apartat dona suport a l'**Activitat 2** de la fitxa. Descriu, en taula, cada part física i el seu paper com a **entrada**, **sortida** o **alimentació/comunicació** dins del model E-P-S de la SA1.

### 1.1. Cara frontal

| Part | Tipus | Funció |
|---|---|---|
| **Matriu de 25 LED** (5×5) | Sortida **i** entrada | Mostra text i imatges (`display.show`, `display.scroll`); els mateixos LED també funcionen com a **sensor de llum** (`display.read_light_level()`, valors 0-255): és a la vegada actuador i sensor. |
| **Botó A** (esquerra) | Entrada digital | Dos estats: premut / no premut (`button_a.is_pressed()`). |
| **Botó B** (dreta) | Entrada digital | Dos estats: premut / no premut (`button_b.is_pressed()`). |
| **Logo tàctil** (davant, centre) | Entrada digital | Sensor tàctil capacitiu; detecta si es toca amb el dit (`pin_logo.is_touched()`). |
| **Micròfon + LED indicador** | Entrada | Capta so (`microphone.sound_level()`); el LED petit s'encén quan capta so fort. |
| **Altaveu** | Sortida | Reprodueix sons i melodies (`audio.play`, `music.play`). |

### 1.2. Cara posterior i vores

| Part | Tipus | Funció |
|---|---|---|
| **Microcontrolador** | Procés | El "cervell" de la placa: hi executa el programa MicroPython, línia a línia. |
| **Acceleròmetre** (intern) | Entrada | Detecta moviment i orientació en 3 eixos i gestos (`accelerometer.get_x/y/z()`, `accelerometer.was_gesture("shake")`...). |
| **Brúixola/magnetòmetre** (intern) | Entrada | Detecta el camp magnètic i l'orientació respecte al nord (`compass.heading()`); cal calibrar-lo abans del primer ús. |
| **Sensor de temperatura** (intern) | Entrada | Llegeix la temperatura del xip, en graus (`temperature()`). |
| **Botó de reinici (RESET)** | — | Reinicia el programa (torna a començar des de la primera línia). |
| **LED groc** (part posterior) | Indicador | Parpelleja **mentre es grava** el programa a la placa: no desendollar fins que s'aturi. |
| **Connector USB (micro-USB)** | Alimentació + comunicació | Alimenta la placa i transfereix el programa des de l'ordinador. |
| **Connector de pila (JST)** | Alimentació | Alimentació externa amb 2 piles AAA, per fer anar la placa sense l'ordinador (no cal a la SA1). |
| **Pins d'expansió (edge connector)** | Entrada/sortida | 25 contactes a la vora inferior (grans: 0, 1, 2, 3V, GND; petits: la resta). No s'hi connecta res fins a la **SA2**, quan s'hi encaixi el Micro:shield. |

> 📎 **Vocabulari:** microcontrolador, sensor, actuador i entrada/sortida es defineixen amb exemples de micro:bit a [`SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md).

---

## 2. La "connexió" del primer programa

A la SA1 **no hi ha cap circuit a muntar**: la micro:bit ja porta tot el que cal (display, botons, sensors) integrat a la placa.

| Pas | Acció |
|---|---|
| 1 | Connecta la micro:bit a l'ordinador amb un cable **micro-USB** (apareix com una unitat `MICROBIT`). |
| 2 | Escriu el programa a [python.microbit.org](https://python.microbit.org) (editor o simulador). |
| 3 | Prem **«Baixa»**: es descarrega el fitxer `.hex`. |
| 4 | **Arrossega** el `.hex` a la unitat `MICROBIT`. |
| 5 | El **LED groc** de darrere parpelleja mentre es grava; quan s'atura, el programa nou ja s'executa. |

> Detall complet del procés (alternativa amb Thonny, incidències, Micro:shield): [`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md).

---

## 3. Comprovació ràpida (abans de transferir el codi)

- [ ] El cable USB és de **dades** (n'hi ha que només carreguen i no transfereixen fitxers).
- [ ] La unitat `MICROBIT` apareix a l'explorador de fitxers de l'ordinador.
- [ ] El programa comença amb `from microbit import *`.
- [ ] **No** es desendolla la placa mentre el LED groc parpelleja.

---

## Simulació al navegador

- ▶ **Simulador interactiu:** [python.microbit.org](https://python.microbit.org) — inclou display 5×5, botons A/B i, per a components concrets, acceleròmetre i sensors. És el **pla B** recomanat quan no hi ha placa física disponible o per fer els deures a casa.

> Limitacions del simulador i com fer-hi constar les mesures: vegeu [`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md) §2.
