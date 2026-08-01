# SA5 · Fitxa ampliada (aprofundiment) — Ràdio: robots que parlen

> 📄 **Versió ampliada**: conté totes les activitats i les rutines d'aprofundiment (pensament computacional, diana, exit ticket, ODS…). La fitxa que fa **tot l'alumnat** és la base: **[SA5_fitxa_alumnat.md](SA5_fitxa_alumnat.md)**.

> 🧑‍🎓 **Quan toca obrir-la?** És **opcional**: quan portis la **fitxa base al dia** i vulguis més (ampliacions de codi, pensament computacional, ODS). Algunes rutines (exit ticket) les activarà el **docent** a l'aula quan toqui.

> 🗺️ **Quan s'usa cada apartat:** les **Activitats 1-3** segueixen les mateixes sessions que la fitxa base (aquí amb les ampliacions de codi) · **Si t'encalles** i **Pensament computacional**: durant el treball · **Vols més?**: amb el nucli al dia · **Exit ticket**: els últims 2' de la Sessió 3 · **Diana** i **Quadern tècnic**: en tancar la SA · **Context real i ODS**: quan el docent l'activi.

**Nom:** ______________________  **Data:** __________

> En aquesta unitat faràs que dues micro:bit es **parlin** per ràdio, dissenyaràs el teu propi **protocol** de comandes i el faràs servir per controlar el vehicle a distància. Tot el treball és **individual**; l'emparellament amb un company és només un banc de proves puntual.

---

## Activitat 1 · Xat per ràdio

Configura la ràdio amb el teu grup assignat i prova [`radio_missatges.py`](codi/radio_missatges/radio_missatges.py).

**0. PREDIU:** `radio.receive()` torna `None` quan no ha arribat cap missatge nou des de l'última volta del bucle. Si el cridessis **un sol cop**, fora d'un `while True:`, quina probabilitat hi ha que capturi el missatge que t'envia un company just en aquell instant?

___________________________________________________________________

1. **Executa** `radio_missatges.py` aparellat amb un company i comprova que et rep i el reps.
2. **Amplia l'historial:** en lloc de mostrar només el darrer missatge amb el botó B, fes que `display.scroll()` mostri **tot** l'historial (`historic`) separat per espais.

**+ Repte:** afegeix un comptador de missatges rebuts (`total_rebuts`) i mostra'l amb `display.scroll(str(total_rebuts))` quan es prem A+B.

---

## Activitat 2 · Un protocol propi de comandes

Parteix de [`comandament.py`](codi/comandament/comandament.py). Dissenya el teu protocol i documenta'l.

**Pregunta:** per què cal un **prefix** (`"CMD:"`) i no n'hi hauria prou amb enviar directament la lletra de l'ordre?

___________________________________________________________________

**El meu protocol:**

| Comanda | Entrada que l'envia | Acció al receptor |
|---|---|---|
| | | |
| | | |
| | | |

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió).** Banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

**+ Ampliació (opcional):** afegeix una comanda de **velocitat variable** (per exemple, `"CMD:V5"` per a velocitat 500) que el receptor interpreti extraient el número del text del missatge.

---

## Activitat 3 · Repte «control remot bàsic» (producte)

Parteix de [`receptor_vehicle.py`](codi/receptor_vehicle/receptor_vehicle.py) i tanca el teu vehicle controlat per ràdio.

**Codi (o descripció de com l'has fet):**

```python

```

**Mini-defensa:** anota aquí la **decisió** que explicaràs (per exemple, per què aquestes comandes o com guardes l'historial):

___________________________________________________________________

---

## Si t'encalles

1. **Pista 1:** comprova **cada extrem per separat** — l'emissor envia realment el missatge (mostra'l al display abans d'enviar-lo)? El receptor rep algun missatge (mostra `radio.receive()` sencer abans de filtrar-lo pel prefix)?
2. **Pista 2:** revisa que el `GRUP` i el `PREFIX` coincideixin **exactament** (majúscules incloses) a les dues plaques.
3. **Pista 3:** aplica **DEPURA** i, si cal, demana ajuda **explicant què ja has provat**.

> **Rutina DEPURA:** **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara i torna a provar · **A**punta-ho al quadern.

## Vols més?

- **Reptes ⭐⭐/⭐⭐⭐:** tria'n un a [`Reptes/Reptes_SA5.md`](../../Reptes/Reptes_SA5.md) i amplia el teu producte (el ⭐ ja és nucli obligatori, fet a la fitxa base).
- **Simulador:** el de [python.microbit.org](https://python.microbit.org) **sí** simula la ràdio, però només **entre instàncies del simulador** (vegeu [`SA5_esquemes_connexions.md`](SA5_esquemes_connexions.md) §Simulació): és una bona via de pràctica individual a casa, encara que no reprodueixi el moviment real del vehicle.

---

## Pensament computacional d'aquesta SA

Avui has practicat la idea de **protocol**: un acord tancat sobre com s'escriuen els missatges perquè qui els rep els pugui interpretar sense ambigüitat. On més has vist "un acord tancat sobre com es comuniquen dues coses" (a la vida real o en altres sistemes que coneguis, per exemple un semàfor, un codi Morse, una trucada de telèfon)? ______________________

## Diana d'autoavaluació

Situa't (0-10):

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Configuro la ràdio (grup, enviar, rebre) | ☐ | ☐ | ☐ | ☐ |
| Dissenyo i documento un protocol de comandes propi | ☐ | ☐ | ☐ | ☐ |
| Connecto la recepció d'un missatge a una funció de moviment | ☐ | ☐ | ☐ | ☐ |

## Exit ticket (abans de marxar, Sessió 3)

1. Una cosa que he après avui: ______________________
2. Una cosa que encara no tinc clara: ______________________
3. On ho faria servir al món real: ______________________

## Context real i ODS

Telecomandaments de drons i cotxes teledirigits, protocols IoT domèstics (llums, endolls intel·ligents), telemetria de vehicles autònoms: tots fan servir el mateix esquema, un missatge curt interpretat segons un protocol tancat. **ODS 9** (indústria, innovació i infraestructura): els protocols de comunicació estandarditzats permeten que dispositius de fabricants diferents s'entenguin, igual que el prefix d'avui permet que el receptor sàpiga interpretar sense ambigüitat el que li arriba. Escriu un exemple propi: ______________________

---

## Quadern tècnic (entrada de la SA5)

> El quadern tècnic és el teu **diari de bord** de tot el curs. Segueix el **mètode de projecte**: *analitzar → dissenyar → programar/prototipar → provar → millorar.*

- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com ho vaig solucionar i què vaig millorar): ___________________________________________________
- **Quin error he tingut i com l'he resolt:** ___________________________
- **La meva taula de comandes** (comanda → acció).
- **Reflexió ètica** (fiabilitat de la comunicació sense fils): per què creus que no es pot garantir que un missatge de ràdio arribi sempre, i quines conseqüències tindria això en un robot real que hagués d'aturar-se per seguretat davant d'una ordre que no arriba:
  - ______________________________________________________
