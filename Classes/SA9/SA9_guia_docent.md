# SA9 · Guia docent — Repte final integrador

**Durada:** 10 h (5 sessions de 2 h; S5 = Prova pràctica T3) · **Maquinari:** tot el maquinari del curs (micro:bit V2 + Micro:shield, Kits Keyestudio 1-3, rover de SA7-SA8); reserva d'humitat del terra (Kit 2) i bomba d'aigua/relé (Kit 3) · **Llenguatge:** MicroPython
**Referència:** [`Programació didàctica/18_SA9_Repte_final_integrador.md`](../../Programació%20didàctica/18_SA9_Repte_final_integrador.md) · **Criteris:** CA1.1, CA1.2, CA2.1, CA2.2, CA3.1, CA4.1, CA4.2, CA5.1, CA5.2, CA5.3 · **Rúbriques:** R1, R2, R3, R4, R5 (totes)

> 🧭 **Com s'usa aquesta guia.** **Abans de la SA:** objectius, materials i logística (la llista, al checklist docent). **A cada sessió:** la secció «SESSIÓ n» corresponent, amb el «Guió de modelatge» a mà. **En avaluar:** «Mapa d'avaluació». Per organitzar defenses/estacions: §Defenses esglaonades i §Organització de la S5.

## ⚠️ Divergències amb el brief d'aquesta tasca (mana la fitxa 18)

- **Sense `Reptes/Reptes_SA9.md`.** El brief d'aquesta tasca ja ho anticipa i la fitxa 18 ho confirma implícitament: a la SA9 **el projecte ÉS el repte** (no n'hi ha un altre de separat), igual que el curs germà acaba a `Reptes_SA8`. El contracte real de `tools/qa.py:comprova_cobertura_sa()` només exigeix `Reptes/Reptes_SAn.md` i `Reptes/Solucionari/SAn/` per a **n ≤ 8**: SA9 en queda exempta sense necessitat de tocar el contracte. En comptes d'això, es crea [`SA9_reptes_proposats.md`](SA9_reptes_proposats.md) (banc de 6 reptes lliures, dins de `Classes/SA9/`) com a substitut natural: la "S1 · Idear" de la fitxa 18 consisteix precisament a **triar** un d'aquests reptes.
- **`SA9_questionari_conceptes.md` i `SA9_exemple_resolt.md` SÍ que calen.** El brief d'aquesta tasca no els llistava explícitament, però el mateix contracte `comprova_cobertura_sa()` els exigeix per a **totes** les SA (bucle `range(1, 10)`, sense excepció per SA9). Es crea contingut adaptat a la naturalesa de projecte (qüestionari: mètode de projecte, integració i ètica/ODS en lloc d'un sensor concret; exemple resolt: un mini-projecte anàleg complet, no un fragment de codi) en lloc d'ajustar el contracte: és el canvi de **menys distorsió** (afegir 2 fitxers previstos genèricament pel contracte) davant l'alternativa de tocar `qa.py` per crear una excepció nova.
- **Sense esquemes/connexions dedicat.** El contracte també exempta SA9 de `SAn_esquemes_connexions.md` (només n ≤ 8): coherent amb el fet que el maquinari nou de cada repte és **triat per l'alumnat** (no hi ha un cablatge únic de SA), i cada repte del banc ja porta el seu propi esquema de components.
- **Curs germà organitzat en equips; aquest curs és individual.** El curs germà (Arduino) estructura la SA9 amb rols d'equip rotatius. Aquest curs és **individual durant tot el curs** (`04_Metodologia.md` §4.3): l'estructura de sessions (Idear/Prototipar/Provar i millorar/Comunicar/Prova T3) es manté, però sense equips ni rols — cada alumne fa tot el cicle sol.
- **`07_Rubriques.md` diu "SA9 S4-S5" a la taula de progressió de la R4·DO; la fitxa 18 mana.** La fitxa 18 és taxativa: el producte **es tanca a la S4** (dossier + defensa) i la **S5 és, sencera, la prova pràctica T3**, "independent del producte" i que "no reavalua el projecte". S'interpreta "S4-S5" de `07_Rubriques.md` com a referència laxa a l'**esglaonament** de les defenses (que poden començar ja a S3, segons `00_Guia_defensa_oral.md`), **mai** com una defensa que envaeixi la S5: cap activitat de projecte no competeix amb la prova pràctica (mateix principi que ja regia SA3/SA6 amb T1/T2, doc. 08).

