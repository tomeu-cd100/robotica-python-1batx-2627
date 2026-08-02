/*
 * Tasques de LLIURAMENT del producte de cada SA (SA1-SA9), amb punts i
 * categoria de nota del trimestre corresponent. Es creen en ESBORRANY, al tema
 * de la seva SA, amb enllaç a la fitxa i al checklist d'autoavaluació del web.
 *
 * Cada tasca demana el mateix, perquè és el contracte del curs: el producte de
 * la SA (codi .py comentat), el repte ⭐ validat pel docent (nucli obligatori,
 * SA2-SA8) i l'entrada del quadern tècnic d'aquella SA.
 *
 * 10 punts per tasca = la nota de la SA en escala 0-10. La ponderació entre
 * dimensions (projectes 45 %, proves 25 %, quadern 20 %, actitud 10 %) es fa
 * amb les categories de nota del curs, no dins de cada tasca.
 *
 * Idempotent per títol. Ús (amb CLASSROOM_SECRETS_DIR definit):
 *   node crear_tasques_lliurament.js           # descoberta
 *   APPLY=1 node crear_tasques_lliurament.js   # crea les tasques
 */
import fs from 'fs';
import { google } from 'googleapis';
import { getAuthClient, ambReintents, trobaTascaPerTitol } from './_form_sa_lib.js';
import { COURSE_ID, WEB_BASE, WEB_ROOT, GRADE_CATEGORIES, SA_TRIMESTRE } from './config.js';

const APPLY = process.env.APPLY === '1';

// Producte de cada SA, resumit de `SAn_guia_docent.md` («Producte de la SA»).
const PRODUCTES = {
  1: { nom: 'Fitxa-pòster d\'anàlisi d\'un robot real',
       detall: 'la fitxa-pòster individual (entrada → procés → sortida d\'un robot real) i les primeres entrades del quadern tècnic.' },
  2: { nom: 'Semàfor o llum d\'ambient',
       detall: 'el programa del semàfor/llum d\'ambient amb el relé, i el repte ⭐ (LED de P1 amb mode alerta).' },
  3: { nom: 'Mascota reactiva (tanca el Projecte T1)',
       detall: 'la mascota amb dues reaccions sensor → resposta com a mínim, coherents amb el caràcter que li has triat, i el repte ⭐ de llum automàtica.' },
  4: { nom: 'Control per botons del vehicle',
       detall: 'avançar, retrocedir, girar i aturar amb funcions pròpies activades pels botons, i el repte ⭐ de la salutació amb paràmetre.' },
  5: { nom: 'Control remot bàsic per ràdio',
       detall: 'el vehicle teledirigit amb un protocol propi (mínim 4 comandes) i el repte ⭐ del recompte de missatges per remitent.' },
  6: { nom: 'Vehicle amb aturada d\'emergència (tanca el Projecte T2)',
       detall: 'control per ràdio + màquina d\'estats + STOP prioritari amb senyal visual de l\'estat, i el repte ⭐ de la SA.' },
  7: { nom: 'Comportament autònom del rover',
       detall: 'seguidor de línia i/o evita-obstacles integrat en una estructura de missions, i el repte ⭐ de velocitat variable de correcció.' },
  8: { nom: 'Telemetria del rover',
       detall: 'dos sensors com a mínim enviats per ràdio i rebuts a la teva pròpia estació base, amb la reflexió sobre la IA aplicada al control.' },
  9: { nom: 'Projecte final: rover ampliat + dossier + defensa',
       detall: 'el rover ampliat amb el teu repte lliure funcionant, el dossier tècnic complet i la defensa oral individual.' },
};

