# Web · Robòtica amb Python · 1r de Batxillerat

Lloc web estàtic que recull **tot el material** de la matèria de manera interconnectada, amb coherència visual: **cada apartat un color** i **cada trimestre un color**. Funciona obrint-lo en local i publicat a GitHub Pages.

## Veure'l en local

Obre `web/index.html` amb el navegador (doble clic). Tot funciona sense servidor: navegació, cercador, tema clar/fosc i botons de copiar codi.

## Estructura

| Carpeta / fitxer | Contingut |
|---|---|
| `index.html` | Portada amb els apartats i les 9 SA per trimestre. |
| `programacio/`, `classes/`, `reptes/`, `avaluacio/`, `normativa/`, `recursos/` | Una pàgina per cada document, més pàgines de codi per SA. |
| `assets/css/` | `estil.css` (sistema de disseny) + `pygments.css` (ressaltat de codi). |
| `assets/js/` | `lloc.js` (tema, menú, cercador, copiar) + `cerca-index.js` (índex de cerca generat). |
| `assets/img/` | Imatges copiades del material. |
| `_generador/generar.py` | Generador que crea tot el web a partir dels `.md` del repositori. |

> El web és **generat**: no editis els `.html` a mà. Edita el material `.md` original i torna a generar.

## Regenerar el web

Després de canviar qualsevol material `.md`, executa des de l'arrel del repositori:

```bash
py web/_generador/generar.py
```

Requereix Python amb dues llibreries (pures, només per generar). Les versions
estan **fixades** a `web/_generador/requirements.txt` perquè el build sigui
reproduïble; instal·la-les preferiblement dins d'un entorn virtual:

```bash
python -m venv .venv
.venv\Scripts\activate                        # Windows
# source .venv/bin/activate                   # Linux/macOS
pip install -r web/_generador/requirements.txt
```

> El peu de cada pàgina («web generat el …») pren la data de **l'últim commit**
> (no la del rellotge), de manera que regenerar el mateix material no provoca
> canvis. En CI es pot fixar amb la variable d'entorn `SOURCE_DATE_EPOCH`.

## Publicar a GitHub Pages

Hi ha un workflow a `.github/workflows/pages.yml` que publica la carpeta `web/` automàticament a cada `push` a `main`.

Només cal activar-ho un cop: a GitHub → **Settings → Pages → Build and deployment → Source: GitHub Actions**.

El web quedarà a `https://tomeu-cd100.github.io/robotica-python-1batx-2627/`.

## Sistema de color

- **Apartats**: Programació (indi), Classes (cian), Reptes (ambre), Avaluació (gerani), Normativa (pissarra), Recursos (maragda).
- **Trimestres**: 1r (blau), 2n (violeta), 3r (magenta). Les pàgines de SA mostren un distintiu del seu trimestre.
