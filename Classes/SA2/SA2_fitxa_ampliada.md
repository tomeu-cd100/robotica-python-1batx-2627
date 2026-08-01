# SA2 · Fitxa ampliada (aprofundiment) — Sortides: el robot actua

> 📄 **Versió ampliada**: conté totes les activitats i les rutines d'aprofundiment (pensament computacional, diana, exit ticket, ODS…). La fitxa que fa **tot l'alumnat** és la base: **[SA2_fitxa_alumnat.md](SA2_fitxa_alumnat.md)**.

> 🧑‍🎓 **Quan toca obrir-la?** És **opcional**: quan portis la **fitxa base al dia** i vulguis més (ampliacions de codi, pensament computacional, ODS). Algunes rutines (exit ticket) les activarà el **docent** a l'aula quan toqui.

> 🗺️ **Quan s'usa cada apartat:** les **Activitats 1-4** segueixen les mateixes sessions que la fitxa base (aquí amb les ampliacions de codi) · **Si t'encalles** i **Pensament computacional**: durant el treball · **Vols més?**: amb el nucli al dia · **Exit ticket**: els últims 2' de la Sessió 3 · **Diana** i **Quadern tècnic**: en tancar la SA · **Context real i ODS**: quan el docent l'activi.

**Nom:** ______________________  **Data:** __________

> En aquesta unitat connectaràs el Micro:shield i faràs que la micro:bit actuï sobre el món exterior: LED, LED RGB, brunzidor i relé. Tancaràs muntant la mascota. Tot el treball és **individual**.

---

## Activitat 1 · Sortida digital amb bucles

Munta el LED extern al pin **P1** ([`SA2_esquemes_connexions.md`](SA2_esquemes_connexions.md)) i parteix de [`led_parpelleig.py`](codi/led_parpelleig/led_parpelleig.py).

**0. PREDIU:** quant de temps estarà encès el LED cada cicle? Cada quants parpellejos apareix un número al display?

___________________________________________________________________

1. **Executa i comprova** la teva predicció.
2. **Modifica** els temps d'encès/apagat i el `% 10` per un altre múltiple.

**+ Repte:** afegeix un **segon LED** en un pin lliure i fes que parpellegin **alternats** (mentre un s'encén, l'altre s'apaga).

---

## Activitat 2 · Sortides PWM i so

Munta el LED RGB (P8/P12/P16) i el brunzidor (P2). Parteix de [`pwm_led_rgb.py`](codi/pwm_led_rgb/pwm_led_rgb.py) i [`musica_altaveu.py`](codi/musica_altaveu/musica_altaveu.py).

**Pregunta:** per què `write_analog()` fa servir l'escala 0-1023 i no 0-255 ni 0-1?

___________________________________________________________________

**El teu color propi:** vermell ______ verd ______ blau ______ → nom del color: ______________________

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió).** Banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md#sa2--mini-check-inici-de-la-sessió-2).

**+ Ampliació (opcional):** fes que el LED RGB canviï de color **seguint el ritme** de la melodia de `musica_altaveu.py` (un color diferent per nota).

**+ Ampliació amb maquinari real (opcional, qui va molt sobrat):** el **Kit 2** inclou una **tira LED adreçable WS2812B** (NeoPixel, ~30 LED; vegeu [`09c_Inventari_kits_disponibles.md`](../../Programació%20didàctica/09c_Inventari_kits_disponibles.md)). Amb el mòdul `neopixel` de MicroPython pots encendre-hi patrons de colors propis (per exemple, un "arc de Sant Martí" o un indicador de nivell). **No es pot simular** a python.microbit.org: cal maquinari real. No forma part del nucli de la SA2; reapareix com a opció al repte final (SA9).

---

## Activitat 3 · Repte «semàfor o llum d'ambient» (producte)

Munta el semàfor complet i escriu el programa: 3 fases (verd/ambre/vermell) amb temps en variables, avís sonor a l'ambre, relé commutant un circuit extern al vermell.

**Codi (o descripció de com l'has fet):**

```python

```

**Mini-defensa (1'):** anota aquí la **decisió** que explicaràs (per exemple, per què aquest ordre de colors o aquests temps):

___________________________________________________________________

---

## Activitat 4 · Muntatge de la mascota

Segueix [`00_Projecte_T1_Mascota.md`](../00_General/00_Projecte_T1_Mascota.md). Descriu **un problema** que hagis tingut en el muntatge i com l'has resolt:

___________________________________________________________________

---

## Si t'encalles

1. **Pista 1:** repassa l'[esquema de connexions](SA2_esquemes_connexions.md) — molts errors de "no funciona" són cablatge, no codi.
2. **Pista 2:** mesura amb el REPL el valor real que envies al pin abans de sospitar del component.
3. **Pista 3:** aplica **DEPURA** i, si cal, demana ajuda **explicant què ja has provat**.

> **Rutina DEPURA:** **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara i torna a provar · **A**punta-ho al quadern.

## Vols més?

- **Reptes ⭐⭐/⭐⭐⭐:** tria'n un a [`Reptes/Reptes_SA2.md`](../../Reptes/Reptes_SA2.md) i amplia el teu producte (el ⭐ ja és nucli obligatori, fet a la fitxa base).
- **Simulador:** el de [python.microbit.org](https://python.microbit.org) **no** reprodueix components externs (vegeu [`SA2_esquemes_connexions.md`](SA2_esquemes_connexions.md) §Simulació); serveix només per validar la lògica.

---

## Pensament computacional d'aquesta SA

Avui has practicat l'**ABSTRACCIÓ**: `write_analog(700)` t'amaga tot el parpelleig ràpid que fa la placa per darrere; `music.play([...])` t'amaga la generació de cada ona sonora. On més has vist "amagar detalls darrere d'una ordre senzilla"? ______________________

## Diana d'autoavaluació

Situa't (0-10):

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Controlo sortides digitals amb bucles | ☐ | ☐ | ☐ | ☐ |
| Controlo sortides PWM (LED, LED RGB, so) | ☐ | ☐ | ☐ | ☐ |
| Munto components al Micro:shield amb seguretat | ☐ | ☐ | ☐ | ☐ |

## Exit ticket (abans de marxar, Sessió 3)

1. Una cosa que he après avui: ______________________
2. Una cosa que encara no tinc clara: ______________________
3. On ho faria servir al món real: ______________________

## Context real i ODS

Semàfors, enllumenat intel·ligent i relés d'electrodomèstics fan servir exactament aquestes idees. **ODS 7** (energia assequible i no contaminant): el PWM permet **regular** la intensitat en lloc de gastar sempre a plena potència. **ODS 11** (ciutats i comunitats sostenibles): semàfors i enllumenat intel·ligent. Escriu un exemple propi: ______________________

---

## Quadern tècnic (entrada de la SA2)

> El quadern tècnic és el teu **diari de bord** de tot el curs. Segueix el **mètode de projecte**: *analitzar → dissenyar → programar/prototipar → provar → millorar.*

- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com ho vaig solucionar i què vaig millorar): ___________________________________________________
- **Quin error he tingut i com l'he resolt:** ___________________________
- **Mascota (S4):** com ha anat el muntatge i què falta per a la SA3.
- **Reflexió ètica** (energia i ODS): un exemple d'estalvi energètic amb PWM al món real:
  - ______________________________________________________
