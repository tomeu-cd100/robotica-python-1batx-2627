# SA4 · Guia docent — Funcions i moviment

**Durada:** 8 h (4 sessions de 2 h; la S4 és la **fabricació del vehicle T2**) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 2 (micro servo, 2 motoreductors + rodes); fabricació del **vehicle** (peces pretallades pel docent) · **Llenguatge:** MicroPython
**Referència:** [`Programació didàctica/13_SA4_Funcions_i_moviment.md`](../../Programació%20didàctica/13_SA4_Funcions_i_moviment.md) · **Criteris:** CA1.1, CA2.1 · **Rúbriques:** R1, R2, R4

> 🧭 **Com s'usa aquesta guia.** **Abans de la SA:** objectius, materials i documents de la carpeta (la logística, al checklist docent). **A cada sessió:** la secció «SESSIÓ n» corresponent, amb el «Guió de modelatge» a mà. **En avaluar:** «Mapa d'avaluació». **Per contextualitzar:** context real i ODS.

## Objectius de la SA
1. Definir i aplicar **funcions** amb paràmetres i valor de retorn per modularitzar el codi.
2. Controlar un **servomotor** (angle) i un **motoreductor** (sentit i velocitat) des del Micro:shield.
3. Encapsular moviments bàsics (avançar, girar, aturar) en funcions reutilitzables.
4. Muntar físicament el **vehicle** del fil conductor a partir de peces pretallades.

## Materials per a la sessió
- 1 micro:bit V2 + 1 Micro:shield per alumne/a + cable micro-USB (dotació individual, vegeu [`09c_Inventari_kits_disponibles.md`](../../Programació%20didàctica/09c_Inventari_kits_disponibles.md)).
- Kit Keyestudio 2 (micro servo, 2 motoreductors + rodes) per alumne/a; portapiles 4×AA.
- Ordinadors amb accés a **python.microbit.org**. Projector. Quadern tècnic (digital).
- Sessió 4: peces pretallades del xassís del vehicle (làser), roda boja, cargols, eines de muntatge bàsiques.

## Documents de la SA (aquesta carpeta)
| Document | Quan s'usa |
|---|---|
| [`SA4_fitxa_alumnat.md`](SA4_fitxa_alumnat.md) | Totes les sessions (Activitats 1-3 + producte + quadern). |
| [`SA4_esquemes_connexions.md`](SA4_esquemes_connexions.md) | Sessions 1-4 (servo, motoreductors, pins definitius de tot el curs). |
| `codi/` | `funcions_moviments`, `coreografia`, `velocitat_pwm` i el repte-producte `control_per_botons`. |
| [`00_Projecte_T2_Vehicle.md`](../00_General/00_Projecte_T2_Vehicle.md) | Sessió 4 (muntatge vinculant del xassís). |

> Cada programa de `codi/` té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs, l'`EXPLICACIO.md` de la seva carpeta). El «Guió de modelatge» oral de sota continua sent teu.

---

## Del codi que ja fèieu al concepte de funció

**Important per contextualitzar aquesta SA:** l'alumnat **ja ha escrit funcions** de manera intuïtiva des de la SA2 (`respira()`, `mostra_color()` a `pwm_led_rgb.py`) i la SA3 (`mapa()`, `canvia_emocio()`, `llegeix_sensors()` a `mascota_reactiva.py`), sense que se'ls hagi explicat mai la sintaxi formal ni el vocabulari (**paràmetre**, **valor de retorn**, **modularitat**). Aquesta SA **no és la primera vegada que veuen un `def`**, sinó la primera vegada que **s'atura a explicar-lo**: comença repassant en veu alta un d'aquests fragments ja coneguts («ja fèieu això sense saber-ne el nom») abans d'introduir vocabulari nou. La fitxa 13 demana explícitament «refactoritzar un codi repetitiu de la SA2 en funcions»: fes-ho amb un exemple **sense** funcions (per exemple, el bucle de `led_parpelleig.py` copiat 3 vegades amb valors diferents) per mostrar el "abans" i el "després".

---

