# -*- coding: utf-8 -*-
"""Tests de generador/pdfutil.py (validesa forta i marca de sincronia)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from generador.pdfutil import (escriu_marca, hash_font, llegeix_marca,  # noqa: E402
                               num_pagines, pdf_valid)

# PDF mínim sintètic: capçalera + un node /Pages amb dues /Page.
PDF_2P = (b"%PDF-1.4\n"
          b"1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n"
          b"2 0 obj << /Type /Pages /Kids [3 0 R 4 0 R] /Count 2 >> endobj\n"
          b"3 0 obj << /Type /Page /Parent 2 0 R >> endobj\n"
          b"4 0 obj << /Type /Page /Parent 2 0 R >> endobj\n"
          + b"%" + b"x" * 1200 + b"\n"  # farciment per superar 1 KB
          b"%%EOF\n")


def _escriu(tmp_path, nom, data):
    p = tmp_path / nom
    p.write_bytes(data)
    return p


def test_num_pagines_compta_nomes_page(tmp_path):
    p = _escriu(tmp_path, "dos.pdf", PDF_2P)
    assert num_pagines(p) == 2  # /Type /Pages no compta


def test_num_pagines_no_pdf(tmp_path):
    p = _escriu(tmp_path, "fals.pdf", b"hola mon, no soc cap pdf" * 100)
    assert num_pagines(p) == 0


def test_pdf_valid(tmp_path):
    assert pdf_valid(_escriu(tmp_path, "ok.pdf", PDF_2P))


def test_pdf_valid_rebutja_truncat(tmp_path):
    # Capçalera correcta i mida gran, però cap pàgina: el cas que el
    # check antic (capçalera + mida) deixava passar.
    truncat = b"%PDF-1.4\n" + b"%" + b"x" * 2000
    assert not pdf_valid(_escriu(tmp_path, "truncat.pdf", truncat))


def test_pdf_valid_rebutja_petit(tmp_path):
    petit = b"%PDF-1.4\n1 0 obj << /Type /Page >> endobj\n%%EOF"
    assert not pdf_valid(_escriu(tmp_path, "petit.pdf", petit))


def test_hash_font_normalitza_crlf():
    assert hash_font("a\r\nb") == hash_font("a\nb")
    assert hash_font("a\nb") != hash_font("a\nc")


def test_marca_roundtrip(tmp_path):
    p = _escriu(tmp_path, "marcat.pdf", PDF_2P)
    assert llegeix_marca(p) is None
    h = hash_font("# font de prova\n")
    escriu_marca(p, h)
    assert llegeix_marca(p) == h
    assert pdf_valid(p)  # la marca no invalida el PDF


def test_marca_es_queda_amb_la_darrera(tmp_path):
    p = _escriu(tmp_path, "remarcat.pdf", PDF_2P)
    escriu_marca(p, hash_font("versio vella"))
    h2 = hash_font("versio nova")
    escriu_marca(p, h2)
    assert llegeix_marca(p) == h2
