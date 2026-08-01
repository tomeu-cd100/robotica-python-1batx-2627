# SA1 · Guia docent — Hola, robot!

**Durada:** 6 h (3 sessions de 2 h) · **Maquinari:** micro:bit V2 sola (sense Micro:shield) · **Llenguatge:** MicroPython
**Referència:** [`Programació didàctica/10_SA1_Hola_robot.md`](../../Programació%20didàctica/10_SA1_Hola_robot.md) · **Criteris:** CA1.2, CA5.3 · **Rúbriques:** R4, R5

> 🧭 **Com s'usa aquesta guia.** **Abans de la SA:** objectius, materials i documents de la carpeta (la logística, al checklist docent). **A cada sessió:** la secció «SESSIÓ n» corresponent, amb el «Guió de modelatge» a mà. **En avaluar:** «Mapa d'avaluació». **Per contextualitzar:** context real i ODS.

## Objectius de la SA
1. Definir robot i sistema embegut; identificar entrada-procés-sortida en exemples reals.
2. Reconèixer l'arquitectura de la micro:bit V2 (matriu de LED, botons, pins, sensors interns, alimentació).
3. Conèixer i aplicar les **normes de seguretat** del laboratori.
4. Familiaritzar-se amb l'**editor MicroPython** (python.microbit.org) i el **simulador**, i llegir/modificar el primer programa.
5. Conèixer i començar a aplicar el **mètode de projecte** (analitzar → dissenyar → programar/prototipar → provar → millorar), que es repetirà a totes les SA fins al projecte final (SA9).

## Materials per a la sessió
- 1 micro:bit V2 per alumne/a (o, si no n'hi ha prou per a tothom, per torns amb el simulador com a pla B) + cable micro-USB.
- Ordinadors amb accés a **python.microbit.org** (no cal instal·lar res ni crear compte).
- Projector. Quadern tècnic (digital) per a cada alumne/a.

## Documents de la SA (aquesta carpeta)
| Document | Quan s'usa |
|---|---|
| [`SA1_fitxa_alumnat.md`](SA1_fitxa_alumnat.md) | Totes les sessions (Activitats 1-4 + producte + quadern). |
| [`SA1_prova_diagnostica.md`](SA1_prova_diagnostica.md) | Sessió 1 (no qualifica). |
| [`SA1_esquemes_connexions.md`](SA1_esquemes_connexions.md) | Sessió 2 (anatomia de la placa, Activitat 2). |
| [`SA1_normes_seguretat.md`](SA1_normes_seguretat.md) | Sessió 2 (lectura i **signatura**). |
| [`SA1_poster_robot_plantilla.md`](SA1_poster_robot_plantilla.md) | Producte de la SA (es comença a la Sessió 3). |
| `codi/` | `hola_mon`, `emocions_botons` i l'ampliació `dau_sacseig`. |

> Cada programa de `codi/` té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs, l'`EXPLICACIO.md` de la seva carpeta): és el text que l'alumnat pot rellegir si falta a classe o repassa a casa. El «Guió de modelatge» oral de sota continua sent teu.

---

## El mètode de projecte (fil conductor del curs)

La SA1 no només respon *"què és un robot?"*: també presenta **com treballarem** a totes les SA. És el cicle d'enginyeria que es repetirà fins al projecte final (SA9) i que comença a treballar la **CA5.3** (valorar l'impacte de la solució i treballar amb autonomia).

> 💡 **Digues-li pel nom des del primer dia:** aquest cicle és la versió d'aula del **design thinking** (`Programació didàctica/04_Metodologia.md` §4.1). Anomena'l així en presentar el pòster: quan el nom formal reaparegui més endavant al curs, serà una **repesca**, no una metodologia nova estrenada a última hora.

