# Reptes SA4 · Funcions i moviment

> 🧑‍🎓 **Quan toca fer-ne un?** És l'**ampliació ⭐** de la SA: comença'l quan tinguis el **nucli al dia** (el repte «control per botons» de la S3, tancat). Ensenya'l al docent perquè el validi.

**Fes els reptes en ordre de dificultat: comença per ⭐, i si arribes a ⭐⭐⭐ hauràs passat pels tres.** Tots parteixen dels programes de `Classes/SA4/codi/` i fan servir el Micro:shield. Es fan amb **maquinari real**: el simulador de python.microbit.org **no** reprodueix ni el servo ni els motoreductors (vegeu [`SA4_esquemes_connexions.md`](../Classes/SA4/SA4_esquemes_connexions.md) §Simulació), tot i que la **lògica** es pot escriure i revisar-hi abans de provar-la a la placa.

> **Continguts SA4:** funcions (`def`), paràmetres, valor de retorn, servomotor amb PWM (`set_analog_period`, `write_analog`), motoreductor amb PWM i sentit (M1/M2), botons A/B, seqüències amb estat. · **Vocabulari/bases:** `Classes/SA0/`.

> **Format "producte real":** cada repte simula un **encàrrec** amb **client**, **lliurable** i **ús al món real**. El requisit tècnic no canvia; el marc ajuda a donar sentit al producte.

---

## ⭐ Repte 1 · Salutació programable per a un aparador

**Context.** Una botiga vol una figura d'aparador que saludi els vianants de manera diferent segons el moment del dia (matí animat, tarda tranquil·la), sense que calgui reprogramar-la cada cop.

> *Client: comerç de barri · Lliurable: figura d'aparador amb salutacions configurables · Món real: cartells i figures animatroniques d'aparador, robots de recepció.*

**Què treballa.** Funcions amb paràmetres, servo amb PWM, `mou_servo()`/`saluda()` de `funcions_moviments.py`.

**Requisit mínim.**
- Parteix de `funcions_moviments.py`: `saluda(vegades)` i `escombra(angle_maxim)` (ja fet).
- Escriu una funció nova `salutacio(estil, vegades)` amb **dos** paràmetres: `estil` (`'curt'` o `'llarg'`) decideix si crida `saluda()` o `escombra()`.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Afegeix un **tercer estil** (`'doble'`) que combini `saluda()` i `escombra()` en una sola crida.
2. *(notable)* Fes que `salutacio()` també mostri una cara diferent al display segons l'`estil` triat.
3. *(⭐⭐⭐)* Activa la salutació amb el botó A i fes que cada premuda triï un `estil` diferent per torns (com una petita seqüència, igual que `control_per_botons.py`).

    **Fites** (valida-les en ordre):
    1. Els dos estils bàsics (`'curt'`/`'llarg'`) es distingeixen clarament en el moviment del servo.
    2. El tercer estil (ampliació 1) combina els dos anteriors sense repetir codi.
    3. La seqüència per botó (ampliació 3) canvia d'estil de manera fiable a cada premuda.

---

## ⭐⭐ Repte 2 · Aparcament automàtic de precisió

**Context.** Un fabricant de robots de neteja vol que el seu prototip s'aproximi lentament a la seva base de càrrega i s'aturi amb suavitat, en lloc de frenar de cop.

> *Client: fabricant de robots domèstics · Lliurable: rutina d'aproximació amb frenada progressiva · Món real: aparcament automàtic, robots aspiradors que tornen a la base.*

**Què treballa.** Funcions de moviment (`avancar`, `aturar`), PWM progressiu, bucles amb `range`.

**Requisit mínim.**
- Parteix de `velocitat_pwm.py`: `avancar(velocitat)` i `aturar()` (ja fet).
- Escriu una funció `frenada(velocitat_inicial)` que redueixi la velocitat **de mica en mica** (com `respira()` a la SA2) fins a aturar-se del tot, en lloc de cridar `aturar()` directament.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Fes que la funció `arrencada(velocitat_final)` faci el mateix però a l'inrevés (pujada progressiva en lloc de baixada).
2. *(notable)* Combina `arrencada()` + `avancar()` (temps fix) + `frenada()` en una única funció `trajecte(velocitat, temps_avancant)`.
3. *(⭐⭐⭐)* Activa `trajecte()` amb el botó A i permet **dues** velocitats diferents segons si es prem A sol o A+B alhora.

    **Fites** (valida-les en ordre):
    1. La frenada progressiva es distingeix clarament d'una aturada brusca (`aturar()` directe).
    2. `trajecte()` encadena arrencada, avanç i frenada sense salts bruscos de velocitat.
    3. Les dues velocitats de l'ampliació 3 es diferencien clarament en el moviment del vehicle.

---

