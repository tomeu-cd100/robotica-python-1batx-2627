# -*- coding: utf-8 -*-
"""
Generador del web de Robòtica amb Python · 1r de Batxillerat.

Converteix tot el material .md del repositori en un lloc web estàtic
autocontingut (carpeta web/), amb enllaços interns reescrits, navegació
per seccions, distintius de trimestre, pàgines de codi per SA i cercador.

Ús:
    py web/_generador/generar.py

Dependències: markdown, pygments  ->  py -m pip install markdown pygments
"""
from __future__ import annotations

import html
import json
import os
import re
import shutil
import subprocess
import unicodedata
import urllib.parse
from datetime import date, datetime, timezone
from pathlib import Path

import markdown
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

# ---------------------------------------------------------------------------
# Rutes base
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent          # web/_generador
WEB = SCRIPT_DIR.parent                                # web
ROOT = WEB.parent                                      # arrel del repositori
ASSETS = WEB / "assets"
IMG_OUT = ASSETS / "img"

# Identitat del lloc i del repo. Un fork ho canvia amb variables d'entorn
# (o editant els valors per defecte): REPO_SLUG="usuari/repo" py generar.py
SITE_TITLE = os.environ.get("SITE_TITLE", "Robòtica amb Python · 1r de Batxillerat")
SITE_TAGLINE = os.environ.get("SITE_TAGLINE",
                              "Material docent · LOMLOE Catalunya · curs 2026-2027")


def build_date() -> str:
    """Data del web derivada del contingut, no del rellotge, perquè dos builds
    del mateix material produeixin una sortida idèntica (build reproduïble).
    Ordre de preferència: data de l'últim commit de git → SOURCE_DATE_EPOCH
    (útil en CI) → data d'avui (últim recurs)."""
    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "log", "-1", "--format=%cs"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        if out:
            return out
    except (OSError, subprocess.SubprocessError):
        pass
    epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if epoch:
        try:
            return datetime.fromtimestamp(int(epoch), tz=timezone.utc).date().isoformat()
        except (ValueError, OverflowError, OSError):
            pass
    return date.today().isoformat()


BUILD_DATE = build_date()

CODE_EXT = {".py"}
IMG_EXT = {".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif"}
DOC_EXT = {".pdf", ".xlsx", ".xls", ".pptx", ".ppt", ".docx", ".doc",
           ".csv", ".odt", ".ods", ".zip"}

# Bases de GitHub per enllaçar/visualitzar documents sense copiar-los al web
REPO_SLUG = os.environ.get("REPO_SLUG", "tomeu-cd100/robotica-python-1batx-2627")
REPO_URL = f"https://github.com/{REPO_SLUG}"
PAGES_BASE = f"https://{REPO_SLUG.split('/')[0]}.github.io/{REPO_SLUG.split('/')[1]}"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO_SLUG}/main/"
TREE_BASE = f"https://github.com/{REPO_SLUG}/tree/main/"
BLOB_BASE = f"https://github.com/{REPO_SLUG}/blob/main/"

# ---------------------------------------------------------------------------
# Definició de seccions (cada apartat un color)
# ---------------------------------------------------------------------------
SECTIONS = [
    {"key": "programacio", "title": "Programació didàctica", "src": "Programació didàctica",
     "icon": "📘", "desc": "Objectius, sabers, metodologia, avaluació, rúbriques i les 9 SA.",
     "pauta": ["Comença per l'<strong>Índex general (00)</strong>: és el mapa de tots els documents.",
               "Per al dia a dia en tens prou amb tres: <strong>04 Metodologia</strong> (com es treballa), <strong>06-07 Avaluació i rúbriques</strong> (com es qualifica) i <strong>08 Seqüenciació</strong> (el calendari).",
               "Cada SA té el seu document (<strong>10 a 18</strong>) amb objectius, sessions i mapa d'avaluació."]},
    {"key": "classes", "title": "Classes", "src": "Classes",
     "icon": "🧑‍🏫", "desc": "Material d'aula per SA: guies, fitxes, esquemes i codi.",
     "pauta": ["Tria la <strong>SA de la setmana</strong> a les targetes de sota (cada trimestre té el seu color).",
               "Dins de cada SA, l'ordre de treball és sempre el mateix: <strong>1) guia docent → 2) fitxa base → 3) esquemes i codi → 4) fitxa ampliada i reptes</strong>.",
               "Les rutines comunes (graella d'activació, mini-checks, pòsters, defensa oral, IA) són al <strong>Material transversal del curs</strong>."]},
    {"key": "reptes", "title": "Reptes", "src": "Reptes",
     "icon": "🎯", "desc": "Reptes triables per SA amb el seu solucionari.",
     "pauta": ["Cada SA té <strong>3 reptes per triar</strong>: mateixos continguts i mínim comú, contextos diferents.",
               "L'alumnat tria <strong>pel context</strong> (no per dificultat) i decideix fins on arriba amb les ampliacions.",
               "El <strong>solucionari</strong> (codi resolt) és material del docent: no es lliura a l'alumnat."]},
    {"key": "avaluacio", "title": "Avaluació", "src": "Avaluació",
     "icon": "📝", "desc": "Proves pràctiques per trimestre i full de qualificació.",
     "pauta": ["Una <strong>prova pràctica per trimestre</strong>, integrada a l'última sessió de SA3, SA6 i SA9 (no costa hores extra).",
               "<strong>T1 i T2 són individuals</strong> per defecte; el radar previ són els mini-checks de cada SA (a Classes → Material transversal).",
               "Després de cada prova, l'alumnat escriu el <strong>pla de millora personal</strong> (3 línies) al quadern; el <strong>full de qualificació</strong> creua criteris CA ↔ rúbriques.",
               "Per a l'alumnat: la guia <a href=\"../classes/00-general/00-avaluacio-per-alumnat.html\"><strong>«Com s'avalua aquesta matèria»</strong></a> (reparteix-la la primera setmana) i la caixa <strong>«🎯 Objectius i avaluació»</strong> de cada fitxa."]},
    {"key": "normativa", "title": "Normativa", "src": "Normativa",
     "icon": "⚖️", "desc": "Marc legal LOMLOE i documents oficials.",
     "pauta": ["Per al dia a dia, la <strong>síntesi (01)</strong> és suficient.",
               "Els <strong>PDF oficials</strong> (Decret 171/2022, RD 243/2022) són per justificar decisions davant d'inspecció o famílies."]},
    {"key": "simulacions", "title": "Simulacions", "src": "Simulacions",
     "icon": "🔌", "desc": "Circuits Wokwi de pràctiques i reptes: codi i diagrama, reproduïbles.",
     "pauta": ["Cada pràctica i repte simulable té el seu <strong>circuit Wokwi</strong>: serveix per treballar sense maquinari o abans de muntar.",
               "Per reproduir-la: projecte nou a <strong>wokwi.com</strong> → enganxa-hi el <code>diagram.json</code> i el codi.",
               "El que no és simulable (micro:bit, robot 3dBot) té el <strong>pla B</strong> indicat a la presentació."]},
    {"key": "recursos", "title": "Recursos", "src": "Recursos",
     "icon": "📚", "desc": "Recursos de professorat en obert i materials de suport.",
     "pauta": ["Material de <strong>consulta i suport</strong>: no forma part de la seqüència del curs.",
               "Comença pel <strong>LLEGEIX-ME</strong> per saber què hi ha i per a què serveix cada cosa."]},
]
SECTION_BY_KEY = {s["key"]: s for s in SECTIONS}

# Pàgines especials de l'arrel del repositori
ROOT_PAGES = [
    {"src": "GUIA_INICI_DOCENT.md", "out": "guia-inici.html",
     "title": "Guia d'inici docent", "public": "docent"},
]

# Menú superior per audiència: (href des de l'arrel, etiqueta, clau activa).
# Les claus «docent» i «alumnat» són hubs d'orientació, no seccions amb carpeta.
TOPNAV_ITEMS = [
    ("index.html", "Inici", "inici", False),
    ("classes/index.html", "Les 9 SA", "classes", False),
    ("reptes/index.html", "Reptes", "reptes", False),
    ("simulacions/index.html", "Simulacions", "simulacions", False),
    ("programacio/index.html", "Programació", "programacio", True),
    ("avaluacio/index.html", "Avaluació", "avaluacio", True),
    ("recursos/index.html", "Recursos", "recursos", True),
]
HUB_KEYS = {"docent", "alumnat"}

TRIMESTRES = {
    1: {"label": "1r trimestre", "sas": [1, 2, 3]},
    2: {"label": "2n trimestre", "sas": [4, 5, 6]},
    3: {"label": "3r trimestre", "sas": [7, 8, 9]},
}
# Etiquetes especials per a subcarpetes que no són SA (clau = slug de la carpeta)
GROUP_LABELS = {
    "00-general": "Material transversal del curs",
}
# Projectes trimestrals (fil conductor): grup propi a Classes, entre SA.
# El rover (T3) va ABANS de SA7: es munta a la sessió 0 del 3r trimestre.
PROJECTES = [
    {"num": 1, "slug": "projecte-t1", "emoji": "🐣", "after_sa": 3, "tri": 1,
     "nom": "Projecte T1 · La mascota reactiva", "curt": "Mascota",
     "producte": "Robot social: es munta a final del 1r trimestre",
     "portada": "00_Projecte_T1_portada.md",
     "dossier": "00_Projecte_T1_Mascota.md"},
    {"num": 2, "slug": "projecte-t2", "emoji": "🚗", "after_sa": 6, "tri": 2,
     "nom": "Projecte T2 · El vehicle teledirigit", "curt": "Vehicle",
     "producte": "Vehicle teledirigit: es munta a SA4 i es tanca a final del 2n trimestre",
     "portada": "00_Projecte_T2_portada.md",
     "dossier": "00_Projecte_T2_Vehicle.md"},
    {"num": 3, "slug": "projecte-t3", "emoji": "🚙", "after_sa": 6, "tri": 3,
     "nom": "Projecte T3 · El rover autònom", "curt": "Rover",
     "producte": "Robot mòbil: es munta a la sessió 0 del 3r trimestre, abans de SA7",
     "portada": "00_Projecte_T3_portada.md",
     "dossier": "00_Projecte_T3_Rover.md"},
]
PROJECTE_BY_SLUG = {p["slug"]: p for p in PROJECTES}
PROJECTE_BY_SRC = {p[k]: p for p in PROJECTES for k in ("portada", "dossier")}
SA_TITLES = {
    0: "Vocabulari essencial i bases de programació",
    1: "Introducció a la robòtica",
    2: "Sortides digitals i PWM",
    3: "Entrades i sensors",
    4: "Moviment: servos i motors",
    5: "micro:bit i MicroPython",
    6: "Sistemes de control",
    7: "Robòtica mòbil",
    8: "IoT i IA",
    9: "Projecte final",
}
# Emoji identificatiu de cada SA (ancorat al món de la robòtica)
SA_ICONES = {0: "🧩", 1: "🤖", 2: "💡", 3: "📡", 4: "⚙️",
             5: "🐍", 6: "🎛️", 7: "🚗", 8: "🌐", 9: "🏆"}
# Frase del producte de cada SA (síntesi del «Producte» de la programació didàctica)
SA_PRODUCTES = {
    0: "Vocabulari i bases de programació",
    1: "Fitxa-pòster d'un robot real",
    2: "Dispositiu de senyalització (semàfor o RGB)",
    3: "Alarma o llum automàtic (sensor→actuador)",
    4: "Mecanisme motoritzat controlat per sensor",
    5: "App micro:bit amb sensors o ràdio",
    6: "Sistema de control (termòstat o màquina d'estats)",
    7: "Robot mòbil autònom (línia o obstacles)",
    8: "Sistema IoT o classificador amb IA",
    9: "Robot autònom + dossier + defensa",
}


def sa_trimestre(n: int) -> int:
    return 1 if n <= 3 else 2 if n <= 6 else 3


# ---------------------------------------------------------------------------
# Classificació per públic (docent / alumnat) — vegeu el commutador de vista
# ---------------------------------------------------------------------------
# Seccions senceres que són material del docent
DOCENT_SECTIONS = {"programacio", "normativa", "avaluacio", "recursos"}
# Fitxers de Classes que són del docent (per patró de nom)
DOCENT_NAME_HINTS = ("_guia_docent", "_checklist_docent", "_solucions")
# 00-general: material transversal visible a l'alumnat (la resta, docent)
GENERAL_ALUMNAT = {
    "00_Targetes_rescat.md", "00_Checklist_taller_avaries.md",
    "00_Glossari_tecnic.md",
    "00_Avaluacio_per_alumnat.md", "00_Fitxes_referencia_tecnica.md",
    "00_Plantilla_disseny_objecte.md", "00_Galeria_exemples_objectes.md",
    "00_Poster_IA_us_assistents.md", "00_Quadern_tecnic.md",
    "00_Repas_expres_MicroPython.md", "00_Repas_expres_Radio.md",
    "00_Repas_expres_Cpp.md", "00_Guia_defensa_oral.md",
    "00_Tauler_reptes.md",
    "00_Fil_conductor_construccions.md", "00_Projecte_T1_Mascota.md",
    "00_Projecte_T2_Vehicle.md", "00_Projecte_T3_Rover.md",
    "00_Projecte_T1_portada.md", "00_Projecte_T2_portada.md",
    "00_Projecte_T3_portada.md",
}


def classify_public(section_key: str, src: Path) -> str:
    """Retorna 'docent' o 'alumnat' per a una pàgina font."""
    if section_key in DOCENT_SECTIONS:
        return "docent"
    name = src.name
    parts = src.parts
    # Qualsevol carpeta "Solucionari" (de reptes o de classes) -> docent
    if "Solucionari" in parts:
        return "docent"
    # Material transversal 00-general
    if "00_General" in parts:
        return "alumnat" if name in GENERAL_ALUMNAT else "docent"
    # Classes per patró de nom
    if any(h in name.lower() for h in DOCENT_NAME_HINTS):
        return "docent"
    return "alumnat"


def is_activitat(src: Path) -> bool:
    """Document que recull activitats que ha de fer l'alumnat (es genera en PDF)."""
    name = src.name
    parts = src.parts
    if name.endswith(("_fitxa_alumnat.md", "_fitxa_ampliada.md")):
        return True
    if name in {"SA1_poster_robot_plantilla.md", "00_Plantilla_disseny_objecte.md",
                "SA1_prova_diagnostica.md", "00_Avaluacio_per_alumnat.md",
                "00_Glossari_tecnic.md", "00_Targetes_rescat.md",
                "00_Quadern_tecnic.md"}:
        return True
    if "SA9" in parts and "plantilles" in parts and name.endswith(".md"):
        return True
    if name.startswith("Prova_practica_T") and name.endswith(".md"):
        return True
    if name.startswith("Reptes_SA") and name.endswith(".md"):
        return True
    return False


