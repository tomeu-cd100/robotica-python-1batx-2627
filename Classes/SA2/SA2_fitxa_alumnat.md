# SA2 · Fitxa base — Sortides: el robot actua

<!-- web:only-github -->

**Nom:** ______________________  **Data:** __________

<!-- /web:only-github -->

> **Per què ara el Micro:shield?** A la SA1 vas fer aparèixer text i imatges al **display** (una sortida senzilla, integrada a la placa) i vas reaccionar a botons. Ara connectaràs el **Micro:shield** i faràs que la micro:bit **actuï sobre el món exterior**: LED, LED RGB, brunzidor i relé. És el mateix salt que fa un sistema embegut real (SA1): passar de mostrar informació a **actuar-hi a sobre**.

> Connectaràs el Micro:shield i faràs que la micro:bit **actuï** sobre components externs: LED, LED RGB, brunzidor i relé. Acabaràs muntant la **mascota** del fil conductor. Tot el treball d'aquesta fitxa és **individual**.

> 🔎 Veuràs `def` en algun exemple o repte d'ampliació: de moment les **funcions** només les **llegim** (per entendre-les), no cal saber escriure-les encara — les aprendrem a la **SA4**.

## 🎯 Objectius i avaluació

**En acabar aquesta SA podré:**
1. Escriure programes amb **variables i bucles** per controlar sortides repetitives.
2. Connectar i controlar **sortides digitals i PWM** (LED, LED RGB, brunzidor, relé) amb seguretat.
3. Programar animacions i sons combinant matriu LED i altaveu.
4. Muntar físicament la **mascota** del fil conductor.

| Què lliuro | Rúbrica | On compta |
|---|---|---|
| Repte **«semàfor o llum d'ambient»** (producte, S3) | **R1**, **R2** | Projectes (45 %) |
| Mini-defensa oral (S3, R4·DO) | **R4** | Projectes (45 %) |
| Muntatge de la **mascota** (S4) | **R2** | Projectes (45 %) |
| Repte **⭐** de [Reptes_SA2.md](../../Reptes/Reptes_SA2.md) (nucli obligatori) | **R1** | Projectes (45 %) |
| Quadern tècnic | **R4** | Quadern tècnic i pràctiques (25 %) |
| Treball a l'aula (seguretat, autonomia) | **R5** | Actitud (10 %) |
| Mini-check (S2) | — | **No qualifica** (radar formatiu) |

> 🪜 **Versió nucli (ja és assoliment satisfactori):** semàfor amb 3 fases (verd/ambre/vermell), temps en variables, funciona de manera fiable. **Versió completa:** + relé commutant un circuit extern + avís sonor + mini-defensa amb una decisió tècnica justificada.

