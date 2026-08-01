# SA3 · Guia docent — Entrades: el robot percep

**Durada:** 8 h (4 sessions de 2 h; la S4 és, SENCERA, la **prova pràctica T1**) · **Maquinari:** micro:bit V2 + Micro:shield; sensors integrats (botons, llum, temperatura, acceleròmetre); Kit Keyestudio 1 (polsador, potenciòmetre, sensor de temperatura bàsic), Kit 2 (sensor de llum, sensor de temperatura, ultrasons HC-SR04, PIR) i Kit 3 (sensor de so, DHT11); mascota muntada a SA2 · **Llenguatge:** MicroPython
**Referència:** [`Programació didàctica/12_SA3_Entrades_el_robot_percep.md`](../../Programació%20didàctica/12_SA3_Entrades_el_robot_percep.md) · **Criteris:** CA1.1, CA2.1, CA2.2 · **Rúbriques:** R1, R2, R3, R4

> 🧭 **Com s'usa aquesta guia.** **Abans de la SA:** objectius, materials i documents de la carpeta (la logística, al checklist docent). **A cada sessió:** la secció «SESSIÓ n» corresponent, amb el «Guió de modelatge» a mà. **En avaluar:** «Mapa d'avaluació». **Per contextualitzar:** context real i ODS.

## Objectius de la SA
1. Llegir entrades **digitals** (botons, polsador) i **analògiques** (potenciòmetre, sensor de llum, sensor de temperatura) i interpretar-ne els valors.
2. Aplicar **condicionals** (`if/elif/else`) per relacionar la lectura d'un sensor amb una acció de sortida.
3. Utilitzar el **REPL/consola** per depurar i visualitzar dades de sensors en temps real.
4. Programar la **mascota expressiva**: reaccions de la matriu LED/so davant estímuls de l'entorn — **es tanca la mascota T1** a la S3.

## Materials per a la sessió
- 1 micro:bit V2 + 1 Micro:shield per alumne/a + cable micro-USB (dotació individual, vegeu [`09c_Inventari_kits_disponibles.md`](../../Programació%20didàctica/09c_Inventari_kits_disponibles.md)).
- Kit Keyestudio 1 (polsador, potenciòmetre, sensor de temperatura bàsic), Kit 2 (sensor de llum, sensor de temperatura, HC-SR04, PIR) i Kit 3 (sensor de so) per alumne/a.
- Ordinadors amb accés a **python.microbit.org** i al **REPL** (webREPL o terminal sèrie). Projector. Quadern tècnic (digital).
- Sessió 3: la **mascota** muntada a la SA2 (S4), amb la caixa oberta i accessible per cablejar.

## Documents de la SA (aquesta carpeta)
| Document | Quan s'usa |
|---|---|
| [`SA3_fitxa_alumnat.md`](SA3_fitxa_alumnat.md) | Totes les sessions (Activitats 1-3 + producte + quadern). |
| [`SA3_esquemes_connexions.md`](SA3_esquemes_connexions.md) | Sessions 1-3 (pins ADC, taula de connexions i pins EXACTES de la mascota). |
| `codi/` | `nivell_llum`, `termometre`, `alarma_ultrasons` i el repte-producte `mascota_reactiva`. |
| [`00_Projecte_T1_Mascota.md`](../00_General/00_Projecte_T1_Mascota.md) | Sessió 3 (cablatge vinculant i tancament de la mascota). |
| [`../../Avaluació/Prova_practica_T1.md`](../../Avaluació/Prova_practica_T1.md) | Sessió 4 (enunciat de la prova). |

> Cada programa de `codi/` té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs, l'`EXPLICACIO.md` de la seva carpeta). El «Guió de modelatge» oral de sota continua sent teu.

---

## El mètode de projecte, aplicat a entrades

Continuem el cicle **analitzar → dissenyar → programar/prototipar → provar → millorar** (SA1-SA2). A la SA3 l'"analitzar" es converteix en *"quin sensor em dona la informació que necessito, i en quina escala?"* (digital 0/1, analògic 0-255 o 0-1023) i el "provar" incorpora una eina nova: el **REPL**, per llegir valors en directe abans d'escriure cap `if`.

---