# ---------------------------------------------------------------------------
# Utilitats pures: viuen al paquet generador/ (amb tests a tests/)
# ---------------------------------------------------------------------------
from generador.utils import (  # noqa: E402
    BODY_CERCA_MAX, apply_outside_code, detect_sa, first_h1, pdf_out_for,
    rel_url, slugify, strip_accents, text_pla_cerca,
)


def depth_prefix(out_rel: str) -> str:
    d = out_rel.count("/")
    return "../" * d


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------
def make_md() -> markdown.Markdown:
    return markdown.Markdown(extensions=[
        "extra", "toc", "sane_lists", "admonition",
        "codehilite", "attr_list",
    ], extension_configs={
        "toc": {"anchorlink": True, "permalink": False},
        "codehilite": {"guess_lang": False, "css_class": "highlight"},
    })


def wrap_tables(body: str) -> str:
    """Embolcalla cada <table> amb un contenidor de scroll horitzontal
    perquè les taules amples (rúbriques) no desbordin en mòbil."""
    body = re.sub(r"<table(\s[^>]*)?>", r'<div class="taula-scroll"><table\1>', body)
    return body.replace("</table>", "</table></div>")


def marca_ruta(body: str) -> str:
    """A les portades de SA, embolcalla la secció «Itinerari…» (des del seu
    <h2> fins al <h2> següent) amb <section class="ruta"> perquè el CSS la
    renderitzi com a passos. Si no hi ha itinerari, no fa res."""
    m = re.search(r'<h2 id="itinerari[^>]*>.*?</h2>', body)
    if not m:
        return body
    nxt = body.find("<h2", m.end())
    end = nxt if nxt != -1 else len(body)
    return (body[:m.start()] + '<section class="ruta">'
            + body[m.start():end] + "</section>" + body[end:])


_TARGETA_RE = re.compile(
    r'<p><strong>(T\d.*?)</strong></p>\s*<ul>(.*?)</ul>', re.DOTALL)
_NIVELL = (("🟢", "n-verd"), ("🟡", "n-groc"), ("🔴", "n-vermell"))


def marca_targetes(body: str) -> str:
    """Converteix cada targeta de rescat (`**Tn.m · «…»**` seguit d'una llista
    🟢/🟡/🔴) en una `<div class="targeta">` apilada, amb la capçalera i les
    files de nivell acolorides. Manté el markdown font net i llegible a GitHub;
    tota la presentació viu al generador i al CSS (`.targeta`)."""
    def _li(m: re.Match) -> str:
        obri = m.group(1)  # etiquetes/atributs del <li> original
        cos = m.group(2)
        for emoji, classe in _NIVELL:
            if cos.lstrip().startswith(emoji):
                cos = cos.lstrip()[len(emoji):].lstrip()
                return f'<li class="{classe}"{obri}>{cos}</li>'
        return m.group(0)

    def _card(m: re.Match) -> str:
        titol, llista = m.group(1), m.group(2)
        llista = re.sub(r'<li([^>]*)>(.*?)</li>', _li, llista, flags=re.DOTALL)
        return (f'<div class="targeta"><div class="cap">{titol}</div>'
                f'<ul>{llista}</ul></div>')

    return _TARGETA_RE.sub(_card, body)


def strip_github_only(text: str) -> str:
    """Treu del text Markdown els blocs marcats amb
    `<!-- web:only-github -->` … `<!-- /web:only-github -->`.

    Serveix per a contingut que només té sentit a GitHub (p. ex. una taula de
    fitxers), perquè al web ja el genera el mateix generador (targetes, sidebar)
    i es duplicaria. A GitHub els comentaris HTML són invisibles i el bloc es
    veu; al web, aquest bloc s'elimina abans de convertir-lo. Font única."""
    return re.sub(r"<!--\s*web:only-github\s*-->.*?<!--\s*/web:only-github\s*-->\s*",
                  "", text, flags=re.DOTALL)


# ---------------------------------------------------------------------------
# Descobriment de pàgines
# ---------------------------------------------------------------------------
class Page:
    def __init__(self, src: Path, section: str, out_rel: str, title: str,
                 trimester: int | None = None, kind: str = "doc",
                 public: str = "alumnat"):
        self.src = src
        self.section = section
        self.out_rel = out_rel
        self.title = title
        self.trimester = trimester
        self.kind = kind  # doc | index | code | special
        self.public = public  # docent | alumnat


def out_for_md(section_key: str, src: Path, src_dir: Path) -> str:
    """Calcula la ruta de sortida (relativa a web/) per a un .md d'una secció."""
    rel = src.relative_to(src_dir)
    parts = list(rel.parts)
    fname = parts[-1]
    is_readme = fname.lower() == "readme.md"
    sub = [slugify(p) for p in parts[:-1]]
    if is_readme:
        # README d'una carpeta -> index.html d'aquesta carpeta
        path = "/".join([section_key] + sub + ["index.html"])
    else:
        slug = slugify(fname[:-3])  # treu .md
        path = "/".join([section_key] + sub + [slug + ".html"])
    return path


def out_for_projecte(src: Path) -> str | None:
    """Ruta de sortida pròpia per a les pàgines de projecte trimestral
    (grup classes/projecte-tN/ en lloc de classes/00-general/)."""
    pr = PROJECTE_BY_SRC.get(src.name)
    if pr is None:
        return None
    if src.name == pr["portada"]:
        return f"classes/{pr['slug']}/index.html"
    return f"classes/{pr['slug']}/{slugify(src.name[:-3])}.html"


def write_redirects_projectes(out_dir: Path) -> None:
    """Les URLs antigues dels dossiers (classes/00-general/…) poden estar
    enllaçades des del Classroom: hi deixem una redirecció."""
    for pr in PROJECTES:
        slug_dossier = slugify(pr["dossier"][:-3]) + ".html"
        antic = out_dir / "classes" / "00-general" / slug_dossier
        nou = f"../{pr['slug']}/{slug_dossier}"
        antic.parent.mkdir(parents=True, exist_ok=True)
        antic.write_text(
            f'<!DOCTYPE html><html lang="ca"><head><meta charset="utf-8">\n'
            f'<meta http-equiv="refresh" content="0; url={nou}">\n'
            f'<link rel="canonical" href="{nou}">\n'
            f'<title>{html.escape(pr["nom"])}</title></head>\n'
            f'<body><p>Aquesta pàgina s\'ha mogut: '
            f'<a href="{nou}">{html.escape(pr["nom"])}</a></p></body></html>\n',
            encoding="utf-8")


def discover() -> tuple[list[Page], dict, dict, list[dict], list[dict], dict]:
    """Retorna (pàgines, md_map, code_map, code_groups, sim_groups, sim_map):
    - pàgines: llista de Page descobertes.
    - md_map: ruta absoluta d'un .md font -> out_rel de la seva pàgina.
    - code_map: ruta absoluta d'un fitxer de codi -> (out_rel, àncora).
    - code_groups: grups de codi per SA (Classes i Solucionari).
    - sim_groups: grups de simulacions Wokwi (una pàgina per projecte).
    - sim_map: ruta absoluta d'una carpeta/fitxer de simulació -> out_rel."""
    pages: list[Page] = []
    md_map: dict[str, str] = {}
    code_map: dict[str, tuple[str, str]] = {}
    code_groups: list[dict] = []

    # Pàgines de seccions
    for sec in SECTIONS:
        src_dir = ROOT / sec["src"]
        if not src_dir.exists():
            continue
        for md_path in sorted(src_dir.rglob("*.md")):
            # Les EXPLICACIO.md dins de codi/ no són pàgines soltes: es
            # rendericen com a pàgina de pràctica (vegeu add_code_group).
            if "codi" in md_path.relative_to(src_dir).parts[:-1]:
                continue
            out_rel = out_for_md(sec["key"], md_path, src_dir)
            pr = PROJECTE_BY_SRC.get(md_path.name) if sec["key"] == "classes" else None
            if pr is not None:
                out_rel = out_for_projecte(md_path)
            text = md_path.read_text(encoding="utf-8")
            title = first_h1(text) or md_path.stem
            sa = detect_sa(md_path.name) or detect_sa(str(md_path.relative_to(src_dir)))
            tri = sa_trimestre(sa) if sa else None
            kind = "index" if md_path.name.lower() == "readme.md" else "doc"
            if pr is not None:
                tri = pr["tri"]
                kind = "index" if md_path.name == pr["portada"] else "doc"
            public = classify_public(sec["key"], md_path)
            pages.append(Page(md_path, sec["key"], out_rel, title, tri, kind, public))
            md_map[str(md_path.resolve())] = out_rel

    # Pàgines especials de l'arrel
    for rp in ROOT_PAGES:
        src = ROOT / rp["src"]
        if src.exists():
            pages.append(Page(src, "inici", rp["out"], rp["title"], None, "special",
                              rp.get("public", "alumnat")))
            md_map[str(src.resolve())] = rp["out"]
    md_map[str((ROOT / "README.md").resolve())] = "index.html"

    # Grups de codi: Classes/SAx i Reptes/Solucionari/SAx
    def add_code_group(label: str, base: Path, out_rel: str, section_key: str,
                       tri: int | None):
        files = sorted([p for p in base.rglob("*") if p.suffix.lower() in CODE_EXT])
        if not files:
            return
        practiques_dir = out_rel[:-len(".html")]  # p. ex. classes/sa2/codi
        items = []
        for f in files:
            rel = f.relative_to(base)
            anchor = slugify(str(rel.with_suffix("")))
            item = {"path": f, "rel": str(rel).replace("\\", "/"), "anchor": anchor}
            # Pàgina de pràctica pròpia: sketch d'alumnat amb una EXPLICACIO.md
            # al costat (per què es fa + el codi per blocs). El fitxer principal
            # d'un sketch en carpeta és el que duu el nom de la carpeta.
            if f.parent.name == "codi":
                expl = f.with_name(f.stem + "_EXPLICACIO.md")
            elif f.stem == f.parent.name:
                expl = f.parent / "EXPLICACIO.md"
            else:
                expl = None
            if section_key == "classes" and expl is not None and expl.exists():
                page_out = f"{practiques_dir}/{slugify(f.stem)}.html"
                titol = first_h1(expl.read_text(encoding="utf-8")) or f.stem
                item.update(expl=expl, page_out=page_out, title=titol)
                code_map[str(f.resolve())] = (page_out, "")
                md_map[str(expl.resolve())] = page_out
                pages.append(Page(expl, section_key, page_out, titol, tri,
                                  "practica", "alumnat"))
            else:
                code_map[str(f.resolve())] = (out_rel, anchor)
            items.append(item)
        pub = "docent" if "Solucionari" in base.parts else "alumnat"
        code_groups.append({"label": label, "out_rel": out_rel,
                            "section": section_key, "tri": tri, "items": items,
                            "public": pub})
        pages.append(Page(base, section_key, out_rel, label, tri, "code", pub))

    classes_dir = ROOT / "Classes"
    for sa in range(1, 10):
        d = classes_dir / f"SA{sa}"
        if d.exists():
            add_code_group(f"Codi · SA{sa}", d, f"classes/sa{sa}/codi.html",
                           "classes", sa_trimestre(sa))
    sol_dir = ROOT / "Reptes" / "Solucionari"
    for sa in range(1, 10):
        d = sol_dir / f"SA{sa}"
        if d.exists():
            add_code_group(f"Codi solucionari reptes · SA{sa}", d,
                           f"reptes/solucionari/sa{sa}/codi.html", "reptes",
                           sa_trimestre(sa))

    # Simulacions Wokwi: una pàgina per projecte (carpeta amb sketch + diagram)
    sim_groups: list[dict] = []
    sim_map: dict[str, str] = {}
    sim_dir = ROOT / "Simulacions" / "Wokwi"
    if sim_dir.exists():
        for folder in sorted([p for p in sim_dir.rglob("*") if p.is_dir()]):
            files = sorted([f for f in folder.iterdir() if f.is_file()
                            and (f.suffix.lower() in CODE_EXT
                                 or f.suffix.lower() in {".json", ".txt"})])
            if not any(f.suffix.lower() == ".py" or f.name == "diagram.json"
                       for f in files):
                continue
            rel = folder.relative_to(sim_dir)
            is_repte = rel.parts[0].lower() == "reptes"
            sub = "reptes" if is_repte else "practiques"
            out_rel = f"simulacions/{sub}/{slugify(folder.name)}.html"
            sa = detect_sa(folder.name)
            tri = sa_trimestre(sa) if sa else None
            title = folder.name.replace("_", " ")
            sim_groups.append({"out_rel": out_rel, "folder": folder, "files": files,
                               "title": title, "tri": tri, "is_repte": is_repte})
            pages.append(Page(folder, "simulacions", out_rel, title, tri, "sim", "alumnat"))
            sim_map[str(folder.resolve())] = out_rel
            for f in files:
                sim_map[str(f.resolve())] = out_rel

    return pages, md_map, code_map, code_groups, sim_groups, sim_map


