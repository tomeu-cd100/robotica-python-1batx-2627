# Quarta ronda de millores — execució

> Execució (02/08/2026) del pla de la quarta auditoria
> (`2026-08-02_Quarta_avaluacio_instruccional.md`, pla a
> `docs/superpowers/plans/2026-08-02-quarta-ronda-millores.md`), més una petició
> nova del docent: **solució de cada kata al banc del docent** per poder
> comentar-la amb l'alumnat.

## 1. Què s'ha fet (per task, un commit per bloc)

- **Arreglos funcionals** (`fix(SA5,SA8,SA9,T3)`): `length=64` al `radio.config()`
  de la telemetria SA8 (emissor, estació base i exemple resolt; el paquet `TEL:`
  supera els 32 bytes per defecte) amb nota de protocol a l'EXPLICACIO; pins
  reals als reptes proposats de SA9 (P17→P8/P12, P11→micròfon intern, avisos del
  conflicte display); `try/except OSError` a la solució model de la prova T3;
  repte ⭐ de SA5 nou (`compta_missatges(remitent)` amb `for`+`startswith`+`return`)
  amb bastida i solucionari — l'anterior es resolia copiant una funció donada.
- **Vista alumnat** (`fix(web,alumnat)`): `00_Entorns_de_treball.md` a
  `GENERAL_ALUMNAT`; semàfor d'IA copiat a `00_Avaluacio_per_alumnat.md` §7;
  «Vaig faltar» reescrit perquè cap pas depengui de documents del docent;
  plantilles del quadern (PDF T1-T3) enllaçades.
- **Avaluació i temps** (`fix(avaluacio)`): mostreig del T1 a 8-10 alumnes/sessió
  (la garantia «un cop per trimestre» era impossible amb 5-6); escala de defensa
  completa (files SA5/SA8) i SA3/SA7 alineades com a formatives (manava l'escala);
  fila pròpia de mini-check a SA1-S3 (PRIMM comprimit, sessió a 100'+20');
  aritmètica de defenses SA9 explícita; SA8-S2 quadrada; nom literal de l'ítem T3
  a la porta mínima; ítem REPL de T1 reetiquetat **CA1.2**; **ítem obligatori de
  depuració amb traceback real a la T2** (1 punt: llegir, explicar la causa,
  arreglar la línia; barem inclòs).
- **Katas amb solució** (`feat(katas)`): les 27 kates del banc duen solució
  desplegable «✅ Solució (per comentar amb l'alumnat)» amb codi complet i l'error
  típic; intercanvi K04↔K19 (regla d'or); K21 convertida a «escriure de zero»
  (buit d'escriptura autònoma del T2); cites K23/K25 corregides. El parser del
  quadern de sessions talla a `**Soluci` i no arrossega les solucions (verificat).
- **Neteja** (`fix(coherencia)`): bastides SA1/SA3 sense regalar el nivell 3;
  referències creuades corregides (Reptes_SA4, SA6_esquemes P1/P10); fitxes
  SA3/SA5 amb el missatge «escriu primer, el resolt és referència» (+ banner
  SOLUCIÓ a `receptor_vehicle`); circuit de rescat descobrible (LLEGEIX-ME +
  9 checklists + títols + rescat SA9 al quadern); ordre canònic
  `radio.on()`→`config()` a guia SA0 i targetes; exemples autoexecutables al
  simulador; comentaris 100% ASCII; dossier SA9 → R4; matís de la parella de
  lectura a `GUIA_INICI_DOCENT.md`.

## 2. Verificacions

- `tools/qa.py` = 0 problemes (només els 2 avisos pii permesos del test) després
  de cada commit; `generar.py` net; pytest 55/55.
- PDFs regenerats i sincronitzats: 9 checklists d'alumnat, 2 targetes de repàs,
  `00_Quadern_sessions_docent.pdf` (recull el nou mapa S8/S9 i el nou enunciat de
  K21); la resta restaurats sense canvi.
- Troballes ALTES de l'auditoria verificades sobre el material abans d'arreglar
  (mida real del paquet `TEL:`, duplicitat del ⭐ SA5, pins SA9).

## 3. Pendents d'aula (no verificables des del repositori)

- Comprovar a l'aula que el mostreig de 8-10 defenses d'1' cap realment a la
  franja de tancament del T1.
- El dia S9 (SA3-S2) acumula mini-check + kata K04 «escriure de zero»: càrrega
  d'escriptura doble; si es fa pesat, K04 pot passar a «completar buits» aquell
  dia.
- Validar amb alumnat real que les solucions desplegables del banc no es
  projecten mai abans de fer la kata (són per al docent).

*Memòria interna. Llicència CC BY-SA 4.0.*
