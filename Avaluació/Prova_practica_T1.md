# Prova pràctica — Trimestre 1 (SA1-SA3)
## "Estació personal d'alertes"

**Durada:** una sessió sencera — **la S4 de la SA3** (~95-100' efectius de prova, més instruccions i recollida) · **Individual** · **Material:** micro:bit V2 + Micro:shield, sensor de llum extern del Kit 2 (a P3), ordinador amb accés al REPL, quadern tècnic propi. Es permet consultar esquemes i el quadern tècnic (no s'avalua la memòria, sinó saber fer i trobar).

> ℹ️ Aquesta prova **no reutilitza la mascota** (el producte de la SA3, ja tancat i avaluat a la Sessió 3): és un programa nou, individual, sobre la micro:bit sola.

### Competències i criteris avaluats
- **CE-R1** (programar) → CA1.1 · **CE-R2** (sensors/circuits) → CA2.1, CA2.2
- Rúbriques: **R1** (codi), **R2** (circuit/mesura), **R4** (documentació).

---

## Enunciat (per nivells)

Programa una micro:bit que actuï d'**estació personal d'alertes**: ha de vigilar la llum i la temperatura de l'aula i avisar quan calgui, tal com hem practicat a `nivell_llum.py` i `termometre.py`.

### Nivell 1 — Nucli obligatori (assoliment satisfactori)
1. Amb els botons **A**/**B** (`is_pressed()`, com a la SA1-SA3), alterna entre dos modes: **mode llum** i **mode temperatura** (mostra una icona diferent per a cada mode).
2. En **mode llum**, llegeix el sensor de llum **intern** (`display.read_light_level()`) i mostra una icona quan sigui de nit/fosc (per sota d'un llindar **calibrat amb el REPL**, no inventat) i una altra quan hi hagi prou llum.
3. En **mode temperatura**, llegeix `temperature()` i mostra, amb un `if/elif/else`, tres icones diferents segons si fa fred, temperatura agradable o calor.
4. **Mentre el programa corre, imprimeix (`print`) la lectura pel REPL** perquè es pugui depurar en directe.

### Nivell 2 — Ampliació (notable)
5. Munta el **sensor de llum extern del Kit 2** (P3, ADC) i compara'l amb l'intern: mostra els dos valors pel REPL (fes servir `mapa()` per posar-los a la mateixa escala 0-255).

### Nivell 3 — Ampliació (excel·lent)
6. Afegeix una segona via d'alerta amb l'**acceleròmetre** (una sacsejada confirma/silencia l'alerta actual) i una tercera amb el **micròfon intern** (un soroll fort per sobre d'un llindar propi dispara un avís sonor amb `music.pitch`). Estructura tot el programa amb **funcions** (una responsabilitat per funció).

### Lliurament
Programa funcionant + **explicació breu al quadern** (què fa cada mode, quins llindars has triat i com els has calibrat amb el REPL, un error que has resolt).

### Pla de millora personal (després de la prova — 3 línies, no puntua)
> Quan rebis el retorn, escriu al quadern: **(1)** què m'ha fallat o m'ha costat més · **(2)** què practicaré concretament (quina secció de `SA0`, quin programa refaré) · **(3)** com comprovaré que ja ho tinc.
> El docent **recupera aquestes 3 línies a l'inici de la SA4**: la primera graella d'activació del trimestre es dedica a comprovar el punt (3) de cadascú. El retorn només serveix si algú hi torna.

---

## Graella de correcció (10 punts)

| Criteri | Punts | CA | Rúbrica |
|---|---|---|---|
| Botons A/B canvien de mode correctament amb `is_pressed()` (icona pròpia per mode) | 1,5 | CA1.1 | R1 |
| Mode llum: condicional correcte amb el sensor intern i llindar calibrat | 1,5 | CA1.1, CA2.2 | R1 |
| Mode temperatura: `if/elif/else` correcte amb les tres icones | 1,5 | CA1.1, CA2.2 | R1 |
| Lectura contínua pel REPL (`print`) | 1 | CA1.1 | R1 |
| Sensor extern (P3) muntat i comparat amb l'intern (ampliació) | 2 | CA2.1, CA2.2 | R1, R2 |
| Acceleròmetre + micròfon integrats, codi amb funcions (ampliació) | 1,5 | CA1.1 | R1 |
| Documentació al quadern (llindars + calibratge + error resolt) | 1 | CA1.1 | R4 |

> Orientació: nucli ben fet ≈ 5-6; amb el sensor extern ≈ 7-8; amb totes dues ampliacions i bona documentació ≈ 9-10.

---

## Solució orientativa (docent)

**Muntatge:** micro:bit V2 + Micro:shield, sensor de llum extern del Kit 2 a **P3** (ADC). Cap altre component: la resta de sensors són interns (llum, temperatura, acceleròmetre, micròfon).

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
# l'assignacio es IDEMPOTENT (mentre el boto es manté premut, cada volta
# torna a fixar el MATEIX mode: no hi ha cap comptador ni commutacio que
# es pugui "disparar" de mes).
# Ampliacio (notable): sensor de llum EXTERN del Kit 2 (P3, ADC) comparat
# amb l'intern (entrada analogica basica, mapa() de la SA3).
# Ampliacio (excel-lent): accelerometre (sacsejada) per confirmar l'alerta
# i microfon intern per detectar un soroll fort com a via addicional
# d'alerta; codi organitzat amb funcions (una responsabilitat per funcio).
# Maquinari: micro:bit V2 + Micro:shield; sensor de llum extern Kit 2 a P3
# (vegeu SA3_esquemes_connexions.md #2). Cap altre cablatge necessari: la
# resta son sensors interns.

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
    extern = pin3.read_analog()                      # 0-1023, sensor Kit 2
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
    # mentre el boto es manté premut, es torna a fixar el mateix mode.
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

**Què mirar en corregir el nucli:** (1) els botons canvien de mode amb `is_pressed()` (SA1-SA3 encara no ensenyen `was_pressed()`, exclusiu de la SA4: exigir-lo al nucli seria avaluar contingut no impartit; l'assignació és idempotent, així que no cal antirebot); (2) el llindar de foscor s'ha **calibrat al REPL**, no copiat a ull; (3) les tres branques de temperatura són excloents i cobreixen tot el rang. Error típic: comparar `read_light_level()` (0-255) directament amb una lectura de `read_analog()` (0-1023) sense `mapa()` — confusió d'escales ja treballada a la SA3.

> Avaluació global del trimestre: combinar el resultat d'aquesta prova amb el producte «mascota reactiva» (S3 de SA3, dimensió «Projectes i productes») — cap evidència no compta dues vegades.
