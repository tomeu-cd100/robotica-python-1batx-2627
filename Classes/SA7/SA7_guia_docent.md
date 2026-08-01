# SA7 · Guia docent — Robòtica mòbil: el rover

**Durada:** 8 h (4 sessions de 2 h) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 2 (motoreductors, rodes, seguidor de línia KS0050, sensor d'ultrasons HC-SR04); rover muntat a la Sessió 0 (peces pretallades pel docent) · **Llenguatge:** MicroPython
**Referència:** [`Programació didàctica/16_SA7_Robotica_mobil_el_rover.md`](../../Programació%20didàctica/16_SA7_Robotica_mobil_el_rover.md) · **Criteris:** CA1.1, CA3.1, CA4.1 · **Rúbriques:** R1, R3, R4

> 🧭 **Com s'usa aquesta guia.** **Abans de la SA:** objectius, materials i logística (la llista, al checklist docent), més la **Sessió 0** de muntatge (secció pròpia, abans de tot). **A cada sessió:** la secció «SESSIÓ n» corresponent, amb el «Guió de modelatge» a mà. **En avaluar:** «Mapa d'avaluació». **Per contextualitzar:** context real i ODS.

## Objectius de la SA
1. Relacionar el control de dos motoreductors amb el gir del rover (**cinemàtica diferencial** bàsica).
2. Programar un comportament autònom de **seguidor de línia**.
3. Programar un comportament autònom d'**evitar obstacles** amb el sensor d'ultrasons.
4. Modelitzar una **trajectòria** senzilla combinant girs i avanços temporitzats.

## Materials per a la sessió
- 1 micro:bit V2 + 1 Micro:shield per alumne/a + cable micro-USB (dotació individual, vegeu [`09c_Inventari_kits_disponibles.md`](../../Programació%20didàctica/09c_Inventari_kits_disponibles.md)).
- El **rover T3** (vehicle T2 ampliat amb HC-SR04 i seguidor de línia), muntat a la Sessió 0, portat per l'alumnat; portapiles carregades.
- Circuit de línia a terra (cinta negra sobre fons clar, o full imprès model) per taula, per a la Sessió 2.
- Espai lliure d'obstacles petits (capses, llibres) per a la Sessió 3-4.
- Ordinadors amb accés a **python.microbit.org** (només per a la lògica sense maquinari, vegeu §Simulació de [`SA7_esquemes_connexions.md`](SA7_esquemes_connexions.md)). Projector. Quadern tècnic (digital).

## Documents de la SA (aquesta carpeta)
| Document | Quan s'usa |
|---|---|
| [`SA7_fitxa_alumnat.md`](SA7_fitxa_alumnat.md) | Totes les sessions (Activitats 1-4 + producte + quadern). |
| [`SA7_esquemes_connexions.md`](SA7_esquemes_connexions.md) | Sessions 1-4 (pins de M1/M2 heretats + HC-SR04 + seguidor de línia). |
| `codi/` | `calibratge_motors`, `segueix_linia`, `evita_obstacles` i el producte `rover_missions`. |

> Cada programa de `codi/` té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs, l'`EXPLICACIO.md` de la seva carpeta). El «Guió de modelatge» oral de sota continua sent teu.

---

## SESSIÓ 0 (prèvia a la SA7, no compta a les 8 h) — Muntatge del rover

> 🔧 **Sessió de fabricació, no de programació.** El rover **no és un xassís nou**: és el vehicle de T2 amb dues peces d'ampliació impreses en 3D (suport HC-SR04, suport seguidor de línia). Aquesta sessió es finança per la compressió d'hores de la SA8 (vegeu `Programació didàctica/08_Sequenciacio_temporal_anual.md`, «Fil conductor i consum del marge») i **no forma part** de les 8 h ni dels instruments de la SA7 pròpiament dita.

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Recuperació | 15' | Reparteix el joc de les dues peces noves (ja impreses pel docent, vegeu [`00_Fil_conductor_construccions.md`](../00_General/00_Fil_conductor_construccions.md) §3) a cada alumne/a. | Recupera el seu vehicle T2 (no cal desmuntar-lo). |
| Muntatge | 60' | Acompanya el muntatge: suport de l'HC-SR04 al davant (sensor mirant endavant) i suport del seguidor de línia sota el xassís (KS0050 mirant a terra); recorda el cablatge nou (P1/P2/P0) sense tocar M1/M2. | Cargola/enganxa les dues peces noves i cableja els dos sensors segons [`SA7_esquemes_connexions.md`](SA7_esquemes_connexions.md). |
| Comprovació | 30' | Passa la **checklist de muntatge** (R2, formativa) taula per taula: GND comú, sensors ben orientats, motors intactes. | Prova que el rover encara respon amb les funcions de moviment de la SA4 (sense els sensors nous encara programats). |
| Tancament | 15' | Recull incidències (peça endarrerida, motor espatllat: vegeu «Pla B» de `00_Projecte_T3_Rover.md`). | Deixa el rover a punt per començar la S1. |

**Instrument:** checklist de muntatge, avaluada amb **R2** (criteri "Muntatge"), de caràcter **formatiu**: no compta a les hores ni als instruments de la SA7 (que comencen a la S1). Igual que el muntatge de la mascota (SA2·S4) i del vehicle (SA4·S4).

**Pla B:** si algun dels dos suports nous no arriba imprès a temps, es pot fixar temporalment el sensor amb cinta/brides i seguir programant a la S1-S3; se substitueix pel suport definitiu quan arribi, sense aturar la SA7 (vegeu `00_Fil_conductor_construccions.md` §4).

---

## SESSIÓ 1 (2 h) — Cinemàtica diferencial: el rover gira

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Repte inicial: *"Com fa un robot per seguir una línia pintada a terra o esquivar un obstacle sense que ningú el guiï?"* Revisió ràpida del rover muntat a la Sessió 0. | Formulen hipòtesis: què necessita "saber" el rover per decidir sol? |
| Explicació | 30' | **Cinemàtica diferencial**: el rover gira variant la velocitat/sentit relatiu de cada roda (dues rodes motrius + roda boja). Recorda que `avancar()`/`retrocedir()`/`girar()`/`aturar()` són **exactament** les de la SA4: cap pin nou. Modelatge de [`calibratge_motors.py`](codi/calibratge_motors/EXPLICACIO.md): per què cal compensar la velocitat entre M1 i M2. | Prenen notes; relacionen exemples propis (un cotxe de joguina, una cadira de rodes elèctrica) amb la cinemàtica diferencial. |
| Pràctica | 60' | Acompanya el calibratge individual (proves curtes, ajustar `FACTOR_M1`/`FACTOR_M2`) i les primeres proves de trajectòria (quadrat, gir tancat) amb temps fixos. | Calibren el seu rover perquè vagi recte; proven una trajectòria en quadrat amb girs i avanços temporitzats (Activitat 1 de la fitxa). |
| Tancament | 20' | Recull dubtes; anticipa que la S2 afegeix el primer sensor propi del rover (seguidor de línia). | Entrada del quadern: factors de calibratge propis + croquis de la trajectòria en quadrat provada. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: el nombre de proves de trajectòria (deixa només el quadrat; el gir tancat és opcional).

**Punts clau:** la **cinemàtica diferencial** no necessita cap component nou: és una propietat de com es combinen les velocitats dels dos motors ja programats a la SA4. Sense **calibratge**, un rover amb dos motoreductors "iguals" de fàbrica gairebé sempre es desvia una mica en avançar recte; el calibratge és individual, no un valor universal.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El rover no avança recte i l'alumnat ho atribueix a un "error de codi" | No sap que els motoreductors reals tenen petites diferències de fàbrica | Fer una prova ràpida amb els dos motors per separat (un sol motor engegat cada cop) per veure que giren a velocitats lleugerament diferents |
| Confondre `girar()` (gir sobre l'eix) amb una corba suau | Encara no distingeix les dues formes de canviar de direcció | Mostrar amb el rover al terra: `girar()` fa que les rodes girin en sentits oposats (gir sobre l'eix), no com una corba de cotxe |
| El quadrat surt amb angles molt diferents de 90° | Temps de gir no calibrat per al seu rover concret (bateria, fricció) | Ajustar el `sleep()` del gir amb proves curtes fins que s'aproximi a 90° |

---

## SESSIÓ 2 (2 h) — Seguidor de línia

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Mini-check | 10' | **Mini-check individual** (10', sense apunts; banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md#sa7--mini-check-inici-de-la-sessió-2)). Comprova el cicle general **llegir → decidir → actuar** aplicat a un sensor del rover, base comuna del seguidor de línia d'avui i de l'evita-obstacles de la S3. | Fan el mini-check (no qualifica). |
| Explicació | 25' | Sensor **seguidor de línia** KS0050 (Kit 2): lectura amb `read_analog()` (0-1023, com qualsevol entrada analògica de la SA3) i **llindar de detecció**, que cal calibrar sobre el circuit real de l'aula. Modelatge de [`segueix_linia.py`](codi/segueix_linia/EXPLICACIO.md): algorisme de correcció de rumb (girar cap al costat on es perd la línia). | Prenen notes; relacionen el llindar amb el de `nivell_llum.py`/`termometre.py` (SA3). |
| Pràctica | 55' | Acompanya la calibració del llindar taula per taula (cada circuit i cada llum d'aula són una mica diferents) i les proves sobre el circuit de línia. | Calibren `LLINDAR_LINIA` al REPL sobre el seu circuit; proven `segueix_linia.py` (Activitat 2 de la fitxa). |
| Tancament | 20' | Recull dubtes; anticipa l'evita-obstacles de la S3. | Documenten al quadern el llindar triat i una foto/captura del circuit de proves. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: el nombre de circuits provats (deixa'n un de sol per taula, ben calibrat, en lloc de provar-ne diversos).

**Punts clau:** el seguidor de línia és un altre **llaç tancat** (com la histèresi de la SA6): el rover llegeix, decideix i actua a cada volta del bucle, sense cap ordre externa. Amb un **únic** sensor no es pot saber cap a quin costat s'ha desviat de veritat el rover: cal triar una estratègia de cerca fixa (per exemple, girar sempre cap a l'esquerra quan es perd la línia).

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El rover no reacciona mai, sempre avança recte | `LLINDAR_LINIA` mal calibrat per a la il·luminació real | Llegir `SEGUIDOR_LINIA.read_analog()` al REPL sobre la línia i fora d'ella, i triar un llindar entremig |
| El rover gira sense parar, mai troba la línia | Sensor mal orientat, o poc contrast al circuit | Comprovar l'alçada i l'angle del suport; assegurar que el circuit té prou contrast (negre sobre blanc) |
| Funciona a la seva taula i no a una altra | El llindar és específic de cada punt de llum de l'aula | Recalibrar-lo a cada nova ubicació, no assumir que un llindar val per a tota la classe |

