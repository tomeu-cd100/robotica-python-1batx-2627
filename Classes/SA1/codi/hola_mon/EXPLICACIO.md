# Hola, món! El primer programa

**Quan es fa:** Sessió 3 (modelatge) · **Fitxer:** `hola_mon.py` · **Maquinari:** [esquemes de la placa](../../SA1_esquemes_connexions.md) (nomes la micro:bit sola: no cal connectar res)

## 🎯 Per què fem aquesta pràctica

És el teu **primer programa** de tot el curs, i és el «Hola, món» de la micro:bit: mostrar un text i una imatge al display. Sembla poca cosa, però conté l'**estructura bàsica de tots els programes que escriuràs**: l'`import` que dona accés a la placa, i les ordres que fan que hi passi alguna cosa.

A més, el treballem amb el mètode **PRIMM**: primer **prediràs** què fa el codi sense executar-lo, i només després el provaràs. Predir abans de provar és el pas que més t'ajuda a entendre de debò — és el «dissenyar» del mètode de projecte.

## 🔮 Abans d'executar: prediu

Mira el codi complet (a baix de tot) **sense executar-lo**. Què farà el display, en quin ordre? Quant durarà cada part? Escriu la predicció a l'Activitat 4 de la [fitxa](../../SA1_fitxa_alumnat.md) i després comprova-la.

## 🧠 El codi, per blocs

### Bloc 1 — L'import: la porta d'entrada a la placa

```python
from microbit import *
```

Aquesta línia va **sempre** a dalt de tot de qualsevol programa de micro:bit. Sense ella, la placa no sap què vol dir `display`, `button_a` o cap altra ordre: totes vénen d'aquest `import`. Si l'oblides, el programa peta amb un `NameError`.

### Bloc 2 — Mostrar text: `display.scroll()`

```python
display.scroll("HOLA")   # Mostra el text lletra a lletra, desplacant-se
```

`display.scroll(...)` mostra un text **lletra a lletra**, desplaçant-se per la matriu de 25 LED (com un rètol lluminós). El programa **espera** que acabi de desplaçar-se abans de continuar amb la línia següent.

### Bloc 3 — Una pausa: `sleep()`

```python
sleep(500)   # Espera 500 ms (mig segon)
```

`sleep(...)` atura el programa el temps indicat, en **mil·lisegons** (1000 ms = 1 segon). Si hi poses `100`, l'espera és una dècima de segon.

### Bloc 4 — Mostrar una imatge: `display.show()`

```python
display.show(Image.HEART)   # Mostra una imatge fixa: un cor
```

`display.show(...)` mostra una **imatge fixa** (a diferència de `scroll`, que desplaça text). `Image` porta un bon grapat d'imatges ja fetes (`Image.HEART`, `Image.HAPPY`, `Image.SAD`, `Image.YES`...) que pots fer servir directament.

Fixa't que **canviant només el text de `scroll()` o la imatge de `show()`** canvies tot el missatge, sense tocar res més de l'estructura.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| `NameError: name 'display' is not defined` | Falta la línia `from microbit import *` a dalt de tot. |
| El programa no arriba a la placa | No s'ha arrossegat el `.hex` descarregat a la unitat `MICROBIT`. Vegeu [`00_Entorns_de_treball.md`](../../../00_General/00_Entorns_de_treball.md). |
| El text passa massa ràpid per llegir-lo | És normal amb textos curts: `scroll` sempre va a la mateixa velocitat; amb un text més llarg es nota millor. |
| «S'ha quedat penjat, no fa res més» | No és un error: `display.show()` deixa la imatge **fixa** perquè no hi ha cap `while True:` que continuï fent coses. |

## 🔗 On ho aplicaràs

- **Ara mateix:** el repte de l'Activitat 4 (fer que els botons A/B mostrin cares diferents, a [`emocions_botons`](../emocions_botons/EXPLICACIO.md)). Intenta'l pel teu compte.
- **Després del teu primer intent:** l'[exemple resolt del batec](../../SA1_exemple_resolt.md) és el **bessó** d'aquesta pràctica — la mateixa idea amb un ritme i un context diferents, raonada pas a pas amb el diari de bord inclòs. Serveix per veure *com es pensa*, no per copiar-lo.
- **Si vas sobrat:** l'ampliació [`dau_sacseig`](../dau_sacseig/EXPLICACIO.md) (acceleròmetre + nombres aleatoris).
- **Tot el curs:** `from microbit import *` és la primera línia de **tots** els programes de micro:bit que faràs; a la SA2 hi afegiràs sortides connectades al Micro:shield (LED, brunzidor, servo).

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA1](../../../../Reptes/Reptes_SA1.md)**.
