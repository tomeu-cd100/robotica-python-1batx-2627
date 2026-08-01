# SA6 · Control: el robot decideix

**Durada:** 8 h (4 sessions; S4 = Prova pràctica T2) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 1 (LED/actuadors), Kit 2 (sensor de temperatura) i Kit 3 (relé, DHT11); vehicle muntat a SA4, control per ràdio de SA5

Sisena situació d'aprenentatge del curs (2n trimestre, l'última): fins ara el vehicle obeïa ordres puntuals; avui es converteix en un **sistema de control** amb una **màquina d'estats** i una **aturada d'emergència prioritària** que interromp qualsevol moviment, es dispari com es dispari. **Es tanca el Projecte T2.** Programació oficial: [`Programació didàctica/15_SA6_Control_el_robot_decideix.md`](../../Programació%20didàctica/15_SA6_Control_el_robot_decideix.md).

> 🎛️ **Treball individual.** El codi i el producte de cada alumne són **sempre individuals**, com a la resta del curs.

## 📦 Què has d'entregar

| Quan | Lliurable | On es lliura |
|---|---|---|
| S1 | `maquina_estats_semafor.py` i `termostat_histeresi.py` provats ([Activitat 1](SA6_fitxa_alumnat.md#1--llaç-obert-llaç-tancat-i-la-primera-fsm-sessió-1)) | Es mostra al docent / quadern tècnic |
| S2 | Mini-check individual (no qualifica) i `vehicle_seguretat.py` amb l'STOP prioritari ([Activitat 2](SA6_fitxa_alumnat.md#2--aturada-demergència-prioritària-sessió-2)) | Es mostra al docent / quadern tècnic |
| S3 | Repte **«vehicle amb aturada d'emergència»** ([Activitat 3](SA6_fitxa_alumnat.md#3--repte-vehicle-amb-aturada-demergència-sessió-3--producte), producte de la SA — tanca el Projecte T2) + mini-defensa breu | El docent el valida a l'aula |
| S4 | **Prova pràctica T2** (individual, sessió sencera) | Es realitza a l'aula |
| ⭐ | [Repte ⭐ de Reptes_SA6.md](../../Reptes/Reptes_SA6.md) (nucli obligatori) | El docent el valida → compta R1 |
| 📓 | Full del quadern tècnic de cada sessió | En acabar cada sessió |
| 🤖 | Vehicle T2 amb màquina d'estats i STOP prioritari (repte «vehicle amb aturada d'emergència») | Es mostra al docent a la S3 |

## Itinerari per sessions

> La teva feina és a la **[fitxa base](SA6_fitxa_alumnat.md)**. Aquesta ruta et diu què toca fer a cada sessió.

1. **Sessió 1 · Llaç obert, llaç tancat i la primera FSM** — distingeix llaç obert de llaç tancat, dissenya el teu diagrama d'estats i prova [`maquina_estats_semafor.py`](codi/maquina_estats_semafor/) i [`termostat_histeresi.py`](codi/termostat_histeresi/). Fes l'[Activitat 1](SA6_fitxa_alumnat.md#1--llaç-obert-llaç-tancat-i-la-primera-fsm-sessió-1).
2. **Sessió 2 · Aturada d'emergència prioritària** — programa l'estat STOP prioritari (polsador + LED) i prova [`registre_dades.py`](codi/registre_dades/). Mini-check individual a l'inici (no qualifica). Fes l'[Activitat 2](SA6_fitxa_alumnat.md#2--aturada-demergència-prioritària-sessió-2).
3. **Sessió 3 · Repte «vehicle amb aturada d'emergència»** — a partir de [`vehicle_seguretat.py`](codi/vehicle_seguretat/), fes l'[Activitat 3](SA6_fitxa_alumnat.md#3--repte-vehicle-amb-aturada-demergència-sessió-3--producte) (producte de la SA, **tanca el Projecte T2**).
4. **Sessió 4 · Prova pràctica T2** — sessió individual sencera, sense material nou.
5. **Abans d'entregar** — repassa [el meu checklist](SA6_checklist_alumnat.md).

Si un dia no tens el vehicle muntat a mà, la **lògica** de la màquina d'estats i de la histèresi es pot escriure i provar al **simulador de [python.microbit.org](https://python.microbit.org)** (vegeu [`SA6_esquemes_connexions.md`](SA6_esquemes_connexions.md) §Simulació): és una bona via de pràctica individual a casa, encara que no reprodueixi el moviment real dels motors ni l'efecte del relé.

### Si vols més

- [Fitxa ampliada](SA6_fitxa_ampliada.md) — pensament computacional, ODS i ampliacions.
- [Qüestionari de conceptes](SA6_questionari_conceptes.md) — per repassar.
- [Exemple resolt](SA6_exemple_resolt.md) — com es pensa un problema semblant.
- [Reptes ⭐⭐/⭐⭐⭐ de la SA6](../../Reptes/Reptes_SA6.md) — ampliació opcional, per a qui va sobrat de temps (el ⭐ ja és nucli obligatori, vegeu «Què has d'entregar»).

## Producte i avaluació

- **Producte:** repte **«vehicle amb aturada d'emergència»** (vehicle amb màquina d'estats RUN/STOP i STOP prioritari, activable per polsador i per ràdio, amb LED indicador), tancat i avaluat a la **S3** — **tanca el Projecte T2**. La **S4** és la prova pràctica T2 individual.
- **Rúbriques:** **R1** (codi, funcionament), **R3** (criteri "Autonomia/control") i **R4** (documentació i defensa).
- Escala de nota, rúbriques i tot el sistema: [`Com s'avalua la matèria`](../00_General/00_Avaluacio_per_alumnat.md).

<!-- web:only-github -->
## Tots els documents

| Fitxer | Descripció |
|---|---|
| [`SA6_guia_docent.md`](SA6_guia_docent.md) | Guia del professorat: objectius, seqüència de les 4 sessions, punts clau, errors freqüents i avaluació. |
| [`SA6_fitxa_alumnat.md`](SA6_fitxa_alumnat.md) | **Fitxa base** (nucli, per a tot l'alumnat): Activitats 1-3 + producte + quadern. |
| [`SA6_fitxa_ampliada.md`](SA6_fitxa_ampliada.md) | **Versió ampliada** (aprofundiment): pensament computacional, diana, ODS i ampliacions. |
| [`SA6_checklist_docent.md`](SA6_checklist_docent.md) | **Checklist docent** (una cara): logística prèvia, punts de control per sessió, avaluació. |
| [`SA6_checklist_alumnat.md`](SA6_checklist_alumnat.md) | **Checklist alumnat** (una cara): què he de fer/lliurar + autoavaluació amb semàfor. |
| [`SA6_questionari_conceptes.md`](SA6_questionari_conceptes.md) | Qüestionari de conceptes (llaç obert/tancat, FSM, histèresi, STOP prioritari): repàs formatiu o prova curta qualificable (10 preguntes). |
| [`SA6_exemple_resolt.md`](SA6_exemple_resolt.md) | Model «jo ho faig»: com es raona un problema anàleg abans de fer el propi. |
| [`SA6_esquemes_connexions.md`](SA6_esquemes_connexions.md) | Pins del vehicle reutilitzats + relé/DHT11 de l'ampliació. |
| `codi/` | Programes MicroPython (vegeu la taula següent). |

### Codi (`codi/`)

| Programa | Nivell | Què mostra |
|---|---|---|
| [`maquina_estats_semafor/maquina_estats_semafor.py`](codi/maquina_estats_semafor/maquina_estats_semafor.py) | Base | Màquina d'estats finits autònoma (variable d'estat + transicions), sense dependre del vehicle. |
| [`termostat_histeresi/termostat_histeresi.py`](codi/termostat_histeresi/termostat_histeresi.py) | Base | Llaç tancat amb **histèresi** (dos llindars): el nucli avaluable del control amb realimentació. |
| [`registre_dades/registre_dades.py`](codi/registre_dades/registre_dades.py) | Base | Data logging natiu de la micro:bit V2 (mòdul `log`), lectura per USB (`MY_DATA.HTM`). |
| [`vehicle_seguretat/vehicle_seguretat.py`](codi/vehicle_seguretat/vehicle_seguretat.py) | Repte / **producte de la SA** | Vehicle amb protocol de ràdio de la SA5 + màquina d'estats RUN/STOP/ALERTA + STOP prioritari (polsador i ràdio). |

Cada programa té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs) a l'`EXPLICACIO.md` de la seva carpeta.
<!-- /web:only-github -->