## SESSIÓ 1 (2 h) — Entrades digitals i condicionals

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Pregunta: *"com sap la teva mascota que li estàs parlant, que hi ha llum o que t'hi acostes?"* (repte inicial de la SA). Recorda el Micro:shield ja muntat. 🥋 **Kata del dia:** K04 (if/while) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Formulen hipòtesis: quins sensors necessitarà la mascota? |
| Explicació | 25' | `button_a.is_pressed()`/`button_b.is_pressed()` amb `if/elif/else`. Introdueix el **polsador extern** (Kit 1): concepte de ***pull-up*** (`pin.set_pull(pin.PULL_UP)`) i **antirebot** (*debounce*, per què un sol clic físic pot llegir-se com molts). | Prenen notes; prediuen quan `is_pressed()` val `True`. |
| Pràctica | 55' | Modelatge en directe al **REPL**: comptador de premudes del polsador (concepte de la fitxa 12, sense fitxer desat: `while True: if pin_polsador.read_digital()==0: comptador += 1`). Introdueix els **sensors integrats** (llum, temperatura) com a primera lectura analògica, sense encara interpretar-la. | Escriuen el comptador al REPL i el proven amb el polsador muntat ([esquemes](SA3_esquemes_connexions.md)) (Activitat 1). |
| Tancament | 20' | Recull dubtes de *pull-up*/antirebot; anticipa la Sessió 2 (entrades analògiques). | Entrada del quadern: primera lectura d'un sensor amb el REPL. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **el polsador extern** de l'Activitat 1 (deixa només els botons A/B interns; el polsador reapareix igualment programat a `mascota_reactiva` a la S3).

**Punts clau:** una entrada **digital** només dona dos valors (`0`/`1`, `is_pressed()`/`read_digital()`), igual que una sortida digital però al revés. El *pull-up* evita que un pin "flotant" doni lectures a l'atzar quan el circuit és obert. L'**antirebot** compara el temps entre deteccions (`running_time()`) per no comptar un sol clic com si fossin deu.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El polsador sembla "fallar" i compta 3-8 premudes d'un sol clic | Rebot mecànic sense antirebot per software | Comparar amb `running_time()` i ignorar deteccions massa properes (vegeu `mascota_reactiva.py`, Sessió 3). |
| `read_digital()` dona valors erràtics sense tocar res | Falta el *pull-up* (`set_pull(PULL_UP)`) | Fixar l'estat de repòs abans de llegir. |
| Es confon `is_pressed()` (botons interns) amb `read_digital()` (pins externs) | Són dues API diferents per a un concepte semblant | Botons A/B → `is_pressed()`; qualsevol altre pin → `read_digital()`. |

---

## SESSIÓ 2 (2 h) — Entrades analògiques: llum i temperatura

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Mini-check | 10' | Passa el **mini-check individual** a l'inici de sessió (banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md#sa3--mini-check-inici-de-la-sessió-2)): `if/else` sobre `display.read_light_level()` de memòria (consolida la S1/introdueix l'analògic). | Responen individualment (no qualifica). |
| Activació | 10' | Recorda l'entrada digital; pregunta: *"i si necessito saber QUANTA llum hi ha, no només si n'hi ha o no?"* | Formulen hipòtesis. |
| Explicació | 25' | **Entrades analògiques**: `read_analog()` (0-1023) i els **sensors integrats** (`display.read_light_level()`, 0-255; `temperature()`, graus C). MicroPython no té `map()`: es programa una funció `mapa()` amb una regla de tres. Potenciòmetre (Kit 1) com a primer exemple pur d'ADC. Recorda els **pins ADC vàlids** (P0, P1, P2, P3, P4, P10) i que **P3/P4/P10 comparteixen circuit amb el display** (`read_analog()` hi falla amb el display actiu): per això les pràctiques d'avui fan servir P0/P1. | Prenen notes; proven `read_analog()` del potenciòmetre en directe al REPL. |
| Pràctica | 55' | Modelatge de [`nivell_llum.py`](codi/nivell_llum/nivell_llum.py) (llum intern vs extern, barres) i [`termometre.py`](codi/termometre/termometre.py) (temperatura intern vs extern, condicionals). | Munten sensor de llum i de temperatura ([esquemes](SA3_esquemes_connexions.md)); escriuen/proven els dos programes (Activitat 2). |
| Tancament | 15' | Recull dubtes; presenta el producte de la S3 (mascota reactiva). | Anoten al quadern el llindar propi triat (per exemple, `LLINDAR_FOSCOR`) i per què. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **el sensor de temperatura extern** de `termometre.py` (deixa només la comparació amb el sensor intern; l'extern reapareix com a ampliació ⭐).

