# SA5 · Ràdio: robots que parlen

**Durada:** 6 h (3 sessions) · **Maquinari:** micro:bit V2 (ràdio integrada); vehicle muntat a SA4 com a receptor

## Vincle competencial
- **Competències específiques:** CE-R1 (principal); CE-R2, CE-R3, CE-R5 (secundàries).
- **Criteris d'avaluació:** CA1.1, CA1.2.
- **Competències clau:** STEM, CD, CCL.

## Sabers
**Bloc E · Sistemes de control i automatització** (inici): **comunicació per ràdio** entre plaques micro:bit (esdeveniments, missatges, protocols senzills) i introducció a **estructures de dades bàsiques** (llistes, tuples) per emmagatzemar missatges i estats.

## Objectius d'aprenentatge
1. Configurar la **ràdio** de la micro:bit (`radio.on()`, grup/canal) i enviar/rebre missatges de text entre dues plaques.
2. Dissenyar un **protocol de missatges** senzill (comandes curtes) per controlar el vehicle a distància.
3. Emmagatzemar comandes o lectures rebudes en **llistes** o **tuples** bàsiques.
4. Relacionar la recepció d'un missatge amb una funció de moviment ja creada a la SA4 (esdeveniment → acció).

## Repte o pregunta inicial
> *"Com envies una ordre a un robot sense fils, i com fas perquè no es 'perdi' cap missatge?"*

> **Ràdio i treball individual (dotació d'1 micro:bit/alumne):** el codi i el producte de cada alumne són **sempre individuals**; provar la ràdio requereix dues places emissores/receptores, així que l'emparellament és **puntual i només de banc de proves**, mai de producte. Regla: cada alumne carrega el **seu propi programa** a la **seva pròpia placa** i s'aparella momentàniament amb la placa d'un company (grups de ràdio per parells de números de llista, rotant si cal) només per verificar que l'enviament/recepció funciona; cadascú prova, documenta i és avaluat pel **seu** codi, no pel del company.

## Seqüència de sessions

| Sessió | Objectiu | Activitats | Mini-check | Deures / simulador |
|---|---|---|---|---|
| **1** | Enviar i rebre missatges senzills per ràdio. | `radio.on()`, `radio.config(group=...)`, `radio.send()`/`radio.receive()`. Cada alumne escriu el **seu propi** codi d'emissor i de receptor; per verificar-lo, s'aparella **puntualment** (banc de proves, no producte compartit) amb la placa d'un company (parells de números de llista) i intercanvien breument el rol d'emissor/receptor. Introducció a llistes per registrar missatges rebuts. | — | Simulador python.microbit.org (mode ràdio, si disponible) o esquema de protocol al quadern: dissenyar 4-5 comandes pròpies (p. ex. `"F"`, `"B"`, `"L"`, `"R"`, `"S"`). |
| **2** | Dissenyar un protocol de comandes i connectar-lo a les funcions de moviment. | Definició d'un protocol propi de comandes curtes; recepció amb `radio.receive()` i crida a les funcions `avancar()`/`girar()`/`aturar()` de la SA4 segons el missatge rebut. Primeres proves amb el propi vehicle com a receptor, aparellat puntualment amb la placa d'un company o del docent com a emissor de proves (el codi receptor que s'avalua és sempre el propi). Mini-check individual (10', enviar/rebre un missatge i actuar-hi sense apunts; banc: `../Classes/00_General/00_Mini_checks_individuals.md`). | Mini-check individual. | Documentar el protocol de comandes al quadern (taula comanda → acció). |
| **3** | Tancar el repte de control per ràdio i introduir estructures de dades. | **Repte "control remot bàsic"**: el vehicle respon en temps real a les comandes rebudes per ràdio amb les funcions de moviment. Tancament de la introducció a **esdeveniments i estructures de dades** (llistes/tuples per registrar l'històric de comandes) com a **+ampliació** — sabers que es completen a la SA6. | — | Acabar i documentar el repte si no s'ha tancat a classe; provar el simulador amb un protocol de comandes ampliat. |

## Producte
Vehicle controlat a distància per ràdio amb un protocol de comandes propi (mínim 4 comandes) i registre de comandes rebudes al quadern tècnic.

## Avaluació
- Instruments: repte de control remot, quadern tècnic, observació.
- Rúbriques: **R1** (codi, criteri "Funcionament"), **R4** (documentació).

## Atenció a la diversitat
- **Bastida:** protocol de comandes model (taula comanda → acció) proporcionat; funció `rep_i_actua()` esquelet.
- **+ Ampliació:** ampliar el protocol amb comandes de velocitat variable o seqüències; registrar l'històric de comandes en una llista i mostrar-lo per REPL.

## Recursos
micro:bit radio module (documentació oficial); python.microbit.org (REPL i simulador). *(Vegeu `09_Materials_recursos_per_unitat.md`.)*
