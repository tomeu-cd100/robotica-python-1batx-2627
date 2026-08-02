/*
 * Crea un Google Form (mode QÜESTIONARI, autocorrecció) per a cada banc de
 * conceptes `Classes/SAn/SAn_questionari_conceptes.md`.
 *
 * Els .md són la FONT DE VERITAT: aquest script els parseja, no re-transcriu
 * cap pregunta. A diferència del curs germà (que marca la resposta correcta en
 * negreta dins de l'opció), aquí les preguntes i les respostes viuen en DOS
 * fitxers diferents, perquè el banc de preguntes es publica a la vista alumnat
 * del web i la clau no s'hi pot filtrar:
 *   - preguntes: `Classes/SAn/SAn_questionari_conceptes.md`
 *   - claus:     `Classes/Solucionari/Questionaris_conceptes_solucions.md`
 *
 * Cada Form: 10 preguntes de resposta única amb 1 punt i correcció automàtica,
 * la pregunta oberta final (sense nota) i els camps de nom i grup. Es mou a la
 * carpeta de Drive del curs. NO s'adjunta al Classroom (això és un altre pas).
 *
 * Ús (des d'aquesta carpeta, amb CLASSROOM_SECRETS_DIR definit):
 *   node crear_questionaris_conceptes_forms.js           # descoberta: valida i no crea res
 *   APPLY=1 node crear_questionaris_conceptes_forms.js   # crea els Forms
 *   APPLY=1 SA=3 node crear_questionaris_conceptes_forms.js
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { google } from 'googleapis';
import { getAuthClient, ambReintents } from './_form_sa_lib.js';
import { DRIVE_FOLDER_ID } from './config.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CLASSES = path.join(__dirname, '..', 'Classes');
const APPLY = process.env.APPLY === '1';
const ONLY = process.env.SA ? `SA${process.env.SA}` : null;

// Treu marques de markdown per obtenir text net per al Form (Forms no en renderitza).
const net = (s) => s.replace(/\*\*/g, '').replace(/`/g, '').replace(/\s+/g, ' ').trim();

// Desindenta un bloc de codi pel seu mínim comú d'espais: dins d'un .md el codi
// va sagnat per quedar dins de l'ítem de la llista, però la sagnia RELATIVA és
// justament el que s'avalua en Python.
function dedent(linies) {
  const ambText = linies.filter(l => l.trim());
  if (!ambText.length) return [];
  const minim = Math.min(...ambText.map(l => l.match(/^ */)[0].length));
  return linies.map(l => l.slice(minim)).join('\n').replace(/^\n+|\n+$/g, '').split('\n');
}

/*
 * Parseja un banc i retorna:
 *   { titol, preguntes: [{ titol, codi, opcions[], correcta }], oberta }
 * El bloc de codi que acompanya una pregunta va a la descripció de l'ítem,
 * perquè Forms no té blocs de codi però sí text auxiliar sota l'enunciat.
 */
/*
 * Claus de correcció del solucionari (material del docent): retorna
 * { SA1: ['b','c',…], … } llegint la primera taula de lletres de cada secció.
 */
export function parseClaus(md) {
  const claus = {};
  let sa = null;
  for (const ln of md.split(/\r?\n/)) {
    const mh = ln.match(/^##\s+(SA\d)\b/);
    if (mh) { sa = mh[1]; continue; }
    if (!sa || claus[sa]) continue;
    if (ln.trim().startsWith('|')) {
      const cel = ln.split('|').map(c => c.trim()).filter(Boolean);
      if (cel.length === 10 && cel.every(c => /^[a-d]$/.test(c))) claus[sa] = cel;
    }
  }
  return claus;
}

export function parseBanc(md, clauExterna) {
  const lines = md.split(/\r?\n/);
  const h1 = (lines.find(l => l.startsWith('# ')) || '# Qüestionari').slice(2).trim();

  const preguntes = [];
  let q = null;
  let seccio = null;         // 'preguntes' | 'oberta' | 'clau' | null
  let dinsCodi = false;
  let oberta = null;
  // La clau ve del solucionari; el fitxer d'alumnat ja no en porta (si algun
  // dia n'hi tornés a haver una, es llegiria igualment com a comprovació).
  const clau = [...(clauExterna || [])];

  for (const ln of lines) {
    if (/^##\s+Preguntes/.test(ln)) { seccio = 'preguntes'; q = null; continue; }
    if (/^##\s+Pregunta oberta/.test(ln)) { seccio = 'oberta'; q = null; continue; }
    if (/^##\s+Clau/.test(ln)) { seccio = 'clau'; q = null; continue; }
    if (/^##\s/.test(ln)) { seccio = null; q = null; continue; }

    if (seccio === 'preguntes') {
      // Blocs de codi: es capturen sencers com a descripció de la pregunta.
      if (/^\s*```/.test(ln)) { dinsCodi = !dinsCodi; continue; }
      if (dinsCodi) {
        // Es guarda la línia CRUA: la desindentació es fa després, per mínim
        // comú, perquè la indentació relativa de Python no es deformi.
        if (q) q.codi.push(ln);
        continue;
      }
      const mq = ln.match(/^\s{0,3}(\d{1,2})\.\s+(.*)/);
      if (mq && Number(mq[1]) >= 1 && Number(mq[1]) <= 10) {
        q = { titol: net(mq[2]), codi: [], opcions: [], correcta: null };
        preguntes.push(q);
        continue;
      }
      const mo = ln.match(/^\s*-\s*([a-d])\)\s*(.*)/);
      if (mo && q) {
        q.opcions.push({ lletra: mo[1], text: net(mo[2]) });
        continue;
      }
      // Text de continuació de l'enunciat (p. ex. la pregunta després del codi).
      const cont = ln.trim();
      if (q && cont && !cont.startsWith('|') && !cont.startsWith('>') &&
          !cont.startsWith('---') && !q.opcions.length) {
        q.titol = `${q.titol} ${net(cont)}`.trim();
      }
      continue;
    }

    if (seccio === 'oberta') {
      const mOberta = ln.match(/^\s*\d{1,2}\.\s+(.*)/);
      if (mOberta && !oberta) oberta = net(mOberta[1]);
      else if (oberta && ln.trim() && !/^[_\s]+$/.test(ln) && !ln.startsWith('---') &&
               !ln.trim().startsWith('|')) {
        oberta = `${oberta} ${net(ln)}`.trim();
      }
      continue;
    }

    if (seccio === 'clau' && ln.trim().startsWith('|') && !clau.length) {
      const cel = ln.split('|').map(c => c.trim()).filter(Boolean);
      // La fila de capçalera és 1..10; la de dades són lletres a-d.
      if (cel.every(c => /^[a-d]$/.test(c))) clau.push(...cel);
    }
  }

  // Assigna la resposta correcta segons la clau (posició i → pregunta i) i
  // desindenta el codi pel mínim comú (la sagnia relativa de Python es manté).
  preguntes.forEach((p, i) => {
    const lletra = clau[i];
    const opcio = p.opcions.find(o => o.lletra === lletra);
    if (opcio) p.correcta = opcio.text;
    p.codi = dedent(p.codi);
  });

  return { titol: h1, preguntes, oberta, clau };
}

