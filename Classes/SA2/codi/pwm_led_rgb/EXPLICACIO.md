# PWM: intensitat i colors combinats

**Quan es fa:** Sessió 2 (modelatge) · **Fitxer:** `pwm_led_rgb.py` · **Maquinari:** [esquemes de connexions](../../SA2_esquemes_connexions.md) — LED a P1 (respiració) i LED RGB a P8/P12/P16 (Kit 1)

## 🎯 Per què fem aquesta pràctica

A `led_parpelleig` només tenies dos estats: encès o apagat. Amb **PWM** (`write_analog`) pots demanar **qualsevol intensitat intermèdia**: un LED que "respira" en lloc de parpellejar, o un LED RGB que combina tres colors purs per fer-ne qualsevol altre. És la mateixa idea que fas servir per regular el volum d'un altaveu o la velocitat d'un motor més endavant al curs.

## 🔮 Abans d'executar: prediu

Mira la funció `respira()` **sense executar-la**. Si `valor` puja de 0 a 1023 de 32 en 32, aproximadament quants passos calen per arribar dalt de tot? I la funció `mostra_color(600, 0, 600)`, quin color creus que dona? Anota-ho a l'Activitat 2 de la [fitxa](../../SA2_fitxa_alumnat.md).

## 🧠 El codi, per blocs

### Bloc 1 — PWM: `write_analog(0-1023)`

```python
pin1.write_analog(700)
```

`write_analog(...)` no és realment "analògic de veritat": la placa **parpelleja el pin molt ràpid** (PWM, *pulse-width modulation*) i el nostre ull ho veu com una intensitat intermèdia. L'escala va de **0** (apagat) a **1023** (intensitat màxima) — **no** de 0 a 255 ni de 0 a 1.

### Bloc 2 — El mecanisme del `for`: recórrer una seqüència de números amb `range`

```python
for valor in range(0, 1024, 32):
    pin.write_analog(valor)
    sleep(10)
```

Un `for` **repeteix** el seu cos un cop per cada element d'una seqüència, guardant l'element actual en una variable (aquí, `valor`) que pots fer servir dins del cos. `range(...)` és la manera més habitual de generar aquesta seqüència de números, i té **tres formes**:

| Forma | Genera | Exemple |
|---|---|---|
| `range(n)` | de `0` a `n-1` | `range(5)` → 0, 1, 2, 3, 4 |
| `range(inici, final)` | de `inici` a `final-1` | `range(2, 6)` → 2, 3, 4, 5 |
| `range(inici, final, pas)` | de `inici` a `final-1`, saltant de `pas` en `pas` | `range(0, 1024, 32)` → 0, 32, 64... fins a 1023 |

Fixa't que el **`final` mai s'inclou** (per això `range(0, 1024, 32)` arriba fins a 1023, no fins a 1024). Una **traça** de les primeres voltes de `for valor in range(0, 1024, 32):` t'ajuda a veure-ho pas a pas:

| Volta | `valor` | Què fa el cos |
|---|---|---|
| 1a | 0 | `pin.write_analog(0)` (apagat), `sleep(10)` |
| 2a | 32 | `pin.write_analog(32)`, `sleep(10)` |
| 3a | 64 | `pin.write_analog(64)`, `sleep(10)` |
| ... | ... | ... fins que `valor` supera 1023: el `for` s'atura sol |

Combinat amb un `sleep(10)` curt, aquesta rampa de valors fa que l'ull vegi una transició **suau** de foscor a claror, en lloc d'un salt brusc.

### Bloc 3 — Barrejar colors: tres canals PWM alhora

```python
def mostra_color(vermell, verd, blau):
    pin8.write_analog(vermell)
    pin12.write_analog(verd)
    pin16.write_analog(blau)
```

Un LED RGB és, per dins, **tres LED** (vermell, verd, blau) amb un pin de control cadascun. Encenent-los a intensitats diferents, l'ull els barreja: `(1023, 0, 0)` és vermell pur, `(600, 0, 600)` és un lila (vermell + blau a mitges), `(0, 0, 0)` l'apaga del tot.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El LED no canvia mai d'intensitat, només encès/apagat | S'ha fet servir `write_digital` en lloc de `write_analog` |
| El LED RGB només mostra un color | Falta escriure als **tres** canals; els que no s'escriuen mantenen l'últim valor | Assegura't que `mostra_color()` sempre passa els tres nombres. |
| `write_analog(255)` sembla molt fluix | 255 és **un quart** de l'escala real (0-1023), no el màxim | Recorda: el màxim de `write_analog` és **1023**. |

## 🔗 On ho aplicaràs

- **Ara mateix:** [`musica_altaveu`](../musica_altaveu/EXPLICACIO.md), amb la mateixa sessió, on el so segueix la mateixa idea de "senyal continu" aplicada al so.
- **Sessió 3 (repte):** [`semafor_rele`](../semafor_rele/EXPLICACIO.md) combina sortides digitals i PWM en un sol sistema.
- **Sessió 4:** aquest codi valida el LED/LED RGB de la **mascota** durant el muntatge.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA2](../../../../Reptes/Reptes_SA2.md)**.
