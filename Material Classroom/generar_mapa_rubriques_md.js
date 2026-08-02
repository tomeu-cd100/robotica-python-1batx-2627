/*
 * Genera `Classes/00_General/00_Mapa_tasques_rubriques.md` a partir de les
 * mateixes dades que fan servir les rúbriques (`crear_rubriques_per_tasca.js`),
 * perquè el document del web i els fulls de Classroom no puguin divergir.
 *
 * Ús:  node generar_mapa_rubriques_md.js
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { RUBRIQUES, MAPA } from './crear_rubriques_per_tasca.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SORTIDA = path.join(__dirname, '..', 'Classes', '00_General', '00_Mapa_tasques_rubriques.md');

const p = [];
p.push('# 📐 Quina rúbrica avalua cada tasca');
p.push('');
p.push('> **Per a qui és?** Per al **docent i per a l\'alumnat**. Tens dret a conèixer amb '
     + 'quins criteris se t\'avalua **abans** de començar la feina: aquí hi ha, tasca per '
     + 'tasca del Google Classroom, quina rúbrica se li aplica i d\'on surt.');
p.push('');
p.push('## Per què les rúbriques estan fusionades');
p.push('');
p.push('El curs té cinc rúbriques (`Programació didàctica/07_Rubriques.md`): **R1** programació, '
     + '**R2** circuit i electrònica, **R3** projecte i robot, **R4** documentació i comunicació '
     + 'i **R5** actitud i autoregulació. Molts productes s\'avaluen amb **dues o tres alhora** '
     + '(per exemple, la mascota de la SA3 amb R1+R2+R3, i el quadern amb R4).');
p.push('');
p.push('Google Classroom, en canvi, només admet **una rúbrica per tasca**. Per això les que '
     + 'toquen a cada tasca s\'han **fusionat en una de sola de 10 punts**, conservant els '
     + 'criteris i el vocabulari originals: no hi ha cap criteri nou ni cap que desaparegui, '
     + 'només canvia com s\'agrupen. En resulten **sis rúbriques (A-F)**.');
p.push('');
p.push('## La taula');
p.push('');
p.push('| Tasca al Classroom | Rúbrica que s\'hi aplica | Fusiona | Què avalua |');
p.push('|---|---|---|---|');
for (const m of MAPA) {
  const r = m.rubrica ? RUBRIQUES[m.rubrica] : null;
  const nom = r ? `**${r.codi}** · ${r.nom.replace(/^Rúbrica \w+ · /, '')}` : '—';
  const origen = r ? r.origen : '—';
  p.push(`| ${m.tasca} | ${nom} | ${origen} | ${m.detall} |`);
}
p.push('');
p.push('> Els **qüestionaris de conceptes** no tenen rúbrica perquè **no qualifiquen mai**: '
     + 'són repàs formatiu i el formulari es corregeix sol.');
p.push('');
p.push('## Què hi ha dins de cada rúbrica');
p.push('');
for (const r of Object.values(RUBRIQUES)) {
  const total = r.criteris.reduce((s, c) => s + c.punts, 0);
  p.push(`### ${r.nom}`);
  p.push('');
  p.push(`**Fusiona:** ${r.origen} · **Total:** ${total} punts`);
  p.push('');
  p.push('| Criteri | Punts | Excel·lent vol dir… |');
  p.push('|---|---|---|');
  for (const c of r.criteris) {
    const exc = c.nivells[c.nivells.length - 1][1];
    p.push(`| ${c.titol} | ${c.punts} | ${exc} |`);
  }
  p.push('');
}
p.push('Cada criteri té els quatre nivells de sempre — **Insuficient · Suficient/Bé · Notable · '
     + 'Excel·lent** — amb 0, la meitat, tres quarts i la totalitat dels punts del criteri.');
p.push('');
p.push('## Per al docent: com s\'apliquen al Classroom');
p.push('');
p.push('Cada rúbrica és un full de càlcul a la carpeta de Drive del curs. A la tasca: '
     + '**Rúbrica → Importar des de Sheets** i triar el full que diu la taula. Els CSV '
     + 'equivalents estan versionats a `Avaluació/rubriques/` i es regeneren amb '
     + '`node Material Classroom/crear_rubriques_per_tasca.js` (aquest document també, amb '
     + '`generar_mapa_rubriques_md.js`: no l\'editis a mà).');
p.push('');
p.push('---');
p.push('');
p.push('*Mapa de tasques i rúbriques. Deriva de `Programació didàctica/07_Rubriques.md` i dels '
     + 'mapes d\'avaluació de les guies docents. Llicència CC BY-SA 4.0.*');
p.push('');

fs.writeFileSync(SORTIDA, p.join('\n'), 'utf8');
console.log(`✅ Escrit ${path.relative(path.join(__dirname, '..'), SORTIDA)}`);
console.log(`   ${MAPA.length} files de mapa · ${Object.keys(RUBRIQUES).length} rúbriques`);
