# SA6 · Exemple resolt (model «jo ho faig») — Una cinta transportadora amb aturada d'emergència

> 🧑‍🎓 **Quan toca mirar-lo?** Després del teu **primer intent** amb `maquina_estats_semafor.py`/`termostat_histeresi.py` (S1) — mai abans. És un problema **anàleg** per veure *com es pensa*, no una solució per copiar: el repte «vehicle amb aturada d'emergència» l'has de fer amb el **teu** vehicle.

> 🔗 **D'on ve i on va.** Aquest exemple és el **bessó comentat** de les pràctiques [`maquina_estats_semafor`](codi/maquina_estats_semafor/EXPLICACIO.md) i [`vehicle_seguretat`](codi/vehicle_seguretat/EXPLICACIO.md): la mateixa idea (màquina d'estats amb STOP prioritari) amb un context expressament diferent — una **cinta transportadora** en lloc del vehicle — perquè vegis **com es pensa**, no per copiar-lo. Quan l'hagis entès, torna a `vehicle_seguretat` i fes el **teu** repte.

> **Nota docent:** mostra'l **després del primer intent** amb la FSM del semàfor, mai abans. No és la solució del repte «vehicle amb aturada d'emergència» (que cada alumne/a fa amb el **seu** vehicle): és un problema **anàleg** resolt pas a pas perquè l'alumnat vegi *com es pensa* una màquina d'estats amb aturada prioritària, no què s'ha de copiar. Comenta en veu alta el pas «🧭 Com ho penso» (per què l'STOP no és "una comanda més") i el «⚠️ Contraexemple».

---

## 🔑 El repte model

> Vull simular una **cinta transportadora** d'un petit magatzem: un motor la fa avançar mentre està en marxa, i té un **polsador d'emergència** visible que, si es prem, atura la cinta **a l'instant**, encara que en aquell moment estigués rebent l'ordre de continuar. La cinta només torna a arrencar amb una ordre explícita de "marxa", mai sola.

Fa servir només conceptes de la SA6: **màquina d'estats** (RUN/STOP), **aturada prioritària** per polsador i un **LED** que mostra l'estat. Maquinari: micro:bit V2, un LED com a simulació del motor (fix = en marxa, apagat = aturada) i un polsador extern.

---

## 🧭 Com ho penso (abans d'escriure res)

1. **Analitzo:** si comprovés el polsador només "de tant en tant" (per exemple, cada 10 voltes del bucle), hi hauria un interval de temps en què la cinta seguiria "en marxa" encara que el polsador estigués premut. Per a una aturada d'emergència, això **no és acceptable**.
2. **Decideixo l'estructura:** una variable d'estat (`RUN`/`STOP`) i una única funció `actualitza_estat()` que centralitza tot el que passa en canviar d'estat (motor, LED, display).
3. **Decideixo l'ordre del bucle:** el polsador es comprova **sempre primer**, abans de mirar cap altra entrada (aquí, el botó A com a simulació d'una "ordre de marxa" per ràdio).
4. **🔮 PREDIU (fes-ho tu abans de llegir el codi):** si el polsador es comprovés **després** del botó A dins del mateix bucle, i tots dos es prement quasi alhora, què podria passar en el pitjor cas? ☐ Res, l'ordre no importa ☐ Podria "colar-se" una arrencada abans de processar l'aturada.

---

## 💡 La solució anotada

```python
# SA6 - exemple_cinta_transportadora.py  (EXEMPLE MODEL, no es el producte)
# Maquina d'estats RUN/STOP amb aturada d'emergencia prioritaria, aplicada a
# una cinta transportadora simulada (LED = motor, boto A = "ordre de marxa").
# Maquinari: LED al pin1 (simula el motor), polsador extern al pin12
# (pull-up, com el del vehicle).

from microbit import *

LED_MOTOR = pin1
POLSADOR_EMERGENCIA = pin12
POLSADOR_EMERGENCIA.set_pull(POLSADOR_EMERGENCIA.PULL_UP)   # sense aixo la
# lectura flota; amb pull-up intern: repos = 1, premut = 0 (LOW)

RUN, STOP = range(2)
estat = STOP


def actualitza_estat(nou):
    # Unic lloc que canvia "estat": aixi cap altra part del programa pot
    # "oblidar-se" d'apagar el motor en entrar a STOP.
    global estat
    if nou == STOP:
        LED_MOTOR.write_digital(0)
        display.show(Image.NO)
    else:
        LED_MOTOR.write_digital(1)
        display.show(Image.YES)
    estat = nou


actualitza_estat(STOP)

while True:
    # 1a comprovacio de cada volta: el polsador d'emergencia, SEMPRE abans
    # de mirar cap altra entrada.
    if not POLSADOR_EMERGENCIA.read_digital():
        actualitza_estat(STOP)
    elif button_a.was_pressed() and estat == STOP:
        actualitza_estat(RUN)   # nomes arrenca amb una ordre explicita

    sleep(20)
```

