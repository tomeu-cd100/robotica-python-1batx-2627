# Solucionari de les proves pràctiques T1, T2 i T3

Material del **docent**: no es lliura a l'alumnat. Codi complet i orientacions de correcció de les tres proves pràctiques trimestrals (`Avaluació/Prova_practica_T1.md`, `T2.md`, `T3.md`). El codi complet incrustat aquí és una **còpia exacta** dels fitxers de `Classes/Solucionari/codi/` (`tools/qa.py:comprova_codi_incrustat()` ho vigila).

---

## T1 (SA1-SA3) — "Estació personal d'alertes"

Enunciat complet, graella i solució raonada: [`Avaluació/Prova_practica_T1.md`](../../Avaluació/Prova_practica_T1.md).

**Resum de correcció:** nucli = botons A/B amb `is_pressed()` (SA1-SA3; `was_pressed()` no s'ensenya fins la SA4) + condicionals amb sensors interns (llum/temperatura) + lectura pel REPL; ampliacions = sensor extern (P0; no P3, que comparteix circuit amb el display) comparat amb l'intern, i acceleròmetre + micròfon amb codi organitzat en funcions.

<details markdown="1">
<summary>Desplega el codi complet (<code>prova_t1_solucio.py</code>)</summary>

```python
# Prova practica T1 - SOLUCIO ORIENTATIVA (docent, NO es lliura a l'alumnat)
# Tema: "estacio personal d'alertes" amb la micro:bit sola (sense muntar la
# mascota: aquesta prova es individual i separada del producte, ja tancat a
# la Sessio 3 de SA3).
# NUCLI (satisfactori): botons A/B per triar mode amb is_pressed() (SA1-SA3;
# was_pressed() NO s'ensenya fins la SA4 i no es pot exigir al nucli) +
# sensors INTERNS de llum i temperatura amb condicionals if/elif/else +
# lectura continua pel REPL (print) per depurar abans de fixar els llindars.
# NOTA: canviar de mode amb is_pressed() no necessita antirebot perque
# l'assignacio es IDEMPOTENT (mentre el boto es mante premut, cada volta
# torna a fixar el MATEIX mode: no hi ha cap comptador ni commutacio que
# es pugui "disparar" de mes).
# Ampliacio (notable): sensor de llum EXTERN del Kit 2 (P0, ADC) comparat
# amb l'intern (entrada analogica basica, mapa() de la SA3).
# Ampliacio (excel-lent): accelerometre (sacsejada) per confirmar l'alerta
# i microfon intern per detectar un soroll fort com a via addicional
# d'alerta; codi organitzat amb funcions (una responsabilitat per funcio).
# Maquinari: micro:bit V2 + Micro:shield; sensor de llum extern Kit 2 a P0
# (no P3: comparteix circuit amb el display, actiu en aquest programa;
# vegeu SA3_esquemes_connexions.md #1 i #2). Cap altre cablatge necessari:
# la resta son sensors interns.

from microbit import *
import music

LLINDAR_FOSCOR = 50        # 0-255, display.read_light_level() (calibra amb REPL)
LLINDAR_FRED = 18          # graus C, temperature()
LLINDAR_CALOR = 26         # graus C, temperature()
LLINDAR_SO = 150           # nivell del microfon intern (calibra amb REPL)

MODE_LLUM, MODE_TEMP = range(2)
mode = MODE_LLUM


def mapa(valor, entrada_min, entrada_max, sortida_min, sortida_max):
    # Mateixa funcio que nivell_llum.py/termometre.py (SA3): passa un valor
    # d'un rang d'entrada a un rang de sortida amb una regla de tres.
    rang_entrada = entrada_max - entrada_min
    rang_sortida = sortida_max - sortida_min
    proporcio = (valor - entrada_min) / rang_entrada
    return sortida_min + proporcio * rang_sortida


def mostra_mode():
    display.show(Image.ARROW_W if mode == MODE_LLUM else Image.ARROW_E)
    sleep(300)


def avalua_llum():
    # NUCLI: llum interna amb condicional + lectura pel REPL.
    intern = display.read_light_level()             # 0-255
    extern = pin0.read_analog()                      # 0-1023, sensor Kit 2
    extern_equivalent = mapa(extern, 0, 1023, 0, 255)
    print("llum intern:", intern, "extern (0-255):", round(extern_equivalent))

    if intern < LLINDAR_FOSCOR:
        display.show(Image.ASLEEP, wait=False, loop=False, delay=200)
    else:
        display.show(Image.SURPRISED, wait=False, loop=False, delay=200)
    sleep(400)


def avalua_temperatura():
    # NUCLI: temperatura interna amb if/elif/else + lectura pel REPL.
    temp = temperature()
    print("temperatura:", temp)

    if temp < LLINDAR_FRED:
        display.show(Image.SAD)
    elif temp > LLINDAR_CALOR:
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)


def comprova_alertes_ampliacio():
    # AMPLIACIO (excel-lent): dues vies mes d'alerta, cadascuna en la seva
    # propia funcio perque es puguin provar (i depurar) per separat.
    if accelerometer.was_gesture('shake'):
        display.show(Image.YES)   # sacsejada: confirma que l'alumne l'ha vist
        sleep(300)
    if microphone.sound_level() > LLINDAR_SO:
        music.pitch(1500, 100)    # so fort: avis agut i curt


while True:
    # NUCLI: is_pressed() (SA1-SA3), no was_pressed() (SA4). Idempotent:
    # mentre el boto es mante premut, es torna a fixar el mateix mode.
    if button_a.is_pressed():
        mode = MODE_LLUM
    if button_b.is_pressed():
        mode = MODE_TEMP
    mostra_mode()

    if mode == MODE_LLUM:
        avalua_llum()
    else:
        avalua_temperatura()

    comprova_alertes_ampliacio()
    sleep(200)
```

</details>

---

## T2 (SA4-SA6) — "Vehicle amb màquina d'estats + control amb histèresi"

Enunciat complet, graella i solució raonada: [`Avaluació/Prova_practica_T2.md`](../../Avaluació/Prova_practica_T2.md).

**Resum de correcció Part A:** nucli = FSM RUN/STOP amb ordres per ràdio (`CMD:`), reutilitzant les funcions de moviment de la SA4-SA5; ampliacions = polsador STOP prioritari (P12) i LED indicador (P1); **ítem obligatori (2 punts, P3.9):** funció nova pròpia amb paràmetre i retorn (`percentatge_a_velocitat()`) que converteix una magnitud i s'usa realment al programa.

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

**Resum de correcció Part B:** nucli = control tot/res amb histèresi (dos llindars) sobre `temperature()`; ampliació = registre amb el mòdul natiu `log`.

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

---

## T3 (SA7-SA8) — "Rover autònom + telemetria"

Enunciat complet, graella i solució raonada: [`Avaluació/Prova_practica_T3.md`](../../Avaluació/Prova_practica_T3.md).

**Resum de correcció Part A (pista):** nucli = recorregut fix calibrat; ampliacions = evita-obstacles (HC-SR04, P1/P2) i seguidor de línia (P0).

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
    try:
        durada_us = machine.time_pulse_us(ECHO, 1, 30000)
    except OSError:
        return None   # timeout llancat com a excepcio: cap eco rebut
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

**Resum de correcció Part B (taula):** nucli = telemetria per ràdio amb prefix `TEL:`; ampliació = integració d'una ordre `CMD:` en el comportament (repàs d'integració de la SA5-SA6, no contingut nou de SA7-SA8); **ítem obligatori (2 punts, P3.9):** comportament nou del rover no treballat a classe, escrit en una funció pròpia (`cal_aparcar()`), redactat a la taula sense necessitat de temps addicional de pista.

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