---

## SESSIÓ 3 (2 h) — Evita-obstacles amb ultrasons

> 🎯 **Repte "tria un comportament autònom".** Aquest repte pot fer de **producte de la SA** si el calendari ho requereix (pla de contingència, tercera retallada, vegeu doc. 08).

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Mostra [`evita_obstacles.py`](codi/evita_obstacles/EXPLICACIO.md) **sense executar-lo** (PRIMM): pregunta què passa si el rover avança i la distància baixa de 15 cm de cop. | Prediuen el comportament davant d'un obstacle sobtat. |
| Explicació | 25' | Sensor d'**ultrasons HC-SR04**: mesura de distància amb `machine.time_pulse_us`, **exactament** el patró de `alarma_ultrasons.py` (SA3), només canviant de pins (trigger **P1**, echo **P2**; a la SA3 es practicava a P14/P15, ara ocupats pels motors). Funció `mesura_distancia()`. Algorisme d'evita-obstacles: aturar, girar, tornar a mesurar. | Prenen notes; comparen amb el patró de la SA3 i identifiquen què canvia (només els pins) i què no (la lògica del time-of-flight). |
| Repte | 65' | Acompanya el repte **"tria un comportament autònom"**: segons el material disponible a cada taula, cada alumne/a tria seguidor de línia i/o evita-obstacles i el prova a fons. | Trien i proven el seu comportament (Activitat 3 de la fitxa); si sobra temps, proven l'altre. |
| Tancament | 20' | Recull dubtes; anticipa la integració de la S4. | Documenten al quadern quin comportament han triat i per què. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: deixa que cadascú tanqui **només un** comportament (línia o obstacles), l'altre queda com a deures/simulador de lògica.

