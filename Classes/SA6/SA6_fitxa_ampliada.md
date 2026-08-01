# SA6 · Fitxa ampliada (aprofundiment) — Control: el robot decideix

> 📄 **Versió ampliada**: conté totes les activitats i les rutines d'aprofundiment (pensament computacional, diana, exit ticket, ODS…). La fitxa que fa **tot l'alumnat** és la base: **[SA6_fitxa_alumnat.md](SA6_fitxa_alumnat.md)**.

> 🧑‍🎓 **Quan toca obrir-la?** És **opcional**: quan portis la **fitxa base al dia** i vulguis més (ampliacions de codi, pensament computacional, ODS). Algunes rutines (exit ticket) les activarà el **docent** a l'aula quan toqui.

> 🗺️ **Quan s'usa cada apartat:** les **Activitats 1-3** segueixen les mateixes sessions que la fitxa base (aquí amb les ampliacions de codi) · **Si t'encalles** i **Pensament computacional**: durant el treball · **Vols més?**: amb el nucli al dia · **Exit ticket**: els últims 2' de la Sessió 3 · **Diana** i **Quadern tècnic**: en tancar la SA · **Context real i ODS**: quan el docent l'activi.

**Nom:** ______________________  **Data:** __________

> Avui converteixes el vehicle teledirigit en un **sistema de control real**: dissenyaràs una màquina d'estats, hi integraràs una aturada d'emergència prioritària i, si vols anar més enllà, un sensor de realimentació. Tot el treball és **individual**.

---

## Activitat 1 · Llaç obert, llaç tancat i la primera FSM

Configura i prova [`maquina_estats_semafor.py`](codi/maquina_estats_semafor/maquina_estats_semafor.py) i [`termostat_histeresi.py`](codi/termostat_histeresi/termostat_histeresi.py).

**0. PREDIU:** dibuixa una línia de temperatura que puja de 20 a 30 graus i torna a baixar fins a 20. Amb `LLINDAR_BAIX = 24` i `LLINDAR_ALT = 26`, marca-hi els punts exactes on el relé canvia d'estat.

___________________________________________________________________

1. **Executa** `maquina_estats_semafor.py` i comprova que els temps de cada estat coincideixen amb el diagrama `TRANSICIONS`.
2. **Amplia el semàfor:** afegeix un quart estat `INTERMITENT` (per exemple, per a un "semàfor apagat de nit") que faci parpellejar el groc cada 500 ms fins que es premi el botó A per tornar a VERD.

