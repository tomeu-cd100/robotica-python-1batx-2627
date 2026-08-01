# SA8 · Guia docent — Autonomia i telemetria

**Durada:** 6 h (3 sessions de 2 h; comprimible a 4 h, vegeu §Mode comprimit) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 3 (IMU MPU6050, DHT11, BMP280, CCS811); rover T3 de la SA7 · **Llenguatge:** MicroPython
**Referència:** [`Programació didàctica/17_SA8_Autonomia_i_telemetria.md`](../../Programació%20didàctica/17_SA8_Autonomia_i_telemetria.md) · **Criteris:** CA1.1, CA3.1, CA4.2 · **Rúbriques:** R1, R3 (criteri "Integració"), R4

> 🧭 **Com s'usa aquesta guia.** **Abans de la SA:** objectius, materials i logística (la llista, al checklist docent). **A cada sessió:** la secció «SESSIÓ n» corresponent, amb el «Guió de modelatge» a mà. **En avaluar:** «Mapa d'avaluació». **Per contextualitzar:** context real i ODS.

## ⚠️ Divergències amb el brief d'aquesta tasca (mana la fitxa 17)

- **Sensors "nucli" vs "ampliació" del Kit 3.** La fitxa 17 demana llegir els 4 sensors avançats (IMU MPU6050, DHT11, BMP280, CCS811) a la S1 i, al producte, "com a mínim dos sensors del Kit 3" enviats per ràdio. Aquesta guia tria **IMU MPU6050 (I2C) + DHT11 (digital)** com a **nucli programat** de `telemetria_radio.py`: són els dos sensors que es poden llegir amb MicroPython pur i sense llibreries externes de manera fiable (I2C de registres i mesura de polsos amb `machine.time_pulse_us`, ja coneguda de l'HC-SR04). **BMP280 i CCS811** exigeixen fórmules de compensació (BMP280) o una seqüència d'arrencada de l'aplicació (CCS811) massa carregoses per al nucli d'aquest curs: queden com a **+ampliació** documentada (pins I2C compartits P19/P20, adreça diferent). És el mateix criteri de gradació nucli/ampliació que la SA6, que va deixar el DHT11 com a **+ampliació** i va resoldre el seu nucli amb el sensor de temperatura **intern** (`temperature()`); aquí, en canvi, el DHT11 sí que passa a formar part del **nucli**, com a primer sensor extern amb driver real que munta l'alumnat.
- **Programa "comportaments".** El brief el proposa com a tercer programa (arquitectura de prioritats); la fitxa 17 no el cita explícitament als seus "Sabers" (que parlen de telemetria i IA), però tampoc el contradiu. S'incorpora a la **Sessió 1** com a bastida conceptual: defineix la FSM (SEGUIR/ESQUIVAR/RECUPERAR) que `telemetria_radio.py` telemetiarà després, sense consumir hores noves (reutilitza sensors i pins ja coneguts de la SA7).

## Objectius de la SA
1. Llegir sensors avançats del Kit 3 (**IMU MPU6050**, DHT11, BMP280, CCS811) i interpretar-ne les magnituds.
2. Enviar dades de sensors per **ràdio** des del rover al **propi programa d'estació base** (telemetria), executat temporalment a la placa d'un company o del docent.
3. Registrar i visualitzar dades rebudes (llista de lectures, mitjana simple) i amb el mòdul `log` natiu.
4. Introduir-se a la **IA aplicada al control**: classificació senzilla de patrons de dades (p. ex. amb Teachable Machine) com a tecnologia emergent.

## Materials per a la sessió
- 1 micro:bit V2 + 1 Micro:shield per alumne/a + cable micro-USB (dotació individual, vegeu [`09c_Inventari_kits_disponibles.md`](../../Programació%20didàctica/09c_Inventari_kits_disponibles.md)).
- El **rover T3** de la SA7, portat per l'alumnat; portapiles carregades.
- **DHT11** i **IMU MPU6050** del Kit 3 (temporalment cablejats al rover per aquesta SA); cablejat de la resta del Kit 3 (BMP280, CCS811) disponible per a qui vulgui l'ampliació.
- Una **segona micro:bit** per parella (la d'un company, per torns, o la del docent) per fer d'estació base de proves puntuals.
- Ordinadors amb accés a **python.microbit.org** (protocol de ràdio i lògica sense maquinari) i a **Teachable Machine** (Sessió 3, navegador). Projector. Quadern tècnic (digital).

## Documents de la SA (aquesta carpeta)
| Document | Quan s'usa |
|---|---|
| [`SA8_fitxa_alumnat.md`](SA8_fitxa_alumnat.md) | Totes les sessions (Activitats 1-3 + producte + quadern). |
| [`SA8_esquemes_connexions.md`](SA8_esquemes_connexions.md) | Sessions 1-3 (pins heretats + DHT11 + IMU MPU6050 + ràdio). |
| `codi/` | `comportaments`, `telemetria_radio` i `estacio_base` (producte). |
| [`Reptes_SA8.md`](../../Reptes/Reptes_SA8.md) | Sessió 3 (fase «Repte», mateix temps de pràctica): repte **⭐** ara **nucli obligatori**; reptes ⭐⭐/⭐⭐⭐ continuen sent ampliació opcional. |

> Cada programa de `codi/` té la seva **pàgina de pràctica** (l'`EXPLICACIO.md` de la seva carpeta). El «Guió de modelatge» oral de sota continua sent teu.

---

## Mode comprimit (4 h): com aplicar la 2a retallada del pla de contingència

> Vegeu `Programació didàctica/08_Sequenciacio_temporal_anual.md` §«Pla de contingència temporal». Si en acabar el 1r trimestre no s'ha tancat la SA3, activa aquesta retallada ja al gener del 3r trimestre (no esperis al maig).

Si el calendari real obliga a comprimir la SA8 de 6 h a 4 h, **fusiona la S1 i la S2** en una única sessió de 2 h: el bloc "sensors avançats + disseny del missatge" (S1) i el bloc "enviar i registrar per ràdio" (S2) s'ajunten, deixant `comportaments.py` com a **repàs ràpid oral** (5') en lloc d'una pràctica completa, i passant directament a muntar `telemetria_radio.py` amb els llindars ja donats (bastida). **La S3 d'IA i producte es manté sencera**: és el nucli del saber "IA aplicada al control" i no es retalla mai. Les **2 h alliberades** amb aquesta compressió financen la **Sessió 0 del rover** (muntatge, prèvia a la SA7).

---

## SESSIÓ 1 (2 h) — Sensors avançats: llegir el Kit 3

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Repte inicial: *"Com sap algú, des d'una altra taula, què està 'sentint' el rover en aquest moment?"* 🥋 **Kata del dia:** K15 (log) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Formulen hipòtesis: què caldria per "explicar" el rover a distància? |
| Explicació | 30' | Presenta els 4 sensors avançats del Kit 3 (IMU MPU6050, DHT11, BMP280, CCS811) i les seves magnituds; explica per què el **nucli** d'aquesta SA programa només IMU+DHT11 (I2C de registres i time-of-flight, ja coneguts) i deixa BMP280/CCS811 com a ampliació. Modelatge de [`comportaments.py`](codi/comportaments/EXPLICACIO.md): repàs de la FSM SEGUIR/ESQUIVAR/RECUPERAR (generalització de la SA7), estructurada explícitament en **`percep()`/`decideix()`/`actua()`**. Verbalitza: **aquest patró és exactament el que farà servir cada repte individual a la SA9** (`plantilla_projecte.py`): avui el veieu funcionar abans d'haver-lo d'escriure de zero. | Prenen notes; relacionen l'IMU amb l'acceleròmetre intern (SA1-SA3) i el DHT11 amb el termòstat (SA6); identifiquen quina funció fa cadascuna de les tres. |
| Pràctica | 60' | Acompanya el muntatge del DHT11 (P8) i l'IMU (I2C, P19/P20) sobre el rover, i la prova de `comportaments.py` sobre el circuit/obstacles ja coneguts. Introdueix el disseny del **format de missatge** de telemetria (quins camps, amb quin prefix). | Munten els dos sensors nous; proven `comportaments.py`; dissenyen el seu format de missatge (Activitat 1 de la fitxa). |
| Tancament | 20' | Recull dubtes; anticipa que la S2 hi afegeix la ràdio. | Entrada del quadern: format de missatge triat + esquema dels 3 estats de la FSM. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: deixa `comportaments.py` com a demostració oral breu (sense que tothom l'executi) i centra el temps en el muntatge dels sensors nous.

**Punts clau:** l'IMU MPU6050 es llegeix per **I2C** (un bus compartit, adreces diferents per sensor), diferent de tots els components anteriors del curs (cadascun al seu pin dedicat). El DHT11 reutilitza el mateix mecanisme de **mesura de temps de vol** (`machine.time_pulse_us`) que ja coneixeu de l'HC-SR04, només que amb 40 polsos consecutius en lloc d'un de sol. `percep()` (llegeix), `decideix()` (canvia d'estat) i `actua()` (mou) són el **mateix esquema** que tancarà el curs a la SA9: separar-los en tres funcions fa que sigui fàcil trobar on toca afegir un sensor nou (a `percep()`) sense tocar la lògica de moviment.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| L'IMU no respon (el programa sembla "penjar-se") | SCL/SDA intercanviats, o GND no comú entre el sensor i el Micro:shield | Revisar [`SA8_esquemes_connexions.md`](SA8_esquemes_connexions.md): SCL a **P19**, SDA a **P20** |
| El DHT11 retorna sempre `None` | Cablejat a un pin diferent de **P8**, o llegit massa sovint (cal esperar 1-2 s entre lectures) | Revisar el pin i espaiar les lectures |
| L'alumnat confon "estat de la FSM" amb "valor d'un sensor" | Encara no distingeix una variable d'estat (decisió pròpia) d'una lectura (dada externa) | Repassar `maquina_estats_semafor.py` (SA6): l'estat el decideix el programa, la lectura la dona el sensor |