## Objectius de la SA
1. Gestionar, individualment, un **projecte** complet (anàlisi → prototip → proves → millora) amb metodologia de disseny.
2. **Integrar** electrònica, programació, control, robòtica mòbil i telemetria en una solució coherent i pròpia.
3. Elaborar un **dossier tècnic** complet i fer-ne una **defensa oral individual**.
4. Valorar l'impacte ètic, social i ambiental de la solució pròpia (ODS) i treballar amb autonomia i responsabilitat.

## Materials per a la sessió
- 1 micro:bit V2 + 1 Micro:shield per alumne/a + cable micro-USB (dotació individual, vegeu [`09c_Inventari_kits_disponibles.md`](../../Programació%20didàctica/09c_Inventari_kits_disponibles.md)).
- El **rover T3** de SA7-SA8, portat per l'alumnat; portapiles carregades.
- **Kits Keyestudio 1-3 complets** de cada alumne (el repte triat determina quins components concrets es fan servir; vegeu [`SA9_reptes_proposats.md`](SA9_reptes_proposats.md)).
- Material de reserva específic: **sensor d'humitat del terra** (Kit 2) i **bomba d'aigua + relé** (Kit 3), per a qui triï el repte de reg/domòtica; comprova l'estanquitat del tub abans de la S1.
- Ordinadors amb accés a **python.microbit.org** i, per a qui ampliï amb IA, **Teachable Machine**. Projector. Quadern tècnic / dossier (digital).
- **Pistes muntades per a la S5** (prova pràctica T3, per estacions): vegeu §Organització de la S5.

## Documents de la SA (aquesta carpeta)
| Document | Quan s'usa |
|---|---|
| [`SA9_fitxa_alumnat.md`](SA9_fitxa_alumnat.md) | Totes les sessions de projecte (S1-S4). |
| [`SA9_reptes_proposats.md`](SA9_reptes_proposats.md) | Sessió 1 (triar repte) i com a referència tota la SA. |
| [`SA9_dossier_plantilla.md`](SA9_dossier_plantilla.md) | Sessions 3-4 (avançar i tancar el dossier). |
| `codi/plantilla_projecte/` | Sessió 2 (punt de partida del prototip). |

> Cada repte del banc cita quin codi de SA1-SA8 reutilitza. El «Guió de modelatge» oral de sota continua sent teu.

---

## Defenses esglaonades (S3-S4)

Amb 15-20 alumnes, una sola sessió de defenses no dona: 5' + preguntes + canvi de muntatge ≈ 10-12' per alumne (60 min per a només 5-6 alumnes). Per això, **com preveu la fitxa 18**:

- **Des de la S3 (Provar i millorar):** qui ja tingui el prototip llest pot defensar avançat. Reserva'n els últims **20-30'** de la S3 per a les primeres 4-6 defenses.
- **A la S4 (Comunicar):** la resta de l'alumnat defensa, repartida al llarg de la sessió mentre la resta acaba de tancar el dossier o observa (coavaluació, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md) §El públic també treballa).
- **Mai a la S5:** cap defensa no s'ajorna a la S5 (prova pràctica T3): és un instrument separat i no hi ha temps (vegeu §Organització de la S5).

## Organització de la S5 (prova pràctica T3, per estacions rotatives)

**No és sessió de projecte.** És, sencera, la prova pràctica individual del 3r trimestre (SA7-SA8), independent del producte de la SA9.

