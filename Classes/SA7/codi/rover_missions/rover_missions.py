# SA7 - rover_missions.py  (PRODUCTE de la SA, integracio, Sessio 4)
# Programa INTEGRADOR: combina la cinematica diferencial (calibratge_motors),
# el seguidor de linia (segueix_linia) i l'evita-obstacles (evita_obstacles)
# en MISSIONS seleccionables amb els botons, sobre una pista de proves.
# Tambe integra un polsador STOP (P12, pull-up), amb el mateix patro
# prioritari de vehicle_seguretat.py (SA6): es comprova SEMPRE el primer,
# abans de qualsevol altra cosa del bucle.
# Cablatge (definitiu, veure 00_Fil_conductor_construccions.md #1b i
# SA7_esquemes_connexions.md): M1=P13/P14, M2=P15/P16, HC-SR04 trigger=P1,
# echo=P2, seguidor de linia=P0, polsador STOP=P12 (pull-up intern).
# Simulador: python.microbit.org NO simula motors, HC-SR04 ni seguidor de
# linia; aquest programa es prova NOMES amb el rover real sobre la pista.

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

POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)   # sense aixo la lectura flota

VELOCITAT_SO_CM_US = 0.0343
LLINDAR_OBSTACLE_CM = 15
LLINDAR_LINIA = 500

VELOCITAT_AVANCAR = 400
VELOCITAT_GIR = 300

# Missions disponibles: es trien amb el boto A (canvia de missio) i
# s'engeguen amb el boto B (comenca/atura).
MISSIO_QUADRAT, MISSIO_PARET, MISSIO_LINIA = range(3)
NOMS_MISSIO = {MISSIO_QUADRAT: "QUADRAT", MISSIO_PARET: "PARET", MISSIO_LINIA: "LINIA"}

missio_actual = MISSIO_QUADRAT
en_marxa = False


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
    # Mateixa lectura robusta que evita_obstacles.py (SA7-S3): time_pulse_us
    # pot senyalar timeout amb un valor negatiu O amb una excepcio OSError
    # (depen de placa/versio); el try/except cobreix el segon cas.
    TRIGGER.write_digital(0)
    utime.sleep_us(2)
    TRIGGER.write_digital(1)
    utime.sleep_us(10)
    TRIGGER.write_digital(0)
    try:
        durada_us = machine.time_pulse_us(ECHO, 1, 30000)
    except OSError:
        return None
    if durada_us < 0:
        return None
    return (durada_us * VELOCITAT_SO_CM_US) / 2


def polsador_premut():
    # Prioritat maxima, patro identic al de vehicle_seguretat.py (SA6): amb
    # pull-up intern, repos = 1, premut = 0 (LOW).
    return not POLSADOR_STOP.read_digital()


def missio_quadrat():
    # Modelitza una trajectoria senzilla: quatre costats i quatre girs de
    # 90 graus, amb girs i avancos TEMPORITZATS (objectiu 4 de la fitxa 16).
    for _ in range(4):
        if polsador_premut():
            return
        avancar(VELOCITAT_AVANCAR)
        sleep(900)
        if polsador_premut():
            return
        girar('dreta')
        sleep(430)   # temps calibrat perque el gir sigui proper a 90 graus
    aturar()


def missio_paret():
    # Anar fins a la paret (HC-SR04) i tornar: combina evita-obstacles amb
    # un gir de mitja volta.
    while not polsador_premut():
        d = mesura_distancia()
        if d is not None and d < LLINDAR_OBSTACLE_CM:
            aturar()
            break
        avancar(VELOCITAT_AVANCAR)
        sleep(50)
    if polsador_premut():
        return
    girar('dreta')
    sleep(860)   # mitja volta (2 x el gir de 90 graus de missio_quadrat)
    aturar()


def missio_linia():
    # Segueix la linia fins que l'HC-SR04 detecti un obstacle al davant:
    # combina els dos sensors nous del rover en una sola missio.
    while not polsador_premut():
        d = mesura_distancia()
        if d is not None and d < LLINDAR_OBSTACLE_CM:
            aturar()
            break
        lectura = SEGUIDOR_LINIA.read_analog()
        if lectura < LLINDAR_LINIA:
            avancar(VELOCITAT_AVANCAR)
        else:
            girar('esquerra')
        sleep(20)
    aturar()


MISSIONS = {
    MISSIO_QUADRAT: missio_quadrat,
    MISSIO_PARET: missio_paret,
    MISSIO_LINIA: missio_linia,
}


display.show(NOMS_MISSIO[missio_actual][0])

while True:
    # 1a comprovacio de cada volta: el polsador d'emergencia, SEMPRE abans
    # de qualsevol altra cosa (mateix criteri que vehicle_seguretat.py, SA6).
    if polsador_premut():
        aturar()
        en_marxa = False
        display.show(Image.NO)

    if button_a.was_pressed() and not en_marxa:
        missio_actual = (missio_actual + 1) % 3
        display.show(NOMS_MISSIO[missio_actual][0])

    if button_b.was_pressed() and not en_marxa:
        en_marxa = True
        MISSIONS[missio_actual]()
        en_marxa = False
        display.show(NOMS_MISSIO[missio_actual][0])

    sleep(20)
