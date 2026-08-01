# Prova pràctica — Trimestre 2 (SA4-SA6)
## "Vehicle amb màquina d'estats + control amb histèresi"

**Durada:** una sessió sencera — **la S4 de la SA6** (~95-100' efectius de prova, més instruccions i recollida) · **Individual** · **Material:** el vehicle T2 propi (muntat a SA4), 2 micro:bit (vehicle + comandament d'una parella, o simulador per assajar el protocol). Es permet consultar esquemes i el quadern tècnic.

> ℹ️ Aquesta prova **no reutilitza el «vehicle amb aturada d'emergència»** (producte de la SA6, ja tancat i avaluat a la Sessió 3): és un programa nou, individual, sobre el mateix vehicle.

### Competències i criteris avaluats
- **CE-R3** (control) → CA3.1 · **CE-R1** (programar) → CA1.1 · **CE-R2** (sensors/circuits) → CA2.1
- Rúbriques: **R1** (codi), **R3** (control), **R4** (documentació).

---

## Enunciat (dues parts)

### PART A — Vehicle amb màquina d'estats (nucli + ampliacions, 6 punts)
1. **Nivell satisfactori (nucli):** programa una **màquina d'estats RUN/STOP** que rebi ordres per ràdio amb el protocol **`CMD:`** (`F`/`B`/`L`/`R`/`S`), reutilitzant les funcions de moviment `avancar()`/`retrocedir()`/`girar()`/`aturar()` ja fetes a la SA4-SA5.
2. **Ampliació (notable):** afegeix un **polsador STOP** (P12, *pull-up*) amb **prioritat màxima**: s'ha de comprovar **abans** que qualsevol ordre de ràdio, a cada volta del bucle.
3. **Ampliació (excel·lent):** afegeix un **LED indicador d'estat** (P1): encès fix quan el vehicle és a RUN, apagat quan és a STOP.

### PART B — Control amb histèresi + registre (nucli + ampliació, 4 punts)
4. **Nivell satisfactori (nucli):** programa un **control tot/res amb histèresi** (dos llindars, no un de sol) sobre la temperatura **interna** de la micro:bit, que engegui/aturi un actuador (relé o LED a P2).
5. **Ampliació:** **registra les lectures** amb el mòdul natiu `log` (`log.set_labels()` + `log.add()`), com a evidència per al quadern.

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
| Part A: polsador STOP prioritari (ampliació) | 1,5 | CA3.1 | R3 |
| Part A: LED indicador d'estat (ampliació) | 1 | CA1.1 | R1, R3 |
| Part B: control tot/res amb histèresi funcional (nucli) | 2,5 | CA2.1, CA3.1 | R1, R3 |
| Part B: registre amb el mòdul `log` (ampliació) | 1 | CA1.1 | R1 |
| Documentació (diagrama d'estats + taula de dades) | 1 | CA3.1 | R4 |

> Orientació: nucli de les dues parts ben fet ≈ 5-6; amb una ampliació de cada part ≈ 7-8; amb totes i bona documentació ≈ 9-10.

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

VELOCITAT = 400

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

> Avaluació global del trimestre: combinar el resultat d'aquesta prova amb el producte «vehicle amb aturada d'emergència» (S3 de SA6, dimensió «Projectes i productes») — cap evidència no compta dues vegades.
