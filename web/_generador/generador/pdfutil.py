# -*- coding: utf-8 -*-
"""
Utilitats compartides de validació i sincronia dels PDF generats.

- Validesa "forta": a més de la capçalera %PDF- i la mida, es compten les
  pàgines reals (objectes /Type /Page). Un tall de Chrome per
  --virtual-time-budget curt pot deixar un PDF amb capçalera vàlida però
  buit o truncat: el recompte el detecta.
- Marca de sincronia font↔PDF: després del %%EOF (els visors ignoren els
  bytes posteriors) s'hi afegeix una línia `%font-md-sha1:<hash>` amb el
  hash de la font (.md o .py de dades). tools/qa.py compara el hash de la
  font actual amb la marca del PDF versionat i avisa si algú ha editat la
  font sense regenerar el PDF.
- El hash es calcula sobre el text NORMALITZAT a LF: el mateix fitxer dona
  el mateix hash al checkout Windows (CRLF) i al del CI (LF).
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

# /Type /Page però no /Type /Pages (el node contenidor)
_RE_PAGE = re.compile(rb"/Type\s*/Page(?![a-zA-Z])")
_RE_MARCA = re.compile(rb"%font-md-sha1:([0-9a-f]{40})")
_PREFIX_MARCA = b"\n%font-md-sha1:"


def num_pagines(pdf_path: Path) -> int:
    """Nombre de pàgines del PDF (0 si no és un PDF o està truncat)."""
    data = Path(pdf_path).read_bytes()
    if not data.startswith(b"%PDF-"):
        return 0
    return len(_RE_PAGE.findall(data))


def pdf_valid(pdf_path: Path, min_bytes: int = 1024) -> bool:
    """Validesa forta: existeix, mida mínima i almenys una pàgina real."""
    p = Path(pdf_path)
    return p.exists() and p.stat().st_size >= min_bytes and num_pagines(p) >= 1


def hash_font(text: str) -> str:
    """SHA-1 del text de la font, normalitzat a LF (Windows i CI coincideixen)."""
    return hashlib.sha1(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def escriu_marca(pdf_path: Path, sha1hex: str) -> None:
    """Afegeix la marca de sincronia després del %%EOF del PDF."""
    with open(pdf_path, "ab") as f:
        f.write(_PREFIX_MARCA + sha1hex.encode("ascii") + b"\n")


def llegeix_marca(pdf_path: Path) -> str | None:
    """Retorna el hash de la marca de sincronia del PDF, o None si no en té."""
    data = Path(pdf_path).read_bytes()
    m = None
    for m in _RE_MARCA.finditer(data[-4096:]):
        pass  # ens quedem l'última (si s'ha regenerat més d'un cop)
    return m.group(1).decode("ascii") if m else None
