"""Tests del nucli arriscat de generar.py: rewrite_links, classify_public,
is_activitat.

Executa'ls des de web/_generador/:  py -m pytest tests/ -q

generar.py s'importa com a mòdul (té guard __main__): en importar només
executa build_date() (git al repo) i defineix constants — cap escriptura.

Adaptació al curs nou: el germà feia servir fitxers REALS de Classes/SA1/
com a fixtures. Aquest repositori encara no té contingut de SA (és
infraestructura), així que els tests de rewrite_links creen els seus
propis fitxers .md temporals amb pytest tmp_path.
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import generar  # noqa: E402
from generar import (  # noqa: E402
    BLOB_BASE, ROOT, classify_public, is_activitat, rewrite_links,
)

OUT_FITXA = "classes/sa1/sa1-fitxa-alumnat.html"
OUT_GUIA = "classes/sa1/sa1-guia-docent.html"


@pytest.fixture
def fitxes(tmp_path):
    """Crea una guia docent i una fitxa d'alumnat sintètiques a tmp_path,
    imitant l'arbre real Classes/SA1/ sense dependre de contingut ja creat."""
    sa1 = tmp_path / "Classes" / "SA1"
    sa1.mkdir(parents=True)
    guia = sa1 / "SA1_guia_docent.md"
    fitxa = sa1 / "SA1_fitxa_alumnat.md"
    guia.write_text("# SA1 - guia docent\n", encoding="utf-8")
    fitxa.write_text("# SA1 - fitxa alumnat\n", encoding="utf-8")
    return fitxa, guia


def _rewrite(body: str, fitxes, md_map: dict | None = None) -> str:
    """Crida rewrite_links com ho fa el generador per a la fitxa de SA1."""
    fitxa, guia = fitxes
    if md_map is None:
        md_map = {str(guia.resolve()): OUT_GUIA,
                  str(fitxa.resolve()): OUT_FITXA}
    return rewrite_links(body, fitxa, OUT_FITXA,
                         md_map=md_map, code_map={}, sim_map={},
                         copied_imgs={})


# --- rewrite_links: enllaços interns .md --------------------------------------
def test_md_existent_es_reescriu_a_html(fitxes):
    out = _rewrite('<p><a href="SA1_guia_docent.md">guia</a></p>', fitxes)
    # mateixa carpeta de sortida -> URL relativa curta
    assert 'href="sa1-guia-docent.html"' in out
    assert "SA1_guia_docent.md" not in out


def test_md_existent_conserva_fragment(fitxes):
    out = _rewrite('<a href="SA1_guia_docent.md#sessions">sessions</a>', fitxes)
    assert 'href="sa1-guia-docent.html#sessions"' in out


def test_md_existent_pero_no_publicat_va_a_github(fitxes):
    # .md real (temporal) que NO és al md_map -> com el fitxer viu fora de
    # ROOT (tmp_path), el fallback a GitHub no s'aplica (relative_to falla)
    # i l'enllaç es deixa tal qual: comprova que almenys no peta ni inventa
    # una URL incorrecta.
    out = _rewrite('<a href="SA1_guia_docent.md">guia</a>', fitxes, md_map={})
    assert 'href="SA1_guia_docent.md"' in out


# --- rewrite_links: URLs externes --------------------------------------------
def test_url_externa_intacta_amb_target_blank(fitxes):
    out = _rewrite('<a href="https://wokwi.com/projects/1234">Wokwi</a>', fitxes)
    assert 'href="https://wokwi.com/projects/1234" target="_blank" rel="noopener"' in out


def test_url_externa_pdf_no_es_reescriu(fitxes):
    url = "https://exemple.cat/decret_171_2022.pdf"
    out = _rewrite(f'<a href="{url}">decret</a>', fitxes)
    assert f'href="{url}" target="_blank" rel="noopener"' in out


def test_mailto_i_data_intactes(fitxes):
    body = ('<a href="mailto:tomeu@conselldecent.com">escriu-me</a>'
            '<img src="data:image/png;base64,AAAA">')
    out = _rewrite(body, fitxes)
    assert 'href="mailto:tomeu@conselldecent.com"' in out
    assert 'target="_blank"' not in out  # mailto no obre pestanya nova
    assert 'src="data:image/png;base64,AAAA"' in out