# ---------------------------------------------------------------------------
# Reescriptura d'enllaços dins l'HTML generat
# ---------------------------------------------------------------------------
def rewrite_links(html_body: str, src_file: Path, out_rel: str,
                  md_map: dict, code_map: dict, sim_map: dict, copied_imgs: dict,
                  md_title_map: dict | None = None) -> str:
    prefix = depth_prefix(out_rel)
    src_dir = src_file.parent if src_file.is_file() else src_file

    def resolve(href: str) -> str | None:
        raw = urllib.parse.unquote(href.split("#")[0].split("?")[0])
        frag = ""
        if "#" in href:
            frag = "#" + href.split("#", 1)[1]
        if not raw:
            return href  # només àncora
        target = (src_dir / raw).resolve()
        key = str(target)
        if key in md_map:
            return rel_url(out_rel, md_map[key]) + frag
        if key in code_map:
            page, anchor = code_map[key]
            return rel_url(out_rel, page) + ("#" + anchor if anchor else "")
        if key in sim_map:
            return rel_url(out_rel, sim_map[key]) + frag
        # Carpeta -> index.html d'aquesta carpeta?
        readme = target / "README.md"
        if str(readme.resolve()) in md_map:
            return rel_url(out_rel, md_map[str(readme.resolve())]) + frag
        # Carpeta de codi (p. ex. "codi/") -> pàgina de codi dels seus sketches
        if target.is_dir():
            tk = str(target)
            for k, (page, _anchor) in code_map.items():
                if k.startswith(tk + "\\") or k.startswith(tk + "/"):
                    return rel_url(out_rel, page) + frag
        # Imatge -> copiar a assets/img
        if target.suffix.lower() in IMG_EXT and target.exists():
            name = copy_image(target, copied_imgs)
            return prefix + "assets/img/" + name + frag
        # .md NO convertit a pàgina -> enllaç al fitxer original a GitHub
        if target.suffix.lower() == ".md" and target.exists():
            try:
                relpath = target.relative_to(ROOT.resolve())
                return BLOB_BASE + urllib.parse.quote(str(relpath).replace("\\", "/")) + frag
            except ValueError:
                pass
        # Document (pdf, full de càlcul…) -> enllaç a GitHub
        if target.suffix.lower() in DOC_EXT and target.exists():
            try:
                relpath = target.relative_to(ROOT.resolve())
                return BLOB_BASE + urllib.parse.quote(str(relpath).replace("\\", "/"))
            except ValueError:
                pass
        return None

    def repl_href(m):
        href = m.group(2)
        if href.startswith(("http://", "https://", "mailto:", "#", "tel:")):
            extra = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
            return f'{m.group(1)}="{href}"{extra}'
        new = resolve(href)
        if new and new.startswith("http"):
            return f'{m.group(1)}="{new}" target="_blank" rel="noopener"'
        return f'{m.group(1)}="{new if new else href}"'

    def repl_src(m):
        src = m.group(1)
        if src.startswith(("http://", "https://", "data:")):
            return m.group(0)
        new = resolve(src)
        return f'src="{new if new else src}"' if new else m.group(0)

    def repl_mdtext(m):
        titol = md_title_map.get(m.group(1)) if md_title_map else None
        return ">" + html.escape(titol) + "</a>" if titol else m.group(0)

    # La reescriptura NO entra mai dins de <pre>/<code>: el codi d'exemple
    # (un href="..." literal en un fragment) és contingut, no navegació (P5).
    def reescriu(segment: str) -> str:
        segment = re.sub(r'(href)="([^"]+)"', repl_href, segment)
        segment = re.sub(r'src="([^"]+)"', repl_src, segment)
        if md_title_map:
            segment = re.sub(r'>([^<>]+\.md)</a>', repl_mdtext, segment)
        return segment

    return apply_outside_code(html_body, reescriu)


def copy_image(src: Path, copied: dict) -> str:
    key = str(src.resolve())
    if key in copied:
        return copied[key]
    IMG_OUT.mkdir(parents=True, exist_ok=True)
    name = slugify(src.stem) + src.suffix.lower()
    # evita col·lisions
    dest = IMG_OUT / name
    i = 1
    while dest.exists() and str(dest.resolve()) not in copied.values():
        name = f"{slugify(src.stem)}-{i}{src.suffix.lower()}"
        dest = IMG_OUT / name
        i += 1
    shutil.copy2(src, dest)
    copied[key] = name
    return name


# ---------------------------------------------------------------------------
# Plantilla HTML
# ---------------------------------------------------------------------------
def topnav_html(out_rel: str, active: str) -> str:
    """Menú per audiència (estil «Aula Maker»): curt i estable a totes les
    pàgines. La resta de seccions s'hi arriba pels hubs, la portada i el
    cercador; cap URL de secció no canvia."""
    prefix = depth_prefix(out_rel)
    items = []
    for href, label, key, docent in TOPNAV_ITEMS:
        classes = []
        if active == key:
            classes.append("actiu")
        if docent:
            classes.append("nomes-docent")
        cls = f' class="{" ".join(classes)}"' if classes else ""
        sec = f' data-sec="{key}"' if key in SECTION_BY_KEY else ""
        items.append(f'<a href="{prefix}{href}"{sec}{cls}>{label}</a>')
    return "\n".join(items)


def page_group(section_key: str, out_rel: str) -> str:
    """Subcarpeta de la secció (p. ex. 'sa1', 'solucionari') o '' si és a l'arrel."""
    parts = out_rel.split("/")
    return parts[1] if len(parts) >= 3 else ""


def group_sort_key(gk: str):
    if gk in GROUP_LABELS:          # material transversal: sempre primer
        return (0, 0, gk)
    pr = PROJECTE_BY_SLUG.get(gk)
    if pr is not None:              # projecte trimestral: darrere la seva SA
        return (1, pr["after_sa"], f"z{pr['num']}")
    sa = detect_sa(gk)
    if sa is not None:
        return (1, sa, gk)
    if gk == "solucionari":
        return (3, 0, gk)
    return (2, 0, gk)


def group_label(gk: str) -> str:
    if gk in GROUP_LABELS:
        return GROUP_LABELS[gk]
    pr = PROJECTE_BY_SLUG.get(gk)
    if pr is not None:
        return f"{pr['emoji']} {pr['nom']}"
    sa = detect_sa(gk)
    if sa is not None:
        return f"SA{sa} · {SA_TITLES.get(sa, '')}".strip(" ·")
    return gk.replace("-", " ").capitalize() if gk else ""


def group_tri(gk: str):
    pr = PROJECTE_BY_SLUG.get(gk)
    if pr is not None:
        return pr["tri"]
    sa = detect_sa(gk)
    return sa_trimestre(sa) if sa else None


def short_label(title: str) -> str:
    """Etiqueta curta per al sidebar: talla el títol al primer subtítol."""
    for sep in (" — ", " · *", "  ·  "):
        if sep in title:
            return title.split(sep)[0].strip()
    return title


def _link(href, label, actiu, tri=None, docent=False, amagat=False):
    cls = ' class="actiu"' if actiu else ""
    li_classes = [c for c, on in (("nomes-docent", docent),
                                  ("amagat-alumnat", amagat)) if on]
    li_cls = f' class="{" ".join(li_classes)}"' if li_classes else ""
    dot = f' <span class="tri-dot" data-tri="{tri}"></span>' if tri else ""
    return f'<li{li_cls}><a href="{href}"{cls}>{label}{dot}</a></li>'


def sidebar_html(section_key: str, current_out: str, pages: list[Page]) -> str:
    if section_key == "inici" or section_key in HUB_KEYS:
        return ""
    root_index = f"{section_key}/index.html"
    sec_pages = [p for p in pages if p.section == section_key and p.out_rel != root_index
                 and p.kind != "practica"]  # les pràctiques pengen de la pàgina Codi

    groups: dict[str, list[Page]] = {}
    for p in sec_pages:
        groups.setdefault(page_group(section_key, p.out_rel), []).append(p)

    out = ['<nav class="sidebar-nav" aria-label="Pàgines de la secció">']
    out.append(f'<p class="sidebar-titol">{SECTION_BY_KEY[section_key]["title"]}</p>')

    # Presentació (índex de la secció)
    out.append("<ul class=\"sb-top\">")
    out.append(_link(rel_url(current_out, root_index), "Presentació",
                     current_out == root_index))
    # pàgines soltes a l'arrel de la secció
    for p in sorted(groups.pop("", []), key=lambda p: p.out_rel):
        out.append(_link(rel_url(current_out, p.out_rel), html.escape(short_label(p.title)),
                         p.out_rel == current_out, p.trimester,
                         docent=(p.public == "docent")))
    out.append("</ul>")

    # grups (subcarpetes): sidebar compacte. Només el grup actiu (la SA on
    # ets) es desplega amb totes les seves pàgines; la resta de SA es redueixen
    # a un sol enllaç a la seva portada, per alleugerir el lateral i el pes de
    # cada HTML.
    for gk in sorted(groups, key=group_sort_key):
        gps = groups[gk]
        gps.sort(key=lambda p: (0 if p.kind == "index" else 1, doc_ordre(p)))
        in_group = any(p.out_rel == current_out for p in gps)
        idx = next((p for p in gps if p.kind == "index"), None)
        tri = group_tri(gk)
        dot = f'<span class="tri-dot" data-tri="{tri}"></span>' if tri else ""
        grp_docent = bool(gps) and all(p.public == "docent" for p in gps)
        if not in_group and idx is not None:
            link_cls = "sb-grup-link nomes-docent" if grp_docent else "sb-grup-link"
            out.append(f'<a class="{link_cls}" href="{rel_url(current_out, idx.out_rel)}">'
                       f'<span>{html.escape(group_label(gk))}</span>{dot}</a>')
            # Si l'índex del grup és docent però el grup té pàgines públiques,
            # la vista alumnat necessita un destí públic: es dupliquen els
            # enllaços (nomes-docent → índex · nomes-alumnat → 1a pàgina pública).
            if not grp_docent and idx.public == "docent":
                publica = next((p for p in gps if p.public == "alumnat"), None)
                if publica is not None:
                    out[-1] = out[-1].replace('class="sb-grup-link"',
                                              'class="sb-grup-link nomes-docent"')
                    out.append(f'<a class="sb-grup-link nomes-alumnat" '
                               f'href="{rel_url(current_out, publica.out_rel)}">'
                               f'<span>{html.escape(group_label(gk))}</span>{dot}</a>')
            continue
        open_attr = " open" if in_group else ""
        summary = f'<summary><span>{html.escape(group_label(gk))}</span>{dot}</summary>'
        items = []
        for p in gps:
            if p is idx:
                label = "Presentació"
            elif p.kind == "code":
                label = "Codi"
            else:
                label = html.escape(short_label(p.title))
            es_consulta = any(k in p.out_rel.lower() for k in NOMES_CONSULTA)
            if p.out_rel == current_out:
                es_consulta = False
            items.append(_link(rel_url(current_out, p.out_rel), label,
                               p.out_rel == current_out,
                               docent=(p.public == "docent"),
                               amagat=es_consulta))
        grp_cls = "sb-grup nomes-docent" if grp_docent else "sb-grup"
        out.append(f'<details class="{grp_cls}"{open_attr}>{summary}<ul>'
                   + "".join(items) + "</ul></details>")

    out.append("</nav>")
    return "\n".join(out)


def toc_html(md: markdown.Markdown) -> str:
    tokens = getattr(md, "toc_tokens", [])
    flat = []

    def walk(items, level):
        for it in items:
            if level <= 2:  # h2 i h3
                flat.append((level, it["id"], it["name"]))
            walk(it.get("children", []), level + 1)

    walk(tokens, 1)
    flat = [t for t in flat if t[0] in (1, 2)]
    if len(flat) < 3:
        return ""
    out = ['<nav class="toc" aria-label="En aquesta pàgina"><p class="toc-titol">En aquesta pàgina</p><ul>']
    for level, _id, name in flat:
        out.append(f'<li class="toc-l{level}"><a href="#{_id}">{html.escape(name)}</a></li>')
    out.append("</ul></nav>")
    return "\n".join(out)


def breadcrumb_html(out_rel: str, section_key: str, title: str,
                    all_outs: set | None = None) -> str:
    prefix = depth_prefix(out_rel)
    crumbs = [f'<a href="{prefix}index.html">Inici</a>']
    if section_key != "inici":
        sec = SECTION_BY_KEY.get(section_key)
        if sec:
            crumbs.append(f'<a href="{prefix}{section_key}/index.html">{sec["title"]}</a>')
        # nivell intermedi: subcarpeta (SA o apartat) amb pàgina índex pròpia
        gk = page_group(section_key, out_rel)
        if gk and all_outs:
            gk_index = f"{section_key}/{gk}/index.html"
            if gk_index != out_rel and gk_index in all_outs:
                crumbs.append(f'<a href="{rel_url(out_rel, gk_index)}">'
                              f'{html.escape(group_label(gk))}</a>')
    crumbs.append(f'<span aria-current="page">{html.escape(title)}</span>')
    return '<nav class="breadcrumb" aria-label="Ubicació">' + \
        ' <span class="sep">/</span> '.join(crumbs) + "</nav>"


def pauta_html(section_key: str) -> str:
    """Caixa «Com s'usa aquesta secció» de l'índex de cada secció."""
    sec = SECTION_BY_KEY.get(section_key)
    steps = sec.get("pauta") if sec else None
    if not steps:
        return ""
    items = "".join(f"<li>{s}</li>" for s in steps)
    return ('<div class="pauta-box"><p class="pauta-tit">📋 Com s\'usa aquesta secció</p>'
            f'<ol>{items}</ol></div>')


# --- Fil transversal de cada SA (Programació ↔ Classes ↔ Codi ↔ Reptes ↔ …) ---
SA_PROVA = {3: ("Prova T1", "avaluacio/prova-practica-t1.html"),
            6: ("Prova T2", "avaluacio/prova-practica-t2.html"),
            9: ("Prova T3", "avaluacio/prova-practica-t3.html")}


def build_sa_fil(pages: list[Page]) -> dict[int, list[tuple[str, str]]]:
    """Per a cada SA (1-9), la llista ordenada de (etiqueta, out_rel) del seu fil."""
    outs = {p.out_rel for p in pages}
    prog: dict[int, str] = {}
    reptes: dict[int, str] = {}
    for p in pages:
        if p.section == "programacio" and p.kind == "doc":
            sa = detect_sa(p.src.name)
            if sa and sa not in prog:
                prog[sa] = p.out_rel
        if p.section == "reptes" and p.kind == "doc" and p.src.name.startswith("Reptes_SA"):
            sa = detect_sa(p.src.name)
            if sa and sa not in reptes:
                reptes[sa] = p.out_rel
    fil: dict[int, list[tuple[str, str]]] = {}
    for sa in range(1, 10):
        items: list[tuple[str, str]] = []
        if sa in prog:
            items.append(("📘 Programació", prog[sa]))
        if f"classes/sa{sa}/index.html" in outs:
            items.append(("🧑‍🏫 Guia i fitxes", f"classes/sa{sa}/index.html"))
        if f"classes/sa{sa}/codi.html" in outs:
            items.append(("💻 Codi", f"classes/sa{sa}/codi.html"))
        if sa in reptes:
            items.append(("🎯 Reptes", reptes[sa]))
        if f"reptes/solucionari/sa{sa}/codi.html" in outs:
            items.append(("🔑 Solucionari", f"reptes/solucionari/sa{sa}/codi.html"))
        if sa in SA_PROVA and SA_PROVA[sa][1] in outs:
            items.append((f"📝 {SA_PROVA[sa][0]}", SA_PROVA[sa][1]))
        if items:
            fil[sa] = items
    return fil