## ⭐⭐⭐ Repte 3 · Coreografia de benvinguda amb servo, so i motors

**Context.** Una empresa d'esdeveniments vol un petit robot de benvinguda per a una fira: quan s'acosta algú, fa una petita coreografia (moviment + so) i després avança uns instants cap al visitant.

> *Client: empresa d'organització d'esdeveniments · Lliurable: coreografia de benvinguda combinada · Món real: robots de recepció, mascotes animatròniques d'esdeveniments.*

**Què treballa.** Funcions que en criden d'altres (`coreografia.py`), funcions de moviment del vehicle (`velocitat_pwm.py`), seqüències amb estat.

**Requisit mínim.**
- Parteix de `coreografia.py` (servo + so + display) i `velocitat_pwm.py` (motors): combina'ls en una funció `benvinguda()` que faci **primer** la part de servo/so/display i **després** un avanç breu del vehicle.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Afegeix una funció `comiat()` simètrica a `benvinguda()` (per exemple, recular en lloc d'avançar).
2. *(notable)* Encadena `benvinguda()` i `comiat()` en una seqüència activada amb els botons A/B (com `control_per_botons.py`), amb el botó B aturant-ho tot immediatament, es processi on es processi.
3. *(⭐⭐⭐)* Fes que la velocitat del vehicle a `benvinguda()`/`comiat()` sigui un **paràmetre** propi de cada crida, i documenta al quadern per què has triat aquests valors.

    **Fites** (valida-les en ordre):
    1. `benvinguda()` combina de manera clara i seguida servo/so/display i moviment del vehicle.
    2. La seqüència per botons (ampliació 2) s'interromp de manera fiable amb el botó B en qualsevol moment.
    3. El paràmetre de velocitat (ampliació 3) canvia visiblement el comportament sense tocar la resta del codi.

---

## 🎨 Fes-lo teu (tria abans de començar)

> El repte fixa **què** ha de fer el sistema; **el context el poses tu**. Tria i anota-ho al quadern — un producte amb decisions teves sempre s'explica i es defensa millor:
> - **Repte 1:** decideix els teus **estils** de salutació i les seves cares al display.
> - **Repte 2:** tria les teves **velocitats** d'arrencada/frenada i el temps del trajecte.
> - **Repte 3:** tria la teva **coreografia** de benvinguda/comiat i la velocitat del vehicle.

## Material necessari (els tres reptes)

- micro:bit V2 + Micro:shield + cable micro-USB.
- Kit Keyestudio 2 (micro servo, motoreductors) i portapiles, muntats segons [`SA4_esquemes_connexions.md`](../Classes/SA4/SA4_esquemes_connexions.md).
- El simulador de python.microbit.org **només** serveix per revisar la lògica (paràmetres, seqüències, botons): el servo i els motors cal provar-los amb maquinari real.

## Per on començar (mètode de projecte + PRIMM)

1. **Analitzar:** quines funcions ja tinc fetes que puc reutilitzar, i quin paràmetre nou necessito?
2. **Dissenyar (Predir):** escriu *abans* què esperes que passi amb els paràmetres que triïs.
3. **Programar/Prototipar:** parteix del programa base de `Classes/SA4/codi/` i modifica'l.
4. **Provar:** executa'l amb el maquinari real, observa, compara amb la teva predicció.
5. **Millorar:** afegeix una ampliació i documenta-la.

## Com s'avalua

| Rúbrica | Per què |
|---|---|
| **R1** (codi) | Funcionament, estructura (funcions ben nomenades i reutilitzades), depuració. |
| **R2** (muntatge) | Muntatge correcte i segur del servo/motoreductors. |
| **R4** (documentació) | Quadern tècnic: predicció, solució i millora. |
| **R5** (actitud) | Autonomia, gestió de l'error. |

## Producte / entrega

- Codi `.py` comentat + entrada al **quadern tècnic** (predicció, què he fet, error trobat i millora).

---

## Orientació docent

- **Errors freqüents:** escriure codi repetitiu enlloc de convertir-lo en funció amb paràmetre; oblidar el `return` en funcions que calculen un valor; alimentar servo/motors només per USB; enviar PWM als dos pins d'un motor alhora.
- **Diferenciació:** el mínim és idèntic per a tothom → tothom assoleix la base; les ampliacions 2-3 introdueixen combinacions de funcions, seqüències amb botons i paràmetres addicionals per a qui va sobrat.
- **Gestió d'aula:** tots requereixen maquinari real per a la part de servo/motors (el simulador només valida la lògica); el repte 3 reaprofita el muntatge complet del vehicle (servo de la mascota + motors del vehicle).
- **Vincle avaluació:** producte coherent amb el de la SA4 (quadern tècnic, R4/R5) i amb les rúbriques R1/R2 del repte «control per botons».
