# SA2 · Guia docent — Sortides: el robot actua

**Durada:** 8 h (4 sessions de 2 h) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 1 (LED, LED RGB, brunzidor) i Kit 3 (relé, LED addicionals) · **Llenguatge:** MicroPython
**Referència:** [`Programació didàctica/11_SA2_Sortides_el_robot_actua.md`](../../Programació%20didàctica/11_SA2_Sortides_el_robot_actua.md) · **Criteris:** CA1.1, CA2.1, CA2.2 · **Rúbriques:** R1, R2, R4

> 🧭 **Com s'usa aquesta guia.** **Abans de la SA:** objectius, materials i documents de la carpeta (la logística, al checklist docent). **A cada sessió:** la secció «SESSIÓ n» corresponent, amb el «Guió de modelatge» a mà. **En avaluar:** «Mapa d'avaluació». **Per contextualitzar:** context real i ODS.

## Objectius de la SA
1. Escriure programes amb **variables i bucles** (`for`, `while`) per controlar sortides repetitives.
2. Connectar i controlar **sortides digitals i PWM** (LED, LED RGB, brunzidor, relé) al Micro:shield amb seguretat.
3. Programar animacions i sons a la **matriu LED** i a l'altaveu de la micro:bit.
4. Muntar físicament la **mascota** del fil conductor a partir de peces pretallades.

## Materials per a la sessió
- 1 micro:bit V2 + 1 Micro:shield per alumne/a + cable micro-USB (dotació individual, vegeu [`09c_Inventari_kits_disponibles.md`](../../Programació%20didàctica/09c_Inventari_kits_disponibles.md)).
- Kit Keyestudio 1 (LED, LED RGB, brunzidor, cables dupont) i Kit 3 (relé, LED addicionals) per alumne/a.
- Ordinadors amb accés a **python.microbit.org**. Projector. Quadern tècnic (digital).
- Sessió 4: peces pretallades de la **mascota** (DM 3 mm, tallades pel docent amb la xTool S1) + escaires impresos + cargoleria (vegeu [`00_Projecte_T1_Mascota.md`](../00_General/00_Projecte_T1_Mascota.md)).

## Documents de la SA (aquesta carpeta)
| Document | Quan s'usa |
|---|---|
| [`SA2_fitxa_alumnat.md`](SA2_fitxa_alumnat.md) | Totes les sessions (Activitats 1-4 + producte + quadern). |
| [`SA2_esquemes_connexions.md`](SA2_esquemes_connexions.md) | Sessions 1-3 (pins del Micro:shield per a cada component). |
| `codi/` | `led_parpelleig`, `pwm_led_rgb`, `musica_altaveu` i el repte-producte `semafor_rele`. |
| [`00_Projecte_T1_Mascota.md`](../00_General/00_Projecte_T1_Mascota.md) | Sessió 4 (fabricació i muntatge). |

> Cada programa de `codi/` té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs, l'`EXPLICACIO.md` de la seva carpeta). El «Guió de modelatge» oral de sota continua sent teu.

> ℹ️ **Divergència documentada respecte al pla original:** el pla de tasques anomenava `neopixel_colors` (tira WS2812B) i `servo_saluda` (micro servo). Cap dels dos consta a `Programació didàctica/11_SA2_Sortides_el_robot_actua.md` ni a l'inventari real de maquinari (`09c`): la tira NeoPixel no forma part de cap kit disponible, i el micro servo és material del **Kit 2**, reservat a la **SA4** («Funcions i moviment»). Aquesta guia segueix la fitxa 11 (font de veritat): LED extern, LED RGB, brunzidor i relé (Kit 1 + Kit 3). El servo de la mascota es **munta físicament a la S4** (vegeu més avall) però **no es programa fins a la SA4**.

---

## El mètode de projecte, aplicat a sortides

Continuem el cicle **analitzar → dissenyar → programar/prototipar → provar → millorar** (SA1). A la SA2 el "analitzar" es converteix en *"quin senyal necessito enviar al component?"* (digital 0/1 o PWM 0-1023) i el "provar" inclou **mirar el component físic**, no només el display.

---

