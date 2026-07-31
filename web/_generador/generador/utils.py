"""Utilitats pures del generador (sense estat de build ni E/S).

Tot el que hi ha aquí és funció pura sobre strings/rutes: es pot testejar
amb pytest sense construir res (vegeu `tests/test_utils.py`).
"""
from __future__ import annotations

import html
import re
import unicodedata

BODY_CERCA_MAX = 1500  # caràcters de cos per pàgina a l'índex de cerca


def strip_accents(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", text)
                   if not unicodedata.combining(c))


def slugify(text: str) -> str:
    text = strip_accents(text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "x"


def text_pla_cerca(html_body: str) -> str:
    """Text pla del cos d'una pàgina per a l'índex de cerca.

    Treu blocs de codi (no volem que 'href' o variables d'exemple apareguin
    com a text), després la resta d'etiquetes, i compacta espais. Es retalla
    a BODY_CERCA_MAX per contenir la mida de cerca-index.js.
    """
    text = re.sub(r"(?s)<pre.*?</pre>", " ", html_body)
    text = re.sub(r"(?s)<(script|style).*?</\1>", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:BODY_CERCA_MAX]


def detect_sa(name: str) -> int | None:
    m = re.search(r"sa\s*([0-9])", name, re.IGNORECASE)
    return int(m.group(1)) if m else None


def first_h1(md_text: str) -> str | None:
    for line in md_text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return re.sub(r"\s+", " ", s[2:].strip())
    return None


def rel_url(from_out: str, to_out: str) -> str:
    """Ruta relativa (POSIX) entre dues sortides relatives a l'arrel del web."""
    from pathlib import PurePosixPath
    import os
    base = PurePosixPath(from_out).parent
    rel = os.path.relpath(to_out, str(base))
    return rel.replace("\\", "/")


def pdf_out_for(out_rel: str) -> str:
    """Ruta de sortida del PDF (relativa a web/) per a una pàgina HTML."""
    return "pdf/" + out_rel[:-5] + ".pdf"  # treu .html


# Blocs on la reescriptura d'enllaços NO ha d'entrar mai: el codi d'exemple
# (un href="..." literal dins d'un sketch o d'un fragment HTML és contingut
# que l'alumnat ha de veure tal qual). Vegeu apply_outside_code.
_RE_CODI = re.compile(r"(?s)(<pre.*?</pre>|<code.*?</code>)")


def apply_outside_code(html_body: str, transform) -> str:
    """Aplica `transform` (str -> str) només FORA de blocs <pre>/<code>.

    Resol el punt fràgil P5 de l'auditoria tècnica (2026-07-08): la
    reescriptura d'enllaços per regex podia tocar text literal dins de blocs
    de codi. Els segments de codi passen intactes.
    """
    parts = _RE_CODI.split(html_body)
    return "".join(p if _RE_CODI.fullmatch(p) else transform(p) for p in parts)
