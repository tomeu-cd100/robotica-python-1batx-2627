# Memòria de treball — Tercera ronda de millores (segona auditoria)
### Data: 1 d'agost de 2026

Registre de l'aplicació del pla de la tercera ronda de millores, sorgit de la
**segona auditoria instruccional** (`2026-08-01_Segona_avaluacio_instruccional.md`):
4 tasks que tanquen les troballes N1-N9 i U1-U6.

---

## 1. Què s'ha aplicat

| Troballa(es) | Task | Què s'ha creat/modificat |
|---|---|---|
| N1, N2, N9 | Task 1 | Sessions amb repte ⭐ (SA1-SA8) requadrades a ~100' efectius + fila «marge/imprevistos 20'»; repte ⭐ com a fila pròpia de 25-30'; mini-defensa per mostreig rotatiu; una sola parella de lectura per sessió; el ⭐ afegit a la taula de dimensions de `00_Avaluacio_per_alumnat.md` §1. |
| U1, punt 3, N3 | Task 2 | `Classes/SA0/SA0_guia_programacio.md` creada (seccions A1-A7 + Part B ràdio, les que citen els mini-checks); porta mínima de programació a `06_Avaluacio_criteris_qualificacio.md` §6.3; estatus formatiu dels qüestionaris aclarit. |
| U2, N6, N7, K16 | Task 3 | Bastida «🧗 Si t'encalles» (3 nivells) al repte ⭐ de SA1-SA8; katas K22-K27 (nivell «completar buits») a S32-S33 per als conceptes post-SA4 que no arribaven mai a aquest nivell; K16 variada perquè no dupliqui el mini-check de SA4; `04_Metodologia.md:37` reescrit per no prometre un «repte a full en blanc» inexistent. |
| U3, U4, U5, U6, N4, N5 | Task 4 (aquest) | Vegeu el detall a continuació. |

### Detall del Task 4

- **U3 — Full de sessió imprimible.** `web/_generador/generar_fulls_imprimibles.py`
  s'ha ampliat amb un parser 100 % derivat dels documents font (banc de katas,
  mini-checks, `Reptes_SAn.md` i `SAn_checklist_docent.md`) que genera
  **`Classes/00_General/pdf/00_Quadern_sessions_docent.pdf`**: un únic PDF, una
  pàgina per sessió lectiva (35 sessions, SA1-SA9), amb la kata del dia (enunciat
  complet), el mini-check si toca, el repte ⭐ (enunciat + requisit mínim) si toca
  i el checklist docent d'aquella sessió. S'ha adoptat l'alternativa que el propi
  pla donava per bona (un sol «Quadern del docent per sessions» en lloc de 34+
  PDF individuals) perquè generar-los i enllaçar-los individualment disparava la
  complexitat sense guany real. La marca de sincronia del PDF es calcula sobre el
  text combinat de tots els documents font (`sessions_quadern_font_text()`), i
  `tools/qa.py:comprova_pdfs()` s'ha ampliat perquè detecti si algun d'ells canvia
  sense regenerar el PDF.
- **U4 — Itinerari de recuperació.** `Classes/00_General/00_Vaig_faltar.md`
  (nou): 5 passos (fitxa de la sessió → EXPLICACIO del programa → kata pendent →
  mini-check pendent → entrada del quadern) + nota sobre treballar amb el
  simulador si no hi ha placa a casa. Enllaçat des de la vista alumnat (afegit a
  `GENERAL_ALUMNAT` de `generar.py`, a la taula de `00_LLEGEIX-ME_Classes.md` i
  des de `00_Targetes_rescat.md`).
- **U5 — Temps de preparació del docent.** `GUIA_INICI_DOCENT.md` §1: ~3-4 h de
  lectura inicial (punts 1-7 de l'itinerari) + ~20 min/SA amb el checklist
  docent; cita el nou quadern de sessions com a eina per preparar una sessió
  concreta sense rellegir res.
- **U6 — Pont cap a la SA2 a la fitxa d'alumnat.** Paràgraf «Per què ara el
  Micro:shield?» a l'inici de `Classes/SA2/SA2_fitxa_alumnat.md`, adaptat del
  «Pont cap a la SA2» de `SA1_guia_docent.md`.
- **N4 — Rutina del mini-check unificada.** `00_Mini_checks_individuals.md`
  §Rutina punt 1 reescrit: el mini-check substitueix la kata d'activació **només**
  a SA6/SA7/SA8/SA9 (S20/S24/S28/S31); a la resta de SA conviuen (kata primer,
  mini-check on digui la guia), alineat amb la capçalera del document i amb el
  banc de katas (que ja ho tenia correcte).
- **N5 — Model kata real a la resta de documents.** `04_Metodologia.md` §4.2
  (fila «Activació») i `00_Avaluacio_per_alumnat.md` §3 («Graella d'activació»)
  actualitzats: fora el text fòssil de l'antiga «graella de 5' amb 3 preguntes
  retrospectives», substituït per la descripció real (kata d'activació amb
  progressió Parsons → completar buits → escriure de zero).

## 2. Verificacions

- `py -3.13 tools/qa.py` → **0 problemes** (230 pàgines, 0 enllaços trencats, 22
  PDF versionats amb 0 desfasats un cop regenerats).
- `py -3.13 web/_generador/generar.py` → net.
- `py -3.13 web/_generador/generar_fulls_imprimibles.py` executat després de tots
  els canvis de contingut: 15 PDF regenerats sense error nou (els avisos «falta»
  d'alguns fulls de `00_General` són pendents preexistents, no relacionats amb
  aquesta ronda) + el nou `00_Quadern_sessions_docent.pdf` (35 pàgines).
- pytest de `web/_generador/tests/`.

## 3. Pendents d'aula (no verificables des del repositori)

- **Temps real del checklist docent com a eina de preparació (~20 min/SA)**:
  l'estimació d'U5 és una hipòtesi raonable a partir de la longitud del document,
  no una mesura; cal cronometrar-la les primeres SA del curs.
- **Ús real del `00_Quadern_sessions_docent.pdf`**: cal validar a l'aula que el
  format d'una pàgina per sessió és prou compacte per portar-lo a taula sense
  haver de tornar a obrir els documents font (l'objectiu original d'U3).
- **Itinerari «Vaig faltar»**: cal observar amb el primer alumne que el faci
  servir si els 5 passos són suficients sense acompanyament del docent, o si cal
  afegir-hi un pas de verificació (p. ex. una pregunta ràpida a la sessió
  següent) perquè no es converteixi en una via per acumular llacunes sense
  detectar-les.

---

*Memòria interna de desenvolupament. Llicència CC BY-SA 4.0.*