## SESSIÓ 1 (2 h) — Sortides digitals amb bucles

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Repartir Micro:shield + Kit 1; encaixar la micro:bit al shield. Pregunta: *"com fa un robot per parpellejar?"* 🥋 **Kata del dia:** K01 (if/while) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Encaixen el shield; observen els connectors *block*. |
| Explicació | 25' | `display.show()`/`display.scroll()` amb bucles `for` (repetir una animació N vegades); acumuladors per comptar repeticions. Introdueix `pin1.write_digital(1/0)` per al LED extern. | Prenen notes; prediuen la sortida d'un bucle `for` senzill. |
| Pràctica | 55' | Modelatge de [`led_parpelleig.py`](codi/led_parpelleig/led_parpelleig.py): LED extern a P1, `while True:` + comptador de parpellejos mostrat al display cada 10 cicles. | Munten el LED al Micro:shield ([esquemes](SA2_esquemes_connexions.md)) i escriuen/proven el programa (Activitat 1). |
| Tancament | 20' | Recull dubtes de cablatge; anticipa la Sessió 2 (PWM). | Entrada del quadern: primer muntatge fora de la placa sola. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **el comptador de parpellejos de l'Activitat 1** (deixa'l per a qui acabi abans).

**Punts clau:** una sortida **digital** només té dos estats (`write_digital(1)`/`write_digital(0)`): igual que un botó, però manant en lloc de llegint. Un bucle `for i in range(n):` repeteix un bloc **n vegades comptades**; un `while True:` el repeteix **per sempre**. Un **acumulador** (`comptador = comptador + 1`) recorda quantes vegades ha passat alguna cosa.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El LED no s'encén mai | Polaritat invertida (LED al revés) o cable al pin equivocat | Comprovar la pota llarga (ànode) cap al pin de senyal; repassar l'[esquema](SA2_esquemes_connexions.md). |
| El LED queda sempre encès | Falta `write_digital(0)` a la segona meitat del bucle | Revisar que cada `sleep()` va acompanyat de l'estat oposat. |
| El comptador no avança | S'inicialitza dins del bucle (`comptador = 0` a cada volta) | La variable acumuladora s'inicialitza **abans** del `while`, no dins. |

---

## SESSIÓ 2 (2 h) — Sortides PWM i so

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Mini-check | 10' | Passa el **mini-check individual** a l'inici de sessió (banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md#sa2--mini-check-inici-de-la-sessió-2)): de memòria, parpelleig d'un LED per sortida digital (consolida la S1). | Responen individualment (no qualifica). |
| Activació | 10' | Recorda `write_digital`; pregunta: *"i si vull un LED a mitja llum, no del tot encès ni apagat?"* 🥋 **Kata del dia:** K18 (if/while) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Formulen hipòtesis. |
| Explicació | 20' | **PWM** (`pinN.write_analog(0-1023)`): explica el parpelleig ràpid que "enganya l'ull". LED RGB: barrejar colors variant la intensitat de cada canal. Mòdul `music`: `music.play()`, notes i durada. | Prenen notes; prediuen l'efecte d'un `write_analog` creixent. |
| Pràctica | 55' | Modelatge de [`pwm_led_rgb.py`](codi/pwm_led_rgb/pwm_led_rgb.py) (efecte de respiració + colors combinats) i [`musica_altaveu.py`](codi/musica_altaveu/musica_altaveu.py) (melodia + to segons botó). | Munten LED RGB i brunzidor ([esquemes](SA2_esquemes_connexions.md)); escriuen/proven els dos programes (Activitat 2). |
| Tancament | 15' | Recull dubtes; presenta el repte de la S3 (semàfor/llum d'ambient). | Anoten al quadern un color RGB propi (valors R/G/B) per provar la sessió vinent. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **els colors combinats del LED RGB** de `pwm_led_rgb.py` (deixa només l'efecte de respiració d'un sol LED).

**Punts clau:** `write_analog(valor)` accepta **0-1023** (no 0-255): és PWM real, un parpelleig tan ràpid (uns 50 Hz per defecte) que l'ull el veu com a "mitja llum". El **so** funciona igual: `music.pitch(freq, duration)` genera un to d'una freqüència concreta; `music.play(['C4:4', 'E4:4', ...])` reprodueix una melodia com a llista de notes.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| `write_analog(500)` no fa res de diferent que `write_digital(1)` | S'ha confós l'escala 0-1023 amb 0-1 | Recordar: `write_analog` sempre porta un número entre 0 i 1023. |
| El so no se sent | Volum del brunzidor extern baix, o s'ha usat `sleep()` sense esperar que acabi la nota | `music.play()` **espera** que acabi; si es vol so no bloquejant, cal `music.play(..., wait=False)`. |
| El LED RGB només mostra un color | Falten canals: cal `write_analog` als **tres** pins (R, G, B) per barrejar | Repassar la taula de pins de l'[esquema](SA2_esquemes_connexions.md). |

---

## SESSIÓ 3 (2 h) — Repte «semàfor o llum d'ambient» (producte de la SA)

> 🎯 **Producte de la SA.** Aquest repte **fa de producte** de la SA2: s'avalua amb R1 (codi) i R2 (muntatge). És també la **primera retallada** del pla de contingència horari (vegeu `08_Sequenciacio_temporal_anual.md`): si cal recuperar temps, la S4 s'allibera sencera per a la fabricació i aquest repte fa de producte final sense necessitat d'ampliar-lo.

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Presenta l'encàrrec: *"un semàfor o una llum d'ambient que reacciona sola"*. Mostra [`semafor_rele.py`](codi/semafor_rele/semafor_rele.py) **sense executar-lo** (PRIMM). 🥋 **Kata del dia:** K02 (variables) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Prediuen la seqüència de colors i temps. |
| Explicació | 15' | Introdueix el **relé** (Kit 3): commuta un circuit extern (p. ex. un llum de 5-12 V aliè a la micro:bit) amb un senyal digital de control; **seguretat**: el relé aïlla el circuit extern, no es toca mai el costat d'alta tensió. | Anoten com es cablegen la bobina i els contactes del relé. |
| Repte | 75' | Acompanya el muntatge i la programació individual: seqüència de LED/RGB/brunzidor amb bucles i temporitzacions + relé per commutar el circuit extern. | Munten i programen el seu repte (Activitat 3, producte). |
| Mini-defensa + tancament | 20' | **Mini-defensa oral (1', R4·DO):** cada alumne/a explica en veu alta **què fa** el seu semàfor i **una decisió** presa (per exemple, per què aquest ordre de colors o aquests temps). No cal acabar-lo del tot per defensar-lo. | Fan la mini-defensa; anoten al quadern la decisió que han justificat. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **l'ús del relé** (deixa el repte només amb LED/RGB/brunzidor; el relé queda com a ampliació ⭐).

