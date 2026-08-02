# Material Classroom — automatització del Google Classroom del curs

Scripts Node (ESM + `googleapis`) que creen l'estructura, els materials i els
formularis del Classroom **Robòtica amb Python - 1r Batx - Curs 2627**
(`871507273731`, [enllaç](https://classroom.google.com/c/ODcxNTA3MjczNzMx)) a
partir del material versionat d'aquest repositori.

## Secrets: no són aquí, i no s'hi han de copiar

Aquesta carpeta **no conté** `credentials.json` ni `token.json`. Les credencials
OAuth viuen només a `Material Classroom/` del curs germà (Robòtica amb Arduino);
els scripts d'aquí les llegeixen d'allà mitjançant la variable d'entorn
`CLASSROOM_SECRETS_DIR`:

```powershell
cd "Material Classroom"
$env:CLASSROOM_SECRETS_DIR = "C:\Users\briera2\Documents\Curs 2627 1 Batx Robotica\Material Classroom"
node estat_classroom.js
```

Si el token caduca, el flux OAuth s'ha de fer amb el compte del centre, al
navegador, i el token es regenera **a la carpeta dels secrets**, no aquí.

## Peces

| Fitxer | Rol |
|---|---|
| `config.js` | Font única d'ids: `COURSE_ID`, `DRIVE_FOLDER_ID`, `GRADE_CATEGORIES` (T1/T2/T3), `WEB_ROOT`/`WEB_BASE`, `SA_TRIMESTRE`. Canviar de curs = tocar només això. |
| `_form_sa_lib.js` | Helpers de Forms (`t()`, `p()`, `radio()`, `autoaval()`…), `getAuthClient()` amb secrets externs, reintents amb backoff (429/5xx) i `crearIPenjar()` amb deduplicació per títol i neteja del Form orfe si falla a mig fer. |
| `estat_classroom.js` | **Només lectura.** Llista categories de nota (amb els ids per a `config.js`), temes i tasques reals del curs → `estat_classroom.json`. |
| `preparar_drive.js` | Crea (o troba) la carpeta de Drive del curs on van tots els Forms. `APPLY=1` per crear-la. |
| `crear_estructura_curs.js` | Crea els temes (SA0-SA9 + general) i un material-enllaç per tema cap a les pàgines de l'alumnat del web publicat. Accepta `--simula`. |
| `crear_questionaris_conceptes_forms.js` | Un Google Form autocorrectiu per SA: parseja les preguntes de `Classes/SAn/SAn_questionari_conceptes.md` i les claus de `Classes/Solucionari/Questionaris_conceptes_solucions.md`. `APPLY=1` per crear; `SA=3` per limitar-ho a una SA. |
| `adjuntar_questionaris_classroom.js` | Penja aquells Forms com a tasca **sense nota** (formativa) al tema de la seva SA. |
| `crear_tasques_lliurament.js` | Tasca de lliurament del producte per SA (10 punts, categoria T1/T2/T3, enllaços a fitxa/checklist/reptes). |
| `crear_rubriques_per_tasca.js` | Les **sis rúbriques unificades (A-F)** i el mapa tasca → rúbrica. Escriu els CSV versionats a `Avaluació/rubriques/`, els puja a Drive com a fulls importables i crea el material «Quina rúbrica avalua cada tasca». És la font de dades del mapa. |
| `generar_mapa_rubriques_md.js` | Genera `Classes/00_General/00_Mapa_tasques_rubriques.md` a partir d'aquelles mateixes dades (el document no s'edita a mà). |
| `crear_quadern_classroom.js` | Material amb les plantilles del quadern tècnic (les del web, no de GitHub) i una tasca de lliurament del quadern sencer per trimestre (10 punts, categoria T1/T2/T3). |

## Estat del curs (02/08/2026)

Creat: 11 temes · 16 materials-enllaç · 9 qüestionaris (Forms autocorrectius +
tasca sense nota) · 9 tasques de lliurament de producte + 3 de quadern tècnic
(10 punts) · 6 fulls de rúbrica a Drive i el material amb el mapa tasca →
rúbrica. **Tot en esborrany**, pendent que el docent ho publiqui i hi posi dates.

Pendent manual (dues coses que l'API no deixa fer):

1. **Rúbrica**: a cada tasca amb nota, *Rúbrica → Importar des de Sheets* → el
   full que digui `Classes/00_General/00_Mapa_tasques_rubriques.md` (A-F).
   L'API de rúbriques demana Education Plus / Teaching & Learning Upgrade, que
   aquest compte no té.
2. **Categoria de nota** (T1/T2/T3): s'ha d'assignar a mà al desplegable de cada
   tasca. L'API accepta el camp `gradeCategory` a la creació però **no l'aplica**,
   i el `patch` amb `updateMask=gradeCategory` el rebutja («Non-supported update
   mask fields»). Els scripts ho comproven després de crear i llisten les tasques
   pendents. El curs té `calculationType: TOTAL_POINTS`, així que la nota global
   surt igualment; les categories només serveixen per agrupar per trimestre.

`node_modules/`, `estat_classroom.json` i els `resultats_*.json` són locals i
estan ignorats per git; els scripts es versionen per excepció al `.gitignore`
de l'arrel del repositori (si n'afegeixes un de nou, afegeix-hi també la línia
`!Material Classroom/<script>.js`, o no existirà en un clone).

## Regles de treball

1. **Simula primer**: els scripts que creen contingut accepten `--simula`.
2. **Tot neix en esborrany** (`DRAFT`): la publicació la decideix el docent des
   del Classroom.
3. **Idempotència**: temes per nom i tasques/materials per títol; re-executar un
   script no duplica res.
4. **Res de dades d'alumnat**: els àmbits OAuth no inclouen `rosters` ni
   `profile.emails`; aquests scripts publiquen material, no llegeixen la classe.
5. **Enllaços al web publicat**: la font de veritat del contingut és aquest
   repositori (GitHub Pages), no una còpia dins de Classroom.
