# SA3 · Fitxa ampliada (aprofundiment) — Entrades: el robot percep

> 📄 **Versió ampliada**: conté totes les activitats i les rutines d'aprofundiment (pensament computacional, diana, exit ticket, ODS…). La fitxa que fa **tot l'alumnat** és la base: **[SA3_fitxa_alumnat.md](SA3_fitxa_alumnat.md)**.

> 🧑‍🎓 **Quan toca obrir-la?** És **opcional**: quan portis la **fitxa base al dia** i vulguis més (ampliacions de codi, pensament computacional, ODS). Algunes rutines (exit ticket) les activarà el **docent** a l'aula quan toqui.

> 🗺️ **Quan s'usa cada apartat:** les **Activitats 1-3** segueixen les mateixes sessions que la fitxa base (aquí amb les ampliacions de codi) · **Si t'encalles** i **Pensament computacional**: durant el treball · **Vols més?**: amb el nucli al dia · **Exit ticket**: els últims 2' de la Sessió 3 · **Diana** i **Quadern tècnic**: en tancar la SA · **Context real i ODS**: quan el docent l'activi.

**Nom:** ______________________  **Data:** __________

> En aquesta unitat faràs que la micro:bit percebi el món amb sensors digitals i analògics, i acabaràs programant i tancant la **mascota reactiva** (Projecte T1). Tot el treball és **individual**.

---

## Activitat 1 · Entrades digitals i condicionals

Munta el polsador extern ([`SA3_esquemes_connexions.md`](SA3_esquemes_connexions.md)) i escriu al REPL un comptador amb `if/elif/else`.

**0. PREDIU:** si premis el polsador ràpid diverses vegades seguides, el comptador pujarà exactament el mateix nombre de cops? Per què (o per què no)?

___________________________________________________________________

1. **Executa i comprova** la teva predicció al REPL.
2. **Afegeix un antirebot** (compara `running_time()` amb la darrera detecció) i torna-ho a provar.

**+ Repte:** fes que el polsador alterni entre **dos comportaments** (per exemple, comptar cap amunt / cap avall) segons quantes vegades s'ha premut (parell/senar).

---

## Activitat 2 · Entrades analògiques: llum i temperatura

Munta el sensor de llum i de temperatura ([`SA3_esquemes_connexions.md`](SA3_esquemes_connexions.md)). Parteix de [`nivell_llum.py`](codi/nivell_llum/nivell_llum.py) i [`termometre.py`](codi/termometre/termometre.py).

**Pregunta:** per què MicroPython no té una funció `map()` integrada com Arduino, i com la substituïm?

___________________________________________________________________

**El teu llindar propi:** `LLINDAR_FOSCOR` = ______ , `FRED` = ______ , `CALOR` = ______ → mesurats amb el REPL a: ______________________

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió).** Banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md#sa3--mini-check-inici-de-la-sessió-2).

**+ Ampliació (opcional):** afegeix un **tercer nivell** a `nivell_llum.py` (per exemple, "penombra" entre "fosc" i "clar") amb un segon llindar.

**+ Ampliació amb maquinari real (opcional, qui va molt sobrat):** prova [`alarma_ultrasons.py`](codi/alarma_ultrasons/alarma_ultrasons.py) (HC-SR04, Kit 2): mesura de distància per **temps de vol**, no per lectura directa. **No es pot simular** a python.microbit.org: cal maquinari real.

---

## Activitat 3 · Repte «mascota reactiva» (producte — tanca la mascota T1)

Cablega la mascota amb el cablatge **exacte** del [dossier del Projecte T1](../00_General/00_Projecte_T1_Mascota.md) i programa **almenys 2 reaccions** sensor→resposta.

**Codi (o descripció de com l'has fet):**

```python

```

**Mini-defensa:** anota aquí la **decisió** que explicaràs (per exemple, per què aquest llindar o aquest ordre de prioritat entre estímuls):

___________________________________________________________________

---

## Si t'encalles

1. **Pista 1:** repassa l'[esquema de connexions](SA3_esquemes_connexions.md) — molts errors de "no reacciona" són cablatge o pin sense ADC, no codi.
2. **Pista 2:** mesura amb el REPL el valor real del sensor abans de triar un llindar.
3. **Pista 3:** aplica **DEPURA** i, si cal, demana ajuda **explicant què ja has provat**.

> **Rutina DEPURA:** **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara i torna a provar · **A**punta-ho al quadern.

## Vols més?

- **Reptes ⭐⭐/⭐⭐⭐:** tria'n un a [`Reptes/Reptes_SA3.md`](../../Reptes/Reptes_SA3.md) i amplia el teu producte (el ⭐ ja és nucli obligatori, fet a la fitxa base).
- **Simulador:** el de [python.microbit.org](https://python.microbit.org) **no** reprodueix cap sensor extern (vegeu [`SA3_esquemes_connexions.md`](SA3_esquemes_connexions.md) §Simulació); només els sensors interns (llum, temperatura, so, acceleròmetre) i els botons.

---

## Pensament computacional d'aquesta SA

Avui has practicat la **DESCOMPOSICIÓ**: separar "llegir el sensor" de "decidir què fer amb el valor" i de "executar la reacció" (com `llegeix_sensors()` i `canvia_emocio()` a `mascota_reactiva.py`). On més has vist "trencar un problema gran en peces petites"? ______________________

## Diana d'autoavaluació

Situa't (0-10):

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Llegeixo entrades digitals amb condicionals | ☐ | ☐ | ☐ | ☐ |
| Llegeixo i interpreto entrades analògiques | ☐ | ☐ | ☐ | ☐ |
| Munto sensors al Micro:shield amb seguretat | ☐ | ☐ | ☐ | ☐ |

## Exit ticket (abans de marxar, Sessió 3)

1. Una cosa que he après avui: ______________________
2. Una cosa que encara no tinc clara: ______________________
3. On ho faria servir al món real: ______________________

## Context real i ODS

Sensors de presència d'enllumenat automàtic, termòstats domèstics, aparcaments amb sensors d'ultrasons. **ODS 3** (salut i benestar): sensors de temperatura/humitat en cures de salut i confort. **ODS 11** (ciutats i comunitats sostenibles): sensors de presència i llum que estalvien energia encenent només quan cal. Escriu un exemple propi: ______________________

---

## Quadern tècnic (entrada de la SA3)

> El quadern tècnic és el teu **diari de bord** de tot el curs. Segueix el **mètode de projecte**: *analitzar → dissenyar → programar/prototipar → provar → millorar.*

- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com ho vaig solucionar i què vaig millorar): ___________________________________________________
- **Quin error he tingut i com l'he resolt:** ___________________________
- **Mascota (tancament del Projecte T1):** reaccions finals, llindars triats i per què.
- **Reflexió ètica** (privacitat de sensors): un sensor de presència o de so també pot "escoltar"/"vigilar" sense voler-ho — un exemple d'ús responsable d'aquests sensors al món real:
  - ______________________________________________________
