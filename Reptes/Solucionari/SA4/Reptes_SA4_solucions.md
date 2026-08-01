# SA4 · Solucionari dels reptes — Funcions i moviment

> **Material del docent.** Solucions completes dels tres reptes de [`Reptes_SA4.md`](../../Reptes_SA4.md), amb el nucli i les tres ampliacions graduades ja incorporades. **No es reparteix a l'alumnat abans que hagi entregat el seu propi repte**: com l'exemple resolt de la SA, serveix per corregir i, si cal, per mostrar *després* del primer intent.

> Cada solució és una còpia exacta del fitxer `.py` de la seva carpeta (`repte1_salutacio_aparador/`, `repte2_aparcament_precisio/`, `repte3_coreografia_benvinguda/`): si canvies un fitxer, actualitza també el bloc de codi d'aquí sota.

---

## ⭐ Repte 1 · Salutació programable per a un aparador

**Idea de la solució:** una funció `salutacio(estil, vegades)` amb dos paràmetres que tria entre `saluda()`/`escombra()` (nucli), un tercer estil `'doble'` que combina totes dues (ampliació 1), una cara pròpia per estil (ampliació 2) i un **comptador** `index_estil` (0/1/2) que decideix per `if/elif` quin estil toca a cada torn amb el botó A (ampliació 3).

```python
# SA4 - Repte 1 (SOLUCIO): salutacio programable per a un aparador
# Nucli + ampliacions 1-3: tercer estil "doble", cara al display segons
# l'estil, i seleccio de l'estil amb el boto A per torns.
# Maquinari: servo de la mascota al pin P0 (Kit 2, com funcions_moviments.py).

from microbit import *

pin0.set_analog_period(20)

index_estil = 0   # ampliacio 3: comptador 0/1/2 que cicla els tres estils


def graus_a_pwm(angle):
    return 26 + (angle * (128 - 26)) // 180


def mou_servo(angle):
    pin0.write_analog(graus_a_pwm(angle))


def saluda(vegades):
    for i in range(vegades):
        mou_servo(0)
        sleep(300)
        mou_servo(180)
        sleep(300)
    mou_servo(90)


def escombra(angle_maxim):
    for angle in range(0, angle_maxim + 1, 20):
        mou_servo(angle)
        sleep(80)
    for angle in range(angle_maxim, -1, -20):
        mou_servo(angle)
        sleep(80)


def salutacio(estil, vegades):
    # Funcio amb DOS parametres: "estil" tria quin moviment fer, "vegades"
    # quantes vegades es repeteix.
    if estil == 'curt':
        display.show(Image.HAPPY)          # ampliacio 2: cara segons l'estil
        saluda(vegades)
    elif estil == 'llarg':
        display.show(Image.SURPRISED)
        escombra(180)
    elif estil == 'doble':
        # Ampliacio 1: tercer estil que combina els dos anteriors.
        display.show(Image.HEART)
        saluda(vegades)
        escombra(120)


while True:
    if button_a.was_pressed():
        # Ampliacio 3: cada premuda tria el seguent estil, segons el comptador.
        if index_estil == 0:
            estil_actual = 'curt'
        elif index_estil == 1:
            estil_actual = 'llarg'
        else:
            estil_actual = 'doble'
        salutacio(estil_actual, 2)
        index_estil = index_estil + 1
        if index_estil == 3:
            index_estil = 0   # torna a comencar el cicle
    sleep(20)
```

---

## ⭐⭐ Repte 2 · Aparcament automàtic de precisió

**Idea de la solució:** una funció `frenada(velocitat_inicial)` que baixa el PWM de mica en mica (nucli), `arrencada(velocitat_final)` simètrica (ampliació 1), `trajecte(velocitat, temps_avancant)` que les encadena (ampliació 2) i dues velocitats segons quins botons es premen (ampliació 3).