def stepper_html(section_key: str, out_rel: str) -> str:
    """Barra de progrés del curs (SA0 → SA9, incloent-hi els 3 projectes
    trimestrals) per a les pàgines de Classes.
    Ressalta la SA actual i acoloreix cada pas segons el seu trimestre
    (reutilitza `data-tri`). A les pàgines sense SA (índex, transversal) no
    ressalta cap pas i serveix de navegació ràpida entre unitats."""
    if section_key != "classes":
        return ""
    cur = detect_sa(out_rel)
    cur_pr = page_group("classes", out_rel)
    passos: list[tuple] = []           # ("sa", n) | ("pr", dict)
    for sa in range(0, 10):
        passos.append(("sa", sa))
        for pr in PROJECTES:
            if pr["after_sa"] == sa:
                passos.append(("pr", pr))
    steps = []
    for tipus, val in passos:
        if tipus == "sa":
            sa = val
            tri = 0 if sa == 0 else sa_trimestre(sa)
            href = rel_url(out_rel, f"classes/sa{sa}/index.html")
            actiu = " actiu" if sa == cur else ""
            aria = ' aria-current="page"' if sa == cur else ""
            steps.append(f'<a class="step{actiu}" data-tri="{tri}" href="{href}"{aria} '
                         f'title="SA{sa} · {html.escape(SA_TITLES.get(sa, ""))}">'
                         f'<span class="step-ic">{SA_ICONES.get(sa, "")}</span>'
                         f'<span class="step-n">SA{sa}</span></a>')
        else:
            pr = val
            href = rel_url(out_rel, f"classes/{pr['slug']}/index.html")
            actiu = " actiu" if cur_pr == pr["slug"] else ""
            aria = ' aria-current="page"' if cur_pr == pr["slug"] else ""
            steps.append(f'<a class="step{actiu}" data-tri="{pr["tri"]}" href="{href}"{aria} '
                         f'title="{html.escape(pr["nom"])}">'
                         f'<span class="step-ic">{pr["emoji"]}</span>'
                         f'<span class="step-n">T{pr["num"]}</span></a>')
    return ('<nav class="stepper" aria-label="Progrés del curs (SA i projectes)">'
            + "".join(steps) + "</nav>")


def sa_fil_html(sa: int, current_out: str, fil: dict) -> str:
    """Barra «Tot sobre la SAx» amb enllaços creuats entre seccions."""
    items = fil.get(sa)
    if not items or len(items) < 2:
        return ""
    tri = sa_trimestre(sa)
    pills = []
    for label, out in items:
        dc = " nomes-docent" if label[:1] in "📘🔑📝" else ""
        if out == current_out:
            pills.append(f'<span class="sa-fil-pill actiu{dc}">{label}</span>')
        else:
            pills.append(f'<a class="sa-fil-pill{dc}" href="{rel_url(current_out, out)}">{label}</a>')
    return (f'<nav class="sa-fil" aria-label="Tot sobre la SA{sa}">'
            f'<span class="sa-fil-tit"><span class="tri-dot" data-tri="{tri}"></span>'
            f'Tot sobre la <strong>SA{sa}</strong>:</span>' + "".join(pills) + "</nav>")


# --- Seqüències «anterior / següent» (itinerari pautat dins de cada bloc) ---
# Ordre canònic dels materials d'una SA: primer el camí de l'alumnat
# (fitxa → suports → checklist → codi), després el material opcional
# (ampliada, qüestionari) i el del docent. "__codi__" és el rang de les
# pàgines de codi (kind == "code").
DOC_ORDRE_CLAUS = ["fil-conductor", "projecte-t",
                   "guia-docent", "vocabulari", "primers-passos", "guia", "diagnostica",
                   "fitxa-alumnat", "banc-de-reptes", "reptes-proposats", "planificacio",
                   "prova", "normes", "esquemes", "connexions",
                   "recursos", "diagrama", "exemple", "__codi__", "auditoria",
                   "practica",
                   "poster", "dossier", "questionari", "checklist-alumnat",
                   "fitxa-ampliada", "checklist-docent"]

# Material que existeix per a l'alumnat però NOMÉS com a consulta opcional
# («Si vols més»): fora del pager i del sidebar en vista alumnat. El
# qüestionari de conceptes SÍ que és al camí (pas «Consolida»: recuperació
# abans de l'autoavaluació).
NOMES_CONSULTA = ("fitxa-ampliada", "recursos-video")


def doc_ordre(p: Page):
    """Ordre pedagògic dels materials d'una SA (l'ordre de la ruta)."""
    n = p.out_rel.lower()
    if p.kind == "code":
        return (DOC_ORDRE_CLAUS.index("__codi__"), n)
    for i, clau in enumerate(DOC_ORDRE_CLAUS):
        if clau != "__codi__" and clau in n:
            return (i, n)
    return (len(DOC_ORDRE_CLAUS), n)


def build_sequences(pages: list[Page]) -> dict[str, str]:
    """Mapa out_rel -> HTML del paginador (‹ anterior · següent ›)."""
    seqs: list[tuple[str, list[Page]]] = []

    def add_seq(label: str, items: list[Page]):
        if len(items) >= 2:
            seqs.append((label, items))

    # Programació didàctica: 00 → 18 (l'ordre alfabètic ja és el pedagògic)
    prog = sorted([p for p in pages if p.section == "programacio" and p.kind == "doc"
                   and page_group("programacio", p.out_rel) == ""],
                  key=lambda p: p.out_rel)
    add_seq("Programació didàctica", prog)

    # Classes: dins de cada SA, presentació → guia → fitxes → esquemes → codi.
    # Els projectes trimestrals s'intercalen amb ponts: SA3→PT1→SA4, SA6→PT2→PT3→SA7.
    blocs: dict[str, tuple[str, list[Page]]] = {}   # clau grup -> (label, items)
    for sa in range(0, 10):
        grp = [p for p in pages if p.section == "classes" and p.kind != "practica"
               and page_group("classes", p.out_rel) == f"sa{sa}"]
        if not grp:
            continue
        idx = [p for p in grp if p.kind == "index"]
        rest = sorted([p for p in grp if p.kind != "index"], key=doc_ordre)
        blocs[f"sa{sa}"] = (f"SA{sa}", idx + rest)
    for pr in PROJECTES:
        grp = [p for p in pages if p.section == "classes"
               and page_group("classes", p.out_rel) == pr["slug"]]
        if not grp:
            continue
        idx = [p for p in grp if p.kind == "index"]
        rest = sorted([p for p in grp if p.kind != "index"], key=doc_ordre)
        blocs[pr["slug"]] = (f"{pr['emoji']} Projecte T{pr['num']}", idx + rest)

    PONTS = [("sa3", "projecte-t1"), ("projecte-t1", "sa4"),
             ("sa6", "projecte-t2"), ("projecte-t2", "projecte-t3"),
             ("projecte-t3", "sa7")]
    pont_next = {a: b for a, b in PONTS if a in blocs and b in blocs}
    pont_prev = {b: a for a, b in PONTS if a in blocs and b in blocs}

    # Reptes: SA1 → SA8
    rep = sorted([p for p in pages if p.section == "reptes" and p.kind == "doc"
                  and p.src.name.startswith("Reptes_SA")], key=lambda p: p.out_rel)
    add_seq("Reptes per SA", rep)

    def render_pager(label: str, items: list[Page], vista: str,
                      outer_prev: Page | None = None,
                      outer_next: Page | None = None) -> dict[str, str]:
        out: dict[str, str] = {}
        for i, p in enumerate(items):
            prev_p = items[i - 1] if i > 0 else outer_prev
            next_p = items[i + 1] if i < len(items) - 1 else outer_next
            parts = [f'<nav class="pager" data-pager-vista="{vista}" aria-label="Itinerari">']
            if prev_p:
                t = "Presentació" if prev_p.kind == "index" else ("Codi" if prev_p.kind == "code" else prev_p.title)
                parts.append(f'<a class="pager-a prev" href="{rel_url(p.out_rel, prev_p.out_rel)}">'
                             f'<span class="pager-dir">← Anterior</span>'
                             f'<span class="pager-tit">{html.escape(t)}</span></a>')
            else:
                parts.append('<span class="pager-a buit"></span>')
            parts.append(f'<span class="pager-seq">{html.escape(label)} · {i + 1}/{len(items)}</span>')
            if next_p:
                t = "Presentació" if next_p.kind == "index" else ("Codi" if next_p.kind == "code" else next_p.title)
                parts.append(f'<a class="pager-a next" href="{rel_url(p.out_rel, next_p.out_rel)}">'
                             f'<span class="pager-dir">Següent →</span>'
                             f'<span class="pager-tit">{html.escape(t)}</span></a>')
            else:
                parts.append('<span class="pager-a buit"></span>')
            parts.append("</nav>")
            out[p.out_rel] = "".join(parts)
        return out

    # Dues variants per seqüència: completa (vista docent) i només-alumnat.
    pager: dict[str, str] = {}
    for label, items in seqs:
        full = render_pager(label, items, "docent")
        for out_rel, htmlp in full.items():
            pager[out_rel] = htmlp
        alum_items = [p for p in items if p.public == "alumnat"
                      and not any(k in p.out_rel.lower() for k in NOMES_CONSULTA)]
        if len(alum_items) >= 2:
            alum = render_pager(label, alum_items, "alumnat")
            for out_rel, htmlp in alum.items():
                pager[out_rel] = pager.get(out_rel, "") + htmlp

    def vista_items(items: list[Page], vista: str) -> list[Page]:
        if vista == "docent":
            return items
        return [p for p in items if p.public == "alumnat"
                and not any(k in p.out_rel.lower() for k in NOMES_CONSULTA)]

    # Blocs de Classes (SA + projectes), amb ponts entre grups adjacents.
    for gk, (label, items) in blocs.items():
        for vista in ("docent", "alumnat"):
            its = vista_items(items, vista)
            op = on = None
            if gk in pont_prev:
                prev_its = vista_items(blocs[pont_prev[gk]][1], vista)
                op = prev_its[-1] if prev_its else None
            if gk in pont_next:
                next_its = vista_items(blocs[pont_next[gk]][1], vista)
                on = next_its[0] if next_its else None
            if len(its) < 2 and not (op or on):
                continue
            full = render_pager(label, its, vista, outer_prev=op, outer_next=on)
            if vista == "docent":
                for out_rel, htmlp in full.items():
                    pager[out_rel] = htmlp
            else:
                for out_rel, htmlp in full.items():
                    pager[out_rel] = pager.get(out_rel, "") + htmlp
    return pager


