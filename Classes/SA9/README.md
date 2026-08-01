# SA9 · Repte final integrador

**Durada:** 10 h (5 sessions; S5 = Prova pràctica T3) · **Maquinari:** tot el maquinari del curs (micro:bit V2 + Micro:shield, Kits Keyestudio 1-3, rover de SA7-SA8); reserva d'humitat del terra (Kit 2) i bomba d'aigua/relé (Kit 3) per al repte de reg/domòtica

Novena i última situació d'aprenentatge del curs (3r trimestre, la tercera): el **projecte de síntesi**. Cada alumne, **individualment**, amplia el seu rover (SA7-SA8) amb un **repte lliure** que resol un problema real senzill, el documenta en un **dossier tècnic** i el **defensa oralment**. Programació oficial: [`Programació didàctica/18_SA9_Repte_final_integrador.md`](../../Programació%20didàctica/18_SA9_Repte_final_integrador.md).

> 🎛️ **Treball individual.** Com a tot el curs, el repte, el codi i el dossier de cada alumne són **sempre individuals**: no hi ha equips ni rols repartits. Cadascú tria el seu propi repte lliure d'entre el [banc de reptes proposats](SA9_reptes_proposats.md) (o en proposa un altre de coherent, validat pel docent).

## 📦 Què has d'entregar

