/*
 * Esquelet del Classroom del curs: TEMES (un per SA + un de general) i, per a
 * cada tema, un MATERIAL-ENLLAÇ a les pàgines de l'alumnat del web publicat.
 * No crea Forms ni fitxers de Drive: només estructura i enllaços.
 *
 * Idempotent: els temes es busquen per nom i els materials per títol; tornar a
 * executar-lo no duplica res.
 *
 * Els materials es creen com a DRAFT: el docent els publica quan toca.
 *
 * Ordre dels temes: Classroom col·loca a dalt l'últim tema creat, així que es
 * creen del final cap al principi (SA9 → SA0 → General) perquè a la pantalla
 * quedin en ordre de curs, amb el material general a dalt de tot.
 *
 * Ús (des d'aquesta carpeta, amb CLASSROOM_SECRETS_DIR definit):
 *   node crear_estructura_curs.js            # crea (DRAFT)
 *   node crear_estructura_curs.js --simula   # només mostra què faria
 */
import fs from 'fs';
import { google } from 'googleapis';
import { getAuthClient, ambReintents } from './_form_sa_lib.js';
import { COURSE_ID, WEB_BASE, WEB_ROOT } from './config.js';

const SIMULA = process.argv.includes('--simula');

const SA = [
  { n: 0, nom: 'Punt de partida' },
  { n: 1, nom: 'Hola, robot!' },
  { n: 2, nom: 'Sortides: el robot actua' },
  { n: 3, nom: 'Entrades: el robot percep' },
  { n: 4, nom: 'Funcions i moviment' },
  { n: 5, nom: 'Ràdio: robots que parlen' },
  { n: 6, nom: 'Control: el robot decideix' },
  { n: 7, nom: 'Robòtica mòbil: el rover' },
  { n: 8, nom: 'Autonomia i telemetria' },
  { n: 9, nom: 'Repte final integrador' },
];

const TEMA_GENERAL = '00 · General (com funciona el curs)';
const temaSA = (sa) => `SA${sa.n} · ${sa.nom}`;

// Enllaços de l'alumnat per SA. SA0 és acollida (no té fitxa ni checklist):
// hi van les tres pàgines de referència que sí que té.
function materialsSA(sa) {
  if (sa.n === 0) {
    return [
      { url: `${WEB_BASE}/sa0/sa0-primers-passos-editor.html`, title: 'Primers passos amb l\'editor' },
      { url: `${WEB_BASE}/sa0/sa0-vocabulari-robotica.html`, title: 'Vocabulari de robòtica' },
      { url: `${WEB_BASE}/sa0/sa0-guia-programacio.html`, title: 'Guia de programació (seccions A1-A9)' },
    ];
  }
  const base = `${WEB_BASE}/sa${sa.n}`;
  const enllacos = [
    { url: `${base}/sa${sa.n}-fitxa-alumnat.html`, title: `Fitxa de l'alumnat · SA${sa.n}` },
    { url: `${base}/sa${sa.n}-checklist-alumnat.html`, title: `Checklist d'autoavaluació · SA${sa.n}` },
  ];
  // SA1-SA8 tenen banc de reptes propi; la SA9 té els reptes de projecte
  // proposats i la plantilla del dossier, dins la seva pròpia carpeta.
  if (sa.n === 9) {
    enllacos.push(
      { url: `${base}/sa9-reptes-proposats.html`, title: 'Reptes de projecte proposats · SA9' },
      { url: `${base}/sa9-dossier-plantilla.html`, title: 'Plantilla del dossier tècnic · SA9' });
  } else {
    enllacos.push(
      { url: `${WEB_ROOT}/reptes/reptes-sa${sa.n}.html`, title: `Reptes · SA${sa.n} (el ⭐ és obligatori)` });
  }
  return enllacos;
}

function descripcioSA(sa) {
  if (sa.n === 0) {
    return 'Material d\'acollida: com s\'escriu i es transfereix un programa, el '
      + 'vocabulari bàsic i la guia de programació que fem servir tot el curs com a '
      + 'referència (seccions A1-A9).';
  }
  return `Material de treball de la SA${sa.n}: la fitxa amb les activitats de cada `
    + 'sessió, el checklist per autoavaluar-te abans de tancar la unitat i els reptes '
    + '(recorda que el repte ⭐ és nucli obligatori, no una ampliació).';
}

