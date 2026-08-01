# Reptes SA6 · Control: el robot decideix

> 🧑‍🎓 **Quan toca fer-ne un?** És l'**ampliació ⭐** de la SA: comença'l quan tinguis el **nucli al dia** (el repte «vehicle amb aturada d'emergència» de la S3, tancat). Ensenya'l al docent perquè el validi.

**Fes els reptes en ordre de dificultat: comença per ⭐, i si arribes a ⭐⭐⭐ hauràs passat pels tres.** Tots parteixen dels programes de `Classes/SA6/codi/` i fan servir el concepte de màquina d'estats i/o histèresi. Es fan amb **maquinari real** quan calgui un actuador (relé/LED) o el vehicle: el simulador de python.microbit.org **sí simula** `temperature()`, els botons i el mòdul `log`, però **NO** simula motors ni relé (vegeu [`SA6_esquemes_connexions.md`](../Classes/SA6/SA6_esquemes_connexions.md) §Simulació), útil per revisar la lògica.

> **Continguts SA6:** llaç obert/tancat, màquina d'estats finits (variable d'estat + transicions), histèresi, aturada d'emergència prioritària, mòdul `log`. · **Vocabulari/bases:** `Classes/SA0/`.

> **Format "producte real":** cada repte simula un **encàrrec** amb **client**, **lliurable** i **ús al món real**. El requisit tècnic no canvia; el marc ajuda a donar sentit al producte.

> 🎛️ **Recorda:** el codi i el producte de cada repte són **teus**, com a tota la SA6.

---

## ⭐ Repte 1 · Termòstat de dues zones

**Context.** Un petit hivernacle escolar té dues zones (semillers i planter) amb necessitats de temperatura diferents. El responsable de l'hort de l'institut vol un sistema que avisi de quina zona necessita escalfor sense que el relé "cliqui" contínuament.

> *Client: hort escolar de l'institut · Lliurable: termòstat amb dues zones simulades i histèresi pròpia per zona · Món real: control climàtic d'hivernacles, incubadores.*

**Què treballa.** Histèresi (dos llindars), variables d'estat múltiples, `termostat_histeresi.py`.

**Requisit mínim.**
- Parteix de `termostat_histeresi.py`: manté la histèresi de dos llindars (ja feta).
- Simula una **segona zona** amb una segona parella de llindars (per exemple, `LLINDAR_BAIX_2`/`LLINDAR_ALT_2`) i un segon "actuador" (un altre pin digital o el display mostrant quina zona està activa).
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Mostra al display, amb `display.show()`, una lletra diferent segons quina zona (o zones) té l'actuador activat en cada moment.
2. *(notable)* Registra amb una llista quantes vegades ha canviat d'estat cada zona durant la sessió de proves, i mostra-ho amb `print()` en prémer A+B.
3. *(⭐⭐⭐)* Afegeix un **tercer llindar d'emergència** molt per sobre de l'alt (per exemple, sobreescalfament): si es supera, l'estat passa a una "alerta" que desactiva els dos actuadors i ho mostra clarament al display, per davant de qualsevol altra lògica de zona.

    **Fites** (valida-les en ordre):
    1. Les dues zones commuten de manera independent i sense oscil·lació ràpida.
    2. El comptador de canvis d'estat (ampliació 2) és correcte per a totes dues zones.
    3. L'alerta d'emergència (ampliació 3) desactiva **sempre** els dos actuadors, sense excepció.

---

## ⭐⭐ Repte 2 · Semàfor de vianants amb botó prioritari

**Context.** Un ajuntament vol millorar un semàfor de vianants perquè, en prémer el botó de sol·licitud de pas, el cicle canviï a vermell per als vehicles **com més aviat millor**, sense esperar tot un cicle sencer si no cal.

> *Client: ajuntament (mobilitat urbana) · Lliurable: semàfor amb FSM i una interrupció prioritària per botó · Món real: semàfors de vianants amb polsador, passos de vianants intel·ligents.*

**Què treballa.** Màquina d'estats amb transicions, prioritat d'una entrada sobre les altres, `maquina_estats_semafor.py`.

**Requisit mínim.**
- Parteix de `maquina_estats_semafor.py`: manté els tres estats VERD/GROC/VERMELL amb les seves transicions temporitzades.
- Afegeix un **botó de sol·licitud** (botó A): si es prem mentre l'estat és VERD, la transició cap a GROC s'avança (per exemple, redueix el temps restant de VERD a un màxim de 1000 ms) en lloc d'esperar el temps normal.
- Codi comentat amb el diagrama d'estats documentat (comentari o quadern).

**Ampliacions graduades.**
1. *(bàsica)* Mostra al display una icona diferent quan el botó de sol·licitud s'ha premut i encara s'està esperant que faci efecte (per exemple, un punt parpellejant).
2. *(notable)* Evita que prémer el botó repetidament durant el VERMELL o el GROC tingui cap efecte (només ha de "comptar" durant el VERD).
3. *(⭐⭐⭐)* Afegeix un **segon semàfor** (per als vianants, en un altre LED o en text al display) que estigui **sempre en l'estat contrari** al de vehicles (vermell per a vehicles = verd per a vianants), sense duplicar la lògica de transicions.

    **Fites** (valida-les en ordre):
    1. El cicle bàsic (VERD→GROC→VERMELL→VERD) funciona igual que al nucli si no es prem mai el botó.
    2. El botó de sol·licitud (requisit mínim) avança la transició únicament durant el VERD.
    3. El semàfor de vianants (ampliació 3) és sempre coherent amb el de vehicles, sense contradiccions.

