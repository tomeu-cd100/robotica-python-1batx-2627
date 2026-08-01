# SA5 · Guia docent — Ràdio: robots que parlen

**Durada:** 6 h (3 sessions de 2 h) · **Maquinari:** micro:bit V2 (ràdio integrada); vehicle T2 muntat a la SA4, usat com a receptor · **Llenguatge:** MicroPython
**Referència:** [`Programació didàctica/14_SA5_Radio_robots_que_parlen.md`](../../Programació%20didàctica/14_SA5_Radio_robots_que_parlen.md) · **Criteris:** CA1.1, CA1.2 · **Rúbriques:** R1, R4

> 🧭 **Com s'usa aquesta guia.** **Abans de la SA:** objectius, materials i assignació de grups de ràdio (la logística, al checklist docent). **A cada sessió:** la secció «SESSIÓ n» corresponent, amb el «Guió de modelatge» a mà. **En avaluar:** «Mapa d'avaluació». **Per contextualitzar:** context real i ODS.

## Objectius de la SA
1. Configurar la **ràdio** de la micro:bit (`radio.on()`, `radio.config(group=...)`) i enviar/rebre missatges de text entre dues plaques.
2. Dissenyar un **protocol de missatges** propi (comandes curtes amb prefix) per controlar el vehicle a distància.
3. Emmagatzemar comandes o missatges rebuts en **llistes** o **tuples** bàsiques.
4. Relacionar la recepció d'un missatge amb una funció de moviment ja creada a la SA4 (esdeveniment → acció).

## Materials per a la sessió
- 1 micro:bit V2 + 1 Micro:shield per alumne/a + cable micro-USB (dotació individual, vegeu [`09c_Inventari_kits_disponibles.md`](../../Programació%20didàctica/09c_Inventari_kits_disponibles.md)).
- El **vehicle T2** muntat a la SA4 (S4), portat per l'alumnat; portapiles carregades.
- Ordinadors amb accés a **python.microbit.org**. Projector. Quadern tècnic (digital).
- Cap component nou: la ràdio és **interna** a la micro:bit V2, no necessita cablatge.

## Documents de la SA (aquesta carpeta)
| Document | Quan s'usa |
|---|---|
| [`SA5_fitxa_alumnat.md`](SA5_fitxa_alumnat.md) | Totes les sessions (Activitats 1-3 + producte + quadern). |
| [`SA5_esquemes_connexions.md`](SA5_esquemes_connexions.md) | Sessions 1-3 (configuració de ràdio i pins reutilitzats del vehicle). |
| `codi/` | `radio_missatges`, `comandament` i el repte-producte `receptor_vehicle`. |
| [`Reptes_SA5.md`](../../Reptes/Reptes_SA5.md) | Sessió 3, en acabar el producte: repte **⭐** (nucli obligatori, mateix temps de pràctica que ja hi havia). Reptes ⭐⭐/⭐⭐⭐, ampliació opcional. |

> Cada programa de `codi/` té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs, l'`EXPLICACIO.md` de la seva carpeta). El «Guió de modelatge» oral de sota continua sent teu.

---

## Assignació de grups de ràdio

> 🔑 **Regla vinculant (fitxa 14).** El codi i el producte de cada alumne són **sempre individuals**. Provar la ràdio necessita dues plaques, així que l'emparellament és **puntual i només de banc de proves**: cada alumne carrega el **seu propi programa** a la **seva pròpia placa** i s'aparella momentàniament amb un company només per verificar l'enviament/recepció.

Assigna els **grups de ràdio per parelles de números de llista** (rotant si el nombre d'alumnes és senar o si cal repetir l'emparellament una altra sessió), per evitar interferències entre totes les plaques de l'aula. Exemple per a 20 alumnes:

| Grup (`radio.config(group=N)`) | Números de llista aparellats |
|---|---|
| 1 | 1, 2 |
| 2 | 3, 4 |
| 3 | 5, 6 |
| ... | ... |
| 10 | 19, 20 |

