# SA8 · Autonomia i telemetria

**Durada:** 6 h (3 sessions; comprimible a 4 h fusionant S1+S2 — vegeu `08_Sequenciacio_temporal_anual.md`) · **Maquinari:** micro:bit V2 (ràdio); Kit Keyestudio 3 (IMU MPU6050, DHT11, BMP280, CCS811); rover de SA7

## Vincle competencial
- **Competències específiques:** CE-R1 (principal), CE-R3 (principal), CE-R4 (principal); CE-R5 (principal).
- **Criteris d'avaluació:** CA1.1, CA3.1, CA4.2.
- **Competències clau:** STEM, CD.

## Sabers
**Bloc F · Robòtica, tecnologies emergents i projecte**: **telemetria i monitoratge** de dades per ràdio; introducció a la **IA** aplicada al control (classificació senzilla, reconeixement de patrons amb dades de sensors).

## Objectius d'aprenentatge
1. Llegir sensors avançats del Kit 3 (**IMU MPU6050**, DHT11, BMP280, CCS811) i interpretar-ne les magnituds.
2. Enviar dades de sensors per **ràdio** des del rover a una micro:bit "estació base" (telemetria).
3. Registrar i visualitzar dades rebudes (llista de lectures, mitjana simple).
4. Introduir-se a la **IA aplicada al control**: classificació senzilla de patrons de dades (p. ex. amb Teachable Machine) com a tecnologia emergent.

## Repte o pregunta inicial
> *"Com sap algú, des d'una altra taula, què està 'sentint' el rover en aquest moment?"*

## Seqüència de sessions

| Sessió | Objectiu | Activitats | Mini-check | Deures / simulador |
|---|---|---|---|---|
| **1** | Llegir sensors avançats i preparar-los per a la telemetria. | IMU MPU6050 (orientació/gestos), DHT11 (temperatura/humitat), BMP280 (pressió), CCS811 (CO₂): lectura i interpretació de magnituds al rover. Disseny del format de missatge de telemetria (què s'envia i amb quina freqüència). *(Sessió fusionable amb la S2 en cas de compressió — vegeu pla de contingència del doc 08.)* | — | Simulador python.microbit.org: provar l'enviament d'un missatge de ràdio amb un valor numèric simulat. |
| **2** | Enviar i registrar dades per telemetria. | Enviament de lectures del rover per **ràdio** a una micro:bit "estació base"; registre en una **llista** de l'estació base i càlcul d'una mitjana simple. Visualització de les dades rebudes al REPL. Mini-check individual (10', enviar un valor de sensor per ràdio sense apunts; banc: `../Classes/00_General/00_Mini_checks_individuals.md`). | Mini-check individual. | Documentar al quadern el format de missatge triat i una captura de les dades rebudes. |
| **3** | Introduir la IA aplicada al control i tancar el producte. | Introducció a la **classificació de patrons** amb dades de sensors (p. ex. Teachable Machine amb dades d'acceleròmetre/so, a nivell de demostració i pràctica guiada). **Producte: sistema de telemetria del rover** (mínim dos sensors, enviament per ràdio, registre a l'estació base) amb reflexió breu sobre l'ús de la IA com a tecnologia emergent. | — | Acabar i documentar el producte si no s'ha tancat a classe. |

## Producte
Sistema de **telemetria del rover**: com a mínim dos sensors del Kit 3 llegits, enviats per ràdio i registrats/visualitzats a l'estació base, amb documentació al quadern tècnic i una reflexió breu sobre la IA aplicada al control.

## Avaluació
- Instruments: sistema de telemetria, quadern tècnic, observació.
- Rúbriques: **R1**, **R3** (criteri "Integració"), **R4** (documentació).

## Atenció a la diversitat
- **Bastida:** format de missatge de telemetria model (p. ex. `"T:23.5"`); funció `envia_lectura()` esquelet.
- **+ Ampliació:** enviar més d'un sensor combinat en un sol missatge (protocol propi més ric); comparar dades classificades manualment vs amb Teachable Machine.

## Recursos
micro:bit Code & AI; introducció a Teachable Machine; documentació Keyestudio dels sensors avançats (IMU, DHT11, BMP280, CCS811). *(Vegeu `09_Materials_recursos_per_unitat.md`.)*
