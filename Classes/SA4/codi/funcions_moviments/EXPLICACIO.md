# Funcions de moviment del servo (Sessió 1)

**Quan es fa:** Sessió 1 · **Fitxer:** `funcions_moviments.py` · **Maquinari:** [esquemes de connexions](../../SA4_esquemes_connexions.md) — micro servo de la mascota (Kit 2) al pin **P0** (muntat des de la SA2, avui es programa per primer cop)

> ✋ Aquesta pàgina explica el codi **model**. Intenta llegir-lo i predir què farà abans de mirar l'explicació sencera (Activitat 1 de la [fitxa](../../SA4_fitxa_alumnat.md)).

## 🎯 Per què fem aquesta pràctica

Fins avui ja havies **usat** codi organitzat en blocs que es criden (`respira()`/`mostra_color()` a la SA2, `mapa()`/`canvia_emocio()` a la SA3) sense parar-t'hi a pensar què eren. Avui poses **nom** al concepte: una **funció** és un tros de codi amb un nom propi que pots **cridar** tantes vegades com vulguis, amb **paràmetres** diferents cada vegada, sense reescriure'l. La fem servir per moure el servo de la mascota (P0), que està muntat des de la SA2 però encara no s'havia programat.

## 🔮 Abans d'executar: prediu

Si crides `escombra(60)` i després `escombra(180)`, el servo farà **el mateix** recorregut les dues vegades, o un de diferent? Per què, si el codi de la funció no ha canviat?

## 🧠 El codi, per blocs

### Bloc 1 — Preparar el servo: `set_analog_period`

```python
pin0.set_analog_period(20)
```

Un servo estàndard espera rebre un pols cada **20 ms** (50 Hz): `set_analog_period(20)` ho fixa un sol cop, a l'inici del programa, abans de moure res.

### Bloc 2 — Una funció AMB VALOR DE RETORN: `graus_a_pwm(angle)`

```python
def graus_a_pwm(angle):
    return 26 + (angle * (128 - 26)) // 180
```

Aquesta funció **no mou res**: només calcula i **retorna** (`return`) el valor que `write_analog` necessita (~26-128) a partir d'un angle en graus (0-180). És el mateix patró que `mapa()` a la SA3, adaptat al servo: entrada (angle) → càlcul → sortida (valor PWM), sense cap efecte visible per si sola.

### Bloc 3 — Una funció AMB UN PARÀMETRE: `mou_servo(angle)`

```python
def mou_servo(angle):
    pin0.write_analog(graus_a_pwm(angle))
```

`mou_servo` és el nostre propi «`set_angle()`»: rep **un paràmetre** (`angle`) i s'encarrega de convertir-lo i enviar-lo al pin. Fixa't que **crida** `graus_a_pwm()` per dins: una funció en pot cridar una altra — així és com es construeixen ordres cada cop més senzilles a partir d'ordres més bàsiques.

### Bloc 4 — Funcions amb paràmetre que es repeteixen: `saluda(vegades)` i `escombra(angle_maxim)`

```python
def saluda(vegades):
    for i in range(vegades):
        mou_servo(0)
        sleep(300)
        mou_servo(180)
        sleep(300)
    mou_servo(90)
```

Sense funcions, per saludar 2 vegades i després 3, hauries de **copiar i enganxar** el mateix bloc de 4 línies diverses vegades, canviant només el número. Amb `saluda(vegades)`, el codi és **un** i el crides amb l'argument que et convingui: `saluda(2)`, `saluda(5)`... Això és **reutilització de codi**, un dels motius principals per fer servir funcions.

`escombra(angle_maxim)` fa el mateix amb un recorregut: la **mateixa** funció serveix per a una escombrada curta (`escombra(60)`) o llarga (`escombra(180)`) només canviant l'argument.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El servo no es mou (però el programa no dona error) | El simulador python.microbit.org **no** simula el servo; cal maquinari real |
| El servo "tremola" o la placa es reinicia en moure'l | Micro:shield alimentat només per USB; cal alimentació externa (portapiles) per als servos |
| `mou_servo(200)` fa un moviment estrany | L'angle ha de ser 0-180; fora d'aquest rang `graus_a_pwm()` calcula un valor fora del que el servo espera |
| Oblido cridar `pin0.set_analog_period(20)` | El servo pot vibrar o no assentar-se bé a cada posició |

## 🔗 On ho aplicaràs

- **Ara mateix:** primer ús programat del servo de la mascota (P0), muntat des de la SA2.
- **Sessió 1-2:** [`coreografia.py`](../coreografia/EXPLICACIO.md) combina aquestes mateixes idees amb so i display.
- **Simulador:** la **lògica** de les funcions (bucles, `range`, paràmetres) es pot escriure i revisar al simulador, però el moviment real del servo només es veu amb maquinari.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA4](../../../../Reptes/Reptes_SA4.md)**.
