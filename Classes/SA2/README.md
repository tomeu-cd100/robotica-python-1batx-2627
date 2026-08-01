# SA2 · Sortides: el robot actua

**Durada:** 8 h (4 sessions) · **Maquinari:** micro:bit V2 + Micro:shield (display 5×5, botons A/B, altaveu i sensors interns); Kit Keyestudio 1 (LED, LED RGB, brunzidor) i Kit 3 (relé, LED addicionals); fabricació de la **mascota** (peces pretallades pel docent)

Segona situació d'aprenentatge del curs (1r trimestre). La micro:bit s'encaixa al **Micro:shield** i comença a **actuar** sobre components externs: LED, LED RGB, brunzidor i relé, amb sortides **digitals i PWM** controlades amb **variables i bucles**. La sessió 4 és la fabricació i el muntatge físic de la **mascota** del fil conductor. Programació oficial: [`Programació didàctica/11_SA2_Sortides_el_robot_actua.md`](../../Programació%20didàctica/11_SA2_Sortides_el_robot_actua.md).

## 📦 Què has d'entregar

| Quan | Lliurable | On es lliura |
|---|---|---|
| S1 | LED extern parpellejant amb comptador ([Activitat 1](SA2_fitxa_alumnat.md#1--sortida-digital-amb-bucles-sessió-1)) | Es mostra al docent / quadern tècnic |
| S2 | LED RGB i brunzidor provats ([Activitat 2](SA2_fitxa_alumnat.md#2--sortides-pwm-i-so-sessió-2)) i mini-check individual (no qualifica) | Es mostra al docent / quadern tècnic |
| S3 | Repte **«semàfor o llum d'ambient»** ([Activitat 3](SA2_fitxa_alumnat.md#3--repte-semàfor-o-llum-dambient-sessió-3--producte), producte de la SA) + mini-defensa oral (1') | El docent el valida a l'aula |
| S4 | 🤖 Muntatge físic de la **mascota** ([Activitat 4](SA2_fitxa_alumnat.md#4--muntatge-de-la-mascota-sessió-4)) | Es queda a l'aula/casa fins a la SA3 |
| ⭐ | [Repte triat](../../Reptes/Reptes_SA2.md) | El docent el valida |
| 📓 | Full del quadern tècnic de cada sessió | En acabar cada sessió |
| 🤖 | Mascota muntada (LED/RGB i so validats, servo muntat) | Es porta a la SA3 |

## Itinerari per sessions

> La teva feina és a la **[fitxa base](SA2_fitxa_alumnat.md)**. Aquesta ruta et diu què toca fer a cada sessió.

1. **Sessió 1 · Sortides digitals amb bucles** — encaixa el Micro:shield, munta el LED extern a **P1** ([esquemes](SA2_esquemes_connexions.md)) i fes l'[Activitat 1](SA2_fitxa_alumnat.md#1--sortida-digital-amb-bucles-sessió-1) amb [`led_parpelleig`](codi/led_parpelleig/).
2. **Sessió 2 · Sortides PWM i so** — munta el LED RGB i el brunzidor i fes l'[Activitat 2](SA2_fitxa_alumnat.md#2--sortides-pwm-i-so-sessió-2) amb [`pwm_led_rgb`](codi/pwm_led_rgb/) i [`musica_altaveu`](codi/musica_altaveu/). Mini-check individual a l'inici (no qualifica).
3. **Sessió 3 · Repte «semàfor o llum d'ambient»** — munta i programa el **producte de la SA** ([Activitat 3](SA2_fitxa_alumnat.md#3--repte-semàfor-o-llum-dambient-sessió-3--producte), a partir de [`semafor_rele`](codi/semafor_rele/)) i fes la mini-defensa oral.
4. **Sessió 4 · Muntatge de la mascota** — segueix el dossier [`00_Projecte_T1_Mascota.md`](../00_General/00_Projecte_T1_Mascota.md) ([Activitat 4](SA2_fitxa_alumnat.md#4--muntatge-de-la-mascota-sessió-4)).
5. **Abans d'entregar** — repassa [el meu checklist](SA2_checklist_alumnat.md).

Si un dia no tens el Micro:shield o els kits a mà, la **lògica** dels programes es pot escriure i provar al **simulador de [python.microbit.org](https://python.microbit.org)**, però **no reprodueix** el LED extern, el LED RGB, el brunzidor ni el relé (vegeu [`SA2_esquemes_connexions.md`](SA2_esquemes_connexions.md) §Simulació): cal validar-los amb maquinari real quan en tinguis.

### Si vols més

- [Fitxa ampliada](SA2_fitxa_ampliada.md) — pensament computacional, ODS i ampliacions.
- [Qüestionari de conceptes](SA2_questionari_conceptes.md) — per repassar.
- [Exemple resolt](SA2_exemple_resolt.md) — com es pensa un problema semblant.
- [Reptes de la SA2](../../Reptes/Reptes_SA2.md) — quan tinguis el nucli al dia.

## Producte i avaluació

- **Producte:** repte **«semàfor o llum d'ambient»** (LED/RGB/brunzidor/relé amb bucles i PWM), tancat i avaluat a la **S3**. Muntatge físic de la **mascota** del fil conductor a la **S4**.
- **Rúbriques:** **R1** (codi), **R2** (muntatge; a la S3 el circuit del repte, a la S4 el criteri "Muntatge" de la mascota) i **R4** (documentació i mini-defensa oral). El mini-check (S2) **no** qualifica.
- Escala de nota, rúbriques i tot el sistema: [`Com s'avalua la matèria`](../00_General/00_Avaluacio_per_alumnat.md).

<!-- web:only-github -->
## Tots els documents

| Fitxer | Descripció |
|---|---|
| [`SA2_guia_docent.md`](SA2_guia_docent.md) | Guia del professorat: objectius, seqüència de les 4 sessions, punts clau, errors freqüents i avaluació. |
| [`SA2_fitxa_alumnat.md`](SA2_fitxa_alumnat.md) | **Fitxa base** (nucli, per a tot l'alumnat): Activitats 1-4 + producte + quadern. |
| [`SA2_fitxa_ampliada.md`](SA2_fitxa_ampliada.md) | **Versió ampliada** (aprofundiment): pensament computacional, diana, ODS i ampliacions. |
| [`SA2_checklist_docent.md`](SA2_checklist_docent.md) | **Checklist docent** (una cara): logística prèvia, punts de control per sessió, avaluació. |
| [`SA2_checklist_alumnat.md`](SA2_checklist_alumnat.md) | **Checklist alumnat** (una cara): què he de fer/lliurar + autoavaluació amb semàfor. |
| [`SA2_questionari_conceptes.md`](SA2_questionari_conceptes.md) | Qüestionari de conceptes (sortides digitals, PWM, LED RGB, so, relé): repàs formatiu o prova curta qualificable (10 preguntes). |
| [`SA2_exemple_resolt.md`](SA2_exemple_resolt.md) | Model «jo ho faig»: com es raona un problema anàleg abans de fer el propi. |
| [`SA2_esquemes_connexions.md`](SA2_esquemes_connexions.md) | Taules de connexió pin a pin al Micro:shield (LED, LED RGB, brunzidor, relé) i pins que reserva la mascota. |
| `codi/` | Programes MicroPython (vegeu la taula següent). |

### Codi (`codi/`)

| Programa | Nivell | Què mostra |
|---|---|---|
| [`led_parpelleig/led_parpelleig.py`](codi/led_parpelleig/led_parpelleig.py) | Base | Sortida digital (`write_digital`) amb bucles i un acumulador. |
| [`pwm_led_rgb/pwm_led_rgb.py`](codi/pwm_led_rgb/pwm_led_rgb.py) | Base | Sortida PWM (`write_analog`): efecte de respiració i colors combinats d'un LED RGB. |
| [`musica_altaveu/musica_altaveu.py`](codi/musica_altaveu/musica_altaveu.py) | Base | Mòdul `music`: to segons el botó premut i una melodia completa. |
| [`semafor_rele/semafor_rele.py`](codi/semafor_rele/semafor_rele.py) | Repte / **producte de la SA** | Integra LED, PWM, so i **relé** en un semàfor complet, amb temps en variables. |

Cada programa té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs) a l'`EXPLICACIO.md` de la seva carpeta.
<!-- /web:only-github -->
