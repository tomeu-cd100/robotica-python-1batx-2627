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
| `crear_estructura_curs.js` | Crea els temes (SA0-SA9 + general) i un material-enllaç per tema cap a les pàgines de l'alumnat del web publicat. Accepta `--simula`. |

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
