# -*- coding: utf-8 -*-
"""
Genera els diagrames de flux de cada SA com a SVG net, en l'estil visual del
curs (caixes teal, accent ambre, system-ui, fletxes). A partir d'una
descripcio de nodes per SA (dades), no dibuixa a ma: layout deterministe
vertical amb una bifurcacio opcional i una fletxa de bucle.

Us:  py web/_generador/gen_diagrames_flux.py   -> escriu Classes/SAn/img/san-flux.svg
"""
from __future__ import annotations
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# --- Estil (identic als SVG existents del curs) ------------------------------
STYLE = """
  .fr{fill:#f6faf9;stroke:#d7e6e5;stroke-width:1.5}
  .box{fill:#eaf3f2;stroke:#0891b2;stroke-width:1.8}
  .start{fill:#0891b2;stroke:#0e7490;stroke-width:1.8}
  .startt{font:700 14px system-ui,'Segoe UI',sans-serif;fill:#ffffff}
  .dec{fill:#fff7ed;stroke:#b45309;stroke-width:1.9}
  .boxt{font:600 13.5px system-ui,'Segoe UI',sans-serif;fill:#0e1b1c}
  .dect{font:700 13px system-ui,'Segoe UI',sans-serif;fill:#7c3a06}
  .wire{fill:none;stroke:#0891b2;stroke-width:2.3}
  .loop{fill:none;stroke:#b45309;stroke-width:2.3;stroke-dasharray:1 0}
  .lbl{font:700 12px system-ui,'Segoe UI',sans-serif;fill:#b45309}
  .yes{font:700 12px system-ui,'Segoe UI',sans-serif;fill:#0e7490}
"""

W = 720
CX = W // 2
BOXW, BOXH = 300, 52
BRW, BRH = 190, 56          # caixes de branca
GAP = 46                    # espai vertical entre files

def esc(s): return html.escape(str(s), quote=True)

