/*
 * Carpeta de Drive del curs: tots els Google Forms que generem hi han d'anar,
 * en lloc de quedar escampats per l'arrel del Drive del docent.
 *
 * Busca una carpeta amb el nom esperat entre les que ha creat aquesta app
 * (l'àmbit és drive.file: només veu els seus fitxers) i, si no hi és, la crea.
 * Escriu l'id per pantalla perquè es fixi a `config.js` (DRIVE_FOLDER_ID).
 *
 * Ús:
 *   node preparar_drive.js            # descoberta: diu si existeix
 *   APPLY=1 node preparar_drive.js    # la crea si no existeix
 */
import { google } from 'googleapis';
import { getAuthClient, ambReintents } from './_form_sa_lib.js';
import { DRIVE_FOLDER_ID } from './config.js';

const APPLY = process.env.APPLY === '1';
const NOM_CARPETA = 'Robòtica amb Python 1r Batx 2627 — Formularis del curs';

async function main() {
  const auth = await getAuthClient();
  const drive = google.drive({ version: 'v3', auth });

  if (DRIVE_FOLDER_ID) {
    const meta = await ambReintents(
      () => drive.files.get({ fileId: DRIVE_FOLDER_ID, fields: 'id, name, trashed' }),
      'llegir la carpeta configurada');
    console.log(`✔ config.js ja apunta a: ${meta.data.name} (${meta.data.id})` +
                (meta.data.trashed ? ' ⚠️ ÉS A LA PAPERERA' : ''));
    return;
  }

  const res = await ambReintents(
    () => drive.files.list({
      q: `name = '${NOM_CARPETA.replace(/'/g, "\\'")}' and ` +
         `mimeType = 'application/vnd.google-apps.folder' and trashed = false`,
      fields: 'files(id, name)',
    }), 'buscar la carpeta');
  const trobada = (res.data.files || [])[0];
  if (trobada) {
    console.log(`✔ Carpeta ja existent: ${trobada.name}\n   id: ${trobada.id}`);
    console.log('\n👉 Posa aquest id a config.js (DRIVE_FOLDER_ID).');
    return;
  }

  if (!APPLY) {
    console.log(`🔎 No existeix cap carpeta «${NOM_CARPETA}».`);
    console.log('   Executa amb APPLY=1 per crear-la.');
    return;
  }

  const creada = await ambReintents(
    () => drive.files.create({
      requestBody: { name: NOM_CARPETA, mimeType: 'application/vnd.google-apps.folder' },
      fields: 'id, name, webViewLink',
    }), 'crear la carpeta');
  console.log(`✅ Carpeta creada: ${creada.data.name}\n   id: ${creada.data.id}` +
              `\n   ${creada.data.webViewLink}`);
  console.log('\n👉 Posa aquest id a config.js (DRIVE_FOLDER_ID).');
}

main().catch(e => {
  console.error('❌', e.message);
  const detall = e?.response?.data;
  if (detall) console.error(JSON.stringify(detall, null, 2));
  process.exit(1);
});
