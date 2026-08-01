#!/usr/bin/env python3
"""QA automàtic del material i del web generat.

Maquinari del curs: micro:bit V2 + Micro:shield + sensors Keyestudio. Tot el
codi d'alumnat és MicroPython (`.py`); no hi ha cap `.ino` ni compilació
Arduino en aquest repositori (a diferència del curs germà d'Arduino+C/C++).

Comprova (i falla amb exit != 0 si troba res):
  1. Enllaços i imatges locals del web generat (web/**/*.html) que apunten
     a fitxers inexistents. [omès amb --nomes-sintaxi: amb el repositori
     quasi buit, les seccions sense contingut trenquen enllaços interns
     esperats sense que sigui un error real]
  2. Cobertura de cada SA: que hi hagi guia docent, fitxa base, fitxa
     ampliada, checklists, README, esquemes/connexions (SA1-SA8) i el
     repte + solucionari corresponent (SA1-SA8). SA0 és material d'acollida
     sense sessions pròpies: contracte reduït, exigeix README + els 3
     fitxers de contingut (vocabulari, primers passos, guia de programació).
     [omès amb --nomes-sintaxi]
  3. Coherència horària: la taula de `08_Sequenciacio_temporal_anual.md`
     ha de sumar les hores del subtotal declarat (quadre nou: SA1=6, SA2=8,
     SA3=8, SA4=8, SA5=6, SA6=8, SA7=8, SA8=6, SA9=10 → 68 h + marge).
     [omès amb --nomes-sintaxi]
  4. Sintaxi de tots els `.py` d'alumnat amb `ast.parse` (només es parsegen,
     mai s'executen: els `import microbit`/`import radio` no calen stub).
  5. Quadern tècnic: les sessions de `web/_generador/quadern_sessions.py`
     quadren amb el quadre d'hores (doc 08) i amb els títols de sessió de
     les guies docents; avisa si falten els PDF generats. [omès amb
     --nomes-sintaxi]
  6. Ordre de l'itinerari: cap pàgina de SA sense clau a DOC_ORDRE_CLAUS.
  7. PII: cap adreça de correu als fitxers versionats .md/.js/.py/.html
     (allowlist per als correus de coautoria; el del docent només avisa).
  8. PDF committats: capçalera %PDF-, mida > 1 KB, ≥ 1 pàgina real i marca
     de sincronia amb la font (.md editat sense regenerar el PDF = error).
  9. Mojibake: cap seqüència «Ã», «â€», «Â·» als .md versionats.
 10. Sintaxi dels `.py` del solucionari (Reptes/**), amb `ast.parse` com
     el punt 4.
 11. Enllaços externs (OPT-IN amb QA_ENLLACOS_EXTERNS=1: depèn de la xarxa;
     mai no bloqueja el CI — els caiguts surten com a avís).
 12. Bloc «Què has d'entregar» de cada SA. [omès amb --nomes-sintaxi]
 13. Pàgines de pràctica: cada sketch d'alumnat té la seva EXPLICACIO.md
     (pàgina de pràctica a la web) i no queda cap sketch *_BASTIDA solt.
     [omès amb --nomes-sintaxi]
 14. Projectes trimestrals: cada projecte de generar.PROJECTES té la seva
     portada a Classes/00_General i la portada enllaça el seu dossier.
     [omès amb --nomes-sintaxi]
 15. Codi incrustat als solucionaris: cada desplegable «Desplega el codi
     complet (<code>fitxer</code>…)» ha de ser una còpia exacta del fitxer
     de Classes/Solucionari/codi/ (si el sketch canvia, cal actualitzar
     el bloc del .md). [omès amb --nomes-sintaxi]

Abans de res (punt 0) comprova que els paquets del generador (markdown,
pygments) estan instal·lats: sense ells els punts 6 i 8 petarien a mig camí.

Ús:  py tools/qa.py                (cal haver generat el web abans per al
                                    punt 1; si web/ no té HTML, s'omet amb avís)
     py tools/qa.py --nomes-sintaxi (salta els checks de contingut/cobertura
                                    de SA: per committar infraestructura
                                    abans que existeixi el material de curs)
"""
from __future__ import annotations

import argparse
import ast
import html.parser
import importlib.util
import os
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

# Consola Windows amb cp1252: força UTF-8 per no petar amb accents/fletxes.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ARREL = Path(__file__).resolve().parent.parent
WEB = ARREL / "web"
errors: list[str] = []
avisos: list[str] = []
NOMES_SINTAXI = False  # es fixa a main() segons --nomes-sintaxi


