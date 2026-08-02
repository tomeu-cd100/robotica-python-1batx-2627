# El vehicle respon a la ràdio: repte «control remot bàsic» (Sessió 3 — producte)

**Quan es fa:** Sessió 3 · **Fitxer:** `receptor_vehicle.py` · **Maquinari:** vehicle T2 muntat a la SA4 (motoreductors **M1**=P13/P14, **M2**=P15/P16, [esquemes](../../SA5_esquemes_connexions.md)); es prova aparellat puntualment amb la placa d'un company que porti [`comandament.py`](../comandament/EXPLICACIO.md)

> ✋ **Aquesta pàgina mostra la SOLUCIÓ del producte «control remot bàsic».** Intenta escriure el receptor pel teu compte a l'Activitat 3 de la [fitxa](../../SA5_fitxa_alumnat.md) abans de mirar-la sencera: el patró (rebre → comprovar el prefix → actuar) ja el coneixes de `comandament.py` i de la SA3.

> 🎯 **Producte de la SA5.** Aquest programa és el que s'avalua amb **R1** (codi) i **R4** (documentació): és la **teva** implementació del receptor, encara que la proves amb l'emissor d'un company.

## 🎯 Per què fem aquesta pràctica

Aquest programa **no introdueix cap funció de moviment nova**: reutilitza exactament `avancar()`, `retrocedir()`, `girar()` i `aturar()` de la SA4 ([`velocitat_pwm.py`](../../../SA4/codi/velocitat_pwm/EXPLICACIO.md)). L'única cosa nova és **l'entrada**: en lloc dels botons A/B (`control_per_botons.py`), l'esdeveniment que decideix quin moviment fer és un **missatge de ràdio**. És el mateix esquema «esdeveniment → acció» de tot el curs, amb una entrada diferent.

## 🔮 Abans d'executar: prediu

Si el `PREFIX` no coincidís exactament entre `comandament.py` i `receptor_vehicle.py` (per exemple, `"CMD:"` en un i `"cmd:"` en l'altre), què passaria? El vehicle es mouria igualment, es mouria malament, o no es mouria mai?

## 🧠 El codi, per blocs

### Bloc 1 — Separar el missatge del protocol

```python
if missatge is not None and missatge.startswith(PREFIX):
    ordre = missatge[len(PREFIX):]
```

Primer es comprova que el missatge **existeixi** (`radio.receive()` pot tornar `None`) i que **comenci pel prefix** esperat; només llavors es treu la part útil (l'ordre) amb un tall de text.

### Bloc 2 — Esdeveniment → acció: `actua(ordre)`

```python
def actua(ordre):
    if ordre == "F":
        avancar(VELOCITAT)
    elif ordre == "S":
        aturar()
    ...
```

Cada ordre rebuda es tradueix en la crida a una funció de moviment **ja feta i ja provada** a la SA4: no cal tornar a escriure com es mouen els motors, només **relacionar** l'ordre amb la funció correcta.

### Bloc 3 — Ampliació: historial amb tuples

```python
historic_comandes.append((ordre, running_time()))
```

Cada entrada de l'historial és una **tupla** `(ordre, instant)`: una parella de valors que, a diferència d'una llista, no es pot modificar un cop creada. És la primera introducció a les tuples del curs; la SA6 hi aprofundirà.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El vehicle no respon a cap ordre | `GRUP` diferent del comandament, o el vehicle no rep alimentació externa (piles) |
| El vehicle respon tard o "es perd" alguna ordre | Normal en ràdio: no totes les trameses arriben (sense confirmació); per això `S` s'envia també amb A+B i amb sacsejada, per poder-lo repetir |
| El vehicle es mou sol sense cap comandament proper | Un altre grup de la classe fa servir el mateix número de `GRUP`; canvia'l |

## 🔗 On ho aplicaràs

- **Ara mateix:** repte «control remot bàsic», producte de la SA5, avaluat amb **R1**/**R4**.
- **SA6:** el vehicle passarà d'obeir ordres puntuals a un **llaç de control** (esdeveniments encadenats, histèresi), reutilitzant aquest mateix esquema de recepció.
- **Simulador:** la lògica del protocol (separar prefix i ordre) es pot revisar al simulador de python.microbit.org, però el moviment real dels motors necessita el vehicle muntat.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA5](../../../../Reptes/Reptes_SA5.md)**.
