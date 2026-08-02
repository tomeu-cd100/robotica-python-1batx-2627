# ⚡ Repàs exprés · MicroPython («Python flash»)

> **Per a qui és?** Per a l'**alumnat**, com a **deures de final de curs** (es reparteix a la SA9, abans de la prova pràctica T3). És una targeta d'**autoestudi amb repàs actiu**: primer **escriu la resposta de memòria** al quadern o en un paper, i només després obre la solució per comprovar-la. Si l'encertes sense mirar, passa a la següent; si falles, repassa la secció indicada de [`SA0_guia_programacio.md`](../SA0/SA0_guia_programacio.md) i torna-ho a intentar l'endemà (el repàs espaiat funciona així).

**Com s'usa:** 10-15 minuts per tanda, màxim 3-4 reptes per dia. No cal placa: pots comprovar el codi al [simulador](https://python.microbit.org/v/3). En paper, les solucions surten impreses: tapa-les amb una targeta o un full doblegat.

---

## R1 · L'esquelet de tot programa (A1-A2)

**Escriu de zero** un programa que mostri el teu nom lletra a lletra, esperi mig segon i acabi mostrant `Image.HAPPY`.

<details markdown="1">
<summary>Solució</summary>

```python
from microbit import *

display.scroll("Aina")
sleep(500)
display.show(Image.HAPPY)
```

Recorda: sense la primera línia (`import`) **res** de `display`, `sleep` ni `Image` existeix. `scroll` = text que passa; `show` = imatge o caràcter fix.
</details>

## R2 · Parpelleig etern (A3-A4)

**Escriu de memòria** el programa que fa parpellejar el LED de **P1**: mig segon encès, mig segon apagat, per sempre.

<details markdown="1">
<summary>Solució</summary>

```python
from microbit import *

while True:
    pin1.write_digital(1)
    sleep(500)
    pin1.write_digital(0)
    sleep(500)
```

Els dos `sleep` són imprescindibles: sense ells el LED canvia tan de pressa que sembla sempre encès. Tot el que ha de passar «per sempre» va **dins** (indentat) del `while True:`.
</details>

## R3 · Decisió amb llindar (A5-A6)

Tens `llum = display.read_light_level()` (0-255) dins del bucle. Escriu l'`if/else` perquè el LED de P1 s'encengui quan `llum < 50` i s'apagui altrament. **(b)** I si el sensor fos extern, llegit amb `pin0.read_analog()`: entre quins valors es mouria la lectura?

<details markdown="1">
<summary>Solució</summary>

```python
while True:
    llum = display.read_light_level()
    if llum < 50:
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)
    sleep(200)
```

**(b)** `read_analog()` va de **0 a 1023** (i `read_light_level()`, de 0 a 255 — no els confonguis a la prova). La lectura va **dins** del bucle: llegir → decidir → actuar, a cada volta.
</details>

## R4 · Funció amb paràmetre (A7)

Escriu una funció `avancar(velocitat)` que faci girar el motor M1 a la velocitat rebuda. Després crida-la a mitja velocitat.

<details markdown="1">
<summary>Solució</summary>

```python
M1_ENDAVANT = pin13
M1_ENRERE = pin14

def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)

avancar(512)
```

L'error clàssic és escriure un número fix dins la funció: aleshores el paràmetre no serveix de res. La gràcia de `velocitat` és que **cada crida** pot ser diferent: `avancar(512)`, `avancar(1023)`…
</details>

## R5 · Funció que retorna un valor (A7)

Escriu una funció `hi_ha_foscor()` que llegeixi la llum i **retorni** `True` si està per sota de 50, i `False` altrament. Escriu també la línia del bucle principal que la fa servir per encendre el LED de P1.

<details markdown="1">
<summary>Solució</summary>

```python
def hi_ha_foscor():
    return display.read_light_level() < 50

while True:
    if hi_ha_foscor():
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)
    sleep(200)
```

`return` **envia el resultat** a qui ha fet la crida (aquí, directament un booleà). Una funció amb `return` no mostra res per si sola: el valor es fa servir a la condició.
</details>

## R6 · `for` sobre una llista (SA5 — repàs: `mostra_historic()`)

Tens `notes = [523, 587, 659]`. Escriu el bucle que fa sonar cada freqüència mig segon amb `music.pitch(freq, 500)`.

<details markdown="1">
<summary>Solució</summary>

```python
import music

notes = [523, 587, 659]
for freq in notes:
    music.pitch(freq, 500)
```

El `for` recorre la llista **element a element**: a cada volta, `freq` val el següent valor. Res d'índexs a mà si no els necessites.
</details>

## R7 · `try/except` per no petar (SA7 — repàs: `mesura_distancia()`)

Tens `text = "37"` (un número que arriba com a **text**). Escriu el bloc que el converteix a enter amb `int(text)` i, si la conversió falla (el text no és un número), mostra `Image.SAD` en lloc de deixar que el programa peti.

<details markdown="1">
<summary>Solució</summary>

```python
try:
    valor = int(text)
    display.scroll(valor)
except ValueError:
    display.show(Image.SAD)
```

`int("hola")` llança un `ValueError` i **atura el programa** si ningú no el captura. El `try/except` és el cinturó de seguretat: el cas bo va al `try`, el pla B a l'`except`.
</details>

---

> Has fallat 2 o més reptes del mateix tema? Per a R1-R5, rellegeix la secció (A1-A7) de [`SA0_guia_programacio.md`](../SA0/SA0_guia_programacio.md) indicada al títol; per a R6, torna a l'activitat nucli del `for` de la fitxa SA5; per a R7, a l'EXPLICACIO d'`evita_obstacles` (SA7). Repeteix només aquells reptes demà. La part de **ràdio** té targeta pròpia: [`00_Repas_expres_Radio.md`](00_Repas_expres_Radio.md).
