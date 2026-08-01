# Pla d'implementació — Millores pedagògiques (auditoria 01/08/2026)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development. Steps use checkbox (`- [ ]`) syntax.

**Goal:** aplicar el pla de millora P1-P4 de `Memòria treball/2026-08-01_Avaluacio_instruccional_curs.md` a teoria, repàs, avaluació i creació, perquè l'escriptura autònoma de codi sigui obligatòria, freqüent i avaluada.

**Architecture:** els canvis toquen documents font (md) i codi d'alumnat; `tools/qa.py` i el generador validen; cada task acaba amb QA net i commit.

**Tech Stack:** markdown + MicroPython; `py -3.13` per a totes les verificacions.

## Global Constraints

- Tot en català; comentaris de codi `.py` en català SENSE accents; sense frontmatter YAML.
- Tot individual; maquinari només el de `09c`; pins segons mapa §1b del fil conductor; res de núvol.
- Hores/sessions NO es toquen (6+8+8/8+6+8/8+6+10 = 68+2): les katas caben als 10' d'activació ja previstos; el repte ⭐ passa al temps de pràctica existent.
- Abans de cada commit: `py -3.13 tools/qa.py` = 0 problemes + `py -3.13 web/_generador/generar.py` net.
- El curs germà és només lectura. Commits català Conventional Commits.
- Referència de les decisions: `Memòria treball/2026-08-01_Avaluacio_instruccional_curs.md` (pla P1-P4).

---

### Task 1: Banc de katas d'activació (P1.1 + repàs espaiat)

**Files:** Create `Classes/00_General/00_Banc_activacio_repas.md`; Modify `Classes/SA2..SA9/SAn_guia_docent.md` (1-2 línies per sessió d'activació referenciant la kata del banc).

- Banc de ~30 katas (una per sessió S4-S33), cadascuna: enunciat de 10', tipus (Parsons / completar buits / escriure de zero — progressió dins de cada concepte), concepte que repassa (espaiat: sempre material de fa 1-2 setmanes), solució completa (bloc docent), i criteri ràpid de correcció a mà alçada.
- Mapa sessió→kata en taula; conceptes coberts: variables, while, if/elif, for-range, funcions/paràmetres, return, global, llistes, for-col·lecció, diccionaris, FSM, radio, try/except.
- Cada guia docent: a l'apartat d'activació de cada sessió, línia «Kata del dia: [Kn del banc]».

### Task 2: Tapar forats de teoria (P2)

**Files:** Modify: `Classes/SA4/codi/funcions_moviments/` (+activitat return a fitxa alumnat SA4 i guia S2), `Classes/SA4/codi/control_per_botons/EXPLICACIO.md` (+prosa sobre `global` i àmbit), `Classes/SA2/SA2_fitxa_alumnat.md` + `Classes/SA2/codi/pwm_led_rgb/EXPLICACIO.md` (formalitzar `for`), `Classes/SA5/` (for-sobre-col·lecció amb llistes de missatges: activitat + codi), `Classes/SA7/` (try/except introduït a S2-S3 amb kata/activitat contextual: lectura robusta de sensor), `Classes/SA8/codi/telemetria_radio|estacio_base/EXPLICACIO.md` (referir try/except a SA7, no estrenar-lo), `Classes/SA8/codi/comportaments/` (refactor exemple al patró percep/decideix/actua + EXPLICACIO), `Programació didàctica/1x_*.md` afectades (sessions i sabers sincronitzats) i `03_Sabers_i_continguts.md` si cal.

- Nova activitat nucli SA4-S2: escriure `distancia_en_passos(cm)` (o equivalent de la fitxa 13) que retorna valor i s'usa.
- S28 queda amb ≤3 conceptes nous (I2C/bits llegits + dict dinàmic); try/except i for-col·lecció ja vistos abans.

### Task 3: Repte ⭐ obligatori + mini-checks d'escriptura (P1.2-P1.3)

**Files:** Modify: `Reptes/Reptes_SA1..SA8.md` (repte ⭐ marcat NUCLI OBLIGATORI; ⭐⭐/⭐⭐⭐ opcionals), `Classes/SAn/SAn_fitxa_alumnat.md` + `SAn_guia_docent.md` + `SAn_checklist_*` (el repte ⭐ entra al flux i a l'avaluació del producte), `Classes/00_General/00_Mini_checks_individuals.md` (tots els mini-checks passen a ESCRIPTURA de codi curt sense apunts, estil SA4; +registre del tipus d'error: sintaxi/concepte/descuit), `Programació didàctica/06_Avaluacio_criteris_qualificacio.md` (el millor mini-check del trimestre qualifica dins la dimensió proves — definir pes i mecànica).

### Task 4: Qüestionaris amb codi (P3.10)

**Files:** Modify `Classes/SA1..SA9/SAn_questionari_conceptes.md` (+solucions): substituir 3 de les 10 preguntes per (a) «què mostra aquest codi?» (traça), (b) «completa la línia que falta», (c) «troba i corregeix l'error» — codi del nivell de la SA, sincronitzat amb solucions.

### Task 5: Proves i rúbriques (P3.9, P3.11, P3.12)

**Files:** Modify: `Avaluació/Prova_practica_T2.md` i `T3.md` (+ítem obligatori 2 punts «escriu una funció nova amb paràmetre i return» — T3: comportament nou del rover no vist; rebalanceig del barem T3: calibratge màx. 2 punts; tot ha de seguir sumant 10), `Classes/Solucionari/Proves_T1_T2_T3_solucions.md` + codi (solucions dels ítems nous), `Programació didàctica/07_Rubriques.md` (subcriteri explícit «codi escrit per l'alumne» ≥40 % del pes de R1 en productes), `Programació didàctica/02_Objectius_competencies.md` (objectiu 2 desglossat en 3 resultats observables amb vincle a instruments), `Avaluació/Full_seguiment_grup.md` (columna tipus d'error mini-checks) si escau.

### Task 6: Coavaluació de lectura + QA global i publicació

**Files:** Create `Classes/00_General/00_Parella_de_lectura.md` (protocol 5': checklist 3 ítems — noms de variables, un comentari útil, cap número màgic; sense producte compartit; referències des de guies on toqui — 1 cop per SA a partir de SA2). Modify: `Programació didàctica/04_Metodologia.md` (recull katas, repte ⭐ nucli, parella de lectura — coherència del discurs metodològic). Final: `py -3.13 tools/qa.py` = 0, `generar.py` net, pytest verd, entrada a `Memòria treball/` documentant l'aplicació de les millores, commit i push.

## Self-review

Cobertura del pla de millora: P1.1→T1, P1.2-1.3→T3, P2 (4-8)→T2, P3.9-3.12→T5, P3.10→T4, P4.13→T6, P4.14→T3/T5. Hores intactes; convencions globals a cada task. ✔
