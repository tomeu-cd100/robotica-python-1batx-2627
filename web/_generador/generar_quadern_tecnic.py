# -*- coding: utf-8 -*-
"""Genera els 3 quaderns tècnics imprimibles (un PDF per trimestre).

Una pàgina A4 per hora lectiva: imprès a doble cara, cada sessió de 2 h
ocupa un full físic (davant = 1a hora amb objectius i vocabulari impresos;
darrere = 2a hora amb el ritual de tancament: error del dia + autoavaluació
semàfor). La darrera sessió del trimestre és el full de la prova pràctica,
amb el pla de millora personal al darrere (reflexió final de curs al T3).

Dades: `quadern_sessions.py` (vigilat per `tools/qa.py`).
Sortida: Classes/00_General/pdf/Quadern_tecnic_T{1,2,3}.pdf

Ús:
    py web/_generador/generar_quadern_tecnic.py
"""
from __future__ import annotations

import html
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generar import PAGES_BASE  # noqa: E402
from generar_fulls_imprimibles import find_browser, print_pdf  # noqa: E402
from generador.pdfutil import escriu_marca, hash_font  # noqa: E402
from quadern_sessions import PROVES, SA_TRIMESTRE, SESSIONS  # noqa: E402

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parent.parent
DESTI = REPO / "Classes" / "00_General" / "pdf"

