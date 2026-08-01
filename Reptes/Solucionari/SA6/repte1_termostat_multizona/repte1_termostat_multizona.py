# SA6 - Repte 1 (SOLUCIO): termostat de dues zones
# Nucli + ampliacions 1-3: display amb la zona activa, comptador de canvis
# d'estat per zona, i una alerta d'emergencia per sobreescalfament que
# desactiva els dos actuadors per davant de qualsevol altra logica.
# Maquinari: temperature() interna (simula les dues zones amb el mateix
# sensor, en un cas real serien dos sensors); actuador zona 1 = pin2 (rele),
# actuador zona 2 = pin1 (LED, substitut segur).

from microbit import *

ACTUADOR_1 = pin2
ACTUADOR_2 = pin1

LLINDAR_BAIX_1 = 24
LLINDAR_ALT_1 = 26
LLINDAR_BAIX_2 = 20
LLINDAR_ALT_2 = 22

LLINDAR_EMERGENCIA = 32   # ampliacio 3: sobreescalfament

actiu_1 = False
actiu_2 = False
alerta = False

canvis_1 = 0   # ampliacio 2: comptador de canvis d'estat per zona
canvis_2 = 0


def actualitza_zona(temp):
    global actiu_1, actiu_2, canvis_1, canvis_2

    if not actiu_1 and temp < LLINDAR_BAIX_1:
        actiu_1 = True
        canvis_1 += 1
    elif actiu_1 and temp > LLINDAR_ALT_1:
        actiu_1 = False
        canvis_1 += 1

    if not actiu_2 and temp < LLINDAR_BAIX_2:
        actiu_2 = True
        canvis_2 += 1
    elif actiu_2 and temp > LLINDAR_ALT_2:
        actiu_2 = False
        canvis_2 += 1


while True:
    temp = temperature()

    if temp > LLINDAR_EMERGENCIA:
        # Ampliacio 3: alerta d'emergencia, per davant de qualsevol zona.
        alerta = True
        actiu_1 = False
        actiu_2 = False
    elif alerta and temp < LLINDAR_ALT_1:
        alerta = False   # torna a control normal quan ja no fa tanta calor

    if alerta:
        ACTUADOR_1.write_digital(0)
        ACTUADOR_2.write_digital(0)
        display.show(Image.SKULL)
    else:
        actualitza_zona(temp)
        ACTUADOR_1.write_digital(1 if actiu_1 else 0)
        ACTUADOR_2.write_digital(1 if actiu_2 else 0)
        # Ampliacio 1: lletra segons quina zona esta activa.
        if actiu_1 and actiu_2:
            display.show("B")
        elif actiu_1:
            display.show("1")
        elif actiu_2:
            display.show("2")
        else:
            display.clear()

    if button_a.was_pressed() and button_b.was_pressed():
        print("Canvis zona 1:", canvis_1, "  Canvis zona 2:", canvis_2)

    sleep(500)
