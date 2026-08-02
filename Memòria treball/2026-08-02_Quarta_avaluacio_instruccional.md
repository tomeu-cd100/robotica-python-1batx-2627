# Quarta avaluació instruccional — auditoria panoràmica post-tercera ronda

> Quarta auditoria (02/08/2026), després d'aplicar el pla de la tercera ronda. Quatre
> anàlisis independents i paral·leles: (1) temps d'aula i sistema d'avaluació, (2) corba
> d'aprenentatge i exercicis SA1-SA5, (3) SA6-SA9, projectes trimestrals i tancament,
> (4) recorregut d'ulls nous (docent que hereta el curs + alumne de 16 anys). Les
> troballes de severitat alta s'han verificat manualment sobre el material abans
> d'incloure-les.

## Dictamen global

**L'esquelet del curs és sòlid i les tres rondes anteriors han aguantat la re-auditoria**:
hores i sessions quadren exactament (34 sessions, 68+2 h), les 8 sessions amb repte ⭐
sumen 100'+20' amb fila pròpia de 25', els percentatges d'avaluació i la porta mínima són
coherents entre els documents del docent i de l'alumnat, el mapa de pins es respecta a
tots els nivells de SA1 a T3, i cap concepte s'exigeix abans d'haver-se treballat.

**Els problemes que queden són d'una altra família**: (1) **dos errors funcionals de
maquinari/ràdio** que farien fallar el material a l'aula (la telemetria de SA8 peta a cada
enviament pel límit de 32 bytes de `radio.send()`; dos reptes de SA9 proposen pins
inexistents o no-ADC); (2) **la classificació de la vista alumnat/docent deixa fora
documents que els itineraris d'alumnat necessiten** (el circuit «Vaig faltar» i el de
rescat topen amb la porta amb contrasenya); i (3) **aritmètica del mostreig de
mini-defenses**: la garantia «tothom passa un cop per trimestre» és impossible al T1 amb
les places actuals.

## Troballes principals

### Severitat alta (farien fallar el material a l'aula)

- **A1 — Telemetria SA8 trencada**: `telemetria_radio.py:243-249` construeix missatges
  `TEL:D:…;S:…;E:…;T:…;H:…;O:…` de 37-48 caràcters, però `radio.config()` (línia 29) no
  fixa `length` i el límit per defecte és 32 bytes → `ValueError` a cada `radio.send()`.
  Cal `length=64` a emissor i `estacio_base.py`, i explicar-ho com a concepte de protocol.
- **A2 — Pins impossibles als reptes SA9**: `SA9_reptes_proposats.md:70` proposa NeoPixel
  a **P17** (no existeix com a GPIO) i `:87` sensor de so a **P11** (botó B, no ADC).
  Reptes 1 i 3 (P4/P10 + display) reprodueixen el conflicte `Pin in display mode` que el
  fil conductor mana evitar.
- **A3 — Repte ⭐ de SA5 buit de feina**: demana `mostra_historial()` quan la funció ja
  existeix resolta (`mostra_historic()`) al fitxer de partida i és l'activitat nucli de la
  S1: el repte nucli es valida copiant. Canviar el requisit (filtrar per remitent, comptar
  per emissor…).
- **A4 — Garantia de mini-defensa impossible al T1**: 2 sessions amb mostreig × 5-6
  alumnes = 10-12 places per a grups de 15-20 (`00_Guia_defensa_oral.md:39`); al T2 va
  justíssim. Ampliar el mostreig del T1 (8-10/sessió) o rebaixar la garantia declarada.
- **A5 — Itineraris d'alumnat que topen amb la contrasenya**: «Vaig faltar» (passos 3-4)
  envia a `00_Banc_activacio_repas.md` i `00_Mini_checks_individuals.md` (docent);
  `00_Entorns_de_treball.md` (com transferir el primer `.hex`) i el semàfor d'IA de
  `00_IA_a_la_materia.md` §5 (que afecta la nota) tampoc són a `GENERAL_ALUMNAT`.
  Reclassificar o extreure versions d'alumnat.

### Severitat mitjana

- **M1 — Mini-defenses SA3/SA7 contradictòries**: l'escala de `00_Guia_defensa_oral.md`
  les declara formatives; els mapes d'avaluació de les guies docents les marquen
  qualificades (R4). La taula de progressió omet SA5 i SA8 (que sí qualifiquen). El §
  mostreig diu «SA1-SA8» quan SA1 no en té.
- **M2 — Mini-check SA1 fora de taula**: viu en una nota, la S3 real queda a 110'/100'.
  Única SA sense fila pròpia.