CSS = """
  @page { size: A4; margin: 11mm 12mm 10mm; }
  * { box-sizing: border-box; print-color-adjust: exact;
      -webkit-print-color-adjust: exact; }
  html, body { margin: 0; padding: 0; }
  body { font-family: "Segoe UI", Arial, sans-serif; color: #111;
         font-size: 10.5pt; line-height: 1.35; }
  .page { height: 273mm; display: flex; flex-direction: column;
          overflow: hidden; page-break-after: always; }
  .page:last-child { page-break-after: auto; }
  /* Capçalera de pàgina */
  .cap { border-bottom: 2px solid #2b8ac6; padding-bottom: 3pt; margin-bottom: 5pt; }
  .cap .fila { display: flex; justify-content: space-between; align-items: baseline; }
  .cap .marca { font-size: 8.5pt; letter-spacing: .06em; color: #2b8ac6;
                font-weight: 700; text-transform: uppercase; }
  .cap .num { font-size: 8.5pt; color: #555; }
  .cap .titol { font-size: 12.5pt; font-weight: 700; margin-top: 1pt; }
  .cap .data { font-size: 9.5pt; color: #333; white-space: nowrap; }
  .cap .data .ratlla { display: inline-block; width: 80pt;
                       border-bottom: 1px solid #333; }
  /* Caixa objectius + vocabulari */
  .avui { background: #f2f8fc; border: 1px solid #cfe3f0; border-radius: 4px;
          padding: 4pt 8pt; margin: 0 0 5pt; font-size: 9.6pt; }
  .avui div { margin: 1.5pt 0; }
  .avui code, .vocab { font-family: inherit; }
  /* Quadrícula de punts (5 mm): files de «·» — text vectorial al PDF */
  .dots { flex: 1 1 auto; border: 1px solid #dfe6ea; border-radius: 4px;
          overflow: hidden; padding-left: 1.4mm; }
  .dots .df { font-family: Consolas, "Courier New", monospace; color: #b9c4cc;
              font-size: 8pt; line-height: 5mm; height: 5mm;
              letter-spacing: 3.45mm; white-space: nowrap; }
  .etiq { font-size: 8pt; color: #8a97a0; text-transform: uppercase;
          letter-spacing: .05em; margin: 3pt 0 2pt; }
  /* Peu de tancament (darrere del full) */
  .peu { margin-top: 5pt; }
  .caixa { border: 1px solid #c9d4db; border-radius: 4px; padding: 5pt 8pt;
           margin: 4pt 0; page-break-inside: avoid; }
  .caixa .t { font-weight: 700; font-size: 9.8pt; margin-bottom: 3pt; }
  .linia { display: flex; align-items: flex-end; gap: 6pt; margin: 6pt 0; }
  .linia .et { white-space: nowrap; font-size: 9.5pt; }
  .linia .r { flex: 1 1 auto; border-bottom: 1px solid #555; height: 13pt; }
  /* Graella semàfor (com als checklists) */
  table.sem { width: 100%; border-collapse: collapse; margin: 4pt 0; }
  table.sem th, table.sem td { border: 1px solid #bbb; padding: 3.5pt 6pt;
                               font-size: 9.5pt; }
  table.sem thead th { background: #eef3f7; text-align: center; width: 11%; }
  table.sem thead th:first-child { text-align: left; width: auto; }
  table.sem td.paint { height: 16pt; }
  /* Portada */
  .portada { justify-content: flex-start; }
  .portada .logo { font-size: 42pt; text-align: center; margin-top: 22mm; }
  .portada h1 { font-size: 25pt; text-align: center; margin: 4pt 0 2pt; }
  .portada .sub { text-align: center; font-size: 13pt; color: #2b8ac6;
                  font-weight: 600; margin-bottom: 14mm; }
  .portada .camps { width: 75%; margin: 0 auto 10mm; }
  .portada .camps .linia .et { font-weight: 600; }
  .destacat { background: #f6fbfe; border: 1.5px solid #2b8ac6; border-radius: 6px;
              padding: 8pt 12pt; margin: 0 auto; width: 85%; font-size: 10.5pt; }
  .destacat .t { font-weight: 700; margin-bottom: 3pt; }
  .peu-portada { margin-top: auto; text-align: center; font-size: 9pt;
                 color: #8a97a0; }
  /* Índex i pàgina d'instruccions */
  h2 { font-size: 12pt; margin: 8pt 0 4pt; padding-bottom: 2pt;
       border-bottom: 1px solid #ccc; }
  table.idx { width: 100%; border-collapse: collapse; margin: 4pt 0; }
  table.idx th, table.idx td { border: 1px solid #ccc; padding: 3pt 6pt;
                               font-size: 9.3pt; text-align: left; }
  table.idx thead th { background: #eef3f7; }
  table.idx td.c { width: 15%; }
  ol.regles { margin: 4pt 0; padding-left: 20pt; }
  ol.regles li { margin: 4pt 0; }
  ul.plain { margin: 4pt 0; padding-left: 18pt; }
  ul.plain li { margin: 3pt 0; }
  .callout { background: #eaf4fb; border-left: 4px solid #2b8ac6;
             padding: 5pt 9pt; margin: 6pt 0; font-size: 9.8pt; }
  strong { font-weight: 700; }
"""


# Quadrícula de punts cada 5 mm: files de caràcters «·». El text queda
# VECTORIAL al PDF (gradients i SVG es rasteritzen i el fitxer es dispara).
# El nombre de files es tria perquè el darrer renglo càpiga SENCER dins la
# caixa (`.dots`, alçada constant a cada tipus de pàgina); si sobren files,
# `overflow:hidden` tallava l'última pel mig i el marc «es tallava».
# Alçades mesurades de la caixa: davant ~237 mm · darrere ~193 mm · prova
# davant ~232 mm (5 mm per fila → deixa ~2 mm de marge fins al marc).
DOTS_DAVANT = 47
DOTS_DARRERE = 38
DOTS_PROVA_DAVANT = 46


def dots(files: int) -> str:
    return '<div class="dots">' + ('<div class="df">' + "·" * 37 + "</div>") * files + "</div>"


def esc(t: str) -> str:
    return html.escape(t, quote=False)


def cap_sessio(t: int, i: int, total: int, s: dict, continuacio: bool = False) -> str:
    """Capçalera d'una pàgina de sessió."""
    seg = " · 2a hora" if continuacio else ""
    data = ('' if continuacio else
            '<span class="data">Data: <span class="ratlla"></span></span>')
    return (f'<div class="cap"><div class="fila">'
            f'<span class="marca">📓 Quadern tècnic · Trimestre {t}</span>'
            f'<span class="num">Sessió {i} de {total}{seg}</span></div>'
            f'<div class="fila"><span class="titol">{s["sa"]} · S{s["s"]} — '
            f'{esc(s["titol"])}</span>{data}</div></div>')


