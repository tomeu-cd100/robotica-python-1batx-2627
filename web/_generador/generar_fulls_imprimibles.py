# -*- coding: utf-8 -*-
"""
Genera PDF imprimibles (per omplir/recollir en paper) dels fulls d'alumnat
que no passen pel pipeline d'activitats: el full de normes de seguretat (amb
signatura) i els 10 checklists d'alumnat (SA0-SA9, amb autoavaluació semàfor).

- Converteix el Markdown amb el MATEIX motor que el web (python-markdown) i
  aplica un post-procés de paper: caselles reals, graella semàfor per pintar
  i línies per escriure (nom, data, signatura). Un sol comportament de
  render a tot el curs: el que es veu al web és el que s'imprimeix.
- Imprimeix cada HTML a PDF amb Chrome/Edge headless.
- Desa cada PDF al costat del seu material: Classes/SAn/pdf/<nom>.pdf

Ús:
    py web/_generador/generar_fulls_imprimibles.py
"""
from __future__ import annotations

import html
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SCRIPT_DIR = Path(__file__).resolve().parent
REPO = SCRIPT_DIR.parent.parent
CLASSES = REPO / "Classes"

# Fulls a convertir: (md relatiu a Classes, "checklist" | "normes" | "targeta")
TARGETS = [
    ("SA1/SA1_normes_seguretat.md", "normes"),
] + [(f"SA{n}/SA{n}_checklist_alumnat.md", "checklist") for n in range(0, 10)] + [
    ("SA1/SA1_poster_robot_plantilla.md", "checklist"),
    ("00_General/00_Plantilla_disseny_objecte.md", "checklist"),
    ("00_General/00_Tauler_reptes.md", "checklist"),
    # Targetes de repàs exprés: es reparteixen en paper com a deures de
    # represa. Curs nou (100% MicroPython, sense C++): la targeta de
    # comparació de paradigmes del germà no aplica.
    # TODO (Tasks 7-15): revisar quines targetes de repàs calen realment
    # (p. ex. sintaxi bàsica, sensors, ràdio) quan existeixin les guies
    # docents; de moment només es manté la de MicroPython i la de ràdio.
    ("00_General/00_Repas_expres_MicroPython.md", "targeta"),
    ("00_General/00_Repas_expres_Radio.md", "targeta"),
]

# Fulls que JA són HTML complet i autocontingut (disseny propi per a A4): es
# converteixen a PDF tal qual, sense passar pel Markdown. Rellotge més llarg
# perquè carreguin fonts/icones de CDN abans d'imprimir.
RAW_HTML = [
    "00_General/impresos/Blocs_Programacio_Offline.html",
    "00_General/impresos/Blocs_Diagrames_Flux.html",
]