def page_shell(*, out_rel, section_key, title, content_html, toc="",
               tri=None, pages, pdf_href=None, public="alumnat"):
    prefix = depth_prefix(out_rel)
    sec = SECTION_BY_KEY.get(section_key)
    accent_attr = f' data-section="{section_key}"'
    tri_badge = ""
    if tri:
        tri_badge = (f'<span class="badge-tri" data-tri="{tri}">'
                     f'{TRIMESTRES[tri]["label"]}</span>')
    pdf_block = ""
    print_cap = ""
    if pdf_href:
        pdf_block = (f'<div class="pagina-eines"><a class="baixa-pdf" href="{pdf_href}" '
                     f'download>⬇ Baixa PDF</a></div>')
        print_cap = (f'<div class="print-cap"><div class="pc-site">{html.escape(SITE_TITLE)}</div>'
                     f'<div class="pc-tit">{html.escape(title)}</div></div>')
    # Material del docent: fora dels cercadors. La porta de contrasenya és
    # JavaScript i els robots no l'executen; sense això, l'alumnat hi podria
    # arribar per Google sense passar mai pel commutador de vista.
    noindex = ('<meta name="robots" content="noindex, nofollow">\n'
               if public == "docent" else "")
    sidebar = sidebar_html(section_key, out_rel, pages)
    stepper = stepper_html(section_key, out_rel)
    has_sidebar = "amb-sidebar" if sidebar else "sense-sidebar"
    toc_block = toc or ""
    layout_class = "amb-toc" if toc_block else "sense-toc"

    return f"""<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · {html.escape(SITE_TITLE)}</title>
<meta name="description" content="{html.escape(SITE_TAGLINE)}">
{noindex}<link rel="stylesheet" href="{prefix}assets/css/estil.css">
<link rel="stylesheet" href="{prefix}assets/css/pygments.css">
<script>(function(){{try{{var d=document.documentElement,t=localStorage.getItem('tema');if(t==='fosc'||(!t&&window.matchMedia('(prefers-color-scheme: dark)').matches))d.setAttribute('data-tema','fosc');var m=localStorage.getItem('mida');if(m&&m!=='100')d.setAttribute('data-mida',m);if(localStorage.getItem('font')==='llegible')d.setAttribute('data-font','llegible');var v=localStorage.getItem('vista')||'alumnat';d.setAttribute('data-vista',v);}}catch(e){{}}}})();</script>
</head>
<body{accent_attr} data-public="{public}" class="{has_sidebar} {layout_class}">
<a class="skip" href="#contingut">Salta al contingut</a>
<header class="topbar">
  <button class="menu-btn" aria-label="Obre el menú" aria-expanded="false">☰</button>
  <a class="brand" href="{prefix}index.html"><span class="brand-mark">◆</span> Robòtica <span class="brand-sub">1r Batx</span></a>
  <nav class="topnav" aria-label="Seccions">
    {topnav_html(out_rel, section_key)}
  </nav>
  <div class="topbar-eines">
    <div class="cercador">
      <input type="search" id="cerca" placeholder="Cerca…" autocomplete="off" aria-label="Cerca al web">
      <div id="cerca-resultats" class="cerca-resultats" hidden></div>
    </div>
    <div class="a11y-grup" role="group" aria-label="Ajustos de lectura">
      <button class="a11y-btn mida-menys" aria-label="Redueix la mida del text" title="Text més petit">A−</button>
      <button class="a11y-btn mida-mes" aria-label="Augmenta la mida del text" title="Text més gran">A+</button>
      <button class="a11y-btn font-toggle" aria-pressed="false" aria-label="Tipografia de lectura fàcil" title="Tipografia de lectura fàcil">Aa</button>
    </div>
    <button class="vista-btn" aria-label="Canvia entre vista d'alumnat i de docent" aria-pressed="false" title="Vista alumnat / docent">
      <span class="vista-ic-alumnat">🎓 Alumnat</span>
      <span class="vista-ic-docent">👩‍🏫 Docent</span>
    </button>
    <button class="tema-btn" aria-label="Canvia el tema clar/fosc" title="Tema clar/fosc">◐</button>
  </div>
</header>
<div class="layout">
  <aside class="sidebar">{sidebar}</aside>
  <main id="contingut">
    <div class="avis-docent">📎 Aquesta pàgina és <strong>material per al docent</strong>. Actives la vista docent al botó de dalt.</div>
    {print_cap}
    {breadcrumb_html(out_rel, section_key, title, {p.out_rel for p in pages})}
    {stepper}
    {pdf_block}
    {tri_badge}
    <article class="prose">
{content_html}
    </article>
  </main>
  {toc_block}
</div>
<footer class="peu">
  <p>{html.escape(SITE_TITLE)} · Tomeu Riera, amb l'assistència de <a href="https://claude.com/claude-code" target="_blank" rel="noopener">Claude Code</a> · material sota llicència <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.ca" target="_blank" rel="noopener">CC BY-SA 4.0</a>.</p>
  <p><a href="{REPO_URL}" target="_blank" rel="noopener">Repositori a GitHub</a> · web generat el {BUILD_DATE}.</p>
</footer>
<script src="{prefix}assets/js/cerca-index.js"></script>
<script src="{prefix}assets/js/lloc.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Generació de pàgines de codi
# ---------------------------------------------------------------------------
def lexer_for(path: Path):
    suf = path.suffix.lower()
    name = {".py": "python"}.get(suf, "text")
    try:
        return get_lexer_by_name(name)
    except Exception:
        return get_lexer_by_name("text")


def capcalera_codi(path: Path) -> tuple[str, str]:
    """(descripció, quan) del comentari de capçalera d'un fitxer de codi.

    La descripció és la primera línia útil (saltant la línia amb el nom del
    fitxer); «quan» és el contingut d'una línia opcional `Quan: ...`, que
    situa el fitxer a la sessió/activitat on es fa servir."""
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()[:30]
    except OSError:
        return "", ""
    nom = path.name.lower()
    desc = quan = ""
    dins_bloc = False
    for ln in lines:
        s = ln.strip()
        if not dins_bloc:
            if s.startswith("/*"):
                dins_bloc = True
                s = s[2:].strip("*/ ").strip()
            elif s.startswith(("//", "#")):
                s = s.lstrip("/#").strip()
            elif not s:
                continue
            else:
                break  # primera línia de codi real: fi de la capçalera
        else:
            if "*/" in s:
                s = s.split("*/", 1)[0]
                dins_bloc = False
            s = s.strip("* ").strip()
        if s.lower().startswith("quan:"):
            quan = s[5:].strip()
        elif s and not desc and nom not in s.lower():
            desc = s
        if desc and quan:
            break
    return desc, quan


def render_code_page(group: dict, pages: list[Page], extra_nav: str = "") -> str:
    formatter = HtmlFormatter(cssclass="highlight", nowrap=False)
    te_practiques = any("page_out" in it for it in group["items"])
    if te_practiques:
        intro = ('Cada pràctica té la seva pàgina: què es pretén, el codi '
                 'explicat per blocs i el fitxer complet per copiar a l\'IDE.')
    else:
        intro = ('Fitxers de codi font. Desplega cada fitxer per llegir-lo i '
                 'fes servir el botó <strong>Copia</strong> per dur-lo a '
                 'l\'editor de micro:bit (Mu, Thonny o l\'editor web).')
    parts = [f'<h1>{html.escape(group["label"])}</h1>',
             f'<p class="codi-intro">{intro}</p>']
    caps = {it["anchor"]: capcalera_codi(it["path"]) for it in group["items"]}
    # índex de fitxers amb l'etiqueta «quan es fa» i la descripció de capçalera
    parts.append('<ul class="codi-llista">')
    for it in group["items"]:
        desc, quan = caps[it["anchor"]]
        if "page_out" in it:
            href = rel_url(group["out_rel"], it["page_out"])
            li = (f'<li><a href="{href}"><strong>{html.escape(it["title"])}</strong></a> '
                  f'<code>{html.escape(it["rel"])}</code>')
        else:
            li = f'<li><a href="#{it["anchor"]}"><code>{html.escape(it["rel"])}</code></a>'
        if quan:
            li += f' <span class="codi-quan">{html.escape(quan)}</span>'
        if desc and "page_out" not in it:
            li += f' — <span class="codi-desc">{html.escape(desc)}</span>'
        parts.append(li + "</li>")
    parts.append("</ul>")
    for it in group["items"]:
        if "page_out" in it:
            continue  # el codi complet viu a la pàgina de la pràctica
        code = it["path"].read_text(encoding="utf-8", errors="replace")
        highlighted = highlight(code, lexer_for(it["path"]), formatter)
        desc, quan = caps[it["anchor"]]
        quan_html = (f'<span class="codi-quan">{html.escape(quan)}</span>'
                     if quan else "")
        desc_html = (f'<span class="codi-desc">{html.escape(desc)}</span>'
                     if desc else "")
        parts.append(
            f'<details class="codi-bloc" id="{it["anchor"]}">'
            f'<summary class="codi-cap"><code class="codi-nom">{html.escape(it["rel"])}</code>'
            f'{quan_html}{desc_html}'
            f'<button class="copia-btn" type="button">Copia</button></summary>'
            f'<div class="codi-cos">{highlighted}</div></details>'
        )
    if extra_nav:
        parts.append(extra_nav)
    content = "\n".join(parts)
    return page_shell(out_rel=group["out_rel"], section_key=group["section"],
                      title=group["label"], content_html=content,
                      tri=group["tri"], pages=pages, public=group.get("public", "alumnat"))


def pager_practiques(group: dict, practs: list[dict], i: int) -> str:
    """Paginador ‹ pràctica anterior · índex · següent › d'una pàgina de pràctica."""
    cur = practs[i]
    prev_p = practs[i - 1] if i > 0 else None
    next_p = practs[i + 1] if i < len(practs) - 1 else None
    parts = ['<nav class="pager" aria-label="Pràctiques de la SA">']
    if prev_p:
        parts.append(f'<a class="pager-a prev" href="{rel_url(cur["page_out"], prev_p["page_out"])}">'
                     f'<span class="pager-dir">← Anterior</span>'
                     f'<span class="pager-tit">{html.escape(prev_p["title"])}</span></a>')
    else:
        parts.append('<span class="pager-a buit"></span>')
    idx_href = rel_url(cur["page_out"], group["out_rel"])
    parts.append(f'<a class="pager-seq" href="{idx_href}">{html.escape(group["label"])} '
                 f'· {i + 1}/{len(practs)}</a>')
    if next_p:
        parts.append(f'<a class="pager-a next" href="{rel_url(cur["page_out"], next_p["page_out"])}">'
                     f'<span class="pager-dir">Següent →</span>'
                     f'<span class="pager-tit">{html.escape(next_p["title"])}</span></a>')
    else:
        parts.append('<span class="pager-a buit"></span>')
    parts.append("</nav>")
    return "".join(parts)


def render_practica_page(item: dict, group: dict, pages: list[Page], md_map: dict,
                         code_map: dict, sim_map: dict, copied_imgs: dict,
                         md_title_map: dict, extra_nav: str = "") -> tuple[str, str]:
    """Pàgina pròpia d'una pràctica: l'EXPLICACIO.md (per què es fa + codi per
    blocs) i, al final, el fitxer complet plegat amb el botó Copia. El codi
    sencer mai apareix desplegat d'entrada: primer la comprensió."""
    formatter = HtmlFormatter(cssclass="highlight", nowrap=False)
    text = strip_github_only(item["expl"].read_text(encoding="utf-8"))
    md = make_md()
    body = wrap_tables(md.convert(text))
    body = rewrite_links(body, item["expl"], item["page_out"], md_map, code_map,
                         sim_map, copied_imgs, md_title_map)
    toc = toc_html(md)
    code = item["path"].read_text(encoding="utf-8", errors="replace")
    highlighted = highlight(code, lexer_for(item["path"]), formatter)
    _desc, quan = capcalera_codi(item["path"])
    quan_html = (f'<span class="codi-quan">{html.escape(quan)}</span>'
                 if quan else "")
    body += (
        '\n<h2 id="codi-complet">El codi complet</h2>'
        f'<details class="codi-bloc" id="{item["anchor"]}">'
        f'<summary class="codi-cap"><code class="codi-nom">{html.escape(item["rel"])}</code>'
        f'{quan_html}'
        f'<button class="copia-btn" type="button">Copia</button></summary>'
        f'<div class="codi-cos">{highlighted}</div></details>'
    )
    if extra_nav:
        body += "\n" + extra_nav
    full = page_shell(out_rel=item["page_out"], section_key=group["section"],
                      title=item["title"], content_html=body, toc=toc,
                      tri=group["tri"], pages=pages, public="alumnat")
    return full, body


def render_sim_page(group: dict, pages: list[Page]) -> str:
    formatter = HtmlFormatter(cssclass="highlight", nowrap=False)
    folder = group["folder"]
    relpath = str(folder.resolve().relative_to(ROOT.resolve())).replace("\\", "/")
    tree = TREE_BASE + urllib.parse.quote(relpath)
    mena = "Repte" if group["is_repte"] else "Pràctica"
    parts = [f'<h1>{html.escape(group["title"])}</h1>',
             f'<p class="codi-intro">Simulació Wokwi ({mena.lower()}). '
             f'Pots reproduir-la a <a href="https://wokwi.com/" target="_blank" rel="noopener">wokwi.com</a>: '
             f'crea un projecte nou i enganxa-hi el contingut de <code>diagram.json</code> i del '
             f'fitxer de codi. <a href="{tree}" target="_blank" rel="noopener">Veure la carpeta a GitHub ↗</a></p>']
    for f in group["files"]:
        code = f.read_text(encoding="utf-8", errors="replace")
        lang = "json" if f.suffix.lower() == "json" else None
        try:
            lexer = get_lexer_by_name(lang) if lang else lexer_for(f)
        except Exception:
            lexer = lexer_for(f)
        highlighted = highlight(code, lexer, formatter)
        anchor = slugify(f.name)
        parts.append(
            f'<section class="codi-bloc" id="{anchor}">'
            f'<header class="codi-cap"><code class="codi-nom">{html.escape(f.name)}</code>'
            f'<button class="copia-btn" type="button">Copia</button></header>'
            f'<div class="codi-cos">{highlighted}</div></section>'
        )
    content = "\n".join(parts)
    return page_shell(out_rel=group["out_rel"], section_key="simulacions",
                      title=group["title"], content_html=content,
                      tri=group["tri"], pages=pages, public="alumnat")


# ---------------------------------------------------------------------------
# Pàgines índex de secció (targetes)
# ---------------------------------------------------------------------------
DOC_ICONS = {".pdf": "📕", ".xlsx": "📊", ".xls": "📊", ".csv": "📊", ".ods": "📊",
             ".pptx": "📽️", ".ppt": "📽️", ".docx": "📄", ".doc": "📄", ".odt": "📄",
             ".zip": "🗜️"}


def section_documents(section_key: str, current_out: str) -> str:
    """Llista de documents de la secció: visor in-situ per als de l'arrel,
    enllaç a GitHub per als de subcarpetes (arxius voluminosos)."""
    sec = SECTION_BY_KEY.get(section_key)
    if not sec:
        return ""
    src_dir = ROOT / sec["src"]
    if not src_dir.exists():
        return ""
    docs = sorted([p for p in src_dir.rglob("*") if p.suffix.lower() in DOC_EXT
                   and not any(part.startswith("_")
                               for part in p.relative_to(src_dir).parts)])
    if not docs:
        return ""
    prefix = depth_prefix(current_out)
    root_docs = [d for d in docs if d.parent == src_dir]
    subfolders: dict[str, list] = {}
    for d in docs:
        if d.parent != src_dir:
            subfolders.setdefault(d.relative_to(src_dir).parts[0], []).append(d)

    cards = []
    for d in root_docs:
        relpath = str(d.relative_to(ROOT)).replace("\\", "/")
        raw = RAW_BASE + urllib.parse.quote(relpath)
        title = d.stem.replace("_", " ")
        ext = d.suffix.lower().lstrip(".")
        href = (prefix + "visor.html?u=" + urllib.parse.quote(raw, safe="")
                + "&t=" + urllib.parse.quote(title, safe="") + "&x=" + ext)
        ic = DOC_ICONS.get(d.suffix.lower(), "📄")
        cards.append(f'<a class="card" href="{href}"><span class="card-ic">{ic}</span>'
                     f'<span class="card-tit">{html.escape(title)} '
                     f'<small class="doc-ext">{ext}</small></span></a>')
    for folder, items in sorted(subfolders.items()):
        tree = TREE_BASE + urllib.parse.quote(f"{sec['src']}/{folder}")
        cards.append(f'<a class="card doc-folder" href="{tree}" target="_blank" rel="noopener">'
                     f'<span class="card-ic">📁</span><span class="card-tit">{html.escape(folder)} '
                     f'<small>({len(items)} fitxers · obre a GitHub ↗)</small></span></a>')
    return ('<h2 class="seccio-sep">Documents</h2>'
            '<div class="card-grid">' + "\n".join(cards) + "</div>")
def section_gallery(section_key: str, current_out: str, copied_imgs: dict) -> str:
    """Galeria amb les imatges presents a la carpeta font de la secció."""
    sec = SECTION_BY_KEY.get(section_key)
    if not sec:
        return ""
    src_dir = ROOT / sec["src"]
    imgs = sorted([p for p in src_dir.rglob("*") if p.suffix.lower() in IMG_EXT
                   and not any(part.startswith("_")
                               for part in p.relative_to(src_dir).parts)])
    if not imgs:
        return ""
    prefix = depth_prefix(current_out)
    tiles = []
    for img in imgs:
        name = copy_image(img, copied_imgs)
        cap = html.escape(img.stem.replace("_", " ").replace("-", " "))
        tiles.append(f'<figure class="galeria-item"><img src="{prefix}assets/img/{name}" '
                     f'alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>')
    return ('<h2 class="seccio-sep">Imatges i materials</h2>'
            '<div class="galeria">' + "\n".join(tiles) + "</div>")


def page_sa(p: Page):
    return detect_sa(p.src.name) or detect_sa(p.out_rel)


