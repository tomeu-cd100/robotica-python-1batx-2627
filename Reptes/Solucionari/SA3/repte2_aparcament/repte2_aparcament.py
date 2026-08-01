# SA3 - Repte 2 (SOLUCIO): aparcament amb sensor de distancia
# Nucli + ampliacions 1-3: distancia al display, ritme progressiu i
# una funcio per zona.
# Maquinari: HC-SR04 (Kit 2), trigger P14, echo P15; brunzidor P2 (Kit 1).

from microbit import *
import machine
import utime
import music

ZONA_ATENCIO_CM = 30
ZONA_PERILL_CM = 15
VELOCITAT_SO_CM_US = 0.0343


def distancia_cm():
    pin14.write_digital(0)
    utime.sleep_us(2)
    pin14.write_digital(1)
    utime.sleep_us(10)
    pin14.write_digital(0)
    durada_us = machine.time_pulse_us(pin15, 1, 30000)
    if durada_us < 0:
        return None
    return (durada_us * VELOCITAT_SO_CM_US) / 2


def zona_lluny(d):
    display.show(str(min(int(d) // 10, 9)))


def zona_atencio(d):
    display.show(str(min(int(d) // 10, 9)))
    music.pitch(660, 80, pin=pin2)
    sleep(300)   # ampliacio 2: ritme mig


def zona_perill(d):
    display.show(str(min(int(d) // 10, 9)))
    music.pitch(880, 80, pin=pin2)
    sleep(100)   # ampliacio 2: ritme rapid, molt a prop


while True:
    d = distancia_cm()
    if d is None:
        display.show("?")
        sleep(200)
        continue

    if d < ZONA_PERILL_CM:
        zona_perill(d)
    elif d < ZONA_ATENCIO_CM:
        zona_atencio(d)
    else:
        zona_lluny(d)
        sleep(200)