**+ Repte:** reescriu `TRANSICIONS` perquè cada estat tingui una durada **diferent** segons si és de dia o de nit (per exemple, llegint `running_time()` com a simulació d'hora).

---

## Activitat 2 · Aturada d'emergència prioritària

Parteix de [`vehicle_seguretat.py`](codi/vehicle_seguretat/vehicle_seguretat.py). Implementa l'STOP prioritari i documenta'l.

**Pregunta:** per què el codi comprova el **polsador** abans de mirar el missatge de ràdio a cada volta del bucle, i no al revés?

___________________________________________________________________

**El meu diagrama d'estats:**

| Estat | Com s'hi entra | Com se'n surt |
|---|---|---|
| RUN | | |
| STOP | | |
| ALERTA *(si l'amplies)* | | |

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió).** Banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

**+ Ampliació (opcional):** prova [`registre_dades.py`](codi/registre_dades/registre_dades.py) i llegeix el fitxer `MY_DATA.HTM` per USB; documenta al quadern una gràfica o taula amb dades reals de temperatura/llum.

---

## Activitat 3 · Repte «vehicle amb aturada d'emergència» (producte)

Parteix de [`vehicle_seguretat.py`](codi/vehicle_seguretat/vehicle_seguretat.py) i tanca el teu vehicle amb l'STOP prioritari.

**Codi (o descripció de com l'has fet):**

```python

```

**Mini-defensa:** anota aquí la **decisió** que explicaràs (per exemple, per què has organitzat `actualitza_estat()` en un únic lloc, o com garanteixes que el polsador i la comanda `"X"` tenen exactament la mateixa prioritat):

___________________________________________________________________

**+ Ampliació — Tercer estat ALERTA:** afegeix un tercer estat `ALERTA` (per exemple, activat pel sensor de temperatura/DHT11 del Kit 3, o per un HC-SR04 si el vols provar): fes que el LED indicador **parpellegi** en ALERTA (a diferència del fix de RUN i l'apagat d'STOP) i documenta la transició nova al teu diagrama.

**+ Ampliació — Realimentació proporcional:** en lloc del tot/res del termòstat, prova de variar la **velocitat** del vehicle en funció d'una distància o d'una lectura contínua (per exemple, més a prop d'un obstacle, més lent), en lloc d'aturar-se de cop. **No és el nucli avaluable d'aquesta SA**, però connecta amb el control que veuràs al 3r trimestre amb el rover (T3).

---

## Si t'encalles

1. **Pista 1:** aïlla el problema — prova primer `maquina_estats_semafor.py` (sense motors ni ràdio) per confirmar que la teva lògica de FSM és correcta abans de barrejar-la amb `vehicle_seguretat.py`.
2. **Pista 2:** si l'STOP "de vegades" no funciona, revisa que **cap** camí del bucle pugui arribar a moure els motors sense passar abans per la comprovació del polsador.
3. **Pista 3:** aplica **DEPURA** i, si cal, demana ajuda **explicant què ja has provat**.

> **Rutina DEPURA:** **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara i torna a provar · **A**punta-ho al quadern.

## Vols més?

- **Reptes ⭐:** tria'n un a [`Reptes/Reptes_SA6.md`](../../Reptes/Reptes_SA6.md) i amplia el teu producte.
- **Simulador:** el de [python.microbit.org](https://python.microbit.org) **sí** simula `temperature()`, els botons i el mòdul `log`, però **NO** simula motors ni relé (vegeu [`SA6_esquemes_connexions.md`](SA6_esquemes_connexions.md) §Simulació): és una bona via de pràctica individual a casa per a la part de lògica.

---

## Pensament computacional d'aquesta SA

Avui has practicat l'**abstracció d'estats**: reduir un sistema complex (motors, ràdio, sensors) a un nombre petit i tancat d'estats possibles, amb transicions clares entre ells. On més has vist "un sistema que només pot ser en un estat de cada vegada, amb regles clares per canviar-hi" (semàfors, ascensors, un rentavaixelles, un videojoc)? ______________________

## Diana d'autoavaluació

Situa't (0-10):

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Distingeixo llaç obert de llaç tancat | ☐ | ☐ | ☐ | ☐ |
| Programo una màquina d'estats amb condicionals | ☐ | ☐ | ☐ | ☐ |
| L'STOP interromp qualsevol moviment, sigui quin sigui l'origen | ☐ | ☐ | ☐ | ☐ |
| Integro un sensor amb histèresi (sense oscil·lació) | ☐ | ☐ | ☐ | ☐ |

## Exit ticket (abans de marxar, Sessió 3)

1. Una cosa que he après avui: ______________________
2. Una cosa que encara no tinc clara: ______________________
3. On ho faria servir al món real: ______________________

## Context real i ODS

Termòstats domèstics, ascensors, semàfors, robots de magatzem amb aturada d'emergència obligatòria per normativa de seguretat laboral: tots són sistemes de control amb estats, i molts porten una aturada prioritària semblant a la d'avui. **ODS 9** (indústria, innovació i infraestructura) i **ODS 12** (producció i consum responsables): la histèresi evita el desgast innecessari d'actuadors i l'STOP prioritari és el mateix principi de seguretat dels robots industrials reals. Escriu un exemple propi: ______________________

---

## Quadern tècnic (entrada de la SA6)

> El quadern tècnic és el teu **diari de bord** de tot el curs. Segueix el **mètode de projecte**: *analitzar → dissenyar → programar/prototipar → provar → millorar.*

- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com ho vaig solucionar i què vaig millorar): ___________________________________________________
- **Quin error he tingut i com l'he resolt:** ___________________________
- **El meu diagrama d'estats final** (estats i transicions, amb l'STOP marcat com a prioritari).
- **Reflexió ètica** (seguretat i automatització): un robot amb aturada d'emergència ha de decidir *sempre* aturar-se davant del dubte, encara que això signifiqui aturar-se "sense necessitat" de tant en tant. Per què creus que aquesta és la decisió de disseny correcta en un sistema de seguretat, encara que sembli "menys eficient":
  - ______________________________________________________
