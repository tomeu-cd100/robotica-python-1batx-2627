# Classes — guia general d'aula

> **Per a qui és?** Docent (per organitzar el curs) i alumnat (per saber on trobar cada cosa). És el mapa de tot el material d'aula: com s'organitza cada SA, l'índex de les 9 situacions d'aprenentatge i l'índex del material transversal (aquesta carpeta, `00_General/`).

## Com s'organitza cada SA

Cada subcarpeta `Classes/SAx/` conté (contracte verificat per `tools/qa.py:comprova_cobertura_sa()`):

- **`SAx_guia_docent.md`** — desenvolupament sessió a sessió per al professorat: objectius, activitats, temps i errors freqüents.
- **`SAx_fitxa_alumnat.md`** — **fitxa base**: el nucli que fa tot l'alumnat (activitats, repte, producte, quadern).
- **`SAx_fitxa_ampliada.md`** — **versió d'aprofundiment** per a qui vulgui/pugui anar més enllà.
- **`SAx_checklist_docent.md`** i **`SAx_checklist_alumnat.md`** — recordatori d'una cara per a cada públic.
- **`SAx_questionari_conceptes.md`** — qüestionari autocorrectiu de repàs dels conceptes clau.
- **`SAx_exemple_resolt.md`** — un exemple complet i comentat del nivell esperat.
- **`SAx_esquemes_connexions.md`** (SA1–SA8) — taula de connexions pin a pin micro:bit/Micro:shield ↔ sensor/actuador.
- **`codi/*.py`** — programes MicroPython comentats, oberts directament a l'editor de micro:bit (python.microbit.org) o a Thonny.

