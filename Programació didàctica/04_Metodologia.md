# 04 · Metodologia

## 4.1. Principis metodològics

La matèria adopta un **enfocament competencial** basat en **situacions d'aprenentatge** contextualitzades, coherent amb el Decret 171/2022, i un format de **treball individual** en totes les activitats. Principis:

- **Aprendre fent** (*learning by doing*) i **fes-ho tu mateix** (*DIY*): cada concepte es consolida amb una pràctica real amb el propi maquinari.
- **Aprenentatge basat en projectes (ABP)** i en **reptes**: les unitats culminen en un producte/repte individual, ampliat des de la SA2 amb un **repte ⭐ de nucli obligatori** (mateix temps de pràctica ja previst; ⭐⭐/⭐⭐⭐ resten ampliació opcional) que garanteix que tothom escriu codi nou, no només llegit o modificat, a cada SA.
- **Recuperació espaiada de la memòria** (*retrieval practice*): cada sessió des de la S4 obre amb una **kata d'activació** de 10' (banc a `Classes/00_General/00_Banc_activacio_repas.md`) que reprèn un concepte de fa 1-2 setmanes amb progressió Parsons → completar buits → escriure de zero.
- **Mini-check d'escriptura individual, un per SA** (`Classes/00_General/00_Mini_checks_individuals.md`): 10' escrivint codi sense apunts, radar formatiu que **no qualifica el dia que es fa**; el **millor dels tres del trimestre sí qualifica** (5 % dins «Proves pràctiques» — detall a `06_Avaluacio_criteris_qualificacio.md` §6.3).
- **Design thinking**: iteració, prototip mínim viable, millora contínua, sempre sobre el fil conductor propi (mascota/vehicle/rover).
- **L'error com a part de l'aprenentatge**: la depuració (*debugging*) és contingut, no fracàs.
- **Progressió del concret a l'abstracte**: del component físic al sistema autònom; del codi guiat al codi autònom.

## 4.2. Estructura tipus d'una sessió (2 h)