**Punts clau:** una entrada **analògica** dona un rang de valors, no només dos estats; l'escala depèn del sensor (**0-255** per als sensors integrats de llum, **0-1023** per a qualsevol pin ADC). **Mapar** un valor és convertir-lo d'un rang a un altre amb una regla de tres (`mapa()`): la mateixa funció serveix per a llum, temperatura o qualsevol sensor analògic futur. Un **llindar** ben calibrat (mesurat al REPL, no inventat) és la base de tota decisió amb `if`.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| Es confon l'escala 0-255 (sensors integrats) amb la 0-1023 (pins ADC) | No s'ha comprovat quina funció retorna quin rang | Repassar la taula de l'[esquema](SA3_esquemes_connexions.md) §1. |
| `read_analog()` sempre dona 0 o sempre el màxim | El component és a un pin **sense ADC** (fora de P0/P1/P2/P3/P4/P10) | Recablejar a un pin vàlid. |
| `ValueError: Pin in display mode` | El component analògic és a P3, P4 o P10 amb el display actiu (comparteixen circuit) | Recablejar a P0/P1/P2. |
| El llindar "no funciona mai" a l'aula | S'ha copiat un valor d'exemple sense mesurar-lo amb el REPL a l'aula real | Calibrar sempre al REPL, mai a ull. |

---

## SESSIÓ 3 (2 h) — Repte «mascota reactiva» (producte de la SA — es tanca la mascota T1)

> 🎯 **Producte de la SA.** Aquest repte **fa de producte** de la SA3 i **tanca el projecte T1** (la mascota): s'avalua amb **R1** (codi), **R2** (muntatge) i **R3** (compliment del repte, ≥2 reaccions sensor→resposta). Mini-defensa breu (R4·DO).

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Presenta l'HC-SR04 (Kit 2): mesura per **temps de vol**, no per lectura directa. Mostra [`alarma_ultrasons.py`](codi/alarma_ultrasons/alarma_ultrasons.py) **sense executar-lo** (PRIMM). 🥋 **Kata del dia:** K05 (condicionals amb sensors/llindar) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Prediuen a partir de quina distància sonarà l'alarma. |
| Explicació | 20' | Modelatge de `alarma_ultrasons.py`: trigger/echo, `machine.time_pulse_us`, seguretat (5 V, possible divisor de tensió a l'echo). Introdueix el PIR (Kit 2, digital, 30-60 s d'estabilització) i el sensor de so (Kit 3, o `microphone.sound_level()` intern). | Munten l'HC-SR04 ([esquemes](SA3_esquemes_connexions.md)) i proven l'alarma. |
| Repte | 70' | Acompanya el muntatge i la programació individual de **mascota_reactiva**: el cablatge **EXACTE** del dossier (P1 LED, P2 brunzidor, P8 PIR, P12 polsador) i almenys **2 reaccions sensor→resposta** coherents amb la personalitat triada. | Cablegen la mascota segons el dossier i programen [`mascota_reactiva.py`](codi/mascota_reactiva/mascota_reactiva.py) com a punt de partida per al seu propi disseny (Activitat 3, producte). |
| Mini-defensa + tancament | 20' | **Mini-defensa breu (R4·DO):** cada alumne/a explica **quines reaccions** té la seva mascota i **una decisió** de disseny (per exemple, per què aquest llindar de so). Checklist de tancament del producte T1. | Fan la mini-defensa; anoten al quadern les reaccions i els llindars finals. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: **`alarma_ultrasons.py`** com a exercici a part (deixa'l com a ampliació ⭐; l'HC-SR04 **no** forma part del cablatge final de la mascota, així que ometre'l no bloqueja el producte).

**Punts clau:** la mascota reactiva és la **integració** de tot el mètode de la SA3: per a **cada** sensor, llegir → comparar amb un llindar → decidir una reacció (cara + so). El cablatge de la mascota **no és negociable**: ha de quadrar exactament amb la taula del dossier (P1, P2, P8, P12), perquè és el mateix maquinari que es va provar a la SA2 (S4, LED i so) i que es completarà a la SA4 (servo). Un **estímul per volta** (`return` després de cada `canvia_emocio()`) evita que dues reaccions es barregin de manera confusa.