- **Estructura per estacions:** part de **programació a la taula** (individual, sense apunts, sobre paper o REPL) + part de **rover per torns** a les pistes disponibles (línia, obstacles, com a SA7).
- **Torns:** amb el nombre de pistes disponibles al taller, organitza grups petits que roten **contínuament** cada 8-10 minuts entre "taula" i "pista" (des del minut 0 de la sessió, no en dues fases seqüencials), perquè ningú esperi sense fer res. Aritmètica de referència (20 alumnes, ~100' efectius, mínim de pistes): [`Avaluació/Prova_practica_T3.md`](../../Avaluació/Prova_practica_T3.md) §Logística.
- **Repàs previ (deures de la S4):** "Python flash" de ràdio (5') + targetes de repàs espaiat, perquè l'alumnat arribi a la S5 amb els conceptes de SA7-SA8 frescos.
- **Enunciat complet:** [`Avaluació/Prova_practica_T3.md`](../../Avaluació/Prova_practica_T3.md).

---

## SESSIÓ 1 (2 h) — Idear

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Repte inicial: *"Quin problema real i senzill del teu entorn pots resoldre ampliant el teu rover?"* Recorda el mètode de disseny (represa de SA1). 🥋 **Kata del dia:** K17 (return) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Formulen hipòtesis sobre possibles reptes. |
| Explicació | 20' | Presenta el [banc de reptes](SA9_reptes_proposats.md) (6 reptes, ⭐/⭐⭐/⭐⭐⭐) i el maquinari de reserva (bomba+relé, PIR, NeoPixel). Explica que **el repte és el projecte**: no hi ha un repte "extra" després. | Escolten i comparen reptes; identifiquen quin maquinari de `09c` ja tenen muntat i quin els caldria afegir. |
| Pràctica | 60' | Acompanya la tria individual del repte i la definició dels **requisits mínims**; ronda per taules resolent dubtes de viabilitat (maquinari disponible, temps). | Trien repte (Activitat 1 de la fitxa), en defineixen els requisits mínims i fan un esbós de la solució; comencen la planificació per sessió. |
| Tancament | 30' | Recull els reptes triats (assegura't que hi ha diversitat i que ningú s'ha quedat sense repte viable); anticipa la S2. | Acaben l'esbós i la planificació si no ho han fet; entrada del quadern: repte triat + requisits. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: deixa la planificació detallada per sessió com a **deures** i centra el temps de classe en la tria del repte i els requisits mínims.

**Punts clau:** aquesta SA no introdueix maquinari nou de manera obligatòria per a tothom (a diferència de SA1-SA8): cadascú tria **quin** component nou afegeix segons el seu repte. El paper del docent és més de **facilitador de disseny** que de modelador de codi.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| L'alumne tria un repte massa ambiciós per al temps disponible (4 sessions) | No distingeix "nucli ⭐" d'"ampliació ⭐⭐⭐" | Recorda que el nucli ⭐ de cada repte és sempre assolible en el temps donat; les ampliacions són per a qui vagi sobrat |
| L'alumne no sap triar entre dos reptes | Indecisió normal a l'inici d'un projecte obert | Pregunta: "quin maquinari ja tens muntat i funcionant del teu rover?" — el que ja tens fet redueix el risc |
| Els requisits mínims són massa vagues ("que funcioni bé") | Encara no ha après a fer requisits observables | Recorda l'exemple del [banc de reptes](SA9_reptes_proposats.md): un requisit és una frase que es pot marcar "fet" o "no fet" |

---

## SESSIÓ 2 (2 h) — Prototipar

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Explicació | 20' | Modelatge de [`plantilla_projecte.py`](codi/plantilla_projecte/EXPLICACIO.md): l'arquitectura percep/decideix/actua, i com copiar-hi funcions ja fetes de SA1-SA8 (motors, sensors, ràdio). | Prenen notes; identifiquen quines funcions pròpies (de fitxers anteriors) poden reutilitzar sense reescriure-les. |
| Pràctica | 80' | Acompanya el muntatge del component nou de cada repte (ronda per taules: reg necessita atenció al relé/bomba, PIR i NeoPixel necessiten cablatge nou) i la primera integració de codi. | Munten el maquinari nou del seu repte i programen un **prototip mínim viable**: almenys un element nou integrat sobre el que ja tenien (Activitat 2 de la fitxa). |
| Tancament | 20' | Recull dubtes de maquinari abans de la S3; anticipa que la S3 és de proves i millora. | Documenten al quadern quin component nou han integrat i com. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: deixa el modelatge de `plantilla_projecte.py` com a lectura prèvia (assignada a la S1) i centra el temps a l'aula en el muntatge i la programació.

**Punts clau:** com que cada alumne fa un repte diferent, aquesta sessió és la de **ronda més intensiva**: el docent no modela un únic programa a tota la classe, sinó que acompanya muntatges diferents en paral·lel. Anticipa quins reptes necessiten més atenció (reg i sentinella PIR: cablatge nou; missatger i estació ambiental: sobretot programació).

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El relé de la bomba no commuta | Bomba connectada directament al Micro:shield, sense passar pel relé | Revisar l'esquema del repte 1 a `SA9_reptes_proposats.md`: la bomba **sempre** a través del relé |
| El PIR o la NeoPixel "no fan res" | Pin equivocat o alimentació insuficient (NeoPixel necessita més corrent que un LED simple) | Revisar el pin triat i, si cal, alimentació externa per a la tira NeoPixel |
| El prototip barreja tota la lògica dins del `while True`, sense `percep()`/`decideix()`/`actua()` | Encara no ha interioritzat l'arquitectura de la plantilla | Recordar `comportaments.py` (SA8): separar lectura, decisió i acció fa el codi més fàcil de depurar |

---

## SESSIÓ 3 (2 h) — Provar i millorar

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Pràctica | 70' | Acompanya les proves sistemàtiques (rutina DEPURA) i la primera iteració de millora; ronda resolent errors de maquinari/codi. | Proven el sistema, identifiquen errors, fan una **iteració de millora** documentada; avancen el [dossier tècnic](SA9_dossier_plantilla.md) (§1-§3). |
| Defenses esglaonades | 20-30' | Escolta les defenses de qui ja té el prototip llest (vegeu §Defenses esglaonades); dona **preguntes** que la resta pugui aprofitar. | Qui està llest defensa (5' + preguntes); la resta observa i pren nota de preguntes útils per a la seva pròpia defensa. |
| Tancament | 10' | Recull dubtes; anticipa que la S4 tanca el dossier i la defensa. | Documenten al quadern les proves fetes i un error trobat/resolt. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: redueix les defenses esglaonades d'avui a 2-3 (les més llestes) i reparteix la resta a la S4.

**Punts clau:** distingeix explícitament una prova del **cas normal** d'una prova de **límit** (què passa si un sensor dona un valor extrem, o si el polsador STOP es prem enmig d'una acció): el dossier (§5) demana com a mínim una prova de límit.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| L'alumnat només prova el "cas feliç" | No ha interioritzat encara la diferència entre provar i validar | Preguntar: "què passa si el sensor es desconnecta a mitja prova?" |
| La "millora" documentada és només cosmètica (canviar un color) | Confon iteració amb retoc | Recordar la R3 (fila «Disseny i iteració»): una iteració és un canvi motivat per un problema real trobat en provar |
| Les primeres defenses esglaonades es fan sense preparació | Pressa per acabar abans que la resta | Recordar el guió de defensa (5 paraules clau, no un text llegit) |