CSS = """
  @page { size: A4; margin: 15mm 15mm 13mm; }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body { font-family: "Segoe UI", Arial, sans-serif; color: #111;
         font-size: 10.7pt; line-height: 1.4; }
  h1 { font-size: 16.5pt; margin: 0 0 8pt; }
  h2 { font-size: 12pt; margin: 13pt 0 5pt; padding-bottom: 2pt;
       border-bottom: 1px solid #ccc; }
  .callout, blockquote { background: #eaf4fb; border-left: 4px solid #2b8ac6;
             padding: 6pt 10pt; margin: 8pt 0; font-size: 10pt; }
  blockquote p { margin: 3pt 0; }
  h3 { font-size: 11pt; margin: 9pt 0 4pt; }
  p { margin: 5pt 0; }
  code { font-family: Consolas, "Courier New", monospace; font-size: 9.6pt;
         background: #f2f2f2; padding: 0 2px; border-radius: 3px; }
  /* Camps per omplir */
  .fields { display: flex; flex-wrap: wrap; gap: 8pt 22pt; margin: 6pt 0 4pt; }
  .field { display: flex; align-items: flex-end; gap: 7pt; flex: 1 1 200pt; }
  .field .et { white-space: nowrap; font-weight: 600; }
  .line { flex: 1 1 auto; border-bottom: 1px solid #333; height: 15pt; }
  .fill-inline { display: inline-block; min-width: 120pt;
                 border-bottom: 1px solid #333; }
  /* Llistes de verificació */
  ul.check { list-style: none; margin: 4pt 0; padding-left: 2pt; }
  ul.check li { display: flex; align-items: flex-start; gap: 8pt; margin: 4pt 0; }
  ul.check .box { flex: 0 0 auto; width: 12pt; height: 12pt; border: 1.3px solid #333;
                  border-radius: 2px; margin-top: 1.5pt; }
  ul.plain, ul:not(.check) { margin: 4pt 0; padding-left: 20pt; }
  ul.plain li, ul:not(.check) li { margin: 3pt 0; }
  ol.normes, ol.num, ol { margin: 4pt 0; padding-left: 20pt; }
  ol.normes li, ol.num li, ol li { margin: 3pt 0; }
  pre { font-family: Consolas, "Courier New", monospace; font-size: 8.4pt;
        line-height: 1.2; background: #f7f7f7; border: 1px solid #e0e0e0;
        border-radius: 4px; padding: 6pt 8pt; white-space: pre; overflow: hidden;
        margin: 6pt 0; }
  /* Graella semàfor */
  table.grid { width: 100%; border-collapse: collapse; margin: 6pt 0; }
  table.grid th, table.grid td { border: 1px solid #bbb; padding: 5pt 7pt; }
  table.grid thead th { background: #eef3f7; font-size: 9.8pt; text-align: center; }
  table.grid thead th:first-child { text-align: left; }
  table.grid td.lab { text-align: left; }
  table.grid td.paint { width: 15%; height: 22pt; }
  /* Signatura (normes) */
  .camp { margin: 13pt 0; display: flex; align-items: flex-end; gap: 10pt; }
  .camp .et { white-space: nowrap; font-weight: 600; }
  .camp .linia { flex: 1 1 auto; border-bottom: 1px solid #333; height: 15pt; }
  .fila2 { display: flex; gap: 26pt; }
  .fila2 .camp { flex: 1; }
  .destacats { margin-top: 15pt; border: 1px solid #2b8ac6; border-radius: 4px;
               padding: 9pt 12pt; background: #f6fbfe; page-break-inside: avoid; }
  .destacats .t { font-weight: 600; margin: 0 0 8pt; }
  strong { font-weight: 700; }
  hr { border: 0; border-top: 1px solid #ddd; margin: 9pt 0; }
  /* Targetes de repàs: solucions de l'autotest obertes en paper */
  details { display: block; border: 1px solid #cfe3f0; border-radius: 4px;
            padding: 5pt 9pt; margin: 6pt 0; background: #f8fcff;
            page-break-inside: avoid; }
  details > summary { font-weight: 600; margin-bottom: 4pt; list-style: none; }
"""


from generador.navegador import find_browser  # noqa: E402  (re-exportat per a generar_quadern_tecnic)
from generador.pdfutil import escriu_marca, hash_font, pdf_valid  # noqa: E402


# --- Markdown -> HTML (MATEIX motor que el web) + post-procés de paper ------
# El .md es converteix amb python-markdown (com generar.py: un sol
# comportament de render a tot el curs) i després es transforma l'HTML per al
# paper: enllaços aplanats, caselles reals, línies per escriure i graella
# semàfor per pintar.
import markdown as md_lib  # noqa: E402

_EXTENSIONS = ["extra", "sane_lists"]
_SEMAFOR = ("🔴", "🟡", "🟢")


def fora_callouts_de_pdf(h: str) -> str:
    """Un full imprimible no s'enllaça a si mateix: fora l'avís del PDF.
    Es filtra PER PARÀGRAF (python-markdown fusiona blockquotes adjacents:
    esborrar el bloc sencer s'enduria el text veí) i abans d'aplanar els
    enllaços, quan els href encara hi són."""
    def neteja(m):
        cos = re.sub(r"<p>(?:(?!</p>).)*?(?:\.pdf|pdf/)(?:(?!</p>).)*?</p>",
                     "", m.group(1), flags=re.S)
        if not re.sub(r"<[^>]+>", "", cos).strip():
            return ""  # blockquote buit del tot: fora
        return "<blockquote>" + cos + "</blockquote>"
    return re.sub(r"<blockquote>(.*?)</blockquote>", neteja, h, flags=re.S)


def aplana_enllacos(h: str) -> str:
    """En paper no es pot clicar: enllaç -> només el text."""
    return re.sub(r"<a [^>]*>(.*?)</a>", r"\1", h, flags=re.S)


# Els runs de _ s'han de protegir ABANS de convertir: el motor de Markdown
# els interpretaria com a marques d'èmfasi i els partiria.
_LINIA = "%%LINIA%%"


def protegeix_camps(md: str) -> str:
    return re.sub(r"_{3,}", _LINIA, md)