- Escriu aquesta taula a la pissarra o comparteix-la digitalment **abans** de la Sessió 1; cada alumne hi busca el seu grup.
- Si cal rotar parelles a la Sessió 3 (per exemple, perquè un company ha faltat), assigna un grup nou i anota-ho: el `GRUP` és una simple constant al capçal del programa, es canvia en 5 segons.
- Recorda-ho a cada sessió: **el grup és només per a la prova**; el codi que s'avalua és el de cadascú.

---

## SESSIÓ 1 (2 h) — Xat per ràdio: enviar i rebre missatges

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Pregunta del repte inicial: *"com envies una ordre a un robot sense fils, i com fas perquè no es 'perdi' cap missatge?"* Reparteix la taula de grups de ràdio. 🥋 **Kata del dia:** K08 (return) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Formulen hipòtesis: com es "sentirien" dues plaques sense fil físic? |
| Explicació | 30' | `radio.on()`, `radio.config(group=N, power=...)` i per què el `group` evita interferències entre 20 plaques a la vegada. Introdueix `radio.send()`/`radio.receive()` i que **`receive()` no espera**: torna `None` si no ha arribat res. | Prenen notes; identifiquen per què cal cridar `receive()` dins d'un bucle. |
| Pràctica | 50' | Modelatge de [`radio_missatges.py`](codi/radio_missatges/radio_missatges.py): enviar amb remitent (`MEU_NOM + ":" + text`), guardar els missatges rebuts en una **llista** (`historic`, xat "5×5"). | Escriuen el **seu propi** codi d'emissor i de receptor; s'aparellen **puntualment** (banc de proves) amb la placa d'un company (mateix grup de la taula) i intercanvien breument el rol d'emissor/receptor. Fan l'Activitat 1 de la fitxa. |
| Activitat nucli · `for` sobre col·lecció | 10' | Modelatge de `mostra_historic()` (A+B): `for missatge in historic:` recorre els **elements** de la llista directament (no `range(len(historic))`). És el primer `for` del curs sobre una col·lecció (fins ara, `for` sempre amb `range`, SA2). | Proven `mostra_historic()` amb 3-4 missatges enviats; identifiquen la diferència amb el `for i in range(...)` de la SA2. |
| Tancament | 20' | Recull dubtes; anticipa el protocol de comandes de la Sessió 2. | Entrada del quadern: què és el `group`, com es guarda un missatge a una llista. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: l'**intercanvi de rols** emissor/receptor (deixa que cadascú provi només el seu; l'intercanvi complet reapareix igualment a la Sessió 2 amb comandament/receptor separats).

**Punts clau:** la **ràdio** de la micro:bit V2 permet enviar i rebre text pla entre plaques properes; el **grup** (`radio.config(group=N)`) és com un "canal" que separa parelles diferents perquè no es sentin entre elles; `radio.receive()` **no bloqueja**: cal cridar-lo repetidament dins del bucle principal per no perdre cap missatge. `for missatge in historic:` recorre els **elements** de la llista directament: és el mateix `for` de la SA2, ara sense `range`.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| No rep mai res | Grups diferents a les dues plaques, o oblit de `radio.on()` en alguna | Comprovar que totes dues cridin `radio.on()` i tinguin el mateix `GRUP`. |
| Rep missatges d'una parella veïna | Coincidència de número de grup amb una altra parella de la classe | Consultar la taula de grups; canviar-ne un si cal. |
| El simulador no es "sent" amb la placa física | El simulador de ràdio només funciona **entre instàncies del simulador**, mai amb maquinari real | Explicar-ho com a limitació coneguda (vegeu §Simulació als esquemes). |

---

## SESSIÓ 2 (2 h) — Dissenyar un protocol de comandes

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Recorda el xat lliure de la S1; pregunta: *"com distingiries una ORDRE d'un missatge qualsevol si les dues coses viatgen igual, com a text?"* 🥋 **Kata del dia:** K21 (funcions/paràmetres) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Formulen hipòtesis: un prefix, una paraula clau... |
| Explicació | 25' | Introdueix la idea de **protocol**: prefix fix (`"CMD:"`) + una ordre curta d'una lletra (`F`/`B`/`L`/`R`/`S`). Modelatge de [`comandament.py`](codi/comandament/comandament.py): botons A/B/A+B i gestos (`accelerometer.was_gesture(...)`) com a entrades diferents que envien el **mateix** protocol de sortida. | Prenen notes; dissenyen la seva pròpia llista de 4-5 comandes (poden reutilitzar F/B/L/R/S o triar-ne d'altres). |
| Pràctica | 55' | Acompanya la connexió amb les funcions de moviment de la SA4 (`avancar`/`retrocedir`/`girar`/`aturar`): la recepció crida la funció que toca segons el missatge rebut. Primeres proves amb el propi vehicle com a receptor, aparellat puntualment amb la placa d'un company o del docent com a emissor de proves. | Programen `comandament.py` (emissor) i comencen `receptor_vehicle.py` (receptor); proven l'aparellament (el codi que s'avalua és sempre el propi). Fan l'Activitat 2 de la fitxa. |
| Mini-check + Tancament | 30' | **Mini-check individual** (10', enviar/rebre un missatge i actuar-hi sense apunts; banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md)). Recull dubtes. | Fan el mini-check (no qualifica); documenten el protocol al quadern (taula comanda → acció). |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: els **gestos** de `comandament.py` (deixa només els botons A/B/A+B; els gestos reapareixen igualment com a ampliació ⭐).