# --- 1 · Enllaços locals del web generat -----------------------------------
class Enllacos(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[str] = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for at in ("href", "src"):
            v = d.get(at)
            if v:
                self.refs.append(v)


def comprova_enllacos_web() -> None:
    if NOMES_SINTAXI:
        print("1) Enllaços del web: omès (--nomes-sintaxi; repositori quasi buit "
              "-> les seccions sense contingut trenquen enllaços interns esperats).")
        return
    pagines = sorted(WEB.rglob("*.html"))
    if not pagines:
        avisos.append("web/ sense HTML: link-check omès (genera el web abans).")
        return
    trencats = 0
    for pag in pagines:
        p = Enllacos()
        p.feed(pag.read_text(encoding="utf-8", errors="replace"))
        for ref in p.refs:
            if ref.startswith(("http:", "https:", "mailto:", "data:", "#", "javascript:")):
                continue
            ruta = urllib.parse.unquote(ref.split("#", 1)[0].split("?", 1)[0])
            if not ruta:
                continue
            desti = (WEB / ruta) if ruta.startswith("/") else (pag.parent / ruta)
            try:
                desti = desti.resolve()
            except OSError:
                pass
            if not desti.exists():
                # Els PDF es generen amb generar_pdf.py: a CI corre sempre
                # abans del QA (error si falta); en local web/pdf/ pot estar
                # desactualitzat i només avisa.
                if "pdf/" in ref and not os.environ.get("CI"):
                    avisos.append(f"[pdf local desactualitzat] {pag.relative_to(WEB)} → {ref}")
                    continue
                errors.append(f"[enllaç] {pag.relative_to(WEB)} → {ref}")
                trencats += 1
    print(f"1) Enllaços del web: {len(pagines)} pàgines, {trencats} referències trencades.")


# --- 2 · Cobertura de cada SA ------------------------------------------------
def comprova_cobertura_sa() -> None:
    if NOMES_SINTAXI:
        print("2) Cobertura SA0-SA9: omesa (--nomes-sintaxi).")
        return
    fallats = 0
    # SA0 és material d'acollida sense sessions pròpies (es fa dins la S1 de
    # SA1): contracte reduït (no guia docent/fitxes/checklists/reptes), però
    # exigeix el README i els 3 fitxers de contingut (vocabulari, primers
    # passos, guia de programació -- aquest darrer és el circuit de reforç
    # 🔴 dels mini-checks, vegeu 00_Mini_checks_individuals.md).
    sa0_base = ARREL / "Classes" / "SA0"
    sa0_esperats = [
        sa0_base / "README.md",
        sa0_base / "SA0_vocabulari_robotica.md",
        sa0_base / "SA0_primers_passos_editor.md",
        sa0_base / "SA0_guia_programacio.md",
    ]
    for f in sa0_esperats:
        if not f.exists():
            errors.append(f"[cobertura] SA0: falta {f.relative_to(ARREL)}")
            fallats += 1
    for n in range(1, 10):
        sa = f"SA{n}"
        base = ARREL / "Classes" / sa
        esperats = [
            base / "README.md",
            base / f"{sa}_guia_docent.md",
            base / f"{sa}_fitxa_alumnat.md",
            base / f"{sa}_fitxa_ampliada.md",
            base / f"{sa}_checklist_docent.md",
            base / f"{sa}_checklist_alumnat.md",
            base / f"{sa}_questionari_conceptes.md",  # retrieval (pas «Consolida»)
            base / f"{sa}_exemple_resolt.md",          # model «jo ho faig»
        ]
        if n <= 8:
            esq = base / f"{sa}_esquemes_connexions.md"
            con = base / f"{sa}_connexions.md"
            if not esq.exists() and not con.exists():
                errors.append(f"[cobertura] {sa}: falta esquemes/connexions")
                fallats += 1
            esperats.append(ARREL / "Reptes" / f"Reptes_{sa}.md")
            sol = ARREL / "Reptes" / "Solucionari" / sa
            if not sol.is_dir():
                errors.append(f"[cobertura] {sa}: falta Reptes/Solucionari/{sa}/")
                fallats += 1
        for f in esperats:
            if not f.exists():
                errors.append(f"[cobertura] {sa}: falta {f.relative_to(ARREL)}")
                fallats += 1
    print(f"2) Cobertura SA0-SA9: {fallats} mancances.")


# --- 3 · Coherència horària --------------------------------------------------
def comprova_hores() -> None:
    if NOMES_SINTAXI:
        print("3) Hores: omès (--nomes-sintaxi).")
        return
    doc = (ARREL / "Programació didàctica" / "08_Sequenciacio_temporal_anual.md")
    if not doc.exists():
        avisos.append(f"[hores] falta {doc.relative_to(ARREL)}: check omès "
                      f"(usa --nomes-sintaxi mentre no existeixi el document 08).")
        return
    text = doc.read_text(encoding="utf-8")
    hores = [int(m.group(2)) for m in re.finditer(r"\|\s*SA(\d)\s*[*†]?\s*\|[^|]+\|\s*(\d+)\s*\|", text)]
    m = re.search(r"Subtotal SA\*\*\s*\|\s*\*\*(\d+)\s*h", text)
    if len(hores) != 9 or not m:
        errors.append(f"[hores] no s'ha pogut llegir la taula del doc 08 (files SA: {len(hores)})")
    else:
        suma, declarat = sum(hores), int(m.group(1))
        if suma != declarat:
            errors.append(f"[hores] la taula suma {suma} h però declara {declarat} h")
        print(f"3) Hores: {hores} → suma {suma} h (declarat {declarat} h).")


def comprova_sintaxi_py(f: Path) -> str | None:
    """Sintaxi d'un .py MicroPython amb ast.parse: només es parseja, mai
    s'executa, així que `import microbit`/`import radio` no calen stub."""
    try:
        ast.parse(f.read_text(encoding="utf-8", errors="replace"), filename=str(f))
    except SyntaxError as e:
        return f"línia {e.lineno}: {e.msg}"
    return None


# --- 4 · Sintaxi dels .py d'alumnat ------------------------------------------
def comprova_python() -> None:
    fitxers = sorted((ARREL / "Classes").rglob("codi/**/*.py")) + \
              sorted((ARREL / "Classes").rglob("codi/*.py"))
    fallats = 0
    for f in sorted(set(fitxers)):
        error = comprova_sintaxi_py(f)
        if error:
            errors.append(f"[python] {f.relative_to(ARREL)}: {error}")
            fallats += 1
    print(f"4) Python d'alumnat: {len(set(fitxers))} fitxers, {fallats} amb errors de sintaxi.")


# --- 5 · Quadern tècnic: sincronitzat amb guies i quadre d'hores -------------
def comprova_quadern() -> None:
    if NOMES_SINTAXI:
        print("5) Quadern tècnic: omès (--nomes-sintaxi).")
        return
    sys.path.insert(0, str(ARREL / "web" / "_generador"))
    import quadern_sessions as q

    doc = (ARREL / "Programació didàctica" / "08_Sequenciacio_temporal_anual.md")
    if not doc.exists():
        avisos.append(f"[quadern] falta {doc.relative_to(ARREL)}: check omès.")
        return
    text = doc.read_text(encoding="utf-8")
    hores = {f"SA{m.group(1)}": int(m.group(2)) for m in
             re.finditer(r"\|\s*SA(\d)\s*[*†]?\s*\|[^|]+\|\s*(\d+)\s*\|", text)}
    fallats = 0
    for t, sessions in q.SESSIONS.items():
        per_sa: dict[str, int] = {}
        for s in sessions:
            per_sa[s["sa"]] = per_sa.get(s["sa"], 0) + 1
        for sa, n in per_sa.items():
            if hores.get(sa) != n * 2:
                errors.append(f"[quadern] {sa}: {n} sessions ({n*2} h) però el "
                              f"doc 08 en declara {hores.get(sa)} h")
                fallats += 1
        if [s for s in sessions if s.get("prova")] != sessions[-1:]:
            errors.append(f"[quadern] T{t}: la sessió de prova ha de ser exactament l'última")
            fallats += 1
        # Títols coherents amb les guies docents (SA9 usa fases, no capçaleres SESSIÓ).
        for s in sessions:
            if s["sa"] == "SA9":
                continue
            guia_path = (ARREL / "Classes" / s["sa"] /
                         f"{s['sa']}_guia_docent.md")
            if not guia_path.exists():
                errors.append(f"[quadern] falta la guia docent "
                              f"{guia_path.relative_to(ARREL)} (referenciada "
                              f"des de {s['sa']} S{s['s']} del quadern)")
                fallats += 1
                continue
            guia = guia_path.read_text(encoding="utf-8")
            cap = re.search(rf"^## SESSIÓ {s['s']} \(2 h\) — (.+)$", guia, re.M)
            if not cap or cap.group(1).strip() != s["titol"]:
                errors.append(f"[quadern] {s['sa']} S{s['s']}: títol «{s['titol']}» "
                              f"no coincideix amb la guia docent")
                fallats += 1
    for t in q.SESSIONS:
        pdf = ARREL / "Classes" / "00_General" / "pdf" / f"Quadern_tecnic_T{t}.pdf"
        if not pdf.exists():
            avisos.append(f"[quadern] falta {pdf.relative_to(ARREL)} "
                          f"(genera'l amb generar_quadern_tecnic.py)")
    total = sum(len(s) for s in q.SESSIONS.values())
    print(f"5) Quadern tècnic: {total} sessions, {fallats} incoherències.")


# --- 6 · Ordre de l'itinerari: cap pàgina sense clau a DOC_ORDRE_CLAUS -------
def comprova_ordre_itinerari() -> None:
    """Cada pàgina d'una SA ha de tenir una clau a DOC_ORDRE_CLAUS; si no,
    cau al calaix de sastre del final de l'itinerari sense avisar. Reutilitza
    la llista real de generar.py per no desincronitzar-se."""
    classes = WEB / "classes"
    sa_dirs = sorted(d for d in classes.glob("sa*") if d.is_dir()) if classes.exists() else []
    if not sa_dirs:
        avisos.append("web/classes sense SA: check d'ordre omès (genera el web abans).")
        return
    sys.path.insert(0, str(ARREL / "web" / "_generador"))
    import generar as g
    claus = [k for k in g.DOC_ORDRE_CLAUS if k != "__codi__"]
    sense_clau = 0
    for d in sa_dirs:
        for pag in sorted(d.rglob("*.html")):
            rel = pag.relative_to(d)
            nom = pag.name.lower()
            # Salta portada i pàgines de codi (ordre propi via __codi__).
            if nom in ("index.html", "codi.html") or "codi" in rel.parts:
                continue
            ruta = str(rel).lower().replace(os.sep, "/")
            if not any(c in ruta for c in claus):
                errors.append(f"[ordre] {pag.relative_to(WEB)}: cap clau a "
                              f"DOC_ORDRE_CLAUS (cauria al final de l'itinerari; "
                              f"afegeix-ne una a generar.py)")
                sense_clau += 1
    print(f"6) Ordre itinerari: {len(sa_dirs)} SA, {sense_clau} pàgines sense clau d'ordre.")


# --- 7 · PII: cap adreça de correu als fitxers versionats --------------------
def fitxers_versionats(*patrons: str) -> list[Path]:
    """Fitxers sota control de versions que casen amb els patrons donats.
    core.quotepath=false + -z: rutes amb accents senceres, separades per NUL."""
    try:
        sortida = subprocess.run(
            ["git", "-c", "core.quotepath=false", "ls-files", "-z", "--", *patrons],
            cwd=ARREL, capture_output=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        avisos.append("git ls-files no disponible: checks sobre fitxers versionats omesos.")
        return []
    return [ARREL / p for p in sortida.decode("utf-8").split("\0") if p]


CORREU_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
CORREUS_PERMESOS = {"noreply@anthropic.com"}  # coautoria dels commits
# Partit en dos perquè aquest mateix fitxer no dispari el check.
CORREU_DOCENT = "tomeu@" + "conselldecent.com"


def comprova_pii() -> None:
    fitxers = fitxers_versionats("*.md", "*.js", "*.py", "*.html")
    fallats = 0
    for f in fitxers:
        if not f.exists():
            continue
        for num, linia in enumerate(
                f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for m in CORREU_RE.finditer(linia):
                correu = m.group(0).rstrip(".")
                if correu in CORREUS_PERMESOS:
                    continue
                on = f"{f.relative_to(ARREL)}:{num}"
                if correu == CORREU_DOCENT:
                    avisos.append(f"[pii] {on}: correu del docent ({correu})")
                else:
                    errors.append(f"[pii] {on}: adreça de correu «{correu}»")
                    fallats += 1
    print(f"7) PII (correus): {len(fitxers)} fitxers, {fallats} adreces no permeses.")


# --- 8 · PDF committats: validesa forta + sincronia amb la font ---------------
def comprova_pdfs() -> None:
    sys.path.insert(0, str(ARREL / "web" / "_generador"))
    from generador.pdfutil import hash_font, llegeix_marca, num_pagines

    fitxers = fitxers_versionats("*.pdf")
    fallats = 0
    for f in fitxers:
        if not f.exists():
            errors.append(f"[pdf] {f.relative_to(ARREL)}: versionat però absent del disc")
            fallats += 1
            continue
        with f.open("rb") as fh:
            capçalera = fh.read(5)
        mida = f.stat().st_size
        if capçalera != b"%PDF-":
            errors.append(f"[pdf] {f.relative_to(ARREL)}: no comença per %PDF-")
            fallats += 1
        elif mida <= 1024:
            errors.append(f"[pdf] {f.relative_to(ARREL)}: només {mida} B (≤ 1 KB)")
            fallats += 1
        elif num_pagines(f) < 1:
            errors.append(f"[pdf] {f.relative_to(ARREL)}: 0 pàgines (render "
                          f"truncat de Chrome? regenera'l)")
            fallats += 1

    # Sincronia font ↔ PDF: cada full imprimible i quadern porta una marca
    # amb el hash de la seva font. Si la font ha canviat sense regenerar el
    # PDF, error; si el PDF encara no té marca (anterior al sistema), avís.
    import generar_fulls_imprimibles as gfi

    parelles: list[tuple[Path, Path]] = []
    for rel, _ in gfi.TARGETS:
        md = ARREL / "Classes" / rel
        parelles.append((md, md.parent / "pdf" / (md.stem + ".pdf")))
    for rel in gfi.RAW_HTML:
        src = ARREL / "Classes" / rel
        parelles.append((src, ARREL / "Classes" / "00_General" / "pdf" /
                         (src.stem + ".pdf")))
    quadern_py = ARREL / "web" / "_generador" / "quadern_sessions.py"
    for pdf in sorted((ARREL / "Classes" / "00_General" / "pdf")
                      .glob("Quadern_tecnic_T*.pdf")):
        parelles.append((quadern_py, pdf))

    desfasats = 0
    for font, pdf in parelles:
        if not font.exists() or not pdf.exists():
            continue  # l'absència ja l'informen altres checks
        marca = llegeix_marca(pdf)
        if marca is None:
            avisos.append(f"[pdf-sync] {pdf.relative_to(ARREL)}: sense marca de "
                          f"sincronia (regenera'l per activar-la)")
        elif marca != hash_font(font.read_text(encoding="utf-8")):
            errors.append(f"[pdf-sync] {pdf.relative_to(ARREL)}: la font "
                          f"{font.relative_to(ARREL)} ha canviat després de "
                          f"generar el PDF (regenera'l)")
            desfasats += 1
    print(f"8) PDF versionats: {len(fitxers)} fitxers, {fallats} invàlids, "
          f"{desfasats} desfasats de la font.")


# --- 9 · Mojibake als .md versionats ------------------------------------------
SEQ_MOJIBAKE = ("Ã", "â€", "Â·")  # «Ã», «â€», «Â·»


def comprova_mojibake() -> None:
    fitxers = fitxers_versionats("*.md")
    fallats = 0
    for f in fitxers:
        if not f.exists():
            continue
        for num, linia in enumerate(
                f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            seqs = [s for s in SEQ_MOJIBAKE if s in linia]
            if seqs:
                errors.append(f"[mojibake] {f.relative_to(ARREL)}:{num}: "
                              f"conté {', '.join('«' + s + '»' for s in seqs)}")
                fallats += 1
    print(f"9) Mojibake: {len(fitxers)} .md, {fallats} línies sospitoses.")


# --- 10 · Sintaxi dels .py del solucionari (Reptes/**) ------------------------
def comprova_python_reptes() -> None:
    fitxers = sorted((ARREL / "Reptes").rglob("*.py"))
    fallats = 0
    for f in fitxers:
        error = comprova_sintaxi_py(f)
        if error:
            errors.append(f"[python-reptes] {f.relative_to(ARREL)}: {error}")
            fallats += 1
    print(f"10) Python del solucionari: {len(fitxers)} fitxers, {fallats} amb errors de sintaxi.")


# --- 12 · Bloc «Què has d'entregar» de cada SA -------------------------------
def comprova_lliurables() -> None:
    """El README de cada SA té el bloc «📦 Què has d'entregar» sincronitzat
    amb les sessions reals de quadern_sessions.py (files S-n, fila de prova,
    files ⭐/📓 sempre i 🤖 a SA2-SA9)."""
    if NOMES_SINTAXI:
        print("12) Lliurables per SA: omès (--nomes-sintaxi).")
        return
    sys.path.insert(0, str(ARREL / "web" / "_generador"))
    import quadern_sessions as q

    sessions_sa: dict[str, int] = {}
    prova_sa: dict[str, int] = {}
    for sessions in q.SESSIONS.values():
        for s in sessions:
            sessions_sa[s["sa"]] = sessions_sa.get(s["sa"], 0) + 1
            if s.get("prova"):
                prova_sa[s["sa"]] = s["s"]

    fallats = 0
    for n in range(1, 10):
        sa = f"SA{n}"
        text = (ARREL / "Classes" / sa / "README.md").read_text(encoding="utf-8")
        m = re.search(r"^## 📦 Què has d'entregar\n(.*?)(?=^## |\Z)",
                      text, re.M | re.S)
        if not m:
            errors.append(f"[lliurables] {sa}: falta el bloc «📦 Què has d'entregar» al README")
            fallats += 1
            continue
        bloc = m.group(1)
        files_s = re.findall(r"^\|\s*S(\d+)\s*\|", bloc, re.M)
        if len(files_s) != sessions_sa.get(sa, 0):
            errors.append(f"[lliurables] {sa}: {len(files_s)} files de sessió "
                          f"però la SA té {sessions_sa.get(sa, 0)} sessions")
            fallats += 1
        if sa in prova_sa:
            fila = re.search(rf"^\|\s*S{prova_sa[sa]}\s*\|(.*)$", bloc, re.M)
            if not fila or "Prova pràctica" not in fila.group(1):
                errors.append(f"[lliurables] {sa}: la fila S{prova_sa[sa]} "
                              f"ha de contenir «Prova pràctica»")
                fallats += 1
        for icona, cal in (("⭐", True), ("📓", True), ("🤖", n >= 2)):
            te = bool(re.search(rf"^\|\s*{icona}\s*\|", bloc, re.M))
            if cal and not te:
                errors.append(f"[lliurables] {sa}: falta la fila {icona}")
                fallats += 1
            elif not cal and te:
                errors.append(f"[lliurables] {sa}: la fila {icona} no hi va (SA1 sense robot)")
                fallats += 1
    print(f"12) Lliurables per SA: 9 README, {fallats} incoherències.")


# --- 13 · Pàgines de pràctica: cada sketch d'alumnat té la seva explicació ---
def comprova_explicacions() -> None:
    """Cada sketch d'alumnat (Classes/SAn/codi) ha de tenir l'explicació que
    el generador converteix en pàgina de pràctica: EXPLICACIO.md dins de la
    carpeta del sketch, o <nom>_EXPLICACIO.md al costat si és un fitxer solt.
    També vigila que no reapareguin sketches *_BASTIDA: les bastides viuen
    fusionades a la secció «Si t'encalles» de la pràctica base."""
    if NOMES_SINTAXI:
        print("13) Pàgines de pràctica: omès (--nomes-sintaxi).")
        return
    total = 0
    fallats = 0
    for sa_dir in sorted((ARREL / "Classes").glob("SA*")):
        codi = sa_dir / "codi"
        if not codi.exists():
            continue
        for f in sorted(codi.rglob("*")):
            if f.suffix.lower() != ".py" or "__pycache__" in f.parts:
                continue
            rel = f.relative_to(ARREL)
            if "_BASTIDA" in f.stem:
                errors.append(f"[explicacions] {rel}: sketch _BASTIDA solt "
                              f"(fusiona'l a la secció «Si t'encalles» de la pràctica base)")
                fallats += 1
                continue
            if f.parent == codi:                      # fitxer solt (micro:bit)
                expl = f.with_name(f.stem + "_EXPLICACIO.md")
            elif f.stem == f.parent.name:             # fitxer principal del sketch
                expl = f.parent / "EXPLICACIO.md"
            else:
                continue                              # fitxer auxiliar (.h, etc.)
            total += 1
            if not expl.exists():
                errors.append(f"[explicacions] {rel}: falta {expl.name} "
                              f"(pàgina de pràctica sense explicació)")
                fallats += 1
    # Pont cap als reptes: cada pàgina de pràctica ha d'enllaçar el document
    # de reptes de la seva SA (si en té), perquè qui acaba abans tingui camí
    # natural cap al repte ⭐ (bloc «Has acabat abans?»).
    sense_pont = 0
    explicacions = sorted((ARREL / "Classes").glob("SA*/codi/**/*EXPLICACIO*.md"))
    for expl in explicacions:
        sa = expl.relative_to(ARREL / "Classes").parts[0]
        if not (ARREL / "Reptes" / f"Reptes_{sa}.md").exists():
            continue
        if f"Reptes_{sa}.md" not in expl.read_text(encoding="utf-8"):
            errors.append(f"[explicacions] {expl.relative_to(ARREL)}: sense "
                          f"enllaç a Reptes_{sa}.md (falta el bloc «Has acabat abans?»)")
            sense_pont += 1
    print(f"13) Pàgines de pràctica: {total} sketches, {fallats} sense explicació, "
          f"{sense_pont} sense pont als reptes.")


# --- 14 · Projectes trimestrals: portada present i enllaçant el dossier -----
def comprova_projectes_trimestrals() -> None:
    """Cada projecte trimestral (generar.PROJECTES) ha de tenir portada a
    Classes/00_General i la portada ha d'enllaçar el seu dossier (si no, la
    secció del web queda sense pàgina d'entrada o sense camí cap al dossier)."""
    if NOMES_SINTAXI:
        print("14) Projectes trimestrals: omès (--nomes-sintaxi).")
        return
    sys.path.insert(0, str(ARREL / "web" / "_generador"))
    import generar as g

    base = ARREL / "Classes" / "00_General"
    fallats = 0
    for pr in g.PROJECTES:
        portada = base / pr["portada"]
        if not portada.exists():
            errors.append(f"[projectes] falta la portada {pr['portada']}")
            fallats += 1
            continue
        text = portada.read_text(encoding="utf-8")
        if pr["dossier"] not in text:
            errors.append(f"[projectes] {pr['portada']} no enllaça el dossier {pr['dossier']}")
            fallats += 1
    print(f"14) Projectes trimestrals: {len(g.PROJECTES)} portades, {fallats} incoherències.")


# --- 15 · Codi incrustat als solucionaris sincronitzat amb el fitxer font ----
RE_CODI_INCRUSTAT = re.compile(
    r"<summary>Desplega el codi complet \(<code>([^<]+)</code>[^<]*</summary>\s*"
    r"\n```\w*\n(.*?)\n```", re.S)


def comprova_codi_incrustat() -> None:
    """Els solucionaris incrusten el codi complet dels robots trimestrals en
    un <details> perquè es pugui llegir sense sortir de la pàgina. El fitxer
    de veritat és el de Classes/Solucionari/codi/ (el vigila comprova_python):
    si els dos divergeixen, la web ensenyaria un codi que no és el provat."""
    if NOMES_SINTAXI:
        print("15) Codi incrustat: omès (--nomes-sintaxi).")
        return
    base_codi = ARREL / "Classes" / "Solucionari" / "codi"
    total = 0
    fallats = 0
    for md in sorted((ARREL / "Classes" / "Solucionari").glob("*.md")):
        text = md.read_text(encoding="utf-8")
        for m in RE_CODI_INCRUSTAT.finditer(text):
            nom, bloc = m.group(1).strip(), m.group(2)
            total += 1
            font = base_codi / Path(nom).stem / nom
            if not font.exists():
                errors.append(f"[codi-incrustat] {md.relative_to(ARREL)}: el "
                              f"desplegable diu «{nom}» però no existeix "
                              f"{font.relative_to(ARREL)}")
                fallats += 1
                continue
            if bloc.rstrip() != font.read_text(encoding="utf-8").rstrip():
                errors.append(f"[codi-incrustat] {md.relative_to(ARREL)}: el "
                              f"bloc del desplegable no coincideix amb "
                              f"{font.relative_to(ARREL)} (copia-hi el fitxer "
                              f"sencer actualitzat)")
                fallats += 1
    print(f"15) Codi incrustat: {total} desplegables, {fallats} desincronitzats.")


# --- 11 · Enllaços externs (OPT-IN: QA_ENLLACOS_EXTERNS=1) ---------------------
RE_URL_EXTERN = re.compile(r"https?://[^\s)\"'<>\]]+")
DOMINIS_IGNORATS = (
    # el web propi i serveis que responen 4xx/redireccions a robots sense sessió
    "classroom.google.com", "docs.google.com", "drive.google.com",
    "github.com/tomeu-cd100",
)


def comprova_enllacos_externs() -> None:
    """Valida (HEAD/GET) els enllaços externs dels .md versionats. Només
    s'executa amb QA_ENLLACOS_EXTERNS=1: depèn de la xarxa (lent i volàtil,
    la del centre bloqueja dominis), així que mai no bloqueja el CI de push.
    Els problemes surten com a AVÍS, no com a error."""
    if os.environ.get("QA_ENLLACOS_EXTERNS") != "1":
        print("11) Enllaços externs: omès (activa'l amb QA_ENLLACOS_EXTERNS=1).")
        return
    import urllib.error
    import urllib.request

    urls: dict[str, Path] = {}
    for f in fitxers_versionats("*.md"):
        if not f.exists():
            continue
        for m in RE_URL_EXTERN.finditer(f.read_text(encoding="utf-8", errors="replace")):
            url = m.group(0).rstrip(".,;:!?")
            if not any(d in url for d in DOMINIS_IGNORATS):
                urls.setdefault(url, f)
    caiguts = 0
    for url, origen in sorted(urls.items()):
        peticio = urllib.request.Request(
            url, method="HEAD", headers={"User-Agent": "Mozilla/5.0 (qa-curs)"})
        try:
            with urllib.request.urlopen(peticio, timeout=10) as resp:
                codi = resp.status
        except urllib.error.HTTPError as e:
            # Alguns servidors rebutgen HEAD: reintenta amb GET abans d'avisar.
            if e.code in (403, 405):
                try:
                    peticio = urllib.request.Request(
                        url, headers={"User-Agent": "Mozilla/5.0 (qa-curs)"})
                    with urllib.request.urlopen(peticio, timeout=10) as resp:
                        codi = resp.status
                except Exception as e2:
                    codi = getattr(e2, "code", str(e2))
            else:
                codi = e.code
        except Exception as e:
            codi = str(e)
        if codi != 200:
            avisos.append(f"[extern] {url} → {codi} (a {origen.relative_to(ARREL)})")
            caiguts += 1
    print(f"11) Enllaços externs: {len(urls)} URL úniques, {caiguts} amb problemes (avís).")


def comprova_dependencies() -> None:
    """Els checks 6 i 8 importen mòduls del generador (generar.py,
    generar_fulls_imprimibles.py) que depenen de paquets externs. Sense ells,
    el QA petava amb un ModuleNotFoundError a mig camí: millor fallar aquí,
    d'hora i amb la instrucció d'instal·lació."""
    falten = [p for p in ("markdown", "pygments") if importlib.util.find_spec(p) is None]
    if falten:
        print("0) Dependències del generador: FALTA " + " i ".join(falten) + ".")
        print("   El QA les necessita (checks 6 i 8 importen el generador).")
        print("   Instal·la-les amb:")
        print("     py -m pip install -r web/_generador/requirements.txt")
        sys.exit(2)
    print("0) Dependències del generador (markdown, pygments): instal·lades.")


def main() -> int:
    global NOMES_SINTAXI
    parser = argparse.ArgumentParser(description="QA del material i del web generat.")
    parser.add_argument("--nomes-sintaxi", action="store_true",
                        help="salta els checks de cobertura/contingut de SA "
                             "(cobertura, hores, quadern, lliurables, "
                             "explicacions, projectes, codi incrustat): per "
                             "committar infraestructura abans que existeixi "
                             "el material de curs.")
    args = parser.parse_args()
    NOMES_SINTAXI = args.nomes_sintaxi

    comprova_dependencies()
    comprova_enllacos_web()
    comprova_cobertura_sa()
    comprova_hores()
    comprova_python()
    comprova_quadern()
    comprova_ordre_itinerari()
    comprova_pii()
    comprova_pdfs()
    comprova_mojibake()
    comprova_python_reptes()
    comprova_enllacos_externs()
    comprova_lliurables()
    comprova_explicacions()
    comprova_projectes_trimestrals()
    comprova_codi_incrustat()
    for a in avisos:
        print(f"⚠️  {a}")
    if errors:
        print(f"\n❌ QA: {len(errors)} problemes:")
        for e in errors:
            print("   " + e)
        return 1
    print("\n✅ QA net.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