function descripcio(n) {
  const p = PRODUCTES[n];
  const reptes = n === 9
    ? 'El repte de projecte el tries tu del banc de reptes proposats.'
    : (n === 1
        ? ''
        : 'El repte ⭐ és NUCLI OBLIGATORI (no una ampliació): ensenya\'l al docent perquè el validi.');
  return [
    `Lliura el producte de la SA${n}: ${p.detall}`,
    '',
    'Què entregues:',
    '· El codi .py comentat (en català, sense accents als comentaris).',
    '· L\'entrada del quadern tècnic d\'aquesta SA (predicció, què has fet, un error i com l\'has resolt).',
    reptes,
    '',
    'Abans d\'entregar, passa el checklist d\'autoavaluació de la SA: si hi tens dos o més 🔴, demana ajuda abans del dia del lliurament.',
  ].filter(Boolean).join('\n');
}

function materials(n) {
  const base = `${WEB_BASE}/sa${n}`;
  const m = [
    { url: `${base}/sa${n}-fitxa-alumnat.html`, title: `Fitxa de l'alumnat · SA${n}` },
    { url: `${base}/sa${n}-checklist-alumnat.html`, title: `Checklist d'autoavaluació · SA${n}` },
  ];
  if (n === 9) {
    m.push({ url: `${base}/sa9-dossier-plantilla.html`, title: 'Plantilla del dossier tècnic' });
  } else if (n >= 2) {
    m.push({ url: `${WEB_ROOT}/reptes/reptes-sa${n}.html`, title: `Reptes · SA${n} (el ⭐ és obligatori)` });
  }
  return m.map(l => ({ link: { url: l.url, title: l.title } }));
}

async function main() {
  const auth = await getAuthClient();
  const classroom = google.classroom({ version: 'v1', auth });

  const topicsRes = await ambReintents(
    () => classroom.courses.topics.list({ courseId: COURSE_ID, pageSize: 100 }),
    'llistar temes');
  const temes = topicsRes.data.topic || [];

  const creades = [];
  for (let n = 1; n <= 9; n++) {
    const titol = `SA${n} · Lliurament del producte: ${PRODUCTES[n].nom}`;
    const tema = temes.find(tp => tp.name && tp.name.toUpperCase().startsWith(`SA${n}`));
    if (!tema) { console.log(`  ⚠ SA${n}: no trobo el tema — executa crear_estructura_curs.js`); continue; }

    const trimestre = SA_TRIMESTRE[n];
    const categoria = GRADE_CATEGORIES[trimestre];
    if (!categoria?.id) { console.log(`  ⚠ SA${n}: falta l'id de la categoria ${trimestre} a config.js`); continue; }

    const existent = await trobaTascaPerTitol(classroom, titol);
    if (existent) { console.log(`  ↷ SA${n}: la tasca ja existeix (${existent.state})`); continue; }
    if (!APPLY) {
      console.log(`  · [descoberta] crearia: ${titol}\n      tema «${tema.name}» · 10 punts · categoria ${trimestre}`);
      continue;
    }

    const cw = await ambReintents(
      () => classroom.courses.courseWork.create({
        courseId: COURSE_ID,
        requestBody: {
          title: titol,
          description: descripcio(n),
          workType: 'ASSIGNMENT',
          state: 'DRAFT',
          maxPoints: 10,
          topicId: tema.topicId,
          gradeCategory: { id: categoria.id },
          materials: materials(n),
        },
      }), `crear la tasca de SA${n}`);
    console.log(`  ✅ SA${n}: creada (DRAFT, 10 punts, ${trimestre}) — id ${cw.data.id}`);
    creades.push({ sa: `SA${n}`, id: cw.data.id, titol, trimestre });
  }

  if (creades.length) {
    fs.writeFileSync('resultats_tasques_lliurament.json',
      JSON.stringify({ creat: new Date().toISOString(), creades }, null, 2));
    console.log('\n💾 Desat a resultats_tasques_lliurament.json');
  }
  if (!APPLY) console.log('\n🔎 Mode descoberta. Executa amb APPLY=1 per crear-les.');
  else console.log('\nFet. Les tasques queden en ESBORRANY: publica-les i posa-hi data quan comenci cada SA.');
}

main().catch(e => {
  console.error('❌', e.message);
  const detall = e?.response?.data;
  if (detall) console.error(JSON.stringify(detall, null, 2));
  process.exit(1);
});