**Punts clau:** el relé és un **interruptor controlat per software**: la bobina (costat baixa tensió, controlada per `write_digital` des del Micro:shield) obre o tanca un contacte mecànic (costat del circuit extern). Permet que un senyal de 3,3 V governi un circuit de tensió i corrent molt més grans **sense connectar-los directament**.

**Mini-rúbrica de la defensa (R4·DO, `07_Rúbriques.md`):** a la SA2 només es valora **Claredat** de manera formativa i s'hi **inicia** la justificació d'una decisió tècnica; el nivell exigent (les 3 dimensions) arriba a partir de la SA4.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El relé fa "clic" però el circuit extern no s'engega | Contactes NO/NC intercanviats, o el circuit extern sense la seva pròpia alimentació | Repassar l'[esquema](SA2_esquemes_connexions.md): el relé **no alimenta** el circuit extern, només el commuta. |
| El semàfor no es repeteix mai igual | Temps de `sleep()` diferents cada cop sense voler-ho (valors escrits a mà en diversos llocs) | Extreure els temps a **variables** al principi del programa (una sola font de veritat). |
| La mini-defensa es queda en "perquè sí" | No s'ha preparat cap decisió abans | Recordar la R4·DO abans de començar el repte: "quina decisió pots justificar?". |

---

## SESSIÓ 4 (2 h) — Fabricació i muntatge de la mascota