---

## SESSIÓ 4 (2 h) — Comunicar

> 🎯 **Producte de la SA9.** Es tanca i s'avalua amb **totes** les rúbriques: **R1, R2, R3, R4 (nivell alt), R5**.

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Pràctica | 40' | Acompanya el tancament del [dossier tècnic](SA9_dossier_plantilla.md) (§4-§9: codi comentat, proves, dificultats, millores futures, conclusions, ètica/ODS). | Tanquen el dossier tècnic. |
| Defensa oral individual | 60' | Dirigeix les defenses (5' + preguntes cadascuna, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md)); modera el torn de preguntes de manera equilibrada (perspectiva coeducativa). | Fan la seva defensa oral individual amb demostració; qui no defensa encara, escolta i omple la coavaluació (2 estrelles i un desig). |
| Tancament | 20' | Recorda els deures de repàs per a la S5 (Python flash + targetes de repàs espaiat); recull dossiers. | Reben el repàs exprés (deures per a la T3); entrada final del quadern (reflexió, ètica/ODS). |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Amb grups nombrosos, la major part de la gestió del temps ja s'ha fet a la S3 (defenses esglaonades): si encara queden moltes defenses, prioritza-les sobre el tancament fi del dossier (es pot acabar de polir com a deures, sense penalitzar).