const MATERIALS_GENERALS = [
  {
    titol: '🧭 Com funciona el curs: d\'on surt la teva nota',
    descripcio: 'Llegeix-ho la primera setmana: les 4 parts de la nota, què qualifica '
      + 'i què no, la porta mínima de programació, els mini-checks i el semàfor d\'ús '
      + 'de la IA.',
    enllacos: [
      { url: `${WEB_BASE}/00-general/00-avaluacio-per-alumnat.html`, title: 'D\'on surt la nota' },
      { url: `${WEB_BASE}/00-general/00-quadern-tecnic.html`, title: 'El quadern tècnic (com es porta)' },
    ],
  },
  {
    titol: '🛠️ Entorn de treball: editor, simulador i transferència del programa',
    descripcio: 'Com escriure el programa, provar-lo al simulador i passar-lo a la placa. '
      + 'Torna-hi sempre que el programa "no faci res" a la micro:bit.',
    enllacos: [
      { url: `${WEB_BASE}/00-general/00-entorns-de-treball.html`, title: 'Entorns de treball' },
      { url: `${WEB_ROOT}/simulacions/simulador-microbit.html`, title: 'Simulador de micro:bit' },
    ],
  },
  {
    titol: '🆘 Si t\'encalles (o si has faltat a classe)',
    descripcio: 'Els dos circuits d\'autonomia del curs: les targetes de rescat (3 nivells '
      + 'de pista per SA, abans de cridar el docent) i l\'itinerari per posar-te al dia '
      + 'tot sol després de faltar a una sessió.',
    enllacos: [
      { url: `${WEB_BASE}/00-general/00-targetes-rescat.html`, title: 'Targetes de rescat' },
      { url: `${WEB_BASE}/00-general/00-vaig-faltar.html`, title: 'Vaig faltar a classe' },
    ],
  },
];

async function llistaTemes(classroom) {
  const res = await ambReintents(
    () => classroom.courses.topics.list({ courseId: COURSE_ID, pageSize: 100 }),
    'llistar temes');
  return res.data.topic || [];
}

async function llistaMaterials(classroom) {
  const titols = new Set();
  let pageToken;
  do {
    const res = await ambReintents(
      () => classroom.courses.courseWorkMaterials.list({
        courseId: COURSE_ID,
        courseWorkMaterialStates: ['PUBLISHED', 'DRAFT'],
        pageSize: 100,
        pageToken,
      }), 'llistar materials');
    for (const m of res.data.courseWorkMaterial || []) titols.add(m.title);
    pageToken = res.data.nextPageToken;
  } while (pageToken);
  return titols;
}

async function assegurarTema(classroom, nom, existents) {
  const trobat = existents.find(tp => tp.name === nom);
  if (trobat) {
    console.log(`↷ Tema ja existent: ${nom}`);
    return trobat.topicId;
  }
  if (SIMULA) {
    console.log(`· [simulació] crearia el tema: ${nom}`);
    return null;
  }
  const res = await ambReintents(
    () => classroom.courses.topics.create({
      courseId: COURSE_ID, requestBody: { name: nom }
    }), `crear tema «${nom}»`);
  console.log(`✅ Tema creat: ${nom}`);
  existents.push({ topicId: res.data.topicId, name: nom });
  return res.data.topicId;
}

async function crearMaterial(classroom, { titol, descripcio, enllacos, topicId }, titolsExistents) {
  if (titolsExistents.has(titol)) {
    console.log(`   ↷ Material ja existent: ${titol}`);
    return null;
  }
  if (SIMULA) {
    console.log(`   · [simulació] crearia el material: ${titol} (${enllacos.length} enllaços)`);
    return null;
  }
  const res = await ambReintents(
    () => classroom.courses.courseWorkMaterials.create({
      courseId: COURSE_ID,
      requestBody: {
        title: titol,
        description: descripcio,
        state: 'DRAFT',
        topicId,
        materials: enllacos.map(l => ({ link: { url: l.url, title: l.title } })),
      },
    }), `crear material «${titol}»`);
  console.log(`   ✅ Material creat (DRAFT): ${titol}`);
  titolsExistents.add(titol);
  return res.data;
}

async function main() {
  const auth = await getAuthClient();
  const classroom = google.classroom({ version: 'v1', auth });

  console.log(`\n=== Estructura del curs ${COURSE_ID}${SIMULA ? ' (SIMULACIÓ)' : ''} ===\n`);
  const temes = await llistaTemes(classroom);
  const titols = await llistaMaterials(classroom);

  const resultats = [];

  // De SA9 cap a SA0 perquè a la pantalla quedin en ordre de curs.
  for (const sa of [...SA].reverse()) {
    const nom = temaSA(sa);
    const topicId = await assegurarTema(classroom, nom, temes);
    const r = await crearMaterial(classroom, {
      titol: `${nom} — material de l'alumnat`,
      descripcio: descripcioSA(sa),
      enllacos: materialsSA(sa),
      topicId,
    }, titols);
    resultats.push({ tema: nom, topicId, material: r?.alternateLink || null });
  }

  // El general es crea l'últim perquè quedi a dalt de tot.
  const topicGeneral = await assegurarTema(classroom, TEMA_GENERAL, temes);
  for (const m of MATERIALS_GENERALS) {
    const r = await crearMaterial(classroom, { ...m, topicId: topicGeneral }, titols);
    resultats.push({ tema: TEMA_GENERAL, topicId: topicGeneral, material: r?.alternateLink || null });
  }

  if (!SIMULA) {
    fs.writeFileSync('resultats_estructura_curs.json',
      JSON.stringify({ creat: new Date().toISOString(), resultats }, null, 2));
    console.log('\n💾 Resultats desats a resultats_estructura_curs.json');
  }
  console.log('\nFet. Els materials queden en ESBORRANY: publica\'ls des del Classroom quan toqui.');
}

main().catch(e => { console.error('❌', e.message); process.exit(1); });
