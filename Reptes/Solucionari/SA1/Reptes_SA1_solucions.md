# SA1 · Solucionari dels reptes — Hola, robot!

> **Material del docent.** Solucions completes dels tres reptes de [`Reptes_SA1.md`](../../Reptes_SA1.md), amb el nucli i les tres ampliacions graduades ja incorporades. **No es reparteix a l'alumnat abans que hagi entregat el seu propi repte**: com l'exemple resolt de la SA, serveix per corregir i, si cal, per mostrar *després* del primer intent.

> Cada solució és una còpia exacta del fitxer `.py` de la seva carpeta (`repte1_targeta/`, `repte2_semafor_humor/`, `repte3_dau_doble/`): si canvies un fitxer, actualitza també el bloc de codi d'aquí sota.

---

## ⭐ Repte 1 · Targeta de benvinguda digital

**Idea de la solució:** el nucli (`hola_mon.py`) ja fa `scroll` + `show`; les ampliacions afegeixen una segona imatge, repetició amb `for`/`while` i una `Image` pròpia construïda amb el patró de 25 dígits.

```python
# SA1 - Repte 1 (SOLUCIO): targeta de benvinguda digital
# Nucli + ampliacions 1-3: segona imatge, repeticio amb while, imatge propia.
# Maquinari: nomes la micro:bit sola.

from microbit import *

NOM = "TOMEU"

# Imatge propia (ampliacio 3): una fletxa senzilla feta amb un patro de 5x5.
# Cada fila son 5 digits de 0 (apagat) a 9 (maxima brillantor), separades per ":".
FLETXA = Image("00900:09990:90909:00900:00900")

while True:
    # Ampliacio 2: repeteix el cicle nom -> imatges 3 vegades amb un while.
    for i in range(3):
        display.scroll(NOM)
        sleep(200)
        display.show(Image.HAPPY)     # Ampliacio 1: primera imatge
        sleep(600)
        display.show(FLETXA)          # Ampliacio 3: imatge propia
        sleep(600)
    sleep(2000)   # Pausa llarga abans de tornar a comencar el cicle sencer
```

**Punts a corregir:** el `NOM` s'ha personalitzat (no ha de quedar "TOMEU"); la `Image` pròpia no és una de predefinida còpia-i-enganxa; el `for`/`while` no repeteix codi enganxat tres cops.

---

## ⭐⭐ Repte 2 · Semàfor d'humor amb tres estats

**Idea de la solució:** cada estat es converteix en una **funció** pròpia; l'ordre dels `if`/`elif` és important (l'estat A+B ha d'anar **abans** que els d'A i B per separat, perquè si no mai s'hi arribaria).

```python
# SA1 - Repte 2 (SOLUCIO): semafor d'humor amb tres estats
# Nucli + ampliacions 1-3: estat A+B, comptador amb logo, funcions propies.
# Maquinari: nomes la micro:bit sola.

from microbit import *


def cara_contenta():
    display.show(Image.HAPPY)


def cara_trista():
    display.show(Image.SAD)


def cara_repos():
    display.show(Image.ASLEEP)


def cara_sorpresa():
    display.show(Image.SURPRISED)


while True:
    # Ampliacio 2: mostra el comptador de pulsacions del boto A en tocar el logo.
    if pin_logo.is_touched():
        display.scroll(str(button_a.get_presses()))
    # Ampliacio 1: estat A+B alhora, abans de mirar-los per separat.
    elif button_a.is_pressed() and button_b.is_pressed():
        cara_sorpresa()
    elif button_a.is_pressed():
        cara_contenta()
    elif button_b.is_pressed():
        cara_trista()
    else:
        cara_repos()
    sleep(100)
```

**Punts a corregir:** l'ordre dels `elif` (A+B abans que A sol i B sol); el `while True:` reduït a crides a funcions (sense `display.show(...)` repetit dins del bucle principal); `get_presses()` reinicia el comptador cada cop que es llegeix (és el comportament esperat de l'API, no un error).

---

## ⭐⭐⭐ Repte 3 · Dau doble sense repeticions

**Idea de la solució:** una funció `tira_dos_daus()` reutilitzable; un bucle `while resultat == ultim_resultat:` que torna a tirar fins que el resultat és diferent de l'anterior; `display.scroll(...)` en lloc de `display.show(...)` perquè els resultats de 10-12 tenen dues xifres.

```python
# SA1 - Repte 3 (SOLUCIO): dau doble sense repeticions
# Nucli + ampliacions 1-3: suma de dos daus, evitar repetir resultat, comptador.
# Maquinari: nomes la micro:bit sola (accelerometre intern).

from microbit import *
import random

ultim_resultat = 0   # Encara no hi ha cap tirada
tirades = 0           # Ampliacio 3: comptador de tirades


def tira_dos_daus():
    # Ampliacio 1: suma de dos daus (2-12).
    dau1 = random.randint(1, 6)
    dau2 = random.randint(1, 6)
    return dau1 + dau2


while True:
    if accelerometer.was_gesture("shake"):
        resultat = tira_dos_daus()
        # Ampliacio 2: si surt el mateix resultat que l'ultima vegada, torna a tirar.
        while resultat == ultim_resultat:
            resultat = tira_dos_daus()

        ultim_resultat = resultat
        tirades += 1

        display.scroll(str(resultat))   # scroll (no show) perque hi ha resultats de 2 xifres (10, 11, 12)
        sleep(200)
        display.clear()

    if pin_logo.is_touched():
        # Ampliacio 3: mostra el comptador de tirades sense interrompre el joc.
        display.scroll(str(tirades))
        display.clear()
```

**Punts a corregir:** el `while resultat == ultim_resultat:` (no un simple `if`, perquè cal poder tirar més d'un cop si torna a coincidir); l'ús de `scroll` per als resultats de dues xifres; que `tirades` només pugi dins del bloc del sacseig, no cada volta del `while True:` principal.

---

## Rúbrica ràpida de correcció (R1, R4, R5)

| Nivell | Codi (R1) | Quadern (R4) |
|---|---|---|
| Nucli assolit (5-6) | El requisit mínim funciona i està comentat | Predicció + solució anotades |
| Notable (7-8) | Una ampliació ben integrada (no apegalada al final) | + un error documentat amb DEPURA |
| Excel·lent (9-10) | Totes les ampliacions, codi net i reutilitzable (funcions) | + reflexió de millora pròpia |

*Solucionari de la SA1. Material del docent.*