**Punts clau:** un **protocol** és un acord tancat sobre com s'escriuen els missatges perquè qui els rep sàpiga interpretar-los sense ambigüitat; un **prefix** (`"CMD:"`) permet distingir les ordres d'un altre trànsit de ràdio; la combinació de botons (A+B) es comprova **abans** que els botons per separat perquè tingui prioritat (com el botó B a `control_per_botons.py`, SA4).

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El receptor no reacciona a res | El `PREFIX` no coincideix exactament (majúscules, dos punts) entre comandament i receptor | Copiar el `PREFIX` literalment, no reescriure'l a mà a l'altra placa. |
| A+B mai s'envia | Es comprova `was_pressed()` de cada botó abans que la combinació `is_pressed()` de tots dos | Comprovar primer la combinació, després cada botó per separat. |
| Els gestos s'envien més d'un cop seguit | Gest llarg detectat diverses vegades | No és greu al protocol (repetir "S" és segur); comentar-ho com a característica, no error. |

---

## SESSIÓ 3 (2 h) — Repte «control remot bàsic» (producte de la SA)

> 🎯 **Producte de la SA.** Aquest repte **fa de producte** de la SA5: s'avalua amb **R1** (codi, criteri "Funcionament") i **R4** (documentació). Introdueix, com a **+ampliació**, l'historial de comandes amb llistes/tuples (es completa a la SA6).
>
> 🤝 **Parella de lectura (5')** abans de lliurar — vegeu `Classes/00_General/00_Parella_de_lectura.md`.

> ⭐ **Repte nucli obligatori.** Un cop tancat el producte, tothom fa el repte **⭐** de [`Reptes_SA5.md`](../../Reptes/Reptes_SA5.md) (xat de classe amb identificació), aprofitant el mateix temps de pràctica que abans es destinava opcionalment a l'ampliació, i l'ensenya al docent perquè el validi. Els reptes **⭐⭐/⭐⭐⭐** continuen sent ampliació opcional per a qui vagi sobrat.

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Mostra [`receptor_vehicle.py`](codi/receptor_vehicle/receptor_vehicle.py) **sense executar-lo** (PRIMM): pregunta què farà cada ordre rebuda. 🥋 **Kata del dia:** K09 (global) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Prediuen el comportament del vehicle davant de cada comanda. |
| Explicació | 20' | Modelatge de la funció `actua(ordre)` (esdeveniment → acció) i de per què reutilitza **exactament** les funcions `avancar`/`retrocedir`/`girar`/`aturar` de la SA4 sense reescriure-les. Introdueix l'historial amb **tuples** (`(ordre, instant)`) com a estructura de dades nova. | Prenen notes; identifiquen quines parts del programa ja coneixien (funcions de moviment) i quines són noves (protocol per ràdio, tuples). |
| Repte | 70' | Acompanya el tancament individual del repte «control remot bàsic»: cadascú prova el **seu** receptor aparellat puntualment amb el comandament d'un company o del docent. | Tanquen `receptor_vehicle.py`, proven el vehicle amb ràdio real (Activitat 3, producte). |
| Tancament | 20' | Recull dubtes; mini-defensa breu de cada alumne/a. | Anoten al quadern el protocol final i un exemple de l'historial de comandes. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: l'**historial amb tuples** (deixa el receptor funcionant sense historial; les tuples reapareixen igualment a la SA6).

**Punts clau:** el vehicle **no aprèn cap funció de moviment nova**: només canvia l'**entrada** (ràdio en lloc de botons), el mateix esquema «esdeveniment → acció» de tot el curs; una **tupla** és una parella (o més) de valors relacionats que, a diferència d'una llista, no es pot modificar un cop creada — útil per registrar «què ha passat i quan» sense risc d'alterar-ho per error.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El vehicle no respon a cap ordre | Grup diferent, o el vehicle no rep alimentació externa (piles) | Revisar `GRUP` i l'alimentació del Micro:shield. |
| El vehicle "perd" alguna ordre de tant en tant | Normal en ràdio: no hi ha confirmació de recepció | Explicar-ho com a limitació coneguda; per això `S` es pot repetir sense problema. |
| El vehicle es mou sol, sense cap comandament proper | Un altre grup de la classe fa servir el mateix número | Reassignar el `GRUP` seguint la taula. |

---

**Producte de la SA:** repte «control remot bàsic» (vehicle controlat a distància per ràdio amb un protocol de comandes propi, mínim 4 comandes, i registre de comandes rebudes al quadern tècnic), tancat i avaluat a la **S3**. Mini-defensa breu (1-2') del repte (R4·DO).

### Mapa d'avaluació (traçabilitat)

| Instrument | Què evidencia | Criteri | Rúbrica | Qualifica? |
|---|---|---|---|---|
| Mini-check (S2) | Enviar/rebre un missatge i actuar-hi sense apunts | CA1.1, CA1.2 | — | **No** (radar formatiu) |
| Fitxa d'alumnat (Act. 1-2) | Ràdio (`radio.on`/`config`/`send`/`receive`); disseny del protocol propi | CA1.1, CA1.2 | R1 | Formativa |
| Repte «control remot bàsic» (S3, producte) | Vehicle controlat per ràdio amb protocol propi (mínim 4 comandes) | CA1.1, CA1.2 | **R1** | Sí |
| Repte **⭐** (`Reptes_SA5.md`, S3, nucli obligatori) | Xat de classe amb identificació i historial, validat pel docent | CA1.1 | **R1** | Sí |
| Mini-defensa (S3, R4·DO) | Claredat + justificació del protocol triat | CA1.2 | **R4** (fila «Defensa oral») | Sí |
| Quadern tècnic | Documentació, taula comanda → acció, historial de comandes | CA1.2 | **R4** | Sí |
| Observació d'aula | Autonomia i respecte de la regla d'individualitat de la ràdio | — | **R5** | Sí |

*(CA1.1 = escriure i depurar programes MicroPython amb estructures de control, funcions i biblioteques (ara, també `radio`), comentant el codi; CA1.2 = utilitzar el simulador i el REPL per experimentar i corregir programes de manera autònoma. Vegeu [`Programació didàctica/06_Avaluacio_criteris_qualificacio.md`](../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md).)*

### Quadern tècnic — entrada de la SA5 (guia per a l'alumnat)

Segueix el mètode de projecte:
- **Què he après** (ràdio, `group`, protocol amb prefix, esdeveniment → acció, llistes/tuples).
- **El repte i com l'he resolt** (predicció → protocol → recepció → moviment).
- **Un error que he tingut i com l'he resolt.**
- **Taula del meu protocol:** comanda → acció.

> Comparteix les rúbriques **R1** i **R4** amb l'alumnat **abans** de començar el repte (avaluació formativa).

### Pont cap a la SA6

A la SA5 hem après a fer que dues plaques **es parlin** per ràdio amb un protocol propi, i hem activat les funcions de moviment del vehicle amb comandes remotes. A la **SA6** el vehicle deixarà de respondre a ordres puntuals per passar a un **llaç de control** (esdeveniments encadenats, histèresi): el mateix esquema «entrada → acció», ara amb una lògica de control més elaborada i les llistes/tuples aprofundides.

---

## Guió de modelatge (què verbalitzar)

- **S1 · Per què el grup:** pregunta *"si totes les plaques de la classe fessin servir el mateix número de grup, què passaria quan 20 persones enviessin missatges alhora?"* — porta la resposta cap al fet que el `group` és el que evita que 20 plaques es "sentin" totes entre elles. *Error a anticipar:* pensar que `radio.send()` només l'escolta la placa "destinatària" (en realitat l'escolten totes les del mateix grup).
- **S2 · Per què un prefix:** pregunta *"si aquesta placa rebés per error un missatge del xat de S1 d'una altra parella, què passaria si el receptor no comprovés el prefix?"* — porta la resposta cap al fet que sense protocol, qualsevol text es podria interpretar (per error) com una ordre.
- **S3 · Mateixa funció, entrada diferent:** ensenya costat a costat `control_per_botons.py` (SA4) i `receptor_vehicle.py` (SA5): pregunta *"què ha canviat i què s'ha mantingut igual?"* — porta la resposta cap al fet que `avancar()`/`girar()`/`aturar()` són **exactament** les mateixes, només canvia com arriba l'ordre.

## Atenció a la diversitat

| Necessitat | Mesura |
|---|---|
| **Bastida (qui ho necessita)** | Protocol de comandes model (taula comanda → acció) proporcionat; funció `rep_i_actua()`/`actua()` amb l'esquelet ja escrit. |
| **+ Ampliació (qui va sobrat)** | Un cop fet el repte ⭐ obligatori: reptes **⭐⭐/⭐⭐⭐** (comandament amb gestos, historial amb estadístiques) — vegeu [Reptes de la SA5](../../Reptes/Reptes_SA5.md). |
| **Diversitat lingüística/lectora** | Taula de comandes amb icones de direcció; glossari a [`00_Glossari_tecnic.md`](../00_General/00_Glossari_tecnic.md). |
| **Sense segona placa disponible** | El docent pot fer d'emissor de proves per torns; el simulador de python.microbit.org **sí** simula la ràdio entre instàncies del simulador (pràctica individual a casa). |

> **Avaluació formativa:** comparteix les rúbriques **R1** i **R4** amb l'alumnat **abans** de començar el repte.

## Pensament computacional i depuració

- **Concepte de PC d'aquesta SA:** **descomposició i protocols**: dividir la comunicació en «qui envia», «què s'envia» i «qui ho interpreta» és el mateix principi que fan servir tots els protocols de xarxa reals (des d'un xat fins a Internet), aquí reduït a la seva mínima expressió (un prefix + una lletra).
- **Depuració:** continua la rutina **DEPURA** (SA1-SA4), amb un èmfasi nou: quan un missatge "no arriba", comprova per separat **cada extrem** (l'emissor envia realment el que creus? el receptor rep realment algun missatge, encara que no faci res amb ell?) abans de sospitar del protocol sencer.

## Context real i ODS

- **Context:** telecomandaments de drons i cotxes teledirigits, telemetria de vehicles autònoms, protocols IoT domèstics (llums, endolls intel·ligents) que fan servir exactament el mateix esquema: missatge curt + protocol tancat.
- **ODS 9** (indústria, innovació i infraestructura): els protocols de comunicació estandarditzats són el que permet que dispositius de fabricants diferents es puguin "entendre", igual que el prefix d'avui permet que el receptor sàpiga interpretar sense ambigüitat el que li arriba.
