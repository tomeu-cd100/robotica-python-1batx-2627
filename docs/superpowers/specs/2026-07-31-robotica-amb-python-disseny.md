# Disseny del curs «Robòtica amb Python» — 1r de Batxillerat · Curs 2026-2027

> Document de disseny validat amb el docent el 31/07/2026. És l'especificació de
> partida per crear tot el material del curs. El pla d'implementació se'n deriva.

## 1. Identitat de la matèria

- **Nom:** Robòtica amb Python.
- **Tipus:** **optativa pròpia de centre**, **anual**, **2 h/setmana** (≈ 35 setmanes ≈ **70 h**).
- **Destinataris:** alumnat de 1r de batxillerat de **qualsevol modalitat**, grup mixt
  de **15-20 alumnes**, **sense base prèvia de programació** (es comença de zero).
- **Idea força:** Python sempre sobre maquinari — **robòtica des del dia 1**. Res
  d'interfícies d'usuari ni d'aplicacions locals/núvol: tot el curs és **robot físic**.
- **Treball individual:** totes les activitats, construccions i projectes són
  **individuals** (hi ha dotació de material per a tot l'alumnat). La coavaluació i
  l'ajuda entre iguals es mantenen com a dinàmica d'aula, però cap producte és compartit.
- **Maquinari de referència: micro:bit** (dotació assegurada, 1 per alumne). Pico i
  pyFirmata queden com a opcions documentades, fora del nucli del curs.
- **Relació amb altres cursos:** conviu en paral·lel amb l'optativa «Robòtica»
  (Arduino/C++, repositori `Curs 2627 1 Batx Robotica`). **Franges horàries diferents:
  sense conflicte de material.** Els dos cursos comparteixen aula, kits i infraestructura
  tècnica de material docent.

## 2. Encaix normatiu

- **Marc:** LOMLOE → RD 243/2022 → **Decret 171/2022** + **Decret 103/2026** (DOGC 9704,
  9/7/2026, definitiu; s'aplica a 1r el 2026-27). Optatives de 1r: 6 h setmanals totals
  en 2-3 franges, cada matèria entre 2 i 4 h. Les 2 h anuals hi encaixen.
- **Via triada:** optativa **pròpia de centre** (Decret 102/2010 d'autonomia + DOIGC).
  Requisits: **nom diferent** de les optatives oficials del decret («Robòtica» i
  «Programació» ja existeixen com a oficials — «Robòtica amb Python» compleix) i
  **vinculació a una matèria de modalitat de referència**.
- **Ancoratge curricular:** **CE5 de Tecnologia i Enginyeria I** («dissenyar, crear i
  avaluar sistemes tecnològics aplicant coneixements de la regulació automàtica, del
  control programat i de les tecnologies emergents…»), amb els **criteris 5.1 i 5.2**
  i els **sabers del bloc Automatització** (llenguatges de programació textual, sistemes
  de control, robòtica i trajectòries, telemetria). Mateix blindatge que el curs germà.
- **Criteris d'avaluació:** els defineix el professorat (com a totes les optatives),
  derivats de CE5.1/CE5.2, amb rúbriques pròpies.
- **Pendent de centre (checklist, no bloqueja el disseny):** aprovació de l'optativa
  pròpia al PEC/PGA; confirmació de franja i mínim de 10 alumnes (DOIGC).
- **Fonts:** PDF oficials descarregats a `Normativa/` (currículums de «Programació» i
  «Robòtica» d'XTEC, Decret 103/2026, annex 3 d'horari, infografia 2026-27). Es
  redactarà una síntesi pròpia `Normativa/01_Normativa_LOMLOE_RoboticaPython_1Batx.md`
  seguint el model del curs germà.

## 3. Maquinari i entorns

| Fase | Plataforma | Disponibilitat |
|---|---|---|
| T1-T2 | **micro:bit V2 + Micro:shield** (1 per alumne) + sensors/actuadors dels kits Keyestudio | ✅ ja al centre |
| T2 | Motoreductors, rodes, micro servos (Kit 2 Keyestudio) | ✅ ja al centre |
| T1-T3 | **Fil conductor de construccions** (mascota T1, vehicle T2, rover T3): DM tallat amb xTool S1 + peces Bambu P2S + motors/sensors Keyestudio + micro:bit | ✅ fabricació pròpia, només consumibles |
| Opcional | **Raspberry Pi Pico** (MicroPython amb Thonny) | 💰 opció documentada **no bloquejant** (full de compra a `09b`) |
| Opcional | Python a PC + Arduino UNO via pyFirmata | ✅ documentat com a ampliació; fragilitat coneguda (pyFirmata sense manteniment, provar `pyfirmata2` amb el Python de les aules) |

- **Entorns:** editor oficial **python.microbit.org** (amb simulador integrat WebAssembly:
  display, botons, sensors interns, ràdio — no simula maquinari extern) i **Thonny**.
  **Wokwi** per a Pico/UNO si s'activa l'opció. El simulador és el pla B d'avaries i la
  feina a casa.
- **Ràdio:** la comunicació entre micro:bits (mòdul `radio`) és el canal de telemetria
  del curs — una segona micro:bit fa d'**estació base física**. Cap servei al núvol.
- **Registre de dades:** data logging natiu de la micro:bit V2 (fitxer a la placa,
  llegible per USB). Tot físic i local.

## 4. Seqüenciació anual (9 SA · 70 h)

Mateix esquema d'hores, marge i contingència que el curs germà (2 h/setmana, proves
pràctiques trimestrals amb sessió pròpia dins la SA de tancament del trimestre).

| Trim. | SA | Títol | Hores | Contingut nuclear |
|---|---|---|---|---|
| 1r | SA1 | Hola, robot! | 6 | Què és un robot, entorns (editor micro:bit), primer programa Python, display i botons, seguretat, diagnòstic inicial |
| | SA2 | Sortides: el robot actua | 8 | LED, NeoPixel, so/música, servo (shield Keyestudio); variables, bucles |
| | SA3 † | Entrades: el robot percep | 8 | Botons, sensors interns (acceleròmetre, llum, temperatura) i externs (ultrasons, LDR, DHT11); condicionals · **prova T1** |
| 2n | SA4 | Funcions i moviment | 8 | Funcions, motors DC i motoreductors, trajectòries bàsiques |
| | SA5 | Ràdio: robots que parlen | 6 | Mòdul `radio`, comandament a distància, jocs multi-placa, protocols senzills |
| | SA6 † | Control: el robot decideix | 8 | Llaç obert/tancat, histèresi (termòstat), màquines d'estats, data logging · **prova T2** |
| 3r | SA7 | Robòtica mòbil: el rover | 8 | Muntatge del rover fabricat, cinemàtica diferencial, seguidor de línia, evita-obstacles |
| | SA8 | Autonomia i telemetria | 6 | Comportaments autònoms combinats, telemetria per ràdio a estació base, dades del recorregut |
| | SA9 † | Repte final integrador | 10 | Projecte **individual** amb el rover + sensors lliures, documentació tècnica, defensa oral · **prova T3** |
| | | **Subtotal** | **68** | + ~2 h de marge |

### Fil conductor de construccions trimestrals

Cada trimestre tanca amb una **construcció real individual** (làser xTool S1 + Bambu
P2S + material dels kits — hi ha dotació per a tot l'alumnat), seguint el model del
curs germà però amb **tot el treball individual: cap activitat en parelles**:

| Trim. | Construcció | Tanca a | Què consolida | Evolució |
|---|---|---|---|---|
| T1 | **Mascota expressiva** — carcassa DM al voltant de la micro:bit; display com a cara, servo (orelles/cua), reacciona a llum/so/sacsejada | SA3 | sortides + entrades | — |
| T2 | **Vehicle teledirigit** — xassís DM + 2 motoreductors i rodes (Kit 2), comandament per ràdio des d'una segona micro:bit, aturada d'emergència per ultrasons | SA6 | moviment + ràdio + control | precursor directe del rover |
| T3 | **Rover autònom** — evolució del vehicle del T2: seguidor de línia, evita-obstacles, telemetria a estació base | SA9 | integració total | reutilitza xassís i motors del T2 |

- La fabricació grossa (xassís, rodes de suport) es fa **un sol cop al T2**; el T3
  afegeix sensors i autonomia, no reconstrueix.
- **Fabricació:** les sessions de tall/impressió es planifiquen com al curs germà,
  **consumint per endavant les retallades del pla de contingència** — amb les tres
  construccions el **marge efectiu queda ≈ 0**; si el calendari s'estreny, les peces
  arriben **pretallades pel docent**.
- **Consumibles del fil conductor:** DM 3 mm + filament PLA + cargols/portapiles.
  Amb construccions **individuals** (15-20 unitats en lloc de ~10 per parelles), la
  previsió puja a **~250-350 €/curs** (full de compra a `09b`); mitigació: *nesting*
  agressiu a làser i disseny de xassís minimalista.
- **Pla de contingència:** no es retallen mai SA1-SA3 ni SA9; primera retallada a les
  sessions de producte de SA2/SA4 (assignades a fabricació); SA8 comprimible de 6 h a
  4 h (assignada a fabricació T3); SA7 de 8 h a 6 h com a **única palanca lliure**.
- **Progressió Python:** seqüències → variables/bucles (SA2) → condicionals (SA3) →
  funcions (SA4) → estructures de dades i esdeveniments (SA5-SA6) → integració (SA7-SA9).
  Objectes: només ús (no definició de classes), nivell inicial real del grup.

## 5. Avaluació

- **Model:** rèplica del curs germà — avaluació competencial contínua amb: **projectes
  i productes** (rúbriques), **proves pràctiques trimestrals** (20 %, individuals, sessió
  sencera dins SA3/SA6/SA9), **mini-checks** individuals de 10', **quadern/documentació
  tècnica**. Qualificació 1-10 sense decimals.
- **Referents:** criteris d'avaluació propis derivats de **CE5.1** (controlar i
  experimentar sistemes robòtics amb llenguatges de programació) i **CE5.2**
  (automatitzar, programar i experimentar trajectòries de robots amb algorismes).
- **Cap evidència no compta dues vegades** (mateixa regla que el curs germà).

## 6. Estructura de carpetes i infraestructura

Rèplica exacta de `Curs 2627 1 Batx Robotica`:

```
Normativa/                  PDF oficials + síntesi pròpia
Programació didàctica/      00-18: índex, justificació, objectius, sabers, metodologia,
                            diversitat, avaluació, rúbriques, seqüenciació, materials,
                            un document per SA (10-18)
Classes/SA0..SA9/           guia_docent, fitxa_alumnat, fitxa_ampliada, checklists,
                            esquemes de connexions, codi/ amb EXPLICACIO.md per sketch
Classes/00_General/         material transversal (fil conductor rover, entorns)
Classes/Solucionari/
Reptes/Reptes_SAn.md        + Solucionari/
Avaluació/                  proves T1-T3, fulls de seguiment i qualificació
Recursos/                   enllaços validats, plantilles làser del rover, fitxes
Simulacions/                projectes del simulador micro:bit (i Wokwi si s'activa Pico)
Material Classroom/         scripts Node data-driven (adaptats del curs germà)
tools/qa.py                 QA adaptat (cobertura SA, enllaços, sintaxi .py, quadre d'hores)
web/_generador/             web estàtica doble vista alumnat/docent → GitHub Pages
CLAUDE.md                   convencions (català, comentaris de codi sense accents, QA)
```

- **Adaptacions del QA:** desapareix la compilació `.ino`; s'hi afegeix comprovació de
  sintaxi MicroPython de tot el codi d'alumnat (`py_compile` amb stubs o validació AST).
- **Codi d'alumnat:** `.py` amb comentaris en català **sense accents** (convenció del
  curs germà).

## 7. Recursos font (per agafar idees; s'enllacen, no es copien)

| Recurs | Ús al curs |
|---|---|
| First lessons with Python (microbit.org) | esquelet d'activitats de SA1-SA2 |
| Tutorials + docs oficials MicroPython micro:bit (readthedocs) | referència d'API permanent |
| Teach Computing KS4 Physical Computing (buggy + rúbrica) | model de SA7 i de rúbrica de projecte final |
| INTEF «Programando la micro:bit con Python» i PDF de projectes | material en castellà per a l'alumnat |
| XTEC «Pensament computacional — Python batxillerat» | referència curricular citable a la programació |
| Docs Keyestudio del Micro:shield i kits de sensors | esquemes de connexió del maquinari concret |
| awesome-microbit (GitHub, CC0) | directori de drivers i idees (p. ex. drivers MicroPython de robots) |
| Get Started with MicroPython on Pico (PDF CC) | base de l'opció Pico si s'activa |
| Real Python — Arduino With Python (pyFirmata) | base de l'ampliació pyFirmata |

**Buit d'oportunitat:** no existeix cap curs complet en català de MicroPython per a
batxillerat — aquest curs l'omple i es publica obert (CC BY-SA, com el curs germà).

## 8. Fora d'abast (decidit explícitament)

- Interfícies d'usuari, apps d'escriptori/mòbil i serveis al núvol.
- Compra de maquinari com a condició per començar (Pico i pyFirmata són opcions).
- Definició de classes pròpies en Python (només ús d'objectes).
- Competicions externes (poden aparèixer com a extensió de SA9, no com a requisit).