---

## ⭐⭐⭐ Repte 3 · Vehicle amb alerta per temperatura i registre de bord

**Context.** Una empresa de robots de magatzem vol que els seus vehicles teledirigits s'aturin automàticament si detecten una temperatura anòmala (per exemple, prop d'una font de calor), i que quedi un registre de quan ha passat, per revisar-ho després d'una jornada de proves.

> *Client: fabricant de robots de magatzem · Lliurable: vehicle amb un tercer estat ALERTA i registre de dades de temperatura · Món real: robots industrials amb aturades de seguretat automàtiques i telemetria bàsica.*

**Què treballa.** Màquina d'estats amb tres estats, histèresi aplicada a un tercer estat, mòdul `log`, `vehicle_seguretat.py` + `registre_dades.py`.

**Requisit mínim.**
- Parteix de `vehicle_seguretat.py`: manté el protocol de ràdio i l'STOP prioritari (polsador + `"X"`) intactes.
- Afegeix l'estat **ALERTA**: si `temperature()` supera un llindar alt, el vehicle passa a ALERTA (s'atura i el LED parpelleja); només torna a RUN quan la temperatura baixa per sota d'un llindar més baix (histèresi, com al termòstat de la S1) **i** arriba una nova ordre de moviment.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Registra amb `log.add()` cada vegada que el vehicle entra o surt de l'estat ALERTA, amb la temperatura del moment.
2. *(notable)* Mostra per REPL (`print()`) quantes vegades ha entrat en ALERTA durant la sessió de proves, llegint el registre acumulat en una llista pròpia (a més del `log`).
3. *(⭐⭐⭐)* Fes que l'ALERTA també es pugui provocar manualment per ràdio amb una comanda pròpia (per exemple, `"A"`), útil per simular una prova de seguretat sense esperar que pugi realment la temperatura.

    **Fites** (valida-les en ordre):
    1. L'STOP prioritari (polsador i `"X"`) segueix funcionant exactament igual que al nucli, sense cap regressió.
    2. L'estat ALERTA s'activa i es desactiva amb histèresi (dos llindars), no amb un de sol.
    3. El registre amb `log` (ampliació 1) queda llegible per USB amb almenys 2 entrades d'ALERTA d'una sessió de proves.

---

## 🎨 Fes-lo teu (tria abans de començar)

> El repte fixa **què** ha de fer el sistema; **el context el poses tu**. Tria i anota-ho al quadern — un producte amb decisions teves sempre s'explica i es defensa millor:
> - **Repte 1:** decideix els teus llindars i com distingeixes visualment les dues zones.
> - **Repte 2:** tria la teva manera de representar el semàfor de vianants (LED, text, icona).
> - **Repte 3:** decideix quin llindar de temperatura té sentit per a la teva ALERTA i com ho documentes al quadern.

## Material necessari (els tres reptes)

- micro:bit V2 + Micro:shield + cable micro-USB, individual.
- Relé o LED (Kit 1/3) per al repte 1; polsador per al repte 2 (o el botó A com a substitut); el vehicle T2 muntat per al repte 3.
- El simulador de python.microbit.org **sí** simula `temperature()`, botons i `log`, útil per revisar la lògica dels tres reptes abans de provar-la amb maquinari real.

## Per on començar (mètode de projecte + PRIMM)

1. **Analitzar:** quina part del programa base ja tinc feta i puc reutilitzar (histèresi, FSM, protocol de ràdio), i quin estat o transició nova necessito?
2. **Dissenyar (Predir):** dibuixa el diagrama d'estats *abans* d'escriure el codi.
3. **Programar/Prototipar:** parteix del programa base de `Classes/SA6/codi/` i modifica'l.
4. **Provar:** executa'l, observa, compara amb el teu diagrama.
5. **Millorar:** afegeix una ampliació i documenta-la.

## Com s'avalua

| Rúbrica | Per què |
|---|---|
| **R1** (codi) | Funcionament, disseny de la FSM, depuració. |
| **R3** (autonomia/control) | STOP/prioritats correctes, histèresi ben aplicada. |
| **R4** (documentació) | Quadern tècnic: diagrama d'estats, predicció, solució i millora. |

## Producte / entrega

- Codi `.py` comentat + entrada al **quadern tècnic** (diagrama d'estats, predicció, què he fet, error trobat i millora).

---

## Orientació docent

- **Errors freqüents:** oblidar l'ordre de comprovació (prioritat) dins del bucle; un sol llindar en lloc de dos (oscil·lació); no centralitzar el canvi d'estat en una única funció.
- **Diferenciació:** el mínim és idèntic per a tothom → tothom assoleix la base; les ampliacions 2-3 introdueixen registre de dades, comandes noves i coherència entre dues FSM.
- **Gestió d'aula:** el repte 1 només necessita relé/LED; el repte 2 es pot fer sense vehicle; el repte 3 reaprofita el vehicle muntat a SA4-SA5.
- **Vincle avaluació:** producte coherent amb el de la SA6 (quadern tècnic, R4/R5) i amb les rúbriques R1/R3 del repte «vehicle amb aturada d'emergència».
