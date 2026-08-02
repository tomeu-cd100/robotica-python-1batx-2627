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
