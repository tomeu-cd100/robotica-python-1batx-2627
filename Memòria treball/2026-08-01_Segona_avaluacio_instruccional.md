# Segona avaluació instruccional — verificació post-millores i recorregut d'ulls nous

> Segona auditoria (01/08/2026), després d'aplicar el pla P1-P4. Dues anàlisis
> independents: (1) re-auditoria crítica de corba/exercicis/avaluació sobre el material
> real, (2) recorregut d'ulls nous (docent que no coneix el curs + alumne de 16 anys).

## Dictamen global

**Els 5 forats de contingut de la primera auditoria estan tancats amb qualitat alta**
(return, global, for, try/except, percep/decideix/actua — traçabilitat exemplar entre
fitxa, codi, EXPLICACIO, kata i prova). El pes **blindat** d'escriptura autònoma de codi
a la nota passa de ~5-8 % a **~15-17 %** (total codi ≈ 33-35 %). El pic de S28 baixa de
6 conceptes a ~3.

**El problema nou és l'aritmètica del temps d'aula**: les millores afegeixen ~25-30' de
rituals i producció per sessió de producte (kata 10' + repte ⭐ 15' + parella 5' + mini-
defensa) sobre taules que sumen 120' quan el temps efectiu real declarat és ~100'. La
primera víctima seria justament el repte ⭐ — la peça central de P1 — que migraria a
deures amb maquinari. I el recorregut d'ulls nous ha trobat **una referència trencada
greu**: el circuit de reforç 🔴 dels mini-checks deriva a `SA0/SA0_guia_programacio.md`,
que **no existeix** (text pla, invisible per al QA).

## Troballes principals

### Re-auditoria (severitat alta)
- **N1 — Dèficit de 20' a totes les sessions amb repte ⭐**: taules de 120' vs ~100'
  efectius; cap retallada prevista allibera el temps sense tocar nucli.
- **N2 — Repte ⭐ infradimensionat**: 15' bruts (~10' nets amb la parella de lectura
  dins) per a reptes estimats en 25-45' per a un novell (SA4 25-40', SA6 30-45',
  SA8 20-30'); la validació individual de 20 alumnes no cap a la franja.

### Re-auditoria (severitat mitjana)
- **N3** — Qüestionaris amb estatus indefinit («qualificable» sense dimensió ni franja).
- **N4** — Contradicció interna: `00_Mini_checks_individuals.md:12` diu que el mini-check
  SEMPRE substitueix l'activació; la capçalera i el banc diuen que a SA2-SA5 conviuen.
- **N6** — Progressió de katas truncada: cap concepte post-SA4 (return, try/except,
  for-col·lecció, FSM, ràdio, llistes) arriba mai al nivell «escriure de zero» al banc.
- **N7** — «Repte a full en blanc SA7-SA8» declarat a `04_Metodologia.md:37` però no
  materialitzat (tots els reptes parteixen d'un .py).
- Buits sense instrument: llegir un traceback real; «aquest programa falla: arregla'l»
  com a ítem puntuat; CA1.2 (REPL) segueix sense ítem etiquetat.
- Escletxa residual: un «adaptador hàbil» pot treure ≈ 6,6 sense escriure codi si la
  mini-entrevista de R1 s'aplica amb màniga ampla; no hi ha porta mínima de programació.

### Recorregut d'ulls nous (impacte alt)
- **U1 — Referència trencada al circuit de rescat**: les 9 files de reforç 🔴 dels
  mini-checks apunten a `SA0_guia_programacio.md` (seccions A1-A9 citades amb nom), que
  no existeix.
- **U2 — El repte ⭐ de SA2 (nucli, qualifica R1) no té bastida «Si t'encalles» pròpia**
  (el producte de la mateixa SA sí que en té); auditar la resta de ⭐.
- **U3 — Gestió del dia complet = 5 pestanyes** (guia + banc de katas + mini-checks +
  reptes + checklist): cal un full de sessió imprimible que ho combini.

### Recorregut (impacte mitjà/baix)
- **U4** — No hi ha itinerari «Vaig faltar a classe» per recuperar sol.
- **U5** — `GUIA_INICI_DOCENT.md` sense estimació del temps de preparació del docent.
- **U6** — El «pont cap a la SA2» (primer shield) només és a la guia docent, no a la
  fitxa de l'alumne. Text fòssil de la «graella d'activació» antiga a
  `04_Metodologia.md:20` i `00_Avaluacio_per_alumnat.md:43` (N5). El ⭐ no surt a la
  taula d'avaluació per a l'alumnat (N9). Kata K16 duplica el mini-check de SA4.

## Què funciona molt bé (no tocar)
Rutina DEPURA i mètode de projecte constants; taules d'errors freqüents i guions de
modelatge a les guies (or per a un docent nou de MicroPython); banc de katas amb regla
de repàs espaiat; mapa de pins únic amb els «per què NO aquest pin»; marges horaris
honestos; esquelets `# TODO` on existeixen.

## Pla de tercera ronda recomanat (prioritzat)

1. **Requadrar les 6-7 sessions amb ⭐ a 100' reals**: Explicació 20'→10' (el PRIMM
   d'activació ja fa mitja feina), repte ⭐ 15'→25-30', mini-defensa per MOSTREIG
   rotatiu (5-6 alumnes/sessió), una sola parella de lectura per sessió.
2. **Crear `Classes/SA0/SA0_guia_programacio.md`** amb les seccions A1-A9 que els
   mini-checks ja citen — desbloqueja el reforç 🔴 de les 9 SA (U1).
3. **Porta mínima de programació al trimestre** (1 paràgraf a §6.3): mínim 1 mini-check
   ≥ 🟡 o ítem de funció nova ≥ 1/2 per aprovar el trimestre.
4. **Bastides «Si t'encalles» per als reptes ⭐** de totes les SA, enllaçades des de
   Reptes_SAn.md (U2), i 6-8 katas noves de nivell buits/zero per a return, try/except,
   for-col·lecció i FSM a S29-S33 (N6).
5. **Full de sessió imprimible** (kata + mini-check + ⭐ + checklist del dia en un full,
   generat dels documents existents) (U3) + neteja de coherència (N3, N4, N5, N7, N9,
   U4, U5, U6, K16).

*Auditoria interna. Llicència CC BY-SA 4.0.*