### Ítem obligatori T3 — comportament nou del rover (funció pròpia)

<details markdown="1">
<summary>Desplega el codi complet (<code>prova_t3_comportament_nou.py</code>)</summary>

```python
# Prova practica T3 - ITEM NOU (obligatori, 2 punts) - SOLUCIO ORIENTATIVA
# (docent, NO es lliura). Comportament NOU del rover, NO treballat a cap
# sessio del curs: "aparca quan detecta la linia DUES vegades seguides".
# Es redacta a la TAULA (mateix bloc horari que la Part B): no necessita
# temps addicional de pista de la rotacio continua. Es valora la logica i
# l'estructura de la funcio (parametre + retorn); si toca torn de pista
# abans d'acabar la sessio es pot provar amb el rover real, pero no cal
# per obtenir la puntuacio.
# Cablatge (00_Fil_conductor_construccions.md #1b, rover T3, igual que
# prova_t3_rover.py): M1=P13/P14, M2=P15/P16, seguidor de linia=P0.
# Simulador: aquest comportament necessita el rover real (motors i sensor
# de linia no es simulen); la funcio cal_aparcar() si es pot provar sola
# al REPL amb valors enters (0, 1, 2...).

from microbit import *

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16
SEGUIDOR_LINIA = pin0

VELOCITAT_AVANCAR = 400
LLINDAR_LINIA = 500


def avancar(velocitat):
    M1_ENDAVANT.write_analog(velocitat)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_analog(velocitat)
    M2_ENRERE.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def cal_aparcar(deteccions_consecutives):
    # FUNCIO NOVA (item obligatori): UN PARAMETRE i VALOR DE RETORN.
    # Comportament no vist a classe: cal aparcar quan la linia s'ha
    # detectat DUES vegades SEGUIDES (no nomes un cop, per evitar un fals
    # positiu d'un sol instant de lectura sorollosa).
    return deteccions_consecutives >= 2


deteccions = 0
aparcat = False

while not aparcat:
    lectura = SEGUIDOR_LINIA.read_analog()
    detecta_linia = lectura < LLINDAR_LINIA

    if detecta_linia:
        deteccions += 1
    else:
        deteccions = 0   # nomes compten deteccions SEGUIDES, sense talls

    if cal_aparcar(deteccions):
        aturar()
        display.show(Image.YES)
        aparcat = True
    else:
        avancar(VELOCITAT_AVANCAR)
        display.show(Image.ARROW_N)

    sleep(50)
```

</details>
