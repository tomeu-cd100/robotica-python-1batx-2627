# Dau del sacseig (ampliació)

**Quan es fa:** Sessió 3 (per a qui va sobrat) o com a feina de repàs · **Fitxer:** `dau_sacseig.py` · **Maquinari:** [esquemes de la placa](../../SA1_esquemes_connexions.md) (nomes la micro:bit sola; usa l'acceleròmetre intern)

## 🎯 Per què fem aquesta pràctica

És l'**ampliació** de la SA1: agafa les mateixes idees d'`hola_mon` i `emocions_botons` (mostrar coses al display, `while True:`, `if`) i hi afegeix dues eines noves: un **sensor intern** (l'acceleròmetre, que detecta que has sacsejat la placa) i l'**atzar** (`random`, per triar un nombre a l'atzar com un dau de veritat).

## 🔮 Abans d'executar: prediu

Mira el codi complet (a baix de tot) **sense executar-lo**. Què ha de fer-se per veure un número al display? Un cop l'has sacsejat, quant de temps es queda el número a la vista abans d'apagar-se? Escriu-ho i comprova-ho al simulador (a python.microbit.org es pot simular el sacseig amb el ratolí).

## 🧠 El codi, per blocs

### Bloc 1 — Un segon import: `random`

```python
from microbit import *
import random
```

A més de `microbit`, aquest programa necessita el mòdul `random` (nombres a l'atzar), que **no** és exclusiu de la micro:bit: és el mateix `random` que fas servir en qualsevol programa de Python.

### Bloc 2 — Detectar el sacseig

```python
if accelerometer.was_gesture("shake"):
```

L'acceleròmetre intern de la micro:bit reconeix alguns **gestos** ja preparats («shake», «up», «down»...). `was_gesture("shake")` retorna `True` **un únic cop** just quan detecta que has sacsejat la placa (no cal que ho comprovis tu mateix mirant els eixos X/Y/Z).

### Bloc 3 — Un nombre a l'atzar

```python
numero = random.randint(1, 6)   # Nombre enter a l'atzar, entre 1 i 6 (tots dos inclosos)
```

`random.randint(1, 6)` retorna un **enter a l'atzar** entre l'1 i el 6, **tots dos inclosos** — exactament com llançar un dau. El resultat es desa a la **variable** `numero` perquè el puguem fer servir a la línia següent.

### Bloc 4 — Mostrar-lo i esperar

```python
display.show(str(numero))   # show() necessita un text, per aixo cal str(...)
sleep(1000)                 # Deixa'l 1 segon a la vista
display.clear()             # Apaga el display, a punt per al seguent sacseig
```

`display.show(...)` amb un **número sol** (1-9) el mostra directament al display; però `numero` és un `int` (enter), i `show()` espera un **text**, per això cal convertir-lo amb `str(numero)`. Després d'un segon (`sleep(1000)`), `display.clear()` apaga el display perquè quedi a punt per al pròxim sacseig.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| `NameError: name 'random' is not defined` | Falta `import random` (a més de `from microbit import *`). |
| El número no desapareix mai | Falta `display.clear()` al final del bloc. |
| Sembla que reacciona sempre igual al mateix moviment | `was_gesture("shake")` cal un sacseig una mica energètic; al simulador, prova el botó de moviment del navegador. |
| El programa no fa res encara que sacsegis fort | Falta el `while True:` que ho comprovi contínuament (sense bucle, només ho mira un cop en arrencar). |

## 🔗 On ho aplicaràs

- **Ara mateix:** els [reptes ⭐⭐⭐ de la SA1](../../../../Reptes/Reptes_SA1.md) reprenen aquest programa per fer un dau més complet.
- **SA3 i tot el curs:** llegir un sensor dins d'un `if` que forma part d'un `while True:` és el patró que faràs servir amb **tots** els sensors del Micro:shield (llum, distància, so...).

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA1](../../../../Reptes/Reptes_SA1.md)**.