def doc_card(href, title, kind="doc", tri=None, docent=False):
    icona = "💻" if kind == "code" else "📄"
    badge = (f'<span class="badge-tri mini" data-tri="{tri}">{TRIMESTRES[tri]["label"]}</span>'
             if tri else "")
    cls = "card nomes-docent" if docent else "card"
    return (f'<a class="{cls}" href="{href}"><span class="card-ic">{icona}</span>'
            f'<span class="card-tit">{html.escape(title)}</span>{badge}</a>')


def sa_hub_card(href, sa, name, meta, tri):
    ic = SA_ICONES.get(sa, "📄") if isinstance(sa, int) else "📄"
    prod = SA_PRODUCTES.get(sa) if isinstance(sa, int) else None
    prod_html = f'<span class="sa-prod">{html.escape(prod)}</span>' if prod else ""
    meta_html = f'<span class="sa-meta">{html.escape(meta)}</span>' if meta else ""
    num_html = f'<span class="sa-num">SA{sa}</span>' if sa != "" else ""
    return (f'<a class="sa-card" href="{href}" data-tri="{tri}">'
            f'<span class="sa-ic" aria-hidden="true">{ic}</span>'
            f'<span class="sa-body">{num_html}'
            f'<span class="sa-nom">{html.escape(name)}</span>'
            f'{prod_html}{meta_html}</span></a>')


def tri_blocks_html(entries: list[tuple]) -> str:
    """entries: llista de (tri, sa_o_ordre, card_html)."""
    if not entries:
        return ""
    blocks = []
    for t, info in TRIMESTRES.items():
        cards = [c for (tri, _o, c) in sorted(entries, key=lambda e: (e[1],)) if tri == t]
        if not cards:
            continue
        blocks.append(
            f'<div class="tri-block" data-tri="{t}">'
            f'<h3 class="tri-tit"><span class="tri-pastilla" data-tri="{t}"></span>{info["label"]}</h3>'
            f'<div class="sa-grid">{"".join(cards)}</div></div>'
        )
    return ('<h2 class="seccio-sep">Situacions d\'aprenentatge</h2>'
            '<div class="tri-wrap">' + "".join(blocks) + "</div>")


def section_index_extra(section_key: str, current_out: str, pages: list[Page]) -> str:
    root_index = f"{section_key}/index.html"
    sec_pages = [p for p in pages if p.section == section_key and p.out_rel != root_index
                 and p.kind != "practica"]  # el recompte de materials no les inclou

    groups: dict[str, list[Page]] = {}
    for p in sec_pages:
        groups.setdefault(page_group(section_key, p.out_rel), []).append(p)
    root_pages = groups.pop("", [])

    tri_entries: list[tuple] = []        # (tri, ordre, card)
    generals: list[Page] = []
    other_blocks: list[str] = []
    transversal_blocks: list[str] = []   # material transversal (no SA): va primer
    preamble_cards: list[str] = []
    has_hubs = False

    # Pàgines soltes a l'arrel: les que tenen trimestre van a blocs de SA
    for p in sorted(root_pages, key=lambda p: p.out_rel):
        if p.trimester:
            sa = page_sa(p) or 0
            tri_entries.append((p.trimester, sa,
                                sa_hub_card(rel_url(current_out, p.out_rel), sa or "",
                                            p.title, "", p.trimester)))
        else:
            generals.append(p)

    # Subcarpetes
    for gk in sorted(groups, key=group_sort_key):
        gps = groups[gk]
        idx = next((x for x in gps if x.kind == "index"), None)
        sa = detect_sa(gk)
        pr = PROJECTE_BY_SLUG.get(gk)
        if idx and pr is not None:
            has_hubs = True
            mats = len([x for x in gps if x is not idx])
            meta = f"{mats} material{'s' if mats != 1 else ''}"
            card = (f'<a class="sa-card" href="{rel_url(current_out, idx.out_rel)}" '
                    f'data-tri="{pr["tri"]}">'
                    f'<span class="sa-ic" aria-hidden="true">{pr["emoji"]}</span>'
                    f'<span class="sa-body">'
                    f'<span class="sa-num">Projecte T{pr["num"]}</span>'
                    f'<span class="sa-nom">{html.escape(pr["curt"])}</span>'
                    f'<span class="sa-prod">{html.escape(pr["producte"])}</span>'
                    f'<span class="sa-meta">{html.escape(meta)}</span></span></a>')
            tri_entries.append((pr["tri"], pr["after_sa"] + pr["num"] / 10, card))
            continue
        if idx and sa is not None:
            has_hubs = True
            mats = len([x for x in gps if x is not idx])
            meta = f"{mats} material{'s' if mats != 1 else ''}"
            href = rel_url(current_out, idx.out_rel)
            if sa == 0:
                preamble_cards.append(sa_hub_card(href, 0, SA_TITLES[0], meta, 0))
            else:
                tri_entries.append((sa_trimestre(sa), sa,
                                    sa_hub_card(href, sa, SA_TITLES.get(sa, gk),
                                                meta, sa_trimestre(sa))))
        else:
            cards = []
            for p in sorted(gps, key=lambda p: (p.kind != "index", p.out_rel)):
                title = "Presentació" if p.kind == "index" else p.title
                cards.append(doc_card(rel_url(current_out, p.out_rel), title, p.kind))
            block = (f'<h2 class="seccio-sep">{html.escape(group_label(gk) or gk)}</h2>'
                     f'<div class="card-grid">{"".join(cards)}</div>')
            (transversal_blocks if gk in GROUP_LABELS else other_blocks).append(block)

    generals_html = ""
    if generals:
        cards = [doc_card(rel_url(current_out, p.out_rel), p.title, p.kind, p.trimester)
                 for p in generals]
        generals_html = ('<h2 class="seccio-sep">Documents i recursos</h2>'
                         '<div class="card-grid">' + "".join(cards) + "</div>")

    sa_html = tri_blocks_html(tri_entries)
    preamble_html = ""
    if preamble_cards:
        preamble_html = ('<h2 class="seccio-sep">Preàmbul</h2>'
                         '<div class="sa-grid">' + "".join(preamble_cards) + "</div>")

    # Ordre: material transversal primer; després, si hi ha SA amb pàgina pròpia
    # (Classes), les SA; si no, els documents primer.
    if has_hubs:
        ordered = transversal_blocks + [preamble_html, sa_html, generals_html] + other_blocks
    else:
        ordered = transversal_blocks + [generals_html, preamble_html, sa_html] + other_blocks
    return "\n".join([b for b in ordered if b])


def subindex_extra(section_key: str, group_key: str, current_out: str,
                   pages: list[Page]) -> str:
    """Materials d'una sola SA (pàgina índex d'una subcarpeta)."""
    gps = [p for p in pages if p.section == section_key
           and page_group(section_key, p.out_rel) == group_key
           and p.out_rel != current_out]
    if not gps:
        return ""

    # Bloc «Comença aquí» destacat, per vista
    def _find(*subs):
        return next((p for p in gps if any(s in p.out_rel.lower() for s in subs)), None)
    fitxa = _find("fitxa-alumnat")
    guia = _find("guia-docent", "guia-programacio")
    codi = next((p for p in gps if p.kind == "code"), None)
    start = []
    al = [(p, t) for p, t in [(fitxa, "Fitxa base"), (codi, "Codi")] if p]
    if al:
        cards_al = "".join(doc_card(rel_url(current_out, p.out_rel), t, p.kind) for p, t in al)
        start.append('<div class="comenca-aqui portada-alumnat">'
                     '<p class="ca-tit">▶ Comença aquí</p>'
                     f'<div class="card-grid">{cards_al}</div></div>')
    do = [(p, t) for p, t in [(guia, "Guia docent"), (fitxa, "Fitxa base")] if p]
    if do:
        cards_do = "".join(doc_card(rel_url(current_out, p.out_rel), t, p.kind) for p, t in do)
        start.append('<div class="comenca-aqui nomes-docent">'
                     '<p class="ca-tit">▶ Comença aquí</p>'
                     f'<div class="card-grid">{cards_do}</div></div>')

    cards = []
    for p in sorted(gps, key=doc_ordre):
        title = "Codi de les pràctiques" if p.kind == "code" else p.title
        cards.append(doc_card(rel_url(current_out, p.out_rel), title, p.kind,
                              docent=(p.public == "docent")))
    titol = ("Tot el material de la SA" if detect_sa(group_key) is not None
             else "Materials d'aquest apartat")
    return ("".join(start)
            + f'<div class="material-sa"><h2 class="seccio-sep">{titol}</h2>'
            + '<div class="card-grid">' + "".join(cards) + "</div></div>")


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
def find_out(pages: list[Page], src_name: str, fallback: str) -> str:
    """Sortida (out_rel) de la pàgina generada des del fitxer font `src_name`."""
    for p in pages:
        try:
            if p.src.name == src_name:
                return p.out_rel
        except Exception:
            pass
    return fallback


# ---------------------------------------------------------------------------
# Fulls imprimibles autocontinguts (HTML propi, no passa pel Markdown) que
# també es publiquen a la web: HTML interactiu + PDF per imprimir.
# Font versionada: Classes/00_General/impresos/. Vegeu generar_fulls_imprimibles.py.
# ---------------------------------------------------------------------------
IMPRESOS_SRC = ROOT / "Classes" / "00_General" / "impresos"
IMPRESOS = [
    {"file": "Blocs_Programacio_Offline.html",
     "title": "Blocs de programació offline",
     "desc": "48 blocs de codi retallables per construir programes sobre la "
             "taula, sense ordinador."},
    {"file": "Blocs_Diagrames_Flux.html",
     "title": "Peces per muntar diagrames de flux",
     "desc": "Caixes, decisions i fletxes retallables (per plastificar) per "
             "dissenyar el flux abans de programar."},
]


def copia_impresos(search_index: list) -> None:
    """Copia els HTML imprimibles a web/impresos/ i el seu PDF ja generat (i
    verificat, amb rellotge llarg per al CDN) de Classes/00_General/pdf/ a
    web/pdf/impresos/, i els posa a l'índex de cerca. No passa per generar_pdf.py:
    així el PDF web és el mateix full validat, sense risc de render incomplet."""
    out_dir = WEB / "impresos"
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf_out = WEB / "pdf" / "impresos"
    pdf_src_dir = ROOT / "Classes" / "00_General" / "pdf"
    for it in IMPRESOS:
        src = IMPRESOS_SRC / it["file"]
        if not src.exists():
            continue
        (out_dir / it["file"]).write_text(
            src.read_text(encoding="utf-8"), encoding="utf-8")
        stem = Path(it["file"]).stem
        pdf_src = pdf_src_dir / f"{stem}.pdf"
        if pdf_src.exists():
            pdf_out.mkdir(parents=True, exist_ok=True)
            shutil.copy2(pdf_src, pdf_out / f"{stem}.pdf")
        search_index.append({"t": it["title"], "s": "Recursos imprimibles",
                             "u": f"impresos/{it['file']}", "tri": None, "p": "alumnat"})


def impresos_card_html(from_out_rel: str) -> str:
    """Targeta amb enllaç a l'HTML interactiu i al PDF de cada imprimible,
    amb URL relatives a la pàgina `from_out_rel`."""
    lis = []
    for it in IMPRESOS:
        stem = Path(it["file"]).stem
        hurl = rel_url(from_out_rel, f"impresos/{it['file']}")
        purl = rel_url(from_out_rel, f"pdf/impresos/{stem}.pdf")
        lis.append(
            f'<li><a href="{hurl}"><strong>{html.escape(it["title"])}</strong></a>'
            f' — {html.escape(it["desc"])} '
            f'<a href="{purl}">(PDF per imprimir)</a></li>')
    return ('<section class="impresos-material">'
            '<h2>Material imprimible</h2>'
            '<ul>' + "".join(lis) + "</ul></section>")


def hub_urls(pages: list[Page]) -> dict[str, str]:
    """URL (des de l'arrel) dels documents que enllacen la portada i els hubs."""
    outs = {p.out_rel for p in pages}
    return {
        "met": find_out(pages, "04_Metodologia.md", "programacio/index.html"),
        "seq": find_out(pages, "08_Sequenciacio_temporal_anual.md", "programacio/index.html"),
        "rub": find_out(pages, "07_Rubriques.md", "programacio/index.html"),
        "full": find_out(pages, "Full_qualificacio_competencies.md", "avaluacio/index.html"),
        "trans": ("classes/00-general/index.html"
                  if "classes/00-general/index.html" in outs else "classes/index.html"),
        "alum": find_out(pages, "00_Avaluacio_per_alumnat.md", "avaluacio/index.html"),
        "targ": find_out(pages, "00_Targetes_rescat.md", "classes/index.html"),
        "glos": find_out(pages, "00_Glossari_tecnic.md", "classes/index.html"),
        "quad": find_out(pages, "00_Quadern_tecnic.md", "classes/index.html"),
    }


def sec_cards_html() -> str:
    """Targetes de totes les seccions (mapa complet, per a la portada i els hubs)."""
    cards = []
    for s in SECTIONS:
        cards.append(
            f'<a class="sec-card" href="{s["key"]}/index.html" data-section="{s["key"]}">'
            f'<span class="sec-ic">{s["icon"]}</span>'
            f'<span class="sec-tit">{s["title"]}</span>'
            f'<span class="sec-desc">{html.escape(s["desc"])}</span></a>'
        )
    return "".join(cards)


def sa_grid_html(pages: list[Page]) -> str:
    """Graella de les 9 SA per trimestre (portada i hub d'alumnat)."""
    outs = {p.out_rel for p in pages}
    sa_to_out = {}
    for p in pages:
        if p.section == "programacio":
            sa = detect_sa(p.src.name)
            if sa and sa not in sa_to_out:
                sa_to_out[sa] = p.out_rel
    for sa in range(1, 10):
        hub = f"classes/sa{sa}/index.html"
        if hub in outs:
            sa_to_out[sa] = hub
    tri_blocks = []
    for t, info in TRIMESTRES.items():
        cards = []
        for sa in info["sas"]:
            href = sa_to_out.get(sa, "programacio/index.html")
            cards.append(
                f'<a class="sa-card" href="{href}" data-tri="{t}">'
                f'<span class="sa-ic" aria-hidden="true">{SA_ICONES[sa]}</span>'
                f'<span class="sa-body">'
                f'<span class="sa-num">SA{sa}</span>'
                f'<span class="sa-nom">{html.escape(SA_TITLES[sa])}</span>'
                f'<span class="sa-prod">{html.escape(SA_PRODUCTES[sa])}</span>'
                f'</span></a>'
            )
        for pr in PROJECTES:
            if pr["tri"] != t:
                continue
            hub = f"classes/{pr['slug']}/index.html"
            if hub not in outs:
                continue
            card = (
                f'<a class="sa-card" href="{hub}" data-tri="{t}">'
                f'<span class="sa-ic" aria-hidden="true">{pr["emoji"]}</span>'
                f'<span class="sa-body">'
                f'<span class="sa-num">Projecte T{pr["num"]}</span>'
                f'<span class="sa-nom">{html.escape(pr["curt"])}</span>'
                f'<span class="sa-prod">{html.escape(pr["producte"])}</span>'
                f'</span></a>')
            if pr["after_sa"] < min(info["sas"]):   # rover: obre el trimestre
                cards.insert(0, card)
            else:
                cards.append(card)
        tri_blocks.append(
            f'<div class="tri-block" data-tri="{t}">'
            f'<h3 class="tri-tit"><span class="tri-pastilla" data-tri="{t}"></span>{info["label"]}</h3>'
            f'<div class="sa-grid">{"".join(cards)}</div></div>'
        )
    return '<div class="tri-wrap">\n' + "".join(tri_blocks) + "\n</div>"


