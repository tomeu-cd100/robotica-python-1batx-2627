# L'estació base: rebre, mostrar i registrar (Sessions 2-3)

**Quan es fa:** Sessions 2-3 (producte) · **Fitxer:** `estacio_base.py` · **Maquinari:** cap component nou (ràdio interna + display); s'executa **temporalment** a la placa d'un company (per torns) o del docent

## 🎯 Per què fem aquesta pràctica

> 🔒 **Regla vinculant (fitxa 17):** aquest programa l'has d'escriure **tu**, encara que s'executi temporalment en una altra placa. La placa és només el banc de proves; el codi, la telemetria rebuda i la interpretació de les dades són sempre la teva evidència pròpia.

`estacio_base.py` és la contrapartida de [`telemetria_radio.py`](../telemetria_radio/EXPLICACIO.md): rep els missatges `"TEL:..."`, els **interpreta**, en mostra un resum al display i en guarda un registre. És el mateix esquema receptor↔emissor de `receptor_vehicle.py`/`comandament.py` (SA5), ara amb un protocol de **dades**, no d'ordres.

## 🔮 Abans d'executar: prediu

Si `analitza()` rep un missatge amb un camp mal escrit (per exemple `"TEL:D23;S:412"`, sense els dos punts després de `D`), què hauria de passar: aturar tot el programa amb un error, o continuar igualment ignorant aquest camp?

## 🧠 El codi, per blocs

### Bloc 1 — Separar el missatge en un diccionari

```python
def analitza(missatge):
    dades = {}
    cos = missatge[len(PREFIX):]
    for camp in cos.split(";"):
        if ":" not in camp:
            continue
        clau, valor = camp.split(":", 1)
        dades[clau] = valor
    return dades
```

Primer es treu el prefix (`"TEL:"`), després es parteix per `;` (un camp per sensor) i cada camp per `:` (clau i valor). El `if ":" not in camp: continue` és una petita defensa: si un camp arriba trencat, es descarta **només aquell camp**, no tot el missatge.

### Bloc 2 — Llista + mitjana simple (objectiu 3 de la fitxa 17)

```python
historic_distancies.append(distancia)
if len(historic_distancies) > MAX_HISTORIC:
    historic_distancies.pop(0)
...
def mitjana(llista):
    return sum(llista) / len(llista) if llista else 0
```

Mateixa idea de `historic_comandes` de `receptor_vehicle.py` (SA5): una llista amb un màxim d'elements (les `MAX_HISTORIC` últimes lectures), a la qual es treu el més antic quan es passa de mida. La mitjana és tan simple com `sum()/len()`, amb una comprovació perquè no peti si la llista encara és buida.

### Bloc 3 — Registre persistent amb `log` (res de núvol)

```python
log.set_labels('dist', 'seguidor', 'estat', 'temp', 'humitat', 'orientacio')
...
log.add(dist=..., seguidor=..., estat=..., temp=..., humitat=..., orientacio=...)
```

Mateix mòdul `log` natiu de la V2 que `registre_dades.py` (SA6): cada lectura queda desada a la memòria flash de la **pròpia placa**, sense cap núvol ni connexió a internet. Es llegeix connectant la placa per USB i obrint el fitxer `MY_DATA.HTM` de la unitat `MICROBIT`.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| No arriba cap missatge | `GRUP` diferent del de `telemetria_radio.py`, o `radio.on()` no cridat a alguna de les dues plaques |
| El display mostra sempre `Image.CONFUSED` | El camp `"E"` no arriba amb un dels tres noms exactes (`SEGUIR`/`ESQUIVAR`/`RECUPERAR`): revisa el `PREFIX` i el format del missatge a totes dues bandes |
| `log.add()` dona error | Falta cridar `log.set_labels()` **abans**, un únic cop, amb els mateixos noms de columna que fas servir a `log.add()` |

## 🔗 On ho aplicaràs

- **Ara mateix:** és el **producte de la SA**, junt amb `telemetria_radio.py`.
- **Sessió 3:** les dades registrades (`MY_DATA.HTM`) són la base de la reflexió sobre ètica de dades i IA de la fitxa ampliada.
- **Simulador:** la **ràdio i el mòdul `log`** SÍ es simulen a python.microbit.org (2 instàncies per assajar l'enviament/recepció).

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA8](../../../../Reptes/Reptes_SA8.md)**.
