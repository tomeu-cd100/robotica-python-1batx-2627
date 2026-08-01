# SA5 · Ràdio: robots que parlen

**Durada:** 6 h (3 sessions) · **Maquinari:** micro:bit V2 (ràdio integrada); vehicle T2 muntat a la SA4 com a receptor

Cinquena situació d'aprenentatge del curs (2n trimestre, segona de tres). Fins ara cada micro:bit ha viscut sola: avui dues plaques es **parlen** per ràdio, sense fils. Dissenyaràs el teu propi **protocol** de comandes curtes i el faràs servir per moure el vehicle a distància, reutilitzant les funcions de moviment que ja vas escriure a la SA4. Programació oficial: [`Programació didàctica/14_SA5_Radio_robots_que_parlen.md`](../../Programació%20didàctica/14_SA5_Radio_robots_que_parlen.md).

> 📻 **Ràdio i treball individual.** El codi i el producte de cada alumne són **sempre individuals**. Provar la ràdio necessita dues plaques (emissora i receptora), així que et pots aparellar **puntualment**, només com a banc de proves, amb la placa d'un company (grups de ràdio per parelles de números de llista, vegeu [`SA5_guia_docent.md`](SA5_guia_docent.md#assignacio-de-grups-de-radio)). Cadascú prova, documenta i és avaluat pel **seu** codi, mai pel del company.

## 📦 Què has d'entregar