```python
# SA4 - Repte 2 (SOLUCIO): aparcament automatic de precisio
# Nucli + ampliacions 1-3: arrencada progressiva, funcio trajecte() que
# combina arrencada+avanc+frenada, i dues velocitats segons boto A o A+B.
# Maquinari: motoreductors M1 (pin13/pin14) i M2 (pin15/pin16), com a
# velocitat_pwm.py. Alimentacio externa (piles), mai per USB.

from microbit import *

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

PAS_PWM = 64   # salt de velocitat a cada iteracio de la rampa


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def arrencada(velocitat_final):
    # Ampliacio 1: puja la velocitat de mica en mica en lloc de saltar
    # directament al valor final.
    for v in range(0, velocitat_final + 1, PAS_PWM):
        avancar(v)
        sleep(30)


def frenada(velocitat_inicial):
    # Nucli: baixa la velocitat de mica en mica fins aturar-se del tot.
    for v in range(velocitat_inicial, -1, -PAS_PWM):
        avancar(v)
        sleep(30)
    aturar()


def trajecte(velocitat, temps_avancant):
    # Ampliacio 2: arrencada + avanc a velocitat constant + frenada.
    arrencada(velocitat)
    sleep(temps_avancant)
    frenada(velocitat)


while True:
    # Ampliacio 3: dues velocitats diferents segons quins botons es premen.
    if button_a.is_pressed() and button_b.is_pressed():
        trajecte(1023, 800)   # rapid
    elif button_a.was_pressed():
        trajecte(400, 800)    # lent
    sleep(20)
```

---

## ⭐⭐⭐ Repte 3 · Coreografia de benvinguda amb servo, so i motors

**Idea de la solució:** `benvinguda(velocitat)` combina servo/so/display i un avanç del vehicle (nucli); `comiat(velocitat)` és la funció simètrica (ampliació 1); totes dues s'encadenen amb els botons A/B i el botó B ho atura tot sempre (ampliació 2); la velocitat és un paràmetre propi de cada crida (ampliació 3).

```python
# SA4 - Repte 3 (SOLUCIO): coreografia de benvinguda amb servo, so i motors
# Nucli + ampliacions 1-3: funcio comiat() simetrica, seguencia per botons
# A/B (B atura sempre) i velocitat com a parametre de cada crida.
# Maquinari: servo P0 + brunzidor P2 (mascota, com coreografia.py) i
# motoreductors M1/M2 (vehicle, com velocitat_pwm.py).

from microbit import *
import music

pin0.set_analog_period(20)

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16


def graus_a_pwm(angle):
    return 26 + (angle * (128 - 26)) // 180


def mou_servo(angle):
    pin0.write_analog(graus_a_pwm(angle))


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def retrocedir(velocitat):
    M1_ENRERE.write_analog(velocitat)
    M1_ENDAVANT.write_digital(0)
    M2_ENRERE.write_analog(velocitat)
    M2_ENDAVANT.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def benvinguda(velocitat):
    # Nucli: primer la part de servo/so/display, despres un avanc breu.
    # Ampliacio 3: "velocitat" es parametre propi d'aquesta crida.
    display.show(Image.HAPPY)
    mou_servo(0)
    music.pitch(880, 150, pin=pin2)
    mou_servo(180)
    music.pitch(660, 150, pin=pin2)
    mou_servo(90)
    avancar(velocitat)
    sleep(600)
    aturar()


def comiat(velocitat):
    # Ampliacio 1: simetrica a benvinguda(), amb un recul en lloc d'avancar.
    display.show(Image.SAD)
    mou_servo(180)
    music.pitch(440, 200, pin=pin2)
    mou_servo(90)
    retrocedir(velocitat)
    sleep(600)
    aturar()


# --- Ampliacio 2: seguencia per botons, amb B aturant-ho tot sempre ---
PAS = 0

while True:
    if button_a.was_pressed():
        if PAS == 0:
            benvinguda(400)
            PAS = 1
        else:
            comiat(400)
            PAS = 0
    if button_b.was_pressed():
        aturar()
        display.show(Image.NO)
        PAS = 0
    sleep(20)
```

---

*Solucionari de la SA4. Material del docent. Es recolza en `Classes/SA4/codi/`. Llicència CC BY-SA 4.0.*
