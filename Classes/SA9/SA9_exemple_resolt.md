# SA9 · Exemple resolt (model «jo ho faig») — Un mini-projecte anàleg complet

> 🧑‍🎓 **Quan toca mirar-lo?** Després d'haver **triat el teu repte** (S1) i fet un primer intent de prototip (S2) — mai abans. No és un repte del [banc](SA9_reptes_proposats.md) per copiar: és un problema **anàleg** senzill perquè vegis *com es pensa i es documenta* un projecte de síntesi, no una solució per calcar.

> 🔗 **D'on ve i on va.** Aquest exemple resol un mini-repte **fora del banc** (un "avisador de porta oberta" amb només la placa micro:bit, sense rover) perquè vegis el cicle sencer —idear → prototipar → provar i millorar → comunicar— aplicat a un problema petit, abans d'aplicar-lo tu al **teu** repte, més gran, amb el rover.

> **Nota docent:** mostra'l **després del primer prototip** de cadascú. Comenta en veu alta el pas «🧭 Com ho penso» (per què cal fixar els requisits abans de programar) i el «⚠️ Contraexemple».

---

## 🔑 El repte model

> Vull un dispositiu que avisi (llum + so) quan algú obre una porta, i que compti quantes vegades s'ha obert des que s'ha engegat. És l'anàleg d'un sentinella PIR del banc de reptes, però amb el **polsador** com a simulador de "porta oberta" (sense el rover ni el PIR), perquè el cicle complet es pugui veure en poc temps.

Fa servir només conceptes que ja coneixes de tot el curs: **entrada digital amb antirebot** (SA3), **una FSM senzilla** (SA6), **comptador acumulador** (SA1-SA2) i **registre amb `log`** (SA6/SA8). Maquinari: només la micro:bit V2 (botó A com a "porta"), sense Kit ni rover.

---

## 🧭 Com ho penso (abans d'escriure res)

1. **Idear:** el requisit mínim és "avisar (llum+so) i comptar les obertures". Ho escric **abans** de tocar el codi, perquè si no, acabo programant coses que no calien.
2. **Prototipar:** parteixo de l'estructura percep/decideix/actua de `plantilla_projecte.py`: `percep()` llegeix el botó, `decideix()` decideix si és una "obertura nova", `actua()` fa sonar/llampegar i actualitza el comptador.
3. **🔮 PREDIU (fes-ho tu abans de llegir el codi):** si compto "una obertura" cada volta del bucle en què el botó està premut (sense antirebot ni control d'estat), què passarà amb el comptador en una sola pressió llarga? ☐ Comptarà 1 ☐ Comptarà moltes vegades seguides.

---

## 💡 La solució anotada

```python
# SA9 - exemple_avisador_porta.py  (EXEMPLE MODEL, no es el producte)
# Avisa (llum+so) quan es "obre la porta" (boto A) i en compta les vegades,
# amb el mateix cicle idear/prototipar/provar/comunicar que el projecte
# real: aqui nomes amb el boto A com a simulacio del PIR d'un sentinella.

from microbit import *

comptador = 0
porta_oberta_abans = False   # variable d'estat: evita comptar la mateixa
                              # obertura mes d'un cop (antirebot per estat)


def percep():
    return button_a.is_pressed()


def decideix(porta_oberta_ara):
    global porta_oberta_abans
    es_obertura_nova = porta_oberta_ara and not porta_oberta_abans
    porta_oberta_abans = porta_oberta_ara
    return es_obertura_nova


def actua(es_obertura_nova):
    global comptador
    if es_obertura_nova:
        comptador += 1
        display.show(Image.HAPPY)
        music.play(['C4:2'], wait=False)
        sleep(150)
        display.clear()


while True:
    porta_oberta_ara = percep()
    es_obertura_nova = decideix(porta_oberta_ara)
    actua(es_obertura_nova)
    sleep(20)
```

**Per què està escrit així (🌟):**
- **`porta_oberta_abans` és la clau:** sense aquesta variable d'estat, mantenir premut el botó comptaria "moltes obertures" en una sola pressió (el mateix problema que l'antirebot per software de SA3, aplicat aquí a un sensor booleà en lloc d'un comptador de premudes).
- **`percep()`/`decideix()`/`actua()` separades:** exactament l'arquitectura de `plantilla_projecte.py`. Si el comptador anés malament, sabria si mirar `percep()` (el botó no es llegeix bé) o `decideix()` (la lògica d'"obertura nova" és incorrecta).
- **`actua()` només actua si `es_obertura_nova` és cert:** separa la "detecció" de la "resposta", igual que a `comportaments.py` (SA8) l'estat i l'acció es tracten per separat.

