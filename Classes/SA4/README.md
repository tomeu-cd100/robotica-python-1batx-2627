# SA4 · Funcions i moviment

**Durada:** 8 h (4 sessions; S4 = fabricació del vehicle T2) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 2 (micro servo, 2 motoreductors + rodes); fabricació del vehicle (peces pretallades pel docent)

Quarta situació d'aprenentatge del curs (2n trimestre, primera de tres). La micro:bit comença a **moure's**: avui poses nom formal al concepte de **funció** (paràmetres, valor de retorn, modularitat) i el fas servir per controlar un servomotor i dos motoreductors del vehicle. La sessió 3 és el producte que activa el moviment amb els botons A/B; la sessió 4 és la **fabricació física** del vehicle T2. Programació oficial: [`Programació didàctica/13_SA4_Funcions_i_moviment.md`](../../Programació%20didàctica/13_SA4_Funcions_i_moviment.md).

## 📦 Què has d'entregar

| Quan | Lliurable | On es lliura |
|---|---|---|
| S1 | `funcions_moviments.py` provat ([Activitat 1](SA4_fitxa_alumnat.md#1--funcions-amb-parametres-i-valor-de-retorn-sessió-1)) | Es mostra al docent / quadern tècnic |
| S2 | `velocitat_pwm.py` provat ([Activitat 2](SA4_fitxa_alumnat.md#2--funcions-de-moviment-del-motoreductor-sessió-2)) i mini-check individual (no qualifica) | Es mostra al docent / quadern tècnic |
| S3 | 🤖 Repte **«control per botons»** ([Activitat 3](SA4_fitxa_alumnat.md#3--repte-control-per-botons-sessió-3--producte), producte de la SA) + mini-defensa breu | El docent el valida a l'aula |
| S4 | Vehicle T2 muntat i prova d'encesa feta | Es mostra al docent |
| ⭐ | [Repte ⭐ de Reptes_SA4.md](../../Reptes/Reptes_SA4.md) (nucli obligatori) | El docent el valida → compta R1 |
| 📓 | Full del quadern tècnic de cada sessió | En acabar cada sessió |
| 🤖 | Vehicle T2 muntat (xassís, motors i roda boja fixats, cablatge exacte, prova de moviment feta) | Es porta a la SA5 per treballar-hi la ràdio |

## Itinerari per sessions

> La teva feina és a la **[fitxa base](SA4_fitxa_alumnat.md)**. Aquesta ruta et diu què toca fer a cada sessió.

1. **Sessió 1 · Funcions amb paràmetres i valor de retorn** — programa el servo de la mascota (P0, [esquemes](SA4_esquemes_connexions.md)) amb [`funcions_moviments.py`](codi/funcions_moviments/) i fes l'[Activitat 1](SA4_fitxa_alumnat.md#1--funcions-amb-parametres-i-valor-de-retorn-sessió-1).
2. **Sessió 2 · Motoreductor amb funcions de moviment** — munta els dos motoreductors i fes l'[Activitat 2](SA4_fitxa_alumnat.md#2--funcions-de-moviment-del-motoreductor-sessió-2) amb [`velocitat_pwm.py`](codi/velocitat_pwm/). Mini-check individual a l'inici (no qualifica).
3. **Sessió 3 · Repte «control per botons»** — a partir de [`control_per_botons.py`](codi/control_per_botons/), fes l'[Activitat 3](SA4_fitxa_alumnat.md#3--repte-control-per-botons-sessió-3--producte) (producte de la SA).
4. **Sessió 4 · Muntatge del vehicle T2** — fabricació física segons el [dossier del vehicle](../00_General/00_Projecte_T2_Vehicle.md).
5. **Abans d'entregar** — repassa [el meu checklist](SA4_checklist_alumnat.md).

Si un dia no tens el Micro:shield o els kits a mà, la **lògica** dels programes es pot escriure i provar al **simulador de [python.microbit.org](https://python.microbit.org)**, però **no reprodueix** ni el servo ni els motoreductors (vegeu [`SA4_esquemes_connexions.md`](SA4_esquemes_connexions.md) §Simulació): cal validar-los amb maquinari real quan en tinguis.

### Si vols més

- [Fitxa ampliada](SA4_fitxa_ampliada.md) — pensament computacional, ODS i ampliacions.
- [Qüestionari de conceptes](SA4_questionari_conceptes.md) — per repassar.
- [Exemple resolt](SA4_exemple_resolt.md) — com es pensa un problema semblant.
- [Reptes ⭐⭐/⭐⭐⭐ de la SA4](../../Reptes/Reptes_SA4.md) — ampliació opcional, per a qui va sobrat de temps (el ⭐ ja és nucli obligatori, vegeu «Què has d'entregar»).

## Producte i avaluació

- **Producte:** repte **«control per botons»** (moviment del vehicle amb funcions pròpies avançar/retrocedir/girar/aturar, activat per botons A/B), tancat i avaluat a la **S3**. Muntatge físic del **vehicle** a la **S4** (fabricació, avaluada amb la rúbrica de muntatge).
- **Rúbriques:** **R1** (codi, criteri "Estructura"/modularitat), **R2** (muntatge del vehicle) i **R4** (documentació i defensa, R4·DO).
- Escala de nota, rúbriques i tot el sistema: [`Com s'avalua la matèria`](../00_General/00_Avaluacio_per_alumnat.md).

<!-- web:only-github -->
## Tots els documents

| Fitxer | Descripció |
|---|---|
| [`SA4_guia_docent.md`](SA4_guia_docent.md) | Guia del professorat: objectius, seqüència de les 4 sessions, punts clau, errors freqüents i avaluació. |
| [`SA4_fitxa_alumnat.md`](SA4_fitxa_alumnat.md) | **Fitxa base** (nucli, per a tot l'alumnat): Activitats 1-3 + producte + quadern. |
| [`SA4_fitxa_ampliada.md`](SA4_fitxa_ampliada.md) | **Versió ampliada** (aprofundiment): pensament computacional, diana, ODS i ampliacions. |
| [`SA4_checklist_docent.md`](SA4_checklist_docent.md) | **Checklist docent** (una cara): logística prèvia, punts de control per sessió, avaluació. |
| [`SA4_checklist_alumnat.md`](SA4_checklist_alumnat.md) | **Checklist alumnat** (una cara): què he de fer/lliurar + autoavaluació amb semàfor. |
| [`SA4_questionari_conceptes.md`](SA4_questionari_conceptes.md) | Qüestionari de conceptes (funcions, paràmetres, valor de retorn, servo, PWM del motor): repàs formatiu o prova curta qualificable (10 preguntes). |
| [`SA4_exemple_resolt.md`](SA4_exemple_resolt.md) | Model «jo ho faig»: com es raona un problema anàleg abans de fer el propi. |
| [`SA4_esquemes_connexions.md`](SA4_esquemes_connexions.md) | Taules de connexió del servo i dels motoreductors (pins definitius de tot el curs). |
| `codi/` | Programes MicroPython (vegeu la taula següent). |

### Codi (`codi/`)

| Programa | Nivell | Què mostra |
|---|---|---|
| [`funcions_moviments/funcions_moviments.py`](codi/funcions_moviments/funcions_moviments.py) | Base | Primeres funcions `def` del curs: paràmetres i valor de retorn, servo de la mascota. |
| [`coreografia/coreografia.py`](codi/coreografia/coreografia.py) | Base | Funcions amb arguments combinades: servo + so + display. |
| [`velocitat_pwm/velocitat_pwm.py`](codi/velocitat_pwm/velocitat_pwm.py) | Base | Funcions de moviment del motoreductor: sentit i velocitat amb PWM. |
| [`control_per_botons/control_per_botons.py`](codi/control_per_botons/control_per_botons.py) | Repte / **producte de la SA** | Seqüència de moviments encadenada amb les funcions pròpies, activada amb els botons A/B. |

Cada programa té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs) a l'`EXPLICACIO.md` de la seva carpeta.
<!-- /web:only-github -->
