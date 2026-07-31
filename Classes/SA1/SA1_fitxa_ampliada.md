# SA1 · Fitxa ampliada (aprofundiment) — Hola, robot!

> 📄 **Versió ampliada**: conté totes les activitats i les rutines d'aprofundiment (pensament computacional, diana, exit ticket, ODS…). La fitxa que fa **tot l'alumnat** és la base: **[SA1_fitxa_alumnat.md](SA1_fitxa_alumnat.md)**.

> 🧑‍🎓 **Quan toca obrir-la?** És **opcional**: quan portis la **fitxa base al dia** i vulguis més (ampliació de codi, pensament computacional, ODS). Algunes rutines (exit ticket) les activarà el **docent** a l'aula quan toqui.

> 🗺️ **Quan s'usa cada apartat:** les **Activitats 1-4** segueixen les mateixes sessions que la fitxa base (aquí amb l'ampliació de codi) · **Si t'encalles** i **Pensament computacional**: durant el treball · **Vols més?**: amb el nucli al dia · **Exit ticket**: els últims 2' de la sessió 3 · **Diana** i **Quadern tècnic**: en tancar la SA · **Context real i ODS**: quan el docent l'activi.

**Nom:** ______________________  **Data:** __________

> En aquesta unitat descobriràs què és un robot i un sistema embegut, coneixeràs la placa micro:bit i faràs el teu primer programa. Tot el treball és **individual**.

---

## Activitat 1 · Entrada – Procés – Sortida

Analitza aquests tres sistemes i completa la taula. Pensa: què *percep* (entrada), què *decideix* (procés) i què *fa* (sortida).

| Sistema | Entrada (sensors) | Procés (decisió) | Sortida (actuadors) |
|---|---|---|---|
| Rentadora | | | |
| Dron | | | |
| Semàfor | | | |

**+ Repte:** afegeix un quart sistema del teu entorn: ______________________

---

## Activitat 2 · La placa micro:bit

Etiqueta aquestes parts a l'esquema de la placa ([`SA1_esquemes_connexions.md`](SA1_esquemes_connexions.md)):
- [ ] Microcontrolador  - [ ] Matriu de 25 LED  - [ ] Botons A i B
- [ ] Pins d'expansió (0, 1, 2...)  - [ ] Connector USB  - [ ] Sensors interns (acceleròmetre, brúixola, llum, temperatura)

**Pregunta:** Quina diferència hi ha entre un senyal **digital** i un d'**analògic**? Posa'n un exemple de cada.

___________________________________________________________________

> **Pista:** *digital* = només dos estats (per exemple, un botó premut/no premut); *analògic* = molts valors (com el nivell de llum, 0-255).

---

## Activitat 3 · Normes de seguretat

Llegeix les normes ([`SA1_normes_seguretat.md`](SA1_normes_seguretat.md)) i **signa** el full. Escriu aquí les 2 normes que et semblen més importants:

1. ___________________________________________________________________
2. ___________________________________________________________________

---

## Activitat 4 · El teu primer programa

**0. PREDIU (abans d'executar res).** Mira el codi de `hola_mon.py` projectat i, **sense executar-lo encara**, escriu què creus que farà el display:

___________________________________________________________________

> Després l'executarem i comprovaràs si ho havies encertat. Predir abans de provar és el que fa un bon equip d'enginyeria!

1. **Investiga.** Obre `hola_mon.py` i identifica les parts:
   - Per què cal `from microbit import *` a la primera línia? _______________________________________
   - Què fa `display.scroll(...)`? ________________________________________
   - Què fa `display.show(...)`? ______________________________________

2. **Modifica** el text i la imatge del programa. Què has posat? ______

3. **Crea (`emocions_botons.py`):** fes que el botó A mostri una cara contenta i el botó B una cara trista. Enganxa aquí el teu codi o descriu com ho has fet:

```python

```

> **+ Ampliació (opcional):** obre `dau_sacseig.py` (sacseja la placa i mostra un nombre a l'atzar amb l'acceleròmetre). Quin sensor detecta el sacseig? ________________________________________

---

## Producte de la SA · Fitxa-pòster

Tria un **robot real** i analitza'l amb la plantilla [`SA1_poster_robot_plantilla.md`](SA1_poster_robot_plantilla.md) (entrada-procés-sortida + dilema ètic). S'avalua amb la rúbrica **R4**.

---

## Si t'encalles

1. **Pista 1:** torna a llegir l'enunciat i digues en veu alta què ha de fer el sistema (entrada → procés → sortida).
2. **Pista 2:** compara el teu codi amb l'esquema del programa model; revisa línia a línia.
3. **Pista 3:** aplica la **rutina DEPURA** i, si cal, demana ajuda **explicant què ja has provat**.

> **Rutina DEPURA** (quan no funciona): **D**escriu (què esperaves vs què passa) · **E**xamina (display, missatge d'error) · **P**rova una hipòtesi cada cop (canvia una sola cosa) · **U**bica el problema (aïlla'l) · **R**epara i torna a provar · **A**punta-ho al quadern.

## Vols més?

- **Reptes ⭐:** tria'n un a [`Reptes/Reptes_SA1.md`](../../Reptes/Reptes_SA1.md) i amplia el teu producte.
- **Simulador:** prova-ho sense maquinari a [python.microbit.org](https://python.microbit.org) (vegeu [`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md)).

---

## Pensament computacional d'aquesta SA

Avui has practicat la **DESCOMPOSICIÓ**: partir un sistema complex en parts senzilles (entrada → procés → sortida). On l'has fet servir? ______________________

## Diana d'autoavaluació

Situa't (0-10):

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Identifico entrada-procés-sortida d'un sistema | ☐ | ☐ | ☐ | ☐ |
| Reconec les parts de la placa i distingeixo digital/analògic | ☐ | ☐ | ☐ | ☐ |
| Llegeixo i modifico codi MicroPython senzill | ☐ | ☐ | ☐ | ☐ |

## Exit ticket (abans de marxar)

1. Una cosa que he après avui: ______________________
2. Una cosa que encara no tinc clara: ______________________
3. On ho faria servir al món real: ______________________

## Context real i ODS

La robòtica és a tot arreu: electrodomèstics, transport, indústria. **ODS 9** (indústria i innovació) i **ODS 12** (consum responsable). Escriu un **benefici** i un **risc** d'automatitzar una tasca quotidiana: ______________________

---

## Quadern tècnic (entrada de la SA1)

> El quadern tècnic és el teu **diari de bord** de tot el curs. Segueix el **mètode de projecte**: *analitzar → dissenyar → programar/prototipar → provar → millorar.*

- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com ho vaig solucionar i què vaig millorar): ___________________________________________________
- **Quin error he tingut i com l'he resolt:** ___________________________
- **Reflexió ètica** (automatització i ODS): un avantatge i un risc de l'automatització:
  - Avantatge: ______________________________________________________
  - Risc: ___________________________________________________________
