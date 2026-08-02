/*
 * Tanca els forats del Classroom respecte a l'avaluació del curs:
 *
 *  1. PROVES PRÀCTIQUES T1/T2/T3 (15 % de la nota): una tasca per trimestre, al
 *     tema de la SA on es fa la prova (S4 de SA3, S4 de SA6, S5 de SA9). Es
 *     corregeixen amb la GRAELLA D'ÍTEMS del seu enunciat, no amb una rúbrica de
 *     nivells: la graella ja reparteix els 10 punts entre ítems i criteris.
 *     ⚠️ L'enunciat viu a `Avaluació/` (vista docent, porta la solució): la
 *     tasca NO l'enllaça; enllaça el material de repàs de l'alumnat.
 *
 *  2. MILLOR MINI-CHECK DEL TRIMESTRE (5 %): una tasca de registre de nota per
 *     trimestre. No hi ha res a lliurar (els mini-checks es fan a classe, en
 *     paper o a l'editor): serveix perquè la nota del millor mini-check tingui
 *     on posar-se, tal com descriu `00_Mini_checks_individuals.md`.
 *
 *  3. MATERIALS que faltaven: els tres dossiers de projecte trimestral (el fil
 *     conductor de construccions), el glossari tècnic i el full de normes de
 *     seguretat de la SA1.
 *
 * Tot en ESBORRANY i idempotent per títol.
 *
 * Ús (amb CLASSROOM_SECRETS_DIR definit):
 *   node crear_proves_i_materials.js           # descoberta
 *   APPLY=1 node crear_proves_i_materials.js   # crea-ho
 */
import fs from 'fs';
import { google } from 'googleapis';
import { getAuthClient, ambReintents, trobaTascaPerTitol } from './_form_sa_lib.js';
import { COURSE_ID, WEB_BASE, WEB_ROOT } from './config.js';

const APPLY = process.env.APPLY === '1';
const TEMA_GENERAL = '00 · General (com funciona el curs)';

// Ordinals en català: 1r, 2n, 3r (no «2r»).
const ORDINAL = { T1: '1r', T2: '2n', T3: '3r' };

// --- 1) Proves pràctiques -----------------------------------------------------
const PROVES = [
  {
    t: 'T1', sa: 'SA3', quan: 'la Sessió 4 de la SA3',
    entra: 'tot el que has fet a SA1-SA3: display i botons, sortides digitals i PWM, '
      + 'entrades analògiques amb llindars calibrats al REPL i condicionals.',
    repas: [
      { url: `${WEB_BASE}/sa0/sa0-guia-programacio.html`, title: 'Guia de programació (seccions A1-A9)' },
      { url: `${WEB_BASE}/00-general/00-repas-expres-micropython.html`, title: 'Repàs exprés de MicroPython' },
    ],
  },
  {
    t: 'T2', sa: 'SA6', quan: 'la Sessió 4 de la SA6',
    entra: 'tot el que has fet a SA4-SA6: funcions amb paràmetres i retorn, moviment del '
      + 'vehicle, protocol de ràdio, màquina d\'estats, histèresi i STOP prioritari. '
      + 'Inclou un ítem obligatori de funció nova i un altre de depuració amb traceback.',
    repas: [
      { url: `${WEB_BASE}/sa0/sa0-guia-programacio.html`, title: 'Guia de programació (seccions A1-A9)' },
      { url: `${WEB_BASE}/00-general/00-repas-expres-radio.html`, title: 'Repàs exprés de ràdio' },
    ],
  },
  {
    t: 'T3', sa: 'SA9', quan: 'la Sessió 5 de la SA9 (per estacions rotatives)',
    entra: 'les destreses de SA7-SA8: cinemàtica del rover, seguidor de línia, ultrasons '
      + 'amb lectura robusta, telemetria per ràdio i un comportament nou que hauràs '
      + 'd\'escriure allà mateix.',
    repas: [
      { url: `${WEB_BASE}/00-general/00-repas-expres-micropython.html`, title: 'Repàs exprés de MicroPython' },
      { url: `${WEB_BASE}/00-general/00-repas-expres-radio.html`, title: 'Repàs exprés de ràdio' },
    ],
  },
];

const descProva = (p) =>
  [`Prova pràctica individual del ${ORDINAL[p.t]} trimestre, que es fa a classe durant ${p.quan}.`,
   '',
   `Hi entra ${p.entra}`,
   '',
   'Es corregeix amb la graella d\'ítems de l\'enunciat (10 punts): cada ítem diu quants',
   'punts val i quin criteri avalua. Pots consultar els teus esquemes i el quadern tècnic:',
   'no s\'avalua la memòria, sinó saber fer i saber trobar.',
   '',
   'Val el 15 % de la nota del trimestre; el 5 % restant de la dimensió surt del teu millor',
   'mini-check (tasca a part).',
   '',
   'Aquí no has de lliurar res: la nota la posa el docent en acabar la prova.'].join('\n');