# --- rewrite_links: fallback per a destins inexistents ------------------------
def test_fitxer_inexistent_es_deixa_tal_qual(fitxes):
    body = ('<a href="no_existeix_xyz.md">trencat</a>'
            '<img src="img/no_existeix_xyz.png">')
    out = _rewrite(body, fitxes)
    assert 'href="no_existeix_xyz.md"' in out
    assert 'src="img/no_existeix_xyz.png"' in out


def test_ancora_local_intacta(fitxes):
    out = _rewrite('<a href="#material">material</a>', fitxes)
    assert 'href="#material"' in out


# --- rewrite_links: mai dins de <pre>/<code> (integració amb apply_outside_code)
def test_no_toca_res_dins_de_pre_ni_code(fitxes):
    body = ('<p><a href="SA1_guia_docent.md">fora</a></p>'
            '<pre><code>&lt;a href="SA1_guia_docent.md"&gt;literal&lt;/a&gt;\n'
            'src="foto.png"</code></pre>'
            '<p>inline <code>href="SA1_guia_docent.md"</code></p>')
    out = _rewrite(body, fitxes)
    # el de fora es reescriu...
    assert 'href="sa1-guia-docent.html"' in out
    # ...però els literals dins de pre/code queden intactes
    assert out.count('href="SA1_guia_docent.md"') == 2
    assert 'src="foto.png"' in out


# --- classify_public -----------------------------------------------------------
def test_seccio_docent_sempre_docent():
    assert classify_public("programacio", Path("Programació didàctica/04_Metodologia.md")) == "docent"


def test_general_alumnat_nomes_la_llista():
    base = Path("Classes/00_General")
    assert classify_public("classes", base / "00_Repas_expres_MicroPython.md") == "alumnat"
    assert classify_public("classes", base / "00_Glossari_tecnic.md") == "alumnat"
    # qualsevol altre transversal és del docent (p. ex. el mode supervivència)
    assert classify_public("classes", base / "00_Mode_supervivencia.md") == "docent"
    assert classify_public("classes", base / "00_Banc_activacio_repas.md") == "docent"


def test_pistes_de_nom_docent():
    base = Path("Classes/SA3")
    assert classify_public("classes", base / "SA3_guia_docent.md") == "docent"
    assert classify_public("classes", base / "SA3_checklist_docent.md") == "docent"


def test_fitxa_alumnat_i_solucionari():
    assert classify_public("classes", Path("Classes/SA3/SA3_fitxa_alumnat.md")) == "alumnat"
    # els esquemes NO són a DOCENT_NAME_HINTS: es publiquen a l'alumnat
    assert classify_public("classes", Path("Classes/SA3/SA3_esquemes_connexions.md")) == "alumnat"
    # qualsevol carpeta Solucionari -> docent, encara que el nom sembli d'alumnat
    assert classify_public("reptes", Path("Reptes/Solucionari/Solucions_SA3.md")) == "docent"


# --- is_activitat ---------------------------------------------------------------
def test_is_activitat_positius():
    assert is_activitat(Path("Classes/SA1/SA1_fitxa_alumnat.md"))
    assert is_activitat(Path("Classes/SA3/SA3_fitxa_ampliada.md"))
    assert is_activitat(Path("Reptes/Reptes_SA4.md"))
    assert is_activitat(Path("Avaluació/Prova_practica_T1.md"))
    assert is_activitat(Path("Classes/00_General/00_Quadern_tecnic.md"))
    assert is_activitat(Path("Classes/SA9/plantilles/dossier.md"))


def test_is_activitat_negatius():
    assert not is_activitat(Path("Classes/SA1/SA1_guia_docent.md"))
    assert not is_activitat(Path("Classes/SA1/README.md"))
    assert not is_activitat(Path("Classes/SA1/SA1_esquemes_connexions.md"))
    assert not is_activitat(Path("Classes/SA9/plantilles/notes.txt"))
    # el solucionari dels reptes no és cap activitat d'alumnat
    assert not is_activitat(Path("Reptes/Solucionari/Solucions_SA4.md"))