function validaBanc(sa, banc) {
  const problemes = [];
  if (banc.preguntes.length !== 10) problemes.push(`${banc.preguntes.length} preguntes (n'esperava 10)`);
  if (banc.clau.length !== 10) problemes.push(`clau de correcció amb ${banc.clau.length} lletres`);
  banc.preguntes.forEach((p, i) => {
    if (p.opcions.length !== 4) problemes.push(`Q${i + 1}: ${p.opcions.length} opcions`);
    if (!p.correcta) problemes.push(`Q${i + 1}: sense resposta correcta assignada`);
  });
  if (!banc.oberta) problemes.push('sense pregunta oberta');
  return problemes;
}

// Construeix les peticions batchUpdate: identificació + 10 MC amb nota + oberta.
function requests(banc) {
  const reqs = [];
  let i = 0;
  const add = (item) => reqs.push({ createItem: { item, location: { index: i++ } } });

  add({
    title: 'Nom i cognoms',
    questionItem: { question: { required: true, textQuestion: {} } },
  });
  add({
    title: 'Grup/classe',
    questionItem: { question: { required: true, textQuestion: {} } },
  });

  for (const p of banc.preguntes) {
    const item = {
      title: p.titol,
      questionItem: {
        question: {
          required: true,
          choiceQuestion: { type: 'RADIO', options: p.opcions.map(o => ({ value: o.text })) },
          grading: {
            pointValue: 1,
            correctAnswers: { answers: [{ value: p.correcta }] },
          },
        },
      },
    };
    if (p.codi.length) item.description = p.codi.join('\n');
    add(item);
  }

  if (banc.oberta) {
    add({
      title: banc.oberta,
      description: 'Pregunta oberta: no puntua, però el docent la pot comentar amb tu.',
      questionItem: { question: { required: false, textQuestion: { paragraph: true } } },
    });
  }
  return reqs;
}

