# Semàfor amb relé (repte / producte de la SA2)

**Quan es fa:** Sessió 3 (repte, producte de la SA) · **Fitxer:** `semafor_rele.py` · **Maquinari:** [esquemes de connexions](../../SA2_esquemes_connexions.md) — LED verd P1, ambre P8, vermell P12, brunzidor P2, relé P13 (Kit 1 + Kit 3)

> ✋ **Aquesta pàgina mostra la SOLUCIÓ del repte "semàfor o llum d'ambient".** És el **producte de la SA2**: intenta-ho pel teu compte a l'Activitat 3 de la [fitxa](../../SA2_fitxa_alumnat.md) abans de mirar-la sencera. Si t'encalles, tens un esquelet a la secció «Si t'encalles» de més avall.

## 🎯 Per què fem aquesta pràctica

És el moment d'**integrar** tot el que has après a la SA2: sortides digitals (LED), PWM (opcional, si vols un LED que s'apaga suau), so (`music`) i, ara, un component nou: el **relé**, que et permet commutar un circuit **extern** a la micro:bit (per exemple, un llum de veritat) sense connectar-lo mai directament als pins de la placa.

## 🔮 Abans d'executar: prediu

Mira el codi complet (a baix) **sense executar-lo**. Quant de temps estarà en cada fase? Quan sonarà el brunzidor? Quan es tancarà el relé? Anota-ho i comprova-ho.

## 🧠 El codi, per blocs

### Bloc 1 — Temps en variables, no repetits pel codi

```python
TEMPS_VERD = 3000
TEMPS_AMBRE = 1000
TEMPS_VERMELL = 3000
```

Si els temps estan en **variables al principi**, canviar la durada del semàfor és canviar **un sol número**, no buscar-lo repetit per tot el programa.

### Bloc 2 — Una funció per no repetir codi: `tot_apagat()`

```python
def tot_apagat():
    pin1.write_digital(0)
    pin8.write_digital(0)
    pin12.write_digital(0)
```

Abans de cada fase, apaguem els tres LED amb una sola crida. Sense aquesta funció, hauries de repetir les tres línies **cada vegada** que canvies de fase.

### Bloc 3 — El relé: commutar un circuit extern

```python
pin13.write_digital(1)   # el rele tanca el circuit extern
sleep(TEMPS_VERMELL)
pin13.write_digital(0)   # el rele torna a obrir el circuit extern
```

El relé és un **interruptor controlat per software**: `write_digital(1)`/`write_digital(0)` mouen la seva bobina (costat de baixa tensió, 3,3 V), que obre o tanca un contacte mecànic al **costat del circuit extern** (que porta la seva pròpia alimentació). Mai es connecta el circuit extern directament a un pin de la micro:bit.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| Dos LED encesos alhora | Falta cridar `tot_apagat()` abans d'encendre'n un de nou |
| El semàfor no es repeteix igual cada volta | Els temps s'han escrit a mà en diversos llocs del codi: torna a extreure'ls a les variables `TEMPS_...` |
| El relé fa "clic" però el circuit extern no s'engega | El relé **no** dona corrent al circuit extern, només el commuta: cal que aquest tingui la seva **pròpia** alimentació |

## 🧗 Si t'encalles: l'esquelet del semàfor

Si estàs en blanc, parteix d'aquest esquelet: les tres fases i els `sleep()` ja hi són; tu omples els `# TODO` amb l'estat correcte de cada LED.

<details markdown="1">
<summary>Desplega l'esquelet (còpia'l a un programa nou)</summary>

```python
# SA2 - semafor_rele  (BASTIDA / esquelet per a l'alumnat)
#
# QUE JA ESTA FET (no ho toquis):
#   - Les variables de temps i l'estructura while True: amb les 3 fases.
#
# QUE HAS DE FER TU:
#   - OMPLE cada fase amb els write_digital() del LED que toca (i, si vols,
#     el to del brunzidor a l'ambre i el rele al vermell).
#
# EINES QUE POTS USAR (nomes conceptes de la SA2):
#   - pin1.write_digital(1/0)   -> LED verd
#   - pin8.write_digital(1/0)   -> LED ambre
#   - pin12.write_digital(1/0)  -> LED vermell
#   - pin13.write_digital(1/0)  -> rele (circuit extern)
#   - music.pitch(freq, ms, pin=pin2)  -> to del brunzidor

from microbit import *
import music

TEMPS_VERD = 3000
TEMPS_AMBRE = 1000
TEMPS_VERMELL = 3000

while True:
    # TODO 1 (fase verda): encen NOMES el LED verd i espera TEMPS_VERD
    pass

    # TODO 2 (fase ambre): encen NOMES el LED ambre, fes sonar un to curt
    #         i espera TEMPS_AMBRE
    pass

    # TODO 3 (fase vermella): encen NOMES el LED vermell, tanca el rele,
    #         espera TEMPS_VERMELL i torna a obrir el rele
    pass
```

</details>

## 🔗 On ho aplicaràs

- **Ara mateix:** és el **producte de la SA2**: es defensa amb una mini-defensa d'1' (R4·DO).
- **Sessió 4:** el LED/RGB i el so d'aquest repte reapareixen (sense el relé) dins la **mascota**.
- **Tot el curs:** el patró "estat → funció que l'aplica" (`tot_apagat()` + una fase per estat) el retrobaràs a la SA6 (sistemes de control).

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA2](../../../../Reptes/Reptes_SA2.md)**.
