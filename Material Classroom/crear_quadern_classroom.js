/*
 * El quadern tècnic al Classroom: un MATERIAL amb les plantilles del web i una
 * TASCA DE LLIURAMENT per trimestre (T1/T2/T3).
 *
 * El quadern és la dimensió «Quadern tècnic i pràctiques» (25 % de la nota,
 * rúbrica R4). El contracte, tal com el descriu
 * `Classes/00_General/00_Quadern_tecnic.md`: l'entrada de cada SA va dins de la
 * tasca de lliurament d'aquella SA, i el quadern SENCER es lliura en acabar
 * cada trimestre — que és el que crea aquest script.
 *
 * Les plantilles s'enllacen des del web publicat (`pdf/adjunts/…`), no des de
 * GitHub: així l'alumnat les baixa d'un clic.
 *
 * Idempotent per títol. Tot es crea en ESBORRANY.
 *
 * Ús (amb CLASSROOM_SECRETS_DIR definit):
 *   node crear_quadern_classroom.js           # descoberta
 *   APPLY=1 node crear_quadern_classroom.js   # crea material i tasques
 */
import fs from 'fs';
import { google } from 'googleapis';
import { getAuthClient, ambReintents, trobaTascaPerTitol } from './_form_sa_lib.js';
import { COURSE_ID, WEB_BASE, WEB_ROOT, GRADE_CATEGORIES } from './config.js';

const APPLY = process.env.APPLY === '1';

const TEMA_GENERAL = '00 · General (com funciona el curs)';
const PAGINA_QUADERN = `${WEB_BASE}/00-general/00-quadern-tecnic.html`;
const plantilla = (t) => `${WEB_ROOT}/pdf/adjunts/Quadern_tecnic_${t}.pdf`;

const MATERIAL = {
  titol: '📓 El teu quadern tècnic: com es porta i plantilles per trimestre',
  descripcio:
    'El quadern tècnic és el teu diari de treball i val el 25 % de la nota ' +
    '(rúbrica R4). Aquí tens com es porta (les 5 regles i els 6 apartats de ' +
    'cada entrada) i la plantilla de cada trimestre per si la vols fer servir ' +
    'de base. S\'escriu a cada sessió, 2-3 minuts: deixar-ho per al final és el ' +
    'pitjor error.',
  enllacos: [
    { url: PAGINA_QUADERN, title: 'Com es porta el quadern tècnic' },
    { url: plantilla('T1'), title: 'Plantilla del quadern · 1r trimestre (PDF)' },
    { url: plantilla('T2'), title: 'Plantilla del quadern · 2n trimestre (PDF)' },
    { url: plantilla('T3'), title: 'Plantilla del quadern · 3r trimestre (PDF)' },
  ],
};

const TRIMESTRES = [
  { t: 'T1', nom: '1r trimestre', sa: 'SA1-SA3' },
  { t: 'T2', nom: '2n trimestre', sa: 'SA4-SA6' },
  { t: 'T3', nom: '3r trimestre', sa: 'SA7-SA9' },
];

function descripcio({ t, nom, sa }) {
  return [
    `Puja el quadern tècnic SENCER del ${nom} (${sa}): una entrada per SA, amb els 6 apartats.`,
    '',
    'Es valora (R4) que estigui complet i al dia, que expliquis les teves decisions i els errors',
    'amb claredat (rutina DEPURA) i que facis servir la terminologia correcta.',
    '',
    'Recorda: l\'entrada de cada SA també l\'has entregat dins de la tasca de lliurament de la SA;',
    'aquí es mira el conjunt del trimestre, no cada entrada per separat.',
    '',
    'Pots pujar el document o, si treballes al núvol, l\'enllaç (comprova que el docent hi tingui accés).',
  ].join('\n');
}