**Punts clau:** el sensor d'ultrasons **no** llegeix una distància directament: envia un pols i mesura el temps de vol de l'eco, exactament com a la SA3. El canvi de pins (de P14/P15 a P1/P2) és **deliberat**: al rover, P14/P15 són ara dels motoreductors (fixats des de la SA4), i el fil conductor del curs documenta aquest canvi explícitament perquè no sembli un error.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| `mesura_distancia()` retorna sempre `None` | Cablatge de trigger/echo intercanviat, o als pins vells (P14/P15) en lloc dels nous (P1/P2) | Revisar [`SA7_esquemes_connexions.md`](SA7_esquemes_connexions.md): trigger **P1**, echo **P2** |
| El rover xoca abans d'aturar-se | `LLINDAR_OBSTACLE_CM` massa baix per a la velocitat d'avanç | Pujar el llindar o reduir la velocitat d'avanç |
| El rover gira i torna a topar amb el mateix obstacle | Temps de gir massa curt per a l'amplada real de l'obstacle | Allargar el `sleep()` del gir, provant amb obstacles reals de l'aula |

---

## SESSIÓ 4 (2 h) — Integració: missions del rover (producte de la SA)

> 🎯 **Producte de la SA7.** Aquest programa **tanca** la SA: s'avalua amb **R1** (funcionament), **R3** (criteri "Autonomia/control") i **R4** (documentació i defensa).

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Recorda el comportament triat a la S3; introdueix la idea de **missió**: combinar més d'un comportament (o afegir-hi millores) sobre una pista real. | Recuperen el seu comportament de la S3. |
| Explicació | 15' | Modelatge de [`rover_missions.py`](codi/rover_missions/EXPLICACIO.md): com se seleccionen missions amb els botons, i com el **polsador STOP** (P12, pull-up, mateix patró prioritari que `vehicle_seguretat.py` de la SA6) es comprova **sempre primer**. | Prenen notes; identifiquen per què cal comprovar el STOP dins de cada missió, no només al bucle principal. |
| Repte | 75' | Acompanya la integració individual: el comportament triat (línia i/o obstacles) amb **millores** (velocitat variable, marge de seguretat) sobre una pista de proves. | Integren i milloren el seu comportament autònom (Activitat 4 de la fitxa, producte). Proven amb obstacles i/o circuit reals. |
| Tancament | 20' | Recull dubtes; **mini-defensa breu** de cada alumne/a (2-3', R4·DO): una decisió de disseny justificada. | Mini-defensa; anoten al quadern la millora aplicada i per què. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: l'ampliació "combinar línia I obstacles en una sola missió" (deixa-la per a qui vagi sobrat; un únic comportament ben integrat i documentat és el nucli innegociable).

