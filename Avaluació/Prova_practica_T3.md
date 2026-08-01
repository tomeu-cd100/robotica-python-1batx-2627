# Prova pràctica — Trimestre 3 (SA7-SA8)
## "Rover autònom + telemetria"

**Durada:** 2 h (la **S5 de la SA9**, sencera) · **Individual, per estacions rotatives** · **Material:** el rover T3 propi (muntat a la Sessió 0 i SA7), pista de proves compartida, micro:bit de la parella per a la telemetria. Es permet consultar esquemes i el quadern tècnic.

> ℹ️ Al 3r trimestre **el pes principal de l'avaluació és el projecte final (SA9)** amb les rúbriques R1-R5 i el dossier tècnic, tancat i defensat a la **S4**. Aquesta prova pràctica és un instrument **separat i individual**: comprova destreses de robòtica i integració (SA7-SA8), puntua **només** a la dimensió «Proves pràctiques» (20 %) i **no reavalua el projecte**. Cap evidència no compta dues vegades.

### Logística: estacions rotatives (poques pistes, tot el grup alhora)

Amb 2-3 pistes no es pot fer la Part A tothom alhora. Organització de la sessió (detall complet a `Classes/SA9/SA9_guia_docent.md` §Organització de la S5):

1. **Tota la classe comença per la Part B** (taula, individual, sense rover): 40-45'.
2. **Part A per torns a les pistes** (10-12' per persona i pista), mentre la resta acaba la Part B i **verifica el codi de la Part A** al banc o al simulador (per a la lògica de radio/protocol; motors i sensors **no** es simulen).
3. Ordre de torns publicat a l'inici; qui ha passat per la pista completa la documentació del quadern.
4. El docent només observa i cronometra a la pista; la correcció de codi es fa després amb el quadern i el codi lliurat.

### Competències i criteris avaluats
- **CE-R4** (robots) → CA4.1, CA4.2 · **CE-R3** (control) → CA3.1
- Rúbriques: **R1** (codi), **R3** (robot/control), **R4** (documentació).

---

## Enunciat (per nivells)

### PART A — Rover a la pista (6 punts)
Programa el rover perquè, sobre la pista marcada:
1. **Nivell satisfactori (nucli):** faci un **recorregut definit i calibrat** (recte + gir de 90° + recte) de manera fiable, compensant la diferència entre motors (com a `calibratge_motors.py`).
2. **Ampliació (notable):** **reaccioni a un obstacle** amb l'HC-SR04 (trigger P1, echo P2): s'atura i l'esquiva.
3. **Ampliació (excel·lent):** **segueixi una línia** amb el sensor KS0050 (P0), corregint la trajectòria cap al costat on la perd.

### PART B — Telemetria a la taula (4 punts)
4. **Nivell satisfactori (nucli):** programa (**sense rover, només la placa**) l'enviament d'una **lectura per ràdio** amb el prefix **`TEL:`** (format clau:valor separat per `;`, com a `telemetria_radio.py`/`estacio_base.py`).
5. **Ampliació:** integra una **decisió a partir d'una ordre rebuda** amb un prefix diferent (**`CMD:`**), de manera que una acció (per exemple, prémer un botó) dispari un comportament (com aturar el rover en un sistema real).

### Lliurament
Demostració a la pista (Part A) + programa de telemetria (Part B) + **explicació al quadern**: estratègia del recorregut/comportament (Part A) i descripció del protocol `TEL:`/`CMD:` (Part B).

### Reflexió final de curs (3 línies, no puntua)
> Última entrada del quadern: **(1)** la competència de què estic més orgullós/osa aquest curs · **(2)** el que encara em costa · **(3)** on ho continuaré (batxillerat tecnològic, Treball de Recerca, projecte propi, competició…). Tanca el quadern com el vas obrir: mirant el procés, no només la nota.

---

## Graella de correcció (10 punts)

| Criteri | Punts | Rúbrica |
|---|---|---|
| Part A: recorregut fix calibrat i fiable (nucli) | 3 | R1, R3 |
| Part A: reacció a obstacle amb HC-SR04 (ampliació) | 1,5 | R3 |
| Part A: seguidor de línia (ampliació) | 1,5 | R3 |
| Part B: telemetria per ràdio amb prefix `TEL:` (nucli) | 2 | R1 |
| Part B: integració decisió/ordre `CMD:` en el comportament (ampliació) | 1 | R1, R3 |
| Documentació (estratègia del recorregut + protocol de ràdio) | 1 | R4 |

> Orientació: nucli de les dues parts ben fet ≈ 5-6; amb una ampliació ≈ 7-8; amb totes i bona documentació ≈ 9-10.

---

## Solució orientativa (docent)

**Cablatge (`00_Fil_conductor_construccions.md` §1b, rover T3):** M1=P13/P14, M2=P15/P16 (heretats, no es toquen), HC-SR04 trigger=P1 echo=P2, seguidor de línia=P0.

### Part A — recorregut, evita-obstacles i seguidor de línia (combinats en un únic fitxer per facilitar la correcció per torns)

<details markdown="1">
<summary>Desplega el codi complet (<code>prova_t3_rover.py</code>)</summary>

```python
# Prova practica T3 - PART A (pista) - SOLUCIO ORIENTATIVA (docent, NO es
# lliura). Un unic fitxer amb els TRES nivells seleccionables amb els
# botons A/B en arrencar (comode per a la correccio per torns a la pista):
#   A -> recorregut fix calibrat (NUCLI, satisfactori)
#   B -> evita obstacles amb HC-SR04 (AMPLIACIO, notable)
#   cap boto en 3 s -> segueix la linia amb el sensor P0 (AMPLIACIO, excel-lent)
# Cablatge (00_Fil_conductor_construccions.md #1b, rover T3): M1=P13/P14,
# M2=P15/P16 (heretats, no es toquen), HC-SR04 trigger=P1 echo=P2,
# seguidor de linia=P0.
# Simulador: cap d'aquests tres comportaments es simula (motors, HC-SR04 i
# seguidor de linia nomes funcionen amb el rover real).

from microbit import *
import machine
import utime

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

TRIGGER = pin1
ECHO = pin2
SEGUIDOR_LINIA = pin0

VELOCITAT_SO_CM_US = 0.0343
LLINDAR_OBSTACLE_CM = 15
LLINDAR_LINIA = 500

VELOCITAT_AVANCAR = 400
VELOCITAT_GIR = 300
T_GIR_90_MS = 450   # temps de gir per fer aprox. 90 graus: calibra'l al banc

FACTOR_M1 = 1.0
FACTOR_M2 = 0.92    # exemple de calibratge (motor dret una mica mes fluix)


def avancar(velocitat):
    # Calibratge (SA7): cada motor rep la seva propia velocitat compensada,
    # no la mateixa consigna crua, perque el rover vagi recte de veritat.
    M1_ENDAVANT.write_analog(int(velocitat * FACTOR_M1))
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(int(velocitat * FACTOR_M2))
    M2_ENRERE.write_digital(0)


def girar(costat, velocitat=VELOCITAT_GIR):
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


def mesura_distancia():
    TRIGGER.write_digital(0)
    utime.sleep_us(2)
    TRIGGER.write_digital(1)
    utime.sleep_us(10)
    TRIGGER.write_digital(0)
    durada_us = machine.time_pulse_us(ECHO, 1, 30000)
    if durada_us < 0:
        return None   # cap eco rebut (fora de rang)
    return (durada_us * VELOCITAT_SO_CM_US) / 2


def recorregut_fix():
    # NUCLI: recte + gir de 90 graus + recte, de manera fiable.
    avancar(VELOCITAT_AVANCAR)
    sleep(1500)
    aturar()
    sleep(200)
    girar('dreta')
    sleep(T_GIR_90_MS)
    aturar()
    sleep(200)
    avancar(VELOCITAT_AVANCAR)
    sleep(1500)
    aturar()
    display.show(Image.YES)


def evita_obstacles(durada_ms=8000):
    # AMPLIACIO (notable): s'atura i esquiva en detectar un obstacle proper.
    inici = running_time()
    while running_time() - inici < durada_ms:
        distancia = mesura_distancia()
        if distancia is not None and distancia < LLINDAR_OBSTACLE_CM:
            aturar()
            display.show(Image.NO)
            girar('esquerra')
            sleep(400)
        else:
            avancar(VELOCITAT_AVANCAR)
            display.show(Image.ARROW_N)
        sleep(50)
    aturar()


def segueix_linia(durada_ms=8000):
    # AMPLIACIO (excel-lent): correccio proporcional simple cap al costat
    # on es perd la linia (amb un unic sensor, es tria un costat fix de cerca).
    inici = running_time()
    while running_time() - inici < durada_ms:
        lectura = SEGUIDOR_LINIA.read_analog()
        if lectura < LLINDAR_LINIA:
            avancar(VELOCITAT_AVANCAR)
            display.show(Image.ARROW_N)
        else:
            girar('esquerra', VELOCITAT_GIR)
            display.show(Image.ARROW_W)
        sleep(20)
    aturar()


display.show(Image.TARGET)
inici_tria = running_time()
opcio = None
while running_time() - inici_tria < 3000:
    if button_a.was_pressed():
        opcio = 'A'
        break
    if button_b.was_pressed():
        opcio = 'B'
        break

if opcio == 'A':
    recorregut_fix()
elif opcio == 'B':
    evita_obstacles()
else:
    segueix_linia()
```

</details>

**Què mirar en corregir el nucli:** (1) el rover avança **recte de veritat** (calibratge de `FACTOR_M1`/`FACTOR_M2`, no motors "a pèl"); (2) el gir de 90° és repetible (`T_GIR_90_MS` mesurat, no a ull); (3) el recorregut acaba amb el rover aturat, no en marxa indefinida.

### Part B — telemetria (`TEL:`) i integració d'una ordre (`CMD:`)

<details markdown="1">
<summary>Desplega el codi complet (<code>prova_t3_telemetria.py</code>)</summary>

```python
# Prova practica T3 - PART B (taula) - SOLUCIO ORIENTATIVA (docent, NO es
# lliura). Programa de TAULA, sense rover: es fa amb la placa sola durant
# la primera part de la sessio (mentre la resta del grup fa la Part A per
# torns a la pista).
# NUCLI (satisfactori): telemetria per radio (prefix "TEL:", mateix format
# clau:valor separat per ";" que telemetria_radio.py/estacio_base.py, SA8).
# Ampliacio: integra la dada en una decisio -> accio: un boto envia una
# ordre "CMD:STOP" (protocol diferent del "TEL:", com exigeix la fitxa 17)
# que, en un rover real, aturaria els motors en rebre-la.
# Maquinari: cap component nou, nomes la radio interna i el display.
# Simulador: la radio SI es simula (dues pestanyes obertes alhora): es pot
# provar tot el protocol sense maquinari.

from microbit import *
import radio

GRUP = 10   # ha de coincidir amb el GRUP de la placa parella (banc de proves)

radio.on()
radio.config(group=GRUP)

PREFIX_TEL = "TEL:"
PREFIX_CMD = "CMD:"

LLINDAR_ALERTA = 28   # graus C
aturat = False

INTERVAL_MS = 2000
ultim_enviament = running_time()


def envia_lectura():
    # NUCLI: mesura i transmet una dada (telemetria) amb el prefix "TEL:".
    temp = temperature()
    alerta = "1" if temp > LLINDAR_ALERTA else "0"
    radio.send(PREFIX_TEL + "T:" + str(temp) + ";A:" + alerta)
    display.show(Image.NO if alerta == "1" else Image.YES)


while True:
    if button_a.was_pressed():
        # AMPLIACIO: una ordre per radio integrada en el comportament
        # (equivalent, en un rover real, a aturar els motors en rebre-la).
        radio.send(PREFIX_CMD + "STOP")

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX_CMD):
        ordre = missatge[len(PREFIX_CMD):]
        if ordre == "STOP":
            aturat = True
            display.show(Image.SKULL)

    if not aturat:
        ara = running_time()
        if ara - ultim_enviament >= INTERVAL_MS:
            ultim_enviament = ara
            envia_lectura()

    sleep(20)
```

</details>

**Què mirar en corregir el nucli:** (1) el missatge de telemetria porta el prefix `TEL:` i camps `clau:valor` separats per `;`; (2) l'enviament es llença **a intervals** (`running_time()`), no a cada volta del bucle; (3) el prefix `CMD:` de l'ampliació és **diferent** del `TEL:`, perquè la placa receptora no confongui una ordre amb una dada.

> Avaluació global del trimestre: combinar el resultat d'aquesta prova amb la rúbrica del **projecte final (SA9)**, defensat a la S4 — instruments separats, cap evidència no compta dues vegades.
