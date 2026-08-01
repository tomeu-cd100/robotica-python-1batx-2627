# Un semàfor com a màquina d'estats (Sessió 1)

**Quan es fa:** Sessió 1 · **Fitxer:** `maquina_estats_semafor.py` · **Maquinari:** cap de nou, només el display 5×5 de la micro:bit

## 🎯 Per què fem aquesta pràctica

Abans d'aplicar una **màquina d'estats finits (FSM)** al vehicle (amb motors i ràdio de per mig), la practiquem sobre un problema petit i conegut: un **semàfor**. Una FSM té dues peces: una **variable d'estat** (que només pot valer una cosa alhora: VERD, GROC o VERMELL, mai dues a la vegada) i unes **transicions** que diuen, per a cada estat, quin és el següent i quan hi passa.

## 🔮 Abans d'executar: prediu

Mirant només el diccionari `TRANSICIONS`, sense executar el programa: si el semàfor comença en VERMELL, quina seqüència d'estats i de temps (en segons) tindrà durant els primers 10 segons?

## 🧠 El codi, per blocs

### Bloc 1 — La variable d'estat

```python
VERD, GROC, VERMELL = range(3)
estat = VERMELL
```

`estat` és una **variable d'estat**: en cada instant només pot valer una d'aquestes tres coses. No hi ha cap combinació "una mica verd i una mica groc": això és precisament el que fa que una FSM sigui fàcil de raonar.

### Bloc 2 — Les transicions com a dades

```python
TRANSICIONS = {
    VERD: (GROC, 3000),
    GROC: (VERMELL, 1000),
    VERMELL: (VERD, 3000),
}
```

En lloc d'un `if estat == VERD: ... elif estat == GROC: ...` encadenat, aquí les transicions es guarden en un **diccionari**: la clau és l'estat actual, el valor és una tupla `(següent estat, durada)`. És la mateixa idea que un `if`/`elif`, escrita com a dades en lloc de com a codi; totes dues formes són vàlides per a una FSM senzilla.

### Bloc 3 — Un únic lloc que canvia l'estat

```python
def actualitza_estat(nou):
    global estat
    estat = nou
    display.show(IMATGES[estat])
    print("Semafor ->", NOMS[estat])
```

Igual que farà `actualitza_estat()` al vehicle (Sessió 2-3), tot el que ha de passar quan canvia l'estat (mostrar-lo, registrar-lo) viu en **un sol lloc**: així no hi ha risc que una part del programa "oblidi" actualitzar el display en canviar d'estat. Per què cal `global estat`: mateix motiu que `global PAS` a `control_per_botons.py` (SA4) — la funció **reassigna** una variable definida fora seu.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El semàfor es queda enganxat en un estat | Falta l'entrada al diccionari `TRANSICIONS` per a aquell estat |
| El display no canvia mai | S'ha oblidat de cridar `actualitza_estat()` en lloc de canviar `estat` directament |
| L'ordre dels colors és estrany | Revisa la taula `TRANSICIONS`: cada clau ha d'apuntar al **següent** estat correcte |

## 🧗 Si t'encalles: la mateixa FSM amb `if`/`elif`

Si el diccionari `TRANSICIONS` se't fa costa amunt, comença amb la versió **equivalent** escrita amb `if`/`elif` encadenats — mateixa lògica, sense diccionari:

```python
def transicio(estat_actual):
    # Retorna (proxim_estat, durada_ms) amb if/elif, sense diccionari.
    if estat_actual == VERD:
        return GROC, 3000
    elif estat_actual == GROC:
        return VERMELL, 1000
    else:  # VERMELL
        return VERD, 3000


while True:
    proxim, durada = transicio(estat)
    sleep(durada)
    actualitza_estat(proxim)
```

Un cop et surti bé, torna a la versió amb `TRANSICIONS` (bloc 2): fa exactament el mateix, però és més curta d'ampliar si el semàfor guanyés un quart estat.

## 🔗 On ho aplicaràs

- **Sessió 2:** el vehicle tindrà la seva pròpia FSM (RUN/STOP/ALERTA), amb la mateixa idea de «un únic lloc que canvia l'estat» però amb l'STOP com a transició **prioritària**.
- **Sessió 3:** `vehicle_seguretat.py` reutilitza exactament aquest patró a `actualitza_estat()`.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA6](../../../../Reptes/Reptes_SA6.md)**.
