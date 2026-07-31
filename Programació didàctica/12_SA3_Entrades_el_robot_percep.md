# SA3 · Entrades: el robot percep

**Durada:** 8 h (4 sessions; S4 = Prova pràctica T1) · **Maquinari:** micro:bit V2 + Micro:shield; sensors integrats (botons, llum, temperatura, acceleròmetre); Kit Keyestudio 1 (polsador, potenciòmetre, sensor de temperatura bàsic), Kit 2 (sensor de llum, sensor de temperatura, ultrasons HC-SR04, PIR, humitat del terra) i Kit 3 (sensor de so, DHT11); mascota muntada a SA2

## Vincle competencial
- **Competències específiques:** CE-R1 (principal), CE-R2 (principal); CE-R3, CE-R5 (secundàries).
- **Criteris d'avaluació:** CA1.1, CA2.1, CA2.2.
- **Competències clau:** STEM, CD.

## Sabers
**Bloc C · Electrònica** (entrades digitals amb *pull-up*/*debounce*; entrades analògiques i conversió A/D) i **Bloc D · MicroPython II** (**condicionals** `if/elif/else` aplicats a la interpretació de senyals de sensors).

## Objectius d'aprenentatge
1. Llegir entrades **digitals** (botons, polsador) i **analògiques** (potenciòmetre, sensor de llum, sensor de temperatura) i interpretar-ne els valors.
2. Aplicar **condicionals** (`if/elif/else`) per relacionar la lectura d'un sensor amb una acció de sortida.
3. Utilitzar el **REPL/consola** per depurar i visualitzar dades de sensors en temps real.
4. Programar la **mascota expressiva**: reaccions de la matriu LED/so davant estímuls de l'entorn.

## Repte o pregunta inicial
> *"Com sap la teva mascota que li estàs parlant, que hi ha llum o que t'hi acostes?"*

## Seqüència de sessions

| Sessió | Objectiu | Activitats | Mini-check | Deures / simulador |
|---|---|---|---|---|
| **1** | Llegir entrades digitals i aplicar condicionals bàsics. | Botons A/B i polsador extern del Kit 1 amb `if/elif/else`; concepte de *pull-up* i **antirebot** (*debounce*). Comptador de premudes amb el REPL. Sensors integrats de la micro:bit (llum, temperatura) com a primera lectura analògica. | — | Simulador python.microbit.org: provar condicions sobre `button_a.is_pressed()`. |
| **2** | Llegir entrades analògiques i mapejar valors. | Potenciòmetre (Kit 1): `read_analog()`, `map()` de rang. **Sensor de llum** (Kit 2): "llum automàtic" (sensor de llum → LED/matriu segons llindar). **Sensor de temperatura** (Kit 1, bàsic): temperatura llegida i interpretada amb condicionals. Mini-check individual (10', condicional amb entrada analògica sense apunts; banc: `../Classes/00_General/00_Mini_checks_individuals.md`). | Mini-check individual. | Calibrar un llindar propi amb el simulador o al REPL i anotar-lo al quadern. |
| **3** | Integrar diversos sensors a la mascota expressiva. | Sensor d'**ultrasons** (Kit 2), **PIR** de moviment i sensor de **so**/DHT11 (Kit 3) aplicats a la mascota: reacció (cara/so) segons proximitat, presència o llum ambiental. **Producte: "mascota expressiva"** amb almenys dos sensors i condicionals encadenats. **Es tanca a la S3** (mini-defensa breu). | — | Documentar al quadern les lectures de sensor i el llindar triat, amb captura del REPL/simulador si cal. |
| **4** | — | **Prova pràctica T1** (individual, sessió sencera — vegeu `../Avaluació/Prova_practica_T1.md`). | — | — |

## Producte
**Mascota expressiva** muntada (SA2) i programada (SA3): reacciona amb la matriu LED i el so davant almenys dos estímuls d'entrada (llum, proximitat, so, presència o temperatura), amb codi organitzat en condicionals i registre de mesures al quadern. **Es tanca a la S3**; la S4 és la prova T1 individual.

## Avaluació
- Instruments: producte (S3) + quadern + **prova pràctica T1** (S4, individual).
- Rúbriques: **R1**, **R2**, **R3** (producte, criteri "compliment del repte"); R1, R2, R4 (prova).

## Atenció a la diversitat
- **Bastida:** simulació prèvia al python.microbit.org; funció model de lectura d'un sensor proporcionada.
- **+ Ampliació:** calibratge fi del sensor; llindars configurables per variable; combinar tres o més sensors en la reacció de la mascota.

## Recursos
micro:bit sensors integrats (acceleròmetre, llum, temperatura); Keyestudio wiki de sensors de percepció; python.microbit.org (REPL). *(Vegeu `09_Materials_recursos_per_unitat.md`.)*
