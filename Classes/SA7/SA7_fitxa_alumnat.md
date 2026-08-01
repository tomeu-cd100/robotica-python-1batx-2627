# SA7 · Fitxa base — Robòtica mòbil: el rover

<!-- web:only-github -->

**Nom:** ______________________  **Data:** __________

<!-- /web:only-github -->

> *"Com fa un robot per seguir una línia pintada a terra o esquivar un obstacle sense que ningú el guiï?"* El teu vehicle (T2) ja és un **rover** (T3): a la Sessió 0 li has muntat un sensor d'ultrasons i un seguidor de línia. Avui li ensenyes a decidir **sol**. Tot el treball d'aquesta fitxa és **individual**.

## 🎯 Objectius i avaluació

**En acabar aquesta SA podré:**
1. Relacionar el control de dos motoreductors amb el gir del rover (**cinemàtica diferencial**).
2. Programar un comportament autònom de **seguidor de línia**.
3. Programar un comportament autònom d'**evitar obstacles** amb el sensor d'ultrasons.
4. Modelitzar una **trajectòria** senzilla combinant girs i avanços temporitzats.

| Què lliuro | Rúbrica | On compta |
|---|---|---|
| Comportament autònom del rover (producte, S4) | **R1**, **R3** | Projectes (45 %) |
| Repte **⭐** de [Reptes_SA7.md](../../Reptes/Reptes_SA7.md) (nucli obligatori, S4) | **R1** | Projectes (45 %) |
| Mini-defensa breu (S4, R4·DO) | **R4** | Projectes (45 %) |
| Quadern tècnic | **R4** | Quadern tècnic i pràctiques (25 %) |
| Treball a l'aula (autonomia, seguretat amb el rover) | **R5** | Actitud (10 %) |
| Mini-check (S2) | — | **No qualifica** (radar formatiu) |
| Checklist de muntatge (Sessió 0, prèvia) | **R2** | Formativa (no compta a les hores de SA7) |

> 🪜 **Versió nucli (ja és assoliment satisfactori):** el rover avança recte calibrat, segueix una línia **o** evita obstacles de manera fiable, amb el codi organitzat en funcions. **Versió completa:** els dos comportaments integrats en una missió, millores (velocitat variable, marge de seguretat), mini-defensa que explica una decisió pròpia.

> Escala de nota 0-10, rúbriques i tot el sistema: **[Com s'avalua la matèria](../00_General/00_Avaluacio_per_alumnat.md)**.

---

## El que has de fer

### 1 · Cinemàtica diferencial (Sessió 1)

El rover reutilitza les funcions de moviment de la SA4 (`avancar()`, `retrocedir()`, `girar()` i `aturar()`, mateixos pins): cap pin nou. A la SA7, `girar()` guanya un segon paràmetre **opcional** de velocitat (`girar(costat, velocitat=300)`) per als girs suaus del seguidor de línia; les crides a l'estil SA4 (`girar("dreta")`) continuen funcionant igual. Prova [`calibratge_motors.py`](codi/calibratge_motors/calibratge_motors.py) i ajusta `FACTOR_M1`/`FACTOR_M2` fins que el rover vagi recte. Prova una trajectòria en **quadrat** (avança + gira 90° × 4).

**Prediu abans d'executar:** si envies la mateixa velocitat als dos motors i el rover es desvia cap a la dreta, quin motor "guanya"? ______________________

### 2 · Seguidor de línia (Sessió 2)

Sensor **seguidor de línia** KS0050 a P0: lectura amb `read_analog()` i **llindar de detecció** calibrat sobre el teu circuit real. Algorisme de correcció: girar cap al costat on es perd la línia. Prova [`segueix_linia.py`](codi/segueix_linia/segueix_linia.py) sobre el circuit de proves.

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió; no qualifica).** Cicle llegir → decidir → actuar aplicat a un sensor del rover. Banc complet: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

### 3 · Evita-obstacles i «tria un comportament autònom» (Sessió 3)