**Mini-rúbrica de la defensa (R4·DO, `07_Rúbriques.md`):** a la SA3 es consolida la justificació d'**una** decisió tècnica (llindar o ordre de prioritat entre estímuls), continuant la progressió iniciada a la SA2.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| La mascota no reacciona mai a un sensor concret | Un sensor de més prioritat "tapa" sempre el seu `if` (falta `return` o ordre mal pensat) | Repassar l'ordre de `llegeix_sensors()` a [`mascota_reactiva.py`](codi/mascota_reactiva/EXPLICACIO.md). |
| El PIR dispara constantment | Temps d'estabilització no respectat, o sensibilitat massa alta | Esperar 30-60 s abans de provar; ajustar el potenciòmetre del mòdul. |
| El polsador "salta" diverses emocions d'un sol toc | Falta l'antirebot per software | Revisar `ANTIREBOT_MS` i la comparació amb `running_time()`. |
| Menys de 2 reaccions completades al final de la sessió | Temps mal repartit, massa polit en una sola reacció | Recorda la prioritat: **2 reaccions fiables** > moltes a mitges (criteri R3). |

---

## SESSIÓ 4 (2 h) — PROVA PRÀCTICA T1 (individual)

> 📋 **Sessió sencera de prova.** No hi ha modelatge nou: aquesta sessió és **íntegrament** la prova pràctica individual que tanca el 1r trimestre. L'enunciat, els criteris i la logística detallada són a [`Avaluació/Prova_practica_T1.md`](../../Avaluació/Prova_practica_T1.md) (document elaborat a banda de les guies docents de SA).

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Organització | 10' | Reparteix l'enunciat i el material individual necessari; recorda les condicions (individual, sense apunts/ajuda, temps tancat). | Preparen el lloc de treball. |
| Prova | ~100' | Supervisa en silenci; només aclareix dubtes d'enunciat, no de solució. | Realitzen la prova pràctica T1 individualment. |
| Tancament | 10' | Recull el material i les entregues; anuncia quan es publicaran els resultats. | Entreguen el treball fet. |

**Punts clau:** aquesta sessió avalua de manera **individual i tancada** els continguts de tot el trimestre (SA1-SA3): entrades i sortides, condicionals, bucles i el mètode de projecte. Vegeu els criteris i l'enunciat complet a [`Avaluació/Prova_practica_T1.md`](../../Avaluació/Prova_practica_T1.md).

**Producte de la SA:** repte «mascota reactiva» (≥2 reaccions sensor→resposta coherents), tancat i avaluat a la **S3** — **tanca el Projecte T1**. La **S4** és la prova pràctica T1 individual.

### Mapa d'avaluació (traçabilitat)

| Instrument | Què evidencia | Criteri | Rúbrica | Qualifica? |
|---|---|---|---|---|
| Mini-check (S2) | `if/else` amb entrada analògica sense apunts | CA1.1 | — | **No** (radar formatiu) |
| Fitxa d'alumnat (Act. 1-2) | Entrades digitals i analògiques bàsiques | CA2.1, CA2.2 | R1 | Formativa |
| Repte «mascota reactiva» (S3, producte) | Integració d'entrades amb condicionals encadenats | CA1.1, CA2.1, CA2.2 | **R1**, **R2**, **R3** | Sí |
| Mini-defensa (S3, R4·DO) | Claredat + justificació d'una decisió (llindar/prioritat) | CA5.2 | **R4** (fila «Defensa oral») | Sí |
| Quadern tècnic | Documentació, lectures de sensor i llindars | CA5.2 | **R4** | Sí |
| Observació d'aula | Autonomia i seguretat amb el maquinari | CA5.3 | **R5** | Sí |
| **Prova pràctica T1** (S4, individual) | Continguts del 1r trimestre (SA1-SA3) | CA1.1, CA2.1, CA2.2 | R1, R2, R4 | Sí |

*(CA1.1 = escriure i depurar programes MicroPython amb estructures de control; CA2.1 = connectar i experimentar amb sensors i actuadors del Micro:shield/Keyestudio amb seguretat; CA2.2 = mesurar i interpretar magnituds i senyals digitals/analògics/PWM. Vegeu [`Programació didàctica/06_Avaluacio_criteris_qualificacio.md`](../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md).)*

### Quadern tècnic — entrada de la SA3 (guia per a l'alumnat)

