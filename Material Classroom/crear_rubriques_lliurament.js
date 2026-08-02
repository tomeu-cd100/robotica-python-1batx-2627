/*
 * Rúbrica de correcció de les tasques de lliurament del producte (SA1-SA9).
 *
 * La rúbrica és la mateixa per a totes les SA i deriva de
 * `Programació didàctica/07_Rubriques.md`: 5 criteris × 2 punts = 10 punts, que
 * és el maxPoints de les tasques de lliurament. Els criteris trien els trossos
 * de R1/R3/R4/R5 que apliquen a un producte de SA, amb el subcriteri «codi
 * escrit per l'alumne mateix» com a criteri propi (P3.11: ha de pesar de debò).
 *
 * Dues sortides:
 *  1. Rúbrica NATIVA al Classroom, via l'API REST de rubrics (la llibreria
 *     googleapis instal·lada encara no l'exposa, així que es crida amb fetch).
 *  2. CSV importable (`Avaluació/rubriques/Rubrica_producte_SA.csv`) com a
 *     alternativa manual i com a còpia versionada i llegible de la rúbrica.
 *
 * Idempotent: si una tasca ja té rúbrica, no en crea una segona.
 *
 * Ús (amb CLASSROOM_SECRETS_DIR definit):
 *   node crear_rubriques_lliurament.js           # escriu el CSV i fa descoberta
 *   APPLY=1 node crear_rubriques_lliurament.js   # a més, crea les rúbriques
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { google } from 'googleapis';
import { getAuthClient, ambReintents } from './_form_sa_lib.js';
import { COURSE_ID, DRIVE_FOLDER_ID } from './config.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const APPLY = process.env.APPLY === '1';
const FONT = 'resultats_tasques_lliurament.json';
const CSV_SORTIDA = path.join(__dirname, '..', 'Avaluació', 'rubriques', 'Rubrica_producte_SA.csv');

// 5 criteris × 2 punts = 10. Nivells alineats amb les bandes de 07_Rubriques.md
// (Insuficient 0-4 · Suficient/Bé 5-6 · Notable 7-8 · Excel·lent 9-10).
const CRITERIS = [
  {
    title: 'Funcionament (R1)',
    description: 'El producte fa el que ha de fer amb el maquinari real.',
    levels: [
      { title: 'Insuficient', points: 0, description: 'No s\'executa o no fa la tasca.' },
      { title: 'Suficient/Bé', points: 1, description: 'Fa la tasca bàsica amb errors menors.' },
      { title: 'Notable', points: 1.5, description: 'Fa la tasca completa de manera fiable.' },
      { title: 'Excel·lent', points: 2, description: 'Funciona i gestiona casos límit o errors.' },
    ],
  },
  {
    title: 'Codi escrit per tu (R1, mínim 40 % de R1)',
    description: 'Estructures i decisions pròpies, no una còpia adaptada de l\'exemple. '
      + 'Es comprova amb dues preguntes sobre el codi lliurat.',
    levels: [
      { title: 'Insuficient', points: 0, description: 'Còpia gairebé literal del codi de base, sense adaptar.' },
      { title: 'Suficient/Bé', points: 1, description: 'Adapta la base amb canvis mínims (noms, valors).' },
      { title: 'Notable', points: 1.5, description: 'Estructures pròpies i adaptacions no trivials.' },
      { title: 'Excel·lent', points: 2, description: 'Disseny propi identificable, amb decisions justificades.' },
    ],
  },
  {
    title: 'Llegibilitat i depuració (R1)',
    description: 'Comentaris, noms significatius i capacitat d\'explicar els errors resolts.',
    levels: [
      { title: 'Insuficient', points: 0, description: 'Sense comentaris ni noms clars; no identifica errors.' },
      { title: 'Suficient/Bé', points: 1, description: 'Comentaris escassos; corregeix amb ajuda.' },
      { title: 'Notable', points: 1.5, description: 'Comentat, noms significatius, depura sol.' },
      { title: 'Excel·lent', points: 2, description: 'Documentat amb cura i explica la causa de l\'error.' },
    ],
  },
  {
    title: 'Projecte i integració (R3)',
    description: 'Compliment del repte (inclòs el repte ⭐ obligatori) i integració amb el que ja tenies muntat.',
    levels: [
      { title: 'Insuficient', points: 0, description: 'No assoleix els objectius; parts inconnexes.' },
      { title: 'Suficient/Bé', points: 1, description: 'Assoleix els mínims; integració parcial.' },
      { title: 'Notable', points: 1.5, description: 'Assoleix tots els objectius; sistema coherent.' },
      { title: 'Excel·lent', points: 2, description: 'Supera els objectius amb millores; integració robusta.' },
    ],
  },
  {
    title: 'Quadern tècnic i comunicació (R4)',
    description: 'Entrada de la SA al quadern: predicció, procés, error documentat amb DEPURA i millora; '
      + 'defensa de la decisió tècnica si et toca mini-defensa.',
    levels: [
      { title: 'Insuficient', points: 0, description: 'Incomplet o confús.' },
      { title: 'Suficient/Bé', points: 1, description: 'Bàsic, comprensible amb llacunes.' },
      { title: 'Notable', points: 1.5, description: 'Complet, ordenat i clar.' },
      { title: 'Excel·lent', points: 2, description: 'Exhaustiu i reflexiu, amb terminologia precisa.' },
    ],
  },
];

function escriuCSV() {
  const esc = (s) => `"${String(s).replace(/"/g, '""')}"`;
  const files = [['Criterion Title', 'Criterion Description', 'Level Title', 'Level Description', 'Points']];
  for (const c of CRITERIS) {
    for (const l of c.levels) {
      files.push([c.title, c.description, l.title, l.description, l.points]);
    }
  }
  fs.mkdirSync(path.dirname(CSV_SORTIDA), { recursive: true });
  fs.writeFileSync(CSV_SORTIDA, files.map(f => f.map(esc).join(',')).join('\n') + '\n', 'utf8');
  console.log(`💾 CSV importable escrit a Avaluació/rubriques/${path.basename(CSV_SORTIDA)}`);
}

async function api(auth, metode, url, cos) {
  const { token } = await auth.getAccessToken();
  const res = await fetch(url, {
    method: metode,
    headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: cos ? JSON.stringify(cos) : undefined,
  });
  const dades = await res.json().catch(() => ({}));
  if (!res.ok) {
    const err = new Error(dades?.error?.message || `HTTP ${res.status}`);
    err.estat = res.status;
    err.dades = dades;
    throw err;
  }
  return dades;
}

/*
 * L'API de rúbriques només és per a comptes amb Education Plus / Teaching &
 * Learning Upgrade. Sense aquesta llicència, el camí que sí que funciona és
 * importar la rúbrica des d'un full de càlcul: aquí es puja el CSV convertit a
 * Google Sheets, a la carpeta del curs, perquè el docent només hagi de triar-lo
 * a «Rúbrica → Importar des de Sheets» a cada tasca.
 */