---

## SESSIÓ 2 (2 h) — Telemetria per ràdio: enviar i registrar

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Explicació | 25' | Modelatge de [`telemetria_radio.py`](codi/telemetria_radio/EXPLICACIO.md): reutilitza la FSM de `comportaments.py`, hi afegeix els sensors del Kit 3 i envia missatges `"TEL:..."` per ràdio cada `INTERVAL_TELEMETRIA_MS`. Recorda per què el prefix és diferent del `"CMD:"` de la SA5/SA6. Modelatge d'[`estacio_base.py`](codi/estacio_base/EXPLICACIO.md): cada alumne l'escriu, encara que s'executi temporalment en una altra placa. | Prenen notes; identifiquen per què enviar telemetria a cada volta del bucle (~20 ms) saturaria la ràdio. |
| Pràctica | 55' | Acompanya el muntatge de `telemetria_radio.py` sobre el rover i `estacio_base.py` en una segona placa (per torns, en parelles de números de llista, o la del docent). | Programen i proven `telemetria_radio.py` i el seu propi `estacio_base.py` (Activitat 2 de la fitxa). |
| Mini-check | 10' | **Mini-check individual** (10', sense apunts; banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md)): enviar un valor de sensor per ràdio amb un protocol propi. | Fan el mini-check (no qualifica). |
| Tancament | 20' | Recull dubtes; anticipa la IA de la S3. | Documenten al quadern el format de missatge final i una captura de les dades rebudes/registrades. |