> 🔌 **Pla B si falla el maquinari el dia de la defensa.** Accepta una **demostració gravada** (vídeo curt fet en una sessió anterior) com a evidència del funcionament, sempre que la defensa en directe (explicació + preguntes) es faci igualment: el que s'avalua amb R4·DO és la comunicació, no només la demo en directe.

**Punts clau (defensa individual):** tot el curs és individual (`04_Metodologia.md` §4.3): **cada alumne defensa el seu propi robot i el seu propi codi**, sempre. Els 3 indicadors de la R4·DO (claredat, decisió tècnica justificada, resposta a preguntes) s'exigeixen avui al **nivell alt**: és el punt d'arribada de l'escala que comença a la SA2.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| L'alumnat explica el codi línia a línia | Confon "documentar" amb "narrar sintaxi" | Recordar el guió: explica **la decisió**, no la sintaxi (`00_Guia_defensa_oral.md`) |
| El dossier arriba incomplet a la defensa | Gestió del temps de les sessions anteriors | Els checklists (docent/alumnat) marquen punts de control per sessió perquè no s'acumuli tot a la S4 |
| La demo falla i l'alumne es bloqueja | Por a l'error davant del grup | Recordar que "DEPURA en veu alta" davant d'una demo que falla és una resposta vàlida i ben valorada |

**Producte de la SA:** rover ampliat amb el repte lliure, funcional, + dossier tècnic complet + defensa oral individual, tancat i avaluat a la **S4**.

### Mapa d'avaluació (traçabilitat)

| Instrument | Què evidencia | Criteri | Rúbrica | Qualifica? |
|---|---|---|---|---|
| Dossier tècnic (§1-§3, avançat S3) | Objectiu, disseny, esquema de connexions | CA1.1, CA2.1, CA3.1 | R2, R4 | Formativa |
| Producte «rover ampliat» (S4) | Repte integrat, funcional | CA1.1, CA1.2, CA2.1, CA2.2, CA3.1, CA4.1, CA4.2 | **R1, R2, R3** | Sí |
| Dossier tècnic complet (S4) | Codi comentat, proves, dificultats, millores, conclusions, ètica/ODS | CA4.1, CA5.1 | **R4** | Sí |
| Defensa oral individual (S4, R4·DO nivell alt) | Claredat + decisió justificada + resposta a preguntes | CA5.2 | **R4** (fila «Defensa oral») | Sí |
| Observació del procés (S1-S4) | Autonomia, gestió de l'error, responsabilitat | CA5.3 | **R5** | Sí |
| Prova pràctica T3 (S5, individual) | Destreses de SA7-SA8 | — | — | Sí, però **separat** (no reavalua el projecte) |

*(CA1.1/CA1.2 = escriure/depurar programes MicroPython amb estructures de control, funcions i biblioteques; CA2.1/CA2.2 = construir/experimentar circuits amb sensors i actuadors; CA3.1 = implementar sistemes de control; CA4.1/CA4.2 = dissenyar/provar robots mòbils i sistemes de monitoratge, valorant la IA; CA5.1/CA5.2/CA5.3 = gestió de projecte, documentació/comunicació, autonomia i responsabilitat. Vegeu [`Programació didàctica/06_Avaluacio_criteris_qualificacio.md`](../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md).)*

### Quadern tècnic — entrada de la SA9 (guia per a l'alumnat)

A la SA9, el quadern tècnic **coincideix** essencialment amb el [dossier tècnic](SA9_dossier_plantilla.md): l'alumnat no duplica contingut, però hi fa constar el resum de cada sessió (repte triat, prototip, proves, tancament i reflexió ètica/ODS).