def peu_tancament(pendent: bool = True) -> str:
    """Ritual de tancament: error del dia + semàfor + pendent."""
    parts = [
        '<div class="peu">',
        '<div class="caixa"><div class="t">🐞 Error del dia (rutina DEPURA) — '
        'un error ben documentat suma nota</div>',
        '<div class="linia"><span class="et">Què passava?</span><span class="r"></span></div>',
        '<div class="linia"><span class="et">Com l\'he trobat?</span><span class="r"></span></div>',
        '<div class="linia"><span class="et">Com l\'he resolt? Quina estratègia m\'ha servit?</span><span class="r"></span></div></div>',
        '<table class="sem"><thead><tr><th>Autoavaluació d\'avui (pinta\'n un)</th>'
        '<th>🔴</th><th>🟡</th><th>🟢</th></tr></thead><tbody>',
        '<tr><td>He entès el que hem treballat</td>'
        '<td class="paint"></td><td class="paint"></td><td class="paint"></td></tr>',
        '<tr><td>Ho sé fer tot sol/a</td>'
        '<td class="paint"></td><td class="paint"></td><td class="paint"></td></tr>',
        '</tbody></table>',
    ]
    if pendent:
        parts.append('<div class="linia"><span class="et">Em queda pendent de '
                     'repassar:</span><span class="r"></span></div>')
    parts.append('</div>')
    return "".join(parts)


def pagines_sessio(t: int, i: int, total: int, s: dict) -> list[str]:
    """Full d'una sessió normal: davant (1a hora) + darrere (2a hora)."""
    davant = (
        f'<div class="page">{cap_sessio(t, i, total, s)}'
        f'<div class="avui"><div>🎯 <strong>Avui:</strong> {esc(s["avui"])}</div>'
        f'<div>📚 <strong>Vocabulari:</strong> <span class="vocab">{esc(s["vocab"])}</span></div></div>'
        f'<div class="etiq">✍️ Apunts · esquemes · pseudocodi (esquemes i '
        f'diagrames, a mà i amb retolador fi)</div>'
        f'{dots(DOTS_DAVANT)}</div>')
    darrere = (
        f'<div class="page">{cap_sessio(t, i, total, s, continuacio=True)}'
        f'{dots(DOTS_DARRERE)}'
        f'{peu_tancament()}</div>')
    return [davant, darrere]


