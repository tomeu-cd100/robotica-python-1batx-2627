# SA3 · Exemple resolt (model «jo ho faig») — Munto i programo un rec automàtic de test amb sensor d'humitat simulat

> 🧑‍🎓 **Quan toca mirar-lo?** Després del teu **primer intent** amb `nivell_llum.py`/`termometre.py` (S2) — mai abans. És un problema **anàleg** per veure *com es pensa*, no una solució per copiar: el repte «mascota reactiva» l'has de fer amb el **teu** disseny.

> 🔗 **D'on ve i on va.** Aquest exemple és el **bessó comentat** de les pràctiques [`nivell_llum`](codi/nivell_llum/EXPLICACIO.md) i [`termometre`](codi/termometre/EXPLICACIO.md): la mateixa idea (llegir un sensor analògic → mapar/comparar → decidir) amb un context expressament diferent — un **avisador de rec** en lloc d'un indicador de llum — perquè vegis **com es pensa**, no per copiar-lo. Quan l'hagis entès, torna a `mascota_reactiva` i fes el **teu** repte.

> **Nota docent:** mostra'l **després del primer intent** amb `nivell_llum.py` i `termometre.py`, mai abans. No és la solució del repte «mascota reactiva» (que cada alumne/a fa amb el **seu** disseny): és un problema **anàleg** resolt pas a pas perquè l'alumnat vegi *com es pensa* una entrada analògica interpretada amb condicionals, no què s'ha de copiar. Comenta en veu alta el pas «🧭 Com ho penso» (per què calibrar amb el REPL abans de fixar el llindar) i el «⚠️ Contraexemple».

---

## 🔑 El repte model