async function main() {
  const auth = await getAuthClient();
  const classroom = google.classroom({ version: 'v1', auth });

  const topicsRes = await ambReintents(
    () => classroom.courses.topics.list({ courseId: COURSE_ID, pageSize: 100 }),
    'llistar temes');
  const temes = topicsRes.data.topic || [];
  const general = temes.find(tp => tp.name === TEMA_GENERAL);
  if (!general) throw new Error(`No trobo el tema «${TEMA_GENERAL}» — executa crear_estructura_curs.js`);

  // 1) Material amb les plantilles
  const materialsExistents = new Set();
  let pageToken;
  do {
    const res = await ambReintents(
      () => classroom.courses.courseWorkMaterials.list({
        courseId: COURSE_ID,
        courseWorkMaterialStates: ['PUBLISHED', 'DRAFT'],
        pageSize: 100, pageToken,
      }), 'llistar materials');
    for (const m of res.data.courseWorkMaterial || []) materialsExistents.add(m.title);
    pageToken = res.data.nextPageToken;
  } while (pageToken);

  if (materialsExistents.has(MATERIAL.titol)) {
    console.log(`↷ Material ja existent: ${MATERIAL.titol}`);
  } else if (!APPLY) {
    console.log(`· [descoberta] crearia el material: ${MATERIAL.titol} (${MATERIAL.enllacos.length} enllaços)`);
  } else {
    await ambReintents(
      () => classroom.courses.courseWorkMaterials.create({
        courseId: COURSE_ID,
        requestBody: {
          title: MATERIAL.titol,
          description: MATERIAL.descripcio,
          state: 'DRAFT',
          topicId: general.topicId,
          materials: MATERIAL.enllacos.map(l => ({ link: { url: l.url, title: l.title } })),
        },
      }), 'crear el material del quadern');
    console.log(`✅ Material creat (DRAFT): ${MATERIAL.titol}`);
  }

  // 2) Una tasca de lliurament per trimestre
  const creades = [];
  const senseCategoria = [];
  for (const tri of TRIMESTRES) {
    const titol = `📓 Quadern tècnic — ${tri.t} (${tri.nom})`;
    const categoria = GRADE_CATEGORIES[tri.t];
    if (!categoria?.id) { console.log(`  ⚠ ${tri.t}: falta l'id de la categoria a config.js`); continue; }

    const existent = await trobaTascaPerTitol(classroom, titol);
    if (existent) { console.log(`  ↷ ${tri.t}: la tasca ja existeix (${existent.state})`); continue; }
    if (!APPLY) {
      console.log(`  · [descoberta] crearia: ${titol} · 10 punts · categoria ${tri.t}`);
      continue;
    }

    const cw = await ambReintents(
      () => classroom.courses.courseWork.create({
        courseId: COURSE_ID,
        requestBody: {
          title: titol,
          description: descripcio(tri),
          workType: 'ASSIGNMENT',
          state: 'DRAFT',
          maxPoints: 10,
          topicId: general.topicId,
          gradeCategory: { id: categoria.id },
          materials: [
            { link: { url: PAGINA_QUADERN, title: 'Com es porta el quadern tècnic' } },
            { link: { url: plantilla(tri.t), title: `Plantilla del quadern · ${tri.nom} (PDF)` } },
          ],
        },
      }), `crear la tasca del quadern ${tri.t}`);
    // ⚠️ Vegeu `crear_tasques_lliurament.js`: l'API accepta `gradeCategory`
    // però no l'aplica; s'ha d'assignar a mà des de Classroom.
    if (!cw.data.gradeCategory?.id) senseCategoria.push(`${titol} → ${tri.t}`);
    console.log(`  ✅ ${tri.t}: tasca creada (DRAFT, 10 punts) — id ${cw.data.id}`);
    creades.push({ trimestre: tri.t, id: cw.data.id, titol });
  }

  if (senseCategoria.length) {
    console.log('\n⚠️ Categoria de nota NO assignada per l\'API (no ho permet). ' +
                'Assigna-la a mà a cada tasca:');
    for (const t of senseCategoria) console.log(`   · ${t}`);
  }

  if (creades.length) {
    fs.writeFileSync('resultats_quadern_classroom.json',
      JSON.stringify({ creat: new Date().toISOString(), creades }, null, 2));
    console.log('\n💾 Desat a resultats_quadern_classroom.json');
  }
  if (!APPLY) console.log('\n🔎 Mode descoberta. Executa amb APPLY=1 per crear-ho.');
  else console.log('\nFet. Tot en ESBORRANY: publica-ho i posa-hi data de final de trimestre.');
}

main().catch(e => {
  console.error('❌', e.message);
  const detall = e?.response?.data;
  if (detall) console.error(JSON.stringify(detall, null, 2));
  process.exit(1);
});
