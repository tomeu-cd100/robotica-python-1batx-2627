# SA1 · Fitxa base — Hola, robot!

<!-- web:only-github -->

**Nom:** ______________________  **Data:** __________

<!-- /web:only-github -->

> Descobriràs què és un robot i un sistema embegut, coneixeràs la placa micro:bit i faràs el teu primer programa. Tot el treball d'aquesta fitxa és **individual**.

## 🎯 Objectius i avaluació

**En acabar aquesta SA podré:**
1. Analitzar qualsevol sistema automàtic amb el model **entrada → procés → sortida**.
2. Reconèixer les parts de la micro:bit i distingir **digital** d'**analògic**.
3. **Predir, llegir i modificar** un programa MicroPython senzill.
4. Treballar amb **seguretat** i portar el **quadern tècnic** al dia.

| Què lliuro | Rúbrica | On compta |
|---|---|---|
| **Fitxa-pòster** d'un robot real (amb dilema ètic) | **R4** | Projectes (45 %) |
| Repte **⭐** de [Reptes_SA1.md](../../Reptes/Reptes_SA1.md) (nucli obligatori) | **R1** | Projectes (45 %) |
| **Quadern tècnic** (primera entrada) | **R4** | Quadern tècnic i pràctiques (25 %) |
| Treball a l'aula (seguretat, autonomia) | **R5** | Actitud (10 %) |
| Prova diagnòstica | — | **No qualifica** (orienta el ritme de la SA) |

> 🪜 **Versió nucli (ja és assoliment satisfactori):** pòster amb entrada → procés → sortida ben identificades i el dilema ètic plantejat. **Versió completa:** sensors i actuadors concrets, alternatives de disseny i dilema argumentat amb pros i contres.

> Escala de nota 0-10, rúbriques i tot el sistema: **[Com s'avalua la matèria](../00_General/00_Avaluacio_per_alumnat.md)**.

---

## El que has de fer

### 1 · Entrada – Procés – Sortida

Completa: què *percep* (entrada), què *decideix* (procés) i què *fa* (sortida).

| Sistema | Entrada (sensors) | Procés (decisió) | Sortida (actuadors) |
|---|---|---|---|
| Rentadora | | | |
| Dron | | | |
| Semàfor | | | |

### 2 · La placa micro:bit

Etiqueta a l'**esquema de la placa** ([`SA1_esquemes_connexions.md`](SA1_esquemes_connexions.md)): microcontrolador · matriu de 25 LED · botons A i B · pins d'expansió · connector USB · sensors interns (acceleròmetre, brúixola, llum, temperatura).

**Digital vs analògic:** quina diferència hi ha? Posa'n un exemple de cada. ______________________
> *Digital* = dos estats (per exemple, un botó premut o no premut); *analògic* = molts valors intermedis (com el nivell de llum, de 0 a 255).

### 3 · Normes de seguretat

Llegeix [`SA1_normes_seguretat.md`](SA1_normes_seguretat.md) i **signa** el full. Les 2 normes que et semblen més importants:
1. ___________________________________   2. ___________________________________

### 4 · El teu primer programa (PRIMM)

0. **PREDIU** (sense executar-lo encara): mira `hola_mon.py` — què creus que farà el display? ______________________
1. **EXECUTA**: prova'l al simulador o a la placa i observa. Coincideix amb la teva predicció? **Sí / No** — què has vist de diferent? ______________________
2. **Investiga** `hola_mon.py`: quina és la primera línia i per què cal sempre? ______ què fa `display.scroll(...)`? ______ què fa `display.show(...)`? ______
3. **Modifica** el text que es desplaça i la imatge que es mostra. Què has posat? ______
4. **Crea**: obre `emocions_botons.py` i fes que els botons A i B mostrin dues cares diferents al display.

> 💡 Si t'encalles escrivint el teu programa, parteix de l'**esquelet** de la secció «Si t'encalles» de la [pàgina de la pràctica d'`emocions_botons`](codi/emocions_botons/EXPLICACIO.md): l'estructura `while True:` i el `from microbit import *` ja hi són; tu omples els `# TODO`.

### 5 · Repte ⭐ (nucli obligatori)

Fes el **repte ⭐ · Targeta de benvinguda digital** de [`Reptes_SA1.md`](../../Reptes/Reptes_SA1.md) en la seva pròpia franja de 25' a la Sessió 3, després de la fase «Crea» (inclou 5' de parella de lectura): parteix de `hola_mon.py` perquè el display mostri el teu **nom** (`scroll`) i, després, una **imatge fixa** que et representi (`show`). És **nucli obligatori** — forma part del producte d'aquesta SA, no és una ampliació. Quan l'acabis, **ensenya'l al docent** perquè el validi.

## Producte · Fitxa-pòster

Tria un **robot real** i analitza'l amb [`SA1_poster_robot_plantilla.md`](SA1_poster_robot_plantilla.md) (entrada-procés-sortida + dilema ètic). Es **comença a la sessió 3**, després de l'Activitat 4, i s'avalua amb la rúbrica **R4**.

## Si t'encalles (DEPURA)
> **D**escriu (què esperaves vs què passa) · **E**xamina (display, missatge d'error) · **P**rova una hipòtesi cada cop · **U**bica el problema · **R**epara i torna a provar · **A**punta-ho al quadern. Si demanes ajuda, explica **què ja has provat**.

<!-- web:only-github -->

## M'autoavaluo (Insuficient · Suficient/Bé · Notable · Excel·lent — la nota és 0-10)
| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Identifico entrada-procés-sortida d'un sistema | ☐ | ☐ | ☐ | ☐ |
| Reconec les parts de la placa i distingeixo digital/analògic | ☐ | ☐ | ☐ | ☐ |
| Llegeixo i modifico codi MicroPython senzill | ☐ | ☐ | ☐ | ☐ |

## Quadern tècnic

> 📓 Escriu-ho a la teva entrada del **[quadern tècnic](../00_General/00_Quadern_tecnic.md)** (guia + plantilla; compta el 25 %).
- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com): ___________________________________________________
- **Un error i com l'he resolt:** _____________________________________

<!-- /web:only-github -->

> 📌 **Vols més?** Ampliació (`dau_sacseig`), [reptes ⭐⭐/⭐⭐⭐](../../Reptes/Reptes_SA1.md), pensament computacional, exit ticket i ODS → **[SA1_fitxa_ampliada.md](SA1_fitxa_ampliada.md)**
