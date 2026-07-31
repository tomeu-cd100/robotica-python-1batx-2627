# 00 · El fil conductor: tres construccions individuals

> **Per a qui és?** Per al **docent**. Explica els tres robots del fil conductor del curs (mascota T1 / vehicle T2 / rover T3), per què són **individuals** i com s'organitza la seva **fabricació digital** (talladora làser + impressora 3D) per a 15-20 alumnes sense que es mengi el marge horari del curs.
> **Quan es llegeix?** Abans de començar el curs (per reservar les sessions de màquina) i just abans de cada sessió de fabricació (SA2·S4, SA4·S4 i la Sessió 0 del 3r trimestre).

## 1. Els tres robots (visió de conjunt)

| | T1 · Mascota reactiva | T2 · Vehicle teledirigit | T3 · Rover autònom |
|---|---|---|---|
| **Trimestre / SA** | 1r (SA2-SA3) | 2n (SA4-SA6) | 3r (Sessió 0 + SA7-SA9) |
| **Es munta a** | SA2 · Sessió 4 | SA4 · Sessió 4 | Sessió 0, prèvia a SA7 |
| **Es tanca (programat) a** | SA3 · Sessió 3 | SA6 · Sessió 3 | SA9 · Sessió 4 |
| **Peça làser (DM 3 mm)** | Carcassa amb cara | Xassís de 2 rodes | **Cap de nova** — reaprofita el xassís de T2 |
| **Peces 3D** | Escaires, difusors d'ull | Roda boja, suports de components | **Només 2 peces petites**: suport HC-SR04, suport seguidor de línia |
| **Actuadors clau** | Matriu LED (cara), so, servo (orelles/cua) | 2 motoreductors + rodes | Els mateixos de T2 (sense canvis) + telemetria |
| **Sensors clau** | Llum, so, sacseig (acceleròmetre) | — (rebre per ràdio) | Seguidor de línia, ultrasons |
| **Dossier complet** | [`00_Projecte_T1_Mascota.md`](00_Projecte_T1_Mascota.md) | [`00_Projecte_T2_Vehicle.md`](00_Projecte_T2_Vehicle.md) | [`00_Projecte_T3_Rover.md`](00_Projecte_T3_Rover.md) |

> ⚠️ **El rover (T3) NO és un robot nou: és el vehicle (T2) ampliat.** No hi ha cap plantilla de tall làser pròpia de T3 — el mateix xassís, motoreductors i roda boja muntats a SA4 es reaprofiten tal qual. La «fabricació» de T3 es limita a **dues peces petites impreses en 3D** (suport de l'HC-SR04 i suport del seguidor de línia), molt més lleugera que la de T1/T2. Vegeu el detall a [`00_Projecte_T3_Rover.md`](00_Projecte_T3_Rover.md).

Cada alumne té el seu **propi exemplar**: no hi ha peces ni codi compartits entre alumnat (vegeu `Programació didàctica/04_Metodologia.md` §4.3). El que **sí** és comú és la **plantilla de tall** (fixa) i les **màquines** (làser i impressora, gestionades pel docent).

## 2. Per què el marge del curs és ≈ 0 h (i com es compensa)

Segons `Programació didàctica/08_Sequenciacio_temporal_anual.md`, la fabricació dels tres robots **consumeix per endavant** dues de les tres retallades del pla de contingència temporal:

| Trimestre | Sessió de fabricació | Retallada que consumeix |
|---|---|---|
| 1r (mascota) | S4 de SA2 | 1a retallada (S4 de SA2 comprimible) |
| 2n (vehicle) | S4 de SA4 | 1a retallada (S4 de SA4 comprimible) |
| 3r (rover) | Sessió 0, prèvia a SA7 | 2a retallada (SA8 comprimida de 6 a 4 h) |

El **marge efectiu real és ≈ 0 h**: no hi ha temps de sobra per a errors de fabricació. Per això, la mitigació és estructural, no opcional:

> 🔑 **El docent pretalla les peces base fora d'horari lectiu.** El temps de tall làser i d'impressió 3D per a 15-20 alumnes **no cap** dins d'una sola sessió de 2 h. L'alumnat **només munta, ajusta i personalitza** a l'aula; mai espera la màquina en directe durant la classe.

Si en acabar el 1r trimestre no s'ha tancat la SA3 (el senyal d'alerta del doc. 08), les peces de la mascota **ja arriben pretallades pel docent**, sense esperar cap sessió addicional de tall.

## 3. Calendari de fabricació per a 15-20 alumnes

### 3.1. xTool S1 (talladora làser) — peces de DM 3 mm

**Només T1 i T2 tenen peça làser pròpia**; T3 no en necessita cap (reaprofita el xassís de T2). Xifres calculades per a **20 alumnes** (extrem superior del grup real de 15-20):