Sensor d'**ultrasons HC-SR04** (trigger P1, echo P2): mesura de distància amb `mesura_distancia()`, **exactament** el mètode de `alarma_ultrasons.py` (SA3), només amb pins nous. Prova [`evita_obstacles.py`](codi/evita_obstacles/evita_obstacles.py): aturar/girar en detectar un obstacle proper.

**Activitat nucli · lectura robusta amb `try`/`except`.** `mesura_distancia()` pot no trobar mai l'eco (obstacle massa lluny o fora d'abast): a més de comprovar que el valor no sigui negatiu, envolta la crida a `machine.time_pulse_us(...)` amb `try:`/`except OSError:` perquè una lectura puntual dolenta **no aturi tot el programa** del rover. Vegeu la [pàgina de pràctica](codi/evita_obstacles/EXPLICACIO.md#bloc-1b--activitat-nucli-lectura-robusta-amb-tryexcept).

**Repte "tria un comportament autònom":** decideix, segons el material disponible a la teva taula, si tanques **seguidor de línia**, **evita-obstacles**, o tots dos. Aquest repte pot fer de producte de la SA si el docent t'ho indica.

### 4 · Integració: missions del rover (Sessió 4 — producte)

Parteix de [`rover_missions.py`](codi/rover_missions/rover_missions.py) i **integra** el comportament triat amb petites millores (velocitat variable, marge de seguretat). **Producte: comportament autònom del rover** funcional i documentat.

**Mini-defensa (breu, davant el docent, per mostreig — no la fa tothom cada sessió, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md#mostreig-rotatiu-de-la-mini-defensa-repte--sa1-sa8)):** si et toca, explica **una decisió** de disseny (per exemple, per què has triat aquest llindar, o com has integrat els dos sensors). Si no et toca, escriu-ho al quadern.

### 5 · Repte ⭐ (nucli obligatori, mateixa Sessió 4)

Fes el **repte ⭐ · Carret de magatzem amb velocitat variable** de [Reptes_SA7.md](../../Reptes/Reptes_SA7.md) en la seva pròpia franja de 25' de la Sessió 4 (inclou 5' de parella de lectura): és **NUCLI OBLIGATORI**, no una ampliació. **Ensenya'l al docent perquè el validi.**

## Producte · Comportament autònom del rover

Es tanca i s'avalua a la **Sessió 4** amb les rúbriques **R1** (codi, funcionament) i **R3** (autonomia/control). La mini-defensa hi suma **R4**.

## Si t'encalles (DEPURA)
> **D**escriu (què esperaves vs què passa) · **E**xamina (LED, display, lectura del sensor) · **P**rova una hipòtesi cada cop · **U**bica el problema · **R**epara i torna a provar · **A**punta-ho al quadern. Nou aquesta SA: si un sensor "no reacciona com toca", comprova **primer** si el valor llegit al REPL és el que esperaves, abans de sospitar de l'algorisme o dels motors.

<!-- web:only-github -->

## M'autoavaluo (Insuficient · Suficient/Bé · Notable · Excel·lent — la nota és 0-10)
| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Relaciono el gir del rover amb la velocitat/sentit de cada motor | ☐ | ☐ | ☐ | ☐ |
| Programo un seguidor de línia amb llindar calibrat | ☐ | ☐ | ☐ | ☐ |
| Programo un evita-obstacles amb l'HC-SR04 | ☐ | ☐ | ☐ | ☐ |
| Modelitzo una trajectòria combinant girs i avanços | ☐ | ☐ | ☐ | ☐ |

## Quadern tècnic

> 📓 Escriu-ho a la teva entrada del **[quadern tècnic](../00_General/00_Quadern_tecnic.md)** (guia + plantilla; compta el 25 %).
- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com): ___________________________________________________
- **Un error i com l'he resolt:** _____________________________________
- **Els meus llindars i factors** (LLINDAR_LINIA, LLINDAR_OBSTACLE_CM, FACTOR_M1/FACTOR_M2) i per què.

<!-- /web:only-github -->

> 📌 **Vols més?** Ampliació, [reptes ⭐⭐/⭐⭐⭐](../../Reptes/Reptes_SA7.md), pensament computacional, exit ticket i ODS → **[SA7_fitxa_ampliada.md](SA7_fitxa_ampliada.md)**
