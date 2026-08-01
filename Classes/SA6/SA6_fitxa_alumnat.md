# SA6 · Fitxa base — Control: el robot decideix

<!-- web:only-github -->

**Nom:** ______________________  **Data:** __________

<!-- /web:only-github -->

> *"Com fas que un vehicle teledirigit s'aturi SEMPRE que calgui, encara que estigui fent una altra cosa?"* Avui el vehicle deixa de ser un simple receptor d'ordres i es converteix en un **sistema de control**: una **màquina d'estats** amb una **aturada d'emergència prioritària**. Tot el treball d'aquesta fitxa és **individual**.

## 🎯 Objectius i avaluació

**En acabar aquesta SA podré:**
1. Distingir un sistema de **llaç obert** d'un de **llaç tancat** i identificar-ne exemples al vehicle.
2. Implementar una **màquina d'estats finits** senzilla (RUN/STOP/ALERTA) amb condicionals.
3. Programar una **aturada d'emergència** que interromp qualsevol altra acció en curs.
4. Integrar un sensor com a realimentació d'un sistema de control bàsic amb **histèresi**.

| Què lliuro | Rúbrica | On compta |
|---|---|---|
| Repte **«vehicle amb aturada d'emergència»** (producte, S3) | **R1**, **R3** | Projectes (45 %) |
| Repte **⭐** de [Reptes_SA6.md](../../Reptes/Reptes_SA6.md) (nucli obligatori) | **R1** | Projectes (45 %) |
| Mini-defensa breu (S3, R4·DO) | **R4** | Projectes (45 %) |
| Quadern tècnic | **R4** | Quadern tècnic i pràctiques (25 %) |
| Treball a l'aula (seguretat amb el relé, autonomia) | **R5** | Actitud (10 %) |
| Mini-check (S2) | — | **No qualifica** (radar formatiu) |
| Prova pràctica T2 (S4) | R1, R3, R4 | Prova pràctica (20 %) |

> 🪜 **Versió nucli (ja és assoliment satisfactori):** màquina d'estats RUN/STOP funcionant, STOP prioritari activable pel polsador i per una comanda de ràdio, histèresi correcta al termòstat (dos llindars, sense oscil·lació). **Versió completa:** LED indicador d'estat, registre de dades amb `log`, mini-defensa que explica una decisió de disseny de la FSM.

> Escala de nota 0-10, rúbriques i tot el sistema: **[Com s'avalua la matèria](../00_General/00_Avaluacio_per_alumnat.md)**.

---

## El que has de fer

### 1 · Llaç obert, llaç tancat i la primera FSM (Sessió 1)

Distingeix **llaç obert** (una comanda fixa, sense comprovar res) de **llaç tancat** (el sistema llegeix un sensor i hi reacciona). Dissenya el teu **diagrama d'estats** (RUN/STOP/ALERTA) abans d'escriure cap codi. Prova [`maquina_estats_semafor.py`](codi/maquina_estats_semafor/maquina_estats_semafor.py) (una FSM autònoma) i [`termostat_histeresi.py`](codi/termostat_histeresi/termostat_histeresi.py) (llaç tancat amb **histèresi**: dos llindars perquè el relé no faci "clic-clic").

**Prediu abans d'executar:** si un termòstat tingués un **sol** llindar (per exemple, `if temp < 25`), i la temperatura ballés uns dècims al voltant de 25°C, què li passaria al relé? ______________________

### 2 · Aturada d'emergència prioritària (Sessió 2)

Programa l'estat **STOP** com a **prioritari sobre qualsevol altre**: es dispara amb el **polsador manual** del xassís (P12) o amb una **comanda de ràdio dedicada** (`"X"`), i interromp el moviment a l'instant, amb el **LED indicador** (P1) mostrant l'estat. Prova també [`registre_dades.py`](codi/registre_dades/registre_dades.py) (mòdul `log` natiu) per documentar el quadern amb dades reals.

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió; no qualifica).** Detectar i corregir l'oscil·lació d'un termòstat sense histèresi. Banc complet: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

**El meu diagrama d'estats (esbós):**

```
[Aquí el teu diagrama: estats i transicions, amb l'STOP marcat com a prioritari]
```

### 3 · Repte «vehicle amb aturada d'emergència» (Sessió 3 — producte)

Parteix de [`vehicle_seguretat.py`](codi/vehicle_seguretat/vehicle_seguretat.py) i tanca el teu vehicle: protocol de ràdio de la SA5 (F/B/L/R/S) + comanda **`"X"`** dedicada + màquina d'estats RUN/STOP + LED indicador. **Tanca el Projecte T2.**

**Mini-defensa (breu, davant el docent, per mostreig — no la fa tothom cada sessió, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md#mostreig-rotatiu-de-la-mini-defensa-repte--sa1-sa8)):** si et toca, explica **una decisió** de disseny (per exemple, per què el polsador es comprova abans que la ràdio a cada volta del bucle, o com has organitzat `actualitza_estat()`). Si no et toca, escriu-ho al quadern.

### 4 · Repte ⭐ (nucli obligatori) (Sessió 3, en acabar el producte)

Un cop tancat el repte «vehicle amb aturada d'emergència», fes el **repte ⭐** de [`Reptes_SA6.md`](../../Reptes/Reptes_SA6.md) (termòstat de dues zones): és **nucli obligatori** —no una ampliació opcional— i té la seva pròpia franja de 25' a la Sessió 3 (inclou 5' de parella de lectura). Ensenya'l al docent perquè el validi.

## Producte · Repte «vehicle amb aturada d'emergència»

Es tanca i s'avalua a la **Sessió 3** amb les rúbriques **R1** (codi, funcionament) i **R3** (autonomia/control). La mini-defensa hi suma **R4**. **Tanca el Projecte T2**: la Sessió 4 és la prova pràctica T2 individual.

## Si t'encalles (DEPURA)
> **D**escriu (què esperaves vs què passa) · **E**xamina (LED, display, missatge d'error) · **P**rova una hipòtesi cada cop · **U**bica el problema · **R**epara i torna a provar · **A**punta-ho al quadern. Nou aquesta SA: si l'STOP "no sempre" atura el vehicle, comprova **on** dins del bucle es fa la comprovació (ha de ser el **primer** `if`, abans de mirar cap altra entrada).

<!-- web:only-github -->

## M'autoavaluo (Insuficient · Suficient/Bé · Notable · Excel·lent — la nota és 0-10)
| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Distingeixo llaç obert de llaç tancat | ☐ | ☐ | ☐ | ☐ |
| Programo una màquina d'estats amb condicionals | ☐ | ☐ | ☐ | ☐ |
| L'STOP interromp qualsevol moviment, sigui quin sigui l'origen | ☐ | ☐ | ☐ | ☐ |
| Integro un sensor amb histèresi (sense oscil·lació) | ☐ | ☐ | ☐ | ☐ |

## Quadern tècnic

> 📓 Escriu-ho a la teva entrada del **[quadern tècnic](../00_General/00_Quadern_tecnic.md)** (guia + plantilla; compta el 25 %).
- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com): ___________________________________________________
- **Un error i com l'he resolt:** _____________________________________
- **El meu diagrama d'estats final** (còpia'l de dalt si cal).

<!-- /web:only-github -->

> 📌 **Vols més?** Ampliació, [reptes ⭐⭐/⭐⭐⭐](../../Reptes/Reptes_SA6.md), pensament computacional, exit ticket i ODS → **[SA6_fitxa_ampliada.md](SA6_fitxa_ampliada.md)**