| Fase | Temps | Descripció |
|---|---|---|
| **0. Arrencada i preparació** | 5-10' | Repartiment i recompte de material individual, encesa d'ordinadors, obrir l'editor MicroPython. **No es pot ometre:** és temps real d'aula. |
| **Activació** | 10' | Repte o pregunta inicial; recuperació del que se sap. Inclou la **graella de repàs espaiat** (5': 3 preguntes retrospectives — sessió anterior · SA anterior · trimestre —, tothom escriu, no qualifica). Banc complet per sessió: `../Classes/00_General/00_Banc_activacio_repas.md`. |
| **Modelatge (amb PRIMM)** | 20' | El docent mostra el concepte/codi clau (live coding). **Predir abans d'executar:** projecta el codi nou **sense executar-lo** i recull prediccions (~5') *abans* d'investigar-lo. |
| **Pràctica guiada** | 30-40' | Cada alumne replica i modifica **individualment** al seu maquinari. |
| **Pràctica autònoma / repte** | 30-40' | Repte obert individual que aplica el concepte. El **"+ repte"** fa de marge: s'escurça si la sessió va justa. |
| **Tancament i registre** | 10' | Posada en comú, autoavaluació i **quadern tècnic** (*logbook*) individual. |
| **Recollida** | 5' | Desconnexió segura, recompte i ordre del material propi. |

> ⏱️ **Temps realista (important per a la planificació):** la suma de les fases nuclears és de ~110-120', però **l'arrencada i la recollida (15-20') són temps real** que sovint no es pressuposta. El temps lectiu efectiu d'una sessió de 2 h és de ~95-105'. Per no quedar endarrerit: tracta el **registre del quadern com a distribuït** (2-3' després del modelatge i del repte, no tot al final) i considera el **"+ repte" com a marge**, no com a obligatori.

## 4.2 bis. De llegir codi a escriure'l: retirada progressiva de la bastida

Amb PRIMM l'alumnat sempre parteix de **codi donat**; el projecte final (SA9) demana **escriure'n de propi**. Perquè el salt no es faci de cop, la bastida es retira **per graons planificats**:

| Tram | Bastida | Què fa l'alumnat |
|---|---|---|
| **SA1–SA3** | PRIMM complet sobre codi donat. | Prediu, modifica i amplia programes MicroPython. **Des de la SA3**, abans de codificar el repte escriu el **pseudocodi (3–5 línies)** al quadern: és el pas *Dissenyar* del mètode de projecte fet visible. |
| **SA4–SA6** | Codi donat com a **referència**, no com a plantilla. | La fase **Crea** de cada repte parteix del **pseudocodi propi**; el programa de la sessió es consulta, no es retoca. |
| **SA7–SA8** | Full-xuleta d'API (`microbit`, `radio`, sensors), sense estructura; el repte ⭐ segueix partint d'un `.py` donat (com a totes les SA), però amb **menys línies ja fetes** i més pseudocodi propi abans d'obrir l'editor. | Amplia el `.py` de partida a partir del **seu** pseudocodi, sense modelatge línia a línia previ; la bastida «Si t'encalles» de `Reptes_SAn.md` (pistes esglaonades, mai la solució) és l'últim graó abans de programar sense cap suport. |
| **SA9** | Cap (plantilla d'esquelet opcional). | Escriu el seu propi codi (per això la SA9 **no** té PRIMM): tria repte, dissenya i programa el projecte final sense partir de cap `.py` donat. |

**On culmina realment la retirada de bastida:** no hi ha cap repte "a full en blanc" a SA7–SA8 (tots els reptes de `Reptes/Reptes_SAn.md` parteixen d'un `.py` de `Classes/SAn/codi/`, com a la resta del curs). La retirada completa de bastida es dona en dos punts, més tard i més exigents: l'**ítem obligatori de comportament NOU del rover** (2 punts, `Avaluació/Prova_practica_T3.md`) — una funció pròpia que resol un comportament **no treballat a cap sessió del curs**, escrita a la taula, individual i sense partir de cap fitxer donat — i el **projecte SA9**, que sí és, literalment, editor buit des del primer dia.

**El pseudocodi, tal com el demanem** (paraules pròpies, sense sintaxi; una acció per línia):

```
REPETEIX sempre:
    llegeix la distància
    SI distància < 10  → encén el LED i fes sonar el piezo
    SINÓ               → apaga-ho tot
```

> Val igualment un **diagrama de flux** senzill (rombes per a decisions, rectangles per a accions). El pseudocodi/diagrama **s'ensenya abans d'obrir l'editor**: 2 minuts del docent eviten 20 minuts de codi sense rumb.

## 4.3. Agrupaments: treball individual i ajuda entre iguals

- **Tot el treball és individual.** No hi ha parelles de programació ni equips de projecte: cada alumne té el seu propi maquinari (micro:bit V2 + Micro:shield + kit Keyestudio) i construeix, munta i programa el seu propi fil conductor (mascota/vehicle/rover).
- **Dinàmica d'ajuda entre iguals, sense productes compartits:** es fomenta que l'alumnat es consulti dubtes conceptuals i estratègies de depuració (p. ex. «pregunta a dos companys abans de preguntar al docent»), però **cada producte lliurat, cada codi i cada quadern tècnic són exclusivament individuals**. No es dissenyen rúbriques de coavaluació de **grup** ni de repartiment de rols cooperatius: aquí no hi ha equips ni nota compartida.
- **Parella de lectura (5'), coavaluació lleugera i individual:** abans de lliurar el producte/repte de cada SA (des de la SA2), dos alumnes intercanvien la *lectura* (no el codi ni l'edició) amb una checklist de 3 ítems i es diuen l'un a l'altre una cosa a millorar. És feedback formatiu entre iguals, **no qualifica** i no altera l'autoria individual del producte (protocol complet a `Classes/00_General/00_Parella_de_lectura.md`).
- **Moments d'autoavaluació i registre individual** al quadern tècnic propi, a cada sessió.

## 4.4. Eines i entorns

- **Programació:** editor MicroPython de micro:bit (python.microbit.org) o Thonny; MakeCode només com a referència de transició per a alumnat amb menys experiència prèvia.
- **Simulació:** **simulador de python.microbit.org** com a **pla B** quan un component falla, mentre s'espera reposició o per a treball previ a casa.
- **Documentació:** quadern tècnic digital (Markdown / document personal), repositori d'evidències individual.
- **Gestió d'aula:** rúbriques compartides, llistes de verificació, exemples model.

> Els recursos concrets (lliçons, bancs de pràctiques, tutorials) són a `Recursos/`.

## 4.5. El quadern tècnic (*logbook*)

Element vertebrador de l'avaluació contínua. Per a cada pràctica/projecte, cada alumne hi recull **individualment**:
- Objectiu i esquema de connexions.
- **Pseudocodi o diagrama de flux** del repte (pas *Dissenyar* — vegeu §4.2 bis), abans del codi.
- Codi comentat i decisions de disseny.
- Proves realitzades, errors trobats i com s'han resolt.
- Conclusions i possibles millores.
- **Glossari personal:** 3 termes nous per SA, amb l'equivalent en **anglès** i una definició pròpia (a partir de `Classes/00_General/00_Glossari_tecnic.md`): la documentació real de la professió és en anglès, i el pont s'ha de construir des del primer dia.

**Dues entrades que tanquen el bucle metacognitiu** (el registre només ensenya si algú hi torna):
- **«Els meus 3 errors del trimestre»** (tancament de cada trimestre): rellegir els apunts DEPURA propis i triar els 3 errors més instructius — què va passar, com es va trobar, què faig diferent ara. És **repàs actiu** del propi material.
- **Pla de millora personal** després de cada prova trimestral (3 línies: què m'ha fallat · què practicaré · com ho comprovaré), que el docent recupera a l'inici de la SA següent (vegeu les proves de `Avaluació/`).

## 4.6. Perspectiva de gènere i coeducació

Principis (amb l'instrument que els fa operatius entre parèntesis):

- **Igualtat d'accés al maquinari**: en un curs 100 % individual no hi ha risc que els rols tècnics recaiguin sistemàticament en un perfil (tothom té el seu propi kit i el seu propi rover): l'atenció es desplaça a garantir que **tothom programa i munta**, no que uns «deleguen» en altres.
- **Referents en enginyeria i tecnologia** lligats al contingut: un per SA, 1 minut dins l'activació de la S1 (`Classes/00_General/00_Referents_tecnologia.md`).
- **Reptes contextualitzats en àmbits diversos** (salut, sostenibilitat, accessibilitat) per ampliar l'interès.

Pautes de gestió d'aula:

1. **A les defenses orals:** cadascú defensa el seu propi treball (no hi ha «un fa, l'altre presenta», perquè no hi ha equips); torn de preguntes moderat pel docent donant la primera paraula de manera repartida al llarg del trimestre.
2. **Observació:** el desequilibri de participació a les defenses o de demanda d'ajuda és un **indicador trimestral** del sistema (vegeu `06b_Avaluacio_programacio_i_practica_docent.md` §1) — es mesura, no s'intueix.
3. **Llenguatge i exemples:** enunciats i contextos sense marca de gènere implícita (el «tu» genèric, exemples d'usuaris diversos als productes).

## 4.7. Sostenibilitat i ètica (ODS)

- Reutilització de components, gestió de residus electrònics, consum energètic dels sistemes.
- Reflexió sobre l'impacte social de l'automatització i la IA.

## 4.8. Espais

- **Aula taller / laboratori** amb llocs de treball individuals, alimentació i emmagatzematge del material de cada alumne.
- Aula amb dispositius per a programació i simulació.
- Espai obert per a proves de robòtica mòbil (circuits de terra per a SA7 i SA9).

## 4.9. Atenció a la diversitat (resum)

Es despleguen mesures universals, addicionals i intensives detallades a `05_Atencio_a_la_diversitat.md`: activitats multinivell, reptes d'ampliació, bastides (codi base, plantilles) i suport individualitzat.
