# SA9 · Fitxa ampliada (aprofundiment) — Repte final integrador

> 📄 **Versió ampliada**: conté totes les activitats i les rutines d'aprofundiment (pensament computacional, diana, exit ticket, ODS…). La fitxa que fa **tot l'alumnat** és la base: **[SA9_fitxa_alumnat.md](SA9_fitxa_alumnat.md)**.

> 🧑‍🎓 **Quan toca obrir-la?** És **opcional**: quan portis la **fitxa base al dia** i vulguis més (ampliacions de repte, pensament computacional, ODS). Algunes rutines (exit ticket) les activarà el **docent** a l'aula quan toqui.

> 🗺️ **Quan s'usa cada apartat:** les **Activitats 1-4** segueixen les mateixes sessions que la fitxa base (aquí amb preguntes d'ampliació) · **Si t'encalles** i **Pensament computacional**: durant el treball · **Vols més?**: amb el nucli al dia · **Exit ticket**: els últims 2' de la Sessió 4 · **Diana** i **Quadern tècnic**: en tancar la SA · **Context real i ODS**: quan el docent l'activi.

**Nom:** ______________________  **Data:** __________

> Avui tanques el curs amb el teu propi projecte: tries, dissenyes, construeixes, proves i defenses una solució teva. Tot el treball és **individual**.

---

## Activitat 1 · Idear

**0. PREDIU:** dels sis reptes del [banc](SA9_reptes_proposats.md), quin creus que et costarà **més** de programar (no de muntar)? Per què?

___________________________________________________________________

1. Tria el teu repte i escriu **3 requisits mínims** que hagi de complir com a mínim.
2. Fes un esbós de la solució (dibuix o descripció de la disposició física i del flux de dades).

**+ Repte:** combina **dos** reptes del banc (per exemple, reg + telemetria: el rover rega i envia un avís per ràdio quan ho fa) o pensa una variant pròpia validada pel docent.

---

## Activitat 2 · Prototipar

Parteix de [`plantilla_projecte.py`](codi/plantilla_projecte/plantilla_projecte.py) i integra-hi el maquinari i la lògica del teu repte.

**Pregunta:** per què `plantilla_projecte.py` separa `percep()`, `decideix()` i `actua()` en tres funcions diferents, en lloc d'escriure-ho tot dins del `while True`?

___________________________________________________________________

**El meu component nou (maquinari afegit al rover):**

| Component | Pin | Del meu repte (⭐/⭐⭐/⭐⭐⭐) |
|---|---|---|
| | | |

---

## Activitat 3 · Provar i millorar

**Pregunta:** quina diferència hi ha entre una prova que confirma que el sistema **funciona en el cas normal** i una prova de **límit** (per exemple, què passa si el sensor d'humitat es desconnecta a mig repte de reg)? Per què cal fer totes dues?

___________________________________________________________________

**+ Ampliació (opcional):** fes una **segona iteració** documentada al dossier (§7, Millores futures avançades a §6): un canvi de disseny motivat per un problema real que has trobat, no només un afegit cosmètic.

---

## Activitat 4 · Comunicar

Tanca el [dossier tècnic](SA9_dossier_plantilla.md) i prepara la teva defensa amb el [guió de defensa](../00_General/00_Guia_defensa_oral.md).

**Pregunta:** dels 3 indicadors de la R4·DO (claredat, decisió justificada, resposta a preguntes), quin creus que et costarà més i com et prepares per a ell?

___________________________________________________________________

**+ Ampliació — alternatives descartades:** al teu dossier (§2), afegeix **una alternativa** de disseny que vas considerar i **per què** la vas descartar (nivell «Excel·lent» de l'indicador «Decisió tècnica justificada»).

---

## Si t'encalles

1. **Pista 1:** aïlla el problema — prova primer el component nou sol (sense la resta del sistema) abans de barrejar-lo amb la FSM completa.
2. **Pista 2:** si un component "no fa res", llegeix-ne el valor al REPL amb `print()` abans de sospitar de la lògica de decisió.
3. **Pista 3:** aplica **DEPURA** i, si cal, demana ajuda **explicant què ja has provat**.

> **Rutina DEPURA:** **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara i torna a provar · **A**punta-ho al dossier.

## Vols més?

- **Reptes ⭐⭐/⭐⭐⭐:** amplia el teu repte fins al criteri d'èxit més alt al [banc de reptes](SA9_reptes_proposats.md).
- **Simulador:** la **ràdio i el mòdul `log`** SÍ es simulen a python.microbit.org; **cap** sensor dels Kits 2-3 ni els motors s'hi simulen (com a SA7-SA8).
- **Treball de Recerca:** el teu repte de la SA9 pot ser la llavor d'un futur TR; parla-ho amb el docent si t'interessa.

---

## Pensament computacional d'aquesta SA

Avui has practicat la **integració de sistemes**: combinar peces ja provades per separat (sensors, FSM, motors, ràdio) en un tot coherent que resol un problema nou és el mateix pas que fan els enginyers reals en passar d'un prototip de laboratori a un producte. On més has vist "peces separades que es combinen en un sistema" (una app del mòbil, un cotxe, una casa domòtica)? ______________________

## Diana d'autoavaluació

Situa't (0-10):

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Gestiono el meu projecte individual (anàlisi → prototip → proves → millora) | ☐ | ☐ | ☐ | ☐ |
| Integro almenys dos blocs del curs en una solució coherent | ☐ | ☐ | ☐ | ☐ |
| El meu dossier tècnic és complet i està ben documentat | ☐ | ☐ | ☐ | ☐ |
| Faig una defensa oral clara, amb una decisió justificada i responc preguntes | ☐ | ☐ | ☐ | ☐ |

## Exit ticket (abans de marxar, Sessió 4)

1. Una cosa que he après avui: ______________________
2. Una cosa que encara no tinc clara: ______________________
3. On ho faria servir al món real: ______________________

## Context real i ODS

Sistemes de reg intel·ligent, robots de vigilància domèstica, estacions ambientals urbanes, robots de logística: tots combinen sensors, decisió i actuació en un producte que resol un problema real, exactament com el teu repte. **ODS 6** (aigua neta, si has fet el repte de reg), **ODS 9** (indústria i innovació) o **ODS 11** (ciutats sostenibles), segons el repte triat. Escriu un exemple propi: ______________________

---

## Quadern tècnic (entrada de la SA9)

> El quadern tècnic és el teu **diari de bord** de tot el curs. A la SA9, coincideix essencialment amb el teu [dossier tècnic](SA9_dossier_plantilla.md): no cal duplicar contingut, sí fer-hi constar el resum de cada sessió.

- **Què he après (integrant tot el curs):** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com ho vaig solucionar i què vaig millorar): ___________________________________________________
- **Quin error he tingut i com l'he resolt:** ___________________________
- **Reflexió ètica i ODS:** quin ODS connecta amb el meu repte, i per què.
  - ______________________________________________________