| Robot | Peça | Mida aprox. | Peces/alumne | Nesting per tauler (600×400 mm, DM 3 mm) | Talls necessaris (20 alumnes) |
|---|---|---|---|---|---|
| T1 Mascota | Carcassa (`mascota.svg`): base + 4 laterals + tapa + 2 orelles | ~180×140 mm | 1 planxa (8 peces) | 2 carcasses/tauler | 10 taulers |
| T2 Vehicle | Xassís de 2 rodes (`xassis_vehicle.svg`) | ~200×150 mm | 1 planxa | 2 xassís/tauler | 10 taulers |
| T3 Rover | — (reaprofita el xassís de T2) | — | — | — | **0 taulers** |
| | | | | **Total anual** | **20 taulers** |

> El **nesting** (col·locar diverses peces d'alumnes diferents al mateix tauler abans de llançar el tall) és imprescindible: reduir de 20 talls individuals a 10 talls de tauler per robot és el que fa viable la fabricació fora d'horari lectiu. El docent agrupa els fitxers validats de 2 alumnes per tauler abans de cada lot.

**Temps orientatiu de tall xTool S1:** ~15-20 min/tauler de DM 3 mm segons densitat de traç (varia amb la potència/velocitat calibrades). Per a 20 alumnes: **~2,5-3,5 h de màquina per robot (T1 i T2)**, repartides en 2-3 sessions fora d'horari lectiu els dies previs a la sessió de muntatge. **T3 no consumeix hores de làser.**

### 3.2. Bambu Lab P2S Combo (impressora 3D) — peces auxiliars

Xifres per a **20 alumnes**:

| Robot | Peça | Temps orientatiu/unitat | Jocs (20 alumnes) |
|---|---|---|---|
| T1 Mascota | Escaires d'angle (×8) + difusors d'ull (×2) | ~10 min/joc (impressió en lot a la placa) | 20 jocs |
| T2 Vehicle | Roda boja + suports de motor i d'electrònica | ~20 min/joc | 20 jocs |
| T3 Rover | Suport HC-SR04 + suport seguidor de línia (**només 2 peces petites**; la roda boja ja es va imprimir a T2 i es reaprofita) | ~8 min/joc (molt més lleuger que T1/T2) | 20 jocs |

**Estratègia:** la Bambu P2S imprimeix **en lot** (diverses còpies a la mateixa placa): un lot de 6-8 jocs per càrrega, llançat entre sessions (nit/cap de setmana). Per a 20 alumnes calen **3 lots per robot** a T1/T2 (1-3 h cadascun) i només **2-3 lots curts** (<1 h cadascun) a T3, gràcies al volum petit de les seves dues peces noves.

### 3.3. Calendari tipus (setmanes prèvies a cada sessió de muntatge)

| Setmana | Acció |
|---|---|
| S-2 | L'alumnat personalitza **només la zona editable** de la plantilla (nom, cara/decoració) sobre una còpia pròpia del `.svg`; el docent en valida el disseny (no envaeix la zona fixa ni trenca cap forat de muntatge). |
| S-1 | El docent agrupa els fitxers validats per **nesting** (2 alumnes/tauler a T1/T2) i llança els **lots de tall làser** i les **impressions 3D** fora d'horari lectiu. |
| S0 (sessió de muntatge) | Cada alumne recull el seu joc de peces (ja tallades/impreses) i **munta, cablatge i prova** durant la sessió (SA2·S4, SA4·S4 o Sessió 0 de 3r trimestre). A T3, «recollir peces» vol dir només **les dues peces d'ampliació noves**: el xassís ja l'ha portat muntat des de T2. |

## 4. Pla B: si una peça no arriba a temps

- **Peces làser o 3D pendents (T1/T2):** l'alumne munta amb una **peça de reserva genèrica** (sense personalitzar) i la substitueix més endavant sense penalització; el que es qualifica al muntatge és el resultat funcional (R2), no el temps d'espera de màquina.
- **Sense cap peça disponible (avaria de màquina):** l'alumne treballa el codi al **simulador** (`00_Entorns_de_treball.md` §2) sobre el mateix esquema de cablatge, i es completa el muntatge físic tan bon punt hi hagi peça — el producte es pot lliurar amb una pròrroga curta, documentada al full d'incidències.
- **Vehicle (T2) espatllat abans de la Sessió 0 de T3:** com que el rover **reaprofita** el xassís del vehicle, es repara només el component afectat (motor, roda, connexió) abans d'ampliar-lo; **mai cal fabricar un xassís nou**, ja que T3 no en té cap de propi.
- **Els dos suports nous de T3 (HC-SR04, seguidor de línia) endarrerits:** es pot fixar temporalment el sensor amb cinta/brides i seguir programant; se substitueix pel suport definitiu quan arribi, sense aturar la SA7.

## 5. Full de cua de màquina (registre del docent)

Full públic per sessió de fabricació, amb una fila per alumne: **nom · fitxer validat (data) · tauler/lot assignat · estat (pendent / tallat / imprès / recollit)**. Mantenir-lo visible (paper a l'aula o full compartit) evita que ningú «perdi» la seva peça enmig d'un lot de 20.

---

⬅️ Torna a [`00_LLEGEIX-ME_Classes.md`](00_LLEGEIX-ME_Classes.md).
