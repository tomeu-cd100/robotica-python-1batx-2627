# El termòstat que no fa "clic-clic": histèresi (Sessió 1)

**Quan es fa:** Sessió 1 · **Fitxer:** `termostat_histeresi.py` · **Maquinari:** sensor de temperatura **intern** de la micro:bit (`temperature()`) + relé (Kit 3) al **pin2** (substitut segur: LED al **pin1** si no tens relé a mà)

## 🎯 Per què fem aquesta pràctica

Un termòstat **tot/res** amb un **únic llindar** (per exemple, `if temp < 25: engega()`) sembla correcte, però a la pràctica **falla**: una lectura real balla uns dècims amunt i avall del llindar contínuament, i el relé fa **clic-clic sense parar** al voltant d'aquest valor (es desgasta en poc temps i pot fer malbé l'actuador). La solució és la **histèresi**: dos llindars en lloc d'un, de manera que l'estat només canvia quan la temperatura els **travessa de veritat**, no quan hi ronda a prop.

## 🔮 Abans d'executar: prediu

Si `LLINDAR_BAIX = 24` i `LLINDAR_ALT = 26`, i la temperatura puja lentament de 20 a 30 graus i després torna a baixar, **quantes vegades** canvia d'estat el relé? Dibuixa la línia de temperatura i marca-hi els punts de canvi abans de mirar el codi.

## 🧠 El codi, per blocs

### Bloc 1 — Dos llindars, no un

```python
LLINDAR_BAIX = 24
LLINDAR_ALT = 26
```

Un termòstat **sense** histèresi tindria un sol llindar (per exemple `25`). Amb histèresi, hi ha una **franja morta** entre els dos llindars (aquí, de 24 a 26) on l'estat **no canvia mai**, per molt que la lectura hi entri i en surti repetidament.

### Bloc 2 — La variable d'estat, no només la lectura

```python
if not actiu and temp < LLINDAR_BAIX:
    actiu = True
elif actiu and temp > LLINDAR_ALT:
    actiu = False
```

La decisió **no** mira només `temp`: mira `temp` **i** l'estat actual (`actiu`). És la diferència clau amb un `if` senzill: aquí es pregunta "estava apagat i ha baixat prou?" o "estava engegat i ha pujat prou?", mai només "quina temperatura fa ara?".

### Bloc 3 — L'actuador reflecteix l'estat, no la lectura

```python
RELE.write_digital(1 if actiu else 0)
```

El relé es commuta a partir de la **variable d'estat** (`actiu`), que només canvia a les dues condicions de dalt. Si es commutés directament amb `temp < 25` a cada volta, tornaríem a tenir el problema del "clic-clic".

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El relé "clica" molt sovint al voltant d'un valor | Un sol llindar, o els dos llindars massa junts (poca franja morta) |
| El relé no canvia mai d'estat | Els llindars estan envoltant una temperatura que mai s'assoleix a l'aula (calibra amb el REPL) |
| Al simulador no es mou res de "real" | El simulador **SIMULA** `temperature()`, però **NO** el relé/actuador extern: només es pot provar la lògica (quan hauria d'activar-se), no l'efecte físic |

## 🔗 On ho aplicaràs

- **Ara mateix:** primer contacte amb un **llaç de control tancat** amb realimentació (la lectura del sensor decideix l'actuador).
- **Sessió 3:** el mateix principi de "no canviar d'estat sense una condició clara" és el que fa que l'**STOP prioritari** del vehicle funcioni sense ambigüitat.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA6](../../../../Reptes/Reptes_SA6.md)**.
