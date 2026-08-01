# SA6 · Guia docent — Control: el robot decideix

**Durada:** 8 h (4 sessions de 2 h; la S4 és, SENCERA, la **prova pràctica T2**) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 1 (LED/actuadors), Kit 2 (sensor de temperatura, motoreductors ja muntats) i Kit 3 (relé, DHT11); vehicle T2 muntat a la SA4 i controlat per ràdio des de la SA5 · **Llenguatge:** MicroPython
**Referència:** [`Programació didàctica/15_SA6_Control_el_robot_decideix.md`](../../Programació%20didàctica/15_SA6_Control_el_robot_decideix.md) · **Criteris:** CA1.1, CA2.1, CA3.1 · **Rúbriques:** R1, R3, R4

> 🧭 **Com s'usa aquesta guia.** **Abans de la SA:** objectius, materials i logística (la llista, al checklist docent). **A cada sessió:** la secció «SESSIÓ n» corresponent, amb el «Guió de modelatge» a mà. **En avaluar:** «Mapa d'avaluació». **Per contextualitzar:** context real i ODS.

## Objectius de la SA
1. Distingir un sistema de **llaç obert** d'un de **llaç tancat** i identificar-ne exemples al vehicle.
2. Implementar una **màquina d'estats finits** senzilla (RUN/STOP/ALERTA) amb condicionals.
3. Programar una **aturada d'emergència** que interromp qualsevol altra acció en curs, sigui quin sigui l'origen (polsador o ràdio).
4. Integrar un sensor (temperatura/relé) com a realimentació d'un sistema de control bàsic, amb **histèresi** (no control proporcional).

## Materials per a la sessió
- 1 micro:bit V2 + 1 Micro:shield per alumne/a + cable micro-USB (dotació individual, vegeu [`09c_Inventari_kits_disponibles.md`](../../Programació%20didàctica/09c_Inventari_kits_disponibles.md)).
- El **vehicle T2** muntat a la SA4 i amb el protocol de ràdio de la SA5, portat per l'alumnat; portapiles carregades.
- Kit 3: **relé** i **DHT11** (ampliació de S3). Cap component nou és imprescindible per al nucli: la histèresi es prova amb el sensor de temperatura **intern** (`temperature()`).
- Ordinadors amb accés a **python.microbit.org**. Projector. Quadern tècnic (digital).

## Documents de la SA (aquesta carpeta)
| Document | Quan s'usa |
|---|---|
| [`SA6_fitxa_alumnat.md`](SA6_fitxa_alumnat.md) | Totes les sessions (Activitats 1-3 + producte + quadern). |
| [`SA6_esquemes_connexions.md`](SA6_esquemes_connexions.md) | Sessions 1-3 (pins reutilitzats del vehicle + relé/DHT11 de l'ampliació). |
| `codi/` | `maquina_estats_semafor`, `termostat_histeresi`, `registre_dades` i el repte-producte `vehicle_seguretat`. |
| [`Reptes_SA6.md`](../../Reptes/Reptes_SA6.md) | Sessió 3, en acabar el producte: repte **⭐** (nucli obligatori, mateix temps de pràctica que ja hi havia). Reptes ⭐⭐/⭐⭐⭐, ampliació opcional. |

> Cada programa de `codi/` té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs, l'`EXPLICACIO.md` de la seva carpeta). El «Guió de modelatge» oral de sota continua sent teu.

---

## SESSIÓ 1 (2 h) — Llaç obert i llaç tancat: la màquina d'estats

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Repte inicial: *"Com fas que un vehicle teledirigit s'aturi SEMPRE que calgui, encara que estigui fent una altra cosa?"* 🥋 **Kata del dia:** K10 (ràdio) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Formulen hipòtesis: què fa que una ordre "guanyi" sempre a les altres? |
| Explicació | 30' | **Llaç obert** (el vehicle segueix una comanda fixa, sense comprovar res) vs **llaç tancat** (el sistema comprova un sensor i hi reacciona: consigna, error, realimentació). Introdueix la **màquina d'estats finits (FSM)**: una variable d'estat + transicions. Modelatge de [`maquina_estats_semafor.py`](codi/maquina_estats_semafor/EXPLICACIO.md). | Prenen notes; distingeixen exemples propis de llaç obert i llaç tancat al vehicle (SA4-SA5). |
| Pràctica | 50' | Acompanya el disseny del **diagrama RUN/STOP/ALERTA** (paper o pissarra) abans d'escriure cap codi (Predicció → disseny). Modelatge de [`termostat_histeresi.py`](codi/termostat_histeresi/EXPLICACIO.md) com a primer exemple de **llaç tancat amb realimentació**: per què un únic llindar fa "clic-clic" i com ho resol la **histèresi** (dos llindars). | Dissenyen el seu diagrama d'estats; proven `maquina_estats_semafor.py` i `termostat_histeresi.py` (Activitat 1 de la fitxa). |
| Tancament | 20' | Recull dubtes; anticipa que la Sessió 2 converteix el diagrama en un STOP real i prioritari. | Entrada del quadern: diagrama d'estats propi + per què calen dos llindars a un termòstat. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer l'explicació detallada del **diccionari `TRANSICIONS`** de `maquina_estats_semafor.py` (Bloc 2 de l'[EXPLICACIO](codi/maquina_estats_semafor/EXPLICACIO.md)): mostra directament la versió amb `if`/`elif` encadenats de la secció «Si t'encalles» del mateix document, equivalent i més ràpida d'explicar en un grup que ja porta retard.