> 🧵 **Fil conductor.** Aquesta sessió és la fabricació del **Projecte T1 · La mascota reactiva** (dossier complet: [`00_Projecte_T1_Mascota.md`](../00_General/00_Projecte_T1_Mascota.md)). No hi ha codi nou: el que ja funciona a `codi/` (LED a P1, so) és el que anirà **dins** de la mascota; els sensors (SA3) hi entraran més endavant.

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Reparteix les peces pretallades (personalitzades per alumne/a, tallades fora d'horari) i la llista de peces del dossier. 🥋 **Kata del dia:** K03 (for-range) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Comproven que tenen totes les peces (§ Llista de peces del dossier). |
| Muntatge | 80' | Acompanya el muntatge pas a pas (§ Muntatge del dossier): base i laterals, fixació de la micro:bit + Micro:shield, servo a la tapa, LED i brunzidor a la boca, cablatge segons la taula de pins del dossier. | Munten la carcassa i cablegen els components, seguint la taula de pins. |
| Prova d'encesa | 20' | Supervisa la **prova d'encesa** (§ del dossier): carregar `led_parpelleig.py` per comprovar que el LED de P1 de la mascota respon i `musica_altaveu.py` per validar el brunzidor/altaveu; comprovar que el servo es mou lliurement a mà (**no es programa encara**). | Carreguen `led_parpelleig.py` i `musica_altaveu.py` per validar el cablatge del LED i del so; deixen la tapa sense encolar. |
| Tancament | 10' | Checklist de muntatge i **retorn ordenat del material** (cargols, retalls sobrants). Anuncia la SA3 (sensors de la mascota). | Omplen el [checklist alumnat](SA2_checklist_alumnat.md) §muntatge i entreguen el material sobrant. |

> ⏱️ **Marge:** aquesta sessió **es pot alliberar sencera** (pla de contingència, `08_Sequenciacio_temporal_anual.md`): si cal recuperar temps, el repte de la S3 ja fa de producte avaluable i la fabricació es reprograma a la primera sessió lliure sense penalitzar la nota.

**Punts clau:** el LED i el so de la mascota **ja funcionen** perquè són el mateix codi de `codi/led_parpelleig` i `codi/musica_altaveu` adaptat als pins del dossier (només P1 i P2: la mascota **no** fa servir el LED RGB de `pwm_led_rgb`, perquè al seu cablatge complet P8 i P12 ja són el PIR i el polsador de la SA3, i escriure-hi PWM ara entraria en conflicte amb aquests sensors); el que hi ha de nou avui és **mecànic** (muntatge físic), no de programació. El servo es mourà de manera programada a la **SA4**.

**Producte de la SA:** repte «semàfor o llum d'ambient» (LED/RGB/brunzidor/relé amb bucles i PWM), tancat i avaluat a la **S3**. Muntatge físic de la **mascota** a la **S4** (avaluat amb la rúbrica de muntatge del dossier, R2).

### Mapa d'avaluació (traçabilitat)

| Instrument | Què evidencia | Criteri | Rúbrica | Qualifica? |
|---|---|---|---|---|
| Mini-check (S2) | Bucle amb sortida digital sense apunts | CA1.1 | — | **No** (radar formatiu) |
| Fitxa d'alumnat (Act. 1-2) | Sortides digitals i PWM bàsiques | CA2.1, CA2.2 | R1 | Formativa |
| Repte «semàfor/llum d'ambient» (S3, producte) | Integració de sortides amb bucles i PWM | CA1.1, CA2.1, CA2.2 | **R1**, **R2** | Sí |
| Mini-defensa (S3, R4·DO) | Claredat + inici de justificació d'una decisió | CA5.2 | **R4** (fila «Defensa oral») | Sí |
| Muntatge de la mascota (S4) | Muntatge físic i cablatge segur | CA2.1 | **R2** (criteri «Muntatge») | Sí |
| Quadern tècnic | Documentació i reflexió del procés | CA5.2 | **R4** | Sí |
| Observació d'aula | Autonomia i seguretat amb el maquinari | CA5.3 | **R5** | Sí |

*(CA1.1 = escriure i depurar programes MicroPython amb estructures de control; CA2.1 = connectar i experimentar amb sensors i actuadors del Micro:shield/Keyestudio amb seguretat; CA2.2 = mesurar i interpretar magnituds i senyals digitals/analògics/PWM. Vegeu [`Programació didàctica/06_Avaluacio_criteris_qualificacio.md`](../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md).)*

### Quadern tècnic — entrada de la SA2 (guia per a l'alumnat)

Segueix el mètode de projecte:
- **Què he après** (sortides digitals vs PWM, `write_analog`, `music`, relé).
- **El repte i com l'he resolt** (predicció → cablatge → codi → millores del semàfor).
- **Un error que he tingut i com l'he resolt.**
- **Mascota (S4):** foto/descripció del muntatge i què falta per a la SA3.

> Comparteix les rúbriques **R1**, **R2** i **R4** amb l'alumnat **abans** de començar el repte (avaluació formativa).

### Pont cap a la SA3

A la SA2 hem **actuat** sobre el món exterior (LED, so, relé). A la **SA3** farem el camí invers: **percebre'l** amb sensors (botons, llum, temperatura, ultrasons) i decidir què fer segons el que llegim — el mateix Micro:shield, ara amb entrades.

---

## Guió de modelatge (què verbalitzar)

- **S1 · Sortida digital:** connecta el LED en directe davant la classe i pregunta *"què li he d'enviar perquè s'encengui: un número o un sí/no?"* — porta la resposta cap al `write_digital(1)`. *Error a anticipar:* oblidar `write_digital(0)` i pensar que el LED "s'apaga sol".
- **S2 · PWM:** puja i baixa la intensitat del LED **en directe** movent el valor de `write_analog` amb el REPL (`0`, `300`, `700`, `1023`) perquè es vegi el canvi progressiu abans d'escriure el bucle de respiració. *Error a anticipar:* confondre l'escala 0-1023 amb 0-255 (percentatge visual) o amb 0-1 (digital).
- **S3 · El relé:** ensenya físicament el relé i pregunta *"per què no connecto directament un llum de 230 V a la micro:bit?"* — porta la resposta cap a l'aïllament elèctric. *Error a anticipar:* pensar que el relé "dona corrent" al circuit extern (en realitat només el commuta; l'alimentació del circuit extern és independent).

