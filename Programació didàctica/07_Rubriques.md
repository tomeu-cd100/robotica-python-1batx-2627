# 07 · Rúbriques d'avaluació

Rúbriques reutilitzables amb **quatre nivells**, cadascun lligat a una **banda de nota (0-10)**. A Batxillerat la qualificació és numèrica; els noms només indiquen la banda: **Insuficient = 0-4 · Suficient/Bé = 5-6 · Notable = 7-8 · Excel·lent = 9-10**.

> ⚠️ **No confonguis les rúbriques `R1–R5` amb les competències específiques `CE-R1–CE-R5`** (doc `02`). Són **dos sistemes diferents** que comparteixen numeració: les **rúbriques** avaluen *com de bé* es fa una feina concreta (codi, muntatge…); les **competències** descriuen *què* s'ha d'assolir al curs. Només coincideixen en l'1 i el 2:
>
> | Núm. | **Rúbrica** (R) — instrument d'avaluació | **Competència** (CE-R) — fita del curs |
> |---|---|---|
> | 1 | Programació (codi) | Programar sistemes |
> | 2 | Circuit i electrònica | Construir i experimentar circuits |
> | 3 | **Projecte i robot** | **Automatitzar i controlar** |
> | 4 | **Documentació i comunicació** | **Dissenyar robots i trajectòries** |
> | 5 | **Actitud i autoregulació** | **Projectar i comunicar** |
>
> Quan un repte diu "s'avalua amb R1, R3, R4" es refereix a les **rúbriques** d'aquest document.

---

## R1 · Rúbrica de programació (codi)

| Criteri | Insuficient (0–4) | Suficient/Bé (5–6) | Notable (7–8) | Excel·lent (9–10) |
|---|---|---|---|---|
| **Funcionament** | El programa no s'executa o no fa la tasca. | Fa la tasca bàsica amb errors menors. | Fa la tasca completa de manera fiable. | Funciona i gestiona casos límit/errors. |
| **Estructura** | Codi desordenat, tot al bucle principal. | Alguna funció, poca modularitat. | Ben modularitzat amb funcions. | Modular, reutilitzable i eficient. |
| **Codi escrit per l'alumne mateix** (no copiat de la base) | Còpia gairebé literal de codi de la base/exemple, sense adaptar-lo. | Adapta codi de la base amb canvis mínims (noms, valors), sense estructura pròpia. | Estructures pròpies (funcions/variables/lògica de control) i adaptacions no trivials respecte al material de base. | Disseny propi identificable: decisions d'estructura i nom justificades, no reduïbles a «canviar quatre coses» d'un exemple. |
| **Llegibilitat** | Sense comentaris ni noms clars. | Comentaris escassos. | Comentat i noms significatius. | Documentat de manera professional. |
| **Depuració** | No identifica errors. | Corregeix amb ajuda. | Depura de forma autònoma. | Depura i explica la causa de l'error. |

> **Pes del subcriteri «Codi escrit per l'alumne mateix» (P3.11):** quan la R1 s'aplica a un **producte** (no a un mini-check o kata puntual), aquest subcriteri pesa **com a mínim el 40 %** de la nota de R1 d'aquell producte (els altres criteris —Funcionament, Estructura, Llegibilitat, Depuració— es reparteixen la resta). L'objectiu és que copiar/adaptar trivialment el codi de base d'una SA no pugui, per si sol, treure una nota alta a R1.
>
> **Nota d'aplicació per al docent — com detectar-ho:** durant la validació del producte (mateix moment que la resta de R1), fes una **mini-entrevista de 2 preguntes** sobre el codi lliurat: **(1)** «Assenyala'm una línia o funció que hagis escrit tu i explica'm què fa» — si no la sap localitzar o explicar, és indici de còpia sense comprensió; **(2)** «Per què ho has fet així (aquesta estructura/nom/valor) i no d'una altra manera?» — una resposta amb criteri propi (encara que senzill) indica adaptació real; «perquè sortia així a l'exemple» indica còpia literal. Documenta breument la resposta (una frase) al quadern de seguiment del docent o al `Full_seguiment_grup.md`: serveix d'evidència per si la nota es qüestiona i per detectar patrons repetits de còpia a tot el grup.