## SESSIÓ 1 (2 h) — Definir funcions amb paràmetres i valor de retorn

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Pregunta del repte inicial: *"com organitzaries el codi perquè 'avançar', 'girar' i 'aturar' es puguin cridar com si fossin ordres pròpies?"* Mostra un fragment repetitiu (3 còpies del mateix bloc amb un valor diferent cada cop). 🥋 **Kata del dia:** K06 (if/while) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Formulen hipòtesis: com evitarien la repetició? |
| Explicació | 30' | Sintaxi de `def nom(parametre):`, com es criden les funcions i què és un **valor de retorn** (`return`). Repassa en veu alta `mapa()` (SA3) i `respira()` (SA2) com a funcions que ja coneixien sense el nom. Introdueix el **servomotor**: `pin0.set_analog_period(20)` i `write_analog(26-128)` per a 0-180°. | Prenen notes; identifiquen paràmetre i valor de retorn a `mapa()`. |
| Pràctica | 60' | Modelatge de [`funcions_moviments.py`](codi/funcions_moviments/funcions_moviments.py): `graus_a_pwm(angle)` (retorna un valor), `mou_servo(angle)` (un paràmetre), `saluda(vegades)` i `escombra(angle_maxim)` (reutilització del mateix codi amb arguments diferents). | Escriuen i proven `funcions_moviments.py` amb el servo de la mascota (P0, [esquemes](SA4_esquemes_connexions.md)); fan l'Activitat 1 de la fitxa. |
| Tancament | 20' | Recull dubtes; anticipa `coreografia.py` (combinar funcions). | Entrada del quadern: què és un paràmetre, què és un valor de retorn. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **`escombra()`** (deixa només `saluda()`; `escombra()` reapareix igualment a `coreografia.py`).

**Punts clau:** una **funció** és un bloc de codi amb nom que es pot **cridar** tantes vegades com calgui; un **paràmetre** és una dada que li passes en cridar-la (canvia el resultat sense canviar el codi); un **valor de retorn** és el que la funció calcula i "torna" a qui l'ha cridada (amb `return`), a diferència d'una funció que només **fa** alguna cosa (mou el servo, mostra una cara) sense retornar res.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El servo no es mou (però el programa no dona error) | El simulador **no** simula el servo | Cal maquinari real; el simulador només valida la lògica dels bucles/paràmetres. |
| Oblida `return` a `graus_a_pwm()` | Es confon una funció que **fa** alguna cosa amb una que **calcula i retorna** un valor | Repassar la diferència amb `mapa()` (SA3), que també retorna. |
| Crida la funció sense paràntesis (`mou_servo`) | Confon el **nom** de la funció amb la seva **crida** | `mou_servo` és el valor de la funció; `mou_servo(90)` l'executa. |

---

## SESSIÓ 2 (2 h) — Controlar un motoreductor amb funcions de moviment

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Recorda el servo (angle fix); pregunta: *"i si un motor no ha d'anar a un angle, sinó girar sense parar?"* 🥋 **Kata del dia:** K20 (condicionals amb sensors/llindar) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Formulen hipòtesis sobre com es controlaria la velocitat. |
| Explicació | 25' | **Motoreductors** del Kit 2: cada motor porta **dos** pins (un per sentit), i la velocitat és PWM (`write_analog`, com el LED de la SA2). Introdueix els pins **definitius** M1/M2 ([esquemes](SA4_esquemes_connexions.md)): a partir d'avui no es tornen a tocar en tot el curs. | Prenen notes; munten els dos motoreductors seguint l'esquema. |
| Pràctica | 45' | Modelatge de [`velocitat_pwm.py`](codi/velocitat_pwm/velocitat_pwm.py): `avancar(velocitat)`, `retrocedir(velocitat)`, `girar(costat)`, `aturar()`. | Proven `velocitat_pwm.py` amb els motors alimentats per portapiles (**mai** USB); fan l'Activitat 2 de la fitxa. |
| Activitat nucli · `return` | 10' | **Escriptura guiada:** demana que cadascú escrigui `temps_per_recorregut(cm)` (paràmetre `cm`, `return` dels ms calculats a partir d'una velocitat calibrada) ABANS de mirar la solució, i que la facin servir amb `sleep(temps_per_recorregut(30))`. És la primera funció amb valor de retorn que **escriu** l'alumnat (a S1 només la van llegir a `graus_a_pwm()`). | Escriuen `temps_per_recorregut(cm)`, la proven i la comparen amb [`velocitat_pwm.py`](codi/velocitat_pwm/EXPLICACIO.md#bloc-5--activitat-nucli-sessió-2-escriu-tu-una-funció-amb-valor-de-retorn). |
| Mini-check + Tancament | 30' | **Mini-check individual** (10', escriure una funció amb paràmetre sense apunts; banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md)). Recull dubtes. | Fan el mini-check (no qualifica); anoten al quadern un comentari de cada paràmetre de les seves funcions de moviment. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **`girar()`** (deixa `avancar()`/`retrocedir()`/`aturar()`; `girar()` reapareix igualment a `control_per_botons.py`, S3).