def render_home(pages: list[Page]) -> str:
    u = hub_urls(pages)
    u_met, u_seq, u_rub = u["met"], u["seq"], u["rub"]
    u_full, u_trans, u_alum = u["full"], u["trans"], u["alum"]
    u_targ, u_glos = u["targ"], u["glos"]
    rutes = f"""
<h2 class="seccio-sep">Per on començo?</h2>
<p class="seccio-intro">Tria la teva situació: cada ruta et porta, pas a pas, al que necessites.</p>
<div class="ruta-grid">
  <div class="ruta-card">
    <p class="ruta-tit">🧭 Agafo la matèria per primer cop</p>
    <ol>
      <li><a href="guia-inici.html">Guia d'inici docent</a> — instal·lació, comptes, checklist i pla B.</li>
      <li><a href="{u_met}">Metodologia</a> — com és una sessió tipus i com es treballa.</li>
      <li><a href="{u_seq}">Calendari del curs</a> — seqüència de SA i pla de contingència.</li>
      <li><a href="classes/00-general/00-fil-conductor-robots.html">Els tres robots del curs</a> — el fil conductor: què es construeix cada trimestre i quan es fabrica.</li>
    </ol>
  </div>
  <div class="ruta-card">
    <p class="ruta-tit">📅 Preparo la classe de la setmana</p>
    <ol>
      <li>Obre la <a href="classes/index.html">SA que toca</a> i llegeix la <strong>guia docent</strong> de la sessió.</li>
      <li>Té a punt la <strong>fitxa base</strong> (o el PDF) i el <strong>codi</strong> de la SA.</li>
      <li>Graella d'activació, mini-checks i pòsters: <a href="{u_trans}">material transversal</a>.</li>
    </ol>
  </div>
  <div class="ruta-card">
    <p class="ruta-tit">📝 He d'avaluar</p>
    <ol>
      <li><a href="{u_rub}">Rúbriques R1-R5</a> — comparteix-les <strong>abans</strong> de començar.</li>
      <li><a href="avaluacio/index.html">Proves per trimestre</a> — T1 i T2, individuals.</li>
      <li><a href="{u_full}">Full de qualificació</a> — creua criteris i rúbriques.</li>
    </ol>
  </div>
  <div class="ruta-card">
    <p class="ruta-tit">🎓 Soc alumne/a</p>
    <ol>
      <li><a href="{u_alum}">Com s'avalua aquesta matèria</a> — d'on surt la nota, què compta i què no.</li>
      <li>A la <strong>fitxa de cada SA</strong>: la caixa «🎯 Objectius i avaluació» (què sabré fer i què lliuro).</li>
      <li><a href="{u_targ}">Targetes de rescat</a> — si t'encalles: pistes en 3 nivells, sense que ningú et faci la feina.</li>
      <li><a href="{u_glos}">Glossari català ↔ anglès</a> — els termes tècnics tal com els trobaràs quan busquis.</li>
    </ol>
    <p class="ruta-mes"><a href="alumnat.html">Entra al teu espai →</a></p>
  </div>
</div>
"""

    alumnat_block = f"""
<div class="portada-alumnat">
<section class="hero">
  <p class="hero-kicker">// {html.escape(SITE_TAGLINE)}</p>
  <h1 class="hero-titol">La teva Robòtica</h1>
  <p class="hero-lead">Tot el material per treballar les 9 situacions d'aprenentatge, en un sol lloc. Ets docent? Activa la <strong>vista docent</strong> amb el botó de dalt a la dreta.</p>
</section>
<h2 class="seccio-sep">Què vols fer?</h2>
<div class="ruta-grid">
  <div class="ruta-card"><p class="ruta-tit">📅 Treballar la SA de la setmana</p>
    <p>Obre la teva situació d'aprenentatge i comença per la fitxa.</p>
    <p class="ruta-mes"><a href="classes/index.html">Entra a les 9 SA →</a></p></div>
  <div class="ruta-card"><p class="ruta-tit">🔌 Practicar a casa</p>
    <p>Munta i prova els circuits sense cap placa, o tria un repte.</p>
    <p class="ruta-mes"><a href="simulacions/index.html">Simulacions</a> · <a href="reptes/index.html">Reptes</a></p></div>
  <div class="ruta-card"><p class="ruta-tit">🆘 M'he encallat</p>
    <p>Pistes que no et fan la feina, i els termes tècnics explicats.</p>
    <p class="ruta-mes"><a href="{u_targ}">Targetes de rescat</a> · <a href="{u_glos}">Glossari</a></p></div>
  <div class="ruta-card"><p class="ruta-tit">📓 El meu quadern tècnic</p>
    <p>El teu diari de treball: compta el 25 % i el pots consultar a les proves.</p>
    <p class="ruta-mes"><a href="{u["quad"]}">Com portar-lo + plantilla →</a></p></div>
</div>
<h2 class="seccio-sep">Les 9 situacions d'aprenentatge</h2>
{sa_grid_html(pages)}
</div>
"""

    docent_block = f"""
<div class="portada-docent nomes-docent">
<section class="hero">
  <p class="hero-kicker">// {html.escape(SITE_TAGLINE)}</p>
  <h1 class="hero-titol">Robòtica a 1r de Batxillerat</h1>
  <p class="hero-lead">9 situacions d'aprenentatge amb micro:bit i Python, en tres trimestres. Tot el material d'aula, la programació didàctica, els reptes i l'avaluació, en un sol lloc.</p>
  <div class="hero-cta">
    <a class="btn btn-primari" href="guia-inici.html">Comença per la guia d'inici</a>
  </div>
</section>
{rutes}
<h2 class="seccio-sep">Les 9 situacions d'aprenentatge</h2>
<p class="seccio-intro">Cada trimestre té el seu color. Clica una SA per anar al seu <strong>material d'aula</strong>; un cop dins, el <strong>fil de la SA</strong> t'enllaça la programació, el codi, els reptes, el solucionari i la prova.</p>
{sa_grid_html(pages)}

<h2 class="seccio-sep">Apartats</h2>
<div class="sec-grid">
{sec_cards_html()}
</div>
</div>
"""
    content = alumnat_block + docent_block
    return page_shell(out_rel="index.html", section_key="inici",
                      title="Inici", content_html=content, pages=pages,
                      public="alumnat")


# ---------------------------------------------------------------------------
# Hubs per audiència (docent i alumnat): pàgines d'orientació, no de contingut.
# Tot el que enllacen ja existeix i s'indexa; el hub és una porta d'entrada.
# ---------------------------------------------------------------------------
def render_hub_docent(pages: list[Page]) -> str:
    u = hub_urls(pages)
    content = f"""
<section class="hero hub-hero">
  <p class="hero-kicker">Espai docent</p>
  <h1 class="hero-titol">Tot el que necessites per fer la classe</h1>
  <p class="hero-lead">Aquesta pàgina no és una secció nova: és una porta d'entrada organitzada pel que fas de veritat. Comença per dalt si agafes la matèria per primer cop; salta a «Setmana a setmana» si ja hi estàs.</p>
</section>

<h2 class="seccio-sep">1 · Començo de nou</h2>
<p class="seccio-intro">La primera vegada, en aquest ordre.</p>
<ol class="hub-passos">
  <li><a href="guia-inici.html">Guia d'inici docent</a> — instal·lació, comptes, checklist de material i pla B.</li>
  <li><a href="{u["met"]}">Metodologia</a> — com és una sessió tipus i com es treballa a l'aula.</li>
  <li><a href="{u["seq"]}">Seqüenciació anual</a> — el calendari de les 9 SA i el pla de contingència.</li>
</ol>

<h2 class="seccio-sep">2 · Setmana a setmana</h2>
<p class="seccio-intro">La rutina de preparar i fer la classe.</p>
<ol class="hub-passos">
  <li>Obre la <a href="classes/index.html">SA que toca</a> i llegeix la <strong>guia docent</strong> de la sessió.</li>
  <li>Té a punt la <strong>fitxa base</strong> (o el seu PDF) i el <strong>codi</strong> de la SA.</li>
  <li>Rutines comunes (graella d'activació, mini-checks, pòsters, defensa oral, IA): <a href="{u["trans"]}">material transversal del curs</a>.</li>
  <li>Per treballar sense maquinari o abans de muntar: <a href="simulacions/index.html">simulacions Wokwi</a>.</li>
</ol>

<h2 class="seccio-sep">3 · Avaluar</h2>
<p class="seccio-intro">Comparteix els criteris <strong>abans</strong> de començar cada SA.</p>
<ol class="hub-passos">
  <li><a href="{u["rub"]}">Rúbriques R1-R5</a> — les mateixes tot el curs; reparteix-les la primera setmana.</li>
  <li><a href="avaluacio/index.html">Proves pràctiques per trimestre</a> — T1, T2 i T3, integrades a l'última sessió de SA3, SA6 i SA9.</li>
  <li><a href="{u["full"]}">Full de qualificació</a> — creua els criteris d'avaluació amb les rúbriques.</li>
</ol>

<h2 class="seccio-sep">Referència completa</h2>
<p class="seccio-intro">Quan necessitis el detall, cada apartat sencer.</p>
<div class="sec-grid">
{sec_cards_html()}
</div>
"""
    return page_shell(out_rel="docent.html", section_key="docent",
                      title="Docent", content_html=content, pages=pages,
                      public="docent")


def render_hub_alumnat(pages: list[Page]) -> str:
    u = hub_urls(pages)
    content = f"""
<section class="hero hub-hero">
  <p class="hero-kicker">Espai alumnat</p>
  <h1 class="hero-titol">El teu espai a Robòtica</h1>
  <p class="hero-lead">Aquí tens el que necessites per orientar-te: com s'avalua (sense sorpreses), on trobar ajuda quan t'encalles i com practicar a casa. Res del que hi ha aquí et penalitza per mirar-ho: els criteris són teus des del primer dia.</p>
</section>

<h2 class="seccio-sep">Com s'avalua (sense sorpreses)</h2>
<ol class="hub-passos">
  <li><a href="{u["alum"]}">Com s'avalua aquesta matèria</a> — d'on surt la nota, què compta i què no.</li>
  <li><a href="{u["rub"]}">Rúbriques completes</a> — tens dret a veure-les <strong>abans</strong> de començar. Mira-les i sabràs què es valora.</li>
  <li>A la fitxa de cada SA, la caixa <strong>«🎯 Objectius i avaluació»</strong> et diu què sabràs fer i què has de lliurar.</li>
</ol>

<h2 class="seccio-sep">El meu quadern tècnic</h2>
<p class="seccio-intro">El teu diari de treball: hi documentes el procés, compta el <strong>25 %</strong> de la nota i <strong>el pots consultar a les proves</strong>.</p>
<ol class="hub-passos">
  <li><a href="{u["quad"]}">Com portar el quadern + plantilla d'entrada</a> — les 5 regles i el bloc per copiar a cada SA.</li>
  <li>Recorda: <strong>escriu-hi cada sessió</strong> (no tot al final) i documenta els errors — <strong>sumen</strong>.</li>
</ol>

<h2 class="seccio-sep">M'he encallat</h2>
<p class="seccio-intro">Encallar-se forma part d'aprendre. Aquí tens ajuda que no et fa la feina.</p>
<ol class="hub-passos">
  <li><a href="{u["targ"]}">Targetes de rescat</a> — pistes en 3 nivells: primer un cop de mà petit, i només si cal, més. Ningú no et dóna la solució feta.</li>
  <li><a href="{u["glos"]}">Glossari català ↔ anglès</a> — els termes tècnics tal com els trobaràs quan busquis per Internet.</li>
</ol>

<h2 class="seccio-sep">Practicar a casa</h2>
<ol class="hub-passos">
  <li><a href="simulacions/index.html">Simulacions Wokwi</a> — munta i prova els circuits sense cap placa, des del navegador.</li>
  <li><a href="reptes/index.html">Reptes</a> — cada SA en té per triar: agafa el context que t'enganxi més.</li>
</ol>

<h2 class="seccio-sep">Fitxes tècniques per tenir a mà</h2>
<p class="seccio-intro">Consulta-les al navegador o imprimeix-les per treballar sobre paper.</p>
{impresos_card_html("alumnat.html")}

<h2 class="seccio-sep">Les 9 situacions d'aprenentatge</h2>
<p class="seccio-intro">Clica una SA per anar al seu material d'aula.</p>
{sa_grid_html(pages)}
"""
    return page_shell(out_rel="alumnat.html", section_key="alumnat",
                      title="Alumnat", content_html=content, pages=pages,
                      public="alumnat")


# ---------------------------------------------------------------------------
# CSS de Pygments (clar + fosc)
# ---------------------------------------------------------------------------
def write_pygments_css():
    ASSETS.joinpath("css").mkdir(parents=True, exist_ok=True)
    light = HtmlFormatter(style="default").get_style_defs(".highlight")
    dark = HtmlFormatter(style="monokai").get_style_defs(
        'html[data-tema="fosc"] .highlight')
    css = ("/* Generat per Pygments — no editar a mà */\n"
           ".highlight { background: transparent; }\n" + light +
           '\nhtml[data-tema="fosc"] .highlight { background: transparent; }\n' + dark)
    (ASSETS / "css" / "pygments.css").write_text(css, encoding="utf-8")