**Per què està escrit així (🌟):**
- **El polsador es comprova primer, sense excepcions:** és la garantia que l'aturada d'emergència mai queda "endarrerida" per cap altra comprovació del bucle.
- **`actualitza_estat()` és l'únic lloc que toca el motor:** si en el futur calgués afegir un tercer estat (per exemple, ALERTA per un sensor de pes), només caldria ampliar aquesta funció, no buscar per tot el programa on s'encén/apaga el LED.
- **STOP -> RUN necessita una ordre explícita:** la cinta no torna a arrencar sola després d'una emergència; cal el botó A de nou, exactament com el vehicle necessita una ordre F/B/L/R explícita per sortir de STOP.

---

## 🔬 Provo i mesuro

- **Predicció ✔:** si el polsador es comprovés **després** del botó A, hi hauria una finestra (per petita que fos) en què una arrencada es podria processar just abans de l'aturada, encara que el polsador ja estigués premut; és exactament el mateix parany que amb l'STOP del vehicle real.
- **Provo cada extrem per separat:** primer verifico que el LED s'encén/apaga correctament amb el botó A sol (sense tocar el polsador), i després que el polsador atura la cinta **des de qualsevol estat**, fins i tot just després d'una ordre de marxa.
- **Sense maquinari:** la lògica de la FSM (sense el LED físic) es pot revisar al simulador de python.microbit.org substituint el polsador extern pel botó B, per exemple.

---

## ⚠️ Contraexemple (errors típics i com es detecten)

- **Comprovar el polsador després d'altres condicions:** el programa no dona cap error, però hi ha un instant en què l'aturada "no es nota". **Pista:** el polsador ha de ser el **primer** `if` del bucle, sempre.
- **Canviar `estat` directament (`estat = RUN`) en lloc de cridar `actualitza_estat()`:** el LED es queda desincronitzat amb la variable d'estat real. **Pista:** tot canvi d'estat ha de passar **sempre** per la mateixa funció.
- **Deixar que la cinta torni a RUN sola quan el polsador es deixa d'estar premut:** és perillós (una emergència real no s'hauria de resoldre sola, sense intervenció humana). **Pista:** STOP només es surt amb una ordre explícita nova, mai automàticament.
- **Oblidar el `pull-up` intern del polsador:** sense pull-up, la lectura "flota" i pot donar falsos positius (o falsos negatius) d'emergència. **Pista:** cal configurar-lo explícitament amb `pin.set_pull(pin.PULL_UP)` abans del bucle, exactament com fa `vehicle_seguretat.py` amb el polsador del vehicle (pin12) i com ja s'ensenyava a la SA3.

---

## 📔 Diari de bord (entrada model, 1a persona)

> **Sessió 1-2:** He après a construir una **màquina d'estats amb aturada prioritària**: la clau no és només "tenir un botó d'aturada", sinó **on** i **com** es comprova dins del bucle. Vaig **predir** que comprovar el polsador després d'una altra condició podria deixar una finestra perillosa, i en provar-ho amb el botó A vaig veure que, efectivament, hi havia un cas (prémer els dos gairebé alhora) en què l'ordre de comprovació canviava el resultat. Ho vaig resoldre posant el polsador com la **primera** comprovació del bucle, sense excepcions. **Evidència:** codi comentat + prova amb el LED i el polsador, amb una nota al quadern explicant per què l'ordre de les comprovacions importa.

**Per què és una bona entrada:** usa el **vocabulari clau** (estat, transició, prioritat), explica *el com* (per què l'ordre de les comprovacions és crític) i és **honesta amb el dubte** (el cas del prémer gairebé simultani) i com es va resoldre.

---

*Exemple resolt de la SA6. Model de treball per a l'alumnat (alliberament gradual: es mostra després del primer intent). Es recolza en `codi/maquina_estats_semafor` i `codi/vehicle_seguretat`. El repte «vehicle amb aturada d'emergència» real l'has de fer amb el **teu** vehicle, no amb aquest. Llicència CC BY-SA 4.0.*
