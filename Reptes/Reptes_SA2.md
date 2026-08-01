# Reptes SA2 · Sortides: el robot actua

> 🧑‍🎓 **Quan toca fer-ne un?** És l'**ampliació ⭐** de la SA: comença'l quan tinguis el **nucli al dia** (el repte «semàfor o llum d'ambient» de la S3 i el muntatge de la mascota de la S4). Ensenya'l al docent perquè el validi.

**Fes els reptes en ordre de dificultat: comença per ⭐, i si arribes a ⭐⭐⭐ hauràs passat pels tres.** Tots parteixen dels programes de `Classes/SA2/codi/` i fan servir el Micro:shield. Es fan amb **maquinari real**: el simulador de python.microbit.org no reprodueix el LED extern, el LED RGB, el brunzidor ni el relé (vegeu [`SA2_esquemes_connexions.md`](../Classes/SA2/SA2_esquemes_connexions.md) §Simulació), tot i que la **lògica** es pot escriure i revisar-hi abans de provar-la a la placa.

> **Continguts SA2:** sortides digitals (`write_digital`) i PWM (`write_analog`, 0-1023), bucles `for`/`while`, acumuladors, LED RGB, mòdul `music`, relé. · **Vocabulari/bases:** `Classes/SA0/`.

> **Format "producte real":** cada repte simula un **encàrrec** amb **client**, **lliurable** i **ús al món real**. El requisit tècnic no canvia; el marc ajuda a donar sentit al producte.

---

## ⭐ Repte 1 · Llum de seguretat per a motxilla

**Context.** Una marca de motxilles vol un pilot LED d'emergència per a ciclistes/vianants: fix mentre tot va bé, parpelleig ràpid en "mode alerta".

> *Client: fabricant de motxilles i accessoris ciclistes · Lliurable: pilot LED de dos modes · Món real: llums de seguretat de bicicleta, senyalització d'obres.*

**Què treballa.** `pin.write_digital()`, bucles `for`/`while`, acumuladors, `button_a`/`button_b`.

**Requisit mínim.**
- Parteix de `led_parpelleig.py`: el LED parpelleja i es compta el nombre de cops (ja fet).
- Afegeix un **segon mode**: mentre el **botó A** està premut, el LED parpelleja **més ràpid** ("mode alerta"); sense prémer'l, parpelleja al ritme normal.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Mostra el comptador de parpellejos al display cada **5** cops en lloc de cada 10 (canvia només el número de l'operador `%`).
2. *(notable)* Afegeix un **tercer mode** amb el botó B: el LED es queda **fix** (mode "aparcada", sense parpellejar) fins que es torna a prémer un botó.
3. *(⭐⭐⭐)* Encapsula cada mode en una **funció pròpia** (`mode_normal()`, `mode_alerta()`, `mode_aparcada()`) cridada des del `while True:` segons l'estat dels botons.

    **Fites** (valida-les en ordre):
    1. El "mode alerta" parpelleja **visiblement** més ràpid que el normal (compara els `sleep()`).
    2. El comptador de l'ampliació 1 es mostra cada 5 parpellejos, no cada 10.
    3. El `while True:` queda reduït a poques línies que criden funcions, sense `write_digital()` repetit pertot.

---

## ⭐⭐ Repte 2 · Ambientador de llum i so per a una habitació

**Context.** Una empresa de decoració *smart home* vol un petit dispositiu que combini un **color ambient** (LED RGB) amb una **melodia curta** en encendre's, com un altaveu intel·ligent d'entrada.

> *Client: empresa de domòtica i decoració · Lliurable: llum ambient amb so d'entrada · Món real: assistents de veu, làmpades intel·ligents amb "escena" de llum i so.*

**Què treballa.** `write_analog()` (PWM, 0-1023), LED RGB (3 canals), mòdul `music`, funcions.

**Requisit mínim.**
- Parteix de `pwm_led_rgb.py` i `musica_altaveu.py`: colors combinats i melodia ja fets.
- En **engegar** el programa (abans del `while True:`), el LED RGB fa una **transició suau** cap al teu color ambient triat i sona una **melodia curta** de benvinguda.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Afegeix un **segon color ambient** que s'activa amb el botó A (per exemple, "mode relax" vs "mode festa"), cadascun amb el seu color RGB.
2. *(notable)* Fes que la **intensitat** del color ambient "respiri" (puja i baixa suaument amb `write_analog`, com a `respira()` de `pwm_led_rgb.py`) mentre no es toqui cap botó.
3. *(⭐⭐⭐)* Sincronitza el **color** amb la **melodia**: un color RGB diferent per a cada nota que sona (per exemple, notes greus = blau, agudes = vermell).

    **Fites** (valida-les en ordre):
    1. La transició d'engegada es veu **suau** (no un salt sobtat de color) i la melodia s'hi sent sencera.
    2. Els dos "modes" de l'ampliació 1 tenen colors clarament diferents i es poden alternar amb el botó sense reiniciar el programa.
    3. A l'ampliació 3, el canvi de color va **al ritme** de les notes (no és aleatori ni fix).

---