> ⏱️ **Marge:** el temps efectiu real és ~100' (arrencada + recollida), no 120'. Si vas just, retalla primer: deixa el registre amb `log` com a demostració (sense que tothom el connecti per USB a l'aula) i centra el temps en el protocol de ràdio.

**Punts clau:** aquesta és la primera SA on **dues plaques diferents** (rover i estació) col·laboren en un mateix producte, però el codi que s'avalua és **sempre individual**: cadascú porta el seu `telemetria_radio.py` i el seu `estacio_base.py`, encara que en algun moment s'executin sobre maquinari compartit.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| L'estació base no rep res | `group` diferent entre les dues plaques, o `radio.on()` no cridat a alguna de les dues | Revisar `SA8_esquemes_connexions.md` §3 (comprovació ràpida) |
| L'estació base mostra sempre `Image.CONFUSED` | El camp `"E"` del missatge no coincideix literalment amb `SEGUIR`/`ESQUIVAR`/`RECUPERAR` | Revisar que el `PREFIX` i els noms de camp siguin **idèntics** a totes dues bandes |
| `log.add()` peta amb un error | `log.set_labels()` no s'ha cridat abans, o amb noms de columna diferents dels que fa servir `log.add()` | Revisar l'ordre: `set_labels()` un únic cop, abans del bucle |

---

## SESSIÓ 3 (2 h) — IA aplicada al control i producte: sistema de telemetria

> 🎯 **Producte de la SA8.** Es tanca i s'avalua amb **R1** (codi, funcionament), **R3** (criteri "Integració") i **R4** (documentació).
>
> ⭐ **Repte nucli obligatori.** Un cop tancat el producte, tothom ha de fer el **repte ⭐ · Estació meteorològica escolar amb alertes** de [`Reptes_SA8.md`](../../Reptes/Reptes_SA8.md) (fila pròpia a la taula, més avall). Els reptes ⭐⭐/⭐⭐⭐ continuen sent ampliació opcional per a qui vagi sobrat.

| Fase | Temps | Activitat docent | Activitat alumnat |
|---|---|---|---|
| Activació | 10' | Recorda `mpu_orientacio()` de `telemetria_radio.py`: un llindar fet a mà sobre la magnitud d'acceleració. Pregunta: *"i si, en lloc d'escriure jo el llindar, li ensenyés exemples perquè ell mateix el trobés?"* 🥋 **Kata del dia:** K16 (funcions/paràmetres) — vegeu el [Banc d'activació](../00_General/00_Banc_activacio_repas.md). | Formulen hipòtesis sobre què canviaria. |
| Explicació/demo | 20' | **Introducció a la IA aplicada al control**, en versió comprimida: regles fetes a mà vs aprenentatge automàtic (dades → model → decisió); demostració guiada amb **Teachable Machine** (o l'extensió ML de MakeCode) sobre dades d'acceleròmetre/so, a nivell de demostració del docent; bloc «Ètica de dades i IA» (RGPD, biaix, consentiment) aplicat a la telemetria del propi rover. | Segueixen la demo; identifiquen el **biaix** si es demostra amb poques dades. |
| Repte | 35' | Acompanya el tancament del **producte: sistema de telemetria del rover** (mínim dos sensors, ràdio, registre amb el propi `estacio_base.py`), amb una reflexió breu sobre l'ús de la IA com a tecnologia emergent. | Tanquen i documenten el producte; escriuen la reflexió d'IA al quadern. |
| **Repte ⭐ (nucli obligatori)** | 25' | Un cop tancat el producte, repte **⭐ · Estació meteorològica escolar amb alertes** de [`Reptes_SA8.md`](../../Reptes/Reptes_SA8.md). | Fan el repte ⭐; 🤝 **parella de lectura (5', dins d'aquests 25')** abans de lliurar-lo; l'ensenyen al docent perquè el validi (**R1**). Qui vagi sobrat continua amb els reptes ⭐⭐/⭐⭐⭐ (ampliació opcional). |
| Mini-defensa (MOSTREIG) + tancament | 10' | Recull dubtes; **mini-defensa breu, per MOSTREIG rotatiu** (2-3', R4·DO): tria **5-6 alumnes** (registre rotatiu, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md#mostreig-rotatiu-de-la-mini-defensa-repte--sa1-sa8)) perquè justifiquin una decisió de disseny; la resta tanca directament. | Els sortejats fan la mini-defensa; la resta anota al quadern la reflexió sobre ètica de dades i IA. |
| **Marge/imprevistos** | 20' | Coixí per a arrencada i recollida: el temps efectiu real d'aula és ~100' (no 120'); aquesta fila ho fa explícit. | — |