**Punts clau:** el rover **no aprèn cap funció de moviment nova**: reutilitza `avancar()`/`retrocedir()`/`girar()`/`aturar()` de la SA4 tal com ja calibrades a la S1. L'única cosa realment nova de la S4 és la **integració**: combinar comportaments ja programats per separat en una sola estructura de missions, amb un polsador STOP que els talla tots per igual.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| El polsador STOP no atura la missió a l'instant | Es comprova només al bucle principal, no dins del bucle intern de cada missió | Revisar que **cada** missió (`missio_quadrat`, `missio_paret`, `missio_linia`) comprovi el polsador a cada iteració pròpia |
| La mini-defensa no distingeix "integrar" de "copiar i enganxar" | L'alumne encara no ha explicitat quina decisió pròpia ha pres | Preguntar: "quina millora és teva, i per què l'has triat i no una altra?" |
| El comportament triat funciona sol però falla en integrar-se amb la missió | El llindar (línia o obstacle) no s'ha recalibrat sobre la pista final de proves | Recalibrar sempre sobre l'espai real on es farà la mini-defensa, no sobre el de proves inicials |

**Producte de la SA:** comportament autònom del rover (seguidor de línia i/o evita-obstacles), integrat en una estructura de missions, funcional i documentat, amb mini-defensa breu.

