# SA8 · Fitxa ampliada (aprofundiment) — Autonomia i telemetria

> 📄 **Versió ampliada**: conté totes les activitats i les rutines d'aprofundiment (pensament computacional, diana, exit ticket, ODS…). La fitxa que fa **tot l'alumnat** és la base: **[SA8_fitxa_alumnat.md](SA8_fitxa_alumnat.md)**.

> 🧑‍🎓 **Quan toca obrir-la?** És **opcional**: quan portis la **fitxa base al dia** i vulguis més (ampliacions de codi, pensament computacional, ODS). Algunes rutines (exit ticket) les activarà el **docent** a l'aula quan toqui.

> 🗺️ **Quan s'usa cada apartat:** les **Activitats 1-3** segueixen les mateixes sessions que la fitxa base (aquí amb les ampliacions de codi) · **Si t'encalles** i **Pensament computacional**: durant el treball · **Vols més?**: amb el nucli al dia · **Exit ticket**: els últims 2' de la Sessió 3 · **Diana** i **Quadern tècnic**: en tancar la SA · **Context real i ODS**: quan el docent l'activi.

**Nom:** ______________________  **Data:** __________

> Avui el teu rover aprèn a **explicar-se**: llegeix sensors avançats i envia el que "sent" per ràdio a un altre programa, escrit també per tu. Tot el treball és **individual**.

---

## Activitat 1 · Sensors avançats i comportaments amb prioritats

Configura i prova [`comportaments.py`](codi/comportaments/comportaments.py).

**0. PREDIU:** si el rover és a l'estat `ESQUIVAR` i encara no ha passat el `sleep(400)` del gir, i en aquell instant tornes a prémer el polsador STOP, què hauria de passar amb el gir en curs?

___________________________________________________________________

1. **Executa** `comportaments.py` i comprova que el rover encadena correctament els tres estats (`SEGUIR` → `ESQUIVAR` → `RECUPERAR` → `SEGUIR`) davant d'un obstacle real.
2. **Dissenya el teu format de missatge de telemetria**: quins camps (com a mínim, dos sensors del Kit 3), amb quin prefix.

**+ Repte:** afegeix un **quart estat** a la FSM (per exemple, `ATURAT_TEMPORAL`, que es dispara si la distància de l'obstacle és extremadament curta, i espera un temps més llarg abans de tornar a `SEGUIR`).

---

## Activitat 2 · Telemetria per ràdio

Parteix de [`telemetria_radio.py`](codi/telemetria_radio/telemetria_radio.py) i escriu el teu propi [`estacio_base.py`](codi/estacio_base/estacio_base.py).

**Pregunta:** per què `telemetria_radio.py` i `estacio_base.py` han de fer servir literalment el mateix `PREFIX` i el mateix `group`? Què passaria si els dos "parlessin idiomes" diferents?

___________________________________________________________________

**El meu protocol de telemetria:**

| Camp | Sensor/dada | Exemple de valor |
|---|---|---|
| `D` | Distància HC-SR04 (cm) | |
| `S` | Seguidor de línia (0-1023) | |
| `E` | Estat de la FSM | |
| `T` | Temperatura DHT11 | |
| `H` | Humitat DHT11 | |
| `O` | Orientació IMU | |

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió).** Banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

**+ Ampliació (opcional):** afegeix el **BMP280** (pressió) o el **CCS811** (CO₂) al mateix bus I2C (P19/P20, adreça diferent) i un nou camp al missatge de telemetria.

---

## Activitat 3 · IA aplicada al control i producte

Parteix de la reflexió sobre `mpu_orientacio()` de [`telemetria_radio.py`](codi/telemetria_radio/telemetria_radio.py).

