# Xat per ràdio: enviar i rebre missatges (Sessió 1)

**Quan es fa:** Sessió 1 · **Fitxer:** `radio_missatges.py` · **Maquinari:** micro:bit V2 (ràdio interna, sense cablatge) · **Grup:** el que t'assigni el docent per aparellar-te puntualment amb un company (banc de proves)

> ✋ Aquesta pàgina explica el codi **model**. El teu codi és **teu**: l'aparellament amb un company és només per comprovar que envia/rep correctament.

## 🎯 Per què fem aquesta pràctica

Fins ara la micro:bit només reaccionava al que passava a la seva pròpia placa (botons, sensors). Avui la fas **parlar amb una altra placa** per ràdio: `radio.on()` l'activa, `radio.config(group=...)` tria amb qui es comunica (només plaques amb el mateix grup es "senten"), i `radio.send()`/`radio.receive()` envien i reben text pla. Introduïm també una **llista** (`historic`) per guardar els últims missatges rebuts.

## 🔮 Abans d'executar: prediu

Si dues plaques tenen **grups diferents** (`GRUP = 1` i `GRUP = 2`), què creus que passarà quan una enviï un missatge? L'altra el rebrà, el rebrà amb retard, o no el rebrà mai?

## 🧠 El codi, per blocs

### Bloc 1 — Activar la ràdio i triar grup

```python
radio.on()
radio.config(group=GRUP, power=6)
```

`radio.on()` engega el mòdul; `group` fa que només les plaques amb el **mateix número** es puguin sentir entre elles (evita interferències amb la resta de la classe). `power` regula l'abast (6 és un valor moderat, prou per treballar dins de l'aula).

### Bloc 2 — Enviar amb remitent: `envia(text)`

```python
def envia(text):
    radio.send(MEU_NOM + ":" + text)
```

El missatge porta el **remitent al davant** (`"A1:Hola"`): és la primera idea de **protocol**, que la Sessió 2 formalitzarà amb un prefix de comandes.

### Bloc 3 — Guardar en una llista: `desa_al_historic(missatge)`

```python
def desa_al_historic(missatge):
    historic.append(missatge)
    if len(historic) > MAX_HISTORIC:
        historic.pop(0)
```

Una **llista** creix amb `append()`; aquí es limita a `MAX_HISTORIC` elements (xat "5×5") descartant sempre el més antic amb `pop(0)`.

### Bloc 4 — Rebre dins del bucle principal

```python
missatge_rebut = radio.receive()
if missatge_rebut is not None:
    desa_al_historic(missatge_rebut)
```

`radio.receive()` **no espera**: torna `None` si no ha arribat res des de l'última volta del bucle. Per això cal cridar-lo dins de `while True:`, no un sol cop.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| No rep mai res | Grups diferents a les dues plaques, o alguna de les dues no ha cridat `radio.on()` |
| Rep missatges d'algú altre de la classe | Coincidència de `group` amb una altra parella; canvia'l per un número que no es repeteixi a prop |
| El text es talla o es veu incomplet | El display només mostra uns quants caràcters de cop; `display.scroll()` el desplaça sencer |

## 🔗 On ho aplicaràs

- **Sessió 2:** [`comandament.py`](../comandament/EXPLICACIO.md) reutilitza `radio.on()`/`radio.config()`/`radio.send()`, ara amb un **protocol** de comandes en lloc d'un xat lliure.
- **Sessió 3:** [`receptor_vehicle.py`](../receptor_vehicle/EXPLICACIO.md) és el **producte**: rep ordres per ràdio i mou el vehicle.
- **Simulador:** python.microbit.org **sí** simula la ràdio, però només entre instàncies obertes del simulador (no amb una placa física real): és una via de pràctica individual a casa.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA5](../../../../Reptes/Reptes_SA5.md)**.