def pagines_prova(t: int, i: int, total: int, s: dict) -> list[str]:
    """Full de la prova pràctica: full de treball + pla de millora/reflexió."""
    p = PROVES[t]
    cap = (f'<div class="cap"><div class="fila">'
           f'<span class="marca">📓 Quadern tècnic · Trimestre {t}</span>'
           f'<span class="num">Sessió {i} de {total} · PROVA</span></div>'
           f'<div class="fila"><span class="titol">🧪 Prova pràctica T{t} — '
           f'«{esc(p["titol"])}»</span>'
           f'<span class="data">Data: <span class="ratlla"></span></span></div></div>')
    davant = (
        f'<div class="page">{cap}'
        f'<div class="callout"><strong>Pots consultar aquest quadern i els '
        f'esquemes durant la prova.</strong> Material: {esc(p["material"])}. '
        f'La prova és per nivells: el nucli ben fet és un 5-6; cada ampliació '
        f'puja cap al 7-10.</div>'
        f'<div class="etiq">✍️ Full de treball de la prova (esquema · '
        f'pseudocodi · càlculs · anotacions)</div>'
        f'{dots(DOTS_PROVA_DAVANT)}</div>')

    if p["reflexio_final"]:
        cos = (
            '<div class="caixa"><div class="t">🎓 Reflexió final de curs '
            '(3 línies — tanca el quadern com el vas obrir: mirant el procés, '
            'no només la nota)</div>'
            '<div class="linia"><span class="et">1 · La competència de què estic més '
            'orgullós/osa:</span><span class="r"></span></div>'
            '<div class="linia"><span class="et">2 · El que encara em costa:</span>'
            '<span class="r"></span></div>'
            '<div class="linia"><span class="et">3 · On ho continuaré (batxillerat, TR, '
            'projecte propi…):</span><span class="r"></span></div></div>')
    else:
        cos = (
            f'<div class="caixa"><div class="t">📈 Pla de millora personal '
            f'(escriu-lo quan rebis el retorn de la prova — es reprèn a l\'inici '
            f'de la SA següent)</div>'
            f'<div class="linia"><span class="et">1 · Què m\'ha fallat o m\'ha costat '
            f'més:</span><span class="r"></span></div>'
            f'<div class="linia"><span class="et">2 · Què practicaré concretament:</span>'
            f'<span class="r"></span></div>'
            f'<div class="linia"><span class="et">3 · Com comprovaré que ja ho tinc:</span>'
            f'<span class="r"></span></div></div>')
    balanc = (
        '<table class="sem"><thead><tr><th>Balanç del trimestre (pinta\'n un '
        'per fila)</th><th>🔴</th><th>🟡</th><th>🟢</th></tr></thead><tbody>'
        '<tr><td>Programació (R1)</td><td class="paint"></td><td class="paint">'
        '</td><td class="paint"></td></tr>'
        '<tr><td>Circuits i muntatge (R2/R3)</td><td class="paint"></td>'
        '<td class="paint"></td><td class="paint"></td></tr>'
        '<tr><td>El meu quadern tècnic (R4)</td><td class="paint"></td>'
        '<td class="paint"></td><td class="paint"></td></tr></tbody></table>')
    darrere = (
        f'<div class="page">{cap_sessio(t, i, total, s, continuacio=True)}'
        f'{dots(DOTS_DARRERE)}'
        f'<div class="peu">{cos}{balanc}</div></div>')
    return [davant, darrere]


def portada(t: int, sessions: list[dict]) -> str:
    sas = " · ".join(f"<strong>{sa}</strong> {esc(nom)}"
                     for sa, nom in SA_TRIMESTRE[t])
    return (
        f'<div class="page portada"><div class="logo">📓</div>'
        f'<h1>Quadern tècnic</h1>'
        f'<div class="sub">Robòtica · 1r de Batxillerat · Trimestre {t}</div>'
        f'<div class="camps">'
        f'<div class="linia"><span class="et">Nom i cognoms</span><span class="r"></span></div>'
        f'<div class="linia"><span class="et">Grup</span><span class="r"></span>'
        f'<span class="et">Curs</span><span class="r"></span></div></div>'
        f'<div class="destacat"><div class="t">Aquest quadern és el teu '
        f'material permès a la prova del trimestre.</div>'
        f'És el <strong>25 % de la nota</strong> (rúbrica R4). Escriu-hi cada '
        f'sessió, no tot al final: un quadern ben portat és el teu millor '
        f'aliat el dia de la prova.<br><br>'
        f'<strong>Aquest trimestre:</strong> {sas}.</div>'
        f'<div class="peu-portada">Tot el material del curs: '
        f'{PAGES_BASE.removeprefix("https://")}</div></div>')