## Atenció a la diversitat

| Necessitat | Mesura |
|---|---|
| **Bastida (qui ho necessita)** | Esquelet `# TODO` a la secció «Si t'encalles» de la pàgina de pràctica de [`semafor_rele`](codi/semafor_rele/EXPLICACIO.md); temps de `sleep()` ja proposats a la fitxa. |
| **+ Ampliació (qui va sobrat)** | Seqüència de llums sincronitzada amb el so (`pwm_led_rgb` + `musica_altaveu` combinats); ús combinat de relé i LED RGB en un patró propi (vegeu [Reptes de la SA2](../../Reptes/Reptes_SA2.md)). |
| **Diversitat lingüística/lectora** | Taula de pins amb icones de component (no només noms); glossari a [`00_Glossari_tecnic.md`](../00_General/00_Glossari_tecnic.md). |
| **Sense maquinari per a tothom** | El simulador de python.microbit.org **no** reprodueix el LED extern, el LED RGB, el brunzidor ni el relé (només matriu, botons i so intern): qui no tingui placa treballa per torns o simula la **lògica** del programa (comentaris de "aquí s'encendria el LED verd") per validar-la després amb maquinari real. |

> **Avaluació formativa:** comparteix les rúbriques **R1**, **R2** i **R4** amb l'alumnat **abans** de començar el producte.

## Pensament computacional i depuració

- **Concepte de PC d'aquesta SA:** **abstracció** (un `write_analog(700)` amaga tot el parpelleig ràpid que fa la placa per darrere; un `music.play([...])` amaga la generació de cada ona sonora). Nomena-ho explícitament quan expliquis PWM.
- **Depuració:** continua la rutina **DEPURA** (SA1), ara amb un pas nou: **mesura** (comprova amb el REPL el valor real que estàs enviant a un pin abans de sospitar del component).

## Avaluació formativa (instruments)

- **Mini-check** (S2): radar formatiu, no qualifica.
- **Mini-defensa (S3, R4·DO):** primer graó de la progressió de defenses orals (vegeu `07_Rúbriques.md`).
- **Exit ticket** (fitxa ampliada): 3 preguntes de tancament.

## Context real i ODS

- **Context:** semàfors, llums d'ambient domòtiques, avisadors sonors i relés en electrodomèstics reals.
- **ODS 7** (energia assequible i no contaminant): el PWM permet **estalviar energia** regulant la intensitat en lloc d'encendre a plena potència sempre. **ODS 11** (ciutats i comunitats sostenibles): semàfors i enllumenat intel·ligent.