def camps_per_omplir(h: str) -> str:
    """Runs de 3+ guions baixos (protegits) -> línia per escriure-hi a mà."""
    h = h.replace(_LINIA, '<span class="fill-inline"></span>')
    return re.sub(r"_{3,}", '<span class="fill-inline"></span>', h)


def caselles(h: str) -> str:
    """`- [ ]` -> casella real per marcar amb boli."""
    h = re.sub(r"<li>\s*\[[ xX]\]\s*(.*?)</li>",
               r'<li><span class="box"></span><span>\1</span></li>', h, flags=re.S)
    return re.sub(r"<ul>(\s*<li><span class=\"box\">)",
                  r'<ul class="check">\1', h)


def taules(h: str) -> str:
    """Totes les taules -> .grid; si la capçalera té 🔴🟡🟢, el cos es buida
    en cel·les .paint per pintar-hi el semàfor a mà."""
    def una(m):
        t = m.group(0)
        t = re.sub(r"<table[^>]*>", '<table class="grid">', t, count=1)
        cap = re.search(r"<thead>.*?</thead>", t, re.S)
        if not (cap and any(s in cap.group(0) for s in _SEMAFOR)):
            return t
        def fila(mf):
            cel = re.findall(r"<td[^>]*>.*?</td>", mf.group(0), re.S)
            if not cel:
                return mf.group(0)
            primera = re.sub(r"<td[^>]*>", '<td class="lab">', cel[0], count=1)
            return ("<tr>" + primera +
                    '<td class="paint"></td>' * (len(cel) - 1) + "</tr>")
        cos = re.search(r"<tbody>.*?</tbody>", t, re.S)
        if cos:
            nou = re.sub(r"<tr>.*?</tr>", fila, cos.group(0), flags=re.S)
            t = t.replace(cos.group(0), nou)
        return t
    return re.sub(r"<table[^>]*>.*?</table>", una, h, flags=re.S)


def inline_md(text: str) -> str:
    """Una línia de Markdown -> HTML inline (sense <p>), ja apte per a paper."""
    h = md_lib.markdown(protegeix_camps(text), extensions=_EXTENSIONS).strip()
    h = re.sub(r"^<p>|</p>$", "", h, flags=re.S)
    return camps_per_omplir(aplana_enllacos(h))


def md_to_body(md: str) -> tuple[str, str]:
    """Retorna (títol, html del cos) per a un full de checklist."""
    m = re.search(r"^# (.+)$", md, re.M)
    title = re.sub(r"[*`]", "", m.group(1)).strip() if m else ""
    h = md_lib.markdown(protegeix_camps(md), extensions=_EXTENSIONS)
    h = fora_callouts_de_pdf(h)
    h = aplana_enllacos(h)
    h = caselles(h)
    h = taules(h)
    h = camps_per_omplir(h)
    return title, h


def render_norms_body(md: str) -> tuple[str, str]:
    """Full de normes: llista numerada + bloc de signatura amb línies amples."""
    title = "SA1 · Normes de seguretat del laboratori de robòtica"
    intro = ("Es llegeixen en veu alta a la <strong>Sessió 2</strong>, es comenten amb "
             "exemples i cada alumne/a <strong>signa</strong> el compromís del final. "
             "El full signat es guarda a la carpeta del grup.")
    # Extreu les 12 normes (línies "N. ...") en ordre.
    normes = [inline_md(m.group(2)) for m in
              (re.match(r"(\d+)\.\s+(.*)", l.strip()) for l in md.splitlines()) if m]
    seccions = [
        ("1. Abans de connectar res", normes[0:3]),
        ("2. Connexions correctes", normes[3:7]),
        ("3. Durant el treball", normes[7:10]),
        ("4. En acabar", normes[10:12]),
    ]
    body = [f"<h1>{html.escape(title)}</h1>",
            f'<div class="callout">{intro}</div>']
    n0 = 1
    for h, items in seccions:
        body.append(f"<h2>{h}</h2>")
        lis = "".join(f"<li>{t}</li>" for t in items)
        body.append(f'<ol class="normes" start="{n0}">{lis}</ol>')
        n0 += len(items)
    body.append('<div class="sig"><h2>Compromís (signatura)</h2>'
                '<p>He llegit i entès les normes de seguretat del laboratori de robòtica '
                'i em comprometo a complir-les durant tot el curs.</p>'
                '<div class="camp"><span class="et">Nom i cognoms</span><span class="linia"></span></div>'
                '<div class="fila2">'
                '<div class="camp"><span class="et">Grup</span><span class="linia"></span></div>'
                '<div class="camp"><span class="et">Data</span><span class="linia"></span></div>'
                '</div>'
                '<div class="camp"><span class="et">Signatura de l\'alumne/a</span><span class="linia"></span></div>'
                '<div class="destacats"><p class="t">Les 2 normes que em semblen més '
                'importants (es traslladen a l\'Activitat 3 de la fitxa):</p>'
                '<div class="camp"><span class="et">1.</span><span class="linia"></span></div>'
                '<div class="camp"><span class="et">2.</span><span class="linia"></span></div>'
                '</div></div>')
    return title, "\n".join(body)