## R2 · Rúbrica de circuit i electrònica

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| **Muntatge** | Connexions incorrectes/insegures. | Funciona amb ajuda. | Muntatge correcte i ordenat. | Òptim, net i ben etiquetat. |
| **Esquema** | Inexistent o erroni. | Esquema bàsic. | Esquema correcte amb simbologia. | Esquema professional i documentat. |
| **Mesura/diagnòstic** | No mesura ni interpreta. | Mesura amb ajuda. | Mesura i interpreta senyals. | Diagnostica avaries amb autonomia. |
| **Seguretat** | No aplica normes. | Aplica amb recordatoris. | Aplica les normes. | Model de bones pràctiques. |

> **Nota (Mesura/diagnòstic):** quan no hi ha instrument físic disponible, és evidència vàlida la **lectura calibrada amb el simulador de python.microbit.org** (amb captura al quadern), anotada com a mesura simulada.

## R3 · Rúbrica de projecte i robot

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| **Compliment del repte** | No assoleix els objectius. | Assoleix els mínims. | Assoleix tots els objectius. | Supera els objectius amb millores. |
| **Disseny i iteració** | Sense procés de disseny. | Una sola versió. | Itera amb proves. | Iteració documentada i justificada. |
| **Integració** | Parts inconnexes. | Integració parcial. | Sistema integrat i coherent. | Integració robusta i optimitzada. |
| **Autonomia/control** | No autònom. | Control bàsic. | Control fiable. | Control avançat (realimentació). |

## R4 · Rúbrica de documentació tècnica i comunicació

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| **Quadern tècnic** | Incomplet. | Bàsic. | Complet i ordenat. | Exhaustiu i reflexiu. |
| **Claredat tècnica** | Confús. | Comprensible amb llacunes. | Clar i rigorós. | Rigorós, precís i ben argumentat. |
| **Defensa oral** | No defensa la solució. | Defensa amb dificultats. | Defensa clara. | Defensa convincent i respon dubtes. |
| **Terminologia** | Incorrecta. | Bàsica. | Adequada. | Precisa i professional. |

### R4·DO — Mini-rúbrica de la defensa oral (detall del criteri «Defensa oral» de la R4)

Les defenses orals **es repeteixen tot el curs**: unes puntuen a la R4 (SA2 S3, SA4 S3, SA6 S3, SA9 S4-S5) i unes altres són **mini-defenses purament formatives, sense nota R4** (SA3 S3, SA7 S4) que preparen l'alumnat per a les properes defenses graduades. Fins ara la R4 només tenia una fila genèrica per a la «Defensa oral». Aquesta mini-rúbrica de **3 indicadors** la desplega, es comparteix amb l'alumnat **des de la SA2** i fa visible la progressió; també serveix per **calibrar l'autoavaluació** (l'alumnat es prepara amb els mateixos 3 indicadors), incloses les mini-defenses formatives de SA3 i SA7.

| Indicador | Insuficient (0–4) | Suficient/Bé (5–6) | Notable (7–8) | Excel·lent (9–10) |
|---|---|---|---|---|
| **Claredat** (què fa el sistema) | No se n'entén el funcionament. | S'entén amb esforç o llegint el codi. | Explicació clara i ordenada (problema → solució). | Clara, concisa i adaptada a qui escolta. |
| **Decisió tècnica justificada** (el *per què*) | Cap decisió justificada («ho he fet així»). | Anomena una decisió però la justifica vagament. | Justifica **una decisió** amb argument tècnic (per què aquests llindars/estats/components). | Justifica decisions i **alternatives descartades**. |
| **Resposta a preguntes** | No respon o respon fora de tema. | Respon parcialment. | Respon amb precisió. | Respon i **reconeix límits** («això fallaria si…»). |

**Progressió esperada al llarg del curs** (mateixos indicadors, exigència creixent):

