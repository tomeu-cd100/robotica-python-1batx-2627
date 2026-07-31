"""Tests de les seccions de projecte trimestral (PROJECTES)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest  # noqa: E402
import generar  # noqa: E402
from generar import (  # noqa: E402
    PROJECTES, PROJECTE_BY_SLUG, PROJECTE_BY_SRC,
    group_label, group_sort_key, group_tri,
    ROOT, classify_public, out_for_projecte,
)

GENERAL = ROOT / "Classes" / "00_General"


def test_projectes_definits():
    assert [p["slug"] for p in PROJECTES] == [
        "projecte-t1", "projecte-t2", "projecte-t3"]
    assert PROJECTE_BY_SLUG["projecte-t3"]["after_sa"] == 6
    assert PROJECTE_BY_SRC["00_Projecte_T1_Mascota.md"]["num"] == 1
    assert PROJECTE_BY_SRC["00_Projecte_T1_portada.md"]["num"] == 1


def test_ordre_grups_amb_projectes():
    """SA3 < PT1 < SA4 i SA6 < PT2 < PT3 < SA7 (i transversal sempre primer)."""
    ordre = sorted(["sa4", "projecte-t1", "sa3", "sa7", "projecte-t3",
                    "projecte-t2", "sa6", "00-general"], key=group_sort_key)
    assert ordre == ["00-general", "sa3", "projecte-t1", "sa4", "sa6",
                     "projecte-t2", "projecte-t3", "sa7"]


def test_etiqueta_i_trimestre():
    assert group_label("projecte-t1") == "🐣 Projecte T1 · La mascota reactiva"
    assert group_label("projecte-t2") == "🦾 Projecte T2 · El braç robòtic"
    assert group_label("projecte-t3") == "🚙 Projecte T3 · El rover autònom"
    assert group_tri("projecte-t1") == 1
    assert group_tri("projecte-t3") == 3


def test_out_for_projecte():
    assert (out_for_projecte(GENERAL / "00_Projecte_T1_portada.md")
            == "classes/projecte-t1/index.html")
    assert (out_for_projecte(GENERAL / "00_Projecte_T3_Rover.md")
            == "classes/projecte-t3/00-projecte-t3-rover.html")
    assert out_for_projecte(GENERAL / "00_Glossari_tecnic.md") is None


def test_projecte_public_alumnat():
    assert classify_public("classes", GENERAL / "00_Projecte_T1_portada.md") == "alumnat"
    assert classify_public("classes", GENERAL / "00_Projecte_T2_Brac.md") == "alumnat"


@pytest.mark.skipif(
    not (ROOT / "Classes" / "SA3" / "SA3_guia_docent.md").exists(),
    reason="SA3 encara sense guia docent real (esquelet inicial)")
def test_pager_pont_sa3_projecte_t1():
    """El web generat ha de tenir el pont SA3 -> Projecte T1 al paginador."""
    web = ROOT / "web"
    sa3 = sorted((web / "classes" / "sa3").glob("*.html"))
    assert sa3, "cal haver generat el web abans dels tests de pont"
    tot = "".join(p.read_text(encoding="utf-8") for p in sa3)
    assert 'pager-a next" href="../projecte-t1/index.html"' in tot
    pt1 = (web / "classes" / "projecte-t1" / "index.html").read_text(encoding="utf-8")
    assert 'class="pager' in pt1


@pytest.mark.skipif(
    not (ROOT / "web" / "classes" / "00-general").is_dir()
    or not any((ROOT / "web" / "classes" / "00-general").glob("00-projecte-t*.html")),
    reason="dossiers de projecte encara no generats (esquelet inicial)")
def test_redireccions_dossiers():
    """Les URLs antigues dels dossiers (classes/00-general/…) han de quedar
    redirigides a la nova ruta classes/projecte-tN/, ja que poden estar
    enllaçades des del Classroom."""
    base = ROOT / "web" / "classes" / "00-general"
    for antic, nou in [
        ("00-projecte-t1-mascota.html", "../projecte-t1/00-projecte-t1-mascota.html"),
        ("00-projecte-t2-brac.html", "../projecte-t2/00-projecte-t2-brac.html"),
        ("00-projecte-t3-rover.html", "../projecte-t3/00-projecte-t3-rover.html"),
    ]:
        f = base / antic
        assert f.exists(), f"falta la redirecció {antic}"
        t = f.read_text(encoding="utf-8")
        assert nou in t and "refresh" in t.lower()
