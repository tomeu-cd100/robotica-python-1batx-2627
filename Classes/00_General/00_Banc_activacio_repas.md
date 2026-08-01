# 00 · Banc d'activació amb repàs espaiat (katas)

> **Per a qui és?** Per al **docent**. Un banc de **katas curtes (10' o menys)** per a la fase d'**Activació** de cada sessió, de la S4 a la S33 (`Programació didàctica/04_Metodologia.md` §4.2, `06_Avaluacio_criteris_qualificacio.md`). Substitueix la pregunta oberta habitual d'aquella franja per un exercici curt d'**escriptura de codi** sobre un concepte de fa 1-2 setmanes. **No qualifica**: és repàs espaiat + fluïdesa d'escriptura, no avaluació.

## El problema que resol

L'alumnat llegeix i modifica codi amb solvència, però té poca pràctica d'**escriure'n de zero**: la producció autònoma viu sobretot als reptes opcionals i a SA9. Aquest banc obliga TOTHOM a escriure unes línies de codi cada sessió, sobre material que ja es va explicar fa temps (no el d'avui): és **repàs espaiat** (retrieval practice) i **fluïdesa** alhora.

## Regla d'or: repàs espaiat

Cada kata repassa un concepte **de fa 1-2 setmanes**, mai el que es treballa aquell mateix dia (això ja el cobreix el Modelatge/PRIMM de la sessió). El curs avança a raó d'~1 sessió/setmana, així que "1-2 setmanes" equival, a la pràctica, a "com a mínim la sessió anterior, normalment 2-4 sessions enrere".

## Progressió per concepte

| Aparició del concepte al banc | Tipus de kata | Què fa l'alumnat |
|---|---|---|
| 1a vegada | **Parsons** | Rep les línies del programa desordenades i les ha d'ordenar (amb la indentació correcta). |
| 2a vegada | **Completar buits** | Rep el programa gairebé complet, amb `___` en els punts clau (paraules clau, condicions, noms). |
| 3a vegada o més | **Escriure de zero** | Rep només l'enunciat (i, si cal, un esquelet mínim). Escriu 2-6 línies pel seu compte. |

La taula de la secció «Mapa sessió → kata» indica, per a cada kata, quina és la seva posició dins d'aquesta progressió.

## Com s'usa (10')

