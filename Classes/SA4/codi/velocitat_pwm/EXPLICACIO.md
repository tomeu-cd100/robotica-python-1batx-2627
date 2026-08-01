# Velocitat i sentit del motoreductor amb PWM (Sessió 2)

**Quan es fa:** Sessió 2 · **Fitxer:** `velocitat_pwm.py` · **Maquinari:** [esquemes de connexions](../../SA4_esquemes_connexions.md) — 2 motoreductors del Kit 2, canals **M1** (pin13 endavant / pin14 enrere) i **M2** (pin15 endavant / pin16 enrere) del driver del Micro:shield; alimentació externa (portapiles), **mai** des de l'USB

> ✋ Aquesta pàgina explica el codi **model**. Munta els motoreductors seguint exactament l'[esquema](../../SA4_esquemes_connexions.md) abans d'alimentar-los.

## 🎯 Per què fem aquesta pràctica

Un motoreductor no és com un servo: no va a un angle, **gira contínuament** en un sentit o l'altre, i la seva velocitat es regula amb **PWM** (`write_analog`, com ja vas fer amb el LED de la SA2). Avui encapsules el control del motor en quatre funcions pròpies —`avancar()`, `retrocedir()`, `girar()`, `aturar()`— que seran la base de tot el moviment del vehicle T2 fins al final del curs.

## 🔮 Abans d'executar: prediu

Cada motor porta **dos** pins (un per a cada sentit). Si `avancar(500)` envia PWM al pin "endavant" i deixa l'altre a `0`, què hauria de passar si, per error, enviessis PWM als **dos** pins alhora?

## 🧠 El codi, per blocs

### Bloc 1 — Constants amb nom: els quatre pins dels motors

```python
M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16
```

Donar **nom** als pins (en lloc d'escriure `pin13` cada vegada) fa que la resta del codi s'entengui sense haver de consultar l'esquema constantment, i és el mateix truc que ja vas fer servir amb `servo_orelles = pin0` al dossier de la mascota.

### Bloc 2 — Una funció amb un paràmetre: `avancar(velocitat)`

```python
def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)
```

El **sentit** de gir es decideix triant a QUIN dels dos pins del motor s'envia el PWM; la **velocitat** és el valor mateix (0-1023, la mateixa escala que ja coneixes de `write_analog`). `retrocedir(velocitat)` fa exactament el mateix però intercanviant quin pin rep el PWM i quin es posa a 0.

### Bloc 3 — Girar sobre el propi eix: `girar(costat)`

```python
def girar(costat):
    velocitat_gir = 300
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat_gir)
        ...
```

`girar()` rep un paràmetre de **text** (`'esquerra'` o `'dreta'`) i posa un motor endavant i l'altre enrere: així el vehicle gira **sobre el seu propi eix** en lloc de descriure una corba àmplia.

### Bloc 4 — Aturar sense paràmetres: `aturar()`

```python
def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)
```

No totes les funcions necessiten paràmetres: `aturar()` sempre fa el mateix (velocitat 0 als quatre pins), així que no en rep cap.

### Bloc 5 — ACTIVITAT NUCLI (Sessió 2): escriu tu una funció AMB VALOR DE RETORN

> ✍️ **Abans de mirar aquest bloc:** intenta escriure tu mateix `temps_per_recorregut(cm)`. Pista: no ha de moure res (com `mou_servo()`), ha de **calcular i retornar** un número (com `graus_a_pwm()` a la SA4-S1).

```python
CM_PER_SEGON = 20


def temps_per_recorregut(cm):
    return int((cm / CM_PER_SEGON) * 1000)


avancar(400)
sleep(temps_per_recorregut(30))   # avanca uns 30 cm i para
aturar()
```

Aquesta és la primera funció **amb valor de retorn que escrius tu** (a la S1 vas veure `graus_a_pwm()` ja feta): `temps_per_recorregut(cm)` no mou el vehicle, només **calcula** quants mil·lisegons cal mantenir el motor engegat per recórrer els centímetres que li demanis, a partir d'una velocitat de referència calibrada (`CM_PER_SEGON`, ajusta-la cronometrant el teu propi vehicle). Fixa't com **s'usa** el resultat: `sleep(temps_per_recorregut(30))` en lloc d'un `sleep(1500)` fix — si canvies `CM_PER_SEGON` (per exemple perquè has canviat les piles), el `30` continua volent dir "30 cm", el càlcul s'adapta sol.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| Un motor no es mou | Micro:shield alimentat només per USB (els motors necessiten l'alimentació externa de les piles) |
| Un motor gira al revés del que esperaves | Sentit del cablatge del canal M1/M2 invertit; inverteix el signe a `avancar()`/`retrocedir()`, no recablis |
| El vehicle no avança recte | PWM desigual entre M1 i M2: calibra els valors de cada motor per compensar |
| Els dos pins d'un motor reben PWM alhora | Error de programació (bloqueja el motor o el fa vibrar sense girar); revisa que l'altre pin es posi sempre a `0` |

## 🔗 On ho aplicaràs

- **Ara mateix:** primera prova dels motoreductors, encara sense el xassís muntat (es cablegen igual que quedaran al vehicle definitiu).
- **Sessió 3:** [`control_per_botons.py`](../control_per_botons/EXPLICACIO.md) reutilitza aquestes mateixes quatre funcions activades amb els botons A/B — és el **producte** de la SA4.
- **Sessió 4:** aquests mateixos pins (M1/M2) es fixen **definitivament** en muntar el xassís del vehicle T2 i no es tornen a tocar a T3 (vegeu `00_Projecte_T2_Vehicle.md`).
- **Simulador:** python.microbit.org **no** simula els motoreductors: cal maquinari real des del primer moment.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA4](../../../../Reptes/Reptes_SA4.md)**.
