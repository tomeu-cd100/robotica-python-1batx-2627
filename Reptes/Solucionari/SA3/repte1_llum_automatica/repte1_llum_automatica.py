# SA3 - Repte 1 (SOLUCIO): llum automatica d'estudi
# Nucli + ampliacions 1-3: segon llindar "molt fosc" amb parpelleig,
# intensitat proporcional (PWM) i temporitzador d'apagada.
# Maquinari: sensor de llum extern al pin P3 (Kit 2), LED extern al pin P1.

from microbit import *

LLINDAR_FOSCOR = 400      # calibrat al REPL
LLINDAR_MOLT_FOSC = 150   # ampliacio 1: per sota, "molt fosc"
TEMPS_MINIM_ENCES = 3000  # ms, ampliacio 3: no s'apaga de cop si torna la llum


def mapa(valor, entrada_min, entrada_max, sortida_min, sortida_max):
    rang_entrada = entrada_max - entrada_min
    rang_sortida = sortida_max - sortida_min
    proporcio = (valor - entrada_min) / rang_entrada
    return int(sortida_min + proporcio * rang_sortida)


t_ultima_encesa = 0


while True:
    llum = pin3.read_analog()

    if llum < LLINDAR_MOLT_FOSC:
        # Ampliacio 1: "molt fosc" -> parpelleig en lloc de fix.
        t_ultima_encesa = running_time()
        pin1.write_digital(1)
        sleep(150)
        pin1.write_digital(0)
        sleep(150)
    elif llum < LLINDAR_FOSCOR:
        # Ampliacio 2: intensitat proporcional a la foscor (PWM).
        t_ultima_encesa = running_time()
        intensitat = mapa(llum, 0, LLINDAR_FOSCOR, 1023, 200)
        pin1.write_analog(intensitat)
        sleep(100)
    else:
        # Ampliacio 3: es manté encès un temps minim encara que torni la llum.
        if running_time() - t_ultima_encesa > TEMPS_MINIM_ENCES:
            pin1.write_digital(0)
        sleep(100)
