// Configuració ÚNICA del curs per a tots els scripts de Material Classroom.
// EN CANVIAR DE CURS (setembre): actualitzar aquí i enlloc més.
//  - COURSE_ID: id numèric del curs (courses.list o la URL de l'API, NO la
//    forma base64 de la URL /c/... del web). El d'aquest curs surt de
//    https://classroom.google.com/c/ODcxNTA3MjczNzMx (base64 → 871507273731).
//  - DRIVE_FOLDER_ID: carpeta de Drive on van tots els Forms del curs.
//  - GRADE_CATEGORIES: ids de les categories de nota (T1/T2/T3). ⚠️ Es
//    regeneren amb cada curs nou de Classroom: obtenir-los amb
//    `node estat_classroom.js` abans d'executar cap script que hi assigni
//    categoria.
//  - WEB_BASE: arrel del web publicat (GitHub Pages d'aquest repositori).
//
// SECRETS: aquest repositori NO conté `credentials.json` ni `token.json`.
// Viuen només a `Material Classroom/` del curs germà (Robòtica amb Arduino) i
// s'hi accedeix amb la variable d'entorn CLASSROOM_SECRETS_DIR — vegeu
// `_form_sa_lib.js` i el README d'aquesta carpeta.

export const COURSE_ID = '871507273731';

// Carpeta de Drive del curs: encara no fixada (els Forms nous hi aniran).
// Mentre sigui null, els scripts que mouen fitxers a Drive han d'avisar i
// aturar-se en lloc de deixar els Forms escampats per l'arrel del Drive.
export const DRIVE_FOLDER_ID = null;

export const WEB_ROOT = 'https://tomeu-cd100.github.io/robotica-python-1batx-2627';
// WEB_BASE apunta a la secció «classes» (compatibilitat amb el patró del curs
// germà, on tots els enllaços de material hi pengen).
export const WEB_BASE = `${WEB_ROOT}/classes`;

// Categories de nota del curs, llegides amb `node estat_classroom.js`
// (02/08/2026, curs «Robòtica amb Python - 1r Batx - Curs 2627»).
export const GRADE_CATEGORIES = {
  T1: { id: '819894652016', name: 'T1' },
  T2: { id: '819894652017', name: 'T2' },
  T3: { id: '819894652018', name: 'T3' },
};

// SA -> trimestre (per assignar categoria de nota).
// SA0 és acollida (dins la S1 de SA1): compta com a T1.
export const SA_TRIMESTRE = { 0: 'T1', 1: 'T1', 2: 'T1', 3: 'T1',
                              4: 'T2', 5: 'T2', 6: 'T2',
                              7: 'T3', 8: 'T3', 9: 'T3' };
