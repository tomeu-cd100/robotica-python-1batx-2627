# SA4 · Funcions i moviment

**Durada:** 8 h (4 sessions) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 2 (micro servo(s), motoreductor(s), rodes); fabricació del **vehicle** (peces pretallades pel docent)

## Vincle competencial
- **Competències específiques:** CE-R1 (principal); CE-R2, CE-R3, CE-R4, CE-R5 (secundàries).
- **Criteris d'avaluació:** CA1.1, CA2.1.
- **Competències clau:** STEM, CD, CE.

## Sabers
**Bloc D · MicroPython II** (**funcions**: definició, paràmetres, valors de retorn, modularitat) i **Bloc C · Electrònica** (actuadors de moviment: servomotor, motor DC/motoreductor, driver de motors del kit).

## Objectius d'aprenentatge
1. Definir i aplicar **funcions** amb paràmetres i valor de retorn per modularitzar el codi.
2. Controlar un **servomotor** (angle) i un **motoreductor** (sentit i velocitat) des del Micro:shield.
3. Encapsular moviments bàsics (avançar, girar, aturar) en funcions reutilitzables.
4. Muntar físicament el **vehicle** del fil conductor a partir de peces pretallades.

## Repte o pregunta inicial
> *"Com organitzaries el codi perquè 'avançar', 'girar' i 'aturar' es puguin cridar com si fossin ordres pròpies?"*

## Seqüència de sessions

| Sessió | Objectiu | Activitats | Mini-check | Deures / simulador |
|---|---|---|---|---|
| **1** | Definir funcions amb paràmetres i valor de retorn. | Sintaxi de `def`, paràmetres i `return`; refactorització d'un codi repetitiu de la SA2 en funcions. Control d'un **servomotor** (`set_angle()` pròpia) al Micro:shield. | — | Simulador python.microbit.org (o codi sense maquinari): escriure una funció pròpia amb paràmetre i provar-la amb diversos valors. |
| **2** | Controlar un motoreductor amb funcions de moviment. | Motoreductor(s) del Kit 2: sentit de gir i velocitat (PWM). Funcions `avancar(velocitat)`, `retrocedir(velocitat)`, `girar(costat)`, `aturar()`. **Activitat nucli:** l'alumnat escriu `temps_per_recorregut(cm)`, una funció amb valor de retorn, i l'usa amb `sleep(...)` (primera funció amb `return` que **escriu**, no només llegeix). Mini-check individual (10', escriure una funció amb paràmetre sense apunts; banc: `../Classes/00_General/00_Mini_checks_individuals.md`). | Mini-check individual. | Documentar al quadern les funcions de moviment creades amb un comentari de cada paràmetre. |
| **3** | Integrar les funcions de moviment en un repte de control remot bàsic. | **Repte "control per botons"**: seqüència de moviments encadenada amb les funcions pròpies, activada amb els botons A/B de la micro:bit (base del futur control remot per ràdio de la SA5-SA6). Aquest repte **fa de producte de la SA** (la S4 s'allibera per a la fabricació, primera retallada del pla de contingència). | — | Acabar i documentar el repte si no s'ha tancat a classe. |
| **4** | Muntar físicament el vehicle del fil conductor. | **Fabricació i muntatge del vehicle** (peces pretallades pel docent): xassís, fixació de motoreductors i rodes, muntatge del servo (si aplica a la direcció), instal·lació de la micro:bit i el Micro:shield, portapiles. Primera prova de moviment amb les funcions de la S2-S3. Checklist de muntatge. | — | Portar el vehicle muntat a la propera sessió (SA5) per treballar-hi la comunicació per ràdio. |

## Producte
Repte de control de moviment amb funcions pròpies (avançar/retrocedir/girar/aturar) activat per botons, tancat i avaluat a la **S3**. Muntatge físic del **vehicle** del fil conductor a la **S4** (fabricació, avaluada amb la rúbrica de muntatge). Mini-defensa breu (1-2') del repte de la S3 (R4·DO).

## Avaluació
- Instruments: repte de moviment (S3), muntatge del vehicle (S4), quadern tècnic, mini-defensa, observació.
- Rúbriques: **R1** (codi, criteri "Estructura"/modularitat), **R2** (muntatge del vehicle), **R4** (documentació i defensa, R4·DO).

## Atenció a la diversitat
- **Bastida:** plantilla de funció de moviment amb el nom i els paràmetres ja definits; esquema de connexió del motoreductor.
- **+ Ampliació:** funció de moviment amb velocitat variable i acceleració progressiva; seqüència coreografiada de moviments.

## Recursos
micro:bit + Micro:shield: documentació de servos i motors; documentació Keyestudio de servo/motoreductor. *(Vegeu `09_Materials_recursos_per_unitat.md`.)*
