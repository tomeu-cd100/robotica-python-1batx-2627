# SA2 · Solucionari dels reptes — Sortides: el robot actua

> **Material del docent.** Solucions completes dels tres reptes de [`Reptes_SA2.md`](../../Reptes_SA2.md), amb el nucli i les tres ampliacions graduades ja incorporades. **No es reparteix a l'alumnat abans que hagi entregat el seu propi repte**: com l'exemple resolt de la SA, serveix per corregir i, si cal, per mostrar *després* del primer intent.

> Cada solució és una còpia exacta del fitxer `.py` de la seva carpeta (`repte1_llum_seguretat/`, `repte2_ambientador/`, `repte3_semafor_emergencia/`): si canvies un fitxer, actualitza també el bloc de codi d'aquí sota.

---

## ⭐ Repte 1 · Llum de seguretat per a motxilla

**Idea de la solució:** dos "modes" de parpelleig (`mode_normal()`/`mode_alerta()`) que només canvien el `sleep()`; un tercer estat fix (`mode_aparcada()`, ampliació 2) commutat amb el botó B; el comptador (ampliació 1) es mostra cada 5 en lloc de cada 10.

```python
# SA2 - Repte 1 (SOLUCIO): llum de seguretat per a motxilla
# Nucli + ampliacions 1-3: comptador cada 5, mode "aparcada", funcions per mode.
# Maquinari: LED extern al pin P1 del Micro:shield (Kit 1).

from microbit import *

comptador = 0          # acumulador: quants parpellejos portem
MODE_APARCADA = False  # ampliacio 2: estat "fix" fins que es torna a premer un boto


def mode_normal():
    pin1.write_digital(1)
    sleep(500)
    pin1.write_digital(0)
    sleep(500)


def mode_alerta():
    # Ampliacio 3: parpelleig mes rapid que el normal.
    pin1.write_digital(1)
    sleep(120)
    pin1.write_digital(0)
    sleep(120)


def mode_aparcada():
    # Ampliacio 2: LED fix, sense parpellejar.
    pin1.write_digital(1)


while True:
    if button_b.is_pressed():
        MODE_APARCADA = not MODE_APARCADA   # commuta el mode amb cada pulsacio
        sleep(300)                          # petita espera per no rebotar

    if MODE_APARCADA:
        mode_aparcada()
    else:
        if button_a.is_pressed():
            mode_alerta()
        else:
            mode_normal()
        comptador = comptador + 1

        # Ampliacio 1: mostra el comptador cada 5 parpellejos (no cada 10).
        if comptador % 5 == 0:
            display.scroll(str(comptador))
```

**Punts a corregir:** el "mode alerta" ha de parpellejar **visiblement** més ràpid (compara els `sleep()` dels dos modes); el mode "aparcada" es queda **fix**, sense cap `sleep()` intern que el faci parpellejar; el `%` de l'ampliació 1 és `5`, no `10`.

---

## ⭐⭐ Repte 2 · Ambientador de llum i so per a una habitació

**Idea de la solució:** una `transicio()` que interpola de 0 fins al color final (requisit mínim), amb el vermell/verd/blau com a **variables simples** (no una tupla); `respira()` reutilitza la mateixa idea de PWM incremental de `pwm_led_rgb.py` per pujar/baixar la intensitat (ampliació 2); quatre crides seguides a `toca_nota()` (una per nota, amb la freqüència i el color escrits a mà) sincronitzen color i so nota a nota (ampliació 3), en lloc de cridar `music.play()` d'un cop.

```python
# SA2 - Repte 2 (SOLUCIO): ambientador de llum i so per a una habitacio
# Nucli + ampliacions 1-3: dos colors amb boto A, respiracio d'intensitat,
# color sincronitzat amb la melodia.
# Maquinari: LED RGB als pins P8 (vermell), P12 (verd), P16 (blau) i
# brunzidor al pin P2 del Micro:shield (Kit 1).
# Nivell SA2: nomes variables simples (cap color en tupla ni diccionari),
# funcions amb parametres separats i if/elif.

from microbit import *
import music

# Colors en tres variables simples (vermell, verd, blau) per a cada mode.
RELAX_R = 0
RELAX_G = 200
RELAX_B = 600     # blau suau

FESTA_R = 700
FESTA_G = 0
FESTA_B = 700     # magenta viu


def mostra_color(vermell, verd, blau):
    pin8.write_analog(vermell)
    pin12.write_analog(verd)
    pin16.write_analog(blau)


def transicio(r_final, g_final, b_final, passos, espera):
    # Transicio suau des d'apagat fins al color final (nucli).
    for i in range(passos + 1):
        vermell = r_final * i // passos
        verd = g_final * i // passos
        blau = b_final * i // passos
        mostra_color(vermell, verd, blau)
        sleep(espera)


def respira(r, g, b, cicles=1):
    # Ampliacio 2: la intensitat del color "respira" (puja i baixa).
    for c in range(cicles):
        for i in range(0, 21):
            mostra_color(r * i // 20, g * i // 20, b * i // 20)
            sleep(20)
        for i in range(20, -1, -1):
            mostra_color(r * i // 20, g * i // 20, b * i // 20)
            sleep(20)


def toca_nota(freq, durada, r, g, b):
    # Una nota + el seu color associat (greu=blau, agut=vermell).
    mostra_color(r, g, b)
    music.pitch(0, 0)  # evita solapament residual d'una nota anterior
    music.pitch(freq, durada, pin=pin2)


def melodia_sincronitzada():
    # Ampliacio 3: canvia de color a cada nota, en lloc de fer sonar
    # la melodia sencera d'un cop amb music.play(). Quatre crides seguides
    # (una per nota) en lloc de recorrer una llista/diccionari.
    toca_nota(262, 200, 0, 0, 1023)      # C4 - blau
    toca_nota(330, 200, 0, 600, 400)     # E4
    toca_nota(392, 200, 400, 600, 0)     # G4
    toca_nota(523, 400, 1023, 0, 0)      # C5 - vermell


# --- Engegada: transicio suau + melodia de benvinguda (requisit minim) ---
transicio(RELAX_R, RELAX_G, RELAX_B, 20, 30)
melodia_sincronitzada()

mode_festa = False

while True:
    if button_a.is_pressed():
        mode_festa = not mode_festa   # Ampliacio 1: alterna entre dos colors ambient
        sleep(300)

    if mode_festa:
        respira(FESTA_R, FESTA_G, FESTA_B)
    else:
        respira(RELAX_R, RELAX_G, RELAX_B)
```

