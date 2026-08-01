# SA2 · Exemple resolt (model «jo ho faig») — Munto i programo l'indicador de càrrega d'un carregador intel·ligent

> 🧑‍🎓 **Quan toca mirar-lo?** Després del teu **primer intent** amb `led_parpelleig.py` (S1) i amb `pwm_led_rgb.py`/`musica_altaveu.py` (S2) — mai abans. És un problema **anàleg** per veure *com es pensa*, no una solució per copiar: el repte «semàfor o llum d'ambient» l'has de fer amb el **teu** disseny.

> 🔗 **D'on ve i on va.** Aquest exemple és el **bessó comentat** de les pràctiques [`led_parpelleig`](codi/led_parpelleig/EXPLICACIO.md) i [`pwm_led_rgb`](codi/pwm_led_rgb/EXPLICACIO.md): la mateixa idea (sortida digital + PWM + bucles) amb un context expressament diferent — l'**indicador de càrrega** d'un carregador intel·ligent en lloc d'un LED solt — perquè vegis **com es pensa**, no per copiar-lo. Quan l'hagis entès, torna a `semafor_rele` i fes el **teu** repte.

> **Nota docent:** mostra'l **després del primer intent** amb `led_parpelleig.py` i `pwm_led_rgb.py`, mai abans. No és la solució del repte «semàfor o llum d'ambient» (que cada alumne/a fa amb el **seu** disseny): és un problema **anàleg** resolt pas a pas perquè l'alumnat vegi *com es pensa* una sortida amb estats, no què s'ha de copiar. Comenta en veu alta el pas «🧭 Com ho penso» (per què digital per uns estats i PWM per uns altres) i el «⚠️ Contraexemple».

---

## 🔑 El repte model

> Molts carregadors "intel·ligents" (mòbil, portàtil...) tenen un **LED d'estat** que diu com va la càrrega sense que calgui mirar la pantalla: parpelleja mentre carrega i es queda **fix** quan ja està al 100%. Reprodueixo aquest comportament amb un **LED extern** al Micro:shield: parpelleja N vegades (simulant "encara carregant") i després es queda **encès a mitja intensitat amb PWM** (simulant "ja ha acabat, mode estalvi").

Fa servir només conceptes de la SA2: sortida **digital** (`write_digital`) amb bucles i acumulador (S1) i sortida **PWM** (`write_analog`) (S2). Maquinari: LED extern al Micro:shield (Kit 1), el mateix muntatge de `led_parpelleig.py`.

---

## 🧭 Com ho penso (abans d'escriure res)

