# Música amb l'altaveu

**Quan es fa:** Sessió 2 (modelatge) · **Fitxer:** `musica_altaveu.py` · **Maquinari:** [esquemes de connexions](../../SA2_esquemes_connexions.md) — brunzidor extern al pin **P2** (o l'altaveu integrat de la micro:bit V2)

## 🎯 Per què fem aquesta pràctica

El so és una altra sortida **PWM**: cada nota és una ona a una freqüència concreta. El mòdul `music` t'ho fa fàcil, sense haver de calcular ones tu mateix: li dónes notes i temps, i ell genera el senyal.

## 🔮 Abans d'executar: prediu

Mira el codi complet **sense executar-lo**. Si prems el botó A i després el B, quins dos sons sentiràs, greu o agut cadascun? I si toques el logo? Comprova-ho a l'Activitat 2 de la [fitxa](../../SA2_fitxa_alumnat.md).

## 🧠 El codi, per blocs

### Bloc 1 — Un to concret: `music.pitch()`

```python
music.pitch(262, 300, pin=pin2)   # 262 Hz durant 300 ms, pel pin P2
```

`music.pitch(freqüència, durada)` reprodueix un **to pur** a la freqüència indicada (en Hz) durant els mil·lisegons indicats. Com més gran la freqüència, més **agut** sona. L'argument `pin=pin2` diu **per on** surt el so (el brunzidor extern); sense indicar-lo, sortiria per l'altaveu integrat.

### Bloc 2 — Una melodia: `music.play()`

```python
MELODIA = ['C4:4', 'E4:4', 'G4:4', 'C5:8']
music.play(MELODIA, pin=pin2)
```

Cada element és `"NotaOctava:Durada"` (Do4, durada 4 "temps"). `music.play(...)` reprodueix la llista **en ordre** i **espera** que acabi abans de continuar amb la línia següent del programa.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| No se sent res | Falta `pin=pin2` (el so va per defecte a l'altaveu integrat, no al brunzidor extern), o el brunzidor mal connectat |
| El programa es "penja" mentre sona la melodia | No és un error: `music.play()` **espera** a acabar. Si vols que continuï fent altres coses alhora, cal l'argument `wait=False`. |
| Els dos botons sonen igual | S'han copiat els mateixos números de freqüència als dos `pitch()` | Revisa que cada branca de l'`if`/`elif` porti una freqüència diferent. |

## 🔗 On ho aplicaràs

- **Ara mateix:** [`pwm_led_rgb`](../pwm_led_rgb/EXPLICACIO.md), la mateixa idea de "senyal continu" aplicada a la llum.
- **Sessió 3 (repte):** [`semafor_rele`](../semafor_rele/EXPLICACIO.md) fa sonar un avís a la fase ambre amb `music.pitch()`.
- **Sessió 4:** les melodies d'estat de la **mascota** (el seu "somriure sonor") parteixen d'aquest mateix codi.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA2](../../../../Reptes/Reptes_SA2.md)**.
