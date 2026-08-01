"""Genera les plantilles SVG de tall laser dels robots del curs (mides en mm).

Robots del curs (micro:bit V2 + Micro:shield, vegeu
Classes/00_General/00_Projecte_T{1,2,3}_*.md i 00_Fil_conductor_construccions.md
Sec. 3.1 "xTool S1 (talladora laser)"):

  - T1 Mascota: caixa de DM 3 mm (base + 4 laterals + tapa + 2 orelles).
  - T2 Vehicle: xassis de DM 3 mm amb encaixos de motor integrats.
  - T3 Rover: NO te cap plantilla laser propia. Reaprofita integrament el
    xassis del vehicle (T2); les seves dues peces d'ampliacio (suport
    HC-SR04, suport del seguidor de linia) son impressio 3D
    (Recursos/peces_3d/*.scad, fora d'abast d'aquest script). Nomes T1 i T2
    consumeixen hores de talladora laser (vegeu 00_Fil_conductor_construccions.md
    Sec. 3.1: "T3 no consumeix hores de laser").

Conveni de capes per a xTool Creative Space:
  - negre  (#000000) = tall
  - vermell (#ff0000) = gravat (zones de personalitzacio i etiquetes)

Us:  py -3.13 tools/genera_plantilles_laser.py
Sortida:  Recursos/plantilles_laser/{mascota,xassis_vehicle}.svg
Material de referencia: DM de 3 mm. Forats M3 = diametre 3,2 mm.
"""
from pathlib import Path

SORTIDA = Path(__file__).resolve().parent.parent / "Recursos" / "plantilles_laser"
TALL = 'fill="none" stroke="#000000" stroke-width="0.2"'
GRAVAT = 'fill="none" stroke="#ff0000" stroke-width="0.2"'
M3 = 3.2  # diametre de forat per a cargol M3


def rect(x, y, w, h, estil=TALL, r=0):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'rx="{r}" {estil}/>')


def cercle(cx, cy, d, estil=TALL):
    return f'<circle cx="{cx}" cy="{cy}" r="{d / 2}" {estil}/>'


def etiqueta(x, y, txt, mida=5):
    return (f'<text x="{x}" y="{y}" font-family="sans-serif" '
            f'font-size="{mida}" fill="#ff0000">{txt}</text>')


def cami(d, estil=TALL):
    return f'<path d="{d}" {estil}/>'


def desa(nom, ample, alt, elements):
    cos = "\n".join(elements)
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{ample}mm" '
           f'height="{alt}mm" viewBox="0 0 {ample} {alt}">\n{cos}\n</svg>\n')
    SORTIDA.mkdir(parents=True, exist_ok=True)
    (SORTIDA / nom).write_text(doc, encoding="utf-8")
    print(f"  {nom}: {ample}x{alt} mm")


def _forats_escaire(e, x, y, w, h):
    """4 forats M3 als caires (a 8 mm de cada cantonada), per als escaires
    d'angle impresos en 3D que uneixen les plaques de la caixa/xassis."""
    for fx, fy in [(x + 8, y + 8), (x + w - 8, y + 8),
                   (x + 8, y + h - 8), (x + w - 8, y + h - 8)]:
        e.append(cercle(fx, fy, M3))


def _finestra_servo(e, x, y):
    """Finestra de micro servo 9 g (23,5 x 12,5 mm) + 2 forats de cargol."""
    e.append(rect(x, y, 23.5, 12.5))
    e.append(cercle(x - 2.5, y + 6.25, 2))
    e.append(cercle(x + 26, y + 6.25, 2))


