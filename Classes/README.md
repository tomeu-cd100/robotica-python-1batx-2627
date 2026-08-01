# Classes — material d'aula

Material llest per a l'aula de cada situació d'aprenentatge, amb el **codi** MicroPython funcional i el solucionari de les ampliacions («+ repte») de les pràctiques. *(El solucionari dels reptes triables A/B/C és a [`../Reptes/Solucionari/`](../Reptes/Solucionari/).)*

> Navega per les **targetes de més avall**: el [material transversal](00_General/README.md), la **SA0** (preàmbul) i les **SA1–SA9** ordenades per trimestre, cadascuna amb la seva subcarpeta i tots els materials enllaçats.

## Com s'organitza

Cada subcarpeta `SAx/` conté, segons la SA (detall complet a [`00_General/00_LLEGEIX-ME_Classes.md`](00_General/00_LLEGEIX-ME_Classes.md)):

- **`SAx_guia_docent.md`** — desenvolupament de la sessió per al professorat.
- **`SAx_fitxa_alumnat.md`** — **fitxa base** (nucli d'una cara, per a tot l'alumnat).
- **`SAx_fitxa_ampliada.md`** — **versió ampliada** (aprofundiment) per a qui vulgui/pugui més.
- **`SAx_checklist_docent.md`** / **`SAx_checklist_alumnat.md`** — recordatori d'una cara per a cada públic.
- **`SAx_questionari_conceptes.md`** — qüestionari autocorrectiu de repàs.
- **`SAx_exemple_resolt.md`** — un exemple complet i comentat.
- **`SAx_esquemes_connexions.md`** (SA1–SA8) — connexions micro:bit/Micro:shield ↔ sensors/actuadors.
- **`codi/`** — programes `.py` (MicroPython), oberts directament a l'editor de micro:bit o a Thonny.

A més, el [**material transversal del curs**](00_General/README.md) (guia general, entorns de treball, fil conductor dels tres robots individuals, IA, avaluació) i el [**Solucionari**](Solucionari/) de les ampliacions, per trimestre.

## El fil conductor individual

Tot l'alumnat construeix, per **conseqüent individual**, el mateix fil conductor de tres robots: 🐣 mascota (T1) → 🚗 vehicle teledirigit (T2) → 🚙 rover autònom (T3). Dossiers complets i calendari de fabricació digital (talladora làser + impressora 3D) a [`00_General/00_Fil_conductor_construccions.md`](00_General/00_Fil_conductor_construccions.md).

## Convencions de codi

- Tot el codi del curs és **MicroPython** (`.py`) per a **micro:bit V2 + Micro:shield**: cap `.ino` ni compilació Arduino (a diferència del curs germà d'Arduino + C++).
- Comentaris en català **sense accents** (evita problemes de codificació a l'editor).
- Assignació de pins **consistent** entre SA (documentada als esquemes de cada SA i fixada de manera definitiva a les sessions de muntatge del vehicle i del rover).

> La planificació didàctica de cada SA és a [`../Programació didàctica/`](../Programació%20didàctica/).