**Punts clau:** un motoreductor **no** va a un angle: gira contínuament, i el **sentit** es decideix triant a quin dels dos pins del motor s'envia el PWM (l'altre a `0`); mai als dos alhora. La **velocitat** és el mateix concepte de PWM que ja coneixies (`write_analog`, 0-1023), aplicat a un motor en lloc d'un LED. `temps_per_recorregut(cm)` és la primera funció amb `return` que **escriu** l'alumnat (no només la llegeix): calcula un temps a partir d'una distància, no mou res per si sola.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El motor no es mou | Micro:shield alimentat només per USB | Alimentar sempre els motors des del portapiles. |
| Un motor gira al revés del que esperaves | Sentit del cablatge del canal invertit | Inverteix el signe al codi (`avancar()`/`retrocedir()`), no recablis. |
| Els dos pins d'un motor reben PWM alhora | Error de programació (bloqueja o vibra sense girar) | Revisar que l'altre pin es posi sempre a `0`. |
| `temps_per_recorregut()` no fa avançar res | Confon una funció amb `return` (calcula) amb una que **fa** alguna cosa; li falta cridar `avancar()`/`sleep()` amb el resultat | Repassar amb `graus_a_pwm()` (S1): el `return` calcula, la crida a `avancar(...)`/`sleep(...)` és qui actua. |

---

## SESSIÓ 3 (2 h) — Repte «control per botons» (producte de la SA)

> 🎯 **Producte de la SA.** Aquest repte **fa de producte** de la SA4: s'avalua amb **R1** (codi, criteri "Estructura"/modularitat) i **R2** (bases del muntatge). Aquesta S3 **allibera la S4** per a la fabricació (primera retallada del pla de contingència si cal): si el repte no es tanca del tot, es completa com a deures.

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Mostra [`control_per_botons.py`](codi/control_per_botons/control_per_botons.py) **sense executar-lo** (PRIMM): pregunta què farà cada botó. 🥋 **Kata del dia:** K07 (funcions/paràmetres) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Prediuen el comportament dels botons A/B. |
| Explicació | 20' | Modelatge de la **seqüència amb estat** (`PAS`, `seguent_moviment()`) i de per què el botó B **sempre** atura, es processi on es processi (anticipa l'estat STOP de la SA6). | Prenen notes; identifiquen quines funcions ja coneixen (`avancar`, `girar`...) i quines són noves (seqüència, botons). |
| Repte | 70' | Acompanya la programació individual del repte: seqüència **pròpia** de moviments encadenada amb les funcions de moviment, activada amb els botons A/B. | Programen la seva pròpia seqüència a partir de `control_per_botons.py` (Activitat 3, producte). |
| Tancament | 20' | Recull dubtes; anuncia la fabricació de la S4. | Anoten al quadern la seqüència triada i per què. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: la **variació personal** de la seqüència (deixa la de `control_per_botons.py` tal qual; la personalització reapareix com a ampliació ⭐).

