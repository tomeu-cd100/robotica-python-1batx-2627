# SA0 · Guia de referència de programació

> **Per a qui és?** Per a **tu, alumne/a**. No és una unitat amb sessions pròpies: és el **material de reforç** al qual et deriva el docent quan un [mini-check](../00_General/00_Mini_checks_individuals.md) et surt 🔴 («no me'n surto sol»). Cada secció és curta (una pàgina), explica **un** concepte, i inclou un exemple mínim que pots copiar i provar al simulador.
>
> 🔗 **Com hi arribes.** Cada secció d'aquesta guia respon a un reforç 🔴 concret de `00_Mini_checks_individuals.md`. Quan el docent t'hi deriva, ja sap quina secció et toca; si vols repassar pel teu compte, l'índex de sota et diu quina secció correspon a quin mini-check.
>
> ⏱️ **Cronologia.** Les seccions estan ordenades **com el curs**: la secció A1-A2 només fa servir el que ja saps a la SA1, la A3-A4 el que ja saps a la SA1+SA2, i així fins a la Part B (SA5). Si encara no has fet la SA d'una secció, encara no cal que la llegeixis.

## Índex (quin mini-check et porta a quina secció)

| Secció d'aquesta guia | Es fa servir des del reforç 🔴 de | Concepte |
|---|---|---|
| [A1-A2 · Primer programa i estructura d'un fitxer `.py`](#a1-a2-primer-programa-i-estructura-dun-fitxer-py) | SA1 | `import`, `display.scroll()`, `display.show()`, `sleep()` |
| [A3-A4 · Bucles i sortides digitals](#a3-a4-bucles-i-sortides-digitals) | SA2 | `while True:`, `write_digital()` |
| [A5 · Condicionals (`if`/`elif`/`else`)](#a5-condicionals-ifelifelse) | SA3 | branques, comparacions |
| [A6 · Entrades analògiques](#a6-entrades-analogiques) | SA3 | `read_analog()`, rangs 0-255 i 0-1023 |
| [A7 · Funcions i paràmetres](#a7-funcions-i-parametres) | SA4 | `def`, paràmetres, crides |
| [Part B · Ràdio](#part-b-radio) | SA5 | `radio.config()`, `radio.on()`, `send()`/`receive()` |

---

## A1-A2 · Primer programa i estructura d'un fitxer `.py`

**L'explicació planera.** Un programa de MicroPython per a la micro:bit és un fitxer de text (`.py`) que s'executa **de dalt a baix, línia a línia**, una sola vegada (llevat que hi hagi un bucle, que veuràs a la secció següent). La **primera línia sempre és la mateixa**: `from microbit import *`. Aquesta línia dona accés a totes les eines de la placa (`display`, `pin0`, `button_a`...): sense ella, cap d'aquestes paraules existeix per a MicroPython i el programa falla a la primera línia que les faci servir.

A partir d'aquí, cada instrucció és una **ordre** que la placa executa en ordre: mostrar alguna cosa al display, esperar una estona, mostrar-ne una altra. Dues instruccions bàsiques del display:

- `display.scroll("TEXT")`: fa passar el text lletra a lletra (fet servir per a paraules).
- `display.show(Image.HAPPY)`: mostra una **imatge fixa** de cop (fet servir per a icones/emocions).

I una instrucció de temps: `sleep(500)` **atura** el programa mig segon (500 mil·lisegons) abans de continuar amb la línia següent. Sense `sleep()`, dues instruccions seguides s'executarien tan de pressa que semblaria que només ha passat la segona.

**Exemple mínim executable:**

```python
# Primer programa: escriu el nom lletra a lletra, espera, i mostra una icona fixa
from microbit import *

display.scroll("HOLA")
sleep(500)
display.show(Image.HAPPY)
sleep(2000)
```

**Error típic.**
- **Símptoma:** el simulador o la placa no fan res, o donen un error com `NameError: name 'display' isn't defined`.
- **Causa:** falta la línia `from microbit import *` al principi del fitxer, o s'ha escrit després de fer-la servir.
- **Solució:** comprova que la **primera línia sense comentaris** del fitxer sigui exactament `from microbit import *`.

---

## A3-A4 · Bucles i sortides digitals

**L'explicació planera.** Un **bucle** repeteix un bloc d'instruccions sense haver-lo d'escriure diverses vegades. El curs en fa servir dos tipus (aquest, `while`, i el `for` que veuràs més endavant al curs). `while True:` repeteix **per sempre** tot el que va indentat (amb sagnia) a sota seu: és el bucle que fa servir la majoria de programes de la micro:bit, perquè un robot ha d'estar sempre percebent i actuant, no fer-ho un sol cop.

Una **sortida digital** és un pin que només pot estar en dos estats: **encès** (`1`) o **apagat** (`0`). S'escriu amb `pin1.write_digital(1)` (encén) o `pin1.write_digital(0)` (apaga). Per fer parpellejar un LED cal alternar els dos estats **dins** del bucle, amb un `sleep()` entre cada canvi perquè l'ull humà el pugui distingir.

**Punt clau d'indentació:** tot el que ha de repetir-se ha d'estar **sagnat** (normalment 4 espais) just a sota de `while True:`. Una línia sense sagnia "surt" del bucle i només s'executa un cop, abans de començar a repetir.

**Exemple mínim executable:**

```python
# Parpelleig d'un LED al pin P1: mig segon ences, mig segon apagat, per sempre
from microbit import *

while True:
    pin1.write_digital(1)   # LED ences
    sleep(500)
    pin1.write_digital(0)   # LED apagat
    sleep(500)
```

**Error típic.**
- **Símptoma:** `IndentationError` en provar el programa, o el LED es queda sempre encès/apagat sense parpellejar.
- **Causa:** falta la sagnia (espais) a les línies dins del `while True:`, o hi falta el `:` final de la línia del `while`.
- **Solució:** revisa que `while True:` acabi en `:` i que **totes** les línies que han de repetir's estiguin sagnades igual (l'editor oficial ho fa automàticament si prems Retorn just després dels dos punts).

---

## A5 · Condicionals (`if`/`elif`/`else`)

**L'explicació planera.** Un condicional fa que el programa **decideixi** entre diversos camins segons si una condició és certa o falsa. `if condicio:` executa el bloc de sota **només** si la condició és certa; `else:` executa el seu bloc quan la condició del `if` **no** es compleix. Quan hi ha més de dues opcions, `elif` (abreviatura de "else if") permet afegir-ne més entremig, sempre abans de l'`else` final.

**El parany més freqüent:** `==` compara dos valors (és la pregunta "són iguals?"), mentre que `=` **assigna** un valor a una variable (és l'ordre "guarda això aquí"). Dins d'un `if` sempre cal `==` (o `<`, `>`, `<=`, `>=`, `!=`), mai un sol `=`.

**Exemple mínim executable:**

```python
# Enten si fa fred, be o calor segons la temperatura interna de la placa
from microbit import *

while True:
    temp = temperature()   # graus C

    if temp < 18:
        display.show(Image.SAD)      # fred
    elif temp > 26:
        display.show(Image.ANGRY)    # calor
    else:
        display.show(Image.HAPPY)    # be

    sleep(500)
```

**Error típic.**
- **Símptoma:** `SyntaxError` a la línia de l'`if`, o el programa sempre entra a la mateixa branca encara que la temperatura canviï.
- **Causa:** oblidar el `:` al final de `if`/`elif`/`else`, o escriure `temp = 18` (assignació) en lloc de `temp == 18` (comparació) dins la condició.
- **Solució:** revisa que cada línia `if`/`elif`/`else` acabi en `:`, i que dins de la condició es faci servir `==` per comparar (mai un sol `=`).

---

## A6 · Entrades analògiques

**L'explicació planera.** A diferència d'una entrada digital (que només distingeix encès/apagat), una **entrada analògica** llegeix un **valor graduat**, no només dos estats: com de fosc o clar és, com de calent és, com de a prop hi ha un obstacle. La micro:bit llegeix aquests valors amb `read_analog()`, que sempre retorna un número entre **0 i 1023** (per exemple, `pin0.read_analog()` per a un sensor connectat al pin P0). Un cas especial és el sensor de llum **intern** de la placa, `display.read_light_level()`, que dona un rang diferent, **0 a 255**: cal saber quin sensor fas servir per no confondre les dues escales.

Per decidir què fer amb una lectura analògica, es compara amb un **llindar** (un número que marca la frontera entre dues situacions), fent servir el condicional que ja coneixes (secció A5): `if lectura < LLINDAR:`. El llindar **no s'inventa**: es mesura al REPL provant el sensor en les dues situacions reals (per exemple, tapat i destapat) i es tria un valor entremig.

**Exemple mínim executable:**

```python
# Llegeix un sensor analogic al pin P0 i decideix segons un llindar calibrat
from microbit import *

LLINDAR = 500   # calibrat al REPL: mig entre "fosc" i "clar"

while True:
    lectura = pin0.read_analog()   # 0-1023

    if lectura < LLINDAR:
        display.show(Image.ASLEEP)
    else:
        display.show(Image.HAPPY)

    sleep(200)
```

**Error típic.**
- **Símptoma:** el programa sembla no reaccionar mai, o reacciona sempre igual encara que el sensor canviï molt.
- **Causa:** el llindar s'ha triat "a ull" (per exemple, `500` sense haver mesurat res) i no coincideix amb els valors reals del sensor, o s'ha confós l'escala 0-255 (llum interna) amb la 0-1023 (entrada analògica externa).
- **Solució:** abans de fixar `LLINDAR`, escriu `pin0.read_analog()` unes quantes vegades al REPL en les dues situacions extremes i tria un valor entre totes dues.

---

## A7 · Funcions i paràmetres

**L'explicació planera.** Una **funció** és un bloc de codi amb un nom, que es defineix un sol cop i es pot **cridar** (executar) tantes vegades com calgui. Es defineix amb `def nom_funcio():` seguit del bloc sagnat amb el que fa. Cridar-la és tan senzill com escriure `nom_funcio()` (amb parèntesis: sense parèntesis només et refereixes a la funció, no l'executes).

Un **paràmetre** és una dada que la funció rep quan es crida, i que pot canviar cada cop: `def avancar(velocitat):` defineix una funció que necessita que li passis un valor de `velocitat` cada vegada que la cridis, per exemple `avancar(400)` o `avancar(100)`. Dins de la funció, `velocitat` es fa servir com si fos una variable normal amb el valor que li has passat. Gràcies als paràmetres, **una** funció serveix per a molts casos, en lloc de repetir el mateix codi amb un número diferent cada vegada.

**Exemple mínim executable:**

```python
# Funcio amb un parametre: mou el motor esquerre (M1) a la velocitat rebuda
# Pins del motor M1, mapa vinculant del fil conductor (00_Fil_conductor_construccions.md):
# P13 = M1 sentit endavant, P14 = M1 sentit enrere.
from microbit import *

M1_ENDAVANT = pin13
M1_ENRERE = pin14

def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)   # 0-1023, PWM
    M1_ENRERE.write_digital(0)            # sentit endavant nomes

avancar(300)   # velocitat baixa
sleep(1000)
avancar(800)   # velocitat alta
```

**Error típic.**
- **Símptoma:** `TypeError: function takes 1 positional argument but 0 were given` (o similar), o la funció sempre es comporta igual encara que li passis valors diferents.
- **Causa:** cridar la funció sense el paràmetre (`avancar()` en lloc de `avancar(300)`), o definir-la amb un valor fix dins en lloc de fer servir el nom del paràmetre (per exemple, escriure `M1_ENDAVANT.write_analog(300)` en comptes de `M1_ENDAVANT.write_analog(velocitat)`).
- **Solució:** revisa que **dins** de la funció es faci servir el nom del paràmetre (no un número fix), i que **cada crida** li passi un valor entre parèntesis.

---

## Part B · Ràdio

**L'explicació planera.** Dues o més micro:bit poden parlar-se sense fils amb el mòdul `radio`. Per fer-ho, calen sempre **tres passos**, en aquest ordre:

1. `import radio` — dona accés a les eines de ràdio (com `from microbit import *` dona accés al display).
2. `radio.config(group=10)` — fixa el **grup**: només les plaques amb el **mateix número** de grup es senten entre elles (així la teva ràdio no interfereix amb la del company del costat).
3. `radio.on()` — **activa** la ràdio. Sense aquesta línia, la placa no envia ni rep res, encara que la resta del codi sigui correcte. Es crida **un sol cop, fora del bucle**, no a cada volta.

Per **enviar**, `radio.send('text')` (sempre text, mai un número sol: si vols enviar un número, cal convertir-lo amb `str()`, per exemple `radio.send('T:' + str(temperature()))`). Per **rebre**, `radio.receive()` retorna el darrer missatge arribat, o `None` si no n'ha arribat cap de nou: per això sempre es crida **dins** del `while True:`, a cada volta, i es compara amb `==` (com als condicionals de la secció A5) per decidir què fer-hi.

**Exemple mínim executable:**

```python
# Receptor per radio: si arriba exactament el missatge 'F', avanca
from microbit import *
import radio

radio.config(group=10)
radio.on()   # una sola vegada, fora del bucle

while True:
    missatge = radio.receive()
    if missatge == 'F':
        avancar(400)
    sleep(20)
```

**Error típic.**
- **Símptoma:** cap de les dues plaques rep mai res, sense cap error visible.
- **Causa:** falta `radio.on()` en una de les dues plaques, o els dos `group=` no coincideixen (per exemple, una placa amb `group=10` i l'altra amb `group=5`).
- **Solució:** comprova que **totes dues** plaques criden `radio.on()` i que fan servir **exactament** el mateix número de `group=`.

---

*Guia de referència de la SA0. Deriva des dels reforços 🔴 de `../00_General/00_Mini_checks_individuals.md`. Llicència CC BY-SA 4.0.*
