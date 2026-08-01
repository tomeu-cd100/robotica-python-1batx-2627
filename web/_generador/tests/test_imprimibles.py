# -*- coding: utf-8 -*-
"""Tests del post-procés de paper de generar_fulls_imprimibles.py
(motor unificat: python-markdown + transformacions per a impressió)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from generar_fulls_imprimibles import (aplana_enllacos, camps_per_omplir,  # noqa: E402
                                       fora_callouts_de_pdf, inline_md,
                                       md_to_body, protegeix_camps)


def test_caselles_reals():
    _, h = md_to_body("# T\n\n- [ ] Primera cosa\n- [x] Segona **cosa**\n")
    assert h.count('class="box"') == 2
    assert '<ul class="check">' in h
    assert "[ ]" not in h and "[x]" not in h
    assert "<strong>cosa</strong>" in h


def test_llista_normal_no_es_toca():
    _, h = md_to_body("# T\n\n- una\n- dues\n")
    assert 'class="box"' not in h and "<li>una</li>" in h


def test_camps_sobreviuen_al_motor():
    # Sense protecció, el motor partiria els ___ com a èmfasi.
    _, h = md_to_body("# T\n\n**Nom:** ______  **Data:** __________\n")
    assert h.count("fill-inline") == 2
    assert "_" not in h.replace("fill-inline", "")
    assert "<strong>Nom:</strong>" in h


def test_taula_semafor_es_buida_per_pintar():
    md = ("# T\n\n| Què | 🔴 | 🟡 | 🟢 |\n|---|---|---|---|\n"
          "| Sé fer X | text | text | text |\n")
    _, h = md_to_body(md)
    assert h.count('<td class="paint"></td>') == 3
    assert '<td class="lab">' in h and "Sé fer X" in h
    assert '<table class="grid">' in h


def test_taula_normal_conserva_cel_les():
    md = "# T\n\n| A | B |\n|---|---|\n| u | dos |\n"
    _, h = md_to_body(md)
    assert "paint" not in h and "dos" in h and 'class="grid"' in h


def test_fora_nomes_el_paragraf_del_pdf():
    # python-markdown fusiona blockquotes adjacents: el veí ha de sobreviure.
    md = ("# T\n\n> 📄 [Versió PDF](pdf/full.pdf)\n\n"
          "> Aquest text important es queda.\n")
    _, h = md_to_body(md)
    assert "full.pdf" not in h and "Versió PDF" not in h
    assert "es queda" in h


def test_blockquote_buit_desapareix():
    h = fora_callouts_de_pdf("<blockquote><p><a href='pdf/x.pdf'>PDF</a></p></blockquote>")
    assert h == ""


def test_enllacos_aplanats():
    assert aplana_enllacos('abans <a href="x.html">text</a> després') == "abans text després"


def test_inline_md():
    h = inline_md("**Fort** i [enllaç](x.md) i ______")
    assert "<strong>Fort</strong>" in h and "enllaç" in h
    assert "href" not in h and "fill-inline" in h and not h.startswith("<p>")


def test_titol_sense_marques():
    t, _ = md_to_body("# SA1 · El meu *checklist*\n\ncos\n")
    assert t == "SA1 · El meu checklist"


def test_proteccio_roundtrip():
    assert camps_per_omplir(protegeix_camps("ab ___ cd")) == \
        'ab <span class="fill-inline"></span> cd'