// --- 2) Millor mini-check -----------------------------------------------------
const descMiniCheck = (t) =>
  [`Nota del MILLOR dels teus mini-checks del ${ORDINAL[t]} trimestre (5 % de la nota).`,
   '',
   'Els mini-checks són els micro-reptes de 10 minuts que fas a classe, sense apunts ni IA.',
   'Cap d\'ells no puntua el dia que el fas: són el teu radar. En tancar el trimestre, el',
   'docent agafa el que t\'ha sortit MILLOR i el converteix en nota (🟢 9-10 · 🟡 6-8 ·',
   '🟠 4-5 · 🔴 1-3). No es fa mitjana: un dia fluix no et penalitza.',
   '',
   'Aquí no has de lliurar res: és el lloc on es registra aquesta nota.'].join('\n');

// --- 3) Materials que faltaven ------------------------------------------------
const MATERIALS = [
  {
    tema: 'SA2',
    titol: '🐾 Projecte del 1r trimestre: la mascota',
    descripcio: 'El dossier del primer projecte del fil conductor: què has de construir, el '
      + 'cablatge EXACTE (quin component va a quin pin i per què no a un altre) i com es '
      + 'tanca a la SA3. Consulta\'l sempre abans de cablejar res.',
    enllacos: [
      { url: `${WEB_BASE}/00-general/00-projecte-t1-mascota.html`, title: 'Dossier del projecte T1 · Mascota' },
      { url: `${WEB_BASE}/00-general/00-fil-conductor-construccions.html`, title: 'Fil conductor i mapa de pins del curs' },
    ],
  },
  {
    tema: 'SA4',
    titol: '🚗 Projecte del 2n trimestre: el vehicle',
    descripcio: 'El dossier del segon projecte: el vehicle que munta la SA4 i que la SA5 i la '
      + 'SA6 fan teledirigit i segur. Inclou el cablatge dels motors (M1/M2) que ja no es toca '
      + 'fins al final de curs.',
    enllacos: [
      { url: `${WEB_BASE}/00-general/00-projecte-t2-vehicle.html`, title: 'Dossier del projecte T2 · Vehicle' },
      { url: `${WEB_BASE}/00-general/00-fil-conductor-construccions.html`, title: 'Fil conductor i mapa de pins del curs' },
    ],
  },
  {
    tema: 'SA7',
    titol: '🤖 Projecte del 3r trimestre: el rover',
    descripcio: 'El dossier del projecte final: com el vehicle es converteix en rover (sensors '
      + 'nous, canvi de pins) i cap a on va la SA9. Atenció a la conversió T2 → T3: alguns '
      + 'components canvien de pin.',
    enllacos: [
      { url: `${WEB_BASE}/00-general/00-projecte-t3-rover.html`, title: 'Dossier del projecte T3 · Rover' },
      { url: `${WEB_BASE}/00-general/00-fil-conductor-construccions.html`, title: 'Fil conductor i mapa de pins del curs' },
    ],
  },
  {
    tema: 'SA1',
    titol: '⚠️ Normes de seguretat del laboratori (es llegeixen i es signen)',
    descripcio: 'Les 12 normes del taller de robòtica. Es llegeixen en veu alta a la Sessió 2, '
      + 'es comenten amb exemples i cadascú signa el compromís: el full signat es guarda a la '
      + 'carpeta del grup.',
    enllacos: [
      { url: `${WEB_BASE}/sa1/sa1-normes-seguretat.html`, title: 'Normes de seguretat · SA1' },
      { url: `${WEB_ROOT}/pdf/adjunts/SA1_normes_seguretat.pdf`, title: 'Full per imprimir i signar (PDF)' },
    ],
  },
  {
    tema: TEMA_GENERAL,
    titol: '📖 Glossari tècnic del curs',
    descripcio: 'Els termes del curs explicats en llenguatge planer, amb l\'equivalent en anglès '
      + 'que trobaràs a la documentació. Quan una paraula et bloquegi, busca-la aquí abans que '
      + 'a Internet.',
    enllacos: [
      { url: `${WEB_BASE}/00-general/00-glossari-tecnic.html`, title: 'Glossari tècnic' },
    ],
  },
];