**Punts a corregir:** la transició d'engegada ha de veure's **progressiva**, no un salt directe al color final; els dos colors de l'ampliació 1 han de ser clarament diferents i alternar-se sense reiniciar el programa; a l'ampliació 3, el color ha de canviar **al ritme** de cada nota, no de manera aleatòria.

---

## ⭐⭐⭐ Repte 3 · Semàfor intel·ligent d'encreuament

**Idea de la solució:** `cicle_normal()` fracciona cada fase en passos d'1 `sleep(100)` i revisa el botó A a cada pas (`revisa_boto()`) perquè el mode d'emergència **interrompi a l'instant**, no al final de la fase; `emergencia` és la variable d'estat (ampliació 2) que decideix, des del `while True:`, si es crida `cicle_normal()` o `mode_emergencia()`.

```python
# SA2 - Repte 3 (SOLUCIO): semafor intel-ligent d'encreuament
# Nucli + ampliacions 1-3: avis sonor intermitent, funcions separades per
# mode, LED RGB sincronitzat amb l'emergencia.
# Maquinari: LED verd P1, ambre P8, vermell P12, brunzidor P2, rele P13
# (Kit 1 + Kit 3). LED RGB opcional als pins P8/P12/P16 (repte 2).

from microbit import *
import music

TEMPS_VERD = 3000
TEMPS_AMBRE = 1000
TEMPS_VERMELL = 3000

emergencia = False   # Ampliacio 2: variable d'estat que decideix quina funcio es crida


def tot_apagat():
    pin1.write_digital(0)
    pin8.write_digital(0)
    pin12.write_digital(0)


def revisa_boto():
    # Comprova el boto A sense bloquejar el cicle: si es prem, commuta
    # l'estat d'emergencia (nucli del requisit: interrupcio immediata).
    global emergencia
    if button_a.is_pressed():
        emergencia = not emergencia
        sleep(300)   # petita espera per no rebotar
    return emergencia


def cicle_normal():
    # --- Fase verda ---
    tot_apagat()
    pin1.write_digital(1)
    for i in range(TEMPS_VERD // 100):
        if revisa_boto():
            return
        sleep(100)

    # --- Fase ambre ---
    tot_apagat()
    pin8.write_digital(1)
    music.pitch(440, 200, pin=pin2)
    for i in range(TEMPS_AMBRE // 100):
        if revisa_boto():
            return
        sleep(100)

    # --- Fase vermella (amb rele) ---
    tot_apagat()
    pin12.write_digital(1)
    pin13.write_digital(1)
    for i in range(TEMPS_VERMELL // 100):
        if revisa_boto():
            pin13.write_digital(0)
            return
        sleep(100)
    pin13.write_digital(0)


def mode_emergencia():
    # Ampliacio 1: avis sonor intermitent + rele intermitent (llum d'emergencia).
    # Ampliacio 3: si hi ha LED RGB muntat, ambre parpellejant en lloc del LED digital.
    tot_apagat()
    pin12.write_digital(1)             # LED vermell parpellejant
    pin13.write_digital(1)             # rele actiu (llum d'emergencia encesa)
    music.pitch(880, 150, pin=pin2)    # avis sonor curt

    if revisa_boto():
        return
    sleep(250)

    pin12.write_digital(0)
    pin13.write_digital(0)

    if revisa_boto():
        return
    sleep(250)


while True:
    if emergencia:
        mode_emergencia()
    else:
        cicle_normal()
```

**Punts a corregir:** prémer el botó A ha d'interrompre el cicle **a l'instant** (no esperar que acabi la fase en curs): cal revisar el botó dins de cada fase, no només entre fases; en tornar al mode normal, el cicle ha de començar **de nou per la fase verda**, no continuar a mig cicle; el relé s'ha de tancar (`write_digital(0)`) sempre que se surti d'una fase, també si se surt per emergència.

---

## Rúbrica ràpida de correcció (R1, R2, R4)

| Nivell | Codi (R1) | Muntatge (R2) | Quadern (R4) |
|---|---|---|---|
| Nucli assolit (5-6) | El requisit mínim funciona i està comentat | Cablatge funcional, encara que millorable | Predicció + solució anotades |
| Notable (7-8) | Una ampliació ben integrada (no apegalada al final) | Cablatge net i endreçat | + un error documentat amb DEPURA |
| Excel·lent (9-10) | Totes les ampliacions, codi net i reutilitzable (funcions) | Muntatge òptim i etiquetat | + reflexió de millora pròpia |

*Solucionari de la SA2. Material del docent.*