## ⭐⭐⭐ Repte 3 · Semàfor intel·ligent d'encreuament

**Context.** L'ajuntament vol un prototip de semàfor "intel·ligent" per a un encreuament amb poc trànsit: normalment fa el cicle habitual, però un **relé addicional** simula l'enllumenat d'emergència que s'activa en mode "alerta".

> *Client: enginyeria de trànsit municipal · Lliurable: prototip de semàfor amb mode d'emergència · Món real: semàfors intel·ligents, enllumenat d'emergència commutat.*

**Què treballa.** Sortides digitals i PWM combinades, `music`, **relé**, variables d'estat, funcions.

**Requisit mínim.**
- Parteix de `semafor_rele.py`: cicle verd/ambre/vermell amb temps en variables, avís sonor i relé (ja fet).
- Afegeix un **mode d'emergència**: si es prem el **botó A** en qualsevol moment, el semàfor **interromp el cicle**, posa el LED vermell **parpellejant** i **activa el relé de manera intermitent** (simulant un llum d'emergència), fins que es torna a prémer el botó A per tornar al cicle normal.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Al mode d'emergència, afegeix un **avís sonor intermitent** (`music.pitch()` curt cada parpelleig) amb el brunzidor.
2. *(notable)* Encapsula el cicle normal i el mode d'emergència en **funcions separades** (`cicle_normal()`, `mode_emergencia()`), i una variable d'estat (`emergencia = True/False`) que decideix quina es crida des del `while True:`.
3. *(⭐⭐⭐)* Sincronitza el **LED RGB** (si el tens muntat d'un repte anterior) amb el mode d'emergència: un patró de color propi (per exemple, ambre parpellejant) en lloc de fer-lo servir només amb el LED digital.

    **Fites** (valida-les en ordre):
    1. Prémer el botó A **interromp** el cicle normal a l'instant (no cal esperar que acabi la fase en curs) i entra en mode d'emergència.
    2. Tornar a prémer el botó A recupera el **cicle normal des del principi** (fase verda), no a mig cicle.
    3. El codi del `while True:` és curt i llegible: decideix quina funció cridar segons `emergencia`, sense repetir la lògica de cap fase dues vegades.

---

## 🎨 Fes-lo teu (tria abans de començar)

> El repte fixa **què** ha de fer el sistema; **el context el poses tu**. Tria i anota-ho al quadern — un producte amb decisions teves sempre s'explica i es defensa millor:
> - **Repte 1:** decideix la **velocitat** exacta de cada mode (normal vs alerta) i per què.
> - **Repte 2:** tria els teus **dos colors ambient** i explica quina "sensació" volies transmetre amb cadascun.
> - **Repte 3:** decideix el **patró** exacte del mode d'emergència (ritme del parpelleig, to del so).

## Material necessari (els tres reptes)

- micro:bit V2 + Micro:shield + cable micro-USB.
- Kit Keyestudio 1 (LED, LED RGB, brunzidor) i Kit 3 (relé), muntats segons [`SA2_esquemes_connexions.md`](../Classes/SA2/SA2_esquemes_connexions.md).
- El simulador de python.microbit.org **només** serveix per revisar la lògica (bucles, condicionals, temps): els components externs cal provar-los amb maquinari real.

## Per on començar (mètode de projecte + PRIMM)

1. **Analitzar:** quins modes/estats necessito i quin senyal (digital o PWM) li correspon a cadascun?
2. **Dissenyar (Predir):** escriu *abans* quines línies de codi necessitaràs i quins pins faràs servir.
3. **Programar/Prototipar:** parteix del programa base de `Classes/SA2/codi/` i modifica'l.
4. **Provar:** executa'l amb el maquinari real, observa, compara amb la teva predicció.
5. **Millorar:** introdueix funcions i una ampliació.

## Com s'avalua

| Rúbrica | Per què |
|---|---|
| **R1** (codi) | Funcionament, estructura, llegibilitat, depuració. |
| **R2** (circuit) | Muntatge correcte i segur dels components externs. |
| **R4** (documentació) | Quadern tècnic: predicció, solució i millora. |
| **R5** (actitud) | Autonomia, gestió de l'error. |

## Producte / entrega

- Codi `.py` comentat + entrada al **quadern tècnic** (predicció, què he fet, error trobat i millora).

---

## Orientació docent

- **Errors freqüents:** confondre l'escala de `write_analog` (0-1023) amb 0-255 o 0-1; oblidar `write_digital(0)` i deixar el LED sempre encès; inicialitzar un acumulador dins del bucle; connectar el costat extern del relé directament a un pin.
- **Diferenciació:** el mínim és idèntic per a tothom → tothom assoleix la base; les ampliacions 2-3 introdueixen funcions i variables d'estat per a qui va sobrat.
- **Gestió d'aula:** tots requereixen maquinari real per a la part de sortides externes (el simulador només valida la lògica); el repte 3 reaprofita el muntatge complet de `semafor_rele` de la S3.
- **Vincle avaluació:** producte coherent amb el de la SA2 (quadern tècnic, R4/R5) i amb les rúbriques R1/R2 del repte «semàfor o llum d'ambient».
