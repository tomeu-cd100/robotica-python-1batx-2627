# SA3 - alarma_ultrasons.py
# Sensor d'ultrasons HC-SR04 (Kit 2): mesura la distancia amb el temps de
# vol de l'eco (time-of-flight) i fa sonar una alarma si t'hi acostes massa.
# Maquinari: HC-SR04 (5 V), trigger P14, echo P15 (Kit 2); brunzidor P2 (Kit 1).
# Veure SA3_esquemes_connexions.md: alimentacio a 5 V i divisor de tensio a
# l'echo si el modul concret ho necessita.

from microbit import *
import machine
import utime
import music

DISTANCIA_ALARMA_CM = 15   # per sota d'aquesta distancia, sona l'alarma
VELOCITAT_SO_CM_US = 0.0343  # cm per microsegon (a temperatura ambient)


def distancia_cm():
    # Trigger: pols de 10 us per iniciar la mesura (utime.sleep_us, no sleep()
    # normal: sleep() nomes treballa en ms i no baixa de l'ordre del segon us).
    pin14.write_digital(0)
    utime.sleep_us(2)
    pin14.write_digital(1)
    utime.sleep_us(10)
    pin14.write_digital(0)

    # Echo: machine.time_pulse_us mesura quant triga el pin en estar a 1.
    durada_us = machine.time_pulse_us(pin15, 1, 30000)   # 30 ms de marge (~5 m)
    if durada_us < 0:
        return None   # cap eco rebut (fora de rang)
    # Anada i tornada: la distancia real es la meitat del recorregut total.
    return (durada_us * VELOCITAT_SO_CM_US) / 2


while True:
    d = distancia_cm()
    if d is not None:
        display.show(str(min(int(d) // 10, 9)))   # xifra de desenes de cm
        if d < DISTANCIA_ALARMA_CM:
            music.pitch(880, 100, pin=pin2)        # avis sonor agut i curt
    else:
        display.show("?")   # fora de rang: cap objecte detectat
    sleep(150)