> ⏱️ **Marge:** la fila «Marge/imprevistos» (20') ja recull que el temps efectiu real és ~100'. Si encara vas just, retalla primer: la pràctica de Teachable Machine (deixa-la com a **demostració del docent** en lloc que tothom entreni el seu propi classificador; la reflexió escrita es manté igual).

> 🔌 **Pla B sense internet a l'aula.** La IA com a **objecte d'estudi** (regles vs aprenentatge, biaix, ètica de dades) es pot treballar **sense connexió**, amb regles ja programades a la micro:bit (`mpu_orientacio()`) i un debat oral. La pràctica de classificació amb Teachable Machine necessita navegador: fer-la a casa, a l'aula d'informàtica, o com a **demostració del docent** (vídeo/captures) si no hi ha ordinadors disponibles a l'aula de robòtica.

**Punts clau (Ètica de dades i IA):** recollir dades — també la **telemetria del propi rover** — implica **privadesa, consentiment i finalitat** (marc del document [`00_IA_a_la_materia.md`](../00_General/00_IA_a_la_materia.md)). Un model d'IA és el resultat d'**entrenar** amb dades: la qualitat de la decisió depèn de les dades (*garbage in, garbage out*), i si les dades d'entrenament són parcials, les decisions ho seran (**biaix**). La IA **no "entén"**: troba patrons estadístics i pot equivocar-se amb seguretat.

**Errors freqüents i solució:**
| Error | Causa | Solució |
|---|---|---|
| L'alumnat pensa que Teachable Machine "entén" els gestos | Confon reconeixement de patrons estadístics amb comprensió | Recordar el marc: dades → model → decisió, sense "enteniment" |
| La reflexió d'IA es queda en "la IA és el futur" sense concretar | Falta connectar-la amb el propi `mpu_orientacio()` (regla feta a mà) | Preguntar: "què hauries de fer diferent si volguessis que el llindar l'aprengués el sistema en lloc de triar-lo tu?" |
| El producte no arriba a enviar telemetria real (només codi sense provar) | Manca de temps o de maquinari a punt | Acceptar el "nucli" (dos sensors, ràdio, registre) com a assoliment satisfactori; deixar l'ampliació (BMP280/CCS811, més sensors) per a qui vagi sobrat |

**Producte de la SA:** sistema de telemetria del rover (com a mínim dos sensors del Kit 3, enviament per ràdio, registre/visualització amb el propi `estacio_base.py`), amb documentació al quadern tècnic i reflexió breu sobre la IA aplicada al control.

### Mapa d'avaluació (traçabilitat)

| Instrument | Què evidencia | Criteri | Rúbrica | Qualifica? |
|---|---|---|---|---|
| Mini-check (S2) | Enviar un valor de sensor per ràdio amb protocol propi | CA1.1 | — | **No** (radar formatiu) |
| Fitxa d'alumnat (Act. 1-3) | Sensors avançats, protocol de telemetria, IA aplicada al control | CA1.1, CA3.1, CA4.2 | R1 | Formativa |
| Producte «sistema de telemetria del rover» (S3) | Mínim dos sensors del Kit 3, ràdio, registre amb `estacio_base.py` propi | CA1.1, CA3.1, CA4.2 | **R1**, **R3** (Integració) | Sí |
| Repte **⭐** (`Reptes_SA8.md`, S3, nucli obligatori) | Llindar de temperatura amb alerta afegit al protocol de telemetria | CA1.1 | **R1** | Sí |
| Mini-defensa (S3, R4·DO) | Claredat + justificació d'una decisió de disseny | CA3.1 | **R4** (fila «Defensa oral») | Sí |
| Quadern tècnic | Format de missatge, llindars de sensors, reflexió d'IA i ètica de dades | CA4.2 | **R4** | Sí |
| Observació d'aula | Autonomia i responsabilitat en manipular sensors i dades | — | **R5** | Sí |

*(CA1.1 = escriure i depurar programes MicroPython amb estructures de control, funcions i biblioteques, comentant el codi; CA3.1 = implementar sistemes de control i explicar-ne el funcionament; CA4.2 = dissenyar i provar sistemes senzills de monitoratge/telemetria, valorant l'ús de la IA com a tecnologia emergent. Vegeu [`Programació didàctica/06_Avaluacio_criteris_qualificacio.md`](../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md).)*

### Quadern tècnic — entrada de la SA8 (guia per a l'alumnat)

Segueix el mètode de projecte:
- **Què he après** (sensors avançats, protocol de telemetria, registre de dades, IA aplicada al control).
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com).
- **Un error que he tingut i com l'he resolt.**
- **El meu format de missatge** de telemetria i per què l'he triat així.
- **Reflexió d'IA i ètica de dades:** una decisió que hauria de prendre abans de recollir dades de qualsevol persona o robot (privadesa, consentiment, finalitat).

> Comparteix les rúbriques **R1**, **R3** i **R4** amb l'alumnat **abans** de començar el repte (avaluació formativa).

### Pont cap a l'avaluació trimestral

A la SA8, el rover autònom de la SA7 aprèn a **explicar-se**: envia el que "sent" a una altra placa, mentre segueix decidint sol amb la mateixa arquitectura de prioritats. A la SA9, tot es tanca en el **repte final integrador**, amb la **S5** com a prova pràctica T3 (per estacions rotatives).

---

## Guió de modelatge (què verbalitzar)

- **S1 · Per què I2C i no un pin dedicat:** pregunta *"si haguéssim de connectar l'IMU, el BMP280 i el CCS811 cadascun al seu propi pin, ens quedarien prou pins lliures?"* — porta la resposta cap a la idea de bus compartit amb adreces diferents.
- **S1 · Regles vs estat:** pregunta *"quina diferència hi ha entre `estat` (a `comportaments.py`) i `distancia` (el que llegeix l'HC-SR04)?"* — porta la resposta cap a decisió pròpia vs dada externa.
- **S2 · Per què un prefix diferent:** pregunta *"si `telemetria_radio.py` i `comandament.py` (SA5) fessin servir el mateix prefix `CMD:`, què podria passar si tots dos corrien alhora amb el mateix `group`?"* — porta la resposta cap a la confusió entre una ordre i una dada.
- **S3 · Regles vs IA:** pregunta *"`mpu_orientacio()` decideix amb un llindar que he escrit jo. Si en lloc d'un llindar entrenéssim un model amb exemples, què canviaria, i què es mantindria igual?"* — porta la resposta cap a que la **decisió final** (INCLINAT/PLA) es manté, però **qui la tria** (jo vs el model, a partir de dades) canvia.

## Atenció a la diversitat

| Necessitat | Mesura |
|---|---|
| **Bastida (qui ho necessita)** | Format de missatge de telemetria model ja donat (p. ex. `"TEL:T:23.5"`); esquelet de la funció `envia_lectura()`/`analitza()` ja escrit (vegeu SA8_fitxa_alumnat.md). |
| **+ Ampliació (qui va sobrat)** | Enviar més d'un sensor combinat (BMP280/CCS811, protocol propi més ric); comparar dades classificades manualment vs amb Teachable Machine; vegeu els reptes **⭐⭐/⭐⭐⭐** de [Reptes_SA8.md](../../Reptes/Reptes_SA8.md) (el ⭐ ja és nucli obligatori, no ampliació). |
| **Diversitat lingüística/lectora** | Diagrama del protocol de telemetria amb icones (emissor → ràdio → receptor) en lloc de només text; glossari a [`00_Glossari_tecnic.md`](../00_General/00_Glossari_tecnic.md). |
| **Sense rover/Kit 3 a punt** | Es treballa la lògica del protocol al **simulador** (ràdio i `log` sí es simulen), amb valors de sensor simulats en variables en lloc de lectures reals; vegeu §Simulació de [`SA8_esquemes_connexions.md`](SA8_esquemes_connexions.md). |

> **Avaluació formativa:** comparteix les rúbriques **R1**, **R3** i **R4** amb l'alumnat **abans** de començar el repte.

## Pensament computacional i depuració

- **Concepte de PC d'aquesta SA:** **abstracció de protocol**: dissenyar un format de missatge (`"TEL:D:23;S:412;..."`) que amagui la complexitat de com es llegeix cada sensor darrere d'un format senzill i comú és el mateix principi que fan servir els protocols de xarxa reals (HTTP, MQTT), només molt més simples.
- **Depuració:** continua la rutina **DEPURA** (SA1-SA7), amb un èmfasi nou: quan un missatge de ràdio "no arriba com toca", comprova primer si el problema és de **protocol** (mateix `group`? mateix `PREFIX`? mateix format de camps?) abans de sospitar dels sensors o de la lògica de decisió.

## Context real i ODS

- **Context:** estacions meteorològiques connectades, sensors de qualitat de l'aire urbans, flotes de robots de magatzem que reporten el seu estat a un panell central: tots combinen sensors, un protocol de dades i un punt de recepció, exactament com avui.
- **ODS 9** (indústria, innovació i infraestructura) i **ODS 11** (ciutats i comunitats sostenibles): la telemetria és la base del monitoratge ambiental i industrial modern; l'ètica de dades (privadesa, consentiment) és imprescindible quan aquesta telemetria implica persones.