- **M3 — Buits residuals de la 2a auditoria encara oberts**: cap ítem etiquetat CA1.2
  (l'ítem REPL de la T1 està etiquetat CA1.1 — reetiquetar-lo els tanca tots dos), i cap
  ítem puntuat «aquest programa falla: arregla'l» amb traceback imprès a cap prova.
- **M4 — Escriptura de zero escassa a T2**: entre S12 i S29 cap kata «escriure de zero»;
  els productes de SA4-S3/SA5-S3 parteixen del fitxer resolt sense banner «✋ SOLUCIÓ».
- **M5 — Referències a material futur o incorrecte**: bastida SA4 cita `mostra_fletxa()`
  (kata de S17, posterior); `SA6_esquemes_connexions.md:36` diu que `termometre.py` usava
  P10 (era P1); K23/K25 citen programes o comportaments equivocats.
- **M6 — Descobribilitat del material d'ajuda**: `00_Targetes_rescat.md` és orfe (cap
  fitxa ni el LLEGEIX-ME l'enllacen); la plantilla del quadern tècnic (PDFs T1-T3) no
  s'enllaça des de cap `.md`; el rescat SA9 apunta a una rutina DEPURA que
  `00_Mode_supervivencia.md` no conté.
- **M7 — Aritmètica de defenses SA9**: amb 20 alumnes, ~8-10 queden sense franja entre
  S3 i S4. Fer explícit començar a la S2 o buidar Pràctica de S4.
- **M8 — Solució model de la prova T3 sense `try/except OSError`** a
  `mesura_distancia()`: el patró de robustesa que el curs ensenya falta justament al
  codi del docent per a la correcció a pista.
- **M9 — Fitxa SA3 contradiu l'EXPLICACIO** sobre si el producte s'escriu (esquelet del
  dossier) o s'adapta (`mascota_reactiva.py` resolt); fitxa SA5-S2 atribueix a
  `comandament.py` la connexió recepció→moviment que és de la S3.

### Severitat baixa (neteja)

- **B1** — Bastides ⭐ de SA1/SA3: el Nivell 3 regala gairebé la solució (deixar `# TODO`
  de línia sencera).
- **B2** — Targetes noves de repàs: R6/R7 de la de MicroPython sense mapatge a secció
  A#; `avancar(400)` sense definir a la solució R3 de la de ràdio i a l'exemple B de
  `SA0_guia_programacio.md` (peta al simulador amb `NameError`); ordre `config()`/`on()`
  de la guia no coincideix amb el codi de SA5.
- **B3** — Caràcters no ASCII en comentaris `.py`: ela geminada a `registre_dades.py:12`,
  «·» a `mascota_reactiva.py:6-7`.
- **B4** — SA8-S2 suma 110' (única taula que no quadra); títols de targetes de rescat
  SA5/SA8 no coincideixen amb els noms oficials de les SA; tres noms per a la secció
  d'errors del quadern; peu de `SA9_dossier_plantilla.md` diu R3/R5 en lloc de R4;
  nom de l'ítem de porta mínima no literal amb la T3; ampliació notable de Reptes_SA1
  demana `while` comptat abans d'estrenar variables; «cap activitat en parelles» de
  `GUIA_INICI_DOCENT.md` sense matisar l'excepció de la parella de lectura.

## Què funciona molt bé (no tocar)

Quadre d'hores i sessions exactes; requadrat 100'+20' aplicat amb coherència a les 8
guies; percentatges i porta mínima idèntics entre docent i alumnat; mapa de pins
respectat de SA1 al rover T3 (amb les notes didàctiques de conversió); protocol de ràdio
coherent de cap a cap (`CMD:`/`TEL:`, mateix patró `startswith`); proves T1-T3 alineades
amb allò practicat i amb l'ítem de codi mai vist promès; bastida SA9 completa sense
regalar res; katas amb regla d'or respectada (llevat de K04); to «tu» consistent i
targetes de repàs genuïnament autocomprovables.

## Pla de quarta ronda recomanat (prioritzat)

1. **Arreglar el que peta**: `length=64` a la ràdio de SA8 (emissor + estació base +
   nota de protocol), pins reals als reptes SA9 (P17→P8/P12, P11→micròfon intern,
   `display.off()` on calgui), `try/except OSError` a la solució T3, repte ⭐ SA5 nou.
2. **Reclassificar la vista alumnat**: `00_Entorns_de_treball.md` a `GENERAL_ALUMNAT`;
   enunciats de katas/mini-checks (sense solucions) accessibles a l'alumnat o itinerari
   «Vaig faltar» reescrit; semàfor d'IA visible a l'alumnat.
3. **Reparar l'aritmètica del mostreig**: places de mini-defensa T1 i defenses SA9;
   alinear formativa/qualificada (SA3/SA7) i completar l'escala (SA5/SA8); fila de
   mini-check a la taula de SA1.
4. **Tancar els buits residuals d'avaluació**: reetiquetar l'ítem REPL com a CA1.2 i
   afegir un ítem puntuat de depuració amb traceback a T2 o T3.
5. **Neteja de coherència** (M4-M9 i B1-B4): banners «✋ SOLUCIÓ» a T2, una kata
   d'escriure de zero entre S14-S18, enllaços a targetes de rescat i plantilla del
   quadern, referències creuades errònies, comentaris ASCII, i les micro-esmenes B4.

*Auditoria interna. Llicència CC BY-SA 4.0.*