**Punts clau:** un sistema de **llaç obert** executa una acció fixa sense comprovar el resultat; un de **llaç tancat** llegeix un sensor (realimentació) i ajusta l'acció en conseqüència. Una **màquina d'estats finits** té sempre una **única** variable d'estat i **transicions** clares entre estats. La **histèresi** (dos llindars, no un) evita que un sistema tot/res oscil·li ràpidament al voltant d'un valor de consigna.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| Confondre llaç obert i llaç tancat | No identifiquen si hi ha o no una lectura de sensor que influeix en la decisió | Preguntar explícitament: "què passaria si el sensor es desconnectés? Canviaria el comportament?" |
| El diagrama d'estats té transicions "impossibles" (de qualsevol estat a qualsevol altre sense condició) | Encara no distingeixen estat de transició | Repassar l'exemple del semàfor: cada fletxa del diagrama porta una condició o un temps |
| Un sol llindar al termòstat | No han vist encara el problema del "clic-clic" en directe | Fer-los observar la lectura de `temperature()` al REPL: balla uns dècims fins i tot sense tocar res |

---

## SESSIÓ 2 (2 h) — Aturada d'emergència prioritària

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Mini-check | 10' | **Mini-check individual** (10', sense apunts, sobre la histèresi de la Sessió 1; banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md#sa6--mini-check-inici-de-la-sessió-2)). | Fan el mini-check (no qualifica). |
| Explicació | 25' | Introdueix l'estat **STOP** com a **prioritari sobre qualsevol altre**: es dispara amb el **polsador manual** (P12) del xassís **o** amb una **comanda de ràdio dedicada** (`"X"`), i interromp el moviment a l'instant. Modelatge de `actualitza_estat()` a [`vehicle_seguretat.py`](codi/vehicle_seguretat/EXPLICACIO.md): un únic lloc que canvia l'estat i sempre atura els motors en entrar a STOP. | Prenen notes; identifiquen per què el polsador s'ha de comprovar **abans** de qualsevol altra cosa a cada volta del bucle. |
| Pràctica | 55' | Acompanya la implementació de l'estat STOP sobre el propi vehicle: polsador P12 (pull-up) i LED indicador P1 (encès fix = RUN, apagat = STOP). Introducció breu de [`registre_dades.py`](codi/registre_dades/EXPLICACIO.md) (mòdul `log` natiu) com a eina per documentar el quadern tècnic amb dades reals. | Programen l'STOP prioritari sobre `vehicle_seguretat.py`; proven `registre_dades.py` i llegeixen `MY_DATA.HTM` per USB (Activitat 2 de la fitxa). |
| Tancament | 20' | Recull dubtes; anticipa la integració del sensor de temperatura a la Sessió 3. | Documenten al quadern el diagrama d'estats final (estats i transicions, amb l'STOP marcat com a prioritari). |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: `registre_dades.py` (deixa'l com a deures/simulador; l'STOP prioritari és el nucli innegociable d'aquesta sessió).

