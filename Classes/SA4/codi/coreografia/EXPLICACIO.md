# Coreografia: funcions amb arguments (Sessió 1-2)

**Quan es fa:** Sessió 1-2 · **Fitxer:** `coreografia.py` · **Maquinari:** [esquemes de connexions](../../SA4_esquemes_connexions.md) — servo de la mascota (**P0**) i brunzidor (**P2**, com a la SA2/SA3)

> ✋ Aquesta pàgina explica el codi **model**. Parteix de [`funcions_moviments.py`](../funcions_moviments/EXPLICACIO.md): si encara no l'has entès, torna-hi abans.

## 🎯 Per què fem aquesta pràctica

Un cop saps definir una funció amb un paràmetre, el pas següent és **combinar-ne diverses** per construir alguna cosa més gran: una coreografia. La idea clau d'avui és que la funció principal (`ball_complet()`) **no conté cap detall tècnic** (angles, pins, freqüències): només **crida**, en ordre, funcions ja fetes. Canviar l'ordre de les crides canvia la coreografia sencera sense tocar cap càlcul.

## 🔮 Abans d'executar: prediu

`salut_musical(vegades)` crida `gest()` i `nota_curta()` dins d'un `for`. Si canvies `salut_musical(2)` per `salut_musical(1)` dins de `ball_complet()`, què canviarà: el nombre de notes que sonen, l'angle del servo, o totes dues coses?

## 🧠 El codi, per blocs

### Bloc 1 — Una funció amb TRES paràmetres: `gest(angle_inici, angle_final, pas)`

```python
def gest(angle_inici, angle_final, pas):
    for angle in range(angle_inici, angle_final + pas, pas):
        mou_servo(angle)
        sleep(60)
```

Una funció pot tenir **més d'un paràmetre**. Aquí, `gest()` és un sol moviment reutilitzable: canviant `angle_inici`, `angle_final` i `pas` (positiu o negatiu) obtens moviments molt diferents sense escriure cap `for` nou.

### Bloc 2 — So amb `pin=` explícit: `nota_curta(freq)`

```python
def nota_curta(freq):
    music.pitch(freq, 150, pin=pin2)
```

Recorda la convenció del curs: quan el so surt pel **brunzidor extern** (P2), `music.pitch`/`music.play` sempre porten `pin=` explícit.

### Bloc 3 — Combinar funcions dins d'una altra funció: `salut_musical(vegades)`

```python
def salut_musical(vegades):
    for i in range(vegades):
        gest(90, 20, -10)
        nota_curta(880)
        gest(20, 90, 10)
        nota_curta(660)
```

`salut_musical()` no calcula res per si sola: **encadena** crides a `gest()` i `nota_curta()` amb un paràmetre propi (`vegades`) que controla quantes vegades es repeteix tot el bloc.

### Bloc 4 — La coreografia sencera: `ball_complet()`

```python
def ball_complet():
    display.show(Image.HAPPY)
    salut_musical(2)
    gest(90, 180, 15)
    nota_curta(523)
    gest(180, 0, -15)
    nota_curta(392)
    mou_servo(90)
    display.show(Image.HEART)
```

Llegeix `ball_complet()` com una **recepta**: cada línia és un pas ja resolt per una altra funció. Si volguessis una coreografia diferent, només caldria canviar **l'ordre i els arguments** d'aquestes crides, no reescriure cap moviment des de zero.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El so no sona pel brunzidor extern | Falta `pin=pin2` a `music.pitch`/`music.play` (surt per l'altaveu intern en lloc del brunzidor) |
| El servo no acaba al mateix punt on va començar | `gest()` amb un `pas` que no arriba exactament a `angle_final` (el `range` no inclou sempre l'últim valor si el pas no hi encaixa) |
| El servo no es mou (però no hi ha error) | El simulador **no** simula el servo; el so i el display sí que es poden provar |

## 🔗 On ho aplicaràs

- **Ara mateix:** exercici de consolidació de funcions amb paràmetres (Sessió 1-2), abans de passar als motoreductors.
- **Sessió 2:** [`velocitat_pwm.py`](../velocitat_pwm/EXPLICACIO.md) aplica exactament la mateixa idea (funcions amb paràmetres) al moviment del vehicle.
- **Simulador:** el so i el display es poden provar a python.microbit.org; el servo no.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA4](../../../../Reptes/Reptes_SA4.md)**.
