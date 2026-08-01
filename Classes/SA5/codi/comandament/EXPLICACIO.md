# Un protocol propi de comandes (Sessió 2)

**Quan es fa:** Sessió 2 · **Fitxer:** `comandament.py` · **Maquinari:** micro:bit V2 (ràdio interna); es prova aparellat puntualment amb la placa d'un company que porti [`receptor_vehicle.py`](../receptor_vehicle/EXPLICACIO.md)

> ✋ Aquesta placa és el **comandament** (emissor); l'altra és el **receptor**. Cadascú programa i és avaluat pel seu propi codi.

## 🎯 Per què fem aquesta pràctica

A la Sessió 1 vas enviar text lliure. Avui dissenyes un **protocol**: un conjunt tancat d'ordres curtes (`F`, `B`, `L`, `R`, `S`) amb un **prefix** (`"CMD:"`) que les distingeix de qualsevol altre missatge de ràdio que pugui circular per l'aula. Aquesta placa envia les ordres amb botons **i** amb gestos de l'acceleròmetre.

## 🔮 Abans d'executar: prediu

Si prems els botons **A i B alhora**, quina ordre creus que s'enviarà: `F`, `B` o `S`? Per què creus que té sentit que aquesta combinació tingui **prioritat màxima**?

## 🧠 El codi, per blocs

### Bloc 1 — El prefix del protocol

```python
PREFIX = "CMD:"

def envia_ordre(ordre):
    radio.send(PREFIX + ordre)
```

Totes les ordres comencen igual (`"CMD:F"`, `"CMD:S"`...): la placa receptora només actuarà sobre missatges que comencin **exactament** per aquest prefix, ignorant qualsevol altre trànsit de ràdio (per exemple, el xat de `radio_missatges.py` d'una altra parella).

### Bloc 2 — Botons: avant, enrere i stop prioritari

```python
if button_a.is_pressed() and button_b.is_pressed():
    envia_ordre("S")
elif button_a.was_pressed():
    envia_ordre("F")
elif button_b.was_pressed():
    envia_ordre("B")
```

Es comprova **primer** la combinació A+B (stop), i només si no s'ha premut es miren els botons per separat: el mateix principi que el botó B "sempre atura" a `control_per_botons.py` (SA4).

### Bloc 3 — Gestos: girs i sacsejada d'emergència

```python
if accelerometer.was_gesture("shake"):
    envia_ordre("S")
```

Els gestos (`"left"`, `"right"`, `"shake"`) són una **segona via d'entrada**, independent dels botons, amb el mateix protocol de sortida: el receptor no distingeix si l'ordre `"S"` ha vingut d'un botó o d'una sacsejada.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El receptor no fa res mai | `GRUP` diferent entre comandament i receptor, o el receptor no comprova el `PREFIX` |
| El vehicle no s'atura mai amb prioritat | Es comprova A/B abans que A+B: cal l'ordre invers (mira primer la combinació) |
| Els gestos s'envien diverses vegades seguides | `was_gesture()` pot repetir-se si el moviment és llarg; ajusta el temps de `sleep()` del bucle si molesta |

## 🔗 On ho aplicaràs

- **Ara mateix:** proves puntuals aparellat amb un company que porti `receptor_vehicle.py` (banc de proves, no producte compartit).
- **Sessió 3:** el mateix protocol (`"CMD:" + ordre`) és el que interpreta [`receptor_vehicle.py`](../receptor_vehicle/EXPLICACIO.md), el **producte** de la SA5.
- **SA6:** aquest mateix comandament es reutilitzarà com a base del control remot complet del vehicle.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA5](../../../../Reptes/Reptes_SA5.md)**.
