# Control per botons (PRODUCTE de la SA4, Sessió 3)

**Quan es fa:** Sessió 3 (repte, producte de la SA) · **Fitxer:** `control_per_botons.py` · **Maquinari:** [esquemes de connexions](../../SA4_esquemes_connexions.md) i [dossier del vehicle T2](../../../00_General/00_Projecte_T2_Vehicle.md) — motoreductors als canals **M1/M2** (pins fixats a `velocitat_pwm.py`), botons **A/B** interns

> ✋ **Aquesta pàgina mostra la SOLUCIÓ del producte "control per botons".** És el **producte de la SA4**: intenta-ho pel teu compte a l'Activitat 3 de la [fitxa](../../SA4_fitxa_alumnat.md) abans de mirar-la sencera.

## 🎯 Per què fem aquesta pràctica

Aquesta és la **integració**: les quatre funcions de moviment de `velocitat_pwm.py` (`avancar`, `retrocedir`, `girar`, `aturar`) encadenades en una **seqüència** i activades amb els botons A/B, com si fossin un comandament molt bàsic. És la base sobre la qual la SA5 construirà el control remot **de veritat**, per ràdio.

## 🔮 Abans d'executar: prediu

Prems A quatre vegades seguides: quin serà el cinquè pas (torna a començar la seqüència o continua endavant)? I si en algun moment prems B enmig d'un gir, què hauria de passar?

## 🧠 El codi, per blocs

### Bloc 1 — Les quatre funcions de moviment (repetides de `velocitat_pwm.py`)

Cada fitxer de `codi/` és independent (com a la resta del curs): `control_per_botons.py` torna a definir `avancar()`, `retrocedir()`, `girar()` i `aturar()` amb els mateixos pins, perquè és un programa autònom que es pot transferir sol a la placa.

### Bloc 2 — Una seqüència amb estat: `seguent_moviment()`

```python
PAS = 0

def seguent_moviment():
    global PAS
    if PAS == 0:
        display.show(Image.ARROW_N)
        avancar(VELOCITAT)
    elif PAS == 1:
        ...
    PAS = (PAS + 1) % 4
```

La variable `PAS` recorda **en quin punt** de la seqüència estem; cada crida a `seguent_moviment()` executa el pas actual i avança al següent (`% 4` fa que torni a `0` després del quart pas). El display mostra una fletxa diferent a cada pas perquè es vegi la seqüència sense haver de veure el vehicle en moviment.

### Bloc 3 — El botó B sempre atura, es processi on es processi

```python
if button_b.was_pressed():
    aturar()
    display.show(Image.NO)
    PAS = 0
```

Aquesta idea —una entrada que **sempre** interromp el que s'estigui fent, sense esperar el seu torn— és exactament el mateix concepte que la SA6 formalitzarà com a estat **STOP prioritari**: avui en fas una primera versió senzilla.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El vehicle no respon a cap botó | `button_a.was_pressed()` només detecta **premudes noves**; si el mantens premut des d'abans de carregar el programa no es detecta la primera vegada |
| La seqüència es "salta" un pas | El botó s'ha premut més d'un cop molt seguit (rebot); `was_pressed()` ja inclou antirebot intern, però comprova-ho igualment |
| El vehicle no s'atura mai del tot | `aturar()` no posa els QUATRE pins a `0`; revisa que no en falti cap |

## 🔗 On ho aplicaràs

- **Ara mateix:** és el **producte de la SA4** (repte «control per botons», avaluat amb R1/R2/R3).
- **SA5:** el mateix esquema (botó → funció de moviment) es converteix en «missatge de ràdio rebut → funció de moviment».
- **SA6:** el botó B d'avui («sempre atura») es formalitza com a estat **STOP prioritari** amb un polsador dedicat al xassís.
- **Simulador:** els botons A/B es simulen, però com que les funcions de moviment criden `write_analog`/`write_digital` sobre motors reals, substitueix-les temporalment per `display.scroll(...)` per validar la **lògica** de la seqüència sense maquinari.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA4](../../../../Reptes/Reptes_SA4.md)**.
