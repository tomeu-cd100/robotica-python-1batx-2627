# SA7 · Fitxa ampliada (aprofundiment) — Robòtica mòbil: el rover

> 📄 **Versió ampliada**: conté totes les activitats i les rutines d'aprofundiment (pensament computacional, diana, exit ticket, ODS…). La fitxa que fa **tot l'alumnat** és la base: **[SA7_fitxa_alumnat.md](SA7_fitxa_alumnat.md)**.

> 🧑‍🎓 **Quan toca obrir-la?** És **opcional**: quan portis la **fitxa base al dia** i vulguis més (ampliacions de codi, pensament computacional, ODS). Algunes rutines (exit ticket) les activarà el **docent** a l'aula quan toqui.

> 🗺️ **Quan s'usa cada apartat:** les **Activitats 1-4** segueixen les mateixes sessions que la fitxa base (aquí amb les ampliacions de codi) · **Si t'encalles** i **Pensament computacional**: durant el treball · **Vols més?**: amb el nucli al dia · **Exit ticket**: els últims 2' de la Sessió 4 · **Diana** i **Quadern tècnic**: en tancar la SA · **Context real i ODS**: quan el docent l'activi.

**Nom:** ______________________  **Data:** __________

> Avui el teu rover deixa de necessitar un comandament: aprèn a **decidir sol** amb cinemàtica diferencial, un sensor de línia i un sensor d'ultrasons. Tot el treball és **individual**.

---

## Activitat 1 · Cinemàtica diferencial

Configura i prova [`calibratge_motors.py`](codi/calibratge_motors/calibratge_motors.py).

**0. PREDIU:** si `FACTOR_M1 = 1.0` i `FACTOR_M2 = 0.5`, com creus que es mourà el rover en cridar `avancar_calibrat(500)`: recte, o descrivint una corba cap a un costat? Cap a quin costat?

___________________________________________________________________

1. **Executa** `calibratge_motors.py` i calibra `FACTOR_M1`/`FACTOR_M2` fins que el teu rover vagi recte en una distància d'1-2 m.
2. **Modelitza una trajectòria:** amb `girar()` i `avancar()` temporitzats, programa una trajectòria en **"L"** (dos costats, un gir de 90°).

**+ Repte:** amplia la trajectòria a un **triangle** o una **estrella**, calculant tu mateix els temps de gir necessaris.

---

## Activitat 2 · Seguidor de línia

Parteix de [`segueix_linia.py`](codi/segueix_linia/segueix_linia.py). Calibra el llindar i documenta'l.

**Pregunta:** per què el llindar de detecció **no** és un valor universal vàlid per a tota la classe, sinó que cal calibrar-lo a cada taula?

___________________________________________________________________

**El meu llindar i com l'he trobat:**

| Lectura sobre la línia (negre) | Lectura fora de la línia (blanc) | Llindar triat |
|---|---|---|
| | | |

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió).** Banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

**+ Ampliació (opcional):** en lloc d'un gir fix cap a un costat quan es perd la línia, prova de **recordar** el darrer costat on es va veure la línia i cerca primer cap allà (pista: guarda l'últim costat detectat en una variable).

---

## Activitat 3 · Evita-obstacles i «tria un comportament autònom»

Parteix de [`evita_obstacles.py`](codi/evita_obstacles/evita_obstacles.py).

**Pregunta:** compara `mesura_distancia()` d'aquesta SA amb `distancia_cm()` de `alarma_ultrasons.py` (SA3): què és **exactament** igual, i què és diferent?

___________________________________________________________________

