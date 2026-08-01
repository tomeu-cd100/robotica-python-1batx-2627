# SA1 · Exemple resolt (model «jo ho faig») — Analitzo un aspirador robot i li poso un senyal de vida

> 🧑‍🎓 **Quan toca mirar-lo?** Després del teu **primer intent** amb la taula E-P-S de l'**Activitat 1 (S1)** i amb `hola_mon.py` de l'**Activitat 4 (S3)** — mai abans. És un problema **anàleg** per veure *com es pensa*, no una solució per copiar: el pòster l'has de fer amb el **teu** robot.

> 🔗 **D'on ve i on va.** Aquest exemple és el **bessó comentat** de la pràctica [Hola, món! El primer programa](codi/hola_mon/EXPLICACIO.md): la mateixa idea (missatge + imatge al display) amb un context expressament diferent — el **senyal de vida** d'un aspirador robot en lloc d'una salutació — perquè vegis **com es pensa**, no per copiar-lo. Quan l'hagis entès, torna a la pàgina de la pràctica i fes-la teva.

> 🗺️ **Com es llegeix per apartats:** **🔑 El repte model** primer, per situar-te · **🧭 Com ho penso** abans d'escriure el **teu** codi (és l'apartat més important: el raonament) · **💡 La solució anotada** només **després del teu intent**, per comparar · **🔬 Provo i mesuro** quan provis el teu: copia'n el **mètode**, no el resultat · **⚠️ Contraexemple** quan una cosa no rutlli — i com a repàs abans d'entregar · **📔 Diari de bord** quan escriguis la teva entrada del quadern.

> **Nota docent:** mostra'l **després del primer intent** amb l'Activitat 1 (taula E-P-S) i amb
> `hola_mon.py`, mai abans. No és la solució del pòster (que cada alumne/a fa amb el **seu**
> robot): és un problema **anàleg** resolt pas a pas perquè l'alumnat vegi *com es pensa* un
> sistema, no què s'ha de copiar. Comenta en veu alta el pas «🧭 Com ho penso» (descomposició
> abans d'escriure, predicció PRIMM abans d'executar) i el «⚠️ Contraexemple».

---

## 🔑 El repte model

> Agafo un robot quotidià —un **aspirador robot**— i l'**analitzo amb el model entrada → procés →
> sortida**: què *percep*, què *decideix* i què *fa*. Després, com que tot robot dona un **senyal
> de vida** quan funciona, escric un programa MicroPython senzill que faci parpellejar un **cor**
> al display de la micro:bit (com el LED d'estat de l'aspirador) i l'anoto línia a línia.

Fa servir només conceptes de la SA1: el model **E-P-S**, la diferència **digital/analògic**, l'anatomia
de la placa i el primer programa (`from microbit import *`, `display.scroll`, `display.show`, `sleep`).
No cal cap component extern: només la micro:bit sola.

---

## 🧭 Com ho penso (abans d'escriure res)

1. **Analitzo (descomposició):** un aspirador robot sembla «màgic», però és un sistema automàtic com
   la rentadora o el semàfor de l'Activitat 1. Si el parteixo en **tres caixes** (SENSOR → CERVELL →
   ACTUADOR) deixa de ser màgic i el puc entendre.
2. **Omplo les caixes preguntant-me tres coses:**
   - **Què percep?** (entrada) → sensor de xoc, sensor de precipici (per no caure de l'escala),
     sensor de brutícia, botó d'engegada.
   - **Què decideix?** (procés) → el microcontrolador: *«si topo → giro», «si detecto precipici →
     recular»*. És el "cervell", com el microcontrolador de la micro:bit.
   - **Què fa?** (sortida) → motors de les rodes, motor de l'aspiració, **llum d'estat**, so d'avís.
3. **Classifico els senyals (digital vs analògic):** el botó d'engegada és **digital** (premut / no
   premut, dos estats). El sensor de brutícia dona **molts valors** (poc / mig / molt) → **analògic**.
   Mateixa idea que a la micro:bit: els botons A/B són digitals; el sensor de llum del display és
   analògic (`display.read_light_level()`, valors 0-255).
4. **🔮 PREDIU (fes-ho tu abans de llegir el codi):** el senyal de vida de baix consum sovint fa un
   **batec**: apareix poc temps i desapareix molt més. Amb `display.show(Image.HEART); sleep(200)` i
   després `display.clear(); sleep(2000)`, el display estarà… ☐ sempre encès ☐ **un instant encès
   i molta estona apagat** ☐ parpellejant simètric. I el bucle `while True:` es repetirà… ☐ **un sol
   cop** ☐ **per sempre**.

---

## 💡 La solució anotada

