# El rover evita obstacles (Sessió 3)

**Quan es fa:** Sessió 3 · **Fitxer:** `evita_obstacles.py` · **Maquinari:** [esquemes de connexions](../../SA7_esquemes_connexions.md) — HC-SR04 (Kit 2) a 5 V, trigger **P1**, echo **P2**; motoreductors del vehicle T2, **M1**=P13/P14, **M2**=P15/P16

## 🎯 Per què fem aquesta pràctica

Aquest programa reutilitza **exactament** el mètode de `alarma_ultrasons.py` (SA3): el sensor no llegeix una distància directament, envia un **pols de so** i mesura **quant triga a tornar l'eco** (*time-of-flight*) amb `machine.time_pulse_us`. L'únic que canvia respecte a la SA3 són els **pins**: al rover, l'HC-SR04 va a trigger **P1** / echo **P2** (a la SA3 es practicava a P14/P15, un banc de proves de la mascota; al rover, P14/P15 són ara dels motoreductors, fixats des de la SA4).

## 🔮 Abans d'executar: prediu

Si el rover avança cap a una paret i la distància mesurada baixa de 15 cm, quines DUES coses fa el codi, en quin ordre: aturar-se abans de girar, o girar sense aturar-se abans?

## 🧠 El codi, per blocs

### Bloc 1 — El trigger i l'echo: mateix patró que la SA3

```python
TRIGGER.write_digital(0)
utime.sleep_us(2)
TRIGGER.write_digital(1)
utime.sleep_us(10)
TRIGGER.write_digital(0)
durada_us = machine.time_pulse_us(ECHO, 1, 30000)
```

Exactament el mateix codi que `distancia_cm()` de `alarma_ultrasons.py` (SA3), amb `TRIGGER = pin1` i `ECHO = pin2` en lloc de `pin14`/`pin15`. El pols de 10 µs al trigger i el `timeout` de 30000 µs a l'echo no canvien: és el mateix sensor, només canvia on està connectat.

### Bloc 1b — ACTIVITAT NUCLI: lectura robusta amb `try`/`except`

```python
try:
    durada_us = machine.time_pulse_us(ECHO, 1, 30000)
except OSError:
    return None
```

> 🔑 **Què fa `try`/`except`:** el codi dins de `try:` s'executa normalment; si en algun punt **peta** amb un error del tipus indicat a `except` (aquí, `OSError`), Python **no atura tot el programa**: salta directament al cos de l'`except` i continua des d'allà. `try` diu "intenta fer això"; `except OSError:` diu "si peta amb aquest tipus d'error concret, fes això altre en lloc de petar".

Un sensor d'ultrasons real **no sempre** troba l'eco que espera (obstacle massa lluny, absorbent, o fora de l'abast dels 30 ms de marge): segons la placa i la versió de MicroPython, `machine.time_pulse_us` pot avisar-ho de dues maneres diferents — retornant un número negatiu (ja el comprovàvem amb `if durada_us < 0:`) o **llançant una excepció** `OSError`. Sense el `try`/`except`, aquesta segona possibilitat aturaria tot el programa del rover (`while True:` inclòs) per una única lectura dolenta. Amb el `try`/`except`, `mesura_distancia()` simplement retorna `None` aquell cop, exactament com fa amb el cas del valor negatiu, i el rover ho tracta igual que ja feia: `if distancia is not None and distancia < LLINDAR_OBSTACLE_CM:`.

### Bloc 2 — Decidir i actuar: aturar, girar, seguir

```python
if distancia is not None and distancia < LLINDAR_OBSTACLE_CM:
    aturar()
    girar('esquerra', VELOCITAT_GIR)
    sleep(400)
else:
    avancar(VELOCITAT_AVANCAR)
```

Primer **s'atura** (mai gira directament sense aturar-se abans: evitaria un cop massa brusc), després **gira** un temps fix cap a un costat, i a la volta següent del bucle torna a mesurar per decidir si ja pot avançar de nou.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| `mesura_distancia()` retorna sempre `None` | Cap eco dins del `timeout`: comprova el cablatge trigger(P1)/echo(P2) |
| El rover xoca abans d'aturar-se | `LLINDAR_OBSTACLE_CM` massa baix per a la velocitat d'avanç: puja'l una mica |
| El rover gira i torna a topar amb el mateix obstacle | El temps de gir (`sleep(400)`) és massa curt per a l'amplada de l'obstacle |

## 🔗 On ho aplicaràs

- **Ara mateix:** és un dels dos comportaments autònoms que pots triar a aquesta mateixa Sessió 3 («tria un comportament autònom»); pot fer de producte de la SA si el calendari ho requereix.
- **Sessió 4 (producte):** [`rover_missions`](../rover_missions/EXPLICACIO.md) integra aquesta mateixa funció `mesura_distancia()` a les missions «paret» i «línia».
- **Simulador:** python.microbit.org **no** simula cap sensor extern, i molt menys el temps de vol de l'HC-SR04: aquesta pràctica es fa **només** amb maquinari real.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA7](../../../../Reptes/Reptes_SA7.md)**.