### Mapa d'avaluació (traçabilitat)

| Instrument | Què evidencia | Criteri | Rúbrica | Qualifica? |
|---|---|---|---|---|
| Checklist de muntatge (Sessió 0) | Rover muntat correctament (peces noves, cablatge) | — | **R2** | Formativa (no compta a les hores de SA7) |
| Mini-check (S2) | Cicle llegir → decidir → actuar aplicat a un sensor del rover | CA1.1 | — | **No** (radar formatiu) |
| Fitxa d'alumnat (Act. 1-3) | Cinemàtica diferencial, seguidor de línia, evita-obstacles | CA1.1, CA3.1, CA4.1 | R1 | Formativa |
| Producte «comportament autònom del rover» (S4) | Comportament integrat funcional (línia i/o obstacles) | CA1.1, CA3.1, CA4.1 | **R1**, **R3** | Sí |
| Mini-defensa (S4, R4·DO) | Claredat + justificació d'una decisió de disseny/millora | CA3.1 | **R4** (fila «Defensa oral») | Sí |
| Quadern tècnic | Factors de calibratge, llindars, proves de trajectòria | CA4.1 | **R4** | Sí |
| Observació d'aula | Autonomia i seguretat en manipular el rover | — | **R5** | Sí |

*(CA1.1 = escriure i depurar programes MicroPython amb estructures de control, funcions i biblioteques, comentant el codi; CA3.1 = implementar sistemes de control i explicar-ne el funcionament; CA4.1 = analitzar i modelitzar el moviment de sistemes robòtics mòbils senzills. Vegeu [`Programació didàctica/06_Avaluacio_criteris_qualificacio.md`](../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md).)*

### Quadern tècnic — entrada de la SA7 (guia per a l'alumnat)

Segueix el mètode de projecte:
- **Què he après** (cinemàtica diferencial, calibratge, seguidor de línia, evita-obstacles, missions).
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com).
- **Un error que he tingut i com l'he resolt.**
- **Els meus llindars i factors** (LLINDAR_LINIA, LLINDAR_OBSTACLE_CM, FACTOR_M1/FACTOR_M2) i per què els he triat així.

> Comparteix les rúbriques **R1**, **R3** i **R4** amb l'alumnat **abans** de començar el repte (avaluació formativa).

### Pont cap a l'avaluació trimestral

A la SA7 el rover deixa de ser un vehicle teledirigit (T2) i es converteix en una plataforma **autònoma**: decideix sol amb cinemàtica diferencial, un sensor de línia i un sensor d'ultrasons. A la SA8 hi afegirà telemetria per ràdio; a la SA9, el repte lliure individual. La **S4** de SA9 tancarà el 3r trimestre amb la prova pràctica T3.

---

## Guió de modelatge (què verbalitzar)

