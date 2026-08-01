# -*- coding: utf-8 -*-
"""Detecció del navegador per imprimir PDF (Chrome/Edge headless).

Font única per a generar_pdf.py, generar_fulls_imprimibles.py i
generar_quadern_tecnic.py (abans cada script en duia una còpia).
Ordre: variable d'entorn CHROME_BIN → rutes conegudes de Windows →
executables al PATH (Linux/macOS, runners de CI).
"""
from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

CHROME_CANDIDATES = [
    r"C:/Program Files/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    r"C:/Program Files/Microsoft/Edge/Application/msedge.exe",
]
PATH_NAMES = ["google-chrome", "google-chrome-stable", "chromium",
              "chromium-browser", "chrome", "msedge"]


def find_browser() -> str:
    env = os.environ.get("CHROME_BIN")
    if env and Path(env).exists():
        return env
    for c in CHROME_CANDIDATES:
        if Path(c).exists():
            return c
    for name in PATH_NAMES:
        found = shutil.which(name)
        if found:
            return found
    sys.exit("No s'ha trobat Chrome ni Edge. Instal·la'n un o posa la ruta a "
             "CHROME_BIN.")
