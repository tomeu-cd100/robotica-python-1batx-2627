# 08 · Seqüenciació temporal anual

**Base de càlcul:** 2 h/setmana · ≈ 35 setmanes lectives · ≈ **70 h**.
Distribució en **3 trimestres** i **9 situacions d'aprenentatge (SA)**. Tot el treball és **individual**: cada alumne avança amb el seu propi maquinari i el seu propi fil conductor (mascota T1 / vehicle T2 / rover T3).

## Visió general

| Trim. | Setmanes aprox. | SA | Títol | Hores |
|---|---|---|---|---|
| **1r** | s1-s12 | SA1 | Hola, robot! | 6 |
| | | SA2 * | Sortides: el robot actua | 8 |
| | | SA3 † | Entrades: el robot percep | 8 |
| **2n** | s13-s24 | SA4 * | Funcions i moviment | 8 |
| | | SA5 | Ràdio: robots que parlen | 6 |
| | | SA6 † | Control: el robot decideix | 8 |
| **3r** | s25-s35 | SA7 | Robòtica mòbil: el rover | 8 |
| | | SA8 | Autonomia i telemetria | 6 |
| | | SA9 † | Repte final integrador | 10 |
| | | | **Subtotal SA** | **68 h** |
| | | | **Marge (diagnòstic, avaluació, imprevistos)** | **~2 h** |
| | | | **Total** | **70 h** |

