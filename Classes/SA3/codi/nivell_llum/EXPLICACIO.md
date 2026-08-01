# Nivell de llum: intern vs extern

**Quan es fa:** Sessió 2 (modelatge) · **Fitxer:** `nivell_llum.py` · **Maquinari:** [esquemes de connexions](../../SA3_esquemes_connexions.md) — sensor de llum extern del Kit 2 al pin **P0** (ADC vàlid); sensor de llum **intern** de la micro:bit (cap cablatge)

> ⚠️ **Per què P0 i no P3?** P3, P4 i P10 també tenen ADC, però comparteixen circuit amb el display: `read_analog()` hi falla (`ValueError: Pin in display mode`) mentre el display estigui actiu, com passa aquí (les barres). P0/P1/P2 són ADC lliures de display.

## 🎯 Per què fem aquesta pràctica

Fins ara la micro:bit **actuava**; avui **percep**. El sensor de llum intern (`display.read_light_level()`) reaprofita la matriu de LED com a fotodiode: llegeix **0-255**. El sensor extern del Kit 2 és un component ADC normal: llegeix **0-1023**, com qualsevol pin analògic. Aquesta pràctica compara els dos i "mapa" la lectura a un indicador de barres, la mateixa idea que faries amb un potenciòmetre.

## 🔮 Abans d'executar: prediu

Amb la mà tapant el sensor extern, quantes barres esperes veure? I si l'apuntes a un llum? Escriu la teva predicció abans de provar-ho a l'Activitat 2 de la [fitxa](../../SA3_fitxa_alumnat.md).

## 🧠 El codi, per blocs

### Bloc 1 — Mapar un rang a un altre: `mapa()`

```python
def mapa(valor, entrada_min, entrada_max, sortida_min, sortida_max):
    rang_entrada = entrada_max - entrada_min
    rang_sortida = sortida_max - sortida_min
    proporcio = (valor - entrada_min) / rang_entrada
    return int(sortida_min + proporcio * rang_sortida)
```

MicroPython **no té** una funció `map()` integrada (com sí té Arduino): la programem nosaltres amb una regla de tres. `mapa(512, 0, 1023, 0, 5)` calcula quina posició (0-5) li toca a un valor a la meitat del rang 0-1023. La mateixa funció serveix per **qualsevol** sensor analògic (llum, potenciòmetre, temperatura): només canvien els rangs.

### Bloc 2 — Barres al display

```python
def barres(n):
    display.clear()
    for columna in range(min(n, 5)):
        for fila in range(5):
            display.set_pixel(columna, 4 - fila, 9)
```

`display.set_pixel(x, y, brillantor)` encén **un** píxel concret (brillantor 0-9), a diferència de `display.show()` que dibuixa una imatge sencera. Encenent columna a columna es dibuixa un indicador de nivell, com el VU-metre d'un equip de música.

### Bloc 3 — Dos sensors, dues escales diferents

```python
llum_interna = display.read_light_level()      # 0-255
llum_externa = pin0.read_analog()               # 0-1023
```

Fixa't que **no** són la mateixa escala: el sensor intern dona 0-255, el de P0 dona 0-1023 (com tots els pins ADC). Barrejar-les sense adonar-te'n és un error típic — sempre cal saber **quin rang** dona cada sensor abans de comparar-lo o mapar-lo.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| `pin0.read_analog()` sempre dona el mateix valor | El sensor extern no és a un pin **ADC vàlid** (només P0, P1, P2, P3, P4, P10) o el cablatge és incorrecte |
| `ValueError: Pin in display mode` | El sensor analògic és a P3, P4 o P10 amb el display actiu (comparteixen circuit): passa'l a P0/P1/P2 |
| Les barres no es mouen mai | S'ha confós l'escala 0-255 (intern) amb la 0-1023 (extern) als paràmetres de `mapa()` |
| El display "parpelleja" estrany en comptes de mostrar barres netes | Falta `display.clear()` a `barres()`: els píxels de la volta anterior es queden encesos |

## 🔗 On ho aplicaràs

- **Ara mateix:** [`termometre`](../termometre/EXPLICACIO.md) reutilitza la mateixa idea de "sensor intern vs extern" i la mateixa `mapa()`.
- **Sessió 3:** [`mascota_reactiva`](../mascota_reactiva/EXPLICACIO.md) fa servir `display.read_light_level()` per decidir quan la mascota "s'adorm".
- **Simulador:** python.microbit.org simula el sensor de llum **intern** (`display.read_light_level()`), però **no** el sensor extern del Kit 2 (`pin0.read_analog()`): la part de barres només es veu sencera amb maquinari real.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA3](../../../../Reptes/Reptes_SA3.md)**.