1. **Analitzo:** el carregador té dos "modes" molt diferents: **carregant** (parpelleig ràpid, avisa que està actiu) i **acabat** (llum fixa suau, no cal cridar l'atenció). Són dos comportaments amb propòsits diferents → probablement necessiten dos tipus de sortida diferents.
2. **Trio digital o PWM per a cada mode:**
   - **Carregant** → el LED només ha d'estar **encès o apagat**, alternant: és un comportament de dos estats → **digital** (`write_digital`), igual que `led_parpelleig.py`.
   - **Acabat** → vull una llum **fixa però no enlluernadora** (estalvi): un valor intermedi entre 0 i 1023 → **PWM** (`write_analog`), igual que a `pwm_led_rgb.py`.
3. **Compto els parpellejos amb un acumulador:** com que "carregant" ha de durar un nombre **concret** de parpellejos (no per sempre), faig servir un `for i in range(n):` en lloc d'un `while True:` per a aquesta part.
4. **🔮 PREDIU (fes-ho tu abans de llegir el codi):** amb `for i in range(5):` i un `write_digital(1)`/`write_digital(0)` amb `sleep(300)` a cada estat, el LED parpellejarà… ☐ **5 vegades exactes** ☐ 10 vegades ☐ per sempre. I després, `pin1.write_analog(300)` deixarà el LED… ☐ apagat ☐ **a una intensitat baixa i fixa** ☐ parpellejant.

---

## 💡 La solució anotada

```python
# SA2 - exemple_carregador.py  (EXEMPLE MODEL, no es el producte)
# Indicador d'un carregador intel·ligent: parpelleja mentre "carrega" i es
# queda fix a mitja intensitat quan "acaba" (mode estalvi).
# Maquinari: LED extern al pin P1 del Micro:shield (Kit 1), com a led_parpelleig.py.

from microbit import *

PARPELLEJOS_CARREGA = 5   # quantes vegades parpelleja mentre "carrega"


def carregant():
    # Sortida DIGITAL amb bucle comptat: nomes dos estats, un nombre fix de cops.
    for i in range(PARPELLEJOS_CARREGA):
        pin1.write_digital(1)   # LED ences
        sleep(300)
        pin1.write_digital(0)   # LED apagat
        sleep(300)


def acabat():
    # Sortida PWM: intensitat fixa i suau (mode estalvi), no encesa/apagada.
    pin1.write_analog(300)   # ~30% de la intensitat maxima (0-1023)


while True:
    carregant()
    acabat()
    sleep(3000)   # es queda "acabat" 3 s abans de tornar a simular una carrega
```

**Per què està escrit així (🌟):**
- **Dues funcions, un propòsit cadascuna** (`carregant()`, `acabat()`): es llegeix com una frase (*"primer carrega, després acaba"*) sense haver d'entrar en el detall de cada `sleep()`.
- **`for` comptat per a "carregant"**: el nombre de parpellejos és una dada coneguda (`PARPELLEJOS_CARREGA`), no infinita: és exactament el cas d'ús d'un `for i in range(n):`, no d'un `while True:`.
- **PWM només on calia un valor intermedi**: si haguéssim fet servir `write_digital` per a l'"acabat" fix, només podríem triar entre apagat i **màxima** intensitat — no l'efecte suau d'estalvi.

---

## 🔬 Provo i mesuro

- **Predicció ✔:** el LED parpelleja **exactament 5 vegades** (el `for` no és infinit) i després es queda **encès i fix a intensitat baixa** (no parpelleja, no s'apaga).
- **Mesuro amb el REPL:** si dic `pin1.write_analog(300)` directament al REPL abans d'escriure el programa, veig l'efecte **a l'instant** i puc ajustar el número (per exemple, `150` és més tènue, `800` gairebé com `write_digital(1)`) abans de decidir el valor final.
- **Sense maquinari:** la **lògica** (nombre de parpellejos, ordre de funcions) es pot revisar llegint el codi o comentant "aquí s'encendria/apagaria" al simulador, però l'efecte de PWM **real** només es veu amb el LED físic connectat (el simulador de python.microbit.org no reprodueix components externs).

---

## ⚠️ Contraexemple (errors típics i com es detecten)

- **Faig servir `while True:` per als 5 parpellejos:** el LED no s'atura mai de parpellejar i el programa no arriba mai a `acabat()`. **Pista:** si el nombre de repeticions és **conegut i fix**, cal `for i in range(n):`, no `while True:`.
- **Confonc `write_analog(300)` amb "30 de 100":** l'escala és **0-1023**, no 0-100 ni 0-255; `300` és més aviat un 30% de la intensitat màxima. **Pista:** sempre que dubtis de l'escala, prova el valor al REPL abans de decidir.
- **Poso `write_analog()` a un LED que en realitat vull digital (parpellejant net):** el resultat parpelleja "esmorteït" en lloc de net, perquè PWM afegeix el seu propi parpelleig ràpid de fons. **Pista:** si el comportament és **dos estats clars** (sí/no, on/off), usa `write_digital`; si és un **valor intermedi**, usa `write_analog`.
- **El programa no arriba a la placa:** no s'ha arrossegat el `.hex` a la unitat `MICROBIT`, o s'ha desendollat mentre parpellejava el LED groc de gravació. Torna-ho a fer sense pressa (vegeu [`SA2_esquemes_connexions.md`](SA2_esquemes_connexions.md)).

---

## 📔 Diari de bord (entrada model, 1a persona)

> **Sessions 1-2:** He après la diferència entre sortida **digital** (`write_digital`, dos estats) i **PWM** (`write_analog`, valors 0-1023). He analitzat un carregador intel·ligent: el LED "carregant" parpelleja un nombre fix de vegades (`for`, digital) i el LED "acabat" es queda fix a mitja intensitat (PWM). Vaig **predir** que el `for i in range(5):` pararia exactament als 5 parpellejos, i es va complir. Al principi vaig provar `write_digital` per al mode "acabat" i només podia triar entre apagat i màxim: l'error va ser no adonar-me que necessitava un **valor intermedi**, que és exactament per a què serveix el PWM. **Evidència:** codi comentat + valors de `write_analog` provats amb el REPL.

**Per què és una bona entrada:** usa el **vocabulari clau** (digital, PWM, acumulador/bucle comptat, escala 0-1023), explica *el com* (per què cada sortida és digital o PWM), i és **honesta amb la dificultat** (triar digital vs PWM) i com es va resoldre.

---

*Exemple resolt de la SA2. Model de treball per a l'alumnat (alliberament gradual: es mostra després del primer intent). Es recolza en `codi/led_parpelleig` i `codi/pwm_led_rgb`. El repte «semàfor o llum d'ambient» real l'has de fer amb el **teu** disseny, no amb aquest. Llicència CC BY-SA 4.0.*