**Punts clau:** l'estat **STOP** es comprova al **principi** de cada volta del bucle, abans de mirar cap altra entrada: així mai hi ha una finestra de temps en què el vehicle "ignora" l'emergència. Un únic lloc del codi (`actualitza_estat()`) concentra tot el que ha de passar en entrar a STOP (aturar motors, mostrar-ho, actualitzar el LED), perquè cap altra part del programa el pugui "oblidar". El mòdul `log` desa dades a la memòria flash de la placa, llegibles per USB sense cap connexió a Internet.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| L'STOP no interromp el moviment | El polsador es comprova només en algun punt del bucle, no a cada volta | Comprovar el polsador **abans** de processar qualsevol altra comanda, a cada iteració del `while True:` |
| El vehicle no torna a moure's mai després d'un STOP | Falta la transició `STOP -> RUN` amb una ordre de moviment explícita | Revisar que una ordre F/B/L/R faci sortir de STOP, no una comanda qualsevol |
| `MY_DATA.HTM` no apareix | Cal desconnectar/reconnectar la placa per USB després d'haver cridat `log.add()` almenys un cop | Provar-ho amb la placa endollada de nou |

---

## SESSIÓ 3 (2 h) — Repte «vehicle amb aturada d'emergència» (producte de la SA — es tanca el Projecte T2)

