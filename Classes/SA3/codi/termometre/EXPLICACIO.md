# Termòmetre: intern vs extern

**Quan es fa:** Sessió 2 (modelatge) · **Fitxer:** `termometre.py` · **Maquinari:** [esquemes de connexions](../../SA3_esquemes_connexions.md) — sensor de temperatura bàsic del Kit 1 al pin **P1** (ADC vàlid); sensor de temperatura **intern** de la micro:bit (cap cablatge)

> ⚠️ **Per què P1 i no P10?** P3, P4 i P10 també tenen ADC, però comparteixen circuit amb el display: `read_analog()` hi falla (`ValueError: Pin in display mode`) mentre el display estigui actiu, com passa aquí. P0/P1/P2 són ADC lliures de display.

## 🎯 Per què fem aquesta pràctica

La micro:bit ja porta un sensor de temperatura intern: `temperature()` (sense pin, sense cablatge) retorna directament graus Celsius. El sensor bàsic del Kit 1, en canvi, és un component analògic normal: cal llegir-lo amb `read_analog()` (0-1023) i **convertir** la lectura a graus amb la funció `mapa()` (la mateixa idea que a `nivell_llum.py`). Interpretem el resultat amb `if/elif/else`.

## 🔮 Abans d'executar: prediu

Si t'escalfes el sensor extern amb els dits, què esperes que passi amb la cara del display? I si el sensor intern nota que la mà de qui sosté la placa l'escalfa (és molt a prop del processador)? Comprova-ho a l'Activitat 2 de la [fitxa](../../SA3_fitxa_alumnat.md).

## 🧠 El codi, per blocs

### Bloc 1 — Sensor intern: directe en graus

```python
temp_interna = temperature()   # graus C, cap conversio
```

`temperature()` no necessita `read_analog()` ni cap `mapa()`: la micro:bit ja fa la conversió per tu i et dona directament un enter en graus Celsius.

### Bloc 2 — Sensor extern: cal convertir la lectura

```python
def graus_del_sensor_extern(lectura_analogica):
    return mapa(lectura_analogica, 0, 1023, 0, 50)
```

El sensor bàsic del Kit 1 no dona graus directament: dona una lectura 0-1023 que cal **mapar** a un rang de graus versemblant (aquí, 0-50 °C, orientatiu). Un sensor real es calibra comparant la seva lectura amb un termòmetre de referència al REPL, no s'inventa el rang.

### Bloc 3 — Interpretar amb condicionals

```python
if temp_interna < FRED:
    display.show(Image.SAD)
elif temp_interna > CALOR:
    display.show(Image.ANGRY)
else:
    display.show(Image.HAPPY)
```

El mateix patró de `nivell_llum` (llegir → comparar amb un llindar → decidir) aplicat a la temperatura: no n'hi ha prou amb "llegir un número", cal **interpretar-lo** amb condicionals per convertir-lo en una decisió (quina cara mostrar).

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El sensor extern sempre dona la mateixa temperatura | Cablatge incorrecte o pin sense ADC (recorda: només P0, P1, P2, P3, P4, P10) |
| `ValueError: Pin in display mode` | El sensor analògic és a P3, P4 o P10 amb el display actiu (comparteixen circuit): passa'l a P0/P1/P2 |
| La cara no canvia mai | `FRED`/`CALOR` mal calibrats per a la temperatura real de l'aula: llegeix el valor amb el REPL abans de fixar els llindars |
| `temp_interna` sembla més alta que la temperatura real de l'aula | El sensor intern és a prop del processador i nota una mica la seva pròpia escalfor: és normal, per això es documenten els **dos** sensors |

## 🔗 On ho aplicaràs

- **Ara mateix:** reutilitza la funció `mapa()` de [`nivell_llum`](../nivell_llum/EXPLICACIO.md).
- **Sessió 3:** el patró "llegir → comparar amb un llindar → decidir" és exactament el que fa servir [`mascota_reactiva`](../mascota_reactiva/EXPLICACIO.md) per a cada sensor.
- **Simulador:** python.microbit.org simula `temperature()` (sensor intern), però **no** el sensor extern del Kit 1: valida la interpretació amb condicionals a la placa real.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA3](../../../../Reptes/Reptes_SA3.md)**.