- **S1 · Per què calibrar:** pregunta *"si els dos motors reben exactament la mateixa consigna de PWM, per què el rover no avança recte?"* — porta la resposta cap a les petites diferències mecàniques reals de fàbrica, no cap a un error de codi.
- **S2 · Per què un llindar i no un valor fix:** pregunta *"si portéssiu el mateix rover a una aula amb més llum natural, la lectura del sensor seria la mateixa sobre la línia negra?"* — porta la resposta cap a la necessitat de calibrar el llindar sobre el circuit i la llum reals, no de memoritzar un número.
- **S3 · Mateix mètode, pins diferents:** ensenya costat a costat `alarma_ultrasons.py` (SA3) i `evita_obstacles.py`: pregunta *"què és exactament igual entre els dos programes, i què és diferent?"* — porta la resposta cap al fet que **només** canvien els pins (P14/P15 → P1/P2), no el mètode de mesura.
- **S4 · Per què el STOP dins de cada missió:** pregunta *"si el polsador només es comprovés al bucle principal, i una missió tingués el seu propi bucle intern llarg, què podria passar?"* — porta la resposta cap a la necessitat de comprovar-lo a **cada** bucle, intern o principal.

## Atenció a la diversitat

| Necessitat | Mesura |
|---|---|
| **Bastida (qui ho necessita)** | Llindars de partida ja indicats (`LLINDAR_LINIA = 500`, `LLINDAR_OBSTACLE_CM = 15`) per calibrar-los a partir d'aquí, no de zero; esquelet de `mesura_distancia()` ja escrit (vegeu l'esquelet de [`00_Projecte_T3_Rover.md`](../00_General/00_Projecte_T3_Rover.md)). |
| **+ Ampliació (qui va sobrat)** | Combinar seguidor de línia I evita-obstacles en un mateix comportament amb prioritats; ajustar la velocitat segons la proximitat (control proporcional bàsic, sense ser el nucli avaluable); vegeu [Reptes de la SA7](../../Reptes/Reptes_SA7.md). |
| **Diversitat lingüística/lectora** | Diagrama del cicle llegir→decidir→actuar amb icones (fletxes, colors) en lloc de només text; glossari a [`00_Glossari_tecnic.md`](../00_General/00_Glossari_tecnic.md). |
| **Sense rover a punt** | Es treballa la lògica al **simulador**, sobre la mateixa estructura de codi però sense el maquinari (pla B: codi per parts amb el rover **alçat** sobre un suport, rodes lliures, per veure els motors respondre sense desplaçar-se); vegeu §Simulació de [`SA7_esquemes_connexions.md`](SA7_esquemes_connexions.md). |

> **Avaluació formativa:** comparteix les rúbriques **R1**, **R3** i **R4** amb l'alumnat **abans** de començar el repte.

## Pensament computacional i depuració

- **Concepte de PC d'aquesta SA:** **modelització de trajectòries**: descompondre un moviment complex (seguir una corba, esquivar un objecte) en una seqüència petita de passos simples (avança, gira, atura) és el mateix principi que fan servir els robots industrials i els vehicles autònoms reals, només amb algorismes molt més sofisticats.
- **Depuració:** continua la rutina **DEPURA** (SA1-SA6), amb un èmfasi nou: quan el rover "no fa el que toca" amb un sensor nou (línia o ultrasons), comprova primer si el problema és de **lectura** (el valor que arriba és el que esperaves, amb el REPL?) abans de sospitar de l'algorisme de decisió o dels motors.

## Context real i ODS

- **Context:** robots de neteja domèstics (seguidor de vora), vehicles autònoms d'inspecció industrial, robots de magatzem que eviten obstacles: tots combinen sensors de percepció senzills amb algorismes de decisió reactius com els d'avui.
- **ODS 9** (indústria, innovació i infraestructura) i **ODS 11** (ciutats i comunitats sostenibles): els robots mòbils autònoms redueixen tasques repetitives i perilloses (inspecció, neteja) i són la base dels vehicles de mobilitat assistida i del transport de mercaderies autònom.