async function main() {
  const auth = await getAuthClient();
  const forms = google.forms({ version: 'v1', auth });
  const drive = google.drive({ version: 'v3', auth });

  const fClaus = path.join(CLASSES, 'Solucionari', 'Questionaris_conceptes_solucions.md');
  if (!fs.existsSync(fClaus)) {
    throw new Error(`No trobo el solucionari amb les claus: ${fClaus}`);
  }
  const claus = parseClaus(fs.readFileSync(fClaus, 'utf8'));

  const resultats = [];
  for (let n = 1; n <= 9; n++) {
    const sa = `SA${n}`;
    if (ONLY && ONLY !== sa) continue;
    const f = path.join(CLASSES, sa, `${sa}_questionari_conceptes.md`);
    if (!fs.existsSync(f)) { console.log(`  ⚠ falta ${sa}`); continue; }

    const banc = parseBanc(fs.readFileSync(f, 'utf8'), claus[sa]);
    const problemes = validaBanc(sa, banc);
    if (problemes.length) {
      console.log(`  ❌ ${sa}: ${problemes.join(' · ')} — no el creo`);
      continue;
    }
    console.log(`  ✔ ${sa}: «${banc.titol}» — 10 preguntes, clau ${banc.clau.join('')}, + oberta`);

    if (!APPLY) continue;

    // Idempotència: si ja hi ha un Form amb aquest nom a la carpeta del curs,
    // no se'n crea un segon.
    const existents = await ambReintents(
      () => drive.files.list({
        q: `name = '${banc.titol.replace(/'/g, "\\'")}' and ` +
           `'${DRIVE_FOLDER_ID}' in parents and trashed = false`,
        fields: 'files(id, name)',
      }), 'buscar duplicats');
    if ((existents.data.files || []).length) {
      const dupId = existents.data.files[0].id;
      console.log(`    ⏭️ ja existeix a Drive (${dupId}) — no es duplica`);
      resultats.push({ sa, formId: dupId, edit: `https://docs.google.com/forms/d/${dupId}/edit`,
                       respon: '(ja existia)' });
      continue;
    }

    const created = await ambReintents(
      () => forms.forms.create({
        requestBody: { info: { title: banc.titol, documentTitle: banc.titol } },
      }), 'crear Form');
    const formId = created.data.formId;

    try {
      // 1) mode qüestionari (sense això, `grading` no s'accepta)
      await ambReintents(
        () => forms.forms.batchUpdate({
          formId,
          requestBody: { requests: [{
            updateSettings: {
              settings: { quizSettings: { isQuiz: true } },
              updateMask: 'quizSettings.isQuiz',
            },
          }] },
        }), 'activar mode qüestionari');

      // 2) descripció + preguntes amb nota
      await ambReintents(
        () => forms.forms.batchUpdate({
          formId,
          requestBody: {
            requests: [
              {
                updateFormInfo: {
                  info: {
                    description: 'Repàs formatiu autocorregible: NO qualifica. ' +
                      'Fes-lo sense apunts, mira la correcció i torna al material ' +
                      'del que hagis fallat.',
                  },
                  updateMask: 'description',
                },
              },
              ...requests(banc),
            ],
          },
        }), 'afegir preguntes');

      // 3) moure a la carpeta del curs
      const meta = await ambReintents(
        () => drive.files.get({ fileId: formId, fields: 'parents' }), 'llegir parents');
      await ambReintents(
        () => drive.files.update({
          fileId: formId,
          addParents: DRIVE_FOLDER_ID,
          removeParents: (meta.data.parents || []).join(','),
          fields: 'id, parents',
        }), 'moure a la carpeta');

      const info = await ambReintents(() => forms.forms.get({ formId }), 'llegir Form');
      resultats.push({ sa, formId, edit: `https://docs.google.com/forms/d/${formId}/edit`,
                       respon: info.data.responderUri });
      console.log('    ✅ creat, autocorrecció activada i mogut a Drive');
    } catch (e) {
      console.log(`    🧹 Error a mig fer: esborrant el Form orfe ${formId}...`);
      try { await drive.files.delete({ fileId: formId }); }
      catch (e2) { console.log(`    ⚠️ No s'ha pogut esborrar: ${e2.message}`); }
      throw e;
    }
  }

  if (resultats.length) {
    fs.writeFileSync('resultats_questionaris_conceptes.json',
      JSON.stringify({ creat: new Date().toISOString(), resultats }, null, 2));
    console.log('\n=== Forms ===');
    for (const r of resultats) console.log(`${r.sa}: ${r.edit}\n     respon: ${r.respon}`);
    console.log('\n💾 Desat a resultats_questionaris_conceptes.json');
  }
  if (!APPLY) console.log('\n🔎 Mode descoberta. Executa amb APPLY=1 per crear-los.');
}

// Permet importar el parser des d'altres scripts sense executar res.
if (process.argv[1] && process.argv[1].endsWith('crear_questionaris_conceptes_forms.js')) {
  main().catch(e => {
    console.error('❌', e.message);
    const detall = e?.response?.data;
    if (detall) console.error(JSON.stringify(detall, null, 2));
    process.exit(1);
  });
}
