# CLAUDE.md — Curs Robòtica amb Python, 1r Batxillerat

Material docent en **català** (Robòtica amb Python, 1r Batx, LOMLOE). Markdown font única;
`web/_generador/generar.py` construeix la web (doble vista alumnat/docent) i
`generar_pdf.py` els PDFs (Chrome/Edge headless). GitHub Pages publica a cada push a `main`.

## Regles

- **Tot en català** als documents. **EXCEPCIÓ: els comentaris del codi d'alumnat
  (`.py`) van en català SENSE accents** (evita problemes de codificació als editors
  dels alumnes).
- **Tot el treball de l'alumnat és individual**: cap activitat en parelles ni en grup.
  No es dissenyen rúbriques ni fitxes de coavaluació de grup.
- **Maquinari nucli: micro:bit V2 + Micro:shield + sensors Keyestudio.** Codi d'alumnat
  només `.py` (MicroPython): **cap `.ino` ni referència a Arduino/compilació** en aquest
  repositori (a diferència del curs germà, que és amb Arduino + C/C++).
- **`web/` (excepte `_generador/`, `assets/css/estil.css`, `assets/js/lloc.js` i
  `README.md`) és artefacte generat**: no s'edita a mà.
- **Abans de committar**: `tools/qa.py` ha de passar (enllaços, cobertura de SA, quadre
  d'hores de `08_Sequenciacio_temporal_anual.md`, sintaxi dels `.py` d'alumnat amb
  `ast.parse`). Mentre el material de les SA encara no existeix, usa
  `tools/qa.py --nomes-sintaxi` (salta cobertura i checks de contingut). El CI **no**
  compila cap sketch: no hi ha job d'Arduino/ESP32.
- **Contracte de cobertura per SA**: definit a `tools/qa.py:comprova_cobertura_sa()` —
  README, guia_docent, fitxa_alumnat, fitxa_ampliada, checklists docent/alumnat,
  qüestionari de conceptes, exemple resolt, i per SA1–SA8 esquemes de connexions +
  `Reptes/Reptes_SAn.md` + solucionari.
- **Quadre d'hores nou** (doc `Programació didàctica/08_Sequenciacio_temporal_anual.md`,
  quan existeixi): SA1=6, SA2=8, SA3=8 (T1) · SA4=8, SA5=6, SA6=8 (T2) · SA7=8, SA8=6,
  SA9=10 (T3) → **68 h + marge** (~70 h de curs). `tools/qa.py:comprova_hores()` valida
  que la taula del document suma el subtotal declarat.
- **Cada SA té el seu document 1:1 a `Programació didàctica/`** — mantén-los sincronitzats.
- **`Material Classroom/`** (si es reutilitza del germà): scripts Node data-driven.
  `credentials.json` i `token.json` són secrets OAuth: no els moguis ni els mostris; no
  n'afegeixis de nous al control de versions.
- **`.superpowers/`** és el workspace intern de treball amb Claude Code (specs, plans):
  no és material docent, no es committeja (al `.gitignore`).

## Convencions

- Nomenclatura estricta: `SA{n}_{tipus}.md` (sufixos `_guia_docent`, `_fitxa_alumnat`,
  `_fitxa_ampliada`, `_checklist_*`, `_esquemes_connexions` determinen la vista
  alumnat/docent de la web); transversals `00_Nom.md`; plantilles `*_PLANTILLA.md`.
- Sense frontmatter YAML: metadades al nom de fitxer + primer `# H1` + línia
  `**Durada:** … · **Maquinari:** …`.
- Directives del generador en comentaris HTML: `<!-- web:only-github -->…<!-- /web:only-github -->`.
- Material transversal a `Classes/00_General/` amb capçalera `> **Per a qui és?**`.
- **Pàgines de pràctica**: cada sketch d'alumnat (`Classes/SAn/codi/`) duu una
  `EXPLICACIO.md` al costat (`<nom>_EXPLICACIO.md` si el sketch és un fitxer solt) que el
  generador converteix en pàgina pròpia (per què es fa + codi per blocs + fitxer complet
  plegat). Les bastides NO són sketches: viuen com a secció «🧗 Si t'encalles» (bloc
  `<details markdown="1">`) dins de l'explicació de la pràctica base. Ho vigila
  `tools/qa.py:comprova_explicacions()`.
- Commits en català, tipus Conventional Commits.