| Moment | Format | Nivell esperat | Puntua a la R4? |
|---|---|---|---|
| **SA2 S3** (mini-defensa, 1') | Davant el docent | Claredat; la decisió justificada s'hi **inicia** | Sí |
| **SA3 S3** (mini-defensa breu, 1') | Davant el docent | Claredat (formativa: retorn per preparar la SA4) | **No** (formativa) |
| **SA4 S3** (mini-defensa, 1-2') | Davant el docent | Claredat + una decisió justificada | Sí |
| **SA6 S3** (defensa a peu de taula, 2-3', abans de la prova T2 de la S4) | Docent | Els 3 indicadors | Sí |
| **SA7 S4** (mini-defensa breu, 1') | Davant el docent | Claredat + decisió justificada (formativa: retorn per preparar la SA9) | **No** (formativa) |
| **SA9 S4-S5** (defensa final + demo) | Grup classe | Els 3 indicadors al nivell alt | Sí |

> La nota de la defensa **continua entrant per la R4** (fila «Defensa oral») només en els moments marcats «Sí»: aquesta mini-rúbrica és el **desglossament formatiu** d'aquella fila, no una rúbrica nova al còmput. Les mini-defenses de **SA3 S3** i **SA7 S4** són **exclusivament formatives** (retorn oral amb els mateixos 3 indicadors, sense nota): preparen l'alumnat per a les defenses graduades següents (SA4 i SA9 respectivament) sense avançar-ne la nota.

> ⏱️ **Mostreig rotatiu (SA1-SA8).** Cap d'aquestes mini-defenses les fa tota la classe la mateixa sessió: el temps d'aula real (~10' dins la fila «Repte ⭐/Mini-defensa» de la guia docent) només dona per a **5-6 alumnes/sessió**, triats amb un registre rotatiu que garanteix que **tothom hi passa almenys un cop per trimestre** (mecànica completa a [`00_Guia_defensa_oral.md`](../Classes/00_General/00_Guia_defensa_oral.md#mostreig-rotatiu-de-la-mini-defensa-repte--sa1-sa8)). Per als alumnes **no sortejats** en una sessió marcada «Sí», la nota d'aquell criteri de la R4 s'agafa de la **primera sessió posterior del mateix trimestre** en què sí que passin (o, si el trimestre s'acaba abans, del quadern tècnic amb el mateix guió de defensa). La SA9 és l'única excepció: allà defensa **tothom**, sense mostreig.

## R5 · Rúbrica d'actitud i autoregulació

> 🔗 **Traçabilitat:** aquesta rúbrica avalua sobretot **CA5.1** (gestionar individualment un projecte tecnològic complet) i **CA5.2** (elaborar documentació tècnica pròpia i comunicar/defensar la solució), lligats a **CE-R5**. Detall dels criteris a `06_Avaluacio_criteris_qualificacio.md`.

| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| **Implicació** | No participa activament a les sessions. | Participa puntualment. | Participa activament. | Aporta i s'avança a les tasques. |
| **Gestió de l'error** | Es bloqueja/abandona. | Persisteix amb ajuda. | Persisteix i prova alternatives. | Converteix l'error en aprenentatge. |
| **Autonomia** | Depèn del docent. | Treballa amb suport. | Treballa de manera autònoma. | Autònom i autoregulat. |
| **Responsabilitat** | No compleix terminis/material propi. | Compleix amb recordatoris. | Compleix. | Exemplar amb material i terminis. |

---

> **Ús:** cada SA indica quines rúbriques s'apliquen al seu producte. Les rúbriques es comparteixen amb l'alumnat **abans** de començar la SA per orientar l'aprenentatge (avaluació formativa).
>
> **Nota sobre la R5 (actitud i autoregulació):** com que el treball és **individual** durant tot el curs, la R5 es valora **al llarg del trimestre** (acumulant l'observació de diverses sessions i SA), no sessió a sessió.
>
> **Nota sobre l'ús d'assistents d'IA (integritat acadèmica):** **no cal una rúbrica nova**. L'ús d'IA (ChatGPT, Copilot…) s'integra a les existents: **R1 · Depuració** ("depura i **explica la causa**" → l'alumne ha de poder **explicar cada línia** que la IA li hagi suggerit), **R4 · Documentació** (quadern **honest**: ús d'IA **citat** i reflexió **pròpia**) i **R5 · Autoregulació/Responsabilitat** (aplicar **DEPURA abans** d'externalitzar; ús declarat). Principi: *declarar l'ús no baixa nota; amagar-lo o no saber-lo explicar, sí*. Protocol complet a `../Classes/00_General/00_IA_a_la_materia.md` §5.
>
> **Traçabilitat de la IA com a contingut (CA5.1):** la IA com a **tecnologia emergent** (sabers: *"IA aplicada als sistemes de control"*) s'avalua sobretot a la **SA8** amb **R1/R3/R4** (telemetria, classificador i pràctica de ML / Teachable Machine), amb llavors prèvies a SA3/SA6/SA7. Vegeu el mapa a `../Classes/00_General/00_IA_a_la_materia.md`.