**Punts clau:** una **seqüència** és una sèrie de crides a funcions ja fetes, controlada per una variable d'estat (`PAS`) que recorda on som; una entrada que **sempre interromp** el que s'estigui fent (el botó B) és la primera versió d'un concepte que la SA6 formalitzarà com a **STOP prioritari**.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El vehicle no respon a cap botó | `was_pressed()` només detecta premudes **noves** després de carregar el programa | Deixar anar el botó abans de tornar a provar. |
| La seqüència es "salta" un pas | Botó premut diverses vegades molt seguides | `was_pressed()` ja porta antirebot intern; comprovar igualment. |
| El vehicle no s'atura mai del tot | `aturar()` no posa els quatre pins a `0` | Revisar que no en falti cap. |

---

## SESSIÓ 4 (2 h) — Muntatge físic del vehicle

> 🔧 **Sessió de fabricació.** Segons el calendari del fil conductor, aquesta sessió es dedica **íntegrament** al muntatge del vehicle T2 (vegeu `08_Sequenciacio_temporal_anual.md` i [`00_Projecte_T2_Vehicle.md`](../00_General/00_Projecte_T2_Vehicle.md)).

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Organització | 10' | Reparteix les peces pretallades (xassís, suports) i el material de muntatge; recorda l'ordre del dossier del vehicle. | Preparen el lloc de treball i revisen la llista de peces. |
| Muntatge | 80' | Acompanya el muntatge pas a pas (§ Muntatge del [dossier](../00_General/00_Projecte_T2_Vehicle.md)): xassís, motoreductors i roda boja, fixació de la micro:bit + Micro:shield i el portapiles, cablatge **exacte** dels pins fixats a la S2 ([esquemes](SA4_esquemes_connexions.md)). | Munten el xassís i cablegen els motors seguint la taula de pins ja provada. |
| Prova d'encesa | 20' | Supervisa la **prova de fum**: carregar `velocitat_pwm.py` o `control_per_botons.py` per comprovar que el vehicle respon abans de donar el muntatge per acabat. | Carreguen el programa de prova i validen que els dos motors giren en el sentit esperat. |
| Tancament | 10' | Checklist de muntatge; recorda portar el vehicle a la SA5. | Recullen material; anoten al quadern com ha anat el muntatge. |

**Punts clau:** el muntatge físic **no** és una activitat nova de programació: és **mecànic**, i valida amb maquinari real tot el que ja es va provar per separat a la S2-S3 (els pins de motor **no canvien**). El vehicle es porta muntat a la SA5 per treballar-hi el control remot per ràdio.

