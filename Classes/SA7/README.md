# SA7 · Robòtica mòbil: el rover

**Durada:** 8 h (4 sessions) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 2 (motoreductors, rodes, seguidor de línia KS0050, sensor d'ultrasons HC-SR04); rover T3 (vehicle T2 ampliat, muntat a la Sessió 0 prèvia)

Setena situació d'aprenentatge del curs (3r trimestre, la primera): el vehicle teledirigit (T2) esdevé un **rover autònom** (T3) — el mateix xassís i motoreductors, amb dos sensors propis nous (seguidor de línia i ultrasons) que li permeten decidir **sol**, sense comandament. Programació oficial: [`Programació didàctica/16_SA7_Robotica_mobil_el_rover.md`](../../Programació%20didàctica/16_SA7_Robotica_mobil_el_rover.md).

> 🎛️ **Treball individual.** El codi i el producte de cada alumne són **sempre individuals**, com a la resta del curs.

> 🔧 **Sessió 0, prèvia (no compta a les 8 h):** el rover es munta abans de començar aquesta SA, sobre el vehicle T2 ja fet. Detall complet: [`00_Projecte_T3_Rover.md`](../00_General/00_Projecte_T3_Rover.md) i la secció «SESSIÓ 0» de la [guia docent](SA7_guia_docent.md).

## 📦 Què has d'entregar

| Quan | Lliurable | On es lliura |
|---|---|---|
| S1 | `calibratge_motors.py` provat i calibrat ([Activitat 1](SA7_fitxa_alumnat.md#1--cinemàtica-diferencial-sessió-1)) | Es mostra al docent / quadern tècnic |
| S2 | Mini-check individual (no qualifica) i `segueix_linia.py` calibrat ([Activitat 2](SA7_fitxa_alumnat.md#2--seguidor-de-línia-sessió-2)) | Es mostra al docent / quadern tècnic |
| S3 | Repte **«tria un comportament autònom»** amb `evita_obstacles.py` i/o `segueix_linia.py` ([Activitat 3](SA7_fitxa_alumnat.md#3--evita-obstacles-i-tria-un-comportament-autònom-sessió-3)) | El docent el valida a l'aula |
| S4 | **Comportament autònom del rover** ([Activitat 4](SA7_fitxa_alumnat.md#4--integració-missions-del-rover-sessió-4--producte), producte de la SA) + mini-defensa breu | El docent el valida a l'aula |
| ⭐ | [Repte triat](../../Reptes/Reptes_SA7.md) | El docent el valida |
| 📓 | Full del quadern tècnic de cada sessió | En acabar cada sessió |
| 🤖 | Rover T3 amb comportament autònom (seguidor de línia i/o evita-obstacles) | Es mostra al docent a la S4 |

## Itinerari per sessions

> La teva feina és a la **[fitxa base](SA7_fitxa_alumnat.md)**. Aquesta ruta et diu què toca fer a cada sessió.

0. **Sessió 0 (prèvia, no compta a les 8 h) · Muntatge del rover** — recupera el teu vehicle T2 i munta-hi les dues peces d'ampliació (suport HC-SR04, suport seguidor de línia). Checklist de muntatge (R2, formativa).
1. **Sessió 1 · Cinemàtica diferencial** — revisió del rover muntat, calibra [`calibratge_motors.py`](codi/calibratge_motors/) i prova una trajectòria en quadrat. Fes l'[Activitat 1](SA7_fitxa_alumnat.md#1--cinemàtica-diferencial-sessió-1).
2. **Sessió 2 · Seguidor de línia** — calibra el llindar de [`segueix_linia.py`](codi/segueix_linia/) sobre el teu circuit. Mini-check individual a l'inici (no qualifica). Fes l'[Activitat 2](SA7_fitxa_alumnat.md#2--seguidor-de-línia-sessió-2).
3. **Sessió 3 · Evita-obstacles** — programa [`evita_obstacles.py`](codi/evita_obstacles/) i tria el teu comportament autònom. Fes l'[Activitat 3](SA7_fitxa_alumnat.md#3--evita-obstacles-i-tria-un-comportament-autònom-sessió-3).
4. **Sessió 4 · Missions del rover** — a partir de [`rover_missions.py`](codi/rover_missions/), fes l'[Activitat 4](SA7_fitxa_alumnat.md#4--integració-missions-del-rover-sessió-4--producte) (producte de la SA).
5. **Abans d'entregar** — repassa [el meu checklist](SA7_checklist_alumnat.md).

Si un dia no tens el rover muntat a mà, pots treballar la **lògica** al simulador de [python.microbit.org](https://python.microbit.org), però **cap** component del rover (motors, HC-SR04, seguidor de línia) s'hi simula (vegeu [`SA7_esquemes_connexions.md`](SA7_esquemes_connexions.md) §Simulació): és una via per esbossar pseudocodi, no per validar el comportament.

### Si vols més

- [Fitxa ampliada](SA7_fitxa_ampliada.md) — pensament computacional, ODS i ampliacions.
- [Qüestionari de conceptes](SA7_questionari_conceptes.md) — per repassar.
- [Exemple resolt](SA7_exemple_resolt.md) — com es pensa un problema semblant.
- [Reptes de la SA7](../../Reptes/Reptes_SA7.md) — quan tinguis el nucli al dia.

## Producte i avaluació

- **Producte:** **comportament autònom del rover** (seguidor de línia i/o evita-obstacles), integrat en una estructura de missions, codi organitzat en funcions i documentació de les proves i millores al quadern tècnic, tancat i avaluat a la **S4**.
- **Rúbriques:** **R1** (codi, funcionament), **R3** (criteri "Autonomia/control") i **R4** (documentació i defensa).
- Escala de nota, rúbriques i tot el sistema: [`Com s'avalua la matèria`](../00_General/00_Avaluacio_per_alumnat.md).

<!-- web:only-github -->
## Tots els documents

| Fitxer | Descripció |
|---|---|
| [`SA7_guia_docent.md`](SA7_guia_docent.md) | Guia del professorat: Sessió 0 (muntatge) + les 4 sessions, punts clau, errors freqüents i avaluació. |
| [`SA7_fitxa_alumnat.md`](SA7_fitxa_alumnat.md) | **Fitxa base** (nucli, per a tot l'alumnat): Activitats 1-4 + producte + quadern. |
| [`SA7_fitxa_ampliada.md`](SA7_fitxa_ampliada.md) | **Versió ampliada** (aprofundiment): pensament computacional, diana, ODS i ampliacions. |
| [`SA7_checklist_docent.md`](SA7_checklist_docent.md) | **Checklist docent** (una cara): logística prèvia, punts de control per sessió, avaluació. |
| [`SA7_checklist_alumnat.md`](SA7_checklist_alumnat.md) | **Checklist alumnat** (una cara): què he de fer/lliurar + autoavaluació amb semàfor. |
| [`SA7_questionari_conceptes.md`](SA7_questionari_conceptes.md) | Qüestionari de conceptes (cinemàtica diferencial, llindar, time-of-flight, missions): repàs formatiu o prova curta qualificable (10 preguntes). |
| [`SA7_exemple_resolt.md`](SA7_exemple_resolt.md) | Model «jo ho faig»: com es raona un problema anàleg abans de fer el propi. |
| [`SA7_esquemes_connexions.md`](SA7_esquemes_connexions.md) | Pins del rover: M1/M2 heretats + HC-SR04 + seguidor de línia. |
| `codi/` | Programes MicroPython (vegeu la taula següent). |

### Codi (`codi/`)

| Programa | Nivell | Què mostra |
|---|---|---|
| [`calibratge_motors/calibratge_motors.py`](codi/calibratge_motors/calibratge_motors.py) | Base | Cinemàtica diferencial i calibratge de motors (compensació M1/M2), sobre les funcions de moviment de la SA4. |
| [`segueix_linia/segueix_linia.py`](codi/segueix_linia/segueix_linia.py) | Base | Seguidor de línia amb el KS0050 (`read_analog`, llindar calibrat) i correcció de rumb. |
| [`evita_obstacles/evita_obstacles.py`](codi/evita_obstacles/evita_obstacles.py) | Base | Evita-obstacles amb l'HC-SR04 (`machine.time_pulse_us`, mateix patró que la SA3, pins nous). |
| [`rover_missions/rover_missions.py`](codi/rover_missions/rover_missions.py) | Repte / **producte de la SA** | Integració de tots els comportaments en missions seleccionables, amb polsador STOP prioritari. |

Cada programa té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs) a l'`EXPLICACIO.md` de la seva carpeta.
<!-- /web:only-github -->
