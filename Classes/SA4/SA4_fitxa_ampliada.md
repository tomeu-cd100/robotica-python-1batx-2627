# SA4 · Fitxa ampliada (aprofundiment) — Funcions i moviment

> 📄 **Versió ampliada**: conté totes les activitats i les rutines d'aprofundiment (pensament computacional, diana, exit ticket, ODS…). La fitxa que fa **tot l'alumnat** és la base: **[SA4_fitxa_alumnat.md](SA4_fitxa_alumnat.md)**.

> 🧑‍🎓 **Quan toca obrir-la?** És **opcional**: quan portis la **fitxa base al dia** i vulguis més (ampliacions de codi, pensament computacional, ODS). Algunes rutines (exit ticket) les activarà el **docent** a l'aula quan toqui.

> 🗺️ **Quan s'usa cada apartat:** les **Activitats 1-3** segueixen les mateixes sessions que la fitxa base (aquí amb les ampliacions de codi) · **Si t'encalles** i **Pensament computacional**: durant el treball · **Vols més?**: amb el nucli al dia · **Exit ticket**: els últims 2' de la Sessió 3 · **Diana** i **Quadern tècnic**: en tancar la SA · **Context real i ODS**: quan el docent l'activi.

**Nom:** ______________________  **Data:** __________

> En aquesta unitat formalitzaràs el concepte de **funció** (paràmetres, valor de retorn) i el faràs servir per moure un servomotor i dos motoreductors, fins a muntar el **vehicle** del fil conductor. Tot el treball és **individual**.

---

## Activitat 1 · Funcions amb paràmetres i valor de retorn

Programa el servo de la mascota ([`SA4_esquemes_connexions.md`](SA4_esquemes_connexions.md)) amb [`funcions_moviments.py`](codi/funcions_moviments/funcions_moviments.py).

**0. PREDIU:** `graus_a_pwm(angle)` té un `return`; `mou_servo(angle)` no en té cap. Quina de les dues es podria fer servir dins d'un `if` (per exemple, `if graus_a_pwm(90) > 100:`) i quina no? Per què?

___________________________________________________________________

1. **Executa** `funcions_moviments.py` i comprova la teva predicció.
2. **Afegeix una funció nova** `centra()` (sense paràmetres) que porti el servo a 90° directament.

**+ Repte:** escriu una funció `saluda_lenta(vegades, pausa)` amb **dos** paràmetres, on `pausa` controli el `sleep()` entre moviments.

---

## Activitat 2 · Funcions de moviment del motoreductor

Munta els dos motoreductors ([`SA4_esquemes_connexions.md`](SA4_esquemes_connexions.md)). Parteix de [`velocitat_pwm.py`](codi/velocitat_pwm/velocitat_pwm.py).

**Pregunta:** per què cada motor necessita **dos** pins (un per sentit) en lloc d'un de sol amb un número positiu o negatiu?

___________________________________________________________________

**Les teves velocitats de prova:** lenta = ______ , ràpida = ______ → comprovades amb el vehicle sobre la taula (rodes a l'aire, sense que caigui).

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió).** Banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

**+ Ampliació (opcional):** afegeix una funció `acceleracio(velocitat_final)` que pugi la velocitat de mica en mica (com `respira()` a la SA2) en lloc de saltar directament al valor final.

---

## Activitat 3 · Repte «control per botons» (producte)

Parteix de [`control_per_botons.py`](codi/control_per_botons/control_per_botons.py) i programa la **teva** seqüència pròpia amb les funcions de moviment.

**Codi (o descripció de com l'has fet):**

```python

```

**Mini-defensa:** anota aquí la **decisió** que explicaràs (per exemple, per què aquest ordre de moviments o aquesta velocitat):

___________________________________________________________________

---

## Si t'encalles

1. **Pista 1:** repassa l'[esquema de connexions](SA4_esquemes_connexions.md) — molts errors de "no es mou" són cablatge o alimentació (USB en lloc de piles), no codi.
2. **Pista 2:** prova la funció **sola** al REPL amb un valor conegut abans de buscar l'error en un programa més gran.
3. **Pista 3:** aplica **DEPURA** i, si cal, demana ajuda **explicant què ja has provat**.

> **Rutina DEPURA:** **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara i torna a provar · **A**punta-ho al quadern.

## Vols més?

- **Reptes ⭐⭐/⭐⭐⭐:** tria'n un a [`Reptes/Reptes_SA4.md`](../../Reptes/Reptes_SA4.md) i amplia el teu producte (el ⭐ ja és nucli obligatori, fet a la fitxa base).
- **Simulador:** el de [python.microbit.org](https://python.microbit.org) **no** reprodueix ni el servo ni els motoreductors (vegeu [`SA4_esquemes_connexions.md`](SA4_esquemes_connexions.md) §Simulació); només botons, display i so sense `pin=`.

---

## Pensament computacional d'aquesta SA

Avui has practicat l'**ABSTRACCIÓ** i la **modularitat**: `avancar(400)` amaga tot el detall de pins i PWM darrere d'un nom que expressa la intenció. On més has vist "amagar el detall darrere d'un nom senzill" (a la vida real o en altres programes)? ______________________

## Diana d'autoavaluació

Situa't (0-10):

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Defineixo i crido funcions amb paràmetres i valor de retorn | ☐ | ☐ | ☐ | ☐ |
| Controlo un servomotor i un motoreductor amb PWM | ☐ | ☐ | ☐ | ☐ |
| Munto el vehicle amb seguretat, cablatge segons l'esquema | ☐ | ☐ | ☐ | ☐ |

## Exit ticket (abans de marxar, Sessió 3)

1. Una cosa que he après avui: ______________________
2. Una cosa que encara no tinc clara: ______________________
3. On ho faria servir al món real: ______________________

## Context real i ODS

Braços robòtics industrials, aspiradors robot, drons: tots encapsulen moviments complexos en ordres senzilles (funcions). **ODS 9** (indústria, innovació i infraestructura): la modularitat del codi permet construir sistemes fiables a partir de peces senzilles i provades per separat, com les funcions de moviment d'avui. Escriu un exemple propi: ______________________

---

## Quadern tècnic (entrada de la SA4)

> El quadern tècnic és el teu **diari de bord** de tot el curs. Segueix el **mètode de projecte**: *analitzar → dissenyar → programar/prototipar → provar → millorar.*

- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com ho vaig solucionar i què vaig millorar): ___________________________________________________
- **Quin error he tingut i com l'he resolt:** ___________________________
- **Muntatge del vehicle:** com ha anat, quines dificultats mecàniques hi ha hagut i com les has resolt.
- **Reflexió ètica** (seguretat elèctrica): per què és important desconnectar l'alimentació abans de tocar el cablatge d'un motor, i què podria passar si no ho fas:
  - ______________________________________________________
