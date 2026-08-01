# SA2 · Sortides: el robot actua

**Durada:** 8 h (4 sessions) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 1 (LED, LED RGB, brunzidor) i Kit 3 (relé, LED addicionals); fabricació de la **mascota** (peces pretallades pel docent)

## Vincle competencial
- **Competències específiques:** CE-R1 (principal), CE-R2 (principal); CE-R3, CE-R5 (secundàries).
- **Criteris d'avaluació:** CA1.1, CA2.1, CA2.2.
- **Competències clau:** STEM, CD, CE.

## Sabers
**Bloc B · MicroPython I** (variables i bucles, `for`/`while`, acumuladors) i **Bloc C · Electrònica** (sortides digitals i PWM: LED, matriu LED, so, relé; connexió al Micro:shield).

## Objectius d'aprenentatge
1. Escriure programes amb **variables i bucles** (`for`, `while`) per controlar sortides repetitives.
2. Connectar i controlar **sortides digitals i PWM** (LED, LED RGB, brunzidor, relé) al Micro:shield amb seguretat.
3. Programar animacions i sons a la **matriu LED** i a l'altaveu de la micro:bit.
4. Muntar físicament la **mascota** del fil conductor a partir de peces pretallades.

## Repte o pregunta inicial
> *"Com fa un robot per parpellejar, fer soroll o encendre's de manera intermitent?"*

## Seqüència de sessions

| Sessió | Objectiu | Activitats | Mini-check | Deures / simulador |
|---|---|---|---|---|
| **1** | Controlar sortides digitals bàsiques amb bucles. | `display.show()`/`display.scroll()` amb bucles `for`; parpelleig d'un LED extern connectat al Micro:shield (`digital_write`); acumuladors per comptar repeticions. Introducció al Kit 1 (LED, LED RGB). | — | Simulador python.microbit.org: variar el nombre de repeticions i el temps d'espera d'una animació senzilla. |
| **2** | Controlar sortides PWM i so. | Sortides **PWM** (`analog_write`) per regular la intensitat d'un LED o el to del brunzidor; melodies senzilles amb l'altaveu integrat. LED RGB (colors combinats). Mini-check individual (10', codi de bucle amb PWM sense apunts; banc: `../Classes/00_General/00_Mini_checks_individuals.md`). | Mini-check individual. | Provar al simulador una seqüència de colors o de tons pròpia. |
| **3** | Integrar diverses sortides en un repte complet. | **Repte "semàfor o llum d'ambient"**: seqüència de LED/RGB/brunzidor amb bucles i temporitzacions, ús del relé del Kit 3 per commutar un circuit extern. Aquest repte **fa de producte de la SA** (la S4 s'allibera per a la fabricació, primera retallada del pla de contingència). | — | Acabar i documentar el repte al quadern tècnic si no s'ha tancat a classe. |
| **4** | Muntar físicament la mascota del fil conductor. | **Fabricació i muntatge de la mascota** (peces pretallades pel docent amb la talladora làser i la impressora 3D): muntatge de l'estructura, fixació de la micro:bit i el Micro:shield, primera prova de la matriu LED com a "cara". Checklist de muntatge i retorn ordenat del material. | — | Portar la mascota muntada a la propera sessió (SA3) per començar-hi a treballar sensors. |

## Producte
Repte de sortides (LED/RGB/brunzidor/relé amb bucles i PWM), tancat i avaluat a la **S3**. Muntatge físic de la **mascota** del fil conductor a la **S4** (fabricació, avaluada amb la rúbrica de muntatge).

## Avaluació
- Instruments: repte de sortides (S3), muntatge de la mascota (S4), quadern tècnic, observació.
- Rúbriques: **R1** (codi), **R2** (muntatge de la mascota; criteri "Muntatge"), **R4** (documentació).

## Atenció a la diversitat
- **Bastida:** simulació prèvia al python.microbit.org; funció model de parpelleig proporcionada.
- **+ Ampliació:** seqüència de llums sincronitzada amb el so; ús combinat de relé i LED RGB en un patró propi.

## Recursos
micro:bit reference (matriu LED, so, pins); Keyestudio wiki de sensors i actuadors bàsics. *(Vegeu `09_Materials_recursos_per_unitat.md`.)*
