# SA8 · Exemple resolt (model «jo ho faig») — Una estació d'ambient amb protocol propi

> 🧑‍🎓 **Quan toca mirar-lo?** Després del teu **primer intent** amb `comportaments.py`/`telemetria_radio.py` (S1-S2) — mai abans. És un problema **anàleg** per veure *com es pensa*, no una solució per copiar: el producte «sistema de telemetria del rover» l'has de fer amb el **teu** rover.

> 🔗 **D'on ve i on va.** Aquest exemple és el **bessó comentat** de les pràctiques [`telemetria_radio`](codi/telemetria_radio/EXPLICACIO.md) i [`estacio_base`](codi/estacio_base/EXPLICACIO.md): la mateixa idea (llegir un sensor, dissenyar un protocol, enviar-ho per ràdio, rebre-ho i registrar-ho) amb un context expressament diferent — una **estació d'ambient de taula** amb només la placa micro:bit, sense rover — perquè vegis **com es pensa**, no per copiar-lo. Quan l'hagis entès, torna al teu rover i fes el **teu** producte.

> **Nota docent:** mostra'l **després del primer intent** amb `telemetria_radio.py`. No és la solució del producte (que cada alumne/a fa amb el **seu** rover i el **seu** `estacio_base.py`): és un problema **anàleg** resolt pas a pas perquè l'alumnat vegi *com es pensa* un protocol de telemetria, no què s'ha de copiar. Comenta en veu alta el pas «🧭 Com ho penso» (per què cal un prefix propi) i el «⚠️ Contraexemple».

---

## 🔑 El repte model

> Vull que una micro:bit "d'ambient" enviï per ràdio la temperatura i el nivell de llum **interns** cada 2 segons, i que una segona micro:bit els rebi, els mostri i en guardi la mitjana de les últimes 5 lectures de temperatura. És l'anàleg del rover que envia la seva telemetria a `estacio_base.py`, però amb els sensors **interns** de la placa (sense Kit 3 ni rover).

Fa servir només conceptes de la SA8: **protocol propi amb prefix**, **enviament periòdic (no a cada volta del bucle)**, i **registre amb llista + mitjana simple**. Maquinari: dues micro:bit V2, sensors **interns** (`temperature()`, `display.read_light_level()`), sense necessitat del rover ni del Kit 3.

---

## 🧭 Com ho penso (abans d'escriure res)

