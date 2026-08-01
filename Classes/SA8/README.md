# SA8 · Autonomia i telemetria

**Durada:** 6 h (3 sessions; comprimible a 4 h) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 3 (IMU MPU6050, DHT11, BMP280, CCS811); rover T3 de la SA7

Vuitena situació d'aprenentatge del curs (3r trimestre, la segona): el rover autònom (T3) que ja decidia sol a la SA7 aprèn ara a **explicar-se**: llegeix sensors avançats del Kit 3 i envia telemetria per **ràdio** al propi programa d'estació base, mentre s'introdueix la **IA aplicada al control** com a tecnologia emergent. Programació oficial: [`Programació didàctica/17_SA8_Autonomia_i_telemetria.md`](../../Programació%20didàctica/17_SA8_Autonomia_i_telemetria.md).

> 🎛️ **Treball individual.** El codi i el producte de cada alumne són **sempre individuals**. Com que enviar telemetria requereix dues plaques, cada alumne **escriu igualment el seu propi programa d'estació base**, executat temporalment a la placa d'un company (per torns) o del docent.

## 📦 Què has d'entregar

| Quan | Lliurable | On es lliura |
|---|---|---|
| S1 | `comportaments.py` provat sobre el rover ([Activitat 1](SA8_fitxa_alumnat.md#1--sensors-avançats-i-comportaments-amb-prioritats-sessió-1)) | Es mostra al docent / quadern tècnic |
| S2 | Mini-check individual (no qualifica) i `telemetria_radio.py` + el meu `estacio_base.py` ([Activitat 2](SA8_fitxa_alumnat.md#2--telemetria-per-ràdio-sessió-2)) | Es mostra al docent / quadern tècnic |
| S3 | **Sistema de telemetria del rover** ([Activitat 3](SA8_fitxa_alumnat.md#3--ia-aplicada-al-control-i-producte-sessió-3), producte de la SA) + mini-defensa breu + reflexió d'IA | El docent el valida a l'aula |
| ⭐ | [Repte triat](../../Reptes/Reptes_SA8.md) | El docent el valida |
| 📓 | Full del quadern tècnic de cada sessió | En acabar cada sessió |
| 🤖 | Rover T3 amb telemetria per ràdio funcionant (Kit 3 + estació base) | Es mostra al docent a la S3 |

## Itinerari per sessions

> La teva feina és a la **[fitxa base](SA8_fitxa_alumnat.md)**. Aquesta ruta et diu què toca fer a cada sessió.

1. **Sessió 1 · Sensors avançats: llegir el Kit 3** — coneix l'IMU MPU6050 i el DHT11, prova [`comportaments.py`](codi/comportaments/) i dissenya el teu format de missatge de telemetria. Fes l'[Activitat 1](SA8_fitxa_alumnat.md#1--sensors-avançats-i-comportaments-amb-prioritats-sessió-1).
2. **Sessió 2 · Telemetria per ràdio** — programa [`telemetria_radio.py`](codi/telemetria_radio/) i el teu propi [`estacio_base.py`](codi/estacio_base/). Mini-check individual a l'inici (no qualifica). Fes l'[Activitat 2](SA8_fitxa_alumnat.md#2--telemetria-per-ràdio-sessió-2).
3. **Sessió 3 · IA aplicada al control i producte** — practica una classificació de patrons (Teachable Machine) i tanca el [sistema de telemetria del rover](SA8_fitxa_alumnat.md#3--ia-aplicada-al-control-i-producte-sessió-3) (producte de la SA).
4. **Abans d'entregar** — repassa [el meu checklist](SA8_checklist_alumnat.md).

Si un dia no tens el rover o el Kit 3 a mà, pots treballar el **protocol** al simulador de [python.microbit.org](https://python.microbit.org): la **ràdio i el mòdul `log` sí es simulen**, però **cap** sensor (DHT11, IMU) ni els motors s'hi simulen (vegeu [`SA8_esquemes_connexions.md`](SA8_esquemes_connexions.md) §Simulació).

### Si vols més

- [Fitxa ampliada](SA8_fitxa_ampliada.md) — pensament computacional, ODS i ampliacions.
- [Qüestionari de conceptes](SA8_questionari_conceptes.md) — per repassar.
- [Exemple resolt](SA8_exemple_resolt.md) — com es pensa un problema semblant.
- [Reptes de la SA8](../../Reptes/Reptes_SA8.md) — quan tinguis el nucli al dia.

## Producte i avaluació

- **Producte:** **sistema de telemetria del rover** (com a mínim dos sensors del Kit 3 — IMU MPU6050 i DHT11 al nucli —, enviats per ràdio i registrats/visualitzats amb el **propi** programa d'estació base), amb documentació al quadern tècnic i reflexió breu sobre la IA com a tecnologia emergent, tancat i avaluat a la **S3**.
- **Rúbriques:** **R1** (codi, funcionament), **R3** (criteri "Integració") i **R4** (documentació i defensa).
- Escala de nota, rúbriques i tot el sistema: [`Com s'avalua la matèria`](../00_General/00_Avaluacio_per_alumnat.md).

<!-- web:only-github -->
## Tots els documents

| Fitxer | Descripció |
|---|---|
| [`SA8_guia_docent.md`](SA8_guia_docent.md) | Guia del professorat: les 3 sessions, mode comprimit, punts clau, errors freqüents i avaluació. |
| [`SA8_fitxa_alumnat.md`](SA8_fitxa_alumnat.md) | **Fitxa base** (nucli, per a tot l'alumnat): Activitats 1-3 + producte + quadern. |
| [`SA8_fitxa_ampliada.md`](SA8_fitxa_ampliada.md) | **Versió ampliada** (aprofundiment): pensament computacional, diana, ODS i ampliacions. |
| [`SA8_checklist_docent.md`](SA8_checklist_docent.md) | **Checklist docent** (una cara): logística prèvia, punts de control per sessió, avaluació. |
| [`SA8_checklist_alumnat.md`](SA8_checklist_alumnat.md) | **Checklist alumnat** (una cara): què he de fer/lliurar + autoavaluació amb semàfor. |
| [`SA8_questionari_conceptes.md`](SA8_questionari_conceptes.md) | Qüestionari de conceptes (I2C, telemetria, protocol, IA aplicada al control): repàs formatiu o prova curta qualificable (10 preguntes). |
| [`SA8_exemple_resolt.md`](SA8_exemple_resolt.md) | Model «jo ho faig»: com es raona un problema anàleg abans de fer el propi. |
| [`SA8_esquemes_connexions.md`](SA8_esquemes_connexions.md) | Pins del rover: pins heretats + DHT11 + IMU MPU6050 (I2C) + ràdio. |
| `codi/` | Programes MicroPython (vegeu la taula següent). |

### Codi (`codi/`)

| Programa | Nivell | Què mostra |
|---|---|---|
| [`comportaments/comportaments.py`](codi/comportaments/comportaments.py) | Base | Arquitectura de prioritats amb FSM (SEGUIR/ESQUIVAR/RECUPERAR), generalització del comportament autònom de la SA7. |
| [`telemetria_radio/telemetria_radio.py`](codi/telemetria_radio/telemetria_radio.py) | Repte / **producte de la SA** | Telemetria per ràdio: IMU MPU6050 (I2C) + DHT11 + HC-SR04/seguidor + estat FSM, missatges `"TEL:..."`. |
| [`estacio_base/estacio_base.py`](codi/estacio_base/estacio_base.py) | Repte / **producte de la SA** | Segona placa: rep, mostra i registra la telemetria (llista + mitjana simple, mòdul `log`). L'escriu **cada alumne**. |

Cada programa té la seva **pàgina de pràctica** (per què es fa + codi explicat per blocs) a l'`EXPLICACIO.md` de la seva carpeta.
<!-- /web:only-github -->