Segueix el mètode de projecte:
- **Què he après** (entrades digitals vs analògiques, `read_analog()`, `mapa()`, *pull-up*, antirebot, temps de vol).
- **El repte i com l'he resolt** (predicció → cablatge → llindars → codi → reaccions de la mascota).
- **Un error que he tingut i com l'he resolt.**
- **Mascota (tancament):** quines reaccions té, quins llindars ha triat i per què.

> Comparteix les rúbriques **R1**, **R2**, **R3** i **R4** amb l'alumnat **abans** de començar el repte (avaluació formativa).

### Pont cap a la SA4

A la SA3 hem completat el cicle **entrada → decisió → sortida** amb condicionals. A la **SA4** organitzarem aquest codi amb **funcions** pròpies i farem que la mascota (i un nou vehicle) es **mogui**: el servo de les orelles, muntat des de la SA2 però encara sense programar, per fi cobra vida.

---

## Guió de modelatge (què verbalitzar)

- **S1 · Digital i antirebot:** prem el polsador diverses vegades ràpid davant la classe sense antirebot i pregunta *"per què el comptador ha pujat més del que hem premut?"* — porta la resposta cap al rebot mecànic. *Error a anticipar:* pensar que el polsador "està trencat" en lloc d'entendre el rebot.
- **S2 · Mapar un rang:** tapa el sensor de llum amb la mà **en directe** i llegeix el valor al REPL abans i després, perquè es vegi el canvi numèric abans d'escriure `mapa()`. *Error a anticipar:* confondre l'escala 0-255 (llum interna) amb la 0-1023 (pin ADC).
- **S3 · Temps de vol:** pregunta *"com pot un sensor mesurar una distància sense tocar res?"* abans d'ensenyar l'HC-SR04 — porta la resposta cap al so i el temps. *Error a anticipar:* pensar que `time_pulse_us` "llegeix la distància" directament (en realitat mesura temps; la distància es calcula després).

## Atenció a la diversitat

| Necessitat | Mesura |
|---|---|
| **Bastida (qui ho necessita)** | Esquelet `# TODO` a la secció «Si t'encalles» del [dossier de la mascota](../00_General/00_Projecte_T1_Mascota.md#-si-tencalles-lesquelet-del-programa); funció `mapa()` ja donada a la fitxa. |
| **+ Ampliació (qui va sobrat)** | Calibratge fi de llindars; combinar 3+ sensors a la mascota; sincronitzar l'HC-SR04 amb la mascota malgrat no ser al cablatge oficial (vegeu [Reptes de la SA3](../../Reptes/Reptes_SA3.md)). |
| **Diversitat lingüística/lectora** | Taula de pins amb icones de component; glossari a [`00_Glossari_tecnic.md`](../00_General/00_Glossari_tecnic.md). |
| **Sense maquinari per a tothom** | El simulador de python.microbit.org **no** reprodueix cap sensor extern (només llum/temperatura/so interns, acceleròmetre i botons): qui no tingui placa treballa per torns o substitueix temporalment un sensor extern per `button_a.is_pressed()` per validar la **lògica**. |

> **Avaluació formativa:** comparteix les rúbriques **R1**, **R2**, **R3** i **R4** amb l'alumnat **abans** de començar el producte.

## Pensament computacional i depuració

- **Concepte de PC d'aquesta SA:** **descomposició** (separar "llegir el sensor" de "decidir què fer amb el valor" de "executar la reacció" en blocs/funcions diferents, com a `llegeix_sensors()` i `canvia_emocio()`). Nomena-ho explícitament quan modelitzis `mascota_reactiva.py`.
- **Depuració:** continua la rutina **DEPURA** (SA1-SA2), amb un èmfasi nou: **mesura sempre amb el REPL** el valor real d'un sensor abans de triar un llindar (no s'inventa mai un número).

## Avaluació formativa (instruments)

- **Mini-check** (S2): radar formatiu, no qualifica.
- **Mini-defensa (S3, R4·DO):** continua la progressió de defenses orals (vegeu `07_Rúbriques.md`).
- **Exit ticket** (fitxa ampliada): 3 preguntes de tancament.

## Context real i ODS

- **Context:** sensors de presència d'enllumenat automàtic, termòstats domèstics, aparcaments amb sensors d'ultrasons, assistents que responen a la veu.
- **ODS 3** (salut i benestar): sensors de temperatura/humitat en cures de salut i confort. **ODS 11** (ciutats i comunitats sostenibles): sensors de presència i llum que estalvien energia encenent només quan cal.