> **\*** SA amb **4a sessió de producte comprimible**: les **8 h (4 sessions)** són el còmput de referència; la S4 és la sessió de producte, però si el calendari real ho exigeix el **repte de la S3 pot fer de producte** i la S4 s'allibera (vegeu el pla de contingència).
>
> **†** SA la **darrera sessió de la qual és, sencera, la prova pràctica trimestral** (T1 a SA3 i T2 a SA6: la S4; T3 a SA9: la S5): el producte es tanca a la sessió anterior i la darrera sessió és la prova **individual**. Cap activitat de sessió no competeix amb la prova (vegeu «Marge i integració de l'avaluació»).
>
> **SA5** compta 6 h (3 sessions); la introducció a esdeveniments i estructures de dades es completa dins el tancament de la S3 i com a **+ampliació**.

## Marge i integració de l'avaluació

Per garantir la **viabilitat real** del curs (2 h/setmana ≈ 70 h), s'apliquen dos criteris:

1. **Flexibilitat de ritme (marge ~2 h):** les SA marcades amb **\*** (SA2, SA4) tenen la S4 de producte **comprimible** (el repte de la S3 pot fer de producte), i la SA5 queda en 3 sessions. Així hi ha marge per al **diagnòstic inicial** (SA1), festius i imprevistos sense alterar el còmput de referència.
2. **Proves pràctiques amb sessió pròpia dins de la SA (T1, T2 i T3):** les proves (`Avaluació/Prova_practica_T1/T2/T3`) ocupen **una sessió sencera**, comptada **dins de les hores** de la SA de tancament del trimestre — no s'hi barreja cap altra activitat:
   - **T1** → la **S4 de SA3 és, sencera, la prova** (individual). El producte de la SA3 es tanca a la **S3** (el repte de la S3 és el producte).
   - **T2** → la **S4 de SA6 és, sencera, la prova** (individual). El producte es tanca a la **S3**.
   - **T3** → la **S5 de SA9 és, sencera, la prova** (individual, **per estacions rotatives**: la part de programació es fa a la taula i la part de rover per torns a les pistes disponibles). El projecte es tanca a la **S4** (dossier + defensa oral; amb grups nombrosos, defenses esglaonades des de la S3, ja previstes a la guia). La prova és **independent del projecte**: avalua destreses individuals de SA7-SA8 i puntua només a la dimensió «Proves pràctiques» (20 %); el projecte puntua a «Projectes i productes» — cap evidència no compta dues vegades.

> Vegeu la ponderació a `06_Avaluacio_criteris_qualificacio.md` (dimensió "Proves pràctiques", 20 %). **Per què així:** una prova individual de ~100' i una sessió de producte amb defensa **no caben en la mateixa sessió de 2 h**; fer-ho explícit evita descobrir-ho al desembre. El cost (1 sessió per trimestre) ja està comptat dins les hores de la SA.

## Pla de contingència temporal («curs mínim viable»)

El marge real (~2 h) és **més petit que les pèrdues habituals** d'un curs (festius que cauen en dia de classe, sortides, vagues, avaries). A més, com es detalla més avall, la fabricació del fil conductor **ja consumeix per endavant** bona part d'aquest marge: cal preveure **on es retalla** abans que passi, no improvisar-ho al març. Ordre oficial de retallada, **sense trencar la progressió**:

1. **No es retallen mai** SA1–SA3 (fonaments d'E/S: tot el curs s'hi recolza) ni SA9 (síntesi i pes avaluatiu del 3r trimestre).
2. **Primera retallada:** comprimir la **S4 de producte** de SA2 i/o SA4: el **repte de la S3 fa de producte** (s'avalua amb les mateixes rúbriques) i la S4 s'allibera — fins a 2 sessions recuperades. *Atenció:* les S4 de SA3 i SA6 **no es retallen** (són les proves T1/T2); si el calendari les desplaça, la prova es fa a la darrera sessió efectiva de la SA.
3. **Segona retallada:** **SA8 comprimible de 6 h a 4 h** (fusionar S1+S2: telemetria + disseny en una sessió; la S3 d'IA es manté — és el nucli del saber "IA aplicada al control").
4. **Tercera retallada (últim recurs):** SA7 de 8 h a 6 h (sacrificar la S4 de seguidor de línia i quedar-se amb l'evita-obstacles com a comportament autònom).
5. **Es mantenen sempre:** una **prova pràctica per trimestre** (amb la seva sessió, comptada dins la SA) i els **mini-checks individuals** (10', són el radar de l'avaluació).

**Senyal d'alerta per decidir a temps:** si en acabar el **1r trimestre no s'ha tancat la SA3**, activa la retallada 2 ja al gener (no esperis al maig); si a **Setmana Santa no s'ha tancat la SA6**, activa també la 3.

## Fil conductor individual i consum del marge

El curs aplica el **fil conductor de tres artefactes individuals** (mascota T1 → vehicle T2 → rover T3, un exemplar propi per alumne, construït amb la talladora làser i la impressora 3D de l'aula): vegeu `../Classes/00_General/00_Fil_conductor_construccions.md`. Cada sessió de fabricació **consumeix per endavant** una de les retallades del pla de contingència anterior; cal deixar-ho explícit aquí perquè no es descobreixi al març.

| Trimestre | Sessió de fabricació | Consum explícit del pla de contingència |
|---|---|---|
| 1r (mascota) | S4 de SA2 | Primera retallada (S4 de SA2 comprimible: el repte de la S3 fa de producte) |
| 2n (vehicle) | S4 de SA4 | Primera retallada (S4 de SA4 comprimible: el repte de la S3 fa de producte) |
| 3r (rover) | Sessió 0 del trimestre | Segona retallada (SA8 comprimible de 6 h a 4 h; les 2 h alliberades es traslladen a l'inici del T3, abans de començar SA7) |

> ⚠️ Amb el fil conductor en marxa, la **primera i la segona retallada** del pla de contingència queden **assignades per endavant** a la fabricació dels artefactes individuals, no disponibles com a marge davant d'imprevistos: el **marge efectiu real és ≈ 0 h**. L'única palanca que queda lliure és la **tercera retallada** (SA7 de 8 h a 6 h, últim recurs).
>
> **Mitigació:** com que cada alumne fabrica el seu propi exemplar (mascota/vehicle/rover) i el temps de tall làser/impressió 3D per al grup real (15-20 alumnes) no és comprimible dins d'una sola sessió, **el docent pretalla les peces base fora d'horari lectiu** (talladora làser en dies previs) i l'alumnat només munta, ajusta i personalitza a l'aula. Això és el que permet que el «consum» de la taula anterior sigui d'una sola sessió per trimestre i no més.
>
> **Senyal d'alerta:** si en acabar el 1r trimestre no s'ha tancat la SA3 (el mateix senyal que activa la retallada 2 més amunt), les peces de la mascota es reparteixen **ja pretallades pel docent**, en lloc d'esperar una sessió de tall làser addicional.

## Fil conductor i progressió

```
Trimestre 1 — FONAMENTS (fil conductor: la mascota)
  SA1 ─ Context, mètode, entorns, seguretat, diagnòstic inicial
  SA2 ─ MicroPython + sortides (matriu LED, so, PWM)
  SA3 ─ MicroPython + entrades (polsadors, sensors del Micro:shield/Keyestudio)
        ▼ (l'alumnat ja controla E/S amb la micro:bit)
Trimestre 2 — CONTROL I MOVIMENT (fil conductor: el vehicle)
  SA4 ─ Funcions i actuadors de moviment (servos, motors)
  SA5 ─ Ràdio (nou paradigma d'esdeveniments, sensors del kit)
  SA6 ─ Sistemes de control (llaç obert/tancat, màquines d'estats)
        ▼ (l'alumnat controla moviment i realimentació)
Trimestre 3 — ROBÒTICA I INTEGRACIÓ (fil conductor: el rover)
  SA7 ─ Robòtica mòbil (rover propi): seguir línia / evitar obstacles
  SA8 ─ Autonomia i telemetria: dades, introducció a la IA
  SA9 ─ Repte final: projecte autònom + documentació + defensa
```

## Criteris de seqüenciació

1. **Maquinari concret → abstracció:** del component (SA2) al sistema autònom (SA9).
2. **Progressió interna a Python:** seqüències + `while True:`/`if` bàsic amb PRIMM (SA1) → variables i bucles (SA2, aprofundeix el bucle) → condicionals aplicats a sensors (SA3, aprofundeix el `if`) → funcions (SA4, formalització d'escriure-les; als reptes ⭐⭐⭐ de SA1-SA3 ja se'n **llegeixen**) → esdeveniments i estructures de dades (SA5-SA6) → integració (SA7-SA9).
3. **Cada SA reutilitza i amplia l'anterior** (avaluació contínua i espiral).
4. **El projecte final (SA9) integra** electrònica + programació + control + robòtica + documentació.

## Connexions interdisciplinàries

- **Matemàtiques I:** funcions, proporcionalitat (mapatge de senyals), geometria (trajectòries), lògica.
- **Física:** electricitat, mecànica del moviment, sensors.
- **Tecnologia i Enginyeria I:** comparteix sabers (CE5, Automatització); possibilitat de coordinació de projectes.
- **Treball de Recerca:** la SA9 pot llavorar un futur TR.

## Flexibilitat

- Si la matèria acaba sent de **3 h/setmana**, cada SA incorpora les activitats *"+ ampliació"*.