| Quan | Lliurable | On es lliura |
|---|---|---|
| S1 | `radio_missatges.py` provat ([Activitat 1](SA5_fitxa_alumnat.md#1--xat-per-radio-sessio-1)) | Es mostra al docent / quadern tècnic |
| S2 | `comandament.py` provat ([Activitat 2](SA5_fitxa_alumnat.md#2--un-protocol-propi-de-comandes-sessio-2)) i mini-check individual (no qualifica) | Es mostra al docent / quadern tècnic |
| S3 | Repte **«control remot bàsic»** ([Activitat 3](SA5_fitxa_alumnat.md#3--repte-control-remot-basic-sessio-3--producte), producte de la SA) + mini-defensa breu | El docent el valida a l'aula |
| ⭐ | [Repte triat](../../Reptes/Reptes_SA5.md) | El docent el valida |
| 📓 | Full del quadern tècnic de cada sessió | En acabar cada sessió |
| 🤖 | Vehicle T2 controlat per ràdio amb el protocol propi (repte «control remot bàsic») | Es mostra al docent a la S3 |

## Itinerari per sessions

> La teva feina és a la **[fitxa base](SA5_fitxa_alumnat.md)**. Aquesta ruta et diu què toca fer a cada sessió.

1. **Sessió 1 · Xat per ràdio** — activa la ràdio (`radio.on()`, `radio.config(group=...)`) i envia/rep missatges de text amb [`radio_missatges.py`](codi/radio_missatges/), aparellat puntualment amb un company. Fes l'[Activitat 1](SA5_fitxa_alumnat.md#1--xat-per-radio-sessio-1).
2. **Sessió 2 · Un protocol propi de comandes** — dissenya el teu protocol (`"CMD:" + ordre`) amb [`comandament.py`](codi/comandament/) i connecta'l a les funcions de moviment de la SA4. Mini-check individual a l'inici (no qualifica). Fes l'[Activitat 2](SA5_fitxa_alumnat.md#2--un-protocol-propi-de-comandes-sessio-2).
3. **Sessió 3 · Repte «control remot bàsic»** — a partir de [`receptor_vehicle.py`](codi/receptor_vehicle/), fes l'[Activitat 3](SA5_fitxa_alumnat.md#3--repte-control-remot-basic-sessio-3--producte) (producte de la SA).
4. **Abans d'entregar** — repassa [el meu checklist](SA5_checklist_alumnat.md).

Si un dia no tens el vehicle muntat o una segona placa a mà, la **lògica** del protocol es pot escriure i provar al **simulador de [python.microbit.org](https://python.microbit.org)**, que **sí simula la ràdio** entre instàncies del simulador (vegeu [`SA5_esquemes_connexions.md`](SA5_esquemes_connexions.md) §Simulació): és una bona via de pràctica individual a casa.

### Si vols més

- [Fitxa ampliada](SA5_fitxa_ampliada.md) — pensament computacional, ODS i ampliacions.
- [Qüestionari de conceptes](SA5_questionari_conceptes.md) — per repassar.
- [Exemple resolt](SA5_exemple_resolt.md) — com es pensa un problema semblant.
- [Reptes de la SA5](../../Reptes/Reptes_SA5.md) — quan tinguis el nucli al dia.

## Producte i avaluació

- **Producte:** repte **«control remot bàsic»** (vehicle controlat per ràdio amb un protocol propi de comandes, mínim 4 comandes) i registre de comandes rebudes al quadern tècnic, tancat i avaluat a la **S3**.
- **Rúbriques:** **R1** (codi, criteri "Funcionament") i **R4** (documentació).
- Escala de nota, rúbriques i tot el sistema: [`Com s'avalua la matèria`](../00_General/00_Avaluacio_per_alumnat.md).

<!-- web:only-github -->
## Tots els documents

| Fitxer | Descripció |
|---|---|
| [`SA5_guia_docent.md`](SA5_guia_docent.md) | Guia del professorat: objectius, seqüència de les 3 sessions, assignació de grups de ràdio, punts clau, errors freqüents i avaluació. |
| [`SA5_fitxa_alumnat.md`](SA5_fitxa_alumnat.md) | **Fitxa base** (nucli, per a tot l'alumnat): Activitats 1-3 + producte + quadern. |
| [`SA5_fitxa_ampliada.md`](SA5_fitxa_ampliada.md) | **Versió ampliada** (aprofundiment): pensament computacional, diana, ODS i ampliacions. |
| [`SA5_checklist_docent.md`](SA5_checklist_docent.md) | **Checklist docent** (una cara): logística prèvia, punts de control per sessió, avaluació. |
| [`SA5_checklist_alumnat.md`](SA5_checklist_alumnat.md) | **Checklist alumnat** (una cara): què he de fer/lliurar + autoavaluació amb semàfor. |
| [`SA5_questionari_conceptes.md`](SA5_questionari_conceptes.md) | Qüestionari de conceptes (ràdio, grup, protocol, esdeveniment): repàs formatiu o prova curta qualificable (10 preguntes). |
| [`SA5_exemple_resolt.md`](SA5_exemple_resolt.md) | Model «jo ho faig»: com es raona un problema anàleg abans de fer el propi. |
| [`SA5_esquemes_connexions.md`](SA5_esquemes_connexions.md) | Configuració de ràdio i pins del vehicle reutilitzats (sense cablatge nou). |
| `codi/` | Programes MicroPython (vegeu la taula següent). |

### Codi (`codi/`)

| Programa | Nivell | Què mostra |
|---|---|---|
| [`radio_missatges/radio_missatges.py`](codi/radio_missatges/radio_missatges.py) | Base | Primer contacte amb el mòdul `radio`: `radio.on()`, `radio.config(group=...)`, `radio.send()`/`radio.receive()`, historial en una llista. |
| [`comandament/comandament.py`](codi/comandament/comandament.py) | Base | Protocol propi de comandes amb prefix (`"CMD:"`), enviades amb botons i gestos. |
| [`receptor_vehicle/receptor_vehicle.py`](codi/receptor_vehicle/receptor_vehicle.py) | Repte / **producte de la SA** | Recepció de comandes i moviment del vehicle amb les funcions de la SA4; historial en tuples. |

Cada programa té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs) a l'`EXPLICACIO.md` de la seva carpeta.
<!-- /web:only-github -->
