# Prova pràctica — Trimestre 2 (SA4-SA6)
## "Vehicle amb màquina d'estats + control amb histèresi"

**Durada:** una sessió sencera — **la S4 de la SA6** (~95-100' efectius de prova, més instruccions i recollida) · **Individual** · **Material:** el vehicle T2 propi (muntat a SA4), 2 micro:bit (vehicle + comandament d'una parella, o simulador per assajar el protocol). Es permet consultar esquemes i el quadern tècnic.

> ℹ️ Aquesta prova **no reutilitza el «vehicle amb aturada d'emergència»** (producte de la SA6, ja tancat i avaluat a la Sessió 3): és un programa nou, individual, sobre el mateix vehicle.

### Competències i criteris avaluats
- **CE-R3** (control) → CA3.1 · **CE-R1** (programar) → CA1.1 · **CE-R2** (sensors/circuits) → CA2.1
- Rúbriques: **R1** (codi), **R3** (control), **R4** (documentació).

---

## Enunciat (dues parts)

### PART A — Vehicle amb màquina d'estats (nucli + ampliacions + ítem obligatori, 6,5 punts)
1. **Nivell satisfactori (nucli):** programa una **màquina d'estats RUN/STOP** que rebi ordres per ràdio amb el protocol **`CMD:`** (`F`/`B`/`L`/`R`/`S`), reutilitzant les funcions de moviment `avancar()`/`retrocedir()`/`girar()`/`aturar()` ja fetes a la SA4-SA5.
2. **Ampliació (notable):** afegeix un **polsador STOP** (P12, *pull-up*) amb **prioritat màxima**: s'ha de comprovar **abans** que qualsevol ordre de ràdio, a cada volta del bucle.
3. **Ampliació (excel·lent):** afegeix un **LED indicador d'estat** (P1): encès fix quan el vehicle és a RUN, apagat quan és a STOP.
4. **Ítem obligatori (2 punts): escriu una funció NOVA.** Escriu una funció pròpia, amb **un paràmetre i un valor de retorn**, que **converteixi una magnitud** del vehicle — per exemple, `percentatge_a_velocitat(percentatge)` que passi un percentatge de velocitat (0-100) al valor PWM que accepta `write_analog()` (0-1023) — i **fes-la servir realment al programa** (p. ex. per fixar `VELOCITAT`). No n'hi ha prou de definir-la: cal cridar-la i utilitzar el valor que retorna.

