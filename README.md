# Robòtica amb Python · 1r de Batxillerat (curs 2026-2027)

Material docent per a la matèria optativa **Robòtica amb Python** de 1r de Batxillerat
(modalitats científica i tecnològica), en el marc de la **LOMLOE** a **Catalunya**
(Decret 171/2022).

> **2 hores setmanals · curs anual (≈70 h) · nivell alt · en català**
> Programació real amb **micro:bit V2** (MicroPython) + **Micro:shield** i sensors
> **Keyestudio**, electrònica i sistemes de control.

> Aquest repositori és una **adaptació** del curs germà
> [«Robòtica» (Arduino + micro:bit)](../Curs%202627%201%20Batx%20Robotica), substituint
> el maquinari Arduino per **micro:bit + Micro:shield + Keyestudio** i el codi `.ino`
> per **MicroPython (`.py`)** exclusivament. Consulta `CLAUDE.md` per a les regles
> completes del repositori.

---

## Estat actual

El curs està **complet**: infraestructura, programació didàctica (00-18), les 9
situacions d'aprenentatge (guia docent, fitxa d'alumnat, esquemes, codi, reptes
i solucionari), avaluació i recursos. `py tools/qa.py` (sense flags) valida tot
el repositori i ha de donar «✅ QA net.» — és el que executa el CI a cada push.
Pendent de fase posterior: Classroom real, fotos de muntatges amb maquinari i
publicació a GitHub Pages (només amb confirmació del docent). Vegeu
`GUIA_INICI_DOCENT.md` per a l'itinerari de lectura i la checklist d'arrencada.

## 🎯 Plantejament

La matèria s'organitza en **9 situacions d'aprenentatge (SA1-SA9)** distribuïdes en
tres trimestres, amb un enfocament competencial i pràctic. Es vincula a
**Tecnologia i Enginyeria I** (competència específica de control i robòtica + bloc
d'automatització).

| Trimestre | SA | Hores |
|---|---|---|
| **1r** | SA1 · SA2 · SA3 | 6 + 8 + 8 = 22 h |
| **2n** | SA4 · SA5 · SA6 | 8 + 6 + 8 = 22 h |
| **3r** | SA7 · SA8 · SA9 | 8 + 6 + 10 = 24 h |

**Total: 68 h + marge** (~70 h de curs). El quadre exacte es fixarà a
`Programació didàctica/08_Sequenciacio_temporal_anual.md`.

---

## 🗂️ Estructura del repositori

| Carpeta | Contingut |
|---|---|
| **`Normativa/`** | Síntesi del marc legal LOMLOE + PDFs oficials. |
| **`Programació didàctica/`** | Programació completa: objectius, sabers, metodologia, avaluació, rúbriques, seqüenciació anual i les 9 SA. |
| **`Classes/`** | Material d'aula per SA (guia docent, fitxa d'alumnat, esquemes de connexions i **codi `.py`**), amb `Solucionari/` per a les ampliacions de les pràctiques. |
| **`Reptes/`** | Reptes triables per a cada SA1-SA8, amb el seu `Solucionari/`. |
| **`Simulacions/`** | Circuits i codi en format **Wokwi** de les pràctiques i dels reptes. |
| **`Avaluació/`** | Proves pràctiques per trimestre, amb graella de correcció i solució orientativa. |
| **`Recursos/`** | Recursos de professorat en obert i materials de suport. |
| **`Memòria treball/`** | Registre datat de l'evolució del projecte. |
| **`web/`** | Web generat (doble vista alumnat/docent) a partir de tot el material `.md`. |

---

## 🧰 Maquinari de referència

Curs pensat per a kits **micro:bit V2** amb **Micro:shield** i sensors
**Keyestudio** (LED, LDR, servos, motors, ultrasons...). Tot el codi d'alumnat és
**MicroPython (`.py`)**: no hi ha cap `.ino` ni compilació Arduino en aquest
repositori. Es pot treballar sense maquinari amb el simulador **Wokwi**.

> ℹ️ El codi inclou comentaris en català **sense accents** de manera intencionada,
> per evitar problemes de codificació als editors de l'alumnat.

**Tot el treball de l'alumnat és individual**: cap activitat en parelles ni en grup.

---

## 🚀 Com usar aquest material

> 🟢 **És el teu primer cop amb aquest material?** Comença per
> **[`GUIA_INICI_DOCENT.md`](GUIA_INICI_DOCENT.md)**.

1. Llegeix la **`GUIA_INICI_DOCENT.md`**.
2. Mira la visió de conjunt a `Programació didàctica/00_Index_general.md` (quan existeixi).
3. Per a cada sessió, obre la SA corresponent dins `Classes/` (guia docent + fitxa
   d'alumnat + codi).
4. Avalua amb les proves de `Avaluació/` i les rúbriques de
   `Programació didàctica/07_Rubriques.md`.

## 🌐 Generar el web

```bash
py -m pip install -r web/_generador/requirements.txt
py web/_generador/generar.py
```

Obre `web/index.html` amb el navegador. El web es reconstrueix a cada canvi del
material `.md`; `web/` (excepte `_generador/`, `assets/css/estil.css`,
`assets/js/lloc.js` i aquest `README.md`) és artefacte generat, no s'edita a mà.

## ✅ Passar el QA

```bash
py tools/qa.py
```

Comprova cobertura de les 9 SA, enllaços interns del web generat, quadre
d'hores, sintaxi dels `.py` (`ast.parse`) d'alumnat i de solucionari, PII,
PDFs versionats, mojibake i coherència dels projectes trimestrals. Ha de donar
«✅ QA net.» (els avisos `⚠️` de PDFs pendents de regenerar no bloquegen). És
exactament el que executa `.github/workflows/qa.yml` a cada push i pull
request. L'opció `--nomes-sintaxi` (salta els checks de cobertura/contingut)
només té sentit per a un fork que encara no tingui el material complet.

---

## ✍️ Autoria

Concepció i direcció pedagògica: **Tomeu Riera**. Material elaborat amb l'assistència
de **[Claude Code](https://claude.com/claude-code)** (Anthropic), sota la supervisió i
revisió del docent.

---

## 📄 Llicència

Aquest material es publica sota llicència **[Creative Commons
Reconeixement-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.ca)**.

Ets lliure de **compartir** i **adaptar** el material per a qualsevol finalitat, fins
i tot comercial, sempre que en facis **reconeixement** de l'autoria i distribueixis
les obres derivades amb la **mateixa llicència**. Vegeu el fitxer [`LICENSE`](LICENSE).
