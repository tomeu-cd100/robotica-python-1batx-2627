"""Tests de la lògica pura del generador (paquet generador/).

Executa'ls des de web/_generador/:  py -m pytest tests/ -q
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from generador.utils import (  # noqa: E402
    BODY_CERCA_MAX, apply_outside_code, detect_sa, first_h1, pdf_out_for,
    rel_url, slugify, strip_accents, text_pla_cerca,
)


# --- slugify / strip_accents -------------------------------------------------
def test_slugify_accents_i_simbols():
    assert slugify("Màquines d'estats (SA6)") == "maquines-d-estats-sa6"
    assert slugify("Català ↔ Anglès") == "catala-angles"
    assert slugify("···") == "x"  # mai buit


def test_strip_accents():
    assert strip_accents("històrica àèïöü") == "historica aeiou"


# --- detect_sa ----------------------------------------------------------------
def test_detect_sa():
    assert detect_sa("SA6_fitxa_alumnat.md") == 6
    assert detect_sa("classes/sa3/index.html") == 3
    assert detect_sa("GUIA_INICI_DOCENT.md") is None


# --- first_h1 -------------------------------------------------------------
def test_first_h1():
    assert first_h1("hola\n# Títol  doble  espai\n## H2") == "Títol doble espai"
    assert first_h1("sense titol") is None


# --- rel_url / pdf_out_for --------------------------------------------------
def test_rel_url():
    assert rel_url("classes/sa1/index.html", "index.html") == "../../index.html"
    assert rel_url("index.html", "classes/sa1/index.html") == "classes/sa1/index.html"
    assert rel_url("classes/sa1/a.html", "classes/sa1/b.html") == "b.html"


def test_pdf_out_for():
    assert pdf_out_for("classes/sa1/fitxa.html") == "pdf/classes/sa1/fitxa.pdf"


# --- text_pla_cerca -----------------------------------------------------------
def test_text_pla_cerca_treu_codi_i_etiquetes():
    cos = '<p>La <strong>histèresi</strong> evita el clic-clic.</p><pre><code>if (temp &lt; 24) {}</code></pre>'
    t = text_pla_cerca(cos)
    assert "histèresi" in t
    assert "temp" not in t  # el codi no s'indexa
    assert "<" not in t


def test_text_pla_cerca_retalla():
    assert len(text_pla_cerca("<p>" + "x" * 99999 + "</p>")) == BODY_CERCA_MAX


# --- apply_outside_code (criteri d'acceptació P5 de l'auditoria 08-07) --------
def test_apply_outside_code_no_toca_pre():
    body = ('<p><a href="fitxa.md">fitxa</a></p>'
            '<pre><code>&lt;a href="literal.md"&gt;exemple&lt;/a&gt;\n'
            'String u = "href=\\"x\\"";</code></pre>'
            '<p><img src="foto.jpg"></p>')
    vist = []

    def marca(seg):
        vist.append(seg)
        return seg.replace('href="fitxa.md"', 'href="fitxa.html"') \
                  .replace('src="foto.jpg"', 'src="assets/img/foto.jpg"')

    out = apply_outside_code(body, marca)
    # (a) l'enllaç relatiu de fora es reescriu
    assert 'href="fitxa.html"' in out
    # (c) la imatge de fora es reescriu
    assert 'src="assets/img/foto.jpg"' in out
    # (b) el bloc de codi queda INTACTE, literal per literal
    assert 'href="literal.md"' in out
    assert 'String u = "href=\\"x\\"";' in out
    # i el transform no ha vist mai el segment <pre>
    assert all("<pre" not in s for s in vist)


def test_apply_outside_code_code_inline():
    body = '<p>escriu <code>href="pin"</code> i <a href="a.md">a</a></p>'
    out = apply_outside_code(body, lambda s: s.replace('href="a.md"', 'href="a.html"'))
    assert '<code>href="pin"</code>' in out
    assert 'href="a.html"' in out