> Comparteix **totes** les rúbriques (R1-R5) amb l'alumnat **des de la Sessió 1** (avaluació formativa): a diferència de la resta de SA, aquí el ventall de solucions possibles és ampli i cal que cadascú sàpiga contra què es mesurarà des del principi.

### Pont cap a l'avaluació trimestral

La SA9 tanca el curs: el rover que a la SA7 va aprendre a decidir sol i a la SA8 va aprendre a explicar-se, arriba aquí a un projecte propi, complet i defensat individualment. La **S5**, per estacions rotatives, tanca alhora el 3r trimestre amb la prova pràctica T3, sense interferir amb l'avaluació del projecte.

---

## Guió de modelatge (què verbalitzar)

- **S1 · Per què triar bé el repte importa:** pregunta *"si tries un repte massa ambiciós per al temps que tens, què passarà a la S3?"* — porta la resposta cap a la idea de "nucli assolible primer, ampliacions després" (mateix criteri que tots els bancs de reptes del curs).
- **S2 · Per què separar percep/decideix/actua:** pregunta *"si el teu rover fa una cosa inesperada, com saps si el problema és de lectura, de decisió o d'actuació?"* — porta la resposta cap a la idea que separar les tres funcions fa que puguis provar-les una a una.
- **S3 · Prova normal vs. prova de límit:** pregunta *"si només proves el cas en què tot va bé, què no estàs comprovant?"* — porta la resposta cap a la idea que els sistemes reals fallen sobretot als casos extrems.
- **S4 · Decisió vs. sintaxi a la defensa:** pregunta *"si expliques línia a línia què fa cada instrucció, què no estàs explicant?"* — porta la resposta cap a la idea que el **per què** d'una tria és més valuós que el **com** sintàctic.

## Atenció a la diversitat

| Necessitat | Mesura |
|---|---|
| **Bastida (qui ho necessita)** | Reptes ⭐ del [banc](SA9_reptes_proposats.md) amb nucli molt acotat (un únic llindar, sense protocol de ràdio); plantilla de projecte i de dossier ja donades; fites parcials per sessió (checklist docent/alumnat). |
| **+ Ampliació (qui va sobrat)** | Ampliacions ⭐⭐/⭐⭐⭐ de cada repte; combinar dos reptes; vincular el repte a una competició (WRO, RoboCup Junior) o a un futur Treball de Recerca; vegeu [`SA9_reptes_proposats.md`](SA9_reptes_proposats.md). |
| **Diversitat lingüística/lectora** | Dossier amb esquema/dibuix abans que text a cada secció; glossari a [`00_Glossari_tecnic.md`](../00_General/00_Glossari_tecnic.md). |
| **Sense rover/kit a punt** | Es treballa la lògica (protocol, llindars, FSM) al **simulador** (ràdio i `log` sí es simulen), amb valors de sensor simulats en variables, com a SA7-SA8. |

> **Avaluació formativa:** comparteix **totes** les rúbriques (R1-R5) amb l'alumnat des de la Sessió 1.

## Pensament computacional i depuració

- **Concepte de PC d'aquesta SA:** **integració de sistemes**: combinar components ja provats per separat (sensors, FSM, motors, ràdio) en un tot coherent que resol un problema real nou és el pas final de tota la progressió del curs (del component aïllat, SA1-SA3, al sistema complet, SA9).
- **Depuració:** continua la rutina **DEPURA** (SA1-SA8), amb èmfasi en aïllar el component **nou** del repte (provar-lo sol) abans de barrejar-lo amb la resta del sistema ja conegut.

## Context real i ODS

- **Context:** sistemes de reg intel·ligent, robots de vigilància domèstica, robots de logística, estacions ambientals urbanes: cada repte del banc reflecteix un producte real que combina percepció, decisió i actuació.
- **ODS:** segons el repte triat — **ODS 6** (aigua neta, reg), **ODS 9** (indústria i innovació, telemetria/missatger), **ODS 11** (ciutats sostenibles, sentinella/ambiental). Cada alumne identifica l'ODS del seu propi repte al dossier (§9).