> Escala de nota 0-10, rúbriques i tot el sistema: **[Com s'avalua la matèria](../00_General/00_Avaluacio_per_alumnat.md)**.

---

## El que has de fer

### 1 · Sortida digital amb bucles (Sessió 1)

Munta el LED extern al pin **P1** ([esquema](SA2_esquemes_connexions.md)) i parteix de `led_parpelleig.py`: fes-lo parpellejar i comptar quants cops ho ha fet.

**Prediu abans d'executar:** quant de temps estarà encès el LED cada cicle? ______________________

### 2 · Sortides PWM i so (Sessió 2)

Munta el LED RGB (P8/P12/P16) i el brunzidor (P2). Parteix de `pwm_led_rgb.py` i `musica_altaveu.py`.

**El teu color propi (R, G, B):** ______ , ______ , ______  → quin color surt? ______________________

**Mini-animació (matriu LED + so):** encadena 2-3 `display.show(Image.___)` amb un `sleep()` entre cada un i un so diferent de `musica_altaveu.py` per a cada imatge (per exemple: `Image.HAPPY` + to agut, `Image.SAD` + to greu). No cal desar-ho com a fitxer a part: prova-ho al REPL o afegeix-ho temporalment al final de `pwm_led_rgb.py`.

**Modifica el `for` de `respira()`:** a `pwm_led_rgb.py`, `respira()` fa servir `range(0, 1024, 32)` per pujar la intensitat. Canvia el **pas** a `range(0, 1024, 8)` i torna a provar-ho: quants passos calen ara per arribar a 1023 (aproximadament)? La rampa es veu més suau o més brusca? ______________________

> 🔎 Pista: `range(inici, final, pas)` és una de les **tres formes** de `range` (les altres són `range(n)` i `range(inici, final)`); vegeu la [pàgina de pràctica de `pwm_led_rgb`](codi/pwm_led_rgb/EXPLICACIO.md#bloc-2--el-mecanisme-del-for-recórrer-una-seqüència-de-números-amb-range).

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió; no qualifica).** Banc complet: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md#sa2--mini-check-inici-de-la-sessió-2).

### 3 · Repte «semàfor o llum d'ambient» (Sessió 3 — producte)

Munta el semàfor complet (LED verd/ambre/vermell + brunzidor + relé, [esquema](SA2_esquemes_connexions.md)) i escriu el programa: 3 fases amb temps en variables, avís sonor a l'ambre, relé commutant un circuit extern al vermell.

> 💡 Si t'encalles, parteix de l'**esquelet** de la secció «Si t'encalles» de la [pàgina de la pràctica de `semafor_rele`](codi/semafor_rele/EXPLICACIO.md).

**Mini-defensa (1', davant el docent, per mostreig — no la fa tothom cada sessió, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md#mostreig-rotatiu-de-la-mini-defensa-repte--sa1-sa8)):** si et toca, explica **què fa** el teu semàfor i **una decisió** que hagis pres (per exemple, per què aquest ordre o aquests temps). Si no et toca aquesta sessió, escriu la mateixa resposta al quadern.

### 4 · Repte ⭐ (nucli obligatori, un cop tancat el semàfor)

Fes el **repte ⭐ · Llum de seguretat per a motxilla** de [`Reptes_SA2.md`](../../Reptes/Reptes_SA2.md), en la seva pròpia franja de 25' (Sessió 3, un cop tancat el semàfor; inclou 5' de parella de lectura): amplia `led_parpelleig.py` (el LED de P1 que ja tens muntat des de la Sessió 1 — el mateix que muntaràs dins la mascota a la S4) perquè, mentre el **botó A** està premut, parpellegi **més ràpid** ("mode alerta"); sense prémer'l, parpelleja al ritme normal. És **nucli obligatori** — forma part del producte d'aquesta SA, no és una ampliació. Quan l'acabis, **ensenya'l al docent** perquè el validi.

### 5 · Muntatge de la mascota (Sessió 4)

Segueix el dossier [`00_Projecte_T1_Mascota.md`](../00_General/00_Projecte_T1_Mascota.md): munta la carcassa, cablega el LED (P1) i el brunzidor amb el codi que ja tens fet (`led_parpelleig.py`, `musica_altaveu.py`), i deixa el servo muntat (es programarà a la SA4).

## Producte · Repte «semàfor o llum d'ambient»

Es tanca i s'avalua a la **Sessió 3** amb les rúbriques **R1** (codi) i **R2** (muntatge). La mini-defensa hi suma **R4**.

## Si t'encalles (DEPURA)
> **D**escriu (què esperaves vs què passa) · **E**xamina (LED, display, missatge d'error) · **P**rova una hipòtesi cada cop · **U**bica el problema · **R**epara i torna a provar · **A**punta-ho al quadern. Nou aquesta SA: **mesura** amb el REPL el valor real que envies a un pin abans de sospitar del component.

<!-- web:only-github -->

## M'autoavaluo (Insuficient · Suficient/Bé · Notable · Excel·lent — la nota és 0-10)
| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Controlo sortides digitals amb bucles | ☐ | ☐ | ☐ | ☐ |
| Controlo sortides PWM (LED, LED RGB, so) | ☐ | ☐ | ☐ | ☐ |
| Munto components al Micro:shield amb seguretat | ☐ | ☐ | ☐ | ☐ |

## Quadern tècnic

> 📓 Escriu-ho a la teva entrada del **[quadern tècnic](../00_General/00_Quadern_tecnic.md)** (guia + plantilla; compta el 25 %).
- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com): ___________________________________________________
- **Un error i com l'he resolt:** _____________________________________
- **Mascota (S4):** com ha anat el muntatge i què falta per a la SA3.

<!-- /web:only-github -->

> 📌 **Vols més?** Ampliació, [reptes ⭐⭐/⭐⭐⭐](../../Reptes/Reptes_SA2.md), pensament computacional, exit ticket i ODS → **[SA2_fitxa_ampliada.md](SA2_fitxa_ampliada.md)**
