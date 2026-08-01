# SA3 · Entrades: el robot percep

**Durada:** 8 h (4 sessions; S4 = Prova pràctica T1) · **Maquinari:** micro:bit V2 + Micro:shield (botons A/B, sensor de llum, sensor de temperatura, acceleròmetre, micròfon integrats); Kit Keyestudio 1 (polsador, potenciòmetre, sensor de temperatura bàsic), Kit 2 (sensor de llum, sensor de temperatura, ultrasons HC-SR04, PIR) i Kit 3 (sensor de so); mascota muntada a SA2

Tercera situació d'aprenentatge del curs (1r trimestre). La micro:bit comença a **percebre**: botons, polsador, potenciòmetre, sensors de llum i temperatura (interns i externs), ultrasons i PIR, tots interpretats amb **condicionals** (`if/elif/else`). La sessió 3 és el producte que **tanca la mascota T1**: la mascota reacciona a l'entorn amb almenys 2 comportaments sensor→resposta. La sessió 4 és **sencera** la prova pràctica individual del 1r trimestre. Programació oficial: [`Programació didàctica/12_SA3_Entrades_el_robot_percep.md`](../../Programació%20didàctica/12_SA3_Entrades_el_robot_percep.md).

## 📦 Què has d'entregar

| Quan | Lliurable | On es lliura |
|---|---|---|
| S1 | Comptador de premudes del polsador amb antirebot ([Activitat 1](SA3_fitxa_alumnat.md#1--entrades-digitals-i-condicionals-sessió-1)) | Es mostra al docent / quadern tècnic |
| S2 | `nivell_llum` i `termometre` provats ([Activitat 2](SA3_fitxa_alumnat.md#2--entrades-analògiques-llum-i-temperatura-sessió-2)) i mini-check individual (no qualifica) | Es mostra al docent / quadern tècnic |
| S3 | 🤖 Repte **«mascota reactiva»** ([Activitat 3](SA3_fitxa_alumnat.md#3--repte-mascota-reactiva-sessió-3--producte-tanca-la-mascota-t1), producte de la SA — **tanca el Projecte T1**) + mini-defensa breu | El docent el valida a l'aula |
| S4 | Prova pràctica T1 (individual) | Es lliura durant la sessió |
| ⭐ | [Repte triat](../../Reptes/Reptes_SA3.md) | El docent el valida |
| 📓 | Full del quadern tècnic de cada sessió | En acabar cada sessió |
| 🤖 | Mascota tancada (≥2 reaccions sensor→comportament, cablatge exacte del dossier) | Es queda a l'aula/casa; ja no torna a obrir-se fins a la SA4 |

## Itinerari per sessions

> La teva feina és a la **[fitxa base](SA3_fitxa_alumnat.md)**. Aquesta ruta et diu què toca fer a cada sessió.

1. **Sessió 1 · Entrades digitals i condicionals** — munta el polsador extern ([esquemes](SA3_esquemes_connexions.md)) i fes l'[Activitat 1](SA3_fitxa_alumnat.md#1--entrades-digitals-i-condicionals-sessió-1) (comptador al REPL, *pull-up* i antirebot).
2. **Sessió 2 · Entrades analògiques: llum i temperatura** — munta el sensor de llum i el de temperatura i fes l'[Activitat 2](SA3_fitxa_alumnat.md#2--entrades-analògiques-llum-i-temperatura-sessió-2) amb [`nivell_llum`](codi/nivell_llum/) i [`termometre`](codi/termometre/). Mini-check individual a l'inici (no qualifica).
3. **Sessió 3 · Repte «mascota reactiva»** — cablega la mascota amb el cablatge exacte del [dossier](../00_General/00_Projecte_T1_Mascota.md), prova [`alarma_ultrasons`](codi/alarma_ultrasons/) i fes l'[Activitat 3](SA3_fitxa_alumnat.md#3--repte-mascota-reactiva-sessió-3--producte-tanca-la-mascota-t1) (a partir de [`mascota_reactiva`](codi/mascota_reactiva/)): **es tanca la mascota T1**.
4. **Sessió 4 · Prova pràctica T1** — sessió sencera, individual: enunciat a [`Avaluació/Prova_practica_T1.md`](../../Avaluació/Prova_practica_T1.md).
5. **Abans d'entregar** — repassa [el meu checklist](SA3_checklist_alumnat.md).

Si un dia no tens el Micro:shield o els kits a mà, la **lògica** dels programes es pot escriure i provar al **simulador de [python.microbit.org](https://python.microbit.org)**, però **no reprodueix** cap sensor extern (només llum/temperatura/so interns, acceleròmetre i botons; vegeu [`SA3_esquemes_connexions.md`](SA3_esquemes_connexions.md) §Simulació): cal validar-los amb maquinari real quan en tinguis.

### Si vols més

- [Fitxa ampliada](SA3_fitxa_ampliada.md) — pensament computacional, ODS i ampliacions.
- [Qüestionari de conceptes](SA3_questionari_conceptes.md) — per repassar (també útil abans de la prova pràctica T1).
- [Exemple resolt](SA3_exemple_resolt.md) — com es pensa un problema semblant.
- [Reptes de la SA3](../../Reptes/Reptes_SA3.md) — quan tinguis el nucli al dia.

## Producte i avaluació

- **Producte:** repte **«mascota reactiva»** (≥2 reaccions sensor→comportament, coherents amb la personalitat triada), tancat i avaluat a la **S3** — **tanca el Projecte T1**. La **S4** és la prova pràctica T1 individual.
- **Rúbriques:** **R1** (codi), **R2** (muntatge), **R3** (compliment del repte) i **R4** (documentació i mini-defensa oral). El mini-check (S2) **no** qualifica.
- Escala de nota, rúbriques i tot el sistema: [`Com s'avalua la matèria`](../00_General/00_Avaluacio_per_alumnat.md).

<!-- web:only-github -->
## Tots els documents

| Fitxer | Descripció |
|---|---|
| [`SA3_guia_docent.md`](SA3_guia_docent.md) | Guia del professorat: objectius, seqüència de les 4 sessions, punts clau, errors freqüents i avaluació. |
| [`SA3_fitxa_alumnat.md`](SA3_fitxa_alumnat.md) | **Fitxa base** (nucli, per a tot l'alumnat): Activitats 1-3 + producte + quadern. |
| [`SA3_fitxa_ampliada.md`](SA3_fitxa_ampliada.md) | **Versió ampliada** (aprofundiment): pensament computacional, diana, ODS i ampliacions. |
| [`SA3_checklist_docent.md`](SA3_checklist_docent.md) | **Checklist docent** (una cara): logística prèvia, punts de control per sessió, avaluació. |
| [`SA3_checklist_alumnat.md`](SA3_checklist_alumnat.md) | **Checklist alumnat** (una cara): què he de fer/lliurar + autoavaluació amb semàfor. |
| [`SA3_questionari_conceptes.md`](SA3_questionari_conceptes.md) | Qüestionari de conceptes (entrades digitals/analògiques, `read_analog()`, mapatge, HC-SR04, PIR): repàs formatiu o prova curta qualificable (10 preguntes). |
| [`SA3_exemple_resolt.md`](SA3_exemple_resolt.md) | Model «jo ho faig»: com es raona un problema anàleg abans de fer el propi. |
| [`SA3_esquemes_connexions.md`](SA3_esquemes_connexions.md) | Taules de connexió pin a pin al Micro:shield (entrades digitals/analògiques, ultrasons) i pins EXACTES de la mascota. |
| `codi/` | Programes MicroPython (vegeu la taula següent). |

### Codi (`codi/`)

| Programa | Nivell | Què mostra |
|---|---|---|
| [`nivell_llum/nivell_llum.py`](codi/nivell_llum/nivell_llum.py) | Base | Entrada analògica (`read_analog`): sensor de llum intern vs extern, mapades a barres al display. |
| [`termometre/termometre.py`](codi/termometre/termometre.py) | Base | Entrada analògica: sensor de temperatura intern vs extern, interpretada amb `if/elif/else`. |
| [`alarma_ultrasons/alarma_ultrasons.py`](codi/alarma_ultrasons/alarma_ultrasons.py) | Base | HC-SR04: mesura per temps de vol (`machine.time_pulse_us`) i alarma sonora per proximitat. |
| [`mascota_reactiva/mascota_reactiva.py`](codi/mascota_reactiva/mascota_reactiva.py) | Repte / **producte de la SA** (tanca T1) | Integra so, llum, PIR, polsador i acceleròmetre en reaccions de la mascota (cara + so), amb el cablatge exacte del dossier. |

Cada programa té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs) a l'`EXPLICACIO.md` de la seva carpeta.
<!-- /web:only-github -->