### PART B — Control amb histèresi + registre (nucli + ampliació, 3 punts)
5. **Nivell satisfactori (nucli):** programa un **control tot/res amb histèresi** (dos llindars, no un de sol) sobre la temperatura **interna** de la micro:bit, que engegui/aturi un actuador (relé o LED a P2).
6. **Ampliació:** **registra les lectures** amb el mòdul natiu `log` (`log.set_labels()` + `log.add()`), com a evidència per al quadern (puntua dins de l'ítem de documentació).

### ÍTEM OBLIGATORI DE DEPURACIÓ (1 punt) — «aquest programa falla: arregla'l»
7. Un company ha escrit aquest fragment per a la Part B i **peta en executar-se**. Aquí tens el codi i el **traceback real**:

```python
llindar = "25"

while True:
    if temperature() > llindar:
        display.show(Image.NO)
    else:
        display.show(Image.YES)
    sleep(500)
```

```
Traceback (most recent call last):
  File "main.py", line 4, in <module>
TypeError: unsupported types for __gt__: 'int', 'str'
```

**(a)** Llegeix el traceback i explica **en una o dues frases** què diu i per què passa (quina línia, quins tipus xoquen). **(b)** Arregla **la línia responsable** (n'hi ha prou de canviar-ne una) i justifica el canvi. *(No cal maquinari: es respon per escrit al full de la prova.)*

### Lliurament
Els dos programes funcionant (o la seva lògica assajada al simulador, si el maquinari no ho permet en aquell moment) + **quadern**: diagrama de la màquina d'estats (Part A) i taula amb almenys una lectura registrada (Part B).

### Pla de millora personal (després de la prova — 3 línies, no puntua)
> Quan rebis el retorn, escriu al quadern: **(1)** què m'ha fallat o m'ha costat més · **(2)** què practicaré concretament · **(3)** com comprovaré que ja ho tinc.
> El docent **recupera aquestes 3 línies a l'inici de la SA7**. Al 3r trimestre tot conflueix al projecte: el que quedi coix aquí, allà es notarà — millor tapar-ho ara.

---

## Graella de correcció (10 punts)

| Criteri | Punts | CA | Rúbrica |
|---|---|---|---|
| Part A: FSM RUN/STOP amb ordres per ràdio (`CMD:`) funcional (nucli) | 3 | CA1.1, CA3.1 | R1, R3 |
| Part A: polsador STOP prioritari + LED indicador d'estat (ampliacions) | 1 | CA3.1 | R3 |
| **Part A: escriu una funció nova amb paràmetre i retorn (obligatori)** | **2** | **CA1.1** | **R1** |
| Part B: control tot/res amb histèresi funcional (nucli) | 2,5 | CA2.1, CA3.1 | R1, R3 |
| **Ítem de depuració: llegir el traceback, explicar la causa i arreglar la línia (obligatori)** | **1** | **CA1.1** | **R1** |
| Documentació (diagrama d'estats + taula de dades del registre `log`) | 0,5 | CA3.1 | R4 |

> Orientació: nuclis + els dos ítems obligatoris ben fets ≈ 6; amb les ampliacions ≈ 7-8; amb tot i bona documentació ≈ 9-10.
> Reequilibri de barem (4a ronda): els ítems «funció nova» (2 p) i «depuració amb traceback» (1 p) són **obligatoris**, no ampliacions — puntuen encara que no es facin les ampliacions. Per fer-hi lloc sense superar els 10 punts, les ampliacions mecàniques s'han compactat (STOP+LED en un sol ítem d'1 punt; el registre `log` puntua dins de la documentació); el nucli de lògica (FSM i histèresi) es manté intacte.

---

## Solució orientativa (docent)

> ⚠️ **Nota física:** l'histèresi de la Part B es prova amb `temperature()` (sensor intern): és una simplificació acceptada per a la prova, coherent amb `termostat_histeresi.py` (SA6); no cal cap conversió ADC → °C.

### Part A — FSM RUN/STOP amb ràdio i STOP prioritari

**Cablatge (`00_Fil_conductor_construccions.md` §1b, vehicle T2):** M1=P13/P14, M2=P15/P16, LED indicador=P1, polsador STOP=P12 (*pull-up* intern).

<details markdown="1">
<summary>Desplega el codi complet (<code>prova_t2_vehicle_fsm.py</code>)</summary>

```python
# Prova practica T2 - PART A - SOLUCIO ORIENTATIVA (docent, NO es lliura)
# NUCLI (satisfactori): maquina d'estats RUN/STOP controlada per ordres de
# radio amb el protocol "CMD:" (F/B/L/R/S), reutilitzant EXACTAMENT les
# funcions de moviment de la SA4/SA5 (avancar/retrocedir/girar/aturar).
# Ampliacio (notable): polsador STOP (P12, pull-up) amb prioritat maxima,
# comprovat SEMPRE abans que la radio a cada volta del bucle (mateix patro
# que vehicle_seguretat.py, SA6).
# Ampliacio (excel-lent): LED indicador d'estat (P1): ences fix = RUN,
# apagat = STOP.
# Item NOU (obligatori, 2 punts): funcio propia amb UN PARAMETRE i VALOR DE
# RETORN que converteix una magnitud (percentatge de velocitat 0-100) al
# valor PWM que accepta write_analog() (0-1023), i que es fa servir de
# veritat al programa per fixar VELOCITAT (no nomes definida, tambe usada).
# Cablatge (00_Fil_conductor_construccions.md #1b, vehicle T2): M1=P13/P14,
# M2=P15/P16, LED indicador=P1, polsador STOP=P12 (pull-up intern).
# Simulador: python.microbit.org NO simula els motors; nomes es pot provar
# la LOGICA de la maquina d'estats i del protocol de radio (dues pestanyes).

from microbit import *
import radio

GRUP = 1   # ha de coincidir amb el GRUP de la placa que envia les ordres

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

LED_ESTAT = pin1
POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)   # repos = 1, premut = 0


def percentatge_a_velocitat(percentatge):
    # ITEM NOU (obligatori, 2 punts): funcio NOVA, amb parametre i retorn,
    # que converteix una magnitud (percentatge 0-100) al rang PWM real
    # (0-1023) que necessiten write_analog(). Es crida mes avall i el
    # resultat es fa servir com a VELOCITAT: no nomes es defineix, s'usa.
    return int(percentatge * 1023 / 100)


VELOCITAT = percentatge_a_velocitat(40)   # ~40% de la velocitat maxima

RUN, STOP = range(2)
estat = STOP


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def retrocedir(velocitat):
    M1_ENRERE.write_analog(velocitat)
    M1_ENDAVANT.write_digital(0)
    M2_ENRERE.write_analog(velocitat)
    M2_ENDAVANT.write_digital(0)


def girar(costat, velocitat=300):
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat)
        M1_ENDAVANT.write_digital(0)
        M2_ENDAVANT.write_analog(velocitat)
        M2_ENRERE.write_digital(0)
    elif costat == 'dreta':
        M1_ENDAVANT.write_analog(velocitat)
        M1_ENRERE.write_digital(0)
        M2_ENRERE.write_analog(velocitat)
        M2_ENDAVANT.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def actualitza_led():
    # AMPLIACIO (excel-lent): un unic lloc que reflecteix l'estat al LED.
    LED_ESTAT.write_digital(1 if estat == RUN else 0)


def actualitza_estat(nou):
    # UNIC lloc que canvia "estat": perque cap altra part del programa
    # pugui "oblidar-se" d'aturar els motors en entrar a STOP.
    global estat
    if nou == STOP:
        aturar()
        display.show(Image.NO)
    estat = nou
    actualitza_led()


actualitza_estat(STOP)

while True:
    # AMPLIACIO (notable): prioritat maxima, comprovada SEMPRE la primera.
    if not POLSADOR_STOP.read_digital():
        actualitza_estat(STOP)

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ordre = missatge[len(PREFIX):]
        if ordre == "S":
            actualitza_estat(STOP)
        elif estat == STOP and ordre in ("F", "B", "L", "R"):
            # Sortir de STOP nomes amb una ordre de moviment explicita.
            actualitza_estat(RUN)

        if estat == RUN:
            if ordre == "F":
                display.show(Image.ARROW_N)
                avancar(VELOCITAT)
            elif ordre == "B":
                display.show(Image.ARROW_S)
                retrocedir(VELOCITAT)
            elif ordre == "L":
                display.show(Image.ARROW_W)
                girar('esquerra')
            elif ordre == "R":
                display.show(Image.ARROW_E)
                girar('dreta')

    sleep(20)
```

</details>

**Què mirar en corregir el nucli:** (1) el polsador es comprova **abans** de processar la ràdio, a cada volta; (2) `actualitza_estat()` és l'únic lloc que canvia `estat` (mai s'assigna la variable directament en cap altre punt); (3) sortir de STOP exigeix una ordre de moviment explícita, no qualsevol missatge. Error típic: comprovar el polsador només dins del `if missatge is not None` — llavors l'STOP no funciona quan no arriba cap ordre de ràdio.

**Què mirar a l'ítem obligatori «funció nova» (2 punts):** (1) la funció és **realment nova** (no una còpia amb un altre nom de `avancar`/`girar`/etc.); (2) té **un paràmetre** i **una instrucció `return`** que aporta un valor útil; (3) el programa **crida la funció i usa el valor retornat** — definir-la sense usar-la no puntua. Qualsevol funció de conversió coherent amb el vehicle és vàlida (percentatge→PWM, cm→temps de gir, etc.); l'exemple `percentatge_a_velocitat()` és només orientatiu.

### Part B — Control amb histèresi + registre amb `log`

<details markdown="1">
<summary>Desplega el codi complet (<code>prova_t2_histeresi_log.py</code>)</summary>

```python
# Prova practica T2 - PART B - SOLUCIO ORIENTATIVA (docent, NO es lliura)
# NUCLI (satisfactori): control tot/res AMB HISTERESI (dos llindars) sobre
# la temperatura interna, exactament el mateix patro que
# termostat_histeresi.py (SA6): un unic llindar faria "clic-clic" quan la
# lectura balla al voltant seu.
# Ampliacio (notable/excel-lent): registre de les lectures amb el modul
# "log" natiu de la V2 (igual que registre_dades.py, SA6), per documentar
# el quadern amb dades reals sense cap ordinador connectat mentre es grava.
# Maquinari: temperature() interna (cap cablatge nou); rele/LED d'ampliacio
# al pin2 (00_Fil_conductor_construccions.md #1b: rele = P2 al vehicle T2).
# Simulador: python.microbit.org simula temperature() i el modul log, pero
# NO simula el rele/actuador extern: nomes se'n pot provar la logica.

from microbit import *
import log

ACTUADOR = pin2   # rele (o LED, si no hi ha rele a ma: mateix comportament)

LLINDAR_BAIX = 24   # per sota d'aixo, activa (te fred)
LLINDAR_ALT = 26     # per sobre d'aixo, desactiva (ja no te fred)

log.set_labels('temp', 'actiu')

actiu = False   # variable d'estat: no nomes la lectura instantania
ACTUADOR.write_digital(0)

while True:
    temp = temperature()

    if not actiu and temp < LLINDAR_BAIX:
        actiu = True
    elif actiu and temp > LLINDAR_ALT:
        actiu = False
    # Si temp esta ENTRE els dos llindars, NO es toca "actiu": aixo es la
    # histeresi (error tipic: un sol "if temp > LLINDAR" -> tot/res SENSE
    # histeresi, no assoliria el nucli sencer).

    ACTUADOR.write_digital(1 if actiu else 0)
    display.show(Image.HEART if actiu else Image.NO)

    log.add(temp=temp, actiu=int(actiu))

    sleep(500)
```

</details>

**Què mirar en corregir el nucli:** (1) dos llindars diferents i separats (no un de sol); (2) `actiu` es manté dins de la banda entre els dos llindars; (3) l'actuador reflecteix sempre `actiu`. Error típic: comparar `temp` amb un únic `LLINDAR` — histèresi absent.

### Ítem de depuració — resposta esperada

**(a)** El traceback assenyala la **línia 4** (`if temperature() > llindar:`) i diu que no es poden comparar amb `>` un **enter** (`temperature()` retorna un `int`) i un **text** (`llindar` val `"25"`, amb cometes): `TypeError: unsupported types for __gt__: 'int', 'str'`.
**(b)** Arreglar la línia responsable, que és la **primera** (`llindar = "25"` → `llindar = 25`, sense cometes; també s'accepta `int(llindar)` a la comparació). Justificació: el llindar ha de ser un número per poder-se comparar amb una temperatura.

**Barem (1 punt):** 0,5 la lectura del traceback (línia + tipus que xoquen, amb paraules pròpies) · 0,5 l'arreglada correcta amb justificació. **0** si només reescriu el programa sencer de memòria sense explicar la causa. Compte: l'error és a la línia 1, però el traceback assenyala la 4 (on esclata) — entendre aquesta diferència és exactament el que avalua l'ítem.

> Avaluació global del trimestre: combinar el resultat d'aquesta prova amb el producte «vehicle amb aturada d'emergència» (S3 de SA6, dimensió «Projectes i productes») — cap evidència no compta dues vegades.
