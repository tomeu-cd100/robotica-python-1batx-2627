# SA5 · Exemple resolt (model «jo ho faig») — Un timbre d'avís per ràdio

> 🧑‍🎓 **Quan toca mirar-lo?** Després del teu **primer intent** amb `radio_missatges.py`/`comandament.py` (S1-S2) — mai abans. És un problema **anàleg** per veure *com es pensa*, no una solució per copiar: el repte «control remot bàsic» l'has de fer amb el **teu** protocol.

> 🔗 **D'on ve i on va.** Aquest exemple és el **bessó comentat** de les pràctiques [`radio_missatges`](codi/radio_missatges/EXPLICACIO.md) i [`comandament`](codi/comandament/EXPLICACIO.md): la mateixa idea (protocol amb prefix + esdeveniment → acció) amb un context expressament diferent — un **timbre d'avís** en lloc del vehicle — perquè vegis **com es pensa**, no per copiar-lo. Quan l'hagis entès, torna a `receptor_vehicle` i fes el **teu** repte.

> **Nota docent:** mostra'l **després del primer intent** amb `radio_missatges.py` i `comandament.py`, mai abans. No és la solució del repte «control remot bàsic» (que cada alumne/a fa amb el **seu** protocol): és un problema **anàleg** resolt pas a pas perquè l'alumnat vegi *com es pensa* el disseny d'un protocol de ràdio amb prefix, no què s'ha de copiar. Comenta en veu alta el pas «🧭 Com ho penso» (per què cal un prefix) i el «⚠️ Contraexemple».

---

## 🔑 El repte model

> Vull que una placa faci de **timbre**: quan es prem el seu botó A, envia un avís per ràdio, i qualsevol altra placa del mateix grup que porti el meu programa "sona" (mostra una cara i fa un so) en rebre'l. Vull distingir aquest avís de qualsevol altre missatge de ràdio que pugui circular (per exemple, d'un altre grup de la classe fent altres proves).

Fa servir només conceptes de la SA5: **ràdio** (`radio.on()`, `radio.config(group=...)`, `send()`/`receive()`) i un **protocol** amb prefix. Maquinari: cap component nou, dues micro:bit V2 amb ràdio interna.

---

## 🧭 Com ho penso (abans d'escriure res)

1. **Analitzo:** si totes les plaques de la classe estan al mateix grup i qualsevol enviés qualsevol text, com sabria la meva placa que un missatge concret és "el meu avís de timbre" i no el xat d'un altre?
2. **Decideixo el protocol:** faig servir un prefix propi, per exemple `"TIMBRE:"`, seguit del nom de qui truca. Així un missatge com `"TIMBRE:Marc"` és inconfusible amb qualsevol altre text.
3. **Separo emissor i receptor:** l'emissor només necessita `radio.send()` quan es prem el botó; el receptor necessita comprovar **cada** missatge rebut amb `startswith()` abans de "sonar".
4. **🔮 PREDIU (fes-ho tu abans de llegir el codi):** si el receptor rebés el missatge `"Timbre:Marc"` (amb minúscula a la "t"), sonaria igualment? ☐ Sí, és el mateix text ☐ No, `startswith()` distingeix majúscules de minúscules.

---

## 💡 La solució anotada

```python
# SA5 - exemple_timbre_radio.py  (EXEMPLE MODEL, no es el producte)
# Protocol propi amb prefix per distingir un avis de qualsevol altre
# text que pugui circular pel mateix grup de radio.
# Maquinari: cap de nou, nomes la radio interna de dues micro:bit V2.

from microbit import *
import radio

GRUP = 5   # el grup assignat pel docent per a aquesta parella de proves
PREFIX = "TIMBRE:"
MEU_NOM = "Marc"

radio.on()
radio.config(group=GRUP, power=6)


def truca():
    # Funcio SENSE parametres: sempre envia el mateix tipus de missatge,
    # nomes canvia si es crida o no.
    radio.send(PREFIX + MEU_NOM)
    display.show(Image.YES)
    sleep(200)
    display.clear()


while True:
    if button_a.was_pressed():
        truca()
    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        # Nomes "sona" si el missatge segueix EXACTAMENT el protocol.
        qui_truca = missatge[len(PREFIX):]
        display.scroll(qui_truca)
        music.play(music.DADADADUM)
    sleep(20)
```

