# Alarma d'ultrasons

**Quan es fa:** Sessió 3 (modelatge, abans del producte) · **Fitxer:** `alarma_ultrasons.py` · **Maquinari:** [esquemes de connexions](../../SA3_esquemes_connexions.md) — HC-SR04 (Kit 2) a 5 V, trigger **P14**, echo **P15**; brunzidor **P2** (Kit 1)

## 🎯 Per què fem aquesta pràctica

El sensor d'ultrasons **no** llegeix un valor directament: envia un **pols de so** (ultrasò, inaudible) i mesura **quant triga a tornar l'eco**. Aquest "temps de vol" (*time-of-flight*) és proporcional a la distància, perquè el so viatja a una velocitat coneguda. És una manera diferent de mesurar que les entrades analògiques directes de `nivell_llum`/`termometre`.

## 🔮 Abans d'executar: prediu

Si apropes la mà lentament al sensor, què esperes que passi amb la xifra del display i amb el so? A partir de quina distància (aproximada) creus que sonarà l'alarma?

## 🧠 El codi, per blocs

### Bloc 1 — El trigger: un pols curtíssim

```python
pin14.write_digital(0)
utime.sleep_us(2)
pin14.write_digital(1)
utime.sleep_us(10)
pin14.write_digital(0)
```

El mòdul envia l'ultrasò quan el pin de **trigger** puja a 1 durant uns 10 microsegons (µs), **no** mil·lisegons: `sleep()` de `microbit` no baixa d'aquest ordre de magnitud, per això aquí es fa servir `utime.sleep_us()`.

### Bloc 2 — L'echo: `machine.time_pulse_us`

```python
durada_us = machine.time_pulse_us(pin15, 1, 30000)
```

`time_pulse_us(pin, valor, timeout)` mesura **quants microsegons** el pin indicat es queda al valor donat (aquí, `1`): és exactament el temps que triga el so a anar i tornar. El `timeout` (30000 µs) evita que el programa es quedi penjat si no arriba cap eco (objecte massa lluny o massa a prop).

### Bloc 3 — De temps a distància

```python
return (durada_us * VELOCITAT_SO_CM_US) / 2
```

`distancia = temps × velocitat`, però el temps mesurat és el d'**anada i tornada**: per això es divideix entre 2. `VELOCITAT_SO_CM_US` (0,0343 cm/µs) és la velocitat del so a l'aire, a temperatura ambient.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| `time_pulse_us` retorna sempre `-1` (o negatiu) | Cap eco dins del `timeout`: comprova el cablatge de trigger/echo o que hi hagi un objecte dins de l'abast |
| La distància surt sempre molt més gran del que toca | S'ha oblidat dividir entre 2 (anada **i** tornada) |
| El mòdul no arriba a funcionar bé, o s'escalfa | Alimentat a 3,3 V en lloc dels 5 V que necessita l'HC-SR04: revisa el connector del Micro:shield |
| Comportament erràtic amb l'echo, o risc pel pin | Alguns mòduls HC-SR04 donen l'echo a 5 V: si el teu mòdul concret ho fa, cal un **divisor de tensió** abans del pin (vegeu l'esquema) |

## 🔗 On ho aplicaràs

- **Ara mateix:** és la preparació tècnica abans del producte de la SA.
- **Sessió 3 (producte):** [`mascota_reactiva`](../mascota_reactiva/EXPLICACIO.md) **no** incorpora l'ultrasò (el cablatge final de la mascota no en té; fa servir el PIR per detectar presència), però el mètode "mesurar temps → calcular → decidir" hi reapareix igualment.
- **Simulador:** python.microbit.org **no** simula cap sensor extern, i molt menys el temps de vol de l'HC-SR04: aquesta pràctica es fa **només** amb maquinari real.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA3](../../../../Reptes/Reptes_SA3.md)**.