| Fase | Pregunta clau | A la SA1 es viu així… |
|---|---|---|
| **1. Analitzar** | Quin problema/repte tinc? Què necessito? | Entendre el repte del primer programa i descompondre'l (entrada-procés-sortida). |
| **2. Dissenyar** | Com ho penso resoldre abans de fer-ho? | Predir/planificar la solució del repte (PRIMM, Sessió 3) abans d'escriure codi. |
| **3. Programar/Prototipar** | Construeixo una primera versió. | Escriure i provar el codi (al simulador o a la placa). |
| **4. Provar** | Funciona? On falla? | Transferir a la placa, observar, identificar errors (taula d'errors freqüents). |
| **5. Millorar** | Com ho faig millor? | Ajustar temps i missatges, provar variants, ampliacions. |

> Es presenta de forma **breu i visual** i es **referencia explícitament** cada cop que l'alumnat resol un repte. No es memoritza: s'aplica. És també l'estructura del **quadern tècnic** ([`00_Quadern_tecnic.md`](../00_General/00_Quadern_tecnic.md)).

---

## SESSIÓ 1 (2 h) — Què és un robot?

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 15' | Llança la pregunta: *"Quins robots tens a casa sense saber-ho?"* | Pluja d'idees; llista a la pissarra. |
| Explicació | 25' | Presenta el model **entrada → procés → sortida** i el concepte de sistema embegut. | Prenen notes; classifiquen exemples. |
| Pràctica | 40' | Reparteix l'**anàlisi de 3 sistemes** (rentadora, dron, semàfor). | Individualment, omplen la taula E-P-S de la fitxa (Activitat 1). |
| Diagnòstic | 30' | Passa la **prova diagnòstica** ([`SA1_prova_diagnostica.md`](SA1_prova_diagnostica.md); no qualifica). | Responen individualment. |
| Tancament | 10' | Recull conclusions; presenta el **mètode de projecte** com a forma de treball del curs (el quadern tècnic s'obrirà formalment a la Sessió 2). | Reflexió breu oral: quin sistema de casa han après a "desxifrar" avui. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **la Pràctica «anàlisi de 3 sistemes» (fes-ne només 2)**.

**Punts clau:** tot sistema automàtic té sensors (entrada), un "cervell" (procés) i actuadors (sortida). El robot és un sistema embegut amb capacitat d'actuar sobre l'entorn. **Tot el curs** treballarem amb el cicle analitzar → dissenyar → programar/prototipar → provar → millorar, sempre de manera **individual**.

**Solucions Activitat 1 (orientatives):**
| Sistema | Entrada | Procés | Sortida |
|---|---|---|---|
| Rentadora | Selector de programa, sensor de nivell d'aigua i de temperatura | Microcontrolador que segueix el cicle (omplir, rentar, centrifugar) | Motor del tambor, electrovàlvula, resistència, bomba de buidatge |
| Dron | Giroscopi/acceleròmetre, GPS, comandament | Controlador de vol que estabilitza i navega | Motors de les hèlixs, LED, càmera |
| Semàfor | Temporitzador, sensor de presència/espira | Lògica de seqüència de fases | LED vermell/groc/verd |

**Prova diagnòstica:** vegeu [`SA1_prova_diagnostica.md`](SA1_prova_diagnostica.md) (versió imprimible amb clau de correcció). **No qualifica**: orienta el ritme i detecta qui parteix amb experiència prèvia de programació.

---

## SESSIÓ 2 (2 h) — Arquitectura de la micro:bit i seguretat

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Reparteix una micro:bit V2 per alumne/a. | Observen les parts visibles. |
| Explicació | 30' | Arquitectura: microcontrolador, matriu de 25 LED, botons A/B, pins d'expansió, alimentació per USB. Senyal analògic vs digital (introducció). (Projecta [`SA1_esquemes_connexions.md`](SA1_esquemes_connexions.md).) | Etiqueten l'esquema de la placa (Activitat 2). |
| Seguretat | 20' | Presenta i comenta les **normes de seguretat** ([`SA1_normes_seguretat.md`](SA1_normes_seguretat.md)): electricitat de molt baixa tensió (USB, 3 V), sense làser (el làser de fabricació digital només l'usa el professorat). | Llegeixen i **signen** el full. |
| Pràctica | 50' | Tour guiat de l'editor **python.microbit.org**: simulador, editor, botó «Baixa», transferència del `.hex` a la placa. | Escriuen i proven un primer programa mínim al simulador. |
| Tancament | 10' | Resol dubtes de l'entorn; **obre formalment el quadern tècnic** (presenta [`00_Quadern_tecnic.md`](../00_General/00_Quadern_tecnic.md)). | **Primera entrada del quadern**: captura o descripció del primer programa provat. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **el tour guiat de l'editor (dins la Pràctica; prioritza que tothom provi el simulador un cop)**.