**Producte de la SA:** repte «control per botons» (avançar/retrocedir/girar/aturar amb funcions pròpies, activat per botons), tancat i avaluat a la **S3**. Muntatge físic del **vehicle** a la **S4** (fabricació, avaluada amb la rúbrica de muntatge). Mini-defensa breu (1-2') del repte de la S3 (R4·DO).

### Mapa d'avaluació (traçabilitat)

| Instrument | Què evidencia | Criteri | Rúbrica | Qualifica? |
|---|---|---|---|---|
| Mini-check (S2) | Funció amb paràmetre sense apunts | CA1.1 | — | **No** (radar formatiu) |
| Fitxa d'alumnat (Act. 1-2) | Funcions amb paràmetres i valor de retorn; servo i motoreductor | CA1.1, CA2.1 | R1 | Formativa |
| Repte «control per botons» (S3, producte) | Modularitat: moviment del vehicle encapsulat en funcions pròpies | CA1.1, CA2.1 | **R1**, **R2** | Sí |
| Mini-defensa (S3, R4·DO) | Claredat + justificació d'una decisió de disseny de la seqüència | CA5.2 | **R4** (fila «Defensa oral») | Sí |
| Muntatge del vehicle (S4) | Fabricació física correcta i segura | CA2.1 | **R2** (muntatge) | Sí |
| Quadern tècnic | Documentació, paràmetres comentats | CA5.2 | **R4** | Sí |
| Observació d'aula | Autonomia i seguretat amb servo/motors | CA5.3 | **R5** | Sí |

*(CA1.1 = escriure i depurar programes MicroPython amb estructures de control (ara, també funcions); CA2.1 = connectar i experimentar amb sensors i actuadors del Micro:shield/Keyestudio amb seguretat. Vegeu [`Programació didàctica/06_Avaluacio_criteris_qualificacio.md`](../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md).)*

### Quadern tècnic — entrada de la SA4 (guia per a l'alumnat)

Segueix el mètode de projecte:
- **Què he après** (funcions, paràmetres, valor de retorn, servo amb PWM, motoreductor amb PWM i sentit).
- **El repte i com l'he resolt** (predicció → funcions → seqüència → botons).
- **Un error que he tingut i com l'he resolt.**
- **Muntatge del vehicle:** com ha anat, quines dificultats mecàniques hi ha hagut.

> Comparteix les rúbriques **R1**, **R2** i **R4** amb l'alumnat **abans** de començar el repte (avaluació formativa).

### Pont cap a la SA5

A la SA4 hem après a **moure't** amb funcions pròpies (servo, motoreductors) i hem muntat el vehicle. A la **SA5** activarem aquestes mateixes funcions de moviment amb **comandes de ràdio** enviades des d'una altra micro:bit, en lloc dels botons A/B: el mateix esquema («entrada → funció de moviment»), amb una entrada nova.

---

## Guió de modelatge (què verbalitzar)

- **S1 · Funció amb valor de retorn:** demana a la classe que et digui, sense mirar el codi, què fa `graus_a_pwm(90)` — porta la resposta cap al fet que **no mou res**, només calcula i retorna un número. *Error a anticipar:* pensar que totes les funcions mouen o mostren alguna cosa.
- **S2 · Sentit amb dos pins:** pregunta *"per què cada motor necessita DOS pins i no un de sol amb un signe positiu/negatiu?"* abans d'ensenyar `avancar()`/`retrocedir()` — porta la resposta cap al fet que un pin PWM només pot enviar valors positius (0-1023). *Error a anticipar:* enviar PWM als dos pins d'un motor alhora.
- **S3 · Interrupció prioritària:** prem el botó B enmig d'un gir davant la classe i pregunta *"per què s'ha aturat immediatament, sense esperar que acabés el gir?"* — porta la resposta cap al fet que el `if` del botó B es comprova **cada volta** del bucle, no només en punts concrets.

## Atenció a la diversitat

| Necessitat | Mesura |
|---|---|
| **Bastida (qui ho necessita)** | Plantilla de funció de moviment amb el nom i els paràmetres ja definits (`def avancar(velocitat):` amb el cos buit); esquema de connexió del motoreductor ja fet. |
| **+ Ampliació (qui va sobrat)** | Funció de moviment amb velocitat variable i acceleració progressiva; seqüència coreografiada de moviments (vegeu [Reptes de la SA4](../../Reptes/Reptes_SA4.md)). |
| **Diversitat lingüística/lectora** | Taula de pins amb icones de component; glossari a [`00_Glossari_tecnic.md`](../00_General/00_Glossari_tecnic.md). |
| **Sense maquinari per a tothom** | El simulador de python.microbit.org **no** reprodueix ni el servo ni els motoreductors: qui no tingui placa treballa per torns o substitueix temporalment les crides de moviment per `display.scroll(...)` per validar la **lògica**. |

> **Avaluació formativa:** comparteix les rúbriques **R1**, **R2** i **R4** amb l'alumnat **abans** de començar el producte.

## Pensament computacional i depuració

- **Concepte de PC d'aquesta SA:** **abstracció** i **modularitat**: `avancar(400)` amaga tot el detall de pins i PWM darrere d'un nom que expressa la intenció ("avançar"), igual que `write_analog(700)` amagava el parpelleig ràpid a la SA2. Nomena-ho explícitament quan modelitzis les funcions de moviment.
- **Depuració:** continua la rutina **DEPURA** (SA1-SA3), amb un èmfasi nou: si una funció no fa el que esperes, **prova-la sola al REPL** amb valors coneguts abans de buscar l'error en un programa més gran que la crida.

## Context real i ODS

- **Context:** robots industrials i domèstics que encapsulen moviments complexos en ordres senzilles (braços robòtics, aspiradors robot, drons); vehicles elèctrics amb control de velocitat per motor independent a cada roda.
- **ODS 9** (indústria, innovació i infraestructura): la modularitat del codi (funcions reutilitzables) és el mateix principi que permet construir sistemes complexos fiables a partir de peces senzilles i provades.
