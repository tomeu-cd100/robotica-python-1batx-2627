# Data logging natiu: la placa registra sola (Sessió 2)

**Quan es fa:** Sessió 2 · **Fitxer:** `registre_dades.py` · **Maquinari:** cap de nou, sensors interns (`temperature()`, `display.read_light_level()`)

## 🎯 Per què fem aquesta pràctica

Fins ara, quan volíem "guardar" alguna cosa, ho fèiem amb una **llista** dins del programa (l'historial de comandes de la SA5): es perd en desconnectar la placa. La micro:bit V2 té una capacitat pròpia, el mòdul **`log`**, que desa dades directament a la seva **memòria flash interna**: sobreviuen a l'apagada i es poden llegir després **sense cap cable de xarxa ni servei al núvol**, només connectant la placa per USB a un ordinador.

## 🔮 Abans d'executar: prediu

Si el programa s'executa durant 1 minut amb `INTERVAL_MS = 2000`, quantes files noves esperes trobar al registre en acabar?

## 🧠 El codi, per blocs

### Bloc 1 — Etiquetar les columnes un sol cop

```python
log.set_labels('temp', 'llum')
```

`set_labels()` fixa els noms de columna del registre **abans** de començar a afegir files: és l'equivalent a escriure la capçalera d'una taula.

### Bloc 2 — Una fila nova a cada crida

```python
log.add(temp=temp, llum=llum)
```

Cada crida a `log.add()` desa una **fila** nova amb els valors indicats, associats al nom de columna corresponent. La placa ho fa tota sola: no cal cap `while` que escrigui a un fitxer manualment.

### Bloc 3 — Llegir-ho per USB

Un cop la placa ha registrat dades, connecta-la per USB (com per programar-la) i obre l'explorador de fitxers: dins de la unitat **MICROBIT** apareix un fitxer **`MY_DATA.HTM`**. Obre'l amb qualsevol navegador: mostra una **taula** i un **gràfic** amb totes les files desades, sense instal·lar cap programa addicional.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| `MY_DATA.HTM` no apareix | Cal que el programa hagi cridat `log.add()` almenys un cop i que la placa s'hagi desconnectat/reconnectat per USB |
| Les columnes surten sense nom | `log.set_labels()` no s'ha cridat, o s'ha cridat **després** del primer `log.add()` |
| El registre no creix més | La memòria flash té un límit: en un exercici curt no hi arribaràs, però és bo saber que existeix |

## 🔗 On ho aplicaràs

- **Context real:** estacions meteorològiques escolars, registres de temperatura d'un hivernacle, quaderns de camp digitals: totes fan servir la mateixa idea, desar dades localment i revisar-les després.
- **Simulador:** python.microbit.org **sí** simula el mòdul `log` (es pot descarregar el registre simulat des del propi simulador), però la lectura real per USB només es pot provar amb la placa física.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA6](../../../../Reptes/Reptes_SA6.md)**.
