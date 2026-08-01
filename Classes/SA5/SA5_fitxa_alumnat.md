# SA5 · Fitxa base — Ràdio: robots que parlen

<!-- web:only-github -->

**Nom:** ______________________  **Data:** __________

<!-- /web:only-github -->

> Avui dues plaques es **parlen** sense fils: dissenyaràs el teu propi **protocol** de comandes i el faràs servir per controlar el vehicle a distància. Tot el treball d'aquesta fitxa és **individual**: provar la ràdio necessita dues plaques, així que t'aparelles **puntualment** (banc de proves) amb la placa d'un company del teu grup de ràdio, però el codi que lliures i que s'avalua és sempre el **teu**.

## 🎯 Objectius i avaluació

**En acabar aquesta SA podré:**
1. Configurar la **ràdio** de la micro:bit (`radio.on()`, grup/canal) i enviar/rebre missatges de text entre dues plaques.
2. Dissenyar un **protocol de missatges** propi (comandes curtes) per controlar el vehicle a distància.
3. Emmagatzemar comandes o missatges rebuts en **llistes** o **tuples** bàsiques.
4. Relacionar la recepció d'un missatge amb una funció de moviment ja creada a la SA4 (esdeveniment → acció).

| Què lliuro | Rúbrica | On compta |
|---|---|---|
| Repte **«control remot bàsic»** (producte, S3) | **R1** | Projectes (45 %) |
| Repte **⭐** de [Reptes_SA5.md](../../Reptes/Reptes_SA5.md) (nucli obligatori) | **R1** | Projectes (45 %) |
| Mini-defensa breu (S3, R4·DO) | **R4** | Projectes (45 %) |
| Quadern tècnic | **R4** | Quadern tècnic i pràctiques (25 %) |
| Treball a l'aula (individualitat de la ràdio, autonomia) | **R5** | Actitud (10 %) |
| Mini-check (S2) | — | **No qualifica** (radar formatiu) |

> 🪜 **Versió nucli (ja és assoliment satisfactori):** ràdio configurada amb el grup assignat, enviament/recepció de missatges funcionant, un protocol de 4 comandes que mou el vehicle correctament. **Versió completa:** protocol propi ben documentat, historial de comandes amb llista o tupla, mini-defensa que explica una decisió de disseny del protocol.

> Escala de nota 0-10, rúbriques i tot el sistema: **[Com s'avalua la matèria](../00_General/00_Avaluacio_per_alumnat.md)**.

---

## El que has de fer

### 1 · Xat per ràdio (Sessió 1)

Activa la ràdio amb el **grup** que t'assigni el docent i prova [`radio_missatges.py`](codi/radio_missatges/radio_missatges.py), aparellat puntualment amb un company del teu grup.

**Prediu abans d'executar:** si dues plaques tenen **grups diferents**, es rebran els missatges l'una a l'altra? ______________________

**Activitat nucli · `for` sobre una llista.** El programa guarda els missatges rebuts a la llista `historic`. Prem **A+B alhora**: `mostra_historic()` els recorre TOTS amb `for missatge in historic:` (un `for` que agafa els **elements** de la llista directament, no un índex). Envia't 3-4 missatges de prova i comprova que els veus tots, en ordre.

### 2 · Un protocol propi de comandes (Sessió 2)

Dissenya **4-5 comandes pròpies** (per exemple `F`, `B`, `L`, `R`, `S`) amb un prefix (per exemple `"CMD:"`) i programa [`comandament.py`](codi/comandament/comandament.py). Connecta la recepció amb les funcions `avancar()`/`girar()`/`aturar()` de la SA4.

**La meva taula de comandes:**

| Comanda | Acció |
|---|---|
| | |
| | |
| | |
| | |

> 🎯 **Mini-check individual (10', al final d'aquesta sessió, combinat amb el tancament; no qualifica).** Enviar/rebre un missatge i actuar-hi sense apunts. Banc complet: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

### 3 · Repte «control remot bàsic» (Sessió 3 — producte)

Parteix de [`receptor_vehicle.py`](codi/receptor_vehicle/receptor_vehicle.py) i tanca el teu vehicle controlat per ràdio amb el **teu** protocol.

**Mini-defensa (breu, davant el docent, per mostreig — no la fa tothom cada sessió, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md#mostreig-rotatiu-de-la-mini-defensa-repte--sa1-sa8)):** si et toca, explica **quin protocol** has dissenyat i **una decisió** (per exemple, per què has triat aquestes comandes o aquesta manera de guardar l'historial). Si no et toca, escriu-ho al quadern.

### 4 · Repte ⭐ (nucli obligatori) (Sessió 3, en acabar el producte)

Un cop tancat el repte «control remot bàsic», fes el **repte ⭐** de [`Reptes_SA5.md`](../../Reptes/Reptes_SA5.md) (xat de classe amb identificació): és **nucli obligatori** —no una ampliació opcional— i té la seva pròpia franja de 25' a la Sessió 3 (inclou 5' de parella de lectura). Ensenya'l al docent perquè el validi.

## Producte · Repte «control remot bàsic»

Es tanca i s'avalua a la **Sessió 3** amb la rúbrica **R1** (codi, funcionament). La mini-defensa hi suma **R4**.

## Si t'encalles (DEPURA)
> **D**escriu (què esperaves vs què passa) · **E**xamina (LED, display, missatge d'error) · **P**rova una hipòtesi cada cop · **U**bica el problema · **R**epara i torna a provar · **A**punta-ho al quadern. Nou aquesta SA: si un missatge "no arriba", comprova **cada extrem per separat** (l'emissor envia realment el que creus? el receptor rep algun missatge, encara que no faci res amb ell?) abans de sospitar de tot el protocol.

<!-- web:only-github -->

## M'autoavaluo (Insuficient · Suficient/Bé · Notable · Excel·lent — la nota és 0-10)
| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Configuro la ràdio (grup, enviar, rebre) | ☐ | ☐ | ☐ | ☐ |
| Dissenyo i documento un protocol de comandes propi | ☐ | ☐ | ☐ | ☐ |
| Connecto la recepció d'un missatge a una funció de moviment | ☐ | ☐ | ☐ | ☐ |

## Quadern tècnic

> 📓 Escriu-ho a la teva entrada del **[quadern tècnic](../00_General/00_Quadern_tecnic.md)** (guia + plantilla; compta el 25 %).
- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com): ___________________________________________________
- **Un error i com l'he resolt:** _____________________________________
- **La meva taula de comandes** (comanda → acció, còpia-la de dalt si cal).

<!-- /web:only-github -->

> 📌 **Vols més?** Ampliació, [reptes ⭐⭐/⭐⭐⭐](../../Reptes/Reptes_SA5.md), pensament computacional, exit ticket i ODS → **[SA5_fitxa_ampliada.md](SA5_fitxa_ampliada.md)**