---

## 🔬 Provo i mesuro

- **Predicció ✔:** sense `porta_oberta_abans`, una sola pressió llarga del botó comptaria desenes d'"obertures" (una per cada volta del bucle, cada ~20 ms). Amb la variable d'estat, compta **exactament una vegada** per pressió.
- **Provo cada extrem per separat:** primer verifico que `percep()` retorna `True`/`False` correctament (amb `print()`), després que `decideix()` només retorna `True` a la transició, i finalment que `actua()` incrementa el comptador.
- **Prova de límit:** deixo el botó premut 10 segons seguits i comprovo que el comptador **no** s'incrementa més d'un cop; després el deixo anar i el torno a prémer, i comprovo que sí que compta la segona vegada.

---

## ⚠️ Contraexemple (errors típics i com es detecten)

- **Comptar a cada volta del bucle en què el botó està premut** (sense `porta_oberta_abans`): una sola pressió es compta desenes de vegades. **Pista:** compara el valor del comptador després d'una pressió curta i d'una de llarga; si canvien molt, falta l'antirebot per estat.
- **Barrejar la detecció i l'acció en una sola funció:** fa més difícil saber si el problema és de lectura o de resposta quan alguna cosa falla. **Pista:** si no pots dir "el problema és a `percep`, `decideix` o `actua`" en menys de 10 segons, probablement les tres coses estan barrejades.
- **No fixar el requisit mínim abans de programar:** l'alumnat que comença a programar sense haver escrit "què ha de fer com a mínim" acaba afegint funcionalitats que no calien i li falta temps per al que sí que calia. **Pista:** si el prototip de la S2 no es pot explicar en una frase, encara no hi ha requisit clar.

---

## 📔 Diari de bord (entrada model, 1a persona)

> **Idear:** vaig escriure el requisit mínim ("avisar i comptar") abans de tocar el codi. **Prototipar:** vaig partir de `plantilla_projecte.py` i vaig omplir `percep()`/`decideix()`/`actua()`. **Provar:** vaig **predir** que sense controlar l'estat, una pressió llarga comptaria moltes vegades, i en provar-ho (abans d'afegir `porta_oberta_abans`) vaig veure que, efectivament, el comptador pujava molt ràpid amb el botó premut. Ho vaig resoldre afegint la variable d'estat. **Evidència:** codi comentat + captura del REPL amb el comptador abans i després de la correcció.

**Per què és una bona entrada:** usa el **vocabulari clau** (variable d'estat, antirebot, percep/decideix/actua), explica *el com* (per què calia l'estat) i és **honesta amb el dubte** (l'error del comptador disparat) i com es va resoldre — exactament el que ha d'aparèixer al [dossier tècnic](SA9_dossier_plantilla.md) §6.

---

*Exemple resolt de la SA9. Model de treball per a l'alumnat (alliberament gradual: es mostra després del primer prototip). Es recolza en `codi/plantilla_projecte`. El teu producte real («rover ampliat amb el repte lliure») l'has de fer amb el **teu** rover i el **teu** repte, no amb aquest exemple. Llicència CC BY-SA 4.0.*