> Tot el codi del curs és **MicroPython** (`.py`) per a la **micro:bit V2 + Micro:shield**: no hi ha cap `.ino` ni cap compilació Arduino en aquest curs (a diferència del curs germà d'Arduino + C++). Vegeu com preparar l'entorn a [`00_Entorns_de_treball.md`](00_Entorns_de_treball.md).

## Les 9 SA (índex)

Vista d'un cop d'ull. **El detall de cada SA** (materials, sessions i codi) és a la seva carpeta. La **planificació completa** (hores, sabers, criteris d'avaluació, pla de contingència) és a `Programació didàctica/`.

| SA | Tema | Durada | Fitxes |
|---|---|---|---|
| **SA0** | Vocabulari essencial i bases de programació *(preàmbul, transversal)* | — | [obre →](../SA0/README.md) |
| **SA1** | Hola, robot! Sistemes embeguts i mètode de projecte | 6 h | [obre →](../SA1/README.md) |
| **SA2** | Sortides: el robot actua | 8 h | [obre →](../SA2/README.md) |
| **SA3** | Entrades: el robot percep *(S4 = Prova T1)* | 8 h | [obre →](../SA3/README.md) |
| **SA4** | Funcions i moviment | 8 h | [obre →](../SA4/README.md) |
| **SA5** | Ràdio: robots que parlen | 6 h | [obre →](../SA5/README.md) |
| **SA6** | Control: el robot decideix *(S4 = Prova T2)* | 8 h | [obre →](../SA6/README.md) |
| **SA7** | Robòtica mòbil: el rover | 8 h | [obre →](../SA7/README.md) |
| **SA8** | Autonomia i telemetria | 6 h | [obre →](../SA8/README.md) |
| **SA9** | Repte final integrador *(S5 = Prova T3)* | 10 h | [obre →](../SA9/README.md) |

> 🗺️ Calendari, hores i pla de contingència complets: [`Programació didàctica/08_Sequenciacio_temporal_anual.md`](../../Programació%20didàctica/08_Sequenciacio_temporal_anual.md).

## El fil conductor: tres construccions individuals

Tot el curs és **individual**: cadascú té el seu propi micro:bit V2 + Micro:shield + kits Keyestudio i fabrica, munta i programa **el seu propi** exemplar de cada robot del fil conductor:

1. 🐣 **Mascota reactiva** (T1, SA2–SA3) — [`00_Projecte_T1_Mascota.md`](00_Projecte_T1_Mascota.md).
2. 🚗 **Vehicle teledirigit** (T2, SA4–SA6) — [`00_Projecte_T2_Vehicle.md`](00_Projecte_T2_Vehicle.md).
3. 🚙 **Rover autònom** (T3, SA7–SA9) — [`00_Projecte_T3_Rover.md`](00_Projecte_T3_Rover.md).

El calendari de fabricació (cua de la talladora làser i de la impressora 3D per a 15-20 alumnes, per lots, i el pla B de peces pretallades) és a [`00_Fil_conductor_construccions.md`](00_Fil_conductor_construccions.md).

## Material transversal (aquesta carpeta)

| Document | Per a qui | Què hi trobaràs |
|---|---|---|
| [`00_Entorns_de_treball.md`](00_Entorns_de_treball.md) | Docent i alumnat | Editor python.microbit.org, simulador, Thonny, com transferir `.py`/`.hex` a la placa. |
| [`00_Fil_conductor_construccions.md`](00_Fil_conductor_construccions.md) | Docent | Els tres robots individuals, calendari de fabricació, nesting i pretallat. |
| [`00_Projecte_T1_Mascota.md`](00_Projecte_T1_Mascota.md) · [`00_Projecte_T2_Vehicle.md`](00_Projecte_T2_Vehicle.md) · [`00_Projecte_T3_Rover.md`](00_Projecte_T3_Rover.md) | Alumnat | Dossier complet de cada robot: peces, muntatge, cablatge, codi mínim i rúbrica. |
| [`00_Glossari_tecnic.md`](00_Glossari_tecnic.md) | Alumnat | Vocabulari català ↔ anglès per llegir documentació real. |
| [`00_Mini_checks_individuals.md`](00_Mini_checks_individuals.md) | Docent | El micro-repte individual de 10' de cada SA (radar formatiu, no qualifica). |
| [`pdf/00_Quadern_sessions_docent.pdf`](pdf/00_Quadern_sessions_docent.pdf) | Docent | Full imprimible d'una pàgina per sessió (kata + mini-check + repte ⭐ + checklist docent), generat de tots els documents anteriors. |
| [`00_Guia_defensa_oral.md`](00_Guia_defensa_oral.md) | Docent i alumnat | Escala de progressió de les defenses orals del curs (R4·DO). |
| [`00_Quadern_tecnic.md`](00_Quadern_tecnic.md) | Alumnat | El diari de treball individual: què hi va, com es porta, com es lliura. |
| [`00_Avaluacio_per_alumnat.md`](00_Avaluacio_per_alumnat.md) | Alumnat | D'on surt la nota, en llenguatge d'alumne. |
| [`00_Mode_supervivencia.md`](00_Mode_supervivencia.md) | Docent (primer any) | Què fer si falla el maquinari; les rutines no negociables i l'ordre d'adopció de la resta. |
| [`00_Targetes_rescat.md`](00_Targetes_rescat.md) | Alumnat | Targetes d'autoajuda quan t'encalles: 3 nivells de pista per SA, abans de cridar el docent. |
| [`00_Vaig_faltar.md`](00_Vaig_faltar.md) | Alumnat | Itinerari en 5 passos per posar-se al dia sol després de faltar a una sessió. |
| [`00_Repas_expres_MicroPython.md`](00_Repas_expres_MicroPython.md) | Alumnat | Targeta d'autoestudi «Python flash»: deures de repàs abans de la prova pràctica T3. |
| [`00_Repas_expres_Radio.md`](00_Repas_expres_Radio.md) | Alumnat | Targeta d'autoestudi de ràdio: deures de repàs abans de la prova pràctica T3. |
| [`00_IA_a_la_materia.md`](00_IA_a_la_materia.md) | Docent | Com s'introdueix la IA al curs i com gestionar assistents d'IA amb integritat acadèmica. |

## Notes

- Comentaris de codi en català **sense accents** (evita problemes de codificació).
- Assignació de pins **consistent** entre SA, documentada als esquemes de cada SA i fixada de manera definitiva a la Sessió 0 de muntatge del vehicle (SA4) i del rover (SA7).
- Vincle amb la programació didàctica: `Programació didàctica/10_SA1...` fins a `18_SA9...`.
- **Ràdio i treball individual:** l'emparellament de plaques per provar la ràdio (SA5, SA8) és **puntual, només de banc de proves**; el codi i el producte avaluats són sempre els de cada alumne (vegeu `Programació didàctica/14_SA5_Radio_robots_que_parlen.md` i `17_SA8_Autonomia_i_telemetria.md`).

---

⬅️ Torna a [`Classes/README.md`](../README.md).