def mascota():
    """T1 - Caixa 70x55x40 (base + 4 laterals + tapa), amb orelles amb
    ranura de servo (Classes/00_General/00_Projecte_T1_Mascota.md).
    Unio amb escaires impresos en 3D i cargols M3 (forats a 8 mm del caire).
    """
    e = []

    def orella(x, y, forma="rodona"):
        """Orella amb una pestanya de 10 mm INTEGRADA al contorn (una sola
        peca de tall) que s'encaixa a la ranura de la tapa. Es pot redibuixar
        el contorn negre sempre que es mantingui la pestanya de 10 mm."""
        cx, cy = x + 17, y + 17
        r = 17
        # punts on la pestanya talla el cercle/triangle: x = cx +/- 5
        yt = round(cy + (r ** 2 - 5 ** 2) ** 0.5, 2)
        pestanya = (f"L {cx - 5} {yt + 10} L {cx + 5} {yt + 10} "
                    f"L {cx + 5} {yt} ")
        if forma == "rodona":
            e.append(cami(f"M {cx - 5} {yt} {pestanya}"
                          f"A {r} {r} 0 1 0 {cx - 5} {yt} Z"))
        else:  # forma == "gat" (triangular)
            b = cy + r * 0.7
            e.append(cami(f"M {cx - r} {b} Q {cx - r * 0.35} {b - r * 1.6} "
                          f"{cx} {b - r * 1.75} "
                          f"Q {cx + r * 0.35} {b - r * 1.6} {cx + r} {b} "
                          f"L {cx + 5} {b} {pestanya[2:]}"
                          f"L {cx - 5} {b} Z"))
        e.append(cercle(cx, cy, r * 1.3, GRAVAT))  # contorn de gravat (personalitzable)

    # BASE 70x55
    e.append(rect(0, 0, 70, 55))
    _forats_escaire(e, 0, 0, 70, 55)
    e.append(etiqueta(3, 10, "BASE"))
    # TAPA 70x55: finestra de servo (orelles/cua) + 2 ranures d'orella
    e.append(rect(78, 0, 70, 55))
    _forats_escaire(e, 78, 0, 70, 55)
    _finestra_servo(e, 91, 21)
    e.append(rect(84, 42, 10.4, 3.4))   # ranura orella esquerra
    e.append(rect(133, 42, 10.4, 3.4))  # ranura orella dreta
    e.append(etiqueta(81, 10, "TAPA"))
    # FRONTAL 70x40: cara de criatura - finestra de la matriu de LED (ulls),
    # PIR com a nas i boca somrient tallada (sortida de so + micro + polsador,
    # muntats darrere, vegeu Cablatge del dossier T1)
    e.append(rect(0, 60, 70, 40))
    _forats_escaire(e, 0, 60, 70, 40)
    e.append(rect(24.5, 70, 21, 21))              # finestra matriu de LED (ulls/cara)
    e.append(cercle(35, 92, 15))                  # finestra del PIR (el nas)
    e.append(cami("M 22 108 Q 35 116 48 108 Q 35 122 22 108 Z"))  # boca somrient
    e.append(etiqueta(3, 70, "FRONTAL - decora (vermell=gravat)", 3.5))
    # DARRERE 70x40: pas del cable USB
    e.append(rect(78, 60, 70, 40))
    _forats_escaire(e, 78, 60, 70, 40)
    e.append(rect(103, 88, 10, 6))
    e.append(etiqueta(81, 70, "DARRERE"))
    # LATERAL A / LATERAL B 55x40 (x2)
    for i, nom in enumerate(["LATERAL A", "LATERAL B"]):
        x0 = 156 + i * 60
        e.append(rect(x0, 60, 55, 40))
        _forats_escaire(e, x0, 60, 55, 40)
        e.append(etiqueta(x0 + 3, 70, nom))
    # Orelles (x2, formes de mostra diferents; l'alumnat en pot redibuixar el
    # contorn sempre que mantingui la pestanya de 10 mm)
    orella(0, 105, "rodona")
    orella(45, 105, "gat")
    e.append(etiqueta(0, 152, "ORELLES x2 - encaixen a la ranura de la TAPA", 4))
    desa("mascota.svg", 285, 158, e)


def xassis_vehicle():
    """T2 - Xassis de DM 3 mm amb encaixos integrats per als 2 motoreductors
    (muntats als laterals) i la roda boja (al davant), amb el centre lliure
    per a la micro:bit + Micro:shield i el portapiles
    (Classes/00_General/00_Projecte_T2_Vehicle.md). Els suports impresos en
    3D (roda_boja.scad, suport_motor.scad) fixen les peces sobre aquests
    encaixos, pero no formen part d'aquest tall.
    """
    e = []
    ample, alt = 190, 140
    e.append(rect(0, 0, ample, alt, r=10))
    # Encaixos (ranures de brida) per als motoreductors, als dos laterals
    for y0 in (50, 75):
        e.append(rect(0, y0, 8, 10))            # motor esquerre (vora x=0)
        e.append(rect(ample - 8, y0, 8, 10))     # motor dret (vora x=ample)
    e.append(etiqueta(2, 45, "MOTOR ESQUERRE", 3.5))
    e.append(etiqueta(ample - 38, 45, "MOTOR DRET", 3.5))
    # Roda boja (davant, centrada): 2 forats M3 per al suport imprès en 3D
    e.append(cercle(ample / 2 - 8, 14, M3))
    e.append(cercle(ample / 2 + 8, 14, M3))
    e.append(etiqueta(ample / 2 - 20, 26, "RODA BOJA", 3.5))
    # Placa central: 4 forats M3 per a la micro:bit + Micro:shield
    cx, cy = ample / 2, alt / 2 - 5
    for fx, fy in [(cx - 20, cy - 15), (cx + 20, cy - 15),
                   (cx - 20, cy + 15), (cx + 20, cy + 15)]:
        e.append(cercle(fx, fy, M3))
    e.append(etiqueta(cx - 22, cy - 20, "MICRO:BIT + MICRO:SHIELD", 3.5))
    # Zona del portapiles (guia de gravat, no es talla)
    e.append(rect(cx - 30, cy + 22, 60, 30, GRAVAT, r=3))
    e.append(etiqueta(cx - 27, cy + 30, "PORTAPILES 4xAA", 3.5))
    # Pas de cables cap al darrere
    e.append(rect(cx - 5, alt - 14, 10, 6))
    # Zona de gravat per al nom de l'alumne (personalitzacio, vegeu
    # "Fabricacio i personalitzacio" del dossier T2)
    e.append(rect(cx - 35, alt - 30, 70, 10, GRAVAT, r=2))
    e.append(etiqueta(cx - 32, alt - 22, "NOM (grava aqui)", 4))
    desa("xassis_vehicle.svg", ample, alt, e)


if __name__ == "__main__":
    mascota()
    xassis_vehicle()
    print("Plantilles generades a Recursos/plantilles_laser/.")
    print("Nota: el rover (T3) NO te plantilla laser propia (reaprofita el")
    print("xassis del vehicle T2); vegeu Recursos/plantilles_laser/README.md.")