# ---------------------------------------------------------------------------
# Visor de documents (PDF.js per a PDF, visor d'Office per a fulls/diapos)
# ---------------------------------------------------------------------------
def render_visor() -> str:
    tpl = r"""<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Visor de documents · %%TITLE%%</title>
<link rel="stylesheet" href="assets/css/estil.css">
<script>(function(){try{var d=document.documentElement,t=localStorage.getItem('tema');if(t==='fosc'||(!t&&window.matchMedia('(prefers-color-scheme: dark)').matches))d.setAttribute('data-tema','fosc');var m=localStorage.getItem('mida');if(m&&m!=='100')d.setAttribute('data-mida',m);if(localStorage.getItem('font')==='llegible')d.setAttribute('data-font','llegible');}catch(e){}})();</script>
</head>
<body data-section="recursos" class="sense-sidebar sense-toc">
<a class="skip" href="#contingut">Salta al contingut</a>
<header class="topbar">
  <a class="brand" href="index.html"><span class="brand-mark">◆</span> Robòtica <span class="brand-sub">1r Batx</span></a>
  <nav class="topnav" aria-label="Seccions"><a href="index.html">Inici</a></nav>
  <div class="topbar-eines">
    <a class="btn btn-secundari" id="doc-gh" href="#" target="_blank" rel="noopener">Obre a GitHub ↗</a>
    <div class="a11y-grup" role="group" aria-label="Ajustos de lectura">
      <button class="a11y-btn mida-menys" aria-label="Redueix la mida del text" title="Text més petit">A−</button>
      <button class="a11y-btn mida-mes" aria-label="Augmenta la mida del text" title="Text més gran">A+</button>
      <button class="a11y-btn font-toggle" aria-pressed="false" aria-label="Tipografia de lectura fàcil" title="Tipografia de lectura fàcil">Aa</button>
    </div>
    <button class="tema-btn" aria-label="Canvia el tema clar/fosc" title="Tema clar/fosc">◐</button>
  </div>
</header>
<div class="layout">
  <main id="contingut">
    <nav class="breadcrumb" aria-label="Ubicació"><a href="index.html">Inici</a> <span class="sep">/</span> <span>Documents</span> <span class="sep">/</span> <span id="doc-titol" aria-current="page">Document</span></nav>
    <h1 id="doc-h1" class="visor-h1">Document</h1>
    <div id="visor-cont" class="visor-cont"><div class="visor-msg">Carregant…</div></div>
  </main>
</div>
<footer class="peu">
  <p>%%TITLE%% · visor de documents. Els fitxers es carreguen des del <a href="%%REPO%%" target="_blank" rel="noopener">repositori a GitHub</a>.</p>
  <p>Tomeu Riera, amb l'assistència de <a href="https://claude.com/claude-code" target="_blank" rel="noopener">Claude Code</a> · material sota llicència <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.ca" target="_blank" rel="noopener">CC BY-SA 4.0</a>.</p>
</footer>
<script type="module">
const p = new URLSearchParams(location.search);
const u = p.get('u'); const t = p.get('t') || 'Document'; const x = (p.get('x') || '').toLowerCase();
document.getElementById('doc-titol').textContent = t;
document.getElementById('doc-h1').textContent = t;
document.title = t + ' · %%TITLE%%';
let gh = u || '#';
if (u && u.indexOf('raw.githubusercontent.com') > -1) {
  gh = u.replace('https://raw.githubusercontent.com/', 'https://github.com/').replace('/main/', '/blob/main/');
}
document.getElementById('doc-gh').href = gh;
const cont = document.getElementById('visor-cont');
const office = ['xlsx','xls','pptx','ppt','docx','doc','ods','odt','csv'];
function msg(h){ cont.innerHTML = '<div class="visor-msg">' + h + '</div>'; }
if (!u) {
  msg('No s\'ha indicat cap document.');
} else if (x === 'pdf') {
  try {
    // pdf.js allotjat en local (assets/vendor/pdfjs, versio 4.7.76 fixada):
    // el visor funciona sense CDN, en xarxes filtrades i offline.
    const pdfjs = await import('./assets/vendor/pdfjs/pdf.min.mjs');
    pdfjs.GlobalWorkerOptions.workerSrc = 'assets/vendor/pdfjs/pdf.worker.min.mjs';
    const pdf = await pdfjs.getDocument({ url: u }).promise;
    cont.innerHTML = '';
    for (let n = 1; n <= pdf.numPages; n++) {
      const page = await pdf.getPage(n);
      const vp = page.getViewport({ scale: 1.6 });
      const c = document.createElement('canvas');
      c.className = 'visor-pagina'; c.width = vp.width; c.height = vp.height;
      cont.appendChild(c);
      await page.render({ canvasContext: c.getContext('2d'), viewport: vp }).promise;
    }
  } catch (e) {
    msg('No s\'ha pogut mostrar el PDF aquí (potser sense connexió). <a href="' + gh + '" target="_blank" rel="noopener">Obre\'l a GitHub ↗</a>');
  }
} else if (office.includes(x)) {
  // Avis de privadesa: la previsualitzacio Office passa pel visor de Microsoft.
  const src = 'https://view.officeapps.live.com/op/embed.aspx?src=' + encodeURIComponent(u);
  cont.innerHTML = '<p class="visor-msg" style="margin-bottom:.5rem">Aquesta previsualització usa el visor en línia de Microsoft (el document és públic al repositori). Si ho prefereixes, <a href="' + gh + '" target="_blank" rel="noopener">obre\'l directament a GitHub ↗</a>.</p>' +
    '<iframe class="visor-iframe" src="' + src + '" allowfullscreen></iframe>';
} else {
  msg('Aquest tipus de fitxer no es pot previsualitzar al web. <a href="' + gh + '" target="_blank" rel="noopener">Descarrega\'l des de GitHub ↗</a>');
}
</script>
<script src="assets/js/lloc.js"></script>
</body>
</html>
"""
    return (tpl.replace("%%TITLE%%", SITE_TITLE)
            .replace("%%REPO%%", REPO_URL))


# ---------------------------------------------------------------------------
# Procés principal
# ---------------------------------------------------------------------------
def main():
    print("Generant el web de Robòtica…")
    pages, md_map, code_map, code_groups, sim_groups, sim_map = discover()
    copied_imgs: dict = {}
    search_index = []
    pdf_manifest = []   # pàgines d'activitat que es generaran en PDF
    sa_fil = build_sa_fil(pages)       # fil transversal de cada SA
    pager_map = build_sequences(pages)  # paginador ‹ anterior · següent ›
    # nom de fitxer .md -> títol humà (per treure la jerga .md dels enllaços)
    md_title_map = {p.src.name: p.title for p in pages
                    if p.kind in ("doc", "index", "special")}

    # neteja de sortides HTML antigues (manté assets, _generador i els PDF)
    for item in WEB.iterdir():
        if item.name in {"assets", "_generador", ".git", "pdf"}:
            continue
        if item.is_dir():
            shutil.rmtree(item)
        elif item.suffix == ".html" or item.name == ".nojekyll":
            item.unlink()
    # imatges: es regeneren netes (evita duplicats acumulats entre tirades)
    if IMG_OUT.exists():
        shutil.rmtree(IMG_OUT)

    write_pygments_css()
    copia_impresos(search_index)  # fitxes tècniques a web/impresos/ + web/pdf/impresos/

    # Pàgines de documents
    for p in pages:
        if p.kind in ("code", "sim", "practica"):
            continue
        text = strip_github_only(p.src.read_text(encoding="utf-8"))
        md = make_md()
        body = md.convert(text)
        body = wrap_tables(body)
        body = rewrite_links(body, p.src, p.out_rel, md_map, code_map, sim_map,
                             copied_imgs, md_title_map)
        if p.kind == "index" and detect_sa(p.out_rel) is not None \
                and p.section == "classes":
            body = marca_ruta(body)
        if p.src.name == "00_Targetes_rescat.md":
            body = marca_targetes(body)
        toc = toc_html(md)
        extra = ""
        pre = ""
        if p.kind == "index":
            if p.out_rel == f"{p.section}/index.html":
                pre = pauta_html(p.section)   # «Com s'usa aquesta secció»
                extra = section_index_extra(p.section, p.out_rel, pages)
                extra += section_gallery(p.section, p.out_rel, copied_imgs)
                extra += section_documents(p.section, p.out_rel)
            else:
                grp = page_group(p.section, p.out_rel)
                extra = subindex_extra(p.section, grp, p.out_rel, pages)
                # Fitxes tècniques imprimibles: a la portada de SA1 (primer
                # contacte) i SA2 (programació de valent).
                if p.section == "classes" and detect_sa(p.out_rel) in (1, 2):
                    extra += "\n" + impresos_card_html(p.out_rel)
        content = (pre + "\n" if pre else "") + body + ("\n" + extra if extra else "")
        # Fil transversal de la SA + paginador d'itinerari (navegació pautada)
        sa = detect_sa(p.out_rel)
        if sa and 1 <= sa <= 9:
            content += "\n" + sa_fil_html(sa, p.out_rel, sa_fil)
        if p.out_rel in pager_map:
            content += "\n" + pager_map[p.out_rel]
        pdf_href = None
        # Els PDF només es generen per a material d'alumnat: un PDF no pot
        # dur la porta de la vista docent (és JavaScript), i la seva URL és
        # endevinable. El docent imprimeix la pàgina des del navegador.
        if (p.kind in ("doc", "special") and is_activitat(p.src)
                and p.public == "alumnat"):
            pdf_out = pdf_out_for(p.out_rel)
            pdf_href = rel_url(p.out_rel, pdf_out)
            pdf_manifest.append({"html": p.out_rel, "pdf": pdf_out, "title": p.title})
        full = page_shell(out_rel=p.out_rel, section_key=p.section,
                          title=p.title, content_html=content, toc=toc,
                          tri=p.trimester, pages=pages, pdf_href=pdf_href,
                          public=p.public)
        dest = WEB / p.out_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(full, encoding="utf-8")
        # El cos de text només s'indexa per a les pàgines d'alumnat:
        # cerca-index.js és un fitxer públic i, si hi guardéssim el text de
        # les pàgines docents, el material del professorat seria llegible
        # sense passar per la porta. Les docents s'hi cerquen pel títol.
        search_index.append({"t": p.title, "s": SECTION_BY_KEY.get(p.section, {}).get("title", "Inici"),
                             "u": p.out_rel, "tri": p.trimester, "p": p.public,
                             "b": text_pla_cerca(content) if p.public == "alumnat" else ""})

    # Pàgines de codi
    n_practiques = 0
    for g in code_groups:
        extra_nav = ""
        sa = detect_sa(g["out_rel"])
        if sa and 1 <= sa <= 9:
            extra_nav += sa_fil_html(sa, g["out_rel"], sa_fil)
        extra_nav += pager_map.get(g["out_rel"], "")
        full = render_code_page(g, pages, extra_nav)
        dest = WEB / g["out_rel"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(full, encoding="utf-8")
        search_index.append({"t": g["label"], "s": SECTION_BY_KEY[g["section"]]["title"],
                             "u": g["out_rel"], "tri": g["tri"], "p": g.get("public", "alumnat")})
        # Pàgines de pràctica (una per sketch amb EXPLICACIO.md)
        practs = [it for it in g["items"] if "page_out" in it]
        for i, it in enumerate(practs):
            nav = ""
            if sa and 1 <= sa <= 9:
                nav += sa_fil_html(sa, it["page_out"], sa_fil)
            nav += pager_practiques(g, practs, i)
            full, cos = render_practica_page(it, g, pages, md_map, code_map,
                                             sim_map, copied_imgs, md_title_map, nav)
            dest = WEB / it["page_out"]
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(full, encoding="utf-8")
            search_index.append({"t": it["title"],
                                 "s": SECTION_BY_KEY[g["section"]]["title"],
                                 "u": it["page_out"], "tri": g["tri"],
                                 "p": "alumnat", "b": text_pla_cerca(cos)})
            n_practiques += 1

    # Pàgines de simulacions Wokwi
    for g in sim_groups:
        full = render_sim_page(g, pages)
        dest = WEB / g["out_rel"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(full, encoding="utf-8")
        search_index.append({"t": g["title"], "s": "Simulacions",
                             "u": g["out_rel"], "tri": g["tri"], "p": "alumnat"})

    # Visor de documents (PDF.js + visor d'Office), sense copiar fitxers
    (WEB / "visor.html").write_text(render_visor(), encoding="utf-8")

    # Home i hubs per audiència (docent i alumnat)
    (WEB / "index.html").write_text(render_home(pages), encoding="utf-8")
    (WEB / "docent.html").write_text(render_hub_docent(pages), encoding="utf-8")
    (WEB / "alumnat.html").write_text(render_hub_alumnat(pages), encoding="utf-8")
    search_index.insert(0, {"t": "Inici", "s": "Inici", "u": "index.html",
                            "tri": None, "p": "alumnat"})
    search_index.insert(1, {"t": "Docent — espai del professorat", "s": "Docent",
                            "u": "docent.html", "tri": None, "p": "docent"})
    search_index.insert(2, {"t": "Alumnat — el teu espai", "s": "Alumnat",
                            "u": "alumnat.html", "tri": None, "p": "alumnat"})

    # Índex de cerca (com a JS per funcionar també en local file://)
    ASSETS.joinpath("js").mkdir(parents=True, exist_ok=True)
    (ASSETS / "js" / "cerca-index.js").write_text(
        "window.INDEX_CERCA = " + json.dumps(search_index, ensure_ascii=False) + ";",
        encoding="utf-8")

    # .nojekyll perquè GitHub Pages no processi amb Jekyll
    (WEB / ".nojekyll").write_text("", encoding="utf-8")

    # Redireccions de les URLs antigues dels dossiers de projecte (Classroom)
    write_redirects_projectes(WEB)

    # Manifest d'activitats per a la generació de PDF (vegeu generar_pdf.py)
    (SCRIPT_DIR / "_activitats.json").write_text(
        json.dumps(pdf_manifest, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"  · {len([p for p in pages if p.kind not in ('code', 'sim', 'practica')])} pàgines de document")
    print(f"  · {len(code_groups)} pàgines de codi")
    print(f"  · {n_practiques} pàgines de pràctica")
    print(f"  · {len(sim_groups)} pàgines de simulació")
    print(f"  · {len(copied_imgs)} imatges copiades")
    print(f"  · {len(search_index)} entrades a l'índex de cerca")
    print(f"  · {len(pdf_manifest)} pàgines d'activitat per a PDF (executa generar_pdf.py)")
    print("Fet. Obre web/index.html o publica la carpeta web/ a GitHub Pages.")


if __name__ == "__main__":
    main()