1. **Analitzo:** necessito dues plaques que "parlin el mateix idioma": el mateix `group` de ràdio i el mateix format de missatge. Si envio `"23;120"` sense cap etiqueta, la placa receptora no sabrà distingir la temperatura de la llum.
2. **Decideixo el protocol:** un prefix propi (`"AMB:"`, d'"ambient", diferent del `"TEL:"` del rover perquè són dos productes diferents) i camps etiquetats separats per `;`, exactament com `telemetria_radio.py`.
3. **Decideixo la freqüència d'enviament:** cada 2 s, no a cada volta del bucle, per no saturar la ràdio (mateixa idea que `INTERVAL_TELEMETRIA_MS`).
4. **🔮 PREDIU (fes-ho tu abans de llegir el codi):** si la placa receptora encara no té cap lectura de temperatura (la llista és buida) i intento calcular-ne la mitjana, què hauria de passar? ☐ El programa peta amb un error ☐ Retorna 0 o un valor per defecte, sense petar.

---

## 💡 La solució anotada

```python
# SA8 - exemple_estacio_ambient.py  (EMISSOR, EXEMPLE MODEL, no es el producte)
# Envia temperatura i llum interns per radio cada 2 s, amb un protocol propi
# (prefix "AMB:", camps etiquetats), igual que fa telemetria_radio.py amb
# el prefix "TEL:" i els sensors del Kit 3.

from microbit import *
import radio

GRUP = 5
radio.on()
radio.config(group=GRUP, power=6, length=64)

PREFIX = "AMB:"
INTERVAL_MS = 2000
ultim_enviament = running_time()

while True:
    ara = running_time()
    if ara - ultim_enviament >= INTERVAL_MS:
        ultim_enviament = ara
        temp = temperature()
        llum = display.read_light_level()
        missatge = PREFIX + "T:" + str(temp) + ";L:" + str(llum)
        radio.send(missatge)
        display.show(Image.ARROW_N)
        sleep(150)
        display.clear()
    sleep(20)
```

```python
# SA8 - exemple_estacio_ambient_receptor.py  (RECEPTOR, EXEMPLE MODEL)
# Rep el protocol "AMB:", el separa en un diccionari (mateixa idea que
# analitza() d'estacio_base.py) i guarda una mitjana simple de temperatura.

from microbit import *
import radio

GRUP = 5
radio.on()
radio.config(group=GRUP, power=6, length=64)

PREFIX = "AMB:"
MAX_HISTORIC = 5
historic_temp = []


def analitza(missatge):
    dades = {}
    for camp in missatge[len(PREFIX):].split(";"):
        if ":" not in camp:
            continue
        clau, valor = camp.split(":", 1)
        dades[clau] = valor
    return dades


def mitjana(llista):
    return sum(llista) / len(llista) if llista else 0


while True:
    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        dades = analitza(missatge)
        try:
            temp = int(dades.get("T", 0))
        except ValueError:
            temp = 0
        historic_temp.append(temp)
        if len(historic_temp) > MAX_HISTORIC:
            historic_temp.pop(0)
        print(missatge, "| mitjana temp:", mitjana(historic_temp))
        display.show(str(temp))
    sleep(50)
```

**Per què està escrit així (🌟):**
- **Un prefix propi (`"AMB:"`) i no `"TEL:"`:** encara que el mecanisme sigui idèntic al del rover, és un producte diferent; reutilitzar el mateix prefix per a dues coses diferents seria una font d'errors si mai coincidissin al mateix `group`.
- **`INTERVAL_MS` controla l'enviament, no el bucle sencer:** el `sleep(20)` final manté el programa reactiu (per exemple, a un futur polsador), mentre que l'enviament de ràdio només passa quan toca.
- **`mitjana()` amb comprovació de llista buida:** evita un error de divisió per zero abans que arribi la primera lectura, exactament com hauria de fer `estacio_base.py` amb `historic_distancies`.

---

## 🔬 Provo i mesuro

- **Predicció ✔:** amb la llista buida, `mitjana([])` retorna `0` gràcies al `if llista else 0`, sense petar.
- **Provo cada extrem per separat:** primer verifico que l'emissor envia cada 2 s exactes (comptant amb un cronòmetre), i després que el receptor mostra la temperatura correcta abans de fiar-me de la mitjana.
- **Protocol trencat a propòsit:** envio un missatge sense el prefix `"AMB:"` des d'una tercera pestanya del simulador i comprovo que el receptor l'ignora (gràcies al `missatge.startswith(PREFIX)`) en lloc de petar.

---

## ⚠️ Contraexemple (errors típics i com es detecten)

- **Prefixos diferents a emissor i receptor** (per exemple, `"AMB:"` a un i `"Amb:"` a l'altre): el receptor no reconeix mai cap missatge. **Pista:** compara els dos `PREFIX` caràcter a caràcter.
- **Enviar a cada volta del bucle sense `INTERVAL_MS`:** la ràdio "es satura" de missatges idèntics i la pantalla del receptor parpelleja sense parar. **Pista:** com a `telemetria_radio.py`, guarda l'instant del darrer enviament i compara amb `running_time()`.
- **Calcular la mitjana sense comprovar la llista buida:** el programa peta amb `ZeroDivisionError` just en arrencar, abans de rebre cap missatge. **Pista:** un `if llista else valor_per_defecte` sempre abans de dividir.
- **Oblidar que `group` ha de coincidir:** si emissor i receptor tenen `group` diferent, és com si estiguessin en "habitacions" de ràdio diferents: mai es sentiran, encara que el protocol sigui perfecte.

---

## 📔 Diari de bord (entrada model, 1a persona)

> **Sessió 1-2:** He après que un **protocol** no és només "enviar un número": cal **acordar** un format (prefix + camps etiquetats) entre les dues plaques abans de res. Vaig **predir** que calcular la mitjana amb la llista buida petaria, i en provar-ho vaig veure que, efectivament, sense la comprovació `if llista else 0`, el programa petava a l'instant. Ho vaig resoldre afegint la comprovació abans de dividir. **Evidència:** codi comentat + captura del REPL amb els missatges rebuts i la mitjana calculada correctament des de la primera lectura.

**Per què és una bona entrada:** usa el **vocabulari clau** (protocol, prefix, interval d'enviament), explica *el com* (per què cal comprovar la llista buida) i és **honesta amb el dubte** (l'error de divisió per zero al primer intent) i com es va resoldre.

---

*Exemple resolt de la SA8. Model de treball per a l'alumnat (alliberament gradual: es mostra després del primer intent). Es recolza en `codi/telemetria_radio` i `codi/estacio_base`. El producte «sistema de telemetria del rover» real l'has de fer amb el **teu** rover, no amb aquest. Llicència CC BY-SA 4.0.*
