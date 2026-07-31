# SA6 · Control: el robot decideix

**Durada:** 8 h (4 sessions; S4 = Prova pràctica T2) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 1 (LED/actuadors), Kit 2 (sensor de temperatura) i Kit 3 (relé, DHT11); vehicle muntat a SA4, control per ràdio de SA5

## Vincle competencial
- **Competències específiques:** CE-R1 (principal), CE-R3 (principal); CE-R2, CE-R4, CE-R5 (secundàries).
- **Criteris d'avaluació:** CA1.1, CA2.1, CA3.1.
- **Competències clau:** STEM, CD, CPSAA.

## Sabers
**Bloc E · Sistemes de control i automatització**: concepte de sistema de control, **llaç obert vs llaç tancat**, sensors com a realimentació, **màquines d'estats finits**, ús d'objectes ja creats de la biblioteca de micro:bit (**objectes només d'ús**, no es programa orientació a objectes pròpia).

## Objectius d'aprenentatge
1. Distingir un sistema de **llaç obert** d'un de **llaç tancat** i identificar-ne exemples al vehicle.
2. Implementar una **màquina d'estats finits** senzilla (p. ex. RUN / STOP / ALERTA) amb condicionals.
3. Programar una **aturada d'emergència** que interromp qualsevol altra acció en curs.
4. Integrar un sensor (temperatura/relé) com a realimentació d'un sistema de control bàsic.

## Repte o pregunta inicial
> *"Com fas que un vehicle teledirigit s'aturi SEMPRE que calgui, encara que estigui fent una altra cosa?"*

## Seqüència de sessions

| Sessió | Objectiu | Activitats | Mini-check | Deures / simulador |
|---|---|---|---|---|
| **1** | Distingir llaç obert i llaç tancat; introduir la màquina d'estats. | Concepte de sistema de control: consigna, error, realimentació. Exemples amb el vehicle (llaç obert: seguir una comanda fixa; llaç tancat: aturar-se en detectar un sensor). Disseny d'una **màquina d'estats** (diagrama RUN/STOP/ALERTA) amb condicionals encadenats. | — | Simulador python.microbit.org: esbossar el diagrama d'estats propi i provar-ne una versió mínima en codi. |
| **2** | Programar l'aturada d'emergència com a estat prioritari. | Implementació de l'estat **STOP d'emergència**: un botó o comanda de ràdio que interromp qualsevol moviment en curs, independentment de l'estat previ. Ús d'un actuador del Kit 1/3 (LED/relé) com a senyal visual de l'estat. Mini-check individual (10', condicional d'estat sense apunts; banc: `../Classes/00_General/00_Mini_checks_individuals.md`). | Mini-check individual. | Documentar el diagrama d'estats final al quadern (estats i transicions). |
| **3** | Integrar sensor de temperatura com a realimentació i tancar el producte. | Sensor de temperatura (Kit 2) i DHT11 (Kit 3) com a entrada de control: exemple de "termòstat" senzill (relé s'activa/desactiva segons llindar) integrat amb la màquina d'estats del vehicle. **Producte: "vehicle teledirigit amb aturada d'emergència"**: control per ràdio (SA5) + màquina d'estats + STOP prioritari. **Es tanca a la S3** (mini-defensa a peu de taula, 2-3'). | — | Acabar i documentar el producte si no s'ha tancat a classe. |
| **4** | — | **Prova pràctica T2** (individual, sessió sencera — vegeu `../Avaluació/Prova_practica_T2.md`). | — | — |

## Producte
**Vehicle teledirigit amb aturada d'emergència**: control remot per ràdio (SA5), moviment per funcions (SA4) i sistema de control amb màquina d'estats i STOP prioritari, amb senyal visual de l'estat. **Es tanca a la S3**; la S4 és la prova T2 individual.

## Avaluació
- Instruments: producte (S3) + quadern + defensa a peu de taula (R4·DO) + **prova pràctica T2** (S4, individual).
- Rúbriques: **R1**, **R3** (criteri "Autonomia/control"), **R4** (documentació i defensa, R4·DO); R1, R3, R4 (prova).

## Atenció a la diversitat
- **Bastida:** diagrama d'estats model (RUN/STOP/ALERTA) amb transicions ja indicades; esquelet de funció `actualitza_estat()`.
- **+ Ampliació:** afegir un tercer estat (ALERTA per temperatura o obstacle) amb transició pròpia; realimentació proporcional en lloc de tot/res.

## Recursos
INTEF / Isaac Computer Science sobre màquines d'estats i control; documentació Keyestudio de relé i DHT11. *(Vegeu `09_Materials_recursos_per_unitat.md`.)*