**Comportament triat (marca'l):** ☐ Seguidor de línia · ☐ Evita-obstacles · ☐ Tots dos

**+ Ampliació — marge de seguretat variable:** en lloc d'un únic `LLINDAR_OBSTACLE_CM` fix, prova de reduir la velocitat d'avanç quan la distància és mitjana (per exemple, entre 15 i 30 cm) i només aturar-te del tot per sota de 15 cm.

---

## Activitat 4 · Missions del rover (producte)

Parteix de [`rover_missions.py`](codi/rover_missions/rover_missions.py) i integra el teu comportament triat.

**Codi (o descripció de com l'has fet):**

```python

```

**Mini-defensa:** anota aquí la **decisió** que explicaràs (per exemple, per què has triat aquest llindar, o com garanteixes que el polsador STOP interromp qualsevol missió):

___________________________________________________________________

**+ Ampliació — combinar línia I obstacles:** integra els dos comportaments en una sola missió amb prioritats (per exemple, l'obstacle sempre "guanya" sobre el seguiment de línia, com fa `missio_linia()` de `rover_missions.py`), i documenta la teva pròpia variant.

**+ Ampliació — control proporcional bàsic:** en lloc del tot/res (avançar a velocitat fixa o aturar-se), varia la velocitat en funció d'una lectura contínua (més a prop d'un obstacle, més lent). **No és el nucli avaluable d'aquesta SA**, però és el mateix concepte que trobaràs de manera més completa a la SA8.

---

## Si t'encalles

1. **Pista 1:** aïlla el problema — prova primer `calibratge_motors.py` (sense sensors) per confirmar que el moviment bàsic és correcte abans de barrejar-lo amb el seguidor de línia o l'HC-SR04.
2. **Pista 2:** si un sensor "no reacciona com toca", llegeix el seu valor al REPL amb `print()` abans de sospitar de l'algorisme de decisió.
3. **Pista 3:** aplica **DEPURA** i, si cal, demana ajuda **explicant què ja has provat**.

> **Rutina DEPURA:** **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara i torna a provar · **A**punta-ho al quadern.

## Vols més?

- **Reptes ⭐⭐/⭐⭐⭐:** tria'n un a [`Reptes/Reptes_SA7.md`](../../Reptes/Reptes_SA7.md) i amplia el teu producte (el ⭐ ja és nucli obligatori, fet a la fitxa base).
- **Simulador:** el de [python.microbit.org](https://python.microbit.org) **NO** simula cap component del rover (ni motors, ni HC-SR04, ni seguidor de línia): vegeu [`SA7_esquemes_connexions.md`](SA7_esquemes_connexions.md) §Simulació. Útil només per esbossar en pseudocodi la **lògica** d'una trajectòria, no per provar-la.

---

## Pensament computacional d'aquesta SA

Avui has practicat la **modelització de trajectòries**: descompondre un moviment complex (seguir una corba, esquivar un objecte) en una seqüència petita de passos simples (avança, gira, atura, torna a mesurar). On més has vist "un sistema que es mou sol combinant passos simples i repetits" (una aspiradora robot, un braç industrial, un dron de repartiment)? ______________________

## Diana d'autoavaluació

Situa't (0-10):

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Relaciono el gir del rover amb la velocitat/sentit de cada motor | ☐ | ☐ | ☐ | ☐ |
| Programo un seguidor de línia amb llindar calibrat | ☐ | ☐ | ☐ | ☐ |
| Programo un evita-obstacles amb l'HC-SR04 | ☐ | ☐ | ☐ | ☐ |
| Modelitzo una trajectòria combinant girs i avanços | ☐ | ☐ | ☐ | ☐ |

## Exit ticket (abans de marxar, Sessió 4)

1. Una cosa que he après avui: ______________________
2. Una cosa que encara no tinc clara: ______________________
3. On ho faria servir al món real: ______________________

## Context real i ODS

Robots de neteja domèstics (seguidor de vora), vehicles autònoms d'inspecció industrial, robots de magatzem que eviten obstacles: tots combinen sensors de percepció senzills amb algorismes de decisió reactius com els d'avui. **ODS 9** (indústria, innovació i infraestructura) i **ODS 11** (ciutats i comunitats sostenibles): els robots mòbils autònoms redueixen tasques repetitives i perilloses. Escriu un exemple propi: ______________________

---

## Quadern tècnic (entrada de la SA7)

> El quadern tècnic és el teu **diari de bord** de tot el curs. Segueix el **mètode de projecte**: *analitzar → dissenyar → programar/prototipar → provar → millorar.*

- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com ho vaig solucionar i què vaig millorar): ___________________________________________________
- **Quin error he tingut i com l'he resolt:** ___________________________
- **Els meus llindars i factors finals** (LLINDAR_LINIA, LLINDAR_OBSTACLE_CM, FACTOR_M1/FACTOR_M2).
- **Reflexió ètica** (autonomia i responsabilitat): un robot que "decideix sol" (quan girar, quan aturar-se) encara depèn totalment dels llindars que tu li has donat. Per què creus que és important documentar **per què** vas triar aquests valors, i no només quins són:
  - ______________________________________________________
