/*
 * Rúbriques UNIFICADES, una per tasca de Classroom.
 *
 * El material del curs avalua cada producte amb diverses rúbriques alhora
 * (p. ex. el producte de la SA3 amb R1+R2+R3, i el quadern amb R4), però una
 * tasca de Classroom només admet UNA rúbrica. Per això aquí es fonen les
 * rúbriques que toquen a cada tasca en una de sola de 10 punts, conservant els
 * criteris de `Programació didàctica/07_Rubriques.md` i el seu vocabulari.
 *
 * Surten 6 rúbriques unificades (A-F) que cobreixen les 12 tasques amb nota.
 * Els qüestionaris de conceptes no en tenen: no qualifiquen.
 *
 * Cada rúbrica es desa com a CSV versionat a `Avaluació/rubriques/` i es puja a
 * Drive com a full de càlcul importable (l'API de rúbriques demana Education
 * Plus, que aquest compte no té). A més, es crea al Classroom el material
 * «Quina rúbrica avalua cada tasca» amb el document del web i tots els fulls.
 *
 * Ús (amb CLASSROOM_SECRETS_DIR definit):
 *   node crear_rubriques_per_tasca.js           # escriu els CSV i fa descoberta
 *   APPLY=1 node crear_rubriques_per_tasca.js   # puja els fulls i crea el material
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { google } from 'googleapis';
import { getAuthClient, ambReintents } from './_form_sa_lib.js';
import { COURSE_ID, DRIVE_FOLDER_ID, WEB_BASE } from './config.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const APPLY = process.env.APPLY === '1';
const DIR_CSV = path.join(__dirname, '..', 'Avaluació', 'rubriques');
const TEMA_GENERAL = '00 · General (com funciona el curs)';
const PAGINA_MAPA = `${WEB_BASE}/00-general/00-mapa-tasques-rubriques.html`;

// --- Criteris reutilitzables (text de 07_Rubriques.md, punts parametritzats) --
const C = {
  funcionament: (p) => ({
    titol: 'Funcionament (R1)',
    desc: 'El producte fa el que ha de fer amb el maquinari real.',
    nivells: [
      ['Insuficient', 'No s\'executa o no fa la tasca.'],
      ['Suficient/Bé', 'Fa la tasca bàsica amb errors menors.'],
      ['Notable', 'Fa la tasca completa de manera fiable.'],
      ['Excel·lent', 'Funciona i gestiona casos límit o errors.'],
    ],
    punts: p,
  }),
  codiPropi: (p) => ({
    titol: 'Codi escrit per tu (R1)',
    desc: 'Estructures i decisions pròpies, no una còpia adaptada de l\'exemple. '
      + 'Es comprova amb dues preguntes sobre el codi lliurat (07_Rubriques.md, P3.11).',
    nivells: [
      ['Insuficient', 'Còpia gairebé literal del codi de base, sense adaptar.'],
      ['Suficient/Bé', 'Adapta la base amb canvis mínims (noms, valors).'],
      ['Notable', 'Estructures pròpies i adaptacions no trivials.'],
      ['Excel·lent', 'Disseny propi identificable, amb decisions justificades.'],
    ],
    punts: p,
  }),
  llegibilitat: (p) => ({
    titol: 'Llegibilitat i depuració (R1)',
    desc: 'Comentaris, noms significatius i capacitat d\'explicar els errors resolts.',
    nivells: [
      ['Insuficient', 'Sense comentaris ni noms clars; no identifica errors.'],
      ['Suficient/Bé', 'Comentaris escassos; corregeix amb ajuda.'],
      ['Notable', 'Comentat, noms significatius, depura sol.'],
      ['Excel·lent', 'Documentat amb cura i explica la causa de l\'error.'],
    ],
    punts: p,
  }),
  muntatge: (p) => ({
    titol: 'Muntatge i seguretat (R2)',
    desc: 'Cablatge correcte segons l\'esquema de pins del curs i normes de seguretat.',
    nivells: [
      ['Insuficient', 'Connexions incorrectes o insegures.'],
      ['Suficient/Bé', 'Funciona amb ajuda; aplica les normes amb recordatoris.'],
      ['Notable', 'Muntatge correcte i ordenat; aplica les normes.'],
      ['Excel·lent', 'Muntatge òptim i net; model de bones pràctiques.'],
    ],
    punts: p,
  }),
  integracio: (p) => ({
    titol: 'Compliment del repte i integració (R3)',
    desc: 'Assoliment dels objectius (inclòs el repte ⭐ obligatori) i integració amb '
      + 'el que ja tenies muntat i programat.',
    nivells: [
      ['Insuficient', 'No assoleix els objectius; parts inconnexes.'],
      ['Suficient/Bé', 'Assoleix els mínims; integració parcial.'],
      ['Notable', 'Assoleix tots els objectius; sistema coherent.'],
      ['Excel·lent', 'Supera els objectius amb millores; integració robusta.'],
    ],
    punts: p,
  }),
  quadern: (p) => ({
    titol: 'Quadern i comunicació (R4)',
    desc: 'Entrada de la SA: predicció, procés, error documentat amb DEPURA i millora; '
      + 'i la mini-defensa si et toca per mostreig.',
    nivells: [
      ['Insuficient', 'Incomplet o confús.'],
      ['Suficient/Bé', 'Bàsic, comprensible amb llacunes.'],
      ['Notable', 'Complet, ordenat i clar.'],
      ['Excel·lent', 'Exhaustiu i reflexiu, amb terminologia precisa.'],
    ],
    punts: p,
  }),
  dossierDefensa: (p) => ({
    titol: 'Dossier tècnic i defensa oral (R4)',
    desc: 'Dossier complet (les 9 seccions) i defensa individual amb demostració: '
      + 'claredat, decisió tècnica justificada i resposta a preguntes.',
    nivells: [
      ['Insuficient', 'Dossier incomplet; no defensa la solució.'],
      ['Suficient/Bé', 'Dossier bàsic; defensa amb dificultats.'],
      ['Notable', 'Dossier complet i ordenat; defensa clara.'],
      ['Excel·lent', 'Dossier exhaustiu i reflexiu; defensa convincent i respon dubtes.'],
    ],
    punts: p,
  }),
  procesR5: (p) => ({
    titol: 'Autonomia i procés (R5)',
    desc: 'Constància, autoregulació, DEPURA abans de demanar ajuda i ús declarat de la IA.',
    nivells: [
      ['Insuficient', 'Depèn contínuament d\'ajuda; no documenta el procés.'],
      ['Suficient/Bé', 'Avança amb suport; procés registrat de forma irregular.'],
      ['Notable', 'Treballa amb autonomia i registra el procés.'],
      ['Excel·lent', 'Autonomia plena, iteració documentada i ús honest i declarat de la IA.'],
    ],
    punts: p,
  }),
  // Criteris propis de la tasca de quadern trimestral (R4 sencera).
  quadernComplet: (p) => ({
    titol: 'Completesa i constància (R4)',
    desc: 'Una entrada per SA del trimestre, escrita durant el curs i no el darrer dia.',
    nivells: [
      ['Insuficient', 'Falten entrades o són de dues ratlles.'],
      ['Suficient/Bé', 'Hi són gairebé totes, desiguals.'],
      ['Notable', 'Totes les entrades, completes i ordenades.'],
      ['Excel·lent', 'Totes, amb els 6 apartats i evidència d\'escriptura continuada.'],
    ],
    punts: p,
  }),
  quadernClaredat: (p) => ({
    titol: 'Claredat tècnica (R4)',
    desc: 'S\'entén què has fet i per què, amb esquemes o pseudocodi quan calen.',
    nivells: [
      ['Insuficient', 'Confús.'],
      ['Suficient/Bé', 'Comprensible amb llacunes.'],
      ['Notable', 'Clar i rigorós.'],
      ['Excel·lent', 'Rigorós, precís i ben argumentat.'],
    ],
    punts: p,
  }),
  quadernErrors: (p) => ({
    titol: 'Errors documentats amb DEPURA (R4)',
    desc: 'Què fallava, com ho vas trobar i com ho vas resoldre. Amagar errors no puja la nota.',
    nivells: [
      ['Insuficient', 'Cap error documentat.'],
      ['Suficient/Bé', 'Els menciona sense explicar com els va resoldre.'],
      ['Notable', 'Errors reals amb la rutina DEPURA aplicada.'],
      ['Excel·lent', 'Explica la causa i què fa diferent des de llavors.'],
    ],
    punts: p,
  }),
  quadernTerminologia: (p) => ({
    titol: 'Terminologia i ús de la IA (R4)',
    desc: 'Vocabulari tècnic correcte i declaració honesta de l\'ús d\'assistents d\'IA.',
    nivells: [
      ['Insuficient', 'Terminologia incorrecta; ús d\'IA no declarat.'],
      ['Suficient/Bé', 'Terminologia bàsica; declaració incompleta.'],
      ['Notable', 'Terminologia adequada i ús declarat.'],
      ['Excel·lent', 'Terminologia precisa i reflexió sobre què li ha aportat la IA.'],
    ],
    punts: p,
  }),
};

// --- Les 6 rúbriques unificades ----------------------------------------------
export const RUBRIQUES = {
  A: {
    codi: 'A', fitxer: 'Rubrica_A_codi_i_quadern.csv',
    nom: 'Rúbrica A · Producte de codi + quadern (R1+R4)',
    origen: 'R1 + R4',
    criteris: [C.funcionament(3), C.codiPropi(3), C.llegibilitat(2), C.quadern(2)],
  },
  B: {
    codi: 'B', fitxer: 'Rubrica_B_codi_muntatge_quadern.csv',
    nom: 'Rúbrica B · Producte amb muntatge (R1+R2+R4)',
    origen: 'R1 + R2 + R4',
    criteris: [C.funcionament(2.5), C.codiPropi(2.5), C.muntatge(2), C.llegibilitat(1.5), C.quadern(1.5)],
  },
  C: {
    codi: 'C', fitxer: 'Rubrica_C_codi_muntatge_projecte_quadern.csv',
    nom: 'Rúbrica C · Producte que tanca projecte, amb muntatge (R1+R2+R3+R4)',
    origen: 'R1 + R2 + R3 + R4',
    criteris: [C.funcionament(2), C.codiPropi(2.5), C.muntatge(1.5), C.integracio(2), C.quadern(2)],
  },
  D: {
    codi: 'D', fitxer: 'Rubrica_D_codi_projecte_quadern.csv',
    nom: 'Rúbrica D · Producte de sistema (R1+R3+R4)',
    origen: 'R1 + R3 + R4',
    criteris: [C.funcionament(2), C.codiPropi(2.5), C.llegibilitat(1.5), C.integracio(2), C.quadern(2)],
  },
  E: {
    codi: 'E', fitxer: 'Rubrica_E_projecte_final.csv',
    nom: 'Rúbrica E · Projecte final SA9 (R1+R2+R3+R4+R5)',
    origen: 'R1 + R2 + R3 + R4 + R5',
    criteris: [C.funcionament(2), C.codiPropi(2), C.muntatge(1), C.integracio(2),
               C.dossierDefensa(2), C.procesR5(1)],
  },
  F: {
    codi: 'F', fitxer: 'Rubrica_F_quadern_trimestral.csv',
    nom: 'Rúbrica F · Quadern tècnic del trimestre (R4)',
    origen: 'R4',
    criteris: [C.quadernComplet(3), C.quadernClaredat(3), C.quadernErrors(2), C.quadernTerminologia(2)],
  },
};

// --- Quina rúbrica va a cada tasca -------------------------------------------
export const MAPA = [
  { tasca: 'SA1 · Lliurament del producte', rubrica: 'A',
    detall: 'Fitxa-pòster (R4) + repte ⭐ «targeta de benvinguda» (R1) + entrada del quadern (R4).' },
  { tasca: 'SA2 · Lliurament del producte', rubrica: 'B',
    detall: 'Semàfor/llum d\'ambient (R1+R2) + repte ⭐ (R1) + muntatge de la mascota (R2) + quadern (R4).' },
  { tasca: 'SA3 · Lliurament del producte', rubrica: 'C',
    detall: 'Mascota reactiva, que tanca el Projecte T1 (R1+R2+R3) + repte ⭐ (R1) + quadern (R4).' },
  { tasca: 'SA4 · Lliurament del producte', rubrica: 'B',
    detall: 'Control per botons (R1+R2) + repte ⭐ (R1) + muntatge del vehicle (R2) + quadern (R4).' },
  { tasca: 'SA5 · Lliurament del producte', rubrica: 'A',
    detall: 'Control remot per ràdio (R1) + repte ⭐ (R1) + mini-defensa i quadern (R4).' },
  { tasca: 'SA6 · Lliurament del producte', rubrica: 'D',
    detall: 'Vehicle amb aturada d\'emergència, que tanca el Projecte T2 (R1+R3) + repte ⭐ (R1) + quadern (R4).' },
  { tasca: 'SA7 · Lliurament del producte', rubrica: 'D',
    detall: 'Comportament autònom del rover (R1+R3) + repte ⭐ (R1) + quadern (R4).' },
  { tasca: 'SA8 · Lliurament del producte', rubrica: 'D',
    detall: 'Telemetria del rover (R1+R3) + repte ⭐ (R1) + mini-defensa i quadern (R4).' },
  { tasca: 'SA9 · Lliurament del producte', rubrica: 'E',
    detall: 'Rover ampliat (R1+R2+R3) + dossier tècnic (R4) + defensa oral (R4·DO) + procés (R5).' },
  { tasca: '📓 Quadern tècnic — T1', rubrica: 'F', detall: 'Quadern sencer del trimestre (R4).' },
  { tasca: '📓 Quadern tècnic — T2', rubrica: 'F', detall: 'Quadern sencer del trimestre (R4).' },
  { tasca: '📓 Quadern tècnic — T3', rubrica: 'F', detall: 'Quadern sencer del trimestre (R4).' },
  { tasca: '📝 Prova pràctica T1 / T2 / T3', rubrica: null,
    detall: 'No porta rúbrica de nivells: es corregeix amb la **graella d\'ítems** del seu '
      + 'enunciat (10 punts), que ja diu quants punts val cada ítem i quin criteri avalua '
      + '(T1 → R1+R2+R4 · T2 → R1+R3+R4 · T3 → R1+R3). És més precisa que una rúbrica per a '
      + 'una prova amb ítems tancats.' },
  { tasca: '🎯 Millor mini-check del trimestre', rubrica: null,
    detall: 'Sense rúbrica: la nota surt de l\'escala de semàfors del mini-check '
      + '(🟢 9-10 · 🟡 6-8 · 🟠 4-5 · 🔴 1-3), aplicada al MILLOR mini-check del trimestre.' },
  { tasca: 'SAn · Qüestionari de conceptes', rubrica: null,
    detall: 'Sense rúbrica: és repàs formatiu i no qualifica mai. El Form es corregeix sol.' },
];

function escriuCSV(r) {
  const esc = (s) => `"${String(s).replace(/"/g, '""')}"`;
  const files = [['Criterion Title', 'Criterion Description', 'Level Title', 'Level Description', 'Points']];
  for (const c of r.criteris) {
    // Nivells: 0 · meitat · tres quarts · màxim dels punts del criteri.
    const escala = [0, c.punts / 2, c.punts * 0.75, c.punts];
    c.nivells.forEach(([titol, desc], i) => {
      files.push([c.titol, c.desc, titol, desc, Number(escala[i].toFixed(2))]);
    });
  }
  fs.mkdirSync(DIR_CSV, { recursive: true });
  fs.writeFileSync(path.join(DIR_CSV, r.fitxer),
    files.map(f => f.map(esc).join(',')).join('\n') + '\n', 'utf8');
  const total = r.criteris.reduce((s, c) => s + c.punts, 0);
  console.log(`  ✔ ${r.nom} — ${r.criteris.length} criteris, ${total} punts → Avaluació/rubriques/${r.fitxer}`);
  if (Math.abs(total - 10) > 0.001) console.log(`     ⚠️ ATENCIÓ: no suma 10 punts (${total})`);
}

async function pujaFull(drive, r) {
  const nom = r.nom;
  const existents = await ambReintents(
    () => drive.files.list({
      q: `name = '${nom.replace(/'/g, "\\'")}' and '${DRIVE_FOLDER_ID}' in parents and trashed = false`,
      fields: 'files(id, name, webViewLink)',
    }), 'buscar el full');
  const trobat = (existents.data.files || [])[0];
  if (trobat) { console.log(`  ↷ ja a Drive: ${nom}`); return trobat; }
  const creat = await ambReintents(
    () => drive.files.create({
      requestBody: { name: nom, mimeType: 'application/vnd.google-apps.spreadsheet',
                     parents: [DRIVE_FOLDER_ID] },
      media: { mimeType: 'text/csv', body: fs.createReadStream(path.join(DIR_CSV, r.fitxer)) },
      fields: 'id, name, webViewLink',
    }), 'pujar el full');
  console.log(`  ✅ pujat: ${nom}`);
  return creat.data;
}

async function main() {
  console.log('=== Rúbriques unificades (CSV versionats) ===');
  for (const r of Object.values(RUBRIQUES)) escriuCSV(r);

  if (!APPLY) {
    console.log('\n🔎 Mode descoberta: amb APPLY=1 es pugen els fulls a Drive i es crea el material.');
    return;
  }

  const auth = await getAuthClient();
  const drive = google.drive({ version: 'v3', auth });
  const classroom = google.classroom({ version: 'v1', auth });

  console.log('\n=== Fulls importables a Drive ===');
  const fulls = {};
  for (const r of Object.values(RUBRIQUES)) fulls[r.codi] = await pujaFull(drive, r);

  // Material del Classroom amb el document del web i tots els fulls.
  const titol = '📐 Quina rúbrica avalua cada tasca (i com importar-la)';
  const existents = new Set();
  let pageToken;
  do {
    const res = await ambReintents(
      () => classroom.courses.courseWorkMaterials.list({
        courseId: COURSE_ID, courseWorkMaterialStates: ['PUBLISHED', 'DRAFT'],
        pageSize: 100, pageToken,
      }), 'llistar materials');
    for (const m of res.data.courseWorkMaterial || []) existents.add(m.title);
    pageToken = res.data.nextPageToken;
  } while (pageToken);

  if (existents.has(titol)) {
    console.log(`\n↷ El material ja existeix: ${titol}`);
  } else {
    const topicsRes = await ambReintents(
      () => classroom.courses.topics.list({ courseId: COURSE_ID, pageSize: 100 }), 'llistar temes');
    const general = (topicsRes.data.topic || []).find(tp => tp.name === TEMA_GENERAL);
    if (!general) throw new Error(`No trobo el tema «${TEMA_GENERAL}»`);

    const enllacos = [{ link: { url: PAGINA_MAPA, title: 'Taula: quina rúbrica avalua cada tasca' } }];
    for (const r of Object.values(RUBRIQUES)) {
      enllacos.push({ link: { url: fulls[r.codi].webViewLink, title: r.nom } });
    }
    const cw = await ambReintents(
      () => classroom.courses.courseWorkMaterials.create({
        courseId: COURSE_ID,
        requestBody: {
          title: titol,
          description:
            'Cada tasca amb nota s\'avalua amb UNA rúbrica de 10 punts. Com que el ' +
            'material del curs avalua alguns productes amb dues o tres rúbriques ' +
            '(R1, R2, R3, R4, R5), aquí estan fusionades en sis rúbriques (A-F): la ' +
            'taula diu quina toca a cada tasca i cada full és importable a Classroom ' +
            'des de la tasca (Rúbrica → Importar des de Sheets).',
          state: 'DRAFT',
          topicId: general.topicId,
          materials: enllacos,
        },
      }), 'crear el material del mapa de rúbriques');
    console.log(`\n✅ Material creat (DRAFT): ${titol}`);
    fs.writeFileSync('resultats_rubriques_per_tasca.json', JSON.stringify({
      creat: new Date().toISOString(),
      material: cw.data.id,
      fulls: Object.fromEntries(Object.entries(fulls).map(([k, v]) => [k, v.webViewLink])),
    }, null, 2));
    console.log('💾 Desat a resultats_rubriques_per_tasca.json');
  }

  console.log('\n👉 A cada tasca: Rúbrica → Importar des de Sheets → tria el full que diu la taula.');
}

if (process.argv[1] && process.argv[1].endsWith('crear_rubriques_per_tasca.js')) {
  main().catch(e => {
    console.error('❌', e.message);
    const detall = e?.response?.data;
    if (detall) console.error(JSON.stringify(detall, null, 2));
    process.exit(1);
  });
}
