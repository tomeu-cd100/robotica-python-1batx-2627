# 03 · Sabers i continguts

Els sabers s'organitzen en **sis blocs**, coherents amb el bloc *Automatització* i *Sistemes elèctrics i electrònics* de Tecnologia i Enginyeria I, i amb els sabers de programació textual del currículum. A diferència del curs germà (Arduino/C++), aquí **tot el codi és MicroPython** de principi a fi; la progressió no és de llenguatge a llenguatge sinó **interna a Python**: de les seqüències més simples fins a la integració de funcions, esdeveniments i estructures de dades.

## Bloc A · Fonaments de sistemes embeguts i metodologia
- Concepte de robot i de sistema embegut. Història i tipologies de robots.
- Arquitectura de la micro:bit V2: CPU, memòria, pins d'E/S, alimentació.
- Senyal analògic vs digital. Nivells lògics. Conceptes de tensió, corrent i resistència aplicats.
- Metodologia de projecte tecnològic: design thinking, prototipatge, iteració, treball **individual**.
- Seguretat elèctrica i normes de treball al taller/laboratori.
- Entorns de treball: editor MicroPython (python.microbit.org), simulador.

## Bloc B · Programació en MicroPython — progressió I (seqüències, variables, bucles)
- Sintaxi de Python: indentació, comentaris, variables, tipus de dades bàsics.
- **Seqüències d'instruccions** (SA1): ordre, execució lineal, `sleep()`. Amb el mètode **PRIMM**, la SA1 ja introdueix `while True:` (perquè el programa no s'aturi) i un `if`/`elif`/`else` bàsic (reaccionar segons botons) com a primer contacte amb bucles i condicionals — es formalitzen i s'aprofundeixen a SA2 i SA3 respectivament.
- **Variables i bucles** (SA2): `for`, `while`, acumuladors, control de sortides repetitives (parpelleigs, tons, animacions a la matriu LED).
- Comunicació per USB i depuració (REPL / consola).

## Bloc C · Electrònica: sensors i actuadors (Micro:shield + Keyestudio)
- Sortides digitals i **PWM**: LED, matriu LED, so (piezo/altaveu), servos.
- Entrades digitals: polsadors, *pull-up/pull-down*, antirebot (*debounce*).
- Entrades analògiques: potenciòmetres, LDR, sensors de temperatura de la gamma Keyestudio.
- Actuadors de moviment: **servomotor**, **motor DC**, driver de motors del kit.
- Connexió, esquemes i simbologia normalitzada del Micro:shield.

## Bloc D · Programació en MicroPython — progressió II (condicionals, funcions)
- **Condicionals** (SA3): `if/elif/else` aplicats a la interpretació de senyals de sensors (aprofundeix el `if` bàsic ja vist a SA1).
- **Funcions** (SA4): **formalització** — definició, paràmetres, valors de retorn, modularitat, aplicades al control de moviment (servos/motors). L'alumnat ja n'ha **llegit** (sense escriure-les) a exemples i reptes ⭐⭐⭐ de SA1-SA3; a SA4 aprèn a escriure-les.
- Depuració sistemàtica i lectura d'errors del REPL.

## Bloc E · Sistemes de control i automatització
- Concepte de sistema de control. **Llaç obert vs llaç tancat**.
- Sensors com a realimentació. Senyal de consigna i error.
- **Comunicació per ràdio** entre plaques micro:bit: esdeveniments, missatges, protocols senzills (SA5).
- **Estructures de dades** bàsiques (llistes, tuples, diccionaris) per emmagatzemar lectures i estats (SA5-SA6).
- **Màquines d'estats finits** aplicades al control (SA6); ús de **classes ja creades** de la biblioteca de micro:bit (`Image`, `Sound`, objectes `microbit.*`) — **objectes només d'ús**, no es programa orientació a objectes pròpia.
- Regulació bàsica (tot/res). Introducció a l'estabilitat.

## Bloc F · Robòtica, tecnologies emergents i projecte (integració)
- Robòtica mòbil: xassís, rodes, **cinemàtica diferencial** aplicada al rover individual.
- Algorismes de comportament: seguidor de línia, evita-obstacles, navegació.
- Modelització i programació de **trajectòries**.
- **Telemetria i monitoratge** de dades per ràdio; introducció a la **IA** aplicada al control (classificació senzilla, reconeixement de patrons amb dades de sensors).
- Gestió de projecte individual, documentació tècnica i comunicació. Ètica i sostenibilitat (ODS).

---

## Distribució dels sabers per situació d'aprenentatge

| Bloc de sabers | SA principals | Progressió Python |
|---|---|---|
| A · Fonaments i metodologia | SA1 (i transversal) | Seqüències + `while True:`/`if` bàsic (PRIMM) |
| B · MicroPython I | SA2 | Variables i bucles |
| C · Sensors i actuadors | SA2, SA3, SA4 | — |
| D · MicroPython II | SA3, SA4 | Condicionals (aprofundiment), funcions (formalització a SA4; es llegeixen, sense escriure-les, a reptes ⭐⭐⭐ de SA1-SA3) |
| E · Control i automatització | SA5, SA6 (i SA4, SA7) | Esdeveniments, estructures de dades, objectes només d'ús |
| F · Robòtica, IoT/IA i projecte | SA7, SA8, SA9 | Integració |

> 🔑 **SA1 no és "només seqüència":** amb el mètode PRIMM, el primer repte de SA1 (`emocions_botons`) ja introdueix `while True:` i un `if`/`elif`/`else` bàsic; SA2 i SA3 els **aprofundeixen** (bucles amb acumuladors; condicionals aplicats a sensors), no els introdueixen de zero. De la mateixa manera, els reptes ⭐⭐⭐ de SA1-SA3 ja fan **llegir** funcions ja escrites (sense demanar que se n'escriguin): SA4 és on es formalitza **escriure** funcions pròpies.

> Els sabers es treballen **integrats en projectes individuals** (no com a temari aïllat), tal com demana l'enfocament competencial del Decret 171/2022.
