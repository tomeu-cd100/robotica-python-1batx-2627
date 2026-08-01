# El rover va recte: calibratge de motors (Sessió 1)

**Quan es fa:** Sessió 1 · **Fitxer:** `calibratge_motors.py` · **Maquinari:** [esquemes de connexions](../../SA7_esquemes_connexions.md) — motoreductors del vehicle T2, **M1**=P13/P14, **M2**=P15/P16 (no es toquen, ja cablejats des de SA4)

## 🎯 Per què fem aquesta pràctica

Les funcions `avancar()`, `retrocedir()`, `girar()` i `aturar()` són les mateixes de la SA4 (mateixos pins, mateixa lògica): el rover no aprèn cap pin nou per moure's. A partir d'aquí, `girar()` guanya un segon paràmetre **opcional** de velocitat (`girar(costat, velocitat=300)`, vegeu `segueix_linia.py`/`evita_obstacles.py`) per als girs suaus dels comportaments autònoms; les crides a l'estil SA4 (`girar('dreta')`) continuen funcionant igual. El que sí és nou és la **cinemàtica diferencial**: el rover gira variant la velocitat/sentit relatiu de cada roda, i per la mateixa raó, si els dos motoreductors no surten idèntics de fàbrica, el rover **es desvia** en avançar "recte" encara que els dos rebin la mateixa consigna de PWM.

## 🔮 Abans d'executar: prediu

Si envies la mateixa velocitat (per exemple, 500) als dos motors i el rover es desvia cap a la dreta en avançar, quin dels dos motors (M1 esquerre o M2 dret) creus que gira relativament més fort?

## 🧠 El codi, per blocs

### Bloc 1 — Els factors de calibratge

```python
FACTOR_M1 = 1.0
FACTOR_M2 = 0.92
```

Cada motor té el seu propi **factor** (0,0-1,0) que multiplica la velocitat demanada. Si el rover es desvia cap a la dreta, el motor esquerre (M1) "guanya": es pot baixar `FACTOR_M1` o pujar `FACTOR_M2` fins que la trajectòria quedi recta.

### Bloc 2 — Aplicar el factor a cada motor per separat

```python
M1_ENDAVANT.write_analog(int(velocitat * FACTOR_M1))
...
M2_ENDAVANT.write_analog(int(velocitat * FACTOR_M2))
```

`avancar_calibrat()` és la mateixa idea que `avancar()` de la SA4, però **cada motor rep la seva pròpia velocitat compensada**, no la mateixa consigna crua. `int(...)` és necessari perquè `write_analog()` espera un enter.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El rover es desvia sempre cap al mateix costat | Encara no has ajustat `FACTOR_M1`/`FACTOR_M2`: calibra amb proves curtes i repetides |
| El rover gira en comptes d'avançar | Els dos factors són molt diferents entre si (per exemple, un a 1.0 i l'altre a 0.3): revisa que el desequilibri real dels motors no sigui tan gran |
| Els girs de `girar()` també surten torts | Normal: aquesta funció **no** es calibra (la simetria del gir ja compensa prou per a proves curtes); no és un error del calibratge |

## 🔗 On ho aplicaràs

- **Ara mateix:** és la base de qualsevol trajectòria del rover (S1-S4): un rover que no va recte no pot seguir una línia ni apuntar bé cap a un obstacle.
- **Sessió 4 (producte):** [`rover_missions`](../rover_missions/EXPLICACIO.md) fa servir la mateixa idea de moviment calibrat a la missió «quadrat».
- **Simulador:** python.microbit.org **no** simula els motoreductors: aquesta pràctica es fa **només** amb maquinari real.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA7](../../../../Reptes/Reptes_SA7.md)**.