**Primer, l'anàlisi E-P-S de l'aspirador (el que hauria d'anar al pòster, amb el *meu* raonament):**

| | Entrada (sensors) | Procés (decisió) | Sortida (actuadors) |
|---|---|---|---|
| **Aspirador robot** | Sensor de xoc, sensor de precipici, sensor de brutícia, botó d'engegada | Microcontrolador: seguir la ruta, esquivar obstacles, tornar a la base a carregar | Motors de rodes, motor d'aspiració, **llum d'estat**, avís sonor |

> **Dilema ètic (el plantejo, no cal resoldre'l):** un aspirador amb càmera i mapa de casa és molt
> còmode… però *on van les dades del plànol del meu pis?* Comoditat vs privacitat.

**I ara el "senyal de vida": el batec del display, anotat línia a línia.**

```python
# SA1 - exemple_batec.py  (EXEMPLE MODEL, no es el producte)
# "Senyal de vida" d'un robot: un batec (cor curt + pausa llarga),
# com la llum d'estat d'un aspirador en repos.
# Maquinari: nomes la micro:bit sola. No cal connectar res.

from microbit import *

while True:
    # while True: es repeteix per sempre, aixo fa que el batec no s'aturi mai.
    display.show(Image.HEART)   # Mostra un cor al display
    sleep(200)                  # ...pero nomes 200 ms (un instant): el "batec" es curt
    display.clear()             # Apaga tot el display
    sleep(2000)                 # ...i espera 2000 ms = 2 s abans del seguent batec
```

**Per què està escrit així (🌟):**
- **`display.show()`/`display.clear()` són canvis d'estat clars** (encès/apagat): és perfecte per a un
  senyal d'estat, que és un comportament **digital** (hi és o no hi és). No cal res "analògic" aquí.
- El batec surt de fer **`sleep()` diferents**: 200 ms de cor + 2000 ms apagat. Canviant només aquests
  dos números canvio tot el comportament, sense tocar la resta.
- **`from microbit import *` sempre a la primera línia** i el comportament dins d'un `while True:`:
  aquesta és l'estructura de *pràcticament tots* els programes de micro:bit del curs.

---

## 🔬 Provo i mesuro

- **Predicció ✔:** el display fa un **flaix curt i una pausa llarga** (batec), no un parpelleig
  simètric. I el `while True:` es repeteix **per sempre** (si sembla que s'atura, és perquè encara
  no ha passat el `sleep` llarg).
- **Sense maquinari:** tot es reprodueix al **simulador de python.microbit.org**; no cal connectar res.
- **Experimento amb els temps:** si vull un batec **més viu** com el d'un cor de veritat, canvio a
  `sleep(120)` + `sleep(900)`. Si l'allargo del tot (`sleep(4000)`), sembla que el robot "dorm". **Un
  número, un comportament.**

---

## ⚠️ Contraexemple (errors típics i com es detecten)

- **Confonc entrada amb sortida:** poso la llum d'estat o el motor a la columna "entrada". *Error:* una
  llum és un **actuador** (sortida), no un sensor. **Pista:** *percep* → entrada; *fa/actua* → sortida.
- **Crec que el programa s'atura sol:** espero que després d'un cicle el display es quedi aturat. *No:*
  el `while True:` es repeteix **sempre**; per aturar-lo cal desendollar la placa o rebre un `reset`.
- **Oblido `from microbit import *`:** el programa peta amb `NameError: name 'display' is not defined`.
  **Sempre** a la primera línia.
- **El programa no arriba a la placa:** no s'ha arrossegat el `.hex` a la unitat `MICROBIT`, o s'ha
  desendollat mentre parpellejava el LED groc de gravació. Torna-ho a fer sense pressa.

---

## 📔 Diari de bord (entrada model, 1a persona)

> **Sessió 1-3:** He après que un robot és un **sistema embegut** i que qualsevol automatisme es pot
> partir en **entrada → procés → sortida**. He analitzat un **aspirador robot**: percep amb sensors de
> xoc i precipici (entrada), decideix la ruta amb el microcontrolador (procés) i actua amb els motors i
> la llum d'estat (sortida). He entès la diferència **digital** (botó: premut/no premut) i **analògic**
> (sensor de brutícia: molts valors). Al primer programa vaig **predir** que el batec seria curt-encès i
> llarg-apagat, i es va complir. Al principi vaig posar la llum a la columna d'entrada: l'error va ser
> confondre **sensor** (percep) amb **actuador** (fa). **Evidència:** taula E-P-S de l'aspirador +
> descripció del cor parpellejant al simulador.

**Per què és una bona entrada:** usa el **vocabulari clau** (sistema embegut, E-P-S, digital/analògic,
`while True:`), explica *el com*, i és **honesta amb la dificultat** (entrada vs sortida) i com es va resoldre.

---

*Exemple resolt de la SA1. Model de treball per a l'alumnat (alliberament gradual: es mostra després
del primer intent). Es recolza en `codi/hola_mon` i `SA1_esquemes_connexions.md`. El pòster real l'has de
fer amb el **teu** robot, no amb aquest. Llicència CC BY-SA 4.0.*