> Un hort automatitzat necessita avisar quan la terra està massa seca, sense encara connectar la bomba de reg (això arribarà a la SA6, control). Reprodueixo aquest avisador amb el **sensor de llum del Kit 2** fent temporalment de "sensor d'humitat simulat" (un valor analògic baix = "sec", com faria un sensor d'humitat real): si la lectura baixa d'un llindar, la cara del display mostra alarma i sona un avís.

Fa servir només conceptes de la SA3: entrada **analògica** (`read_analog()`, 0-1023) mapada amb la funció `mapa()` (S2) i **condicionals** per decidir una reacció (com a `nivell_llum.py`/`termometre.py`). Maquinari: sensor de llum extern al Micro:shield (Kit 2), el mateix muntatge de `nivell_llum.py`.

---

## 🧭 Com ho penso (abans d'escriure res)

1. **Analitzo:** necessito una lectura analògica (0-1023) i una decisió binària ("sec" o "bé"): és exactament el patró de `termometre.py` (llegir → comparar amb un llindar → decidir), no el de barres de `nivell_llum.py`.
2. **Trio el llindar SENSE inventar-lo:** abans d'escriure cap `if`, connecto el sensor i llegeixo el valor real al **REPL** en diverses condicions (tapat = "sec" simulat, destapat = "bé" simulat). Només amb aquests dos valors reals decideixo on posar el llindar, a mig camí entre tots dos.
3. **Decideixo la reacció:** cara de "alarma" (`Image.SAD`) + un to curt, només **quan canvia** l'estat (no a cada volta del bucle, per no repetir el so sense parar).
4. **🔮 PREDIU (fes-ho tu abans de llegir el codi):** si el llindar és `400` i el sensor llegeix `250`, la cara mostrarà… ☐ **alarma (sec)** ☐ contenta (bé) ☐ no canvia mai. I si després puja a `600`?

---

## 💡 La solució anotada

```python
# SA3 - exemple_rec_automatic.py  (EXEMPLE MODEL, no es el producte)
# Avisa quan un sensor analogic (aqui, el de llum del Kit 2 fent de sensor
# d'humitat simulat) baixa per sota d'un llindar calibrat amb el REPL.
# Maquinari: sensor de llum extern al pin P3 del Micro:shield (Kit 2),
# com a nivell_llum.py.

from microbit import *
import music

LLINDAR_SEC = 400   # calibrat al REPL: mitjana entre "tapat" i "destapat"

estat_anterior = None   # cap estat encara: forcem que la primera lectura avisi


while True:
    lectura = pin3.read_analog()   # 0-1023

    if lectura < LLINDAR_SEC:
        estat = "sec"
    else:
        estat = "be"

    if estat != estat_anterior:   # NOMES actua quan l'estat CANVIA
        estat_anterior = estat
        if estat == "sec":
            display.show(Image.SAD)
            music.pitch(300, 200, pin=pin2)
        else:
            display.show(Image.HAPPY)

    sleep(200)
```

**Per què està escrit així (🌟):**
- **Llindar mesurat, no inventat:** `LLINDAR_SEC = 400` ve de comparar valors reals llegits al REPL, no d'un número a l'atzar — el mateix mètode que calibraràs a `mascota_reactiva.py`.
- **`estat_anterior` evita repetir la reacció:** sense aquesta variable, el so sonaria **a cada volta** del bucle mentre estigués "sec" (cada 200 ms), no només quan canvia — exactament el mateix problema que resol `canvia_emocio()` a la mascota.
- **Dues branques clares (`if`/`else`), un únic llindar:** és el patró més senzill possible; la mascota farà el mateix però amb **diversos** llindars i sensors alhora.

---

## 🔬 Provo i mesuro

- **Predicció ✔:** amb llindar `400` i lectura `250` (< 400), la cara mostra **alarma** ("sec"); a `600` (≥ 400) torna a "bé".
- **Mesuro amb el REPL:** abans de fixar `LLINDAR_SEC`, escric `pin3.read_analog()` diverses vegades tapant i destapant el sensor, i anoto els dos valors extrems; el llindar és el punt mig entre tots dos, no un número "rodó" triat a ull.
- **Sense maquinari:** la **lògica** (canvi d'estat, condicional) es pot revisar llegint el codi, però la lectura real del sensor **només** es veu amb el component físic connectat (el simulador de python.microbit.org no reprodueix sensors externs).

---

## ⚠️ Contraexemple (errors típics i com es detecten)

- **Trio el llindar "a ull" sense mesurar res:** el programa sembla funcionar a casa però falla a l'aula (llum ambiental diferent). **Pista:** sempre mesura els dos extrems reals al REPL abans de fixar cap número.
- **Oblido `estat_anterior` i comparo `lectura` directament dins l'`if` cada volta:** el so sona sense parar mentre estigui "sec", no només al canviar. **Pista:** si una reacció només ha de passar **un cop** en entrar a un estat, cal una variable que recordi l'estat anterior.
- **Confonc el llindar amb l'escala 0-255 dels sensors interns:** el sensor extern (pin ADC) sempre dona 0-1023, no 0-255. **Pista:** repassa quina funció retorna quin rang abans de triar el llindar.
- **El programa no reacciona mai:** el component és a un pin **sense ADC** (fora de P0/P1/P2/P3/P4/P10). **Pista:** repassa la taula de l'[esquema](SA3_esquemes_connexions.md) §1.

---

## 📔 Diari de bord (entrada model, 1a persona)

> **Sessions 2-3:** He après la diferència entre llegir un sensor analògic (`read_analog()`, 0-1023) i **decidir** què fer amb la lectura amb un `if`/`else`. He analitzat un avisador de rec: el sensor de llum fent de "sensor d'humitat simulat" avisa quan la lectura baixa d'un llindar. Vaig **predir** que amb llindar 400 i lectura 250 sortiria l'alarma, i es va complir. Al principi el so em sonava sense parar mentre estava "sec": l'error va ser no adonar-me que necessitava recordar l'**estat anterior** per actuar només quan canvia, no a cada volta del bucle. **Evidència:** codi comentat + els dos valors extrems mesurats al REPL abans de fixar el llindar.

**Per què és una bona entrada:** usa el **vocabulari clau** (entrada analògica, llindar calibrat, canvi d'estat), explica *el com* (per què cal mesurar abans de decidir un llindar), i és **honesta amb la dificultat** (el so repetit) i com es va resoldre.

---

*Exemple resolt de la SA3. Model de treball per a l'alumnat (alliberament gradual: es mostra després del primer intent). Es recolza en `codi/nivell_llum` i `codi/termometre`. El repte «mascota reactiva» real l'has de fer amb el **teu** disseny, no amb aquest. Llicència CC BY-SA 4.0.*
