# Programació didàctica — Robòtica amb Python · 1r de Batxillerat
### Curs 2026-2027 · LOMLOE · Catalunya (Decret 171/2022, modificat pel Decret 103/2026)

> Conjunt de documents Markdown que conformen la programació didàctica completa de la matèria.
> **Hores:** 2 h setmanals · **Modalitat:** anual (≈ 70 h) · **Llengua:** català.
> **Referent curricular:** optativa **pròpia de centre**, ancorada a la **Competència específica 5** (control programat i robòtica) i als criteris **5.1/5.2** de *Tecnologia i Enginyeria I*, i al bloc de sabers **Automatització**. Vegeu `../Normativa/01_Normativa_LOMLOE_RoboticaPython_1Batx.md`.

---

## 📑 Índex de documents

| # | Document | Contingut |
|---|---|---|
| 00 | `00_Index_general.md` | Aquest índex, decisions clau i com navegar. |
| 01 | `01_Introduccio_context_justificacio.md` | Context, justificació, alumnat, marc normatiu. |
| 02 | `02_Objectius_competencies.md` | Competències clau, competències específiques de la matèria i objectius. |
| 03 | `03_Sabers_i_continguts.md` | Sabers organitzats en blocs i la seva distribució. |
| 04 | `04_Metodologia.md` | Enfocament competencial, treball individual, PRIMM, eines, espais. |
| 05 | `05_Atencio_a_la_diversitat.md` | Mesures universals, addicionals i intensives. |
| 06 | `06_Avaluacio_criteris_qualificacio.md` | Criteris d'avaluació, instruments i ponderació. |
| 06b | `06b_Avaluacio_programacio_i_practica_docent.md` | Avaluació de la programació mateixa i de la pràctica docent. |
| 07 | `07_Rubriques.md` | Rúbriques d'avaluació reutilitzables (R1-R5). |
| 08 | `08_Sequenciacio_temporal_anual.md` | Seqüenciació de les 9 situacions d'aprenentatge. |
| 09 | `09_Materials_recursos_per_unitat.md` | Mapatge del maquinari disponible a cada unitat. |
| 09b | `09b_Guia_compra_pressupost.md` | Llista de compra i pressupost orientatiu per engegar des de zero. |
| 09c | `09c_Inventari_kits_disponibles.md` | Inventari del maquinari real del centre i on s'usa cada element. |
| 10-18 | `10_SA1...` → `18_SA9...` | Les 9 situacions d'aprenentatge (unitats), a `../Classes/SA1`…`SA9`. |

---

## 🧭 Fil conductor de la matèria

> **"D'un component al rover autònom"**: cada alumne, treballant **individualment**, avança del control d'un component electrònic fins a la programació i la documentació d'un **rover autònom propi** que resol un repte real.

**Tres etapes (una per trimestre), cadascuna amb el seu artefacte individual:**

1. **Fonaments** — programació MicroPython amb la micro:bit V2 + Micro:shield; fil conductor: **la mascota** (una criatura amb cara, llums i so a la matriu LED que reacciona a estímuls).
2. **Control i moviment** — funcions, ràdio i sistemes de control; fil conductor: **el vehicle** (un xassís amb motors que es mou i respon a comandaments).
3. **Robòtica i integració** — robòtica mòbil, autonomia i projecte final; fil conductor: **el rover** (el vehicle evoluciona a un robot autònom amb sensors i telemetria).

Cada alumne fabrica, munta i programa el **seu propi** exemplar a cada etapa (peces de fabricació digital pretallades pel docent si cal, vegeu `08_Sequenciacio_temporal_anual.md`). No hi ha treball en parella ni en grup en cap moment del curs.

---

## ⚙️ Decisions de disseny preses (ajustables)

1. **Un sol llenguatge, MicroPython, de principi a fi.** No hi ha Arduino/C++ en aquest curs: tot el codi d'alumnat és `.py` executat a la micro:bit V2. La progressió és interna a Python (seqüències → variables/bucles → condicionals → funcions → estructures de dades/esdeveniments → integració); vegeu `03_Sabers_i_continguts.md`.
2. **Treball 100 % individual.** Cada alumne té el seu propi maquinari (1 micro:bit V2 + 1 Micro:shield + kits Keyestudio) i construeix el seu propi fil conductor (mascota/vehicle/rover). No es dissenyen rúbriques ni fitxes de coavaluació de grup; l'ajuda entre iguals es fomenta com a dinàmica d'aula, no com a producte compartit (vegeu `04_Metodologia.md`).
3. **2 h setmanals anuals (≈ 70 h).**
4. **Avaluació per projectes/situacions d'aprenentatge** amb quadern tècnic (*logbook*) i defenses orals individuals.
5. **Maquinari nucli: micro:bit V2 + Micro:shield + kits Keyestudio**, 1 de tot per alumne (vegeu `09c_Inventari_kits_disponibles.md`).
6. **Simulador (python.microbit.org)** com a pla B quan un component falla o mentre s'espera reposició.

> ⚠️ **A confirmar amb el centre:** hores exactes (2/3 h) i continuïtat a 2n. Vegeu `../Normativa/01_Normativa_LOMLOE_RoboticaPython_1Batx.md`.

---

## 🗺️ Mapa de seqüenciació (resum)

| Trim. | SA | Títol | Hores | Maquinari | Progressió Python |
|---|---|---|---|---|---|
| 1r | SA1 | Hola, robot! | 6 | micro:bit V2 | Seqüències |
| 1r | SA2 | Sortides: el robot actua | 8 | micro:bit V2 + Micro:shield | Variables i bucles |
| 1r | SA3 | Entrades: el robot percep | 8 | micro:bit V2 + Micro:shield + Keyestudio | Condicionals |
| 2n | SA4 | Funcions i moviment | 8 | Micro:shield + servos/motors Keyestudio | Funcions |
| 2n | SA5 | Ràdio: robots que parlen | 6 | micro:bit V2 (ràdio) | Esdeveniments i estructures de dades |
| 2n | SA6 | Control: el robot decideix | 8 | Micro:shield + sensors Keyestudio | Màquines d'estats (objectes només d'ús) |
| 3r | SA7 | Robòtica mòbil: el rover | 8 | Rover individual (fil conductor) | Integració |
| 3r | SA8 | Autonomia i telemetria | 6 | Rover + ràdio + sensors | Integració (dades) |
| 3r | SA9 | Repte final integrador | 10 | Lliure (tot el maquinari) | Integració final |

**Total: 68 h** (+ marge ~2 h per a diagnòstic i imprevistos fins a 70 h). Les proves T1, T2 i T3 ocupen, senceres, la S4 de SA3, la S4 de SA6 i la S5 de SA9 (vegeu `08_Sequenciacio_temporal_anual.md`).