def pagina_us(t: int, sessions: list[dict]) -> str:
    files = "".join(
        f'<tr><td class="c"><strong>{s["sa"]} · S{s["s"]}</strong></td>'
        f'<td>{"🧪 " if s["prova"] else ""}{esc(s["titol"])}</td>'
        f'<td class="c"></td></tr>' for s in sessions)
    return (
        '<div class="page"><div class="cap"><div class="fila">'
        f'<span class="marca">📓 Quadern tècnic · Trimestre {t}</span></div>'
        '<div class="fila"><span class="titol">Com s\'usa i com s\'avalua</span>'
        '</div></div>'
        '<h2>Les 5 regles</h2><ol class="regles">'
        '<li><strong>Un full per sessió:</strong> davant a la 1a hora, darrere '
        'a la 2a. Els objectius i el vocabulari ja hi són impresos.</li>'
        '<li><strong>Escriu a cada sessió, no tot al final.</strong> 2-3 minuts '
        'després de cada part és suficient.</li>'
        '<li><strong>Els esquemes i diagrames, a mà</strong> sobre la '
        'quadrícula: circuit, diagrama de flux, pseudocodi.</li>'
        '<li><strong>Els errors es documenten</strong> a la caixa «Error del '
        'dia»: què fallava, com el vas trobar (DEPURA) i com el vas resoldre. '
        'Un error ben documentat <strong>suma</strong> (R1 i R4); amagar-lo, no.</li>'
        '<li><strong>Si fas servir IA, ho declares</strong> al full del dia i '
        'saps explicar cada línia del codi que lliuris.</li></ol>'
        '<h2>Què s\'avalua (rúbrica R4 — 25 % de la nota)</h2><ul class="plain">'
        '<li><strong>Quadern complet i al dia</strong> (cada sessió té la seva '
        'pàgina treballada).</li>'
        '<li><strong>Claredat tècnica:</strong> s\'entén què vas fer i per què; '
        'decisions justificades.</li>'
        '<li><strong>Errors i depuració:</strong> documentats amb la rutina '
        'DEPURA.</li>'
        '<li><strong>Terminologia correcta</strong> (tens el vocabulari imprès '
        'a cada pàgina: fes-lo servir).</li></ul>'
        '<div class="callout">🧪 A la <strong>prova del trimestre</strong> '
        '(última sessió) pots tenir aquest quadern sobre la taula. Al final de '
        'cada SA, <strong>fotografia les pàgines</strong> i puja-les a la tasca '
        'de Classroom corresponent.</div>'
        '<h2>Índex del trimestre</h2>'
        '<table class="idx"><thead><tr><th>Sessió</th><th>Títol</th>'
        '<th>Data</th></tr></thead><tbody>' + files + '</tbody></table></div>')


def quadern_html(t: int) -> str:
    sessions = SESSIONS[t]
    total = len(sessions)
    pagines = [portada(t, sessions), pagina_us(t, sessions)]
    for i, s in enumerate(sessions, start=1):
        if s["prova"]:
            pagines += pagines_prova(t, i, total, s)
        else:
            pagines += pagines_sessio(t, i, total, s)
    cos = "\n".join(pagines)
    return (f'<!doctype html><html lang="ca"><head><meta charset="utf-8">'
            f'<title>Quadern tècnic — Trimestre {t}</title>'
            f'<style>{CSS}</style></head><body>{cos}</body></html>')


def main():
    browser = find_browser()
    print(f"Generant 3 quaderns tècnics amb: {browser}")
    ok = True
    with tempfile.TemporaryDirectory(prefix="quadern_") as tmp:
        for t in sorted(SESSIONS):
            tmp_html = Path(tmp) / f"quadern_t{t}.html"
            tmp_html.write_text(quadern_html(t), encoding="utf-8")
            pdf = DESTI / f"Quadern_tecnic_T{t}.pdf"
            if print_pdf(browser, tmp_html, pdf, tmp):
                # La font del quadern són les DADES de quadern_sessions.py:
                # la marca permet a tools/qa.py detectar dades editades
                # sense regenerar els PDF.
                font = (Path(__file__).with_name("quadern_sessions.py")
                        .read_text(encoding="utf-8"))
                escriu_marca(pdf, hash_font(font))
                pags = 2 + 2 * len(SESSIONS[t])
                print(f"  ✓ {pdf.relative_to(REPO)} ({pags} pàgines previstes)")
            else:
                print(f"  ⚠ no generat: T{t}")
                ok = False
    if not ok:
        sys.exit(1)
    print("Fet.")


if __name__ == "__main__":
    main()