> 🎯 **Producte de la SA6.** Aquest repte **tanca el Projecte T2**: s'avalua amb **R1** (funcionament), **R3** (criteri "Autonomia/control") i **R4** (documentació i defensa). El sensor de temperatura/relé i l'estat ALERTA són **+ampliació**, no nucli.
>
> 🤝 **Parella de lectura (5')** abans de lliurar — vegeu `Classes/00_General/00_Parella_de_lectura.md`.

> ⭐ **Repte nucli obligatori.** Un cop tancat el producte, tothom fa el repte **⭐** de [`Reptes_SA6.md`](../../Reptes/Reptes_SA6.md) (termòstat de dues zones), aprofitant el mateix temps de pràctica que abans es destinava opcionalment a l'ampliació, i l'ensenya al docent perquè el validi. Els reptes **⭐⭐/⭐⭐⭐** continuen sent ampliació opcional per a qui vagi sobrat.

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Mostra [`vehicle_seguretat.py`](codi/vehicle_seguretat/EXPLICACIO.md) **sense executar-lo** (PRIMM): pregunta què passa si arriba `"X"` mentre el vehicle avança. 🥋 **Kata del dia:** K11 (llistes) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Prediuen el comportament davant de cada comanda, amb èmfasi en la prioritat de l'STOP. |
| Explicació | 20' | Sensor de temperatura (Kit 2 / intern) i **DHT11** (Kit 3) com a **+ampliació**: exemple de "termòstat" integrat amb la màquina d'estats del vehicle (mateix esquema d'histèresi de la Sessió 1, ara amb el relé del Kit 3). Recorda que **no** és control proporcional. | Prenen notes; qui vagi sobrat integra el sensor com a tercer estat ALERTA (opcional). |
| Repte | 70' | Acompanya el tancament individual del repte «vehicle amb aturada d'emergència»: cadascú prova el **seu** protocol complet (F/B/L/R/S/X) amb el comandament d'un company o del docent. | Tanquen `vehicle_seguretat.py`: protocol de ràdio + màquina d'estats + STOP prioritari + LED. Proven l'STOP amb el polsador i amb `"X"` per ràdio. |
| Tancament | 20' | Recull dubtes; **mini-defensa breu** de cada alumne/a (2-3', R4·DO): decisió de disseny justificada. | Mini-defensa; anoten al quadern el diagrama d'estats final i una decisió justificada. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: l'ampliació del sensor de temperatura/DHT11 (deixa-la com a **+ampliació** per a qui vagi sobrat; l'STOP prioritari amb polsador i ràdio és el nucli innegociable).

**Punts clau:** el vehicle **no aprèn cap funció de moviment nova**: reutilitza `avancar()`/`retrocedir()`/`girar()`/`aturar()` de la SA4 i el protocol `"CMD:"` de la SA5; l'única cosa realment nova és la **màquina d'estats amb STOP prioritari**. La comanda `"X"` té la mateixa prioritat màxima que el polsador físic: totes dues vies criden **exactament** la mateixa funció `actualitza_estat(STOP)`.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| L'STOP per ràdio no funciona però el del polsador sí | El codi de recepció comprova el prefix i l'ordre `"X"` fora de lloc, o abans del `startswith(PREFIX)` | Revisar que `"X"` es tracti igual que qualsevol altra ordre rebuda, dins del bloc que ja comprova el prefix |
| El vehicle "es perd" alguna ordre de STOP per ràdio | Normal en ràdio: no hi ha confirmació de recepció | Recordar que per això el polsador físic és la via de seguretat principal, no només la ràdio |
| La mini-defensa no distingeix STOP prioritari d'un `elif` més | L'alumne encara pensa l'STOP com "una comanda més" | Preguntar: "si el vehicle estigués processant una altra comanda, l'STOP l'interromp igualment?" |

---

## SESSIÓ 4 (2 h) — PROVA PRÀCTICA T2 (individual)

> 📋 **Sessió sencera de prova.** No hi ha modelatge nou: aquesta sessió és **íntegrament** la prova pràctica individual que tanca el 2n trimestre. L'enunciat, els criteris i la logística detallada són a [`Avaluació/Prova_practica_T2.md`](../../Avaluació/Prova_practica_T2.md) (document elaborat a banda de les guies docents de SA).

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Organització | 10' | Reparteix l'enunciat i el material individual necessari; recorda les condicions (individual, sense apunts/ajuda, temps tancat). | Preparen el lloc de treball. |
| Prova | ~100' | Supervisa en silenci; només aclareix dubtes d'enunciat, no de solució. | Realitzen la prova pràctica T2 individualment. |
| Tancament | 10' | Recull el material i les entregues; anuncia quan es publicaran els resultats. | Entreguen el treball fet. |

**Punts clau:** aquesta sessió avalua de manera **individual i tancada** els continguts del 2n trimestre (SA4-SA6): funcions de moviment, ràdio i sistemes de control amb màquina d'estats. Vegeu els criteris i l'enunciat complet a [`Avaluació/Prova_practica_T2.md`](../../Avaluació/Prova_practica_T2.md).

**Producte de la SA:** repte «vehicle amb aturada d'emergència» (control per ràdio + màquina d'estats + STOP prioritari, amb senyal visual de l'estat), tancat i avaluat a la **S3** — **tanca el Projecte T2**. La **S4** és la prova pràctica T2 individual.

### Mapa d'avaluació (traçabilitat)

| Instrument | Què evidencia | Criteri | Rúbrica | Qualifica? |
|---|---|---|---|---|
| Mini-check (S2) | Detectar i corregir l'oscil·lació d'un termòstat sense histèresi | CA3.1 | — | **No** (radar formatiu) |
| Fitxa d'alumnat (Act. 1-2) | FSM, llaç obert/tancat, histèresi, STOP prioritari | CA1.1, CA3.1 | R1 | Formativa |
| Repte «vehicle amb aturada d'emergència» (S3, producte) | Vehicle amb màquina d'estats i STOP prioritari (polsador + ràdio) | CA1.1, CA2.1, CA3.1 | **R1**, **R3** | Sí |
| Repte **⭐** (`Reptes_SA6.md`, S3, nucli obligatori) | Termòstat de dues zones amb histèresi, validat pel docent | CA3.1 | **R1** | Sí |
| Mini-defensa (S3, R4·DO) | Claredat + justificació d'una decisió de disseny de la FSM | CA3.1 | **R4** (fila «Defensa oral») | Sí |
| Quadern tècnic | Diagrames d'estats, taula d'histèresi, registre de dades | CA3.1 | **R4** | Sí |
| Observació d'aula | Autonomia i seguretat en manipular relé/actuadors | — | **R5** | Sí |
| **Prova pràctica T2 (S4)** | Funcions, ràdio i sistemes de control de tot el trimestre | CA1.1, CA2.1, CA3.1 | R1, R3, R4 | **Sí** |

*(CA1.1 = escriure i depurar programes MicroPython amb estructures de control, funcions i biblioteques, comentant el codi; CA2.1 = connectar i experimentar amb sensors i actuadors del Micro:shield/Keyestudio aplicant criteris de seguretat; CA3.1 = implementar sistemes de control (llaç obert/tancat, màquines d'estats) i explicar-ne el funcionament. Vegeu [`Programació didàctica/06_Avaluacio_criteris_qualificacio.md`](../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md).)*

### Quadern tècnic — entrada de la SA6 (guia per a l'alumnat)

Segueix el mètode de projecte:
- **Què he après** (llaç obert/tancat, FSM, histèresi, STOP prioritari, `log`).
- **El repte i com l'he resolt** (diagrama → codi → prova → millora).
- **Un error que he tingut i com l'he resolt.**
- **El meu diagrama d'estats final** (RUN/STOP, i ALERTA si l'has ampliat).

> Comparteix les rúbriques **R1**, **R3** i **R4** amb l'alumnat **abans** de començar el repte (avaluació formativa).

### Pont cap a l'avaluació trimestral

A la SA6 el vehicle ha passat d'obeir ordres puntuals (SA5) a un **sistema de control** amb màquina d'estats i aturada d'emergència prioritària: **es tanca el Projecte T2**. La **S4** avalua individualment tot el 2n trimestre a la prova pràctica T2.

---

## Guió de modelatge (què verbalitzar)

- **S1 · Per què dos llindars:** pregunta *"si aquest termòstat tingués un sol llindar a 25°C, i la temperatura ballés entre 24,8 i 25,2 graus repetidament, què li passaria al relé?"* — porta la resposta cap a la histèresi com a solució, no com a "una regla més".
- **S2 · Per què el polsador es mira primer:** pregunta *"si el polsador es comprovés DESPRÉS de processar un missatge de ràdio, en quin moment concret podria "colar-se" una ordre de moviment abans de l'STOP?"* — porta la resposta cap a l'ordre de les comprovacions dins del bucle, no només a la seva existència.
- **S3 · Mateixa idea, dues vies:** ensenya costat a costat el bloc del polsador i el bloc de la comanda `"X"`: pregunta *"què tenen en comú les dues vies d'activar l'STOP?"* — porta la resposta cap al fet que totes dues criden **la mateixa** funció `actualitza_estat(STOP)`, mai codi duplicat.

## Atenció a la diversitat

| Necessitat | Mesura |
|---|---|
| **Bastida (qui ho necessita)** | Diagrama d'estats model (RUN/STOP/ALERTA) amb transicions ja indicades; esquelet de funció `actualitza_estat()` ja escrit (vegeu l'esquelet de [`00_Projecte_T2_Vehicle.md`](../00_General/00_Projecte_T2_Vehicle.md)). |
| **+ Ampliació (qui va sobrat)** | Un cop fet el repte ⭐ obligatori: reptes **⭐⭐/⭐⭐⭐** (semàfor amb botó prioritari, vehicle amb alerta de temperatura i registre de bord) — vegeu [Reptes de la SA6](../../Reptes/Reptes_SA6.md). |
| **Diversitat lingüística/lectora** | Diagrama d'estats amb icones (fletxes, colors) en lloc de només text; glossari a [`00_Glossari_tecnic.md`](../00_General/00_Glossari_tecnic.md). |
| **Sense vehicle a punt** | Es treballa la lògica de la FSM i de la histèresi al **simulador** (`maquina_estats_semafor.py`, `termostat_histeresi.py`); `vehicle_seguretat.py` necessita el vehicle físic per als motors, però la part de protocol/estats es pot revisar igualment. |

> **Avaluació formativa:** comparteix les rúbriques **R1**, **R3** i **R4** amb l'alumnat **abans** de començar el repte.

## Pensament computacional i depuració

- **Concepte de PC d'aquesta SA:** **abstracció d'estats**: reduir un sistema complex (un vehicle amb motors, ràdio i sensors) a un nombre petit i tancat d'**estats possibles** amb **transicions** clares és el mateix principi que fan servir els ascensors, els semàfors o els caixers automàtics: en cada instant el sistema és en un únic estat conegut, mai en una barreja ambigua.
- **Depuració:** continua la rutina **DEPURA** (SA1-SA5), amb un èmfasi nou: quan una transició d'estat "no es veu" (el LED o el display no canvien), comprova primer si el problema és de **lectura** (el sensor/polsador dona el valor esperat?) o de **decisió** (la condició que hauria de canviar l'estat és correcta?) abans de sospitar de l'actuador.

## Context real i ODS

- **Context:** termòstats domèstics i industrials, ascensors, semàfors, robots de magatzem amb aturada d'emergència obligatòria per normativa de seguretat laboral: tots són sistemes de control amb estats i, en molts casos, amb una aturada prioritària semblant a la d'avui.
- **ODS 9** (indústria, innovació i infraestructura) i **ODS 12** (producció i consum responsables): la histèresi evita el desgast innecessari d'actuadors (menys consum, més durada); l'STOP prioritari és el mateix principi de seguretat que porten els robots industrials reals abans de posar-los en marxa.
