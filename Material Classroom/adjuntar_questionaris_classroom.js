/*
 * Adjunta al Classroom els Google Forms dels qüestionaris de conceptes creats
 * amb `crear_questionaris_conceptes_forms.js` (llegeix
 * `resultats_questionaris_conceptes.json`).
 *
 * Cada qüestionari es penja com a tasca SENSE NOTA (maxPoints 0) al tema de la
 * seva SA: són repàs formatiu i no qualifiquen mai
 * (`Programació didàctica/06_Avaluacio_criteris_qualificacio.md` §6.2).
 * Es creen en ESBORRANY: el docent les publica en acabar cada SA.
 *
 * Idempotent: si ja existeix una tasca amb el mateix títol, la salta.
 *
 * Ús (des d'aquesta carpeta, amb CLASSROOM_SECRETS_DIR definit):
 *   node adjuntar_questionaris_classroom.js           # descoberta
 *   APPLY=1 node adjuntar_questionaris_classroom.js   # crea les tasques
 */
import fs from 'fs';
import { google } from 'googleapis';
import { getAuthClient, ambReintents, trobaTascaPerTitol } from './_form_sa_lib.js';
import { COURSE_ID } from './config.js';

const APPLY = process.env.APPLY === '1';
const FONT = 'resultats_questionaris_conceptes.json';

const DESCRIPCIO =
  'Repàs formatiu de la SA: 10 preguntes de resposta única que es corregeixen ' +
  'soles en enviar el formulari, més una pregunta oberta. NO qualifica: serveix ' +
  'perquè sàpigues què tens fluix abans de la prova del trimestre. Fes-lo sense ' +
  'apunts i, del que hagis fallat, torna al material de la SA.';

async function main() {
  if (!fs.existsSync(FONT)) {
    throw new Error(`Falta ${FONT}: executa primer APPLY=1 node crear_questionaris_conceptes_forms.js`);
  }
  const { resultats } = JSON.parse(fs.readFileSync(FONT, 'utf8'));

  const auth = await getAuthClient();
  const classroom = google.classroom({ version: 'v1', auth });

  const topicsRes = await ambReintents(
    () => classroom.courses.topics.list({ courseId: COURSE_ID, pageSize: 100 }),
    'llistar temes');
  const temes = topicsRes.data.topic || [];

  for (const r of resultats) {
    const titol = `${r.sa} · Qüestionari de conceptes (repàs formatiu, no qualifica)`;
    const tema = temes.find(tp => tp.name && tp.name.toUpperCase().startsWith(r.sa));
    if (!tema) {
      console.log(`  ⚠ ${r.sa}: no trobo el tema al Classroom — executa crear_estructura_curs.js`);
      continue;
    }
    if (!r.respon || r.respon === '(ja existia)') {
      console.log(`  ⚠ ${r.sa}: no tinc l'enllaç de resposta del Form (${r.respon}) — el salto`);
      continue;
    }

    const existent = await trobaTascaPerTitol(classroom, titol);
    if (existent) {
      console.log(`  ↷ ${r.sa}: la tasca ja existeix (${existent.state})`);
      continue;
    }
    if (!APPLY) {
      console.log(`  · [descoberta] crearia: ${titol} → tema «${tema.name}»`);
      continue;
    }

    const cw = await ambReintents(
      () => classroom.courses.courseWork.create({
        courseId: COURSE_ID,
        requestBody: {
          title: titol,
          description: DESCRIPCIO,
          workType: 'ASSIGNMENT',
          state: 'DRAFT',
          maxPoints: 0,          // sense nota: és formatiu
          topicId: tema.topicId,
          materials: [{ link: { url: r.respon, title: 'Qüestionari (Google Form autocorrectiu)' } }],
        },
      }), `crear la tasca de ${r.sa}`);
    console.log(`  ✅ ${r.sa}: tasca creada (DRAFT) → ${cw.data.alternateLink}`);
  }

  if (!APPLY) console.log('\n🔎 Mode descoberta. Executa amb APPLY=1 per crear-les.');
  else console.log('\nFet. Les tasques queden en ESBORRANY: publica-les en acabar cada SA.');
}

main().catch(e => {
  console.error('❌', e.message);
  const detall = e?.response?.data;
  if (detall) console.error(JSON.stringify(detall, null, 2));
  process.exit(1);
});