1. Projecta o imprimeix **només l'enunciat** de la kata del dia (mai la solució).
2. Cronometra 8-10': individual, en paper o a l'editor, **sense apunts**.
3. Correcció **a mà alçada** en 30 segons per alumne, amb el criteri de la fitxa (no es puntua ni es registra com a nota).
4. Si un concepte falla de manera massiva (més d'un terç de la classe), és un avís per revisar-lo abans de la propera prova (`06_Avaluacio_criteris_qualificacio.md`).

> ⚠️ **Dies sense kata.** No hi ha kata els dies de **prova pràctica** (S11, S22, S34: l'activació d'aquell dia és repàs lliure/dubtes). Als dies amb **mini-check individual**, cal mirar la guia docent sessió a sessió: a la majoria la fila **Activació (10')** és **independent** de la fila «Mini-check» (SA2-S2, SA3-S2, SA4-S2, SA5-S2), així que **sí que hi ha kata**. Només a **S20 (SA6-S2), S24 (SA7-S2), S28 (SA8-S2) i S31 (SA9-S2)** la guia docent té **una única fila «Mini-check»** que ocupa tota la franja inicial, sense cap fila «Activació» separada: només aquests quatre dies **no** tenen kata per aquest motiu (`00_Mini_checks_individuals.md` §Rutina, punt 1). Tampoc n'hi ha a **S15** (fabricació pura del vehicle, sense fase d'Activació pròpia a la guia). **S32 i S33** (SA9-S3/S4) sí que tenen kata des de la tercera ronda de millores: com que són les últimes sessions abans de la prova pràctica T3 (S34) i cap concepte post-SA4 (return, try/except, for-col·lecció, FSM, ràdio, llistes) arribava mai al nivell «escriure de zero», s'hi ha afegit una fila **Activació (10')** de **repàs combinat** (3 mini-katas curtes en lloc d'una), retallant 10' d'una altra fase de la mateixa sessió perquè el total no superi les 2 h (vegeu `SA9_guia_docent.md`).

## Conceptes coberts

variables · `while`/`if`/`elif` · `for` amb `range` · condicionals amb sensors/llindar · funcions (`def`, paràmetres) · `return` · `global` · llistes · `for` sobre una col·lecció · ràdio (`radio.send`/`radio.receive`) · diccionaris / FSM · `log` · `try`/`except`.

> Els conceptes **`for` sobre col·lecció** i **`try`/`except`** ja no s'estrenen a SA8 (Task 2 del pla de millora pedagògica, fet): `for element in col·lecció` s'escriu per primer cop a **SA5-S1** (`mostra_historic()` de `radio_missatges.py`) i `try`/`except` a **SA7-S3** (`mesura_distancia()` de `evita_obstacles.py`, lectura robusta de l'HC-SR04). Les katas K13 (S25, SA7-S3) i K14 (S26, SA7-S4) ja tenen, doncs, el concepte explicat abans de repassar-lo.

---

## Mapa sessió → kata

| Sessió | SA · Sessió | Kata | Concepte | Tipus |
|---|---|---|---|---|
| S4 | SA2 · S1 | [K01](#k01--s4--ifwhile--parsons) | if/while | Parsons |
| S5 | SA2 · S2 | [K18](#k18--s5--ifwhile--completar-buits) | if/while | Completar buits |
| S6 | SA2 · S3 | [K02](#k02--s6--variables--parsons) | variables | Parsons |
| S7 | SA2 · S4 | [K03](#k03--s7--for-range--parsons) | for-range | Parsons |
| S8 | SA3 · S1 | [K04](#k04--s8--ifwhile--escriure-de-zero) | if/while | Escriure de zero |
| S9 | SA3 · S2 | [K19](#k19--s9--variables--completar-buits) | variables | Completar buits |
| S10 | SA3 · S3 | [K05](#k05--s10--condicionals-amb-sensorsllindar--parsons) | condicionals amb sensors/llindar | Parsons |
| S11 | SA3 · S4 | — | *(prova pràctica T1: repàs lliure)* | — |
| S12 | SA4 · S1 | [K06](#k06--s12--ifwhile--escriure-de-zero) | if/while | Escriure de zero |
| S13 | SA4 · S2 | [K20](#k20--s13--condicionals-amb-sensorsllindar--completar-buits) | condicionals amb sensors/llindar | Completar buits |
| S14 | SA4 · S3 | [K07](#k07--s14--funcionsparametres--parsons) | funcions/paràmetres | Parsons |
| S15 | SA4 · S4 | — | *(fabricació del vehicle: sense fase d'Activació a la guia)* | — |
| S16 | SA5 · S1 | [K08](#k08--s16--return--parsons) | return | Parsons |
| S17 | SA5 · S2 | [K21](#k21--s17--funcionsparametres--completar-buits) | funcions/paràmetres | Completar buits |
| S18 | SA5 · S3 | [K09](#k09--s18--global--parsons) | global | Parsons |
| S19 | SA6 · S1 | [K10](#k10--s19--radio--parsons) | ràdio | Parsons |
| S20 | SA6 · S2 | — | *(mini-check SA6, substitueix l'activació)* | — |
| S21 | SA6 · S3 | [K11](#k11--s21--llistes--parsons) | llistes | Parsons |
| S22 | SA6 · S4 | — | *(prova pràctica T2: repàs lliure)* | — |
| S23 | SA7 · S1 | [K12](#k12--s23--fsmdiccionari--parsons) | FSM/diccionari | Parsons |
| S24 | SA7 · S2 | — | *(mini-check SA7, substitueix l'activació)* | — |
| S25 | SA7 · S3 | [K13](#k13--s25--for-sobre-col·lecció--parsons) | for sobre col·lecció | Parsons |
| S26 | SA7 · S4 | [K14](#k14--s26--tryexcept--parsons) | try/except | Parsons |
| S27 | SA8 · S1 | [K15](#k15--s27--log--parsons) | log | Parsons |
| S28 | SA8 · S2 | — | *(mini-check SA8, la guia no té fase d'Activació aquell dia)* | — |
| S29 | SA8 · S3 | [K16](#k16--s29--funcionsparametres--escriure-de-zero) | funcions/paràmetres | Escriure de zero |
| S30 | SA9 · S1 | [K17](#k17--s30--return--completar-buits) | return | Completar buits |
| S31 | SA9 · S2 | — | *(mini-check SA9, la guia no té fase d'Activació aquell dia)* | — |
| S32 | SA9 · S3 | [K22](#k22--s32--tryexcept--completar-buits) · [K23](#k23--s32--llistes--completar-buits) · [K24](#k24--s32--for-sobre-col·lecció--completar-buits) | try/except · llistes · for sobre col·lecció | Repàs combinat (3 mini-katas), completar buits |
| S33 | SA9 · S4 | [K25](#k25--s33--ràdio--completar-buits) · [K26](#k26--s33--fsmdiccionari--completar-buits) · [K27](#k27--s33--return--completar-buits) | ràdio · FSM/diccionari · return | Repàs combinat (3 mini-katas), completar buits |
| S34 | SA9 · S5 | — | *(prova pràctica T3: repàs lliure)* | — |

---

## Les katas

### K01 · S4 — if/while — Parsons

**Repassa:** el `while True:` + `if/elif/else` amb botons de SA1 (`emocions_botons.py`).

**Enunciat per a l'alumnat:**
> Aquestes línies formen un programa vàlid però estan **desordenades**. Escriu-les en l'ordre correcte, amb la indentació que toqui, perquè: mentre es manté premut el botó A es mostri una cara contenta, i en cas contrari una cara adormida, per sempre.
> ```
> sleep(100)
> from microbit import *
> while True:
> if button_a.is_pressed():
> display.show(Image.HAPPY)
> else:
> display.show(Image.ASLEEP)
> ```

**Solució completa:**
```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    else:
        display.show(Image.ASLEEP)
    sleep(100)
```

**Correcció ràpida (30''):** `while True:` amb dos punts i tot el cos indentat sota seu · `if`/`else` alineats entre ells i indentats un nivell més · `sleep(100)` dins del bucle (no abans de `while`).

---

### K18 · S5 — if/while — Completar buits

**Repassa:** 2a aparició d'aquest concepte al banc (K01 Parsons a S4): el gest de sacsejada de `dau_sacseig.py` (SA1), en lloc dels botons.

**Enunciat per a l'alumnat:**
> Completa els `___` perquè, en sacsejar la placa, el programa mostri un número de dau (1-6) a l'atzar.
> ```python
> from microbit import *
> import random
>
> while ___:
>     if accelerometer.was_gesture("shake"):
>         numero = random.randint(1, ___)
>         display.show(___(numero))
>         sleep(1000)
> ```

**Solució completa:**
```python
from microbit import *
import random

while True:
    if accelerometer.was_gesture("shake"):
        numero = random.randint(1, 6)
        display.show(str(numero))
        sleep(1000)
```

**Correcció ràpida (30''):** `while True:` (no `1` ni cap altra cosa) · `random.randint(1, 6)` amb el límit superior **6** (un dau) · `str(numero)` abans de `show()`.

---

### K02 · S6 — variables — Parsons

**Repassa:** l'acumulador (`comptador`) inicialitzat fora del bucle de `led_parpelleig.py` (SA2).

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè el programa compti les sacsejades de la placa i mostri el comptador cada cop que en detecta una.
> ```
> sleep(100)
> comptador = 0
> from microbit import *
> while True:
> comptador = comptador + 1
> display.show(str(comptador))
> if accelerometer.was_gesture("shake"):
> ```

**Solució completa:**
```python
from microbit import *

comptador = 0

while True:
    if accelerometer.was_gesture("shake"):
        comptador = comptador + 1
        display.show(str(comptador))
    sleep(100)
```

**Correcció ràpida (30''):** `comptador = 0` **fora** i **abans** del `while` (s'inicialitza un sol cop) · `comptador = comptador + 1` dins de l'`if`, no fora · `str(comptador)` abans de `show()`.

---

### K03 · S7 — for-range — Parsons

**Repassa:** el `for i in range(vegades):` de `funcions_moviments.py` (`saluda()`, SA4 — aquí encara sense funció, en context de SA2).

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè una cara contenta parpellegi exactament **5 vegades** fent servir un `for`.
> ```
> sleep(300)
> display.clear()
> from microbit import *
> VEGADES = 5
> sleep(300)
> for i in range(VEGADES):
> display.show(Image.HAPPY)
> ```

**Solució completa:**
```python
from microbit import *

VEGADES = 5

for i in range(VEGADES):
    display.show(Image.HAPPY)
    sleep(300)
    display.clear()
    sleep(300)
```

**Correcció ràpida (30''):** `for i in range(VEGADES):` amb dos punts i les 4 línies del cos indentades igual · cap comptador manual ni `while` · `VEGADES` en majúscules abans del `for` (convenció de constant).

---

### K04 · S8 — if/while — Escriure de zero

**Repassa:** 3a aparició d'aquest concepte al banc (K01 Parsons a S4, K18 completar buits a S5): ara, de zero, amb un cas nou (LED extern en lloc de display).

**Enunciat per a l'alumnat:**
> Sense mirar apunts, completa aquest esquelet (màxim 4 línies noves) perquè el LED del pin **P1** estigui encès mentre es manté premut el botó A, i apagat en cas contrari.
> ```python
> from microbit import *
>
> while True:
>     # escriu aqui 3-4 linies
>     sleep(50)
> ```

**Solució completa:**
```python
from microbit import *

while True:
    if button_a.is_pressed():
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)
    sleep(50)
```

**Correcció ràpida (30''):** `if`/`else` amb dos punts i indentació correcta dins del `while` · `is_pressed()` amb parèntesis (no `was_pressed`, que només detecta el moment de prémer) · `1` a la branca `if` i `0` a l'`else`, no invertits.

---

### K05 · S10 — condicionals amb sensors/llindar — Parsons

**Repassa:** la comparació amb `LLINDAR_FOSCOR` de `nivell_llum.py` (SA3).

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè el programa mostri una cara adormida quan hi ha poca llum (per sota del llindar) i esborri el display en cas contrari.
> ```
> sleep(200)
> LLINDAR_FOSCOR = 50
> display.clear()
> from microbit import *
> while True:
> llum = display.read_light_level()
> if llum < LLINDAR_FOSCOR:
> display.show(Image.ASLEEP)
> else:
> ```

**Solució completa:**
```python
from microbit import *

LLINDAR_FOSCOR = 50

while True:
    llum = display.read_light_level()
    if llum < LLINDAR_FOSCOR:
        display.show(Image.ASLEEP)
    else:
        display.clear()
    sleep(200)
```

**Correcció ràpida (30''):** `llum = display.read_light_level()` es **llegeix dins del bucle**, a cada volta · la comparació és `llum < LLINDAR_FOSCOR` (el llindar és el segon terme) · `LLINDAR_FOSCOR` es defineix un cop, fora del bucle.

---

### K19 · S9 — variables — Completar buits

**Repassa:** 2a aparició d'aquest concepte al banc (K02 Parsons a S6): l'acumulador `comptador`, ara comptant polsacions del botó A en lloc de parpellejos.

**Enunciat per a l'alumnat:**
> Completa els `___` perquè el programa compti cada vegada que es prem el botó A i mostri el comptador actualitzat.
> ```python
> from microbit import *
>
> comptador = ___
>
> while True:
>     if button_a.was_pressed():
>         comptador = comptador ___ 1
>         display.___(str(comptador))
>     sleep(100)
> ```

**Solució completa:**
```python
from microbit import *

comptador = 0

while True:
    if button_a.was_pressed():
        comptador = comptador + 1
        display.show(str(comptador))
    sleep(100)
```

**Correcció ràpida (30''):** `comptador = 0` **fora** del bucle (s'inicialitza un sol cop) · `comptador = comptador + 1` (acumulador, no un valor fix) · `display.show(...)`, amb `str()` abans.

---

### K06 · S12 — if/while — Escriure de zero

**Repassa:** 4a aparició d'aquest concepte al banc (K01 Parsons a S4, K18 completar buits a S5, K04 escriure de zero a S8): repeteix «escriure de zero» amb un cas nou, com marca la progressió a partir de la 3a vegada.

**Enunciat per a l'alumnat:**
> Sense mirar apunts, completa aquest esquelet (màxim 4 línies noves) perquè es mostri una fletxa cap a la dreta (`Image.ARROW_E`) quan es faci el gest `'right'` amb la placa, i el display s'esborri en cas contrari.
> ```python
> from microbit import *
>
> while True:
>     # escriu aqui 3-4 linies
>     sleep(100)
> ```

**Solució completa:**
```python
from microbit import *

while True:
    if accelerometer.was_gesture('right'):
        display.show(Image.ARROW_E)
    else:
        display.clear()
    sleep(100)
```

**Correcció ràpida (30''):** `if`/`else` amb dos punts i indentació correcta dins del `while` · `was_gesture('right')` ben escrit (cometes, parèntesi) · `display.clear()` a l'`else` (si no hi és, la fletxa es queda encesa per sempre).

---

### K20 · S13 — condicionals amb sensors/llindar — Completar buits

**Repassa:** 2a aparició d'aquest concepte al banc (K05 Parsons a S10): un llindar de temperatura en lloc d'un llindar de llum, com `termometre.py` (SA3).

**Enunciat per a l'alumnat:**
> Completa els `___` perquè el programa mostri una cara de sorpresa quan la temperatura superi els 28 graus, i esborri el display en cas contrari.
> ```python
> from microbit import *
>
> LLINDAR_CALOR = ___
>
> while True:
>     temp = ___()
>     if temp > LLINDAR_CALOR:
>         display.show(Image.SURPRISED)
>     ___:
>         display.clear()
>     sleep(200)
> ```

**Solució completa:**
```python
from microbit import *

LLINDAR_CALOR = 28

while True:
    temp = temperature()
    if temp > LLINDAR_CALOR:
        display.show(Image.SURPRISED)
    else:
        display.clear()
    sleep(200)
```

**Correcció ràpida (30''):** `LLINDAR_CALOR = 28` (un número raonable, no una variable buida) · `temperature()` és la funció que llegeix el sensor intern · `else:` amb dos punts, mateixa indentació que l'`if`.

---

### K07 · S14 — funcions/paràmetres — Parsons

**Repassa:** `def` amb un paràmetre, de `funcions_moviments.py` (`saluda(vegades)`, taught S12).

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè defineixin una funció `saluda(vegades)` que repeteix un gest content tantes vegades com li digui el paràmetre, i que després es cridi 3 vegades.
> ```
> saluda(3)
> display.clear()
> sleep(300)
> def saluda(vegades):
> sleep(300)
> for i in range(vegades):
> display.show(Image.HAPPY)
> ```

**Solució completa:**
```python
def saluda(vegades):
    for i in range(vegades):
        display.show(Image.HAPPY)
        sleep(300)
        display.clear()
        sleep(300)


saluda(3)
```

**Correcció ràpida (30''):** `def saluda(vegades):` amb dos punts i el cos indentat **sota** el `def` · la crida `saluda(3)` va **fora** de la funció (sense indentar), amb parèntesis i un valor concret.

---

### K08 · S16 — return — Parsons

**Repassa:** `graus_a_pwm(angle)`, la primera funció **amb valor de retorn** del curs (`funcions_moviments.py`, SA4 S1/S3).

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè una funció converteixi un angle (0-180°) al valor PWM que espera un servomotor, i mostri el resultat per a un angle de 90°.
> ```
> valor = graus_a_pwm(90)
> def graus_a_pwm(angle):
> display.scroll(str(valor))
> return 26 + (angle * (128 - 26)) // 180
> ```

**Solució completa:**
```python
def graus_a_pwm(angle):
    return 26 + (angle * (128 - 26)) // 180


valor = graus_a_pwm(90)
display.scroll(str(valor))
```

**Correcció ràpida (30''):** `return` és la **darrera** línia del cos de la funció (calcula i torna un valor, no mostra res) · `valor = graus_a_pwm(90)` recull el que retorna la funció · `str(valor)` abans de `scroll()`.

---

### K21 · S17 — funcions/paràmetres — Completar buits

**Repassa:** 2a aparició d'aquest concepte al banc (K07 Parsons a S14): una funció amb un paràmetre que decideix quina fletxa mostrar, com les funcions de moviment de `funcions_moviments.py`/`velocitat_pwm.py` (SA4).

**Enunciat per a l'alumnat:**
> Completa els `___` perquè la funció mostri una fletxa cap a l'esquerra o cap a la dreta segons el paràmetre rebut, i crida-la amb `'dreta'`.
> ```python
> def mostra_fletxa(costat):
>     if costat == 'esquerra':
>         display.show(___)
>     elif costat == ___:
>         display.show(Image.ARROW_E)
>
>
> ___('dreta')
> ```

**Solució completa:**
```python
def mostra_fletxa(costat):
    if costat == 'esquerra':
        display.show(Image.ARROW_W)
    elif costat == 'dreta':
        display.show(Image.ARROW_E)


mostra_fletxa('dreta')
```

**Correcció ràpida (30''):** el paràmetre `costat` es compara amb un text entre cometes (`'esquerra'`/`'dreta'`), no amb un número · el cos de la funció va indentat sota `def` · la crida final `mostra_fletxa('dreta')` és fora de la funció, amb parèntesis i cometes.

---

### K09 · S18 — global — Parsons

**Repassa:** `canvia_emocio()` de `mascota_reactiva.py` (SA3, S8-S10), la primera funció del curs que canvia amb `global` una variable definida fora seu.

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè una funció canviï una variable `emocio` definida fora d'ella, i mostri el nou valor.
> ```
> canvia_emocio(1)
> emocio = 0
> global emocio
> def canvia_emocio(nova):
> display.show(str(emocio))
> emocio = nova
> ```

**Solució completa:**
```python
emocio = 0


def canvia_emocio(nova):
    global emocio
    emocio = nova
    display.show(str(emocio))


canvia_emocio(1)
```

**Correcció ràpida (30''):** `emocio = 0` es defineix **fora** de la funció, abans de tot · `global emocio` és la **primera** línia dins del cos de la funció (abans de tocar-la) · la crida `canvia_emocio(1)` és fora de la funció.

---

### K10 · S19 — ràdio — Parsons

**Repassa:** `radio.on()`/`radio.config()`/`radio.send()`/`radio.receive()` de `radio_missatges.py` (SA5 S1).

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè el programa enviï "Hola" en prémer el botó A, i mostri qualsevol missatge que arribi.
> ```
> radio.on()
> import radio
> sleep(20)
> radio.config(group=5)
> if button_a.was_pressed():
> while True:
> radio.send("Hola")
> missatge = radio.receive()
> if missatge is not None:
> display.scroll(missatge)
> ```

**Solució completa:**
```python
from microbit import *
import radio

radio.on()
radio.config(group=5)

while True:
    if button_a.was_pressed():
        radio.send("Hola")
    missatge = radio.receive()
    if missatge is not None:
        display.scroll(missatge)
    sleep(20)
```

**Correcció ràpida (30''):** `radio.on()` i `radio.config()` es criden **un sol cop, fora** del bucle · `radio.receive()` **pot tornar `None`**: cal comprovar-ho abans de fer-hi res.

---

### K11 · S21 — llistes — Parsons

**Repassa:** l'`historic` (`append()`/`pop(0)`) de `radio_missatges.py` (SA5 S1).

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè una funció guardi missatges en una llista, però descarti sempre el més antic quan ja n'hi hagi més de `MAX`.
> ```
> desa("A")
> historic = []
> historic.append(missatge)
> MAX = 3
> def desa(missatge):
> historic.pop(0)
> if len(historic) > MAX:
> desa("B")
> ```

**Solució completa:**
```python
historic = []
MAX = 3


def desa(missatge):
    historic.append(missatge)
    if len(historic) > MAX:
        historic.pop(0)


desa("A")
desa("B")
```

**Correcció ràpida (30''):** `historic = []` i `MAX = 3` es defineixen **fora** de la funció, abans de tot · `append()` és sempre la primera acció dins de `desa()` · `pop(0)` treu el **primer** element (el més antic), no el darrer.

---

### K12 · S23 — FSM/diccionari — Parsons

**Repassa:** el diccionari `TRANSICIONS` de `maquina_estats_semafor.py` (SA6 S1).

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè una petita màquina d'estats alterni "encès"/"apagat" cada segon, fent servir un diccionari de transicions.
> ```
> sleep(1000)
> estat = APAGAT
> canvia()
> ENCES, APAGAT = range(2)
> global estat
> TRANSICIONS = {ENCES: APAGAT, APAGAT: ENCES}
> def canvia():
> while True:
> estat = TRANSICIONS[estat]
> display.show(str(estat))
> ```

**Solució completa:**
```python
ENCES, APAGAT = range(2)
estat = APAGAT

TRANSICIONS = {ENCES: APAGAT, APAGAT: ENCES}


def canvia():
    global estat
    estat = TRANSICIONS[estat]
    display.show(str(estat))


while True:
    canvia()
    sleep(1000)
```

**Correcció ràpida (30''):** `TRANSICIONS[estat]` retorna directament el **següent** estat (no cal cap `if/elif`) · `global estat` dins de `canvia()` · el `while True:` només crida `canvia()` i espera; tota la lògica de transició viu al diccionari.

---

### K13 · S25 — for sobre col·lecció — Parsons

**Repassa:** `for missatge in historic:` de `mostra_historic()` (`radio_missatges.py`, SA5-S1), ara en el context de les mesures de distància del rover: iterar directament sobre els elements d'una llista, en lloc d'un índex.

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè el programa recorri una llista de distàncies mesurades i mostri un avís cada cop que una és inferior a 10 cm.
> ```
> sleep(300)
> distancies = [12, 8, 20, 5]
> display.clear()
> for d in distancies:
> display.show("!")
> if d < 10:
> else:
> ```

**Solució completa:**
```python
distancies = [12, 8, 20, 5]

for d in distancies:
    if d < 10:
        display.show("!")
    else:
        display.clear()
    sleep(300)
```

**Correcció ràpida (30''):** `for d in distancies:` recorre els **valors** directament (sense `range(len(...))` ni índex) · tot el cos (`if/else` i `sleep`) va indentat dins del `for`.

---

### K14 · S26 — try/except — Parsons

**Repassa:** `try`/`except OSError` de `mesura_distancia()` (`evita_obstacles.py`, SA7-S3), ara en el context de convertir de manera segura un text rebut a número, sense que un valor inesperat aturi el programa.

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè el programa intenti convertir un missatge a número i, si no ho aconsegueix, mostri una "E" d'error en lloc d'aturar-se.
> ```
> display.show("E")
> valor = int(missatge)
> missatge = "12"
> try:
> display.show(str(valor))
> except ValueError:
> ```

**Solució completa:**
```python
missatge = "12"

try:
    valor = int(missatge)
    display.show(str(valor))
except ValueError:
    display.show("E")
```

**Correcció ràpida (30''):** `try:` i `except ValueError:` van al **mateix nivell** d'indentació · el codi que **pot fallar** (`int(missatge)`) va dins del `try`, no dins de l'`except` · el missatge d'error només s'executa si falla la conversió.

---

### K15 · S27 — log — Parsons

**Repassa:** `log.set_labels()`/`log.add()` de `registre_dades.py` (SA6 S2).

**Enunciat per a l'alumnat:**
> Ordena aquestes línies perquè el programa registri la temperatura i la llum cada 2 segons amb el mòdul `log` de la micro:bit.
> ```
> sleep(2000)
> import log
> log.set_labels('temp', 'llum')
> log.add(temp=temperature(), llum=display.read_light_level())
> while True:
> ```

**Solució completa:**
```python
import log

log.set_labels('temp', 'llum')

while True:
    log.add(temp=temperature(), llum=display.read_light_level())
    sleep(2000)
```

**Correcció ràpida (30''):** `log.set_labels()` es crida **un sol cop, abans** del bucle · `log.add()` fa servir els **mateixos noms** de columna (`temp`, `llum`) que `set_labels()` · `sleep(2000)` dins del bucle marca la cadència.

---

### K16 · S29 — funcions/paràmetres — Escriure de zero

**Repassa:** 3a aparició d'aquest concepte al banc (K07 Parsons a S14, K21 completar buits a S17): funció amb **dos** paràmetres, un d'ells amb **valor per defecte**, com `girar(costat, velocitat=300)` de `segueix_linia.py`/`telemetria_radio.py`. **Variant a propòsit** del mini-check individual de la SA4 (que demana `avancar(velocitat)`, un sol paràmetre sense valor per defecte): aquí es repassa un cas diferent, no el mateix ítem.

**Enunciat per a l'alumnat:**
> Sense mirar apunts, escriu (4-6 línies) una funció `girar(costat, velocitat=300)` que faci girar el motor M1 (pins P13/P14) a la velocitat rebuda si `costat` val `'esquerra'`, i el motor M2 (pins P15/P16) si val `'dreta'`. Crida-la un cop passant els dos arguments, i un altre cop **sense** indicar la velocitat (per comprovar que fa servir el valor per defecte).

**Solució completa:**
```python
def girar(costat, velocitat=300):
    if costat == 'esquerra':
        pin13.write_analog(velocitat)
        pin14.write_digital(0)
    elif costat == 'dreta':
        pin15.write_analog(velocitat)
        pin16.write_digital(0)


girar('esquerra', 400)
girar('dreta')
```

**Correcció ràpida (30''):** `def girar(costat, velocitat=300):` amb el valor per defecte **al paràmetre**, no a la crida · `if`/`elif` compara `costat` amb un text entre cometes · `girar('dreta')` (sense segon argument) fa servir automàticament `300`, no peta ni cal repetir-lo.

---

### K17 · S30 — return — Completar buits

**Repassa:** 2a aparició d'aquest concepte (K08 Parsons): una funció que retorna un text segons una condició, com `NOMS_MISSIO`/classificacions de `rover_missions.py`.

**Enunciat per a l'alumnat:**
> Completa els `___` perquè la funció classifiqui una distància com a `"PROP"` (menys de 15 cm) o `"LLUNY"` (la resta), i mostri el resultat de classificar 10.
> ```python
> def classifica(distancia):
>     if distancia < 15:
>         return "PROP"
>     else:
>         return ___
>
>
> resultat = ___(10)
> display.scroll(str(resultat))
> ```

**Solució completa:**
```python
def classifica(distancia):
    if distancia < 15:
        return "PROP"
    else:
        return "LLUNY"


resultat = classifica(10)
display.scroll(str(resultat))
```

**Correcció ràpida (30''):** cada branca (`if` i `else`) té el seu propi `return` amb un text diferent · la crida `classifica(10)` es fa amb parèntesis i s'assigna a `resultat` · `str(resultat)` abans de `scroll()`.

---

## Repàs combinat pre-T3 (K22-K27)

Sis katas noves, afegides a la tercera ronda de millores perquè cap concepte post-SA4 arribava mai al nivell «escriure de zero» (return, try/except, for-col·lecció, FSM, ràdio i llistes es quedaven a Parsons o completar buits). Es fan a **S32 i S33** (SA9-S3/S4), les dues últimes sessions abans de la prova pràctica T3: **tres mini-katas molt curtes** (2-3' cadascuna) en una única fila «Activació (10')», en lloc d'una de sola, com a repàs espaiat intensiu de tancament de curs.

### K22 · S32 — try/except — Completar buits

**Repassa:** 2a aparició d'aquest concepte al banc (K14 Parsons a S26): ara convertint a número un missatge rebut per ràdio, com `llegeix_dht11()`/`mesura_distancia()`.

**Enunciat per a l'alumnat:**
> Completa els `___` perquè el programa intenti convertir a número el missatge rebut per ràdio i, si no ho aconsegueix, mostri `"E"` en lloc d'aturar-se.
> ```python
> missatge = radio.receive()
> if missatge is not None:
>     ___:
>         valor = int(missatge)
>         display.scroll(str(valor))
>     except ___:
>         display.show("E")
> ```

**Solució completa:**
```python
missatge = radio.receive()
if missatge is not None:
    try:
        valor = int(missatge)
        display.scroll(str(valor))
    except ValueError:
        display.show("E")
```

**Correcció ràpida (30''):** `try:` i `except ValueError:` van al **mateix** nivell d'indentació, dins de l'`if` · `int(missatge)` (que pot fallar) va dins del `try` · `display.show("E")` només s'executa si la conversió falla.

---

### K23 · S32 — llistes — Completar buits

**Repassa:** 2a aparició d'aquest concepte al banc (K11 Parsons a S21): ara buscant el valor màxim d'una llista de temperatures, com el seguiment de màxim/mínim d'`estacio_base.py` (SA8).

**Enunciat per a l'alumnat:**
> Completa els `___` perquè la funció retorni el valor més alt d'una llista de temperatures.
> ```python
> def maxim(llista):
>     valor_maxim = llista[0]
>     for valor in ___:
>         if valor > ___:
>             valor_maxim = valor
>     return ___
>
>
> temperatures = [21, 25, 19, 28, 22]
> display.scroll(str(maxim(___)))
> ```

**Solució completa:**
```python
def maxim(llista):
    valor_maxim = llista[0]
    for valor in llista:
        if valor > valor_maxim:
            valor_maxim = valor
    return valor_maxim


temperatures = [21, 25, 19, 28, 22]
display.scroll(str(maxim(temperatures)))
```

**Correcció ràpida (30''):** `valor_maxim` s'inicialitza amb el **primer** element (`llista[0]`), no amb `0` (una llista de negatius fallaria) · `for valor in llista:` recorre els **valors**, no índexs · `return valor_maxim` és la darrera línia de la funció.

---

### K24 · S32 — for sobre col·lecció — Completar buits

**Repassa:** 2a aparició d'aquest concepte al banc (K13 Parsons a S25): ara comptant quantes distàncies d'una llista són de perill, en lloc de només mostrar un avís.

**Enunciat per a l'alumnat:**
> Completa els `___` perquè la funció compti quantes distàncies d'una llista són inferiors a 10.
> ```python
> def compta_perill(distancies):
>     comptador = ___
>     for d in ___:
>         if d < ___:
>             comptador = comptador + 1
>     return comptador
>
>
> mesures = [12, 8, 5, 20, 9]
> display.scroll(str(compta_perill(___)))
> ```

**Solució completa:**
```python
def compta_perill(distancies):
    comptador = 0
    for d in distancies:
        if d < 10:
            comptador = comptador + 1
    return comptador


mesures = [12, 8, 5, 20, 9]
display.scroll(str(compta_perill(mesures)))
```

**Correcció ràpida (30''):** `comptador = 0` **abans** del `for` (acumulador, un sol cop) · `for d in distancies:` recorre els valors directament · `comptador = comptador + 1` només dins de l'`if`.

---

### K25 · S33 — ràdio — Completar buits

**Repassa:** 2a aparició d'aquest concepte al banc (K10 Parsons a S19): ara amb un protocol amb prefix `"CMD:"`, com `semafor_rele.py`/`vehicle_seguretat.py` (SA6), en lloc del xat sense protocol.

**Enunciat per a l'alumnat:**
> Completa els `___` perquè el programa enviï una ordre d'aturada amb prefix `"CMD:"` en prémer A, i la reconegui correctament en rebre-la.
> ```python
> PREFIX = "CMD:"
>
> if button_a.was_pressed():
>     radio.send(___ + "S")
>
> missatge = radio.receive()
> if missatge is not None and missatge.___(PREFIX):
>     ordre = missatge[___:]
>     if ordre == "S":
>         aturar()
> ```

**Solució completa:**
```python
PREFIX = "CMD:"

if button_a.was_pressed():
    radio.send(PREFIX + "S")

missatge = radio.receive()
if missatge is not None and missatge.startswith(PREFIX):
    ordre = missatge[len(PREFIX):]
    if ordre == "S":
        aturar()
```

**Correcció ràpida (30''):** `radio.send(PREFIX + "S")` concatena el prefix davant l'ordre · `startswith(PREFIX)` comprova que el missatge és del protocol esperat **abans** de fer-hi res · `missatge[len(PREFIX):]` talla el prefix per quedar-se amb l'ordre.

---

### K26 · S33 — FSM/diccionari — Completar buits

**Repassa:** 2a aparició d'aquest concepte al banc (K12 Parsons a S23): ara amb **tres** estats (SEGUIR/ESQUIVAR/RECUPERAR, com `comportaments.py`/`telemetria_radio.py`) en lloc de dos.

**Enunciat per a l'alumnat:**
> Completa els `___` perquè la funció canviï d'estat segons el diccionari de transicions de tres estats.
> ```python
> SEGUIR, ESQUIVAR, RECUPERAR = range(3)
> estat = SEGUIR
>
> TRANSICIONS = {SEGUIR: ___, ESQUIVAR: RECUPERAR, RECUPERAR: ___}
>
>
> def seguent_estat():
>     global estat
>     estat = TRANSICIONS[___]
>     return estat
>
>
> display.show(str(seguent_estat()))
> ```

**Solució completa:**
```python
SEGUIR, ESQUIVAR, RECUPERAR = range(3)
estat = SEGUIR

TRANSICIONS = {SEGUIR: ESQUIVAR, ESQUIVAR: RECUPERAR, RECUPERAR: SEGUIR}


def seguent_estat():
    global estat
    estat = TRANSICIONS[estat]
    return estat


display.show(str(seguent_estat()))
```

**Correcció ràpida (30''):** `TRANSICIONS` té una entrada per a **cada** estat, sense buits · `TRANSICIONS[estat]` fa servir l'estat **actual** per trobar el següent · `global estat` abans de reassignar-la dins de la funció.

---

### K27 · S33 — return — Completar buits

**Repassa:** 3a aparició d'aquest concepte al banc (K08 Parsons a S16, K17 completar buits a S30): repeteix el nivell **completar buits** (mida reduïda a propòsit perquè hi càpiga dins d'un terç d'una fila d'Activació de 10'), ara amb **tres** branques de retorn, com les zones de `termostat_histeresi.py`/`nivell_llum.py`.

**Enunciat per a l'alumnat:**
> Completa els `___` perquè la funció retorni `"FRED"` si la temperatura és inferior a 18, `"CALOR"` si és superior a 26, i `"NORMAL"` en la resta de casos.
> ```python
> def zona(temp):
>     if temp ___ 18:
>         return "FRED"
>     elif temp ___ 26:
>         return ___
>     else:
>         return "NORMAL"
>
>
> display.scroll(zona(22))
> ```

**Solució completa:**
```python
def zona(temp):
    if temp < 18:
        return "FRED"
    elif temp > 26:
        return "CALOR"
    else:
        return "NORMAL"


display.scroll(zona(22))
```

**Correcció ràpida (30''):** `temp < 18` i `temp > 26` són comparacions, no assignacions (`<`/`>`, no `=`) · cada branca (`if`/`elif`/`else`) té el seu propi `return` amb un text diferent · només **una** branca s'executa per crida.

---

> Aquest banc l'usen `Programació didàctica/04_Metodologia.md` §4.2 i `06_Avaluacio_criteris_qualificacio.md`, i el criden les guies docents de SA2-SA9 a la franja d'Activació de cada sessió amb la kata que toca. Document intern del curs. Llicència CC BY-SA 4.0.
