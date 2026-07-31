# Emocions amb botons

**Quan es fa:** Sessió 3 (repte, fase «Crea» del PRIMM) · **Fitxer:** `emocions_botons.py` · **Maquinari:** [esquemes de la placa](../../SA1_esquemes_connexions.md) (el mateix d'[`hola_mon`](../hola_mon/EXPLICACIO.md): nomes la micro:bit sola)

> ✋ **Aquesta pàgina és la SOLUCIÓ del repte de l'Activitat 4** (*els botons A/B canvien la cara del display*). **Intenta-ho pel teu compte abans de mirar-la**: el repte és teu. Si t'encalles, tens un cop de mà a la secció «Si t'encalles» de més avall — que és una escala, no la resposta.

## 🎯 Per què fem aquesta pràctica

A `hola_mon` vas **llegir i modificar** codi d'altri; aquí és la fase **Crea** del PRIMM: escriure el teu primer programa **des de zero**. Introdueix dues eines noves que ja no deixaràs anar: el bucle **`while True:`** (perquè el programa no s'aturi mai) i la instrucció **`if`/`elif`/`else`** (perquè reaccioni de manera diferent segons què passi).

## 🔮 Abans d'executar: prediu

Mira el codi complet (a baix, plegat) **sense executar-lo**. Si prems el botó A, què mostrarà? I el B? I si no prems res? Apunta-ho i comprova-ho.

## 🧠 El codi, per blocs

### Bloc 1 — El bucle `while True:`: per sempre

```python
from microbit import *

while True:
    ...
```

`while True:` crea un bucle que es repeteix **indefinidament**: mentre la placa estigui engegada, el codi de dins es torna a executar una vegada i una altra. Sense aquest bucle, el programa comprovaria els botons **un sol cop** i s'aturaria.

### Bloc 2 — Triar entre opcions: `if` / `elif` / `else`

```python
if button_a.is_pressed():
    display.show(Image.HAPPY)   # Botó A premut -> cara contenta
elif button_b.is_pressed():
    display.show(Image.SAD)     # Botó B premut -> cara trista
else:
    display.show(Image.ASLEEP)  # Cap botó premut -> cara "en repos"
```

Llegeix-ho com una decisió en cadena: **si** el botó A està premut, mostra la cara contenta; **si no, però** el B ho està, mostra la trista; **si no** (cap dels dos), mostra la de repòs. `button_a.is_pressed()` retorna `True` o `False` segons si el botó **està premut en aquest instant**.

### Bloc 3 — Una petita pausa

```python
sleep(100)   # Petita pausa abans de tornar a mirar
```

Sense aquesta pausa el bucle comprovaria els botons milers de vegades per segon, gastant bateria sense necessitat. Amb 100 ms n'hi ha prou perquè es noti **instantani** a la vista.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El display no canvia mai | Falta el `while True:`: sense bucle, el programa comprova els botons **un cop** i s'atura. |
| Sempre mostra la cara de repòs, encara que premis A | Indentació incorrecta: les línies de dins de l'`if` han d'anar **indentades** (amb un tabulador o 4 espais). |
| Error de sintaxi a la línia de l'`elif` | Falta els dos punts (`:`) al final de la línia `if ...:` o `elif ...:`. |
| Canvio el codi i no passa res | No l'has tornat a **transferir** a la placa: cada canvi necessita descarregar i arrossegar un altre `.hex`. |

## 🧗 Si t'encalles: l'esquelet de reacció a botons

Si estàs en blanc davant del programa buit, no miris encara la solució: parteix d'aquest esquelet. L'`import` i el `while True:` ja hi són; tu només omples els `# TODO:` amb `display.show(...)`.

<details markdown="1">
<summary>Desplega l'esquelet (còpia'l a un programa nou)</summary>

```python
# SA1 - emocions_botons  (BASTIDA / esquelet per a l'alumnat)
#
# QUE JA ESTA FET (no ho toquis):
#   - L'import de microbit ja hi es.
#   - El while True: ja esta muntat, perque el programa no s'aturi mai.
#
# QUE HAS DE FER TU:
#   - OMPLE cada branca amb un display.show(Image....) diferent.
#     Quan premis A ha de sortir una cara, quan premis B una altra,
#     i quan no premis res, una tercera.
#
# EINES QUE POTS USAR (nomes conceptes de la SA1):
#   - button_a.is_pressed()   -> True si el boto A esta premut ara
#   - button_b.is_pressed()   -> True si el boto B esta premut ara
#   - display.show(Image.HAPPY / Image.SAD / Image.ASLEEP / Image.SURPRISED...)
#
# IDEA: la llista completa d'imatges predefinides es a la documentacio
#   oficial de la classe Image; prova'n unes quantes al simulador.

from microbit import *

while True:
    if button_a.is_pressed():
        pass  # TODO 1: display.show(Image. ... )
    elif button_b.is_pressed():
        pass  # TODO 2: display.show(Image. ... )
    else:
        pass  # TODO 3: display.show(Image. ... )
    sleep(100)
```

</details>

## 🔗 On ho aplicaràs

- **Si vas sobrat:** l'ampliació [`dau_sacseig`](../dau_sacseig/EXPLICACIO.md) (acceleròmetre + nombres aleatoris, amb `if` dins d'un `while True:` igual que aquí).
- **SA2 i tot el curs:** l'estructura `while True:` + `if/elif/else` torna a sortir a **pràcticament tots** els programes que faràs (llegir un sensor i decidir què fer).

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA1](../../../../Reptes/Reptes_SA1.md)**.