async function main() {
  const auth = await getAuthClient();
  const classroom = google.classroom({ version: 'v1', auth });

  const topicsRes = await ambReintents(
    () => classroom.courses.topics.list({ courseId: COURSE_ID, pageSize: 100 }),
    'llistar temes');
  const temes = topicsRes.data.topic || [];
  const temaPer = (clau) => clau === TEMA_GENERAL
    ? temes.find(tp => tp.name === TEMA_GENERAL)
    : temes.find(tp => tp.name && tp.name.toUpperCase().startsWith(clau));

  const creades = [];
  const senseCategoria = [];

  // 1) i 2): proves i millor mini-check
  console.log('=== Tasques de la dimensió «Proves pràctiques» (20 %) ===');
  for (const p of PROVES) {
    const tema = temaPer(p.sa);
    if (!tema) { console.log(`  ⚠ ${p.t}: no trobo el tema ${p.sa}`); continue; }

    const feines = [
      {
        titol: `📝 Prova pràctica ${p.t} (individual, a classe)`,
        descripcio: descProva(p),
        materials: p.repas.map(l => ({ link: { url: l.url, title: l.title } })),
      },
      {
        titol: `🎯 Millor mini-check del ${ORDINAL[p.t]} trimestre`,
        descripcio: descMiniCheck(p.t),
        materials: [{ link: { url: `${WEB_BASE}/00-general/00-avaluacio-per-alumnat.html`,
                              title: 'Com funciona el millor mini-check (D\'on surt la nota, §5)' }}],
      },
    ];

    for (const f of feines) {
      const existent = await trobaTascaPerTitol(classroom, f.titol);
      if (existent) { console.log(`  ↷ ja existeix: ${f.titol}`); continue; }
      if (!APPLY) { console.log(`  · [descoberta] crearia: ${f.titol} → tema «${tema.name}», 10 punts`); continue; }

      const cw = await ambReintents(
        () => classroom.courses.courseWork.create({
          courseId: COURSE_ID,
          requestBody: {
            title: f.titol,
            description: f.descripcio,
            workType: 'ASSIGNMENT',
            state: 'DRAFT',
            maxPoints: 10,
            topicId: tema.topicId,
            materials: f.materials,
          },
        }), `crear «${f.titol}»`);
      if (!cw.data.gradeCategory?.id) senseCategoria.push(`${f.titol} → ${p.t}`);
      console.log(`  ✅ creada (DRAFT, 10 punts): ${f.titol}`);
      creades.push({ titol: f.titol, id: cw.data.id, trimestre: p.t });
    }
  }

  // 3) materials
  console.log('\n=== Materials que faltaven ===');
  const titolsMaterials = new Set();
  let pageToken;
  do {
    const res = await ambReintents(
      () => classroom.courses.courseWorkMaterials.list({
        courseId: COURSE_ID, courseWorkMaterialStates: ['PUBLISHED', 'DRAFT'],
        pageSize: 100, pageToken,
      }), 'llistar materials');
    for (const m of res.data.courseWorkMaterial || []) titolsMaterials.add(m.title);
    pageToken = res.data.nextPageToken;
  } while (pageToken);

  for (const m of MATERIALS) {
    const tema = temaPer(m.tema);
    if (!tema) { console.log(`  ⚠ ${m.titol}: no trobo el tema ${m.tema}`); continue; }
    if (titolsMaterials.has(m.titol)) { console.log(`  ↷ ja existeix: ${m.titol}`); continue; }
    if (!APPLY) { console.log(`  · [descoberta] crearia: ${m.titol} → tema «${tema.name}»`); continue; }

    await ambReintents(
      () => classroom.courses.courseWorkMaterials.create({
        courseId: COURSE_ID,
        requestBody: {
          title: m.titol,
          description: m.descripcio,
          state: 'DRAFT',
          topicId: tema.topicId,
          materials: m.enllacos.map(l => ({ link: { url: l.url, title: l.title } })),
        },
      }), `crear material «${m.titol}»`);
    console.log(`  ✅ creat (DRAFT): ${m.titol}`);
  }

  if (senseCategoria.length) {
    console.log('\n⚠️ Categoria de nota NO assignada per l\'API (no ho permet). Assigna-la a mà:');
    for (const t of senseCategoria) console.log(`   · ${t}`);
  }
  if (creades.length) {
    fs.writeFileSync('resultats_proves_i_materials.json',
      JSON.stringify({ creat: new Date().toISOString(), creades }, null, 2));
    console.log('\n💾 Desat a resultats_proves_i_materials.json');
  }
  if (!APPLY) console.log('\n🔎 Mode descoberta. Executa amb APPLY=1 per crear-ho.');
  else console.log('\nFet. Tot en ESBORRANY.');
}

main().catch(e => {
  console.error('❌', e.message);
  const detall = e?.response?.data;
  if (detall) console.error(JSON.stringify(detall, null, 2));
  process.exit(1);
});
