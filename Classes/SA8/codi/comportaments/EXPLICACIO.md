# Arquitectura de prioritats: comportaments amb estats (Sessió 1)

**Quan es fa:** Sessió 1 · **Fitxer:** `comportaments.py` · **Maquinari:** [esquemes de connexions](../../SA8_esquemes_connexions.md) — mateix cablatge de la SA7, sense pins nous: M1=P13/P14, M2=P15/P16, HC-SR04 trigger=P1/echo=P2, seguidor de línia=P0, polsador STOP=P12 (pull-up)

## 🎯 Per què fem aquesta pràctica

A la SA7 vas triar **un** comportament autònom (línia **o** obstacles) i, com a molt, els vas combinar dins d'una missió (`rover_missions.py`). Avui generalitzes la idea amb una **arquitectura de prioritats**: una única variable d'estat (`SEGUIR`, `ESQUIVAR`, `RECUPERAR`, exactament el mateix patró de FSM de `maquina_estats_semafor.py` i `vehicle_seguretat.py`, SA6) decideix **quin** comportament mana en cada instant, sense barrejar-los en un embolic de `if` encadenats. Aquest programa **estructura explícitament** el codi en tres funcions —`percep()`, `decideix()`, `actua()`— que és exactament l'esquema que farà servir la plantilla del repte final (`plantilla_projecte.py`, SA9): avui el veus funcionar sobre un problema ja conegut, abans d'haver-lo d'escriure des de zero. Aquesta mateixa FSM és la que `telemetria_radio.py` telemetiarà per ràdio a la Sessió 2-3: per això calia tenir-la clara abans d'afegir-hi ràdio i sensors nous.

## 🔮 Abans d'executar: prediu

Si el rover està a l'estat `SEGUIR` i, de sobte, l'HC-SR04 detecta un obstacle molt a prop MENTRE encara veu la línia, quin estat "guanya"? Per què?

## 🧠 El codi, per blocs

### Bloc 1 — Tres estats, una sola variable

```python
SEGUIR, ESQUIVAR, RECUPERAR = range(3)
estat = SEGUIR
```

En qualsevol instant, `estat` només pot valer **una** de les tres coses. És el mateix truc que la SA6: la variable d'estat és el que impedeix que el codi "faci dues coses alhora" de manera contradictòria.

### Bloc 2 — `percep()`: NOMÉS llegeix sensors

```python
def percep():
    return {
        "distancia": mesura_distancia(),
        "linia": SEGUIDOR_LINIA.read_analog(),
    }
```

`percep()` no decideix res ni mou cap motor: la seva única feina és llegir els sensors i tornar-ne els valors (aquí, com un diccionari). Cada volta del bucle en fa una crida, abans de tota la resta.

### Bloc 3 — `decideix()`: NOMÉS canvia d'estat

```python
def decideix(dades):
    global estat
    if estat == SEGUIR:
        if dades["distancia"] is not None and dades["distancia"] < LLINDAR_OBSTACLE_CM:
            actualitza_estat(ESQUIVAR)
    elif estat == RECUPERAR:
        if dades["linia"] < LLINDAR_LINIA:
            actualitza_estat(SEGUIR)
```

Fixa't en l'**ordre** de la comprovació a `SEGUIR`: l'obstacle és **prioritari** sobre la línia, la mateixa idea que ja vas veure a `missio_linia()` de `rover_missions.py` (SA7). `decideix()` **mai** mou motors: només decideix, a partir de les dades de `percep()`, si toca canviar d'estat per a la propera volta. La transició `ESQUIVAR → RECUPERAR` NO hi és: és **garantida** (sempre passa igual, no depèn de cap sensor) i forma part de completar la maniobra, per això viu dins `actua()`.

### Bloc 4 — `actua()`: executa el moviment segons l'estat

```python
def actua(dades, estat_abans):
    if estat_abans == SEGUIR:
        ...
    elif estat_abans == ESQUIVAR:
        girar('dreta')
        sleep(400)
        aturar()
        actualitza_estat(RECUPERAR)
    elif estat_abans == RECUPERAR:
        if dades["linia"] >= LLINDAR_LINIA:
            avancar(VELOCITAT_AVANCAR)
            sleep(150)
            aturar()
```

`actua()` rep `estat_abans` (l'estat en què érem **abans** de cridar `decideix()`) perquè el moviment d'aquesta volta ha de correspondre a la situació que hem **percebut**, no a l'estat que acabem de decidir per a la propera volta. `ESQUIVAR` fa un gir de temps fix i, en acabar-lo, ell mateix completa la transició cap a `RECUPERAR` (per això aquí sí que hi ha un `actualitza_estat()`: no és una decisió condicionada per cap sensor, és el pas final de la maniobra).

### Bloc 5 — El bucle principal: percep → decideix → actua

```python
dades = percep()
estat_abans = estat
decideix(dades)
actua(dades, estat_abans)
```

Tres passos, en aquest ordre, a cada volta: primer **percep** (què hi ha), després **decideix** (quin estat toca a partir d'ara), i finalment **actua** (què fa el rover ara mateix). El polsador STOP es comprova **abans** de tot això, com sempre des de la SA6.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El rover no surt mai de `RECUPERAR` | El circuit no té prou contrast, o el gir d'`ESQUIVAR` l'ha allunyat massa de la línia |
| El rover "oscil·la" entre `SEGUIR` i `ESQUIVAR` sense parar | `LLINDAR_OBSTACLE_CM` massa alt per a l'espai real de proves |
| El polsador STOP no interromp `ESQUIVAR` a temps | Revisa que la comprovació de `polsador_premut()` sigui la **primera** de cada volta del bucle, abans de mirar `estat` |
| `actua()` fa el moviment "d'un pas enrere" | S'ha fet servir `estat` (el ja actualitzat) en lloc de `estat_abans` a `actua()` |

## 🔗 On ho aplicaràs

- **Ara mateix:** és la base conceptual per dissenyar el format del missatge de telemetria (quin estat cal enviar).
- **Sessió 2-3 (producte):** [`telemetria_radio`](../telemetria_radio/EXPLICACIO.md) reutilitza **exactament** aquesta mateixa FSM, hi afegeix els sensors del Kit 3 i l'envia per ràdio.
- **SA9:** `plantilla_projecte.py` fa servir aquesta mateixa arquitectura `percep()`/`decideix()`/`actua()` per al teu repte final; avui n'has vist un exemple complet i funcional.
- **Simulador:** python.microbit.org **no** simula cap component d'aquest programa: es prova **només** amb el rover real.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA8](../../../../Reptes/Reptes_SA8.md)**.