**Punts clau:**
- **Digital** = dos estats (0/3,3 V, prement/no prement un botó). **Analògic** = valors continus (p. ex. el nivell de llum, 0-255).
- La micro:bit V2 té sensors **interns** (acceleròmetre, brúixola, llum, temperatura, micròfon): no cal cap component extern per començar.
- **Seguretat:** la micro:bit funciona a **molt baixa tensió** (USB o piles), sense risc elèctric rellevant si es manipula amb cura; el **làser** de la talladora (que s'usarà més endavant per al fil conductor) el fa servir **només el professorat**.

---

## SESSIÓ 3 (2 h) — El primer programa MicroPython

> **Mètode de lectura de codi: PRIMM.** En lloc de copiar codi, l'alumnat el **Prediu**, l'**Executa**, l'**Investiga**, el **Modifica** i en **Crea** un de nou. Predir *abans* d'executar és el pas que més consolida la comprensió. Encaixa amb el mètode de projecte (predir = dissenyar; executar/investigar = provar; modificar/crear = millorar).

| Fase (PRIMM) | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| **Predir** | 15' | Projecta `hola_mon.py` **sense executar-lo**: *"Què creieu que farà? Què fa cada línia?"* | Escriuen la seva **predicció** a la fitxa (Activitat 4). |
| **Executar** | 10' | Carrega el programa (simulador o placa real). | Comproven la predicció; comenten diferències. |
| **Investigar** | 20' | Lectura guiada: `from microbit import *`, `display.scroll()`, `display.show()`, `Image`. | Anoten què fa cada part i per què. |
| **Modificar** | 25' | Demana canviar el text i afegir una imatge diferent. | Modifiquen el text i la imatge i observen l'efecte. |
| **Crea** | 30' | Proposa el programa **`emocions_botons`**: els botons A/B canvien la cara del display. Per a qui acaba aviat, l'ampliació `dau_sacseig`. | Escriuen/proven; comparen solucions. |
| **Debat + tancament** | 20' | Mini-debat **ètica de l'automatització** (ODS); presenta la **fitxa-pòster** ([`SA1_poster_robot_plantilla.md`](SA1_poster_robot_plantilla.md)). | Reflexió escrita al quadern; trien el robot del pòster. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **l'ampliació `dau_sacseig` de la fase «Crea»** (queda com a feina per als reptes ⭐).

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió; no qualifica).** Abans de començar el bloc PRIMM, passa el mini-check de la SA1: banc complet a [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md#sa1--mini-check-inici-de-la-sessió-3). Llegeix un programa curt (`display.scroll`/`display.show`/`sleep`) sense executar-lo i explica-hi línia a línia. Serveix de radar formatiu, no de nota.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El programa no fa res a la placa | No s'ha transferit el `.hex` (falta arrossegar-lo a la unitat `MICROBIT`) | Repassar `00_Entorns_de_treball.md` §4: baixar i arrossegar el `.hex`. |
| `NameError: name 'display' is not defined` | Falta `from microbit import *` a la primera línia | Recordar que **totes** les ordres de la placa (`display`, `button_a`...) vénen d'aquest import. |
| El text passa massa ràpid/lent | Cap `sleep()` o valor massa petit/gran entre missatges | Ajustar el valor de `sleep()` (en mil·lisegons). |
| El programa dels botons només s'executa un cop | Falta el `while True:` que ho repeteixi | Recordar que sense bucle el programa passa un cop i s'atura. |

**Producte de la SA:** fitxa-pòster individual d'anàlisi d'un robot real ([`SA1_poster_robot_plantilla.md`](SA1_poster_robot_plantilla.md)) + primeres entrades del quadern tècnic.

### Mapa d'avaluació (traçabilitat)

| Instrument | Què evidencia | Criteri | Rúbrica | Qualifica? |
|---|---|---|---|---|
| Prova diagnòstica | Coneixements previs (per adaptar el ritme) | — | — | **No** (diagnòstica) |
| Mini-check (S3) | Lectura bàsica de codi MicroPython | CA1.2 | — | **No** (radar formatiu) |
| Fitxa d'alumnat (Act. 1-3) | Comprensió E-P-S, placa, codi | CA5.3 | R4 | Formativa |
| Fitxa-pòster | Anàlisi d'un sistema + dilema ètic (ODS) | CA5.3 | **R4** | Sí |
| Quadern tècnic | Documentació i reflexió del procés | CA5.3 | **R4** | Sí |
| Observació d'aula | Autonomia, seguretat, responsabilitat | CA5.3 | **R5** | Sí |

*(CA1.2 = utilitzar el simulador i l'editor per experimentar i corregir programes; CA5.3 = valorar l'impacte ètic/social/ambiental i treballar amb autonomia. Vegeu [`Programació didàctica/06_Avaluacio_criteris_qualificacio.md`](../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md).)*

### Quadern tècnic — primera entrada (guia per a l'alumnat)

El quadern tècnic és el **diari de bord** que es farà servir tota la matèria ([`00_Quadern_tecnic.md`](../00_General/00_Quadern_tecnic.md)). La 1a entrada (SA1) inclou, seguint el mètode de projecte:
- **Què he après** (conceptes clau: robot, sistema embegut, E-P-S, digital/analògic).
- **Repte i com l'he resolt** (predicció → solució → millores del primer programa).
- **Un error que he tingut i com l'he resolt.**
- **Reflexió ètica** (un avantatge i un risc de l'automatització + ODS).

> Comparteix les rúbriques **R4** i **R5** amb l'alumnat **abans** de començar (avaluació formativa; vegeu [`Programació didàctica/07_Rubriques.md`](../../Programació%20didàctica/07_Rubriques.md)).

### Pont cap a la SA2

A la SA1 hem fet aparèixer **text i imatges** al display (una sortida senzilla) i hem après a **reaccionar** a botons. A la **SA2** controlarem **sortides digitals i PWM** connectades al Micro:shield (LED, brunzidor, servo): passem d'un display integrat a **actuar sobre el món exterior**.

---

## Guió de modelatge (què verbalitzar)

> Frases i preguntes clau per al **Modelatge** de cada sessió. Pensat perquè el docent **afegeixi valor encara que no improvisi codi**: el que cal mirar, què preguntar (predicció) i l'error que cal anticipar.

- **S1 · Entrada–Procés–Sortida:** dibuixa 3 caixes (SENSOR → CERVELL → ACTUADOR). Per a cada exemple pregunta *"què percep? què decideix? què fa?"* — **no donis tu la resposta**, que la classe ompli les caixes. *Error a anticipar:* confondre entrada (sensor) amb sortida (actuador).
- **S2 · La placa:** assenyala **físicament** cada part de la micro:bit abans de projectar-ne l'esquema. Pregunta: *"aquesta llumeta de 25 punts, és una entrada o una sortida?"* *Error a anticipar:* pensar que el display només és decoratiu (també fa de sensor de llum!).
- **S3 · Primer programa (PRIMM):** projecta `hola_mon.py` **sense executar-lo**. Pregunta: *"què farà? i si canvio 'HOLA' per un altre text?"*. Verbalitza que `from microbit import *` cal **sempre** a la primera línia, i que `sleep()` és en **mil·lisegons**. *Error a anticipar:* oblidar l'import i no entendre el `NameError`.

## Atenció a la diversitat

| Necessitat | Mesura |
|---|---|
| **Bastida (qui ho necessita)** | Apartats guiats de la fitxa i de la plantilla del pòster; taula E-P-S amb un exemple ja resolt de model; l'esquelet amb `# TODO` de la secció «Si t'encalles» de la [pàgina de la pràctica d'`emocions_botons`](codi/emocions_botons/EXPLICACIO.md). |
| **+ Ampliació (qui va sobrat)** | Programa `dau_sacseig.py` (acceleròmetre + nombres aleatoris); investigar un robot real amb IA o autonomia avançada i preparar una defensa breu. |
| **Diversitat lingüística/lectora** | Glossari mínim a la pissarra (sensor, actuador, procés, embegut; vegeu [`00_Glossari_tecnic.md`](../00_General/00_Glossari_tecnic.md)); diagrames en lloc de text dens. |
| **Sense maquinari per a tothom** | Tot és reproduïble al **simulador de python.microbit.org**; es pot treballar per torns amb la placa física mentre la resta prova al simulador. |

> **Avaluació formativa:** comparteix les rúbriques **R4** i **R5** amb l'alumnat **abans** de començar el producte.

## Pensament computacional i depuració

- **Concepte de PC d'aquesta SA:** **descomposició** (partir un sistema en entrada → procés → sortida). Nomena-ho explícitament a l'Activitat 1.
- **Depuració:** presenta la **rutina DEPURA** com a forma estàndard d'afrontar errors tot el curs (és a la fitxa); el docent té la taula d'**errors freqüents** de més amunt.

> DEPURA: **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara · **A**punta.

## Avaluació formativa (instruments)

- **Diana d'autoavaluació** (fitxa): posicionament en 3 criteris clau.
- **Exit ticket** (fitxa ampliada): 3 preguntes de tancament; recull-les per ajustar la sessió següent.

## Context real i ODS

- **Context:** robots quotidians i sistemes embeguts invisibles (electrodomèstics, transport, indústria).
- **ODS 9** (indústria, innovació) i **ODS 12** (consum responsable): hi connecten el dilema ètic del pòster i la reflexió del quadern.