const NOM_FULL = 'Rúbrica de producte de SA (importable a Classroom)';

async function pujaFullRubrica(auth) {
  const drive = google.drive({ version: 'v3', auth });
  const existents = await ambReintents(
    () => drive.files.list({
      q: `name = '${NOM_FULL.replace(/'/g, "\\'")}' and '${DRIVE_FOLDER_ID}' in parents and trashed = false`,
      fields: 'files(id, name, webViewLink)',
    }), 'buscar el full de la rúbrica');
  const trobat = (existents.data.files || [])[0];
  if (trobat) {
    console.log(`\n↷ El full de la rúbrica ja és a Drive:\n   ${trobat.webViewLink}`);
    return trobat;
  }
  const creat = await ambReintents(
    () => drive.files.create({
      requestBody: {
        name: NOM_FULL,
        mimeType: 'application/vnd.google-apps.spreadsheet',   // conversió CSV → Sheets
        parents: [DRIVE_FOLDER_ID],
      },
      media: { mimeType: 'text/csv', body: fs.createReadStream(CSV_SORTIDA) },
      fields: 'id, name, webViewLink',
    }), 'pujar el full de la rúbrica');
  console.log(`\n✅ Full de la rúbrica pujat a Drive:\n   ${creat.data.webViewLink}`);
  return creat.data;
}

async function main() {
  escriuCSV();

  if (!fs.existsSync(FONT)) {
    console.log(`\n⚠ Falta ${FONT}: executa abans APPLY=1 node crear_tasques_lliurament.js`);
    return;
  }
  const { creades } = JSON.parse(fs.readFileSync(FONT, 'utf8'));
  const auth = await getAuthClient();

  console.log(`\n=== Rúbriques de les ${creades.length} tasques de lliurament ===`);
  let viaAPI = true;
  for (const t of creades) {
    const base = `https://classroom.googleapis.com/v1/courses/${COURSE_ID}/courseWork/${t.id}/rubrics`;
    try {
      const existents = await api(auth, 'GET', base);
      if ((existents.rubrics || []).length) {
        console.log(`  ↷ ${t.sa}: ja té rúbrica`);
        continue;
      }
      if (!APPLY) {
        console.log(`  · [descoberta] ${t.sa}: crearia la rúbrica (5 criteris, 10 punts)`);
        continue;
      }
      await api(auth, 'POST', base, { criteria: CRITERIS });
      console.log(`  ✅ ${t.sa}: rúbrica creada (5 criteris, 10 punts)`);
    } catch (e) {
      console.log(`  ❌ ${t.sa}: ${e.message}`);
      // Sense llicència Education Plus, l'API de rúbriques no és utilitzable:
      // no té sentit provar-ho tasca per tasca, es passa al camí del full.
      if (e.estat === 403 || e.estat === 401 ||
          /IneligibleToModifyRubrics|eligibility/i.test(e.message)) {
        console.log('     → aquest compte no pot crear rúbriques per API; es prepara el full importable.');
        viaAPI = false;
        break;
      }
    }
  }

  if (!viaAPI) {
    if (!APPLY) {
      console.log('\n🔎 Mode descoberta: amb APPLY=1 es pujaria el full importable a Drive.');
      return;
    }
    await pujaFullRubrica(auth);
    console.log('\n👉 A cada tasca de lliurament: Rúbrica → Importar des de Sheets → tria el full.');
    console.log('   (El CSV equivalent queda versionat al repositori, com a font de veritat.)');
    return;
  }

  if (!APPLY) console.log('\n🔎 Mode descoberta. Executa amb APPLY=1 per crear-les.');
}

main().catch(e => {
  console.error('❌', e.message);
  if (e.dades) console.error(JSON.stringify(e.dades, null, 2));
  process.exit(1);
});
