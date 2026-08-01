# SA9 · Fitxa base — Repte final integrador

<!-- web:only-github -->

**Nom:** ______________________  **Data:** __________

<!-- /web:only-github -->

> *"Quin problema real i senzill del teu entorn pots resoldre ampliant el teu rover?"* Aquest és el **projecte de síntesi** del curs: tries un repte lliure, l'integres al teu rover (SA7-SA8), el documentes i el defenses tu sol/a. Tot el treball d'aquesta fitxa és **individual**.

## 🎯 Objectius i avaluació

**En acabar aquesta SA podré:**
1. Gestionar, individualment, un **projecte** complet (anàlisi → prototip → proves → millora).
2. **Integrar** electrònica, programació, control, robòtica mòbil i telemetria en una solució coherent i pròpia.
3. Elaborar un **dossier tècnic** complet i fer-ne una **defensa oral individual**.
4. Valorar l'impacte ètic, social i ambiental de la meva solució (ODS) i treballar amb autonomia.

| Què lliuro | Rúbrica | On compta |
|---|---|---|
| Rover ampliat amb el repte lliure (producte, S4) | **R1, R2, R3** | Projectes (45 %) |
| Dossier tècnic (S4) | **R4** | Quadern tècnic i pràctiques (25 %) |
| Defensa oral individual, nivell alt (S4, R4·DO) | **R4** | Projectes (45 %) |
| Treball a l'aula (autonomia, gestió de l'error, responsabilitat) | **R5** | Actitud (10 %) |
| Mini-check (S2) | — | **No qualifica** (radar formatiu) |
| Prova pràctica T3 (S5, individual) | — | Proves pràctiques (20 %); **no** reavalua el projecte |

> 🪜 **Versió nucli (ja és assoliment satisfactori):** un repte del [banc](SA9_reptes_proposats.md) amb el seu criteri ⭐ complert, dossier amb les 9 seccions omplertes i defensa amb els 3 indicadors al nivell «Suficient/Notable». **Versió completa:** criteri ⭐⭐/⭐⭐⭐ del repte, iteració documentada, defensa amb decisions justificades i alternatives descartades.

> Escala de nota 0-10, rúbriques i tot el sistema: **[Com s'avalua la matèria](../00_General/00_Avaluacio_per_alumnat.md)**.

---

## El que has de fer

### 1 · Idear (Sessió 1)

Tria el teu **repte lliure** al [banc de reptes](SA9_reptes_proposats.md) (o proposa'n un altre de coherent, validat pel docent). Defineix els **requisits mínims** (què ha de fer com a mínim el sistema) i fes un **esbós** de la solució (dibuix o descripció).

**Planificació:** llista, per a cada sessió que et queda (S2, S3, S4), què hi vols tenir fet.

| Sessió | Què vull tenir fet |
|---|---|
| S2 | |
| S3 | |
| S4 | |

### 2 · Prototipar (Sessió 2)

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió; no qualifica).** Integrar sensor + condicional + ràdio en una sola funció pròpia, sense apunts. Banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

Munta i programa un **prototip mínim viable**: parteix de la [plantilla de projecte](codi/plantilla_projecte/plantilla_projecte.py) i integra-hi almenys **un element nou** (sensor, actuador o comunicació) sobre el que ja tenies a SA7-SA8. Consulta el [banc de reptes](SA9_reptes_proposats.md) per al maquinari i l'esquema de components del teu repte.

### 3 · Provar i millorar (Sessió 3)

Prova el sistema, identifica errors (rutina **DEPURA**) i fes una **primera iteració de millora**, documentada. Avança el [dossier tècnic](SA9_dossier_plantilla.md) (§1-§3: objectiu, disseny, esquema de connexions).

> 🎤 **Defenses esglaonades.** Si el docent ho anuncia (grups nombrosos), qui ja tingui el prototip llest pot fer la seva defensa oral individual avui mateix, en lloc d'esperar a la S4.

### 4 · Comunicar (Sessió 4)

**Tanca el dossier tècnic** (totes les 9 seccions de [`SA9_dossier_plantilla.md`](SA9_dossier_plantilla.md)) i fes la teva **defensa oral individual** (5' + preguntes, [guia de defensa](../00_General/00_Guia_defensa_oral.md)): problema, solució, una decisió tècnica justificada, demostració amb el teu maquinari.

**Deures:** repàs exprés de MicroPython i de ràdio ("Python flash", targetes de repàs espaiat) de cara a la prova pràctica T3 de la S5.

## Producte · Rover ampliat + dossier tècnic + defensa

Es tanca i s'avalua a la **Sessió 4** amb **totes** les rúbriques: **R1, R2, R3, R4 (nivell alt), R5**.

## La Sessió 5: prova pràctica T3 (no és sessió de projecte)

**Individual, per estacions rotatives**: part de programació a la taula i part de rover per torns a les pistes disponibles. Avalua destreses individuals de SA7-SA8; **no** reavalua el teu projecte de la SA9. Enunciat: `Avaluació/Prova_practica_T3.md` (el rebràs a l'aula).

## Si t'encalles (DEPURA)
> **D**escriu (què esperaves vs què passa) · **E**xamina (LED, display, lectura del sensor, missatge rebut) · **P**rova una hipòtesi cada cop · **U**bica el problema · **R**epara i torna a provar · **A**punta-ho al dossier (§6, Dificultats i solucions). Si un component nou (relé, PIR, NeoPixel) "no fa res", **primer** revisa el pin i l'alimentació, després sospita del codi.

<!-- web:only-github -->

## M'autoavaluo (Insuficient · Suficient/Bé · Notable · Excel·lent — la nota és 0-10)
| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Gestiono el meu projecte individual (anàlisi → prototip → proves → millora) | ☐ | ☐ | ☐ | ☐ |
| Integro almenys dos blocs del curs en una solució coherent | ☐ | ☐ | ☐ | ☐ |
| El meu dossier tècnic és complet i està ben documentat | ☐ | ☐ | ☐ | ☐ |
| Faig una defensa oral clara, amb una decisió justificada i responc preguntes | ☐ | ☐ | ☐ | ☐ |

## Quadern tècnic

> 📓 Escriu-ho a la teva entrada del **[quadern tècnic](../00_General/00_Quadern_tecnic.md)** (guia + plantilla; compta el 25 %). A la SA9, el quadern tècnic **és** essencialment el teu [dossier tècnic](SA9_dossier_plantilla.md): no cal duplicar-hi el contingut, però sí que hi facis constar el resum de cada sessió.
- **S1:** repte triat + requisits mínims.
- **S2:** prototip mínim viable + què hi has integrat de nou.
- **S3:** proves fetes + un error i com l'has resolt.
- **S4:** producte tancat + reflexió final (què has après, ètica/ODS).

<!-- /web:only-github -->

> 📌 **Vols més?** Ampliació, pensament computacional, exit ticket i ODS → **[SA9_fitxa_ampliada.md](SA9_fitxa_ampliada.md)**