def wrap(title: str, body: str) -> str:
    return (f'<!doctype html><html lang="ca"><head><meta charset="utf-8">'
            f"<title>{html.escape(title)}</title><style>{CSS}</style></head>"
            f"<body>{body}</body></html>")


def print_pdf(browser: str, html_path: Path, pdf_path: Path, profile: str,
              budget: int = 4000) -> bool:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    # Esborra la sortida abans de renderitzar: si Chrome falla, no queda el PDF
    # antic fent passar el check de mida (evita committar una versio desfasada).
    if pdf_path.exists():
        try:
            pdf_path.unlink()
        except PermissionError:
            print(f"  ⚠ {pdf_path.name}: bloquejat (tanca'l al visor). No regenerat.")
            return False
    # Perfil FRESC per render: compartir-lo entre molts renders fa que Chrome
    # reutilitzi la cau i de tant en tant surti una versio desfasada.
    # Si Chrome talla el render (PDF truncat o sense pàgines), es reintenta
    # amb el doble i el quàdruple de temps virtual.
    for factor in (1, 2, 4):
        with tempfile.TemporaryDirectory(prefix="fullpdf1_") as prof:
            cmd = [browser, "--headless=new", "--disable-gpu", "--disk-cache-size=1",
                   *([] if sys.platform == "win32" else ["--no-sandbox"]),
                   "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
                   f"--virtual-time-budget={budget * factor}", f"--user-data-dir={prof}",
                   f"--print-to-pdf={pdf_path}", html_path.as_uri()]
            subprocess.run(cmd, capture_output=True, text=True)
        if pdf_valid(pdf_path):
            return True
    return False


def main():
    browser = find_browser()
    print(f"Generant {len(TARGETS)} fulls imprimibles amb: {browser}")
    ok, fail = 0, 0
    with tempfile.TemporaryDirectory(prefix="fullpdf_") as profile, \
         tempfile.TemporaryDirectory(prefix="fullhtml_") as htmldir:
        for rel, kind in TARGETS:
            md_path = CLASSES / rel
            if not md_path.exists():
                print(f"  ⚠ falta: {rel}")
                fail += 1
                continue
            md = md_path.read_text(encoding="utf-8")
            if kind == "normes":
                title, body = render_norms_body(md)
            else:
                title, body = md_to_body(md)
                # el <h1> ja surt del cos per als checklists
            if kind == "targeta":
                # En paper no hi ha desplegables: les solucions de l'autotest
                # surten obertes (la targeta és d'autoestudi a casa).
                body = body.replace("<details>", "<details open>")
            html_doc = wrap(title, body)
            tmp_html = Path(htmldir) / (md_path.stem + ".html")
            tmp_html.write_text(html_doc, encoding="utf-8")
            pdf_path = md_path.parent / "pdf" / (md_path.stem + ".pdf")
            if print_pdf(browser, tmp_html, pdf_path, profile):
                # Marca de sincronia: tools/qa.py detecta un .md editat
                # sense regenerar el seu PDF comparant aquest hash.
                escriu_marca(pdf_path, hash_font(md))
                print(f"  ✓ {pdf_path.relative_to(REPO)}")
                ok += 1
            else:
                print(f"  ⚠ no generat: {rel}")
                fail += 1

        # Fulls que ja són HTML autocontingut: s'imprimeixen tal qual.
        for rel in RAW_HTML:
            src = CLASSES / rel
            if not src.exists():
                print(f"  ⚠ falta: {rel}")
                fail += 1
                continue
            pdf_path = CLASSES / "00_General" / "pdf" / (src.stem + ".pdf")
            if print_pdf(browser, src, pdf_path, profile, budget=10000):
                escriu_marca(pdf_path, hash_font(src.read_text(encoding="utf-8")))
                print(f"  ✓ {pdf_path.relative_to(REPO)}")
                ok += 1
            else:
                print(f"  ⚠ no generat: {rel}")
                fail += 1
    print(f"Fet. {ok} PDF generats" + (f", {fail} amb error." if fail else "."))
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
