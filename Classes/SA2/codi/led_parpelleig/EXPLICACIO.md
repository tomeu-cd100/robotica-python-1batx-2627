# LED parpellejant amb comptador

**Quan es fa:** Sessió 1 (modelatge) · **Fitxer:** `led_parpelleig.py` · **Maquinari:** [esquemes de connexions](../../SA2_esquemes_connexions.md) — LED extern al pin **P1** del Micro:shield (Kit 1)

## 🎯 Per què fem aquesta pràctica

A la SA1 vas fer parpellejar la **matriu de LED** integrada. Ara controlaràs un **LED extern**, connectat pel teu al Micro:shield: és el primer cop que la micro:bit **actua sobre un component fora de la placa**. També hi combines dues eines noves: el bucle `while True:` amb **temporitzacions dobles** (encès/apagat) i un **acumulador** que compta quants cops ha passat alguna cosa.

## 🔮 Abans d'executar: prediu

Mira el codi complet (a baix) **sense executar-lo**. Quant de temps estarà encès el LED cada cicle? Cada quants parpellejos apareixerà un número al display? Escriu-ho a l'Activitat 1 de la [fitxa](../../SA2_fitxa_alumnat.md) i comprova-ho després.

## 🧠 El codi, per blocs

### Bloc 1 — Una sortida digital: `write_digital()`

```python
pin1.write_digital(1)   # LED ences
sleep(500)
pin1.write_digital(0)   # LED apagat
```

`pin1` és l'objecte que representa el pin físic P1 del Micro:shield. `write_digital(1)` envia **3,3 V** (LED encès); `write_digital(0)` envia **0 V** (LED apagat). Només hi ha aquests dos estats possibles: és una sortida **digital**, com un interruptor.

### Bloc 2 — Un acumulador: comptar parpellejos

```python
comptador = 0   # abans del bucle: comença de zero

while True:
    ...
    comptador = comptador + 1   # dins del bucle: suma 1 cada volta
```

Un **acumulador** és una variable que es va actualitzant a partir del seu propi valor anterior. S'inicialitza **una sola vegada, fora del bucle**; si s'inicialitzés dins, tornaria a zero a cada volta i mai no avançaria.

### Bloc 3 — Actuar només de tant en tant: l'operador `%`

```python
if comptador % 10 == 0:
    display.scroll(str(comptador))
```

`comptador % 10` és el **residu** de dividir `comptador` entre 10: val `0` exactament quan `comptador` és múltiple de 10 (10, 20, 30...). És la manera d'escriure *"cada 10 vegades"* sense un segon comptador.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El LED no s'encén mai | Polaritat del LED invertida, o cablejat a un pin diferent de P1 | Revisa la pota llarga (ànode) i l'[esquema de connexions](../../SA2_esquemes_connexions.md). |
| El LED queda sempre encès | Falta el `write_digital(0)` (s'ha esborrat o mal indentat) | Comprova que cada `sleep()` va seguit de l'estat contrari. |
| El comptador sempre mostra 10 | `comptador = 0` s'ha posat **dins** del `while True:` | Mou la inicialització **abans** del bucle. |

## 🔗 On ho aplicaràs

- **Ara mateix:** el mateix pin P1 torna a la Sessió 2 amb PWM ([`pwm_led_rgb`](../pwm_led_rgb/EXPLICACIO.md)): passaràs d'encès/apagat a intensitats intermèdies.
- **Sessió 4:** aquest mateix codi (o el de `pwm_led_rgb`) és el que faràs servir per validar el cablatge del LED indicador de la **mascota** en muntar-la.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA2](../../../../Reptes/Reptes_SA2.md)**.
