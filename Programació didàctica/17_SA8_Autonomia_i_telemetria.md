# SA8 · Autonomia i telemetria

**Durada:** 6 h (3 sessions; comprimible a 4 h fusionant S1+S2 — vegeu `08_Sequenciacio_temporal_anual.md`) · **Maquinari:** micro:bit V2 (ràdio); Kit Keyestudio 3 (IMU MPU6050, DHT11, BMP280, CCS811); rover de SA7

## Vincle competencial
- **Competències específiques:** CE-R1 (principal), CE-R3 (principal), CE-R4 (principal), CE-R5 (principal); CE-R2 (secundària).
- **Criteris d'avaluació:** CA1.1, CA3.1, CA4.2.
- **Competències clau:** STEM, CD.

## Sabers
**Bloc F · Robòtica, tecnologies emergents i projecte**: **telemetria i monitoratge** de dades per ràdio; introducció a la **IA** aplicada al control (classificació senzilla, reconeixement de patrons amb dades de sensors).

## Objectius d'aprenentatge
1. Llegir sensors avançats del Kit 3 (**IMU MPU6050**, DHT11, BMP280, CCS811) i interpretar-ne les magnituds.
2. Enviar dades de sensors per **ràdio** des del rover al **propi programa d'estació base** (telemetria), executat temporalment a la placa d'un company o del docent.
3. Registrar i visualitzar dades rebudes (llista de lectures, mitjana simple).
4. Introduir-se a la **IA aplicada al control**: classificació senzilla de patrons de dades (p. ex. amb Teachable Machine) com a tecnologia emergent.

## Repte o pregunta inicial
> *"Com sap algú, des d'una altra taula, què està 'sentint' el rover en aquest moment?"*

> **Ràdio, estació base i treball individual (dotació d'1 micro:bit/alumne):** el codi i el producte de cada alumne són **sempre individuals**. Com que enviar telemetria requereix dues plaques (rover + estació base), cada alumne **escriu igualment el seu propi programa d'estació base** (és el que s'avalua, no la placa on corre) i l'executa temporalment a la placa d'un company (per torns, grups de ràdio per parells de números de llista) o a la micro:bit del docent. La placa és només l'eina de banc de proves; el codi, la telemetria rebuda i la interpretació de les dades són sempre l'evidència pròpia de cada alumne.

## Seqüència de sessions

| Sessió | Objectiu | Activitats | Mini-check | Deures / simulador |
|---|---|---|---|---|
| **1** | Llegir sensors avançats i preparar-los per a la telemetria. | IMU MPU6050 (orientació/gestos), DHT11 (temperatura/humitat), BMP280 (pressió), CCS811 (CO₂): lectura i interpretació de magnituds al rover. Disseny del format de missatge de telemetria (què s'envia i amb quina freqüència). *(Sessió fusionable amb la S2 en cas de compressió — vegeu pla de contingència del doc 08.)* | — | Simulador python.microbit.org: provar l'enviament d'un missatge de ràdio amb un valor numèric simulat. |
| **2** | Enviar i registrar dades per telemetria. | Enviament de lectures del rover per **ràdio** al propi programa d'estació base, executat temporalment a la placa d'un company (per torns) o del docent; registre en una **llista** i càlcul d'una mitjana simple. Visualització de les dades rebudes al REPL. Mini-check individual (10', enviar un valor de sensor per ràdio sense apunts; banc: `../Classes/00_General/00_Mini_checks_individuals.md`). | Mini-check individual. | Documentar al quadern el format de missatge triat i una captura de les dades rebudes. |
| **3** | Introduir la IA aplicada al control i tancar el producte. | Introducció a la **classificació de patrons** amb dades de sensors (p. ex. Teachable Machine amb dades d'acceleròmetre/so, a nivell de demostració i pràctica guiada). **Producte: sistema de telemetria del rover** (mínim dos sensors, enviament per ràdio, registre amb el propi programa d'estació base) amb reflexió breu sobre l'ús de la IA com a tecnologia emergent. | — | Acabar i documentar el producte si no s'ha tancat a classe. |

## Producte
Sistema de **telemetria del rover**: com a mínim dos sensors del Kit 3 llegits al rover propi, enviats per ràdio i registrats/visualitzats amb el **propi programa d'estació base** (executat temporalment a la placa d'un company o del docent), amb documentació al quadern tècnic i una reflexió breu sobre la IA aplicada al control.

## Avaluació
- Instruments: sistema de telemetria, quadern tècnic, observació.
- Rúbriques: **R1**, **R3** (criteri "Integració"), **R4** (documentació).

## Atenció a la diversitat
- **Bastida:** format de missatge de telemetria model (p. ex. `"T:23.5"`); funció `envia_lectura()` esquelet.
- **+ Ampliació:** enviar més d'un sensor combinat en un sol missatge (protocol propi més ric); comparar dades classificades manualment vs amb Teachable Machine.

## Recursos
micro:bit Code & AI; introducció a Teachable Machine; documentació Keyestudio dels sensors avançats (IMU, DHT11, BMP280, CCS811). *(Vegeu `09_Materials_recursos_per_unitat.md`.)*
