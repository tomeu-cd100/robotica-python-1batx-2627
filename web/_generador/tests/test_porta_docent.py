"""Tests de la porta de la vista docent sobre el web GENERAT.

La porta (web/assets/js/lloc.js) és fricció, no seguretat, però ha de cobrir
tot el material docent: cap PDF sense porta, res als cercadors i cap text
docent dins de l'índex de cerca públic.

Executa'ls des de web/_generador/:  py -3.11 -m pytest tests/ -q
(Cal haver generat el web abans: py -3.11 web/_generador/generar.py)
"""
import json
import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import generar  # noqa: E402
from generar import ROOT  # noqa: E402

WEB = ROOT / "web"
# Adaptació al curs nou: a l'esquelet inicial, Classes/SAn/ només té un
# README.md placeholder (que ja genera una pàgina), sense guia docent real.
# El skip original només mirava si web/classes/ existia; calia un criteri
# sobre CONTINGUT real (guia docent d'alguna SA) perquè aquests tests (que
# esperen >50 pàgines docent) no s'executin sobre l'esquelet buit.
sense_web = pytest.mark.skipif(
    not any((ROOT / "Classes").glob("SA*/SA*_guia_docent.md")),
    reason="cap guia docent de SA: contingut encara no creat (esquelet inicial)")


def _pagines_docent():
    return [f for f in WEB.rglob("*.html")
            if 'data-public="docent"' in f.read_text(encoding="utf-8", errors="ignore")]


@sense_web
def test_cap_pdf_de_material_docent():
    """Un PDF no pot dur la porta (és JavaScript) i la seva URL és
    endevinable: cap pàgina docent no ha de tenir PDF generat."""
    pages, *_ = generar.discover()
    docents = [p for p in pages if p.public == "docent"]
    assert docents, "cap pàgina docent: el web no s'ha generat bé"
    for p in docents:
        pdf = WEB / generar.pdf_out_for(p.out_rel)
        assert not pdf.exists(), f"PDF de material docent publicat: {pdf}"


@sense_web
def test_pagines_docent_amb_noindex():
    docents = _pagines_docent()
    assert len(docents) > 50, f"només {len(docents)} pàgines docent trobades"
    for f in docents:
        t = f.read_text(encoding="utf-8", errors="ignore")
        assert 'name="robots" content="noindex, nofollow"' in t, \
            f"pàgina docent indexable: {f.relative_to(WEB)}"


@sense_web
def test_index_de_cerca_sense_text_docent():
    """cerca-index.js és públic: les entrades docent hi són pel títol
    (el cercador les filtra en vista alumnat) però sense cos de text."""
    t = (WEB / "assets" / "js" / "cerca-index.js").read_text(encoding="utf-8")
    dades = json.loads(re.search(r"=\s*(\[.*\])\s*;?\s*$", t, re.S).group(1))
    docents = [e for e in dades if e.get("p") == "docent"]
    assert docents, "cap entrada docent a l'índex de cerca"
    amb_cos = [e["u"] for e in docents if e.get("b")]
    assert not amb_cos, f"text de material docent a l'índex públic: {amb_cos[:5]}"


@sense_web
def test_pagines_alumnat_indexables():
    """La restricció és només per al material docent: la resta del web
    ha de continuar sent visible als cercadors."""
    inici = (WEB / "index.html").read_text(encoding="utf-8")
    assert 'name="robots"' not in inici
