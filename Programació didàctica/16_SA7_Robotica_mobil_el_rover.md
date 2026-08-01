# SA7 · Robòtica mòbil: el rover

**Durada:** 8 h (4 sessions) · **Maquinari:** micro:bit V2 + Micro:shield; Kit Keyestudio 2 (motoreductors, rodes, seguidor de línia, ultrasons HC-SR04); fabricació del **rover** (peces pretallades pel docent)

## Vincle competencial
- **Competències específiques:** CE-R1 (principal), CE-R3 (principal), CE-R4 (principal), CE-R5 (principal); CE-R2 (secundària).
- **Criteris d'avaluació:** CA1.1, CA3.1, CA4.1.
- **Competències clau:** STEM, CD, CE.

## Sabers
**Bloc F · Robòtica, tecnologies emergents i projecte** (inici): robòtica mòbil (xassís, rodes, cinemàtica diferencial), algorismes de comportament (seguidor de línia, evita-obstacles), modelització de trajectòries. **Bloc D, ampliació**: gestió d'errors en temps d'execució amb `try`/`except` (lectura robusta d'un sensor), avançada des de la SA8 per descarregar-hi la sessió de pic de conceptes.

> **Fabricació del rover:** el muntatge físic del rover es fa en una **sessió prèvia a la SA7** ("Sessió 0" del 3r trimestre), finançada per la compressió d'hores de la SA8 (vegeu `08_Sequenciacio_temporal_anual.md`, «Fil conductor i consum del marge»). En arribar a la S1 d'aquesta SA, l'alumnat ja disposa del **rover muntat** (peces pretallades pel docent) i hi comença a programar comportaments. Igual que el muntatge de la mascota (SA2·S4) i del vehicle (SA4·S4), el **muntatge del rover** a la Sessió 0 té instrument propi: **checklist de muntatge** avaluada amb **R2** (criteri "Muntatge"), de caràcter **formatiu** (no compta a les hores ni als instruments de la SA7 pròpiament dita, que comencen a la S1).

## Objectius d'aprenentatge
1. Relacionar el control de dos motoreductors amb el gir del rover (**cinemàtica diferencial** bàsica).
2. Programar un comportament autònom de **seguidor de línia**.
3. Programar un comportament autònom d'**evitar obstacles** amb el sensor d'ultrasons.
4. Modelitzar una **trajectòria** senzilla combinant girs i avanços temporitzats.

## Repte o pregunta inicial
> *"Com fa un robot per seguir una línia pintada a terra o esquivar un obstacle sense que ningú el guiï?"*

## Seqüència de sessions

| Sessió | Objectiu | Activitats | Mini-check | Deures / simulador |
|---|---|---|---|---|
| **1** | Controlar el gir diferencial del rover. | Revisió del rover muntat; funcions de moviment (SA4) adaptades als dos motoreductors del rover. **Cinemàtica diferencial**: girar variant la velocitat/sentit relatiu de cada roda. Primeres proves de trajectòria (quadrat, gir tancat). | — | Simulador python.microbit.org (lògica sense maquinari): esbossar en pseudocodi una trajectòria en "L". |
| **2** | Programar el comportament de seguidor de línia. | Sensor **seguidor de línia** del Kit 2: lectura i llindar de detecció. Algorisme bàsic de correcció de trajectòria (girar cap al costat on es perd la línia). Proves sobre un circuit de línia a terra. Mini-check individual (10', condicional de correcció de trajectòria sense apunts; banc: `../Classes/00_General/00_Mini_checks_individuals.md`). | Mini-check individual. | Documentar al quadern el llindar de detecció triat i una captura/foto del circuit de proves. |
| **3** | Programar el comportament d'evitar obstacles. | Sensor d'**ultrasons HC-SR04**: mesura de distància i funció `mesura_distancia()`. **Activitat nucli:** lectura robusta amb `try`/`except OSError` al voltant de `machine.time_pulse_us(...)` (primer `try`/`except` que escriu l'alumnat). Algorisme d'evita-obstacles (aturar/girar en detectar un obstacle proper). **Repte "tria un comportament autònom"**: seguidor de línia o evita-obstacles, segons el material disponible a cada taula. Aquest repte **fa de producte de la SA** si el calendari ho requereix (pla de contingència, tercera retallada). | — | Acabar i documentar el comportament triat si no s'ha tancat a classe. |
| **4** | Integrar i millorar el comportament autònom del rover. | Integració del comportament triat (seguidor de línia i/o evita-obstacles) amb petites millores (velocitat variable, marge de seguretat). **Producte: comportament autònom del rover** funcional i documentat, amb mini-defensa breu. | — | — |

## Producte
Rover individual amb un **comportament autònom** funcional (seguidor de línia i/o evita-obstacles), codi organitzat en funcions i documentació de les proves i millores al quadern tècnic.

## Avaluació
- Instruments: comportament autònom del rover, quadern tècnic, mini-defensa, observació.
- Rúbriques: **R1**, **R3** (criteris "Compliment del repte" i "Autonomia/control"), **R4** (documentació).

## Atenció a la diversitat
- **Bastida:** algorisme d'evita-obstacles esquelet amb els llindars ja indicats; circuit de línia model imprès.
- **+ Ampliació:** combinar seguidor de línia I evita-obstacles en un mateix comportament amb prioritats; ajustar velocitat segons proximitat (control proporcional bàsic).

## Recursos
Documentació de robòtica educativa amb micro:bit (seguidor de línia, evita-obstacles); Open Roberta Lab (suport de simulació). *(Vegeu `09_Materials_recursos_per_unitat.md`.)*