| Quan | Lliurable | On es lliura |
|---|---|---|
| S1 | Repte triat + esbós i requisits mínims ([Activitat 1](SA9_fitxa_alumnat.md#1--idear-sessió-1)) | Es mostra al docent / quadern tècnic |
| S2 | Prototip mínim viable, amb almenys un element nou integrat ([Activitat 2](SA9_fitxa_alumnat.md#2--prototipar-sessió-2)) | Es mostra al docent / quadern tècnic |
| S3 | Proves documentades + 1a iteració de millora ([Activitat 3](SA9_fitxa_alumnat.md#3--provar-i-millorar-sessió-3)); qui ja té el prototip llest pot fer la defensa esglaonada | Es mostra al docent / quadern tècnic |
| S4 | **Dossier tècnic tancat** + **defensa oral individual** + demostració ([Activitat 4](SA9_fitxa_alumnat.md#4--comunicar-sessió-4), producte de la SA) | El docent el valida a l'aula |
| S5 | **Prova pràctica T3** (individual, per estacions rotatives; independent del projecte) | El docent la valida a l'aula |
| ⭐ | [Banc de reptes proposats](SA9_reptes_proposats.md) — tria'n un a la S1 | El docent el valida |
| 📓 | Full del quadern tècnic de cada sessió | En acabar cada sessió |
| 🤖 | Rover ampliat amb el repte lliure, funcional | Es mostra al docent a la S4 |

## Itinerari per sessions

> La teva feina és a la **[fitxa base](SA9_fitxa_alumnat.md)**. Aquesta ruta et diu què toca fer a cada sessió.

1. **Sessió 1 · Idear** — tria el teu repte lliure al [banc de reptes](SA9_reptes_proposats.md), defineix els requisits mínims i esbossa la solució. Fes l'[Activitat 1](SA9_fitxa_alumnat.md#1--idear-sessió-1).
2. **Sessió 2 · Prototipar** — munta i programa un primer prototip mínim viable a partir de la [plantilla de projecte](codi/plantilla_projecte/) i del codi de SA1-SA8. Fes l'[Activitat 2](SA9_fitxa_alumnat.md#2--prototipar-sessió-2).
3. **Sessió 3 · Provar i millorar** — depura, itera i avança el [dossier tècnic](SA9_dossier_plantilla.md). Fes l'[Activitat 3](SA9_fitxa_alumnat.md#3--provar-i-millorar-sessió-3).
4. **Sessió 4 · Comunicar** — tanca el dossier i fes la [defensa oral individual](../00_General/00_Guia_defensa_oral.md). Fes l'[Activitat 4](SA9_fitxa_alumnat.md#4--comunicar-sessió-4).
5. **Sessió 5 · Prova pràctica T3** — individual, per estacions rotatives; **no** és sessió de projecte (vegeu §Producte i avaluació).
6. **Abans d'entregar** — repassa [el meu checklist](SA9_checklist_alumnat.md).

Si un dia no tens el rover o els kits a mà, treballa la **lògica** (protocol, llindars, FSM) al simulador de [python.microbit.org](https://python.microbit.org): la ràdio i el mòdul `log` sí es simulen, però **cap** sensor ni els motors s'hi simulen (com a SA7-SA8).

### Si vols més

- [Fitxa ampliada](SA9_fitxa_ampliada.md) — pensament computacional, ODS i ampliacions.
- [Qüestionari de conceptes](SA9_questionari_conceptes.md) — per repassar (gestió de projecte, integració, ètica/ODS).
- [Exemple resolt](SA9_exemple_resolt.md) — com es pensa i es documenta un mini-projecte anàleg.
- [Plantilla del dossier tècnic](SA9_dossier_plantilla.md) — l'esquelet exacte que has d'omplir.

## Producte i avaluació

- **Producte:** **rover ampliat amb el repte lliure**, funcional, + **dossier tècnic** individual (anàlisi, esquemes, codi comentat, proves, millores, conclusions, reflexió ètica/ODS) + **defensa oral individual**. **Es tanca a la S4.**
- **Rúbriques:** **R1, R2, R3, R4 (nivell alt), R5** — totes.
- La **S5** és la **prova pràctica T3**, individual, per estacions rotatives: un instrument **separat** que avalua destreses de SA7-SA8, **no** reavalua el projecte (cap evidència compta dues vegades). Enunciat: [`Avaluació/Prova_practica_T3.md`](../../Avaluació/Prova_practica_T3.md).
- Escala de nota, rúbriques i tot el sistema: [`Com s'avalua la matèria`](../00_General/00_Avaluacio_per_alumnat.md).

<!-- web:only-github -->
## Tots els documents

| Fitxer | Descripció |
|---|---|
| [`SA9_guia_docent.md`](SA9_guia_docent.md) | Guia del professorat: les 5 sessions, defenses esglaonades, organització de la S5 per estacions, punts clau, errors freqüents i avaluació. |
| [`SA9_fitxa_alumnat.md`](SA9_fitxa_alumnat.md) | **Fitxa base** (nucli, per a tot l'alumnat): Activitats 1-4 (Idear/Prototipar/Provar i millorar/Comunicar) + producte + quadern. |
| [`SA9_fitxa_ampliada.md`](SA9_fitxa_ampliada.md) | **Versió ampliada** (aprofundiment): pensament computacional, diana, ODS i ampliacions. |
| [`SA9_checklist_docent.md`](SA9_checklist_docent.md) | **Checklist docent** (una cara): logística prèvia, punts de control per sessió, avaluació. |
| [`SA9_checklist_alumnat.md`](SA9_checklist_alumnat.md) | **Checklist alumnat** (una cara): què he de fer/lliurar + autoavaluació amb semàfor. |
| [`SA9_questionari_conceptes.md`](SA9_questionari_conceptes.md) | Qüestionari de conceptes (mètode de projecte, integració, documentació, ètica/ODS): repàs formatiu o prova curta qualificable (10 preguntes). |
| [`SA9_exemple_resolt.md`](SA9_exemple_resolt.md) | Model «jo ho faig»: com es pensa i es documenta un mini-projecte anàleg abans de fer el propi. |
| [`SA9_dossier_plantilla.md`](SA9_dossier_plantilla.md) | Plantilla del dossier tècnic que lliura l'alumnat (objectiu, disseny, esquema, codi comentat, proves, dificultats, millores). |
| [`SA9_reptes_proposats.md`](SA9_reptes_proposats.md) | Banc de 6 reptes lliures individuals (reg/domòtica, missatger, sentinella i 3 més), amb maquinari de `09c`. |
| `codi/` | Plantilla de projecte MicroPython (vegeu la taula següent). |

### Codi (`codi/`)

| Programa | Nivell | Què mostra |
|---|---|---|
| [`plantilla_projecte/plantilla_projecte.py`](codi/plantilla_projecte/plantilla_projecte.py) | Base | Esquelet executable de la FSM del curs (percep/decideix/actua) amb seccions TODO per integrar-hi el repte propi. |

Cada programa té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs) a l'`EXPLICACIO.md` de la seva carpeta.
<!-- /web:only-github -->
