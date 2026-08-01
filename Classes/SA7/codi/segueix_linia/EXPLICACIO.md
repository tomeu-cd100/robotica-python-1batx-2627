# El rover segueix una línia (Sessió 2)

**Quan es fa:** Sessió 2 · **Fitxer:** `segueix_linia.py` · **Maquinari:** [esquemes de connexions](../../SA7_esquemes_connexions.md) — seguidor de línia KS0050 (Kit 2) a **P0** (analògic, ADC vàlid); motoreductors del vehicle T2, **M1**=P13/P14, **M2**=P15/P16

## 🎯 Per què fem aquesta pràctica

El seguidor de línia és un altre **llaç tancat** (com la histèresi de la SA6): el rover **llegeix** el sensor, **decideix** si encara veu la línia i **actua** en conseqüència, a cada volta del bucle. No hi ha cap ordre externa: el rover decideix sol, en temps real, cap a on ha de corregir.

## 🔮 Abans d'executar: prediu

Si el rover avança i, en un moment donat, la lectura de `SEGUIDOR_LINIA.read_analog()` puja per sobre del llindar (la línia negra ja no hi és sota el sensor), cap a quin costat s'ha desviat el rover: dreta o esquerra?

## 🧠 El codi, per blocs

### Bloc 1 — Llegir el sensor amb `read_analog()`

```python
lectura = SEGUIDOR_LINIA.read_analog()
```

El KS0050 dona un valor **0-1023**, com qualsevol entrada analògica (SA3): un valor baix quan hi ha superfície fosca (línia negra) sota el sensor, i un valor alt quan hi ha fons clar. El valor exacte **depèn de la il·luminació real de l'aula**: cal calibrar `LLINDAR_LINIA` amb el REPL, provant el sensor sobre el circuit real.

### Bloc 2 — Decidir: seguir recte o corregir

```python
if lectura < LLINDAR_LINIA:
    avancar(VELOCITAT_AVANCAR)
else:
    girar('esquerra', VELOCITAT_GIR)
```

Mentre el sensor "veu" la línia (lectura per sota del llindar), el rover avança recte. Quan la perd (lectura per sobre), gira cap a un costat fix fins que la torni a trobar. Amb un **únic** sensor no es pot saber cap a quin costat s'ha desviat de veritat: per això es tria una estratègia de cerca fixa (aquí, sempre cap a l'esquerra).

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El rover no reacciona mai, sempre avança recte | `LLINDAR_LINIA` massa alt o massa baix per a la il·luminació real: calibra'l al REPL sobre el circuit |
| El rover gira sense parar, mai troba la línia | El sensor no està ben orientat cap a terra, o el circuit té massa poc contrast |
| Funciona bé en un circuit i malament en un altre | El llindar és específic de cada il·luminació: cal recalibrar-lo si canvia la llum de l'aula |

## 🔗 On ho aplicaràs

- **Ara mateix:** és un dels dos comportaments autònoms que pots triar a la Sessió 3 («tria un comportament autònom»).
- **Sessió 4 (producte):** [`rover_missions`](../rover_missions/EXPLICACIO.md) integra aquest mateix llindar a la missió «línia».
- **Simulador:** python.microbit.org **no** simula el seguidor de línia ni els motors: aquesta pràctica es fa **només** amb maquinari real, sobre un circuit de línia a terra.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA7](../../../../Reptes/Reptes_SA7.md)**.
