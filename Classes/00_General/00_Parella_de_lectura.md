# Parella de lectura (5') — coavaluació de lectura de codi

> **Per a qui és?** Docent (guió de sessió) i alumnat (checklist i regla del joc).

## Què és i què NO és

- **És** feedback formatiu de 5 minuts entre dos companys, just abans de lliurar el repte de la sessió: A llegeix el codi de B (i a l'inrevés) i li diu **una** cosa a millorar.
- **NO és** treball en grup ni programació per parelles: **cada alumne llegeix, no toca ni edita** el codi de l'altre. El producte que es lliura és sempre individual i propi.
- **NO puntua.** No hi ha nota ni registre a cap rúbrica: és una pausa de qualitat abans de lliurar, com rellegir un text abans d'entregar-lo.
- Es fa **un cop per SA**, a la sessió del producte/repte, quan el codi ja funciona (o gairebé): llegir codi trencat no ensenya res.

## Guió de 5 minuts

| Temps | Qui | Què fa |
|---|---|---|
| 0'-30" | Docent | Diu «Parella de lectura» i empareixen (el de la taula del costat, o qui el docent assigni). Cadascú es queda **al seu propi ordinador**. |
| 30"-2' | A | Llegeix el codi de B a la pantalla de B (B no parla, no explica, no ajuda: el codi ha de parlar sol). Marca mentalment els 3 ítems de la checklist. |
| 2'-2'30" | A → B | A diu a B **una** cosa concreta a millorar (no una llista sencera: una). |
| 2'30"-4' | B | Llegeix el codi d'A de la mateixa manera. |
| 4'-4'30" | B → A | B diu a A **una** cosa concreta a millorar. |
| 4'30"-5' | Tots dos | Cadascú torna al seu codi: aplica (o no) el suggeriment abans de lliurar. La decisió final és seva. |

## Checklist de 3 ítems

Quan llegeixis el codi d'un company, mira NOMÉS aquests 3 punts (en aquest ordre):

1. **Noms de variables que expliquen què contenen.** Un nom com `t` o `x` no diu res; `temps_espera` o `distancia_cm` sí.
2. **Almenys un comentari útil que digui PER QUÈ, no QUÈ.** El codi ja diu què fa; un bon comentari explica la raó d'una decisió que no és òbvia només mirant el codi.
3. **Cap «número màgic» sense nom.** Un número solt al mig del codi (`if dist < 15:`) no diu d'on surt; amb un nom (`LLINDAR_CM = 15`) o un comentari que digui per què és 15, sí.

## Exemples

### Ítem 1 — noms de variables

Dolent (els noms no diuen res):

```python
x = read_analog(P1)
y = mapa(x, 0, 1023, 0, 100)
if y > 50:
    write_digital(P8, 1)
```

Bo (els noms expliquen què contenen):

```python
lectura_sensor = read_analog(P1)
percentatge_llum = mapa(lectura_sensor, 0, 1023, 0, 100)
if percentatge_llum > 50:
    write_digital(P8, 1)
```

### Ítem 2 — un comentari que digui PER QUE, no QUE

Dolent (el comentari repeteix el codi, no aporta res):

```python
# suma 1 a comptador
comptador = comptador + 1
```

Bo (el comentari explica la rao, no repeteix la linia):

```python
# comptem els avisos per activar l'alarma nomes a partir del tercer,
# per evitar falses alarmes amb un sol pas puntual
comptador = comptador + 1
```

### Ítem 3 — cap número màgic sense nom

Dolent (d'on surt el 15? per que 15 i no 10?):

```python
if distancia < 15:
    aturar()
```

Bo (el nom explica el que representa el numero):

```python
LLINDAR_SEGURETAT_CM = 15
if distancia < LLINDAR_SEGURETAT_CM:
    aturar()
```

## Regla clara

**El codi de cadascú és seu.** La parella de lectura és una segona mirada abans de lliurar, no una correcció d'un altre alumne ni una feina compartida. Qui rep el suggeriment decideix si l'aplica. El docent no recull ni qualifica què s'ha dit: només vetlla que les parelles llegeixin (no toquin) i que el comentari sigui concret i respectuós.