**Per què està escrit així (🌟):**
- **El prefix és una constant amb nom:** `PREFIX = "TIMBRE:"` s'escriu **un** cop; si mai calgués canviar-lo, només cal tocar una línia, no cercar-lo per tot el programa.
- **`startswith()` protegeix contra falsos positius:** sense aquesta comprovació, qualsevol missatge del grup (per exemple, un xat d'un altre exercici) faria "sonar" el timbre per error.
- **Emissor i receptor comparteixen exactament el mateix `PREFIX`:** és el mateix principi que `comandament.py`/`receptor_vehicle.py`: el protocol és un **acord**, no funciona si cadascú l'escriu diferent.

---

## 🔬 Provo i mesuro

- **Predicció ✔:** `"Timbre:Marc"` (amb minúscula) **no** activa el timbre, perquè `startswith("TIMBRE:")` distingeix majúscules de minúscules; és exactament el mateix parany que amb el `PREFIX` de `comandament.py`.
- **Provo cada extrem per separat:** abans de confiar que "no funciona", mostro al display el missatge sencer rebut (`display.scroll(missatge)`) sense filtrar-lo pel prefix, per comprovar que **arriba** alguna cosa abans de sospitar del filtre.
- **Sense maquinari:** la lògica del protocol es pot revisar al simulador de python.microbit.org (que sí simula la ràdio entre instàncies), però cal dues instàncies obertes per veure-ho de veritat.

---

## ⚠️ Contraexemple (errors típics i com es detecten)

- **Emissor i receptor amb `PREFIX` diferent (una lletra de diferència):** el programa no dona cap error, però el timbre **mai** sona. **Pista:** copia el `PREFIX` literalment d'una placa a l'altra, no el reescriguis a mà.
- **Oblidar `radio.on()` en una de les dues plaques:** aquesta placa no envia ni rep res, però tampoc dona error. **Pista:** revisa que **totes dues** plaques hagin cridat `radio.on()` al principi.
- **Grup diferent entre les dues plaques:** cap missatge arriba mai, com si la ràdio no funcionés. **Pista:** comprova el número de `GRUP` a la taula que dona el docent.
- **Comprovar el prefix amb `==` en lloc de `startswith()`:** si el missatge porta res després del nom (per exemple, un espai final), la comparació falla encara que sembli "el mateix" text. **Pista:** `startswith()` només mira l'inici, és més robust per a protocols amb contingut variable després del prefix.

---

## 📔 Diari de bord (entrada model, 1a persona)

> **Sessions 1-2:** He après a dissenyar un **protocol** senzill per ràdio: un prefix fix (`"TIMBRE:"`) que distingeix el meu missatge de qualsevol altre text que pugui circular pel mateix grup. Vaig **predir** que un prefix amb una lletra diferent (majúscula/minúscula) no activaria el timbre, i es va complir. Al principi no rebia res: l'error va ser que havia oblidat cridar `radio.on()` en una de les dues plaques, no el protocol en si. Ho vaig trobar comprovant **cada extrem per separat** (mostrant el missatge sencer abans de filtrar-lo). **Evidència:** codi comentat + prova aparellada amb un company, amb captura del display mostrant el nom rebut.

**Per què és una bona entrada:** usa el **vocabulari clau** (ràdio, grup, protocol, prefix), explica *el com* (per què calia `startswith()` i no `==`), i és **honesta amb el dubte** (per què no rebia res al principi) i com es va resoldre.

---

*Exemple resolt de la SA5. Model de treball per a l'alumnat (alliberament gradual: es mostra després del primer intent). Es recolza en `codi/radio_missatges` i `codi/comandament`. El repte «control remot bàsic» real l'has de fer amb el **teu** protocol, no amb aquest. Llicència CC BY-SA 4.0.*
