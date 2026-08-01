# Arquitectura de prioritats: comportaments amb estats (Sessió 1)

**Quan es fa:** Sessió 1 · **Fitxer:** `comportaments.py` · **Maquinari:** [esquemes de connexions](../../SA8_esquemes_connexions.md) — mateix cablatge de la SA7, sense pins nous: M1=P13/P14, M2=P15/P16, HC-SR04 trigger=P1/echo=P2, seguidor de línia=P0, polsador STOP=P12 (pull-up)

## 🎯 Per què fem aquesta pràctica

A la SA7 vas triar **un** comportament autònom (línia **o** obstacles) i, com a molt, els vas combinar dins d'una missió (`rover_missions.py`). Avui generalitzes la idea amb una **arquitectura de prioritats**: una única variable d'estat (`SEGUIR`, `ESQUIVAR`, `RECUPERAR`, exactament el mateix patró de FSM de `maquina_estats_semafor.py` i `vehicle_seguretat.py`, SA6) decideix **quin** comportament mana en cada instant, sense barrejar-los en un embolic de `if` encadenats. Aquesta mateixa FSM és la que `telemetria_radio.py` telemetiarà per ràdio a la Sessió 2-3: per això calia tenir-la clara abans d'afegir-hi ràdio i sensors nous.

## 🔮 Abans d'executar: prediu

Si el rover està a l'estat `SEGUIR` i, de sobte, l'HC-SR04 detecta un obstacle molt a prop MENTRE encara veu la línia, quin estat "guanya"? Per què?

## 🧠 El codi, per blocs

### Bloc 1 — Tres estats, una sola variable

```python
SEGUIR, ESQUIVAR, RECUPERAR = range(3)
estat = SEGUIR
```

En qualsevol instant, `estat` només pot valer **una** de les tres coses. És el mateix truc que la SA6: la variable d'estat és el que impedeix que el codi "faci dues coses alhora" de manera contradictòria.

### Bloc 2 — Les transicions, dins de cada branca

```python
if estat == SEGUIR:
    if distancia is not None and distancia < LLINDAR_OBSTACLE_CM:
        aturar()
        actualitza_estat(ESQUIVAR)
    elif lectura_linia < LLINDAR_LINIA:
        avancar(VELOCITAT_AVANCAR)
    else:
        girar('esquerra')
```

Fixa't en l'**ordre**: la comprovació de l'obstacle és la primera dins de `SEGUIR`, per davant de la lectura de la línia. És la mateixa idea de prioritat que ja vas veure a `missio_linia()` de `rover_missions.py` (SA7): l'obstacle **sempre** guanya al seguiment de línia.

### Bloc 3 — ESQUIVAR i RECUPERAR: sortides temporitzades i per sensor

```python
elif estat == ESQUIVAR:
    girar('dreta')
    sleep(400)
    aturar()
    actualitza_estat(RECUPERAR)
elif estat == RECUPERAR:
    if lectura_linia < LLINDAR_LINIA:
        actualitza_estat(SEGUIR)
    else:
        avancar(VELOCITAT_AVANCAR)
        sleep(150)
        aturar()
```

`ESQUIVAR` surt sempre cap a `RECUPERAR` després d'un temps fix (com un gir temporitzat de `rover_missions.py`); `RECUPERAR` surt cap a `SEGUIR` només quan el sensor de línia ho confirma. Dues maneres diferents de decidir quan canviar d'estat, cadascuna adequada al seu cas.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El rover no surt mai de `RECUPERAR` | El circuit no té prou contrast, o el gir d'`ESQUIVAR` l'ha allunyat massa de la línia |
| El rover "oscil·la" entre `SEGUIR` i `ESQUIVAR` sense parar | `LLINDAR_OBSTACLE_CM` massa alt per a l'espai real de proves |
| El polsador STOP no interromp `ESQUIVAR` a temps | Revisa que la comprovació de `polsador_premut()` sigui la **primera** de cada volta del bucle, abans de mirar `estat` |

## 🔗 On ho aplicaràs

- **Ara mateix:** és la base conceptual per dissenyar el format del missatge de telemetria (quin estat cal enviar).
- **Sessió 2-3 (producte):** [`telemetria_radio`](../telemetria_radio/EXPLICACIO.md) reutilitza **exactament** aquesta mateixa FSM, hi afegeix els sensors del Kit 3 i l'envia per ràdio.
- **Simulador:** python.microbit.org **no** simula cap component d'aquest programa: es prova **només** amb el rover real.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA8](../../../../Reptes/Reptes_SA8.md)**.
