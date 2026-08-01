# Pla d'implementació — Material del curs «Robòtica amb Python» (1r Batx)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** crear tot el material docent del curs «Robòtica amb Python» (optativa pròpia de centre, 1r Batx, 2 h/set, 70 h, tot individual, micro:bit) replicant l'estructura i les eines del curs germà `..\Curs 2627 1 Batx Robotica`.

**Architecture:** markdown com a font única; `web/_generador/generar.py` construeix la web de doble vista (alumnat/docent); `tools/qa.py` garanteix cobertura per SA, enllaços i sintaxi del codi; publicació a GitHub Pages. El contingut es crea per capes: infraestructura → normativa → programació didàctica → material d'aula SA a SA → avaluació → web.

**Tech Stack:** Python 3 (generador + QA), MicroPython (codi d'alumnat micro:bit V2), git, GitHub Pages.

## Global Constraints (de l'espec — vigents a TOTS els tasks)

- **Tot en català**; comentaris del codi d'alumnat (`.py`) en català **sense accents**.
- **Tot el treball de l'alumnat és individual** — cap activitat, construcció ni projecte en parelles o grups.
- **Maquinari nucli: micro:bit V2 + Micro:shield + sensors/actuadors Keyestudio** (1 per alumne). Pico i pyFirmata només com a opcions documentades (no al nucli de cap SA).
- **Res d'interfícies d'usuari ni núvol**: telemetria = ràdio micro:bit→micro:bit; registre = data logging natiu V2.
- **Ancoratge curricular:** CE5 de Tecnologia i Enginyeria I + criteris 5.1/5.2 + sabers del bloc Automatització (Decret 171/2022; el 103/2026 no els modifica).
- **Seqüenciació:** 9 SA = 6+8+8 / 8+6+8 / 8+6+10 = 68 h + ~2 h marge; proves pràctiques T1/T2/T3 = darrera sessió de SA3/SA6/SA9.
- **Fil conductor de construccions individuals:** T1 mascota expressiva (tanca SA3) · T2 vehicle teledirigit (tanca SA6) · T3 rover autònom (evolució del vehicle, SA7-SA9).
- **Nomenclatura del curs germà:** `SA{n}_{tipus}.md` amb sufixos `_guia_docent`, `_fitxa_alumnat`, `_fitxa_ampliada`, `_checklist_docent`, `_checklist_alumnat`, `_esquemes_connexions`; transversals `00_Nom.md`; codi a `Classes/SAn/codi/<nom>/` amb `<nom>.py` + `EXPLICACIO.md`.
- Sense frontmatter YAML: H1 + línia `**Durada:** … · **Maquinari:** …`.
- **Abans de cada commit:** `python tools/qa.py` ha de passar (o el task explica per què encara no pot passar sencer i què se'n verifica).
- Llicència CC BY-SA 4.0, com el curs germà.
- El curs germà és **només lectura**: se'n copia i adapta, mai s'hi escriu.

**Rutes:** `NOU = C:\Users\briera2\Documents\Curs 2627 1 Batx Robotica amb python` · `GERMA = C:\Users\briera2\Documents\Curs 2627 1 Batx Robotica`.

---

### Task 1: Infraestructura base (generador, QA, CLAUDE.md, esquelet)

**Files:**
- Create: `CLAUDE.md`, `README.md`, `LICENSE`, `.gitignore`, `GUIA_INICI_DOCENT.md` (esborrany breu)
- Create: `web/_generador/` (còpia adaptada de `GERMA\web\_generador\`), `tools/qa.py` (còpia adaptada de `GERMA\tools\qa.py`)
- Create: carpetes buides amb `README.md`: `Classes/00_General`, `Classes/SA0`…`SA9`, `Classes/Solucionari`, `Reptes/Solucionari`, `Avaluació`, `Recursos`, `Simulacions`, `Programació didàctica`, `Memòria treball`
- Create: `.github/workflows/` (còpia adaptada del workflow del germà)

**Interfaces:**
- Produces: `python tools/qa.py` executable (mode `--nomes-sintaxi` ha de passar amb el repositori quasi buit); `python web/_generador/generar.py` executable; contracte de cobertura per SA que TOTS els tasks de Classes han de complir.

- [ ] **Step 1:** copiar `GERMA\tools\qa.py`, `GERMA\web\_generador\` (sense `__pycache__` ni `.pytest_cache`), `GERMA\.gitignore`, `GERMA\LICENSE`, `GERMA\.github\workflows\` cap a `NOU`.
- [ ] **Step 2:** llegir `tools/qa.py` copiat i adaptar-lo: (a) eliminar toda referència a compilació `.ino` / `arduino:avr:uno`; (b) la comprovació de sintaxi passa a cobrir tots els `.py` d'alumnat amb `ast.parse` (els `import microbit`/`import radio` no s'executen, només es parsegen — cap stub necessari); (c) el quadre d'hores es llegirà de `Programació didàctica/08_Sequenciacio_temporal_anual.md` amb els valors nous (6+8+8/8+6+8/8+6+10); (d) afegir flag `--nomes-sintaxi` que salta cobertura de SA (per poder committar infraestructura abans que existeixi contingut).
- [ ] **Step 3:** adaptar `web/_generador/generar.py` i config: títol del curs «Robòtica amb Python — 1r Batxillerat», rutes idèntiques (mateixos noms de carpetes que el germà, no cal tocar l'estructura), eliminar seccions específiques d'Arduino si n'hi ha de codificades en dur (cercar «Arduino», «.ino», «Wokwi» al codi del generador i decidir cas a cas: `.ino` fora, Wokwi es manté com a tipus d'enllaç).
- [ ] **Step 4:** escriure `CLAUDE.md` nou: còpia del del germà amb aquests canvis — nom del curs, «tot individual, cap activitat en parelles», maquinari micro:bit, codi d'alumnat només `.py`, QA sense `.ino`.
- [ ] **Step 5:** escriure `README.md` (presentació del curs, estructura de carpetes, com generar web i passar QA) i `GUIA_INICI_DOCENT.md` mínima (què llegir primer; s'ampliarà al final).
- [ ] **Step 6:** verificar: `python tools/qa.py --nomes-sintaxi` → OK; `python web/_generador/generar.py` → genera `web/` sense errors (contingut quasi buit és acceptable).
- [ ] **Step 7:** commit `feat: infraestructura base (generador web, qa, esquelet de carpetes)`.

---

### Task 2: Normativa — síntesi pròpia

**Files:**
- Create: `Normativa/01_Normativa_LOMLOE_RoboticaPython_1Batx.md`, `Normativa/README.md`
- (PDF oficials ja committats)

**Interfaces:**
- Produces: document de síntesi que `Programació didàctica/01` i `02` citaran com a font.

- [ ] **Step 1:** escriure `01_Normativa_LOMLOE_RoboticaPython_1Batx.md` a partir del model `GERMA\Normativa\01_Normativa_LOMLOE_Robotica_1Batx_Catalunya.md`, actualitzat amb: Decret 103/2026 **definitiu** (DOGC 9704, 9/7/2026) — ja no «pendent d'aprovació»; via triada = **optativa pròpia de centre** (nom «Robòtica amb Python», diferent de les oficials «Robòtica» i «Programació»); vinculació CE5 TiE I + criteris 5.1/5.2 + sabers Automatització; currículums oficials de «Programació» (3 CE, 4 blocs) i «Robòtica» (3 CE, 3 blocs) resumits com a **referents no vinculants**; taula horària 2026-27 (optatives 6 h en 2-3 franges, mín. 2 h màx. 4 h per matèria); checklist de centre (PEC/PGA, franja, mínim 10 alumnes).
- [ ] **Step 2:** `Normativa/README.md`: índex dels 5 PDF + síntesi, amb URL oficials d'origen (les verificades: XTEC Programació/Robòtica PDF, fitxa DOGC del Decret 103/2026, annex 3, infografia).
- [ ] **Step 3:** `python tools/qa.py --nomes-sintaxi` → OK. Commit `docs(normativa): sintesi LOMLOE per a l'optativa propia Robotica amb Python`.

---

### Task 3: Programació didàctica — documents transversals (00-09c)

**Files:**
- Create a `Programació didàctica/`: `00_Index_general.md`, `01_Introduccio_context_justificacio.md`, `02_Objectius_competencies.md`, `03_Sabers_i_continguts.md`, `04_Metodologia.md`, `05_Atencio_a_la_diversitat.md`, `06_Avaluacio_criteris_qualificacio.md`, `06b_Avaluacio_programacio_i_practica_docent.md`, `07_Rubriques.md`, `08_Sequenciacio_temporal_anual.md`, `09_Materials_recursos_per_unitat.md`, `09b_Guia_compra_pressupost.md`, `09c_Inventari_kits_disponibles.md`, `README.md`

**Interfaces:**
- Consumes: síntesi normativa (Task 2).
- Produces: quadre d'hores oficial a `08_…` que `tools/qa.py` valida; criteris d'avaluació i rúbriques R1-R5 que les guies docents de SA citaran; noms de les 9 SA canònics.

- [ ] **Step 1:** per a cada document, llegir l'homòleg del germà i reescriure'l per a aquest curs (no copiar literal: canvien llenguatge, maquinari, individualitat i fil conductor). Continguts clau per document:
  - `02`: objectius ancorats a CE5/5.1/5.2; competències clau LOMLOE; perfil de sortida.
  - `03`: sabers d'Automatització mapats SA a SA; progressió Python explícita (seqüències→variables/bucles→condicionals→funcions→estructures de dades/esdeveniments→integració; objectes només d'ús).
  - `04`: metodologia — treball **individual**, PRIMM com al germà si s'hi usa, demos docents, simulador com a pla B, dinàmica d'ajuda entre iguals sense productes compartits.
  - `06`: model d'avaluació del germà adaptat: projectes/productes + proves pràctiques 20 % + mini-checks + quadern tècnic; qualificació 1-10 sense decimals; criteris derivats de 5.1/5.2 escrits explícitament (mínim 6 criteris propis numerats).
  - `07`: rúbriques R1-R5 (producte, codi, documentació tècnica, defensa oral, quadern) amb 4 nivells cadascuna, text complet.
  - `08`: quadre d'hores EXACTE de l'espec (6+8+8/8+6+8/8+6+10 = 68 + ~2 marge), taula de fabricació del fil conductor amb consum de contingència (marge efectiu ≈ 0, mitigació peces pretallades), pla de contingència (mai SA1-SA3 ni SA9; SA2/SA4 producte comprimible; SA8 6→4 h; SA7 8→6 h últim recurs).
  - `09`: mapa material→SA (micro:bit + shield + sensors Keyestudio per SA).
  - `09b`: full de compra: consumibles fil conductor individual (~250-350 €/curs: DM 3 mm, PLA, cargols, portapiles), i **opcions no bloquejants** (Pico ~5-8 €/u, quantitats si mai s'activa).
  - `09c`: inventari real: micro:bit V2 + Micro:shield ×alumne, kits Keyestudio 1-3 ×alumne (contingut resumit del `GERMA\…\09c`), xTool S1, Bambu P2S; taula SA→material amb estat ✅.
- [ ] **Step 2:** `python tools/qa.py` (ja sense `--nomes-sintaxi` si el quadre d'hores es valida; si la cobertura de SA encara falla per falta de Classes, usar el flag i deixar-ho anotat). Commit `docs(programacio): documents transversals 00-09c`.

---

### Task 4: Programació didàctica — un document per SA (10-18)

**Files:**
- Create: `Programació didàctica/10_SA1_Hola_robot.md`, `11_SA2_Sortides_el_robot_actua.md`, `12_SA3_Entrades_el_robot_percep.md`, `13_SA4_Funcions_i_moviment.md`, `14_SA5_Radio_robots_que_parlen.md`, `15_SA6_Control_el_robot_decideix.md`, `16_SA7_Robotica_mobil_el_rover.md`, `17_SA8_Autonomia_i_telemetria.md`, `18_SA9_Repte_final_integrador.md`

**Interfaces:**
- Consumes: criteris i rúbriques (Task 3).
- Produces: per a cada SA: objectius, sabers, seqüència de sessions (títol + activitats per sessió de 2 h), producte avaluable, criteris aplicats — les guies docents de Classes (Tasks 6-14) han de ser 1:1 amb aquests documents.

- [ ] **Step 1:** escriure els 9 documents seguint el patró del germà (`GERMA\…\10_SA1_Introduccio_robotica.md` com a plantilla d'estructura). Sessions per SA: SA1=3, SA2=4, SA3=4 (S4=prova T1), SA4=4, SA5=3, SA6=4 (S4=prova T2), SA7=4, SA8=3, SA9=5 (S5=prova T3). Cada sessió: objectiu, activitats concretes amb el maquinari disponible, mini-check si en toca, deures/simulador. Els productes: SA3→mascota muntada i programada; SA6→vehicle teledirigit amb aturada d'emergència; SA9→rover autònom amb repte lliure + dossier + defensa individual.
- [ ] **Step 2:** revisar coherència 08↔10-18 (hores i sessions quadren). `python tools/qa.py` (mateix criteri que Task 3). Commit `docs(programacio): fitxes SA1-SA9`.

---

### Task 5: Classes/00_General — material transversal

**Files:**
- Create a `Classes/00_General/`: `00_LLEGEIX-ME_Classes.md`, `00_Entorns_de_treball.md` (editor python.microbit.org + simulador + Thonny + transferència .hex/.py), `00_Fil_conductor_construccions.md` (mascota/vehicle/rover, calendari de fabricació, nesting, pretallat), `00_Projecte_T1_Mascota.md`, `00_Projecte_T2_Vehicle.md`, `00_Projecte_T3_Rover.md`, `00_Glossari_tecnic.md`, `00_Mini_checks_individuals.md`, `00_Guia_defensa_oral.md`, `00_Quadern_tecnic.md`, `00_Avaluacio_per_alumnat.md`, `00_Mode_supervivencia.md` (què fer si falla maquinari: simulador), `00_IA_a_la_materia.md` (adaptat del germà)
- Create: `Classes/README.md`

**Interfaces:**
- Consumes: fil conductor de l'espec; rúbriques (Task 3).
- Produces: documents `00_Projecte_T*.md` que les SA de tancament enllacen; capçalera `> **Per a qui és?**` a cada transversal (convenció del generador).

- [ ] **Step 1:** escriure els documents; els tres `00_Projecte_T*` amb: objectiu, llista de peces (làser/3D/kit), esquema de muntatge en text + taula, programari mínim i ampliacions, rúbrica aplicable, calendari de fabricació individual (cua de làser/impressora per a 15-20 unitats: batches i sessions).
- [ ] **Step 2:** `python tools/qa.py` + `python web/_generador/generar.py` (la web ja mostra transversals). Commit `feat(classes): material transversal 00_General`.

---

### Task 6: SA0 — Punt de partida (vocabulari i primeres passes)

**Files:**
- Create a `Classes/SA0/`: `README.md`, `SA0_vocabulari_robotica.md`, `SA0_primers_passos_editor.md` (crear compte no cal: editor web sense registre; desar .hex/.py; connectar placa)

**Interfaces:**
- Produces: material d'acollida previ a SA1 (sense hores pròpies: es fa dins la S1 de SA1, com al germà).

- [ ] **Step 1:** escriure els documents (vocabulari: robot, sensor, actuador, microcontrolador, programa, bucle…; amb exemples micro:bit).
- [ ] **Step 2:** `python tools/qa.py` → la cobertura de SA0 és reduïda (el contracte del germà per SA0 és laxa; ajustar `comprova_cobertura_sa()` si cal perquè SA0 només exigeixi README). Commit `feat(classes): SA0 punt de partida`.

---

### Tasks 7-15: Classes/SA1 … SA9 + Reptes + Solucionari (un task per SA)

Aquests nou tasks segueixen TOTS el mateix contracte. Es llisten les particularitats de cada SA després del contracte comú.

**Contracte comú (cada SAn):**

**Files:**
- Create a `Classes/SAn/`: `README.md`, `SAn_guia_docent.md`, `SAn_fitxa_alumnat.md`, `SAn_fitxa_ampliada.md`, `SAn_checklist_docent.md`, `SAn_checklist_alumnat.md`, `SAn_esquemes_connexions.md` (SA1-SA8), `codi/<programa>/<programa>.py` + `codi/<programa>/EXPLICACIO.md` per a cada programa
- Create: `Reptes/Reptes_SAn.md` + `Reptes/Solucionari/Reptes_SAn_solucions.md`

**Interfaces:**
- Consumes: doc `1x_SAn_….md` de Programació didàctica (Task 4) — la guia docent n'és el desplegament 1:1; rúbriques (Task 3).
- Produces: SA completa que passa `tools/qa.py:comprova_cobertura_sa()`.

**Steps (idèntics per a cada SA):**
- [ ] **Step 1:** escriure `SAn_guia_docent.md` (desplegament sessió a sessió del doc de programació: minutatge, demos, errors típics, mini-checks) i `SAn_fitxa_alumnat.md` (instruccions de l'alumne, individual).
- [ ] **Step 2:** escriure el codi d'alumnat: cada programa en carpeta pròpia amb `EXPLICACIO.md` (per què + codi per blocs + fitxer complet; bastides com a secció «🧗 Si t'encalles» dins l'explicació). Comentaris en català sense accents. Verificar sintaxi: `python tools/qa.py --nomes-sintaxi`.
- [ ] **Step 3:** escriure `SAn_esquemes_connexions.md` (connexions al Micro:shield: pin, cable, sensor — en taules; sense imatges de moment, placeholder d'imatge NO: descripció textual completa), `SAn_fitxa_ampliada.md` (+ampliació per a qui va sobrat), checklists docent/alumnat.
- [ ] **Step 4:** escriure `Reptes/Reptes_SAn.md` (3 reptes: ⭐ bàsic / ⭐⭐ mig / ⭐⭐⭐ avançat) + solucionari amb codi complet.
- [ ] **Step 5:** `python tools/qa.py` — la cobertura de SA1..SAn ha de passar. `python web/_generador/generar.py` sense errors. Commit `feat(classes): SAn <titol>`.

**Particularitats (programes de `codi/` per SA):**

- **Task 7 — SA1 Hola, robot!** (3 sessions): `hola_mon` (display «HOLA», cor), `emocions_botons` (A/B canvien cara), `dau_sacseig` (acceleròmetre → nombre aleatori). Extra: `SA1_prova_diagnostica.md`, `SA1_normes_seguretat.md` (adaptades: electricitat baixa, làser només docent).
- **Task 8 — SA2 Sortides** (4 sessions): `semafor_leds` (LEDs externs al shield), `neopixel_colors` (tira WS2812B), `musica_altaveu` (module `music`), `servo_saluda` (servo 180° al shell). Producte S4: seqüència so+llum+moviment.
- **Task 9 — SA3 Entrades** (4 sessions, S4 = prova T1): `nivell_llum` (sensor intern + TEMT6000), `termometre` (LM35/DHT11 + display), `alarma_ultrasons` (HC-SR04), `mascota_reactiva` (integra: llum/so/sacseig → reaccions display+servo — programa de la mascota T1). Fabricació mascota segons `00_Projecte_T1_Mascota.md`.
- **Task 10 — SA4 Funcions i moviment** (4 sessions): `funcions_moviments` (defs per a endavant/enrere/gir amb motoreductors via driver del shield), `coreografia` (seqüència de moviments parametritzada), `velocitat_pwm` (control de velocitat). Nota tècnica: documentar a la guia com s'alimenten i connecten els motoreductors Keyestudio al Micro:shield (pins, driver, piles AA).
- **Task 11 — SA5 Ràdio** (3 sessions): `radio_missatges` (xat 5×5), `comandament` (una micro:bit envia ordres A/B/gestos), `receptor_vehicle` (rep ordres i mou motors — base del vehicle T2). Protocol: grups de ràdio per alumne (canal = número de llista) per evitar interferències — documentat a la guia.
- **Task 12 — SA6 Control** (4 sessions, S4 = prova T2): `termostat_histeresi` (LM35 + relé/LED, llaç tancat), `maquina_estats_semafor` (FSM amb dict/if), `registre_dades` (data logging natiu V2, lectura per USB), `vehicle_seguretat` (vehicle T2: teledirigit + aturada d'emergència per polsador/ràdio; ultrasons com a ampliació opcional — decisió del docent 31/07; els ultrasons debuten a SA7 — producte del trimestre). Fabricació vehicle segons `00_Projecte_T2_Vehicle.md`.
- **Task 13 — SA7 Robòtica mòbil** (4 sessions): `calibratge_motors` (rectilini), `segueix_linia` (sensor seguidor de línia Keyestudio), `evita_obstacles` (HC-SR04 + gir), `rover_missions` (missions combinades a pista). Guia: conversió vehicle→rover (afegir sensors al xassís del T2).
- **Task 14 — SA8 Autonomia i telemetria** (3 sessions): `telemetria_radio` (rover emet distància/estat → estació base ho mostra), `estacio_base` (segona micro:bit: display + registre), `comportaments` (prioritats: seguir línia fins obstacle → esquivar → tornar). Sense núvol.
- **Task 15 — SA9 Repte final** (5 sessions, S5 = prova T3): sense codi nou obligatori — `plantilla_projecte/plantilla_projecte.py` (esquelet comentat: seccions sensors/decisió/actuació) + `00_General/00_Guia_defensa_oral.md` ja fet. Extra: `SA9_dossier_plantilla.md`, `SA9_reptes_proposats.md` (6 reptes lliures amb el rover + sensors dels kits: reg automàtic amb bomba+humitat, rover missatger guiat, sentinella PIR…). No hi ha `Reptes_SA9.md` (el projecte ÉS el repte; igual que al germà, que acaba a `Reptes_SA8.md`).

---

### Task 16: Avaluació — proves i fulls

**Files:**
- Create a `Avaluació/`: `00_LLEGEIX-ME_Avaluacio.md`, `Prova_practica_T1.md` (individual, micro:bit + sensors: 4-5 exercicis pràctics amb barem), `Prova_practica_T2.md` (moviment + ràdio + FSM), `Prova_practica_T3.md` (per estacions rotatives: taula micro:bit + pista rover per torns), `Full_seguiment_grup.md`, `Full_qualificacio_competencies.md`, `README.md`
- Create: `Classes/Solucionari/Proves_T1_T2_T3_solucions.md`

**Interfaces:**
- Consumes: criteris del `06_…` i rúbriques del `07_…` (Task 3).

- [ ] **Step 1:** escriure les 3 proves amb exercicis concrets, barem per exercici (total 10) i vincle exercici→criteri d'avaluació; solucionari amb codi complet.
- [ ] **Step 2:** fulls de seguiment i qualificació (taules per alumne, dimensions del model d'avaluació).
- [ ] **Step 3:** `python tools/qa.py`. Commit `feat(avaluacio): proves trimestrals i fulls`.

---

### Task 17: Recursos i Simulacions

**Files:**
- Create a `Recursos/`: `00_LLEGEIX-ME_Recursos.md`, `Enllacos_i_tutorials.md` (els validats de la recerca: microbit.org First lessons, docs MicroPython readthedocs, INTEF castellà, XTEC Python batxillerat, docs Keyestudio del shield i kits, awesome-microbit; cada un amb ús recomanat i llicència), `Referencia_MicroPython_microbit.md` (xuleta pròpia: display/botons/ràdio/pins/música — 2 pàgines), `plantilles_laser/README.md` + plantilles SVG de mascota/vehicle/rover (adaptar `GERMA\tools\genera_plantilles_laser.py` si serveix, o dibuixar SVG paramètric nou a `tools/genera_plantilles_laser.py`)
- Create a `Simulacions/`: `Index_simulacions.md`, `Simulador_microbit.md` (què simula python.microbit.org i què no — llista exacta; com usar-lo per a cada SA; límits: no simula shield/motors), `Wokwi_opcional.md` (només per a l'opció Pico)

**Interfaces:**
- Consumes: llista de recursos de la recerca (a l'espec §7).

- [ ] **Step 1:** escriure documents de Recursos; generar les plantilles SVG amb el script i desar-les (mascota: cos + orelles amb ranura servo; vehicle: base + suports motor; rover: afegits de sensors sobre el vehicle).
- [ ] **Step 2:** escriure Simulacions. `python tools/qa.py`. Commit `feat(recursos): enllacos validats, plantilles laser i simulacions`.

---

### Task 18: Web final, QA global i publicació

**Files:**
- Modify: el que el QA/generador destapin
- Create: `Memòria treball/2026-XX-XX_Creacio_del_curs.md` (registre de decisions, com fa el germà)

- [ ] **Step 1:** `python tools/qa.py` complet (cobertura SA0-SA9, enllaços, quadre d'hores, sintaxi) → arreglar tot el que falli.
- [ ] **Step 2:** `python web/_generador/generar.py` → revisar `web/index.html`, vista alumnat i vista docent manualment (obrir al navegador).
- [ ] **Step 3:** escriure el document de memòria de treball; actualitzar `GUIA_INICI_DOCENT.md` amb l'itinerari de lectura definitiu.
- [ ] **Step 4:** commit `docs: memoria de creacio i guia inici docent`. Crear repositori GitHub (`gh repo create`, públic, com el germà) + push + activar Pages — **només amb confirmació del docent** (publicació externa).

---

### Fase posterior (fora d'aquest pla)

- `Material Classroom/`: scripts data-driven per crear tasques/qüestionaris/rúbriques al Google Classroom del grup — quan el Classroom del curs existeixi (skill `classroom-sync`).
- Imatges/fotos reals de muntatges (es faran al setembre amb el maquinari davant).
- Opció Pico: només si s'aprova compra.

## Self-review

- Cobertura de l'espec: identitat/normativa→T2; sabers/avaluació/seqüenciació→T3-T4; fil conductor→T5 + T9/T12/T13; SA per SA→T7-T15; avaluació→T16; recursos/simulacions→T17; infraestructura/web→T1/T18; fora d'abast respectat (cap task d'interfícies, núvol ni compres). ✔
- Sense placeholders: cada task nomena fitxers exactes i continguts concrets; el codi d'alumnat s'especifica per programa amb comportament definit. ✔
- Consistència de noms: títols de SA idèntics a l'espec §4; sufixos de fitxer = convenció del germà; `qa.py` adaptat a `.py` únicament. ✔
