# SA3 · Fitxa base — Entrades: el robot percep

<!-- web:only-github -->

**Nom:** ______________________  **Data:** __________

<!-- /web:only-github -->

> Faràs que la micro:bit **percebi** el món: botons, llum, temperatura, distància, presència i so. Acabaràs programant la **mascota reactiva** i **tancant el Projecte T1**. Tot el treball d'aquesta fitxa és **individual**.

## 🎯 Objectius i avaluació

**En acabar aquesta SA podré:**
1. Llegir entrades **digitals** (botons, polsador) i **analògiques** (potenciòmetre, llum, temperatura) i interpretar-ne els valors.
2. Aplicar **condicionals** (`if/elif/else`) per relacionar un sensor amb una acció.
3. Fer servir el **REPL** per depurar i visualitzar dades de sensors en directe.
4. Programar la **mascota reactiva**: reaccions de la matriu LED/so davant estímuls de l'entorn.

| Què lliuro | Rúbrica | On compta |
|---|---|---|
| Repte **«mascota reactiva»** (producte, S3 — tanca T1) | **R1**, **R2**, **R3** | Projectes (45 %) |
| Mini-defensa breu (S3, R4·DO) | **R4** | Projectes (45 %) |
| Quadern tècnic | **R4** | Quadern tècnic i pràctiques (25 %) |
| Treball a l'aula (seguretat, autonomia) | **R5** | Actitud (10 %) |
| Mini-check (S2) | — | **No qualifica** (radar formatiu) |
| **Prova pràctica T1** (S4, individual) | R1, R2, R4 | Segons `06_Avaluacio_criteris_qualificacio.md` |

> 🪜 **Versió nucli (ja és assoliment satisfactori):** mascota amb **2 reaccions** sensor→resposta (cara + so), llindars calibrats amb el REPL, funciona de manera fiable. **Versió completa:** ≥3 reaccions coherents, antirebot al polsador, mini-defensa que justifica el llindar/l'ordre de prioritat triat.

> Escala de nota 0-10, rúbriques i tot el sistema: **[Com s'avalua la matèria](../00_General/00_Avaluacio_per_alumnat.md)**.

---

## El que has de fer

### 1 · Entrades digitals i condicionals (Sessió 1)

Munta el polsador extern ([esquema](SA3_esquemes_connexions.md)) i escriu al **REPL** un comptador de premudes amb `if/elif/else`, com a la classe.

**Prediu abans d'executar:** si premis el polsador ràpid 3 cops seguits sense antirebot, el comptador pujarà exactament 3? ______________________

### 2 · Entrades analògiques: llum i temperatura (Sessió 2)

Munta el sensor de llum i el de temperatura del Kit ([esquema](SA3_esquemes_connexions.md)). Parteix de `nivell_llum.py` i `termometre.py`.

**El teu llindar de foscor (`LLINDAR_FOSCOR`):** ______  → mesurat amb el REPL a: ______________________

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió; no qualifica).** Banc complet: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md#sa3--mini-check-inici-de-la-sessió-2).

### 3 · Repte «mascota reactiva» (Sessió 3 — producte, tanca la mascota T1)

Cablega la mascota amb el cablatge **exacte** del [dossier del Projecte T1](../00_General/00_Projecte_T1_Mascota.md): P1 (LED), P2 (brunzidor), P8 (PIR), P12 (polsador). Parteix de `mascota_reactiva.py` i programa **almenys 2 reaccions** sensor→resposta coherents amb el nom/caràcter que li has triat.

> 💡 Si t'encalles, parteix de l'**esquelet** del [dossier de la mascota](../00_General/00_Projecte_T1_Mascota.md#-si-tencalles-lesquelet-del-programa).

**Mini-defensa (breu, davant el docent):** explica **quines reaccions** té la teva mascota i **una decisió** que hagis pres (per exemple, per què aquest llindar o aquest ordre de prioritat).

## Producte · Repte «mascota reactiva» (tanca el Projecte T1)

Es tanca i s'avalua a la **Sessió 3** amb les rúbriques **R1** (codi), **R2** (muntatge) i **R3** (compliment del repte). La mini-defensa hi suma **R4**.

## Sessió 4 · Prova pràctica T1

La Sessió 4 és **sencera** la prova pràctica individual del 1r trimestre. Enunciat i criteris: [`Avaluació/Prova_practica_T1.md`](../../Avaluació/Prova_practica_T1.md).

## Si t'encalles (DEPURA)
> **D**escriu (què esperaves vs què passa) · **E**xamina (LED, display, missatge d'error) · **P**rova una hipòtesi cada cop · **U**bica el problema · **R**epara i torna a provar · **A**punta-ho al quadern. Nou aquesta SA: **mesura sempre amb el REPL** el valor real d'un sensor abans de triar un llindar.

<!-- web:only-github -->

## M'autoavaluo (Insuficient · Suficient/Bé · Notable · Excel·lent — la nota és 0-10)
| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Llegeixo entrades digitals amb condicionals | ☐ | ☐ | ☐ | ☐ |
| Llegeixo i interpreto entrades analògiques | ☐ | ☐ | ☐ | ☐ |
| Munto sensors al Micro:shield amb seguretat | ☐ | ☐ | ☐ | ☐ |

## Quadern tècnic

> 📓 Escriu-ho a la teva entrada del **[quadern tècnic](../00_General/00_Quadern_tecnic.md)** (guia + plantilla; compta el 25 %).
- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com): ___________________________________________________
- **Un error i com l'he resolt:** _____________________________________
- **Mascota (tancament):** reaccions finals i llindars triats.

<!-- /web:only-github -->

> 📌 **Vols més?** Ampliació, [reptes ⭐](../../Reptes/Reptes_SA3.md), pensament computacional, exit ticket i ODS → **[SA3_fitxa_ampliada.md](SA3_fitxa_ampliada.md)**