def wrap_lines(text, maxch):
    """Parteix en <=2 linies per cabre a la caixa."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= maxch:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines[:2]

def tspans(text, x, y, cls, maxch=34):
    lines = wrap_lines(text, maxch)
    dy0 = -(len(lines) - 1) * 8
    out = []
    for i, ln in enumerate(lines):
        out.append(f'<text class="{cls}" x="{x}" y="{y + dy0 + i*16}" '
                   f'text-anchor="middle">{esc(ln)}</text>')
    return "".join(out)

def box(x, y, w, h, cls, text, tcls, maxch=34):
    return (f'<rect class="{cls}" x="{x-w//2}" y="{y-h//2}" width="{w}" '
            f'height="{h}" rx="11"/>' + tspans(text, x, y, tcls, maxch))

def diamond(x, y, text):
    w, h = 230, 96
    pts = f"{x},{y-h//2} {x+w//2},{y} {x},{y+h//2} {x-w//2},{y}"
    return (f'<polygon class="dec" points="{pts}"/>'
            + tspans(text, x, y, "dect", 26))

def arrow(x1, y1, x2, y2, cls="wire", marker="m"):
    return f'<path class="{cls}" d="M{x1},{y1} L{x2},{y2}" marker-end="url(#{marker})"/>'


def render(flow):
    """flow = {title, desc, nodes:[...], loop:(from_idx,to_idx,label)}
    node: ('start'|'action', text) o ('decision', cond, [(lbl,text),...])
    """
    parts = []
    y = 46
    centers = []      # y-center de cada node (spine)
    heights = []
    # primer passem per calcular alcades
    for n in flow["nodes"]:
        if n[0] == "decision":
            centers.append(y + 48); heights.append(96 + BRH + 40); y += 96 + BRH + 40 + GAP
        else:
            centers.append(y + BOXH//2); heights.append(BOXH); y += BOXH + GAP
    total_h = y + 10

    svg_body = []
    # fletxes spine (entre nodes consecutius)
    for i in range(len(flow["nodes"]) - 1):
        y1 = centers[i] + (heights[i]//2 if flow["nodes"][i][0] != "decision" else 96//2 + BRH + 20)
        y2 = centers[i+1] - (heights[i+1]//2 if flow["nodes"][i+1][0] != "decision" else 48)
        # per decisions la sortida ja la gestiona la branca; saltem si l'anterior es decisio
        if flow["nodes"][i][0] == "decision":
            continue
        top_next = centers[i+1] - (48 if flow["nodes"][i+1][0]=="decision" else BOXH//2)
        bot_this = centers[i] + BOXH//2
        svg_body.append(arrow(CX, bot_this, CX, top_next - 2))

    # nodes
    for i, n in enumerate(flow["nodes"]):
        cy = centers[i]
        if n[0] == "start":
            svg_body.append(box(CX, cy, BOXW, BOXH, "start", n[1], "startt"))
        elif n[0] == "action":
            svg_body.append(box(CX, cy, BOXW, BOXH, "box", n[1], "boxt"))
        elif n[0] == "decision":
            cond, branches = n[1], n[2]
            svg_body.append(diamond(CX, cy, cond))
            k = len(branches)
            slot = W // (k + 1)
            by = cy + 48 + 20 + BRH//2
            conv_y = by + BRH//2 + 22
            for j, (lbl, text) in enumerate(branches):
                bx = slot * (j + 1)
                # fletxa diamant -> branca (para una mica abans per deixar lloc a l'etiqueta)
                svg_body.append(arrow(CX, cy + 48, bx, by - BRH//2 - 16))
                # etiqueta de la branca: sobre la seva caixa, amb fons blanc per no trepitjar la fletxa
                lblw = 8 + len(lbl) * 7
                svg_body.append(f'<rect x="{bx - lblw//2}" y="{by - BRH//2 - 28}" '
                                f'width="{lblw}" height="18" rx="5" fill="#f6faf9"/>')
                svg_body.append(f'<text class="yes" x="{bx}" '
                                f'y="{by - BRH//2 - 15}" text-anchor="middle">{esc(lbl)}</text>')
                svg_body.append(box(bx, by, BRW, BRH, "box", text, "boxt", 24))
                # branca -> convergencia (nomes vertical fins conv_y) si hi ha node seguent o bucle
                svg_body.append(f'<path class="wire" d="M{bx},{by+BRH//2} L{bx},{conv_y}"/>')
            # linia de convergencia horitzontal
            xs = [slot*(j+1) for j in range(k)]
            svg_body.append(f'<path class="wire" d="M{min(xs)},{conv_y} L{max(xs)},{conv_y}"/>')

    # bucle (fletxa ambre de tornada)
    if flow.get("loop"):
        fi, ti, label = flow["loop"]
        # origen: part baixa de l'ultim node (o de la convergencia si es decisio)
        if flow["nodes"][fi][0] == "decision":
            oy = centers[fi] + 48 + 20 + BRH + 22
        else:
            oy = centers[fi] + BOXH//2
        ty = centers[ti]
        lx = 40  # canal esquerra
        d = (f"M{CX},{oy} L{CX-BOXW//2-30},{oy} "
             f"L{lx},{oy} L{lx},{ty} L{CX-BOXW//2-2},{ty}")
        svg_body.append(f'<path class="loop" d="{d}" marker-end="url(#mo)"/>')
        svg_body.append(f'<text class="lbl" x="{lx+8}" y="{(oy+ty)//2}" '
                        f'transform="rotate(-90 {lx+8} {(oy+ty)//2})" '
                        f'text-anchor="middle">{esc(label)}</text>')

    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {total_h}" '
           f'width="{W}" height="{total_h}" role="img" aria-labelledby="t d">'
           f'<title id="t">{esc(flow["title"])}</title>'
           f'<desc id="d">{esc(flow["desc"])}</desc>'
           f'<style>{STYLE}</style>'
           f'<defs>'
           f'<marker id="m" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">'
           f'<path d="M0,0 L7,3 L0,6 Z" fill="#0891b2"/></marker>'
           f'<marker id="mo" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">'
           f'<path d="M0,0 L7,3 L0,6 Z" fill="#b45309"/></marker>'
           f'</defs>'
           f'<rect class="fr" x="1" y="1" width="{W-2}" height="{total_h-2}" rx="14"/>'
           + "".join(svg_body) + '</svg>')
    return svg


FLOWS = {
    1: {"title": "Flux del senyal d'estat (Blink)",
        "desc": "En engegar, setup() configura el pin una vegada; despres el loop repeteix per sempre: encendre el LED, esperar, apagar-lo, esperar.",
        "nodes": [("start", "Engego la placa"),
                  ("action", "setup(): configuro el pin com a sortida"),
                  ("action", "Encenc el LED (digitalWrite HIGH)"),
                  ("action", "Espero un temps (delay)"),
                  ("action", "Apago el LED (digitalWrite LOW)"),
                  ("action", "Espero un temps (delay)")],
        "loop": (5, 2, "es repeteix")},
    2: {"title": "Flux del semafor",
        "desc": "Despres de configurar els pins, el loop repeteix la seqüencia de fases: vermell, verd i groc, cadascuna amb el seu temps.",
        "nodes": [("start", "Engego la placa"),
                  ("action", "setup(): configuro els 3 LED"),
                  ("action", "Fase VERMELL (encendre, esperar)"),
                  ("action", "Fase VERD (encendre, esperar)"),
                  ("action", "Fase GROC (encendre, esperar)")],
        "loop": (4, 2, "es repeteix")},
    3: {"title": "Flux de la llum automatica (sensor + llindar)",
        "desc": "El loop llegeix el sensor analogic i decideix per llindar: si la llum es per sota del llindar encen el LED; si no, l'apaga. I torna a comencar.",
        "nodes": [("start", "Engego la placa"),
                  ("action", "Llegeixo el sensor (analogRead, 0-1023)"),
                  ("decision", "llum < LLINDAR ?",
                   [("SÍ (fosc)", "Encenc el LED"), ("NO (clar)", "Apago el LED")])],
        "loop": (2, 1, "cada volta")},
    4: {"title": "Flux dels moviments del motor",
        "desc": "Amb les funcions de moviment ja fetes, el loop encadena els gestos: endavant, atura, enrere, atura; i es repeteix.",
        "nodes": [("start", "Engego la placa"),
                  ("action", "setup(): configuro els pins del motor"),
                  ("action", "endavant(velocitat)"),
                  ("action", "atura()"),
                  ("action", "enrere(velocitat)"),
                  ("action", "atura()")],
        "loop": (5, 2, "es repeteix")},
    5: {"title": "Flux del vigilant (micro:bit)",
        "desc": "Dins del while True, es llegeix un sensor integrat i es decideix segons el llindar: si el supera mostra una alerta, si no un estat de repos.",
        "nodes": [("start", "from microbit import *"),
                  ("action", "Llegeixo el sensor integrat"),
                  ("decision", "valor > LLINDAR ?",
                   [("SÍ", "Mostro alerta"), ("NO", "Mostro repos")])],
        "loop": (2, 1, "while True")},
    6: {"title": "Flux del control amb histeresi",
        "desc": "Llaç tancat: es llegeix el sensor i, amb dos llindars (histeresi), s'engega per sota del llindar baix i s'atura per sobre de l'alt; enmig es mante l'estat.",
        "nodes": [("start", "Engego la placa"),
                  ("action", "Llegeixo el sensor (realimentacio)"),
                  ("decision", "on es el valor?",
                   [("< BAIX", "Engego l'actuador"),
                    ("> ALT", "Aturo l'actuador"),
                    ("enmig", "Mantinc l'estat")])],
        "loop": (2, 1, "llaç tancat")},
    7: {"title": "Flux del robot reactiu (percepcio-decisio-accio)",
        "desc": "El loop llegeix la distancia (percepcio), decideix segons dos llindars i actua sobre els motors: recula si esta massa a prop, avanca si hi ha via lliure, s'atura enmig; i es repeteix.",
        "nodes": [("start", "Engego la placa"),
                  ("action", "PERCEP: llegeixo la distancia (ultrasons)"),
                  ("decision", "quina distancia? (DECIDEIX)",
                   [("< A_PROP", "ACTUA: enrere"),
                    ("> A_LLUNY", "ACTUA: endavant"),
                    ("enmig", "ACTUA: atura")])],
        "loop": (2, 1, "percepcio-accio")},
    8: {"title": "Flux de la telemetria (emissor)",
        "desc": "Amb la radio engegada, el loop mesura un sensor, construeix la dada etiquetada, l'envia per radio i espera; i es repeteix.",
        "nodes": [("start", "Engego la radio (on + group)"),
                  ("action", "Mesuro el sensor"),
                  ("action", "Construeixo la dada: 'T:' + valor"),
                  ("action", "radio.send(dada)"),
                  ("action", "Espero (sleep)")],
        "loop": (4, 1, "while True")},
    9: {"title": "Flux del metode de projecte",
        "desc": "S'analitza (requisits, MVP) i es dissenya; despres el cicle construir-provar es repeteix: si funciona es documenta i es lliura, si no es millora i es torna a construir (iteracio).",
        "nodes": [("start", "Analitzar (requisits, MVP)"),
                  ("action", "Dissenyar (planificar, taulell)"),
                  ("action", "Construir"),
                  ("action", "Provar"),
                  ("decision", "funciona?",
                   [("SÍ", "Documentar i lliurar"), ("NO", "Millorar")])],
        "loop": (4, 2, "iteracio")},
}


def main():
    for n, flow in FLOWS.items():
        svg = render(flow)
        out = ROOT / "Classes" / f"SA{n}" / "img" / f"sa{n}-flux.svg"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(svg, encoding="utf-8")
        print(f"  sa{n}-flux.svg  ({len(svg)} bytes)")
    print(f"Fet. {len(FLOWS)} diagrames de flux SVG.")


if __name__ == "__main__":
    main()