**Pregunta:** `mpu_orientacio()` decideix amb un llindar que **tu** has escrit (0.85-1.15 g). Si volguessis que un model de IA (per exemple, Teachable Machine) aprengués aquesta decisió a partir d'exemples, què hauries de fer **abans** d'entrenar-lo (pensa en quantitat i varietat d'exemples)?

___________________________________________________________________

**Comportament triat per al producte (marca'l):** ☐ Nucli (IMU + DHT11) · ☐ Nucli + un sensor d'ampliació (BMP280/CCS811)

**+ Ampliació — comparació manual vs IA:** classifica manualment 10 lectures de `mpu_orientacio()` amb el teu llindar i, si tens accés a Teachable Machine, compara-ho amb el que decidiria un model entrenat amb poques mostres. Anota on coincideixen i on no, i per què creus que passa.

---

## Si t'encalles

1. **Pista 1:** aïlla el problema — prova primer `comportaments.py` (sense ràdio ni Kit 3) per confirmar que la FSM és correcta abans de barrejar-la amb la telemetria.
2. **Pista 2:** si un sensor "no reacciona com toca", llegeix el seu valor al REPL amb `print()` abans de sospitar de l'algorisme de decisió.
3. **Pista 3:** aplica **DEPURA** i, si cal, demana ajuda **explicant què ja has provat**.

> **Rutina DEPURA:** **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara i torna a provar · **A**punta-ho al quadern.

## Vols més?

- **Reptes ⭐⭐/⭐⭐⭐:** tria'n un a [`Reptes/Reptes_SA8.md`](../../Reptes/Reptes_SA8.md) i amplia el teu producte (el ⭐ ja és nucli obligatori, fet a la fitxa base).
- **Simulador:** la **ràdio i el mòdul `log`** SÍ es simulen a python.microbit.org (2 instàncies); **cap** sensor (DHT11, IMU) ni els motors s'hi simulen (vegeu [`SA8_esquemes_connexions.md`](SA8_esquemes_connexions.md) §Simulació).

---

## Pensament computacional d'aquesta SA

Avui has practicat l'**abstracció de protocol**: un format de missatge senzill (`"TEL:D:23;T:24"`) amaga darrere seu com es llegeix cada sensor concret, perquè qui rep el missatge no necessiti saber-ho. On més has vist "un format senzill que amaga complexitat" (una URL, un codi de barres, un missatge de xat)? ______________________

## Diana d'autoavaluació

Situa't (0-10):

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Llegeixo l'IMU MPU6050 i el DHT11 i n'interpreto les magnituds | ☐ | ☐ | ☐ | ☐ |
| Envio dades de sensors per ràdio amb un protocol propi | ☐ | ☐ | ☐ | ☐ |
| Registro i visualitzo dades rebudes (llista, mitjana) | ☐ | ☐ | ☐ | ☐ |
| Explico la diferència entre una regla feta a mà i un model d'IA entrenat amb dades | ☐ | ☐ | ☐ | ☐ |

## Exit ticket (abans de marxar, Sessió 3)

1. Una cosa que he après avui: ______________________
2. Una cosa que encara no tinc clara: ______________________
3. On ho faria servir al món real: ______________________

## Context real i ODS

Estacions meteorològiques connectades, sensors de qualitat de l'aire urbans, flotes de robots de magatzem que reporten el seu estat a un panell central: tots combinen sensors, un protocol de dades i un punt de recepció, com avui. **ODS 9** (indústria, innovació i infraestructura) i **ODS 11** (ciutats i comunitats sostenibles). Escriu un exemple propi: ______________________

---

## Quadern tècnic (entrada de la SA8)

> El quadern tècnic és el teu **diari de bord** de tot el curs. Segueix el **mètode de projecte**: *analitzar → dissenyar → programar/prototipar → provar → millorar.*

- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com ho vaig solucionar i què vaig millorar): ___________________________________________________
- **Quin error he tingut i com l'he resolt:** ___________________________
- **El meu format de missatge de telemetria** final i per què.
- **Reflexió ètica (privadesa i dades):** la telemetria del teu rover és una dada que **tu** has generat. Per què creus que és important pensar en la privadesa i el consentiment fins i tot quan les dades semblen "només d'un robot"?
  - ______________________________________________________
