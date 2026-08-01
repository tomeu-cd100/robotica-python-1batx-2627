# Plantilla del projecte: percep → decideix → actua (Sessió 2)

**Quan es fa:** Sessió 2 (Prototipar) · **Fitxer:** `plantilla_projecte.py` · **Maquinari:** el teu rover (SA7-SA8) + el maquinari nou del teu repte (vegeu [`SA9_reptes_proposats.md`](../../SA9_reptes_proposats.md) i el mapa de pins)

## 🎯 Per què fem aquesta pràctica

Durant tot el curs cada programa ha seguit la mateixa arquitectura: **llegir** (sensors), **decidir** (una FSM amb una única variable d'estat, com `maquina_estats_semafor.py` de SA6 o `comportaments.py` de SA8) i **actuar** (motors, display, ràdio). Aquesta plantilla et dona aquesta estructura ja parada perquè no comencis el teu projecte final des d'un full en blanc: només has d'omplir els blocs `TODO` amb el codi del **teu** repte.

## 🔮 Abans d'executar: prediu

Si copies aquí la funció `mesura_distancia()` de `rover_missions.py` (SA7) sense canviar-ne res, què esperes que passi si l'HC-SR04 no és connectat als pins que la plantilla dona per fets?

## 🧠 El codi, per blocs

### Bloc 1 — Pins i constants (TODO)

```python
POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)
INTERVAL_MOSTREIG_MS = 500
```

El polsador STOP (`P12`, pull-up) **ja hi és**, perquè el patró de seguretat és el mateix de tot el curs des de SA6. La resta de pins del teu repte (rele, sensor d'humitat, PIR...) els has d'afegir tu, seguint el mapa de pins.

### Bloc 2 — Una única variable d'estat

```python
ESTAT_A, ESTAT_B = range(2)
estat = ESTAT_A
```

Substitueix `ESTAT_A`/`ESTAT_B` pels noms reals dels estats del teu repte (per exemple, `ESPERA`/`REGANT` en el repte de reg). Com sempre, **un únic** estat a la vegada.

### Bloc 3 — percep / decideix / actua

```python
def percep():
    return {}

def decideix(dades):
    global estat
    if estat == ESTAT_A:
        pass
    elif estat == ESTAT_B:
        pass

def actua():
    pass
```

Aquestes tres funcions són el **cor** del teu projecte: `percep()` només llegeix, `decideix()` només canvia `estat`, `actua()` només mou/activa. Mantenir-les separades fa que el codi sigui més fàcil de depurar (com ja vas veure amb `comportaments.py`, SA8): si el rover "actua malament", saps si el problema és de lectura, de decisió o d'actuació.

### Bloc 4 — Bucle principal amb prioritat de seguretat

```python
if polsador_premut():
    display.show(Image.NO)
    sleep(20)
    continue
```

La comprovació del polsador STOP és **sempre la primera** de cada volta, exactament com a totes les SA des de SA6: cap estat de la teva FSM no la pot saltar.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| El programa no fa res (només mostra la `X` del polsador) | El polsador STOP està sempre premut: revisa el pull-up i el cablatge de P12 |
| `decideix()` no canvia mai d'estat | Encara tens `pass` als dos `TODO`: substitueix-los per condicions reals sobre `dades` |
| El programa peta amb `KeyError` al mostrar l'estat | Vas afegir un estat nou a la FSM però no l'has afegit a `NOMS_ESTAT` |

## 🔗 On ho aplicaràs

- **Ara mateix:** és el punt de partida del teu prototip mínim viable (S2).
- **Sessions 3-4:** hi vas afegint el codi real del teu repte, provant i iterant, fins al producte final documentat al [dossier tècnic](../../SA9_dossier_plantilla.md).

> ⭐ **Tria el teu repte:** [Banc de reptes de la SA9](../../SA9_reptes_proposats.md).
