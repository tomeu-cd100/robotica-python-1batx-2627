# SA4 · Fitxa base — Funcions i moviment

<!-- web:only-github -->

**Nom:** ______________________  **Data:** __________

<!-- /web:only-github -->

> Avui poses **nom** al concepte de **funció** (ja n'havies escrit sense saber-ho a la SA2/SA3) i el fas servir per moure un servomotor i dos motoreductors: acabaràs muntant el **vehicle** del fil conductor. Tot el treball d'aquesta fitxa és **individual**.

## 🎯 Objectius i avaluació

**En acabar aquesta SA podré:**
1. Definir i cridar **funcions** amb paràmetres i valor de retorn per modularitzar el codi.
2. Controlar un **servomotor** (angle) i un **motoreductor** (sentit i velocitat) des del Micro:shield.
3. Encapsular moviments bàsics (avançar, girar, aturar) en funcions reutilitzables.
4. Muntar físicament el **vehicle** del fil conductor a partir de peces pretallades.

| Què lliuro | Rúbrica | On compta |
|---|---|---|
| Repte **«control per botons»** (producte, S3) | **R1**, **R2** | Projectes (45 %) |
| Mini-defensa breu (S3, R4·DO) | **R4** | Projectes (45 %) |
| Muntatge del vehicle T2 (S4) | **R2** | Projectes (45 %) |
| Quadern tècnic | **R4** | Quadern tècnic i pràctiques (25 %) |
| Treball a l'aula (seguretat, autonomia) | **R5** | Actitud (10 %) |
| Mini-check (S2) | — | **No qualifica** (radar formatiu) |

> 🪜 **Versió nucli (ja és assoliment satisfactori):** funcions `avancar`/`retrocedir`/`girar`/`aturar` funcionant, seqüència de 3-4 passos activada amb els botons A/B, vehicle muntat i cablejat segons l'esquema. **Versió completa:** seqüència pròpia ben justificada, mini-defensa que explica una decisió de disseny, vehicle amb prova de moviment fiable a la primera.

> Escala de nota 0-10, rúbriques i tot el sistema: **[Com s'avalua la matèria](../00_General/00_Avaluacio_per_alumnat.md)**.

---

## El que has de fer

### 1 · Funcions amb paràmetres i valor de retorn (Sessió 1)

Programa el servo de la mascota ([esquema](SA4_esquemes_connexions.md), pin **P0**) partint de [`funcions_moviments.py`](codi/funcions_moviments/funcions_moviments.py).

**Prediu abans d'executar:** `graus_a_pwm(angle)` **mou** el servo, o **només calcula** un número? ______________________

### 2 · Funcions de moviment del motoreductor (Sessió 2)

Munta els dos motoreductors ([esquema](SA4_esquemes_connexions.md), pins **M1**/**M2**, alimentació externa). Parteix de [`velocitat_pwm.py`](codi/velocitat_pwm/velocitat_pwm.py): `avancar(velocitat)`, `retrocedir(velocitat)`, `girar(costat)`, `aturar()`.

**Comenta cada paràmetre** de les teves funcions de moviment (per exemple, `# velocitat: 0-1023, com mes alt mes rapid`): ______________________

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió; no qualifica).** Escriu una funció amb paràmetre sense apunts. Banc complet: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

### 3 · Repte «control per botons» (Sessió 3 — producte)

Parteix de [`control_per_botons.py`](codi/control_per_botons/control_per_botons.py) i programa la **teva** seqüència de moviments (avançar/girar/retrocedir/aturar) activada amb els botons A/B.

**Mini-defensa (breu, davant el docent):** explica **quina seqüència** has triat i **una decisió** de disseny (per exemple, per què aquest ordre de moviments o aquesta velocitat).

## Producte · Repte «control per botons»

Es tanca i s'avalua a la **Sessió 3** amb les rúbriques **R1** (codi, modularitat) i **R2**. La mini-defensa hi suma **R4**.

## Sessió 4 · Muntatge del vehicle T2

Fabricació i muntatge físic segons el [dossier del vehicle T2](../00_General/00_Projecte_T2_Vehicle.md): xassís, motoreductors i roda boja, micro:bit + Micro:shield i portapiles, cablatge **exacte** dels pins fixats a la Sessió 2. Fes la prova d'encesa amb `velocitat_pwm.py` o `control_per_botons.py` abans de donar el muntatge per acabat.

## Si t'encalles (DEPURA)
> **D**escriu (què esperaves vs què passa) · **E**xamina (LED, display, missatge d'error) · **P**rova una hipòtesi cada cop · **U**bica el problema · **R**epara i torna a provar · **A**punta-ho al quadern. Nou aquesta SA: si una funció no fa el que esperes, **prova-la sola al REPL** amb valors coneguts abans de buscar l'error en un programa més gran.

<!-- web:only-github -->

## M'autoavaluo (Insuficient · Suficient/Bé · Notable · Excel·lent — la nota és 0-10)
| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Defineixo i crido funcions amb paràmetres i valor de retorn | ☐ | ☐ | ☐ | ☐ |
| Controlo un servomotor i un motoreductor amb PWM | ☐ | ☐ | ☐ | ☐ |
| Munto el vehicle amb seguretat, cablatge segons l'esquema | ☐ | ☐ | ☐ | ☐ |

## Quadern tècnic

> 📓 Escriu-ho a la teva entrada del **[quadern tècnic](../00_General/00_Quadern_tecnic.md)** (guia + plantilla; compta el 25 %).
- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com): ___________________________________________________
- **Un error i com l'he resolt:** _____________________________________
- **Muntatge del vehicle:** com ha anat, quines dificultats mecàniques hi ha hagut.

<!-- /web:only-github -->

> 📌 **Vols més?** Ampliació, [reptes ⭐](../../Reptes/Reptes_SA4.md), pensament computacional, exit ticket i ODS → **[SA4_fitxa_ampliada.md](SA4_fitxa_ampliada.md)**
