# Missions del rover (Sessió 4 — producte)

**Quan es fa:** Sessió 4 · **Fitxer:** `rover_missions.py` · **Maquinari:** rover complet (M1=P13/P14, M2=P15/P16, HC-SR04 trigger=P1/echo=P2, seguidor de línia=P0, polsador STOP=P12) — [esquemes de connexions](../../SA7_esquemes_connexions.md)

> 🎯 **Producte de la SA7.** Aquest programa és el que **integra** el comportament autònom triat a la Sessió 3, amb el rover complet sobre una pista de proves: s'avalua amb **R1**, **R3** (criteri "Autonomia/control") i **R4**.

## 🎯 Per què fem aquesta pràctica

Fins ara cada comportament (calibratge, seguidor de línia, evita-obstacles) s'ha provat **per separat**. Aquí es combinen en **missions** seleccionables amb els botons A/B, sobre una pista real, i s'hi afegeix un **polsador STOP** (P12) amb el mateix patró prioritari de `vehicle_seguretat.py` (SA6): es comprova **sempre primer**, a cada volta del bucle, abans de qualsevol altra cosa.

## 🔮 Abans d'executar: prediu

Si el rover està executant la missió «paret» i, a mig camí, es prem el polsador STOP, què esperes que passi: el rover acaba la missió i llavors s'atura, o s'atura **immediatament**, encara que la missió no hagi arribat a la paret?

## 🧠 El codi, per blocs

### Bloc 1 — Seleccionar i engegar una missió amb els botons

```python
if button_a.was_pressed() and not en_marxa:
    missio_actual = (missio_actual + 1) % 3
    ...
if button_b.was_pressed() and not en_marxa:
    en_marxa = True
    MISSIONS[missio_actual]()
```

El botó A **canvia** la missió mostrada al display (només si el rover no és en marxa); el botó B la **comença**. `MISSIONS` és un diccionari que fa correspondre cada constant de missió amb la seva funció, la mateixa idea que `TRANSICIONS` a `maquina_estats_semafor.py` (SA6): la lògica es representa com a dades.

### Bloc 2 — El polsador STOP, sempre el primer `if`

```python
if polsador_premut():
    aturar()
    en_marxa = False
```

Exactament el mateix criteri que `vehicle_seguretat.py`: si el polsador es comprovés després, o només "de tant en tant", hi hauria una finestra de temps en què el rover seguiria movent-se amb el botó ja premut. Dins de cada missió (`missio_quadrat`, `missio_paret`, `missio_linia`) també es comprova `polsador_premut()` a cada iteració del seu propi bucle intern, pel mateix motiu.

### Bloc 3 — Una missió que combina els dos sensors nous

```python
def missio_linia():
    while not polsador_premut():
        d = mesura_distancia()
        if d is not None and d < LLINDAR_OBSTACLE_CM:
            aturar()
            break
        lectura = SEGUIDOR_LINIA.read_analog()
        ...
```

`missio_linia()` és la integració real d'aquesta SA: el rover segueix la línia (com `segueix_linia.py`) fins que l'HC-SR04 detecta un obstacle al davant (com `evita_obstacles.py`), moment en què s'atura. És l'exemple de com dos comportaments programats per separat es combinen sense reescriure'ls des de zero.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El polsador STOP no atura el rover a l'instant | Alguna missió no comprova `polsador_premut()` dins del seu propi bucle intern, només al bucle principal |
| El botó A canvia de missió mentre el rover és en marxa | Falta la comprovació `not en_marxa` abans de canviar `missio_actual` |
| La missió «quadrat» no fa un quadrat real | El temps de gir (`sleep(430)`) no està calibrat per al teu rover: ajusta'l fins que el gir sigui proper a 90 graus |

## 🔗 On ho aplicaràs

- **Ara mateix:** és el **producte** de la SA7: comportament autònom del rover, funcional i documentat.
- **SA8:** hi afegiràs telemetria per ràdio sobre aquest mateix rover, sense tocar les funcions de moviment ni de sensors.
- **Simulador:** python.microbit.org **no** simula motors, HC-SR04 ni seguidor de línia: aquest programa es prova **només** amb el rover real sobre la pista.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA7](../../../../Reptes/Reptes_SA7.md)**.
