# SA8 - Repte 2 (SOLUCIO): estacio base multisensor amb registre avancat
# Nucli (rebre, analitzar, registrar amb log) + ampliacions 1-3: navegacio
# de camps amb botons A/B, marca de "nou record" al log, i deteccio de
# "sense senyal" quan fa massa temps que no arriba cap missatge.
# Maquinari: identic a estacio_base.py (nomes radio interna + display).

from microbit import *
import radio
import log

GRUP = 1
radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "TEL:"

log.set_labels('dist', 'seguidor', 'estat', 'temp', 'humitat', 'orientacio', 'record')

MAX_HISTORIC = 10
historic_distancies = []

# Requisit minim: seguiment de maxim/minim de temperatura.
temp_maxima = None
temp_minima = None

# Ampliacio 1: navegacio entre vistes amb els botons.
VISTES = ["ULTIMA", "MITJANA", "MAXMIN"]
vista_actual = 0

# Ampliacio 3: deteccio de "sense senyal".
LLINDAR_SENSE_SENYAL_MS = 5000
ultim_missatge_rebut = running_time()
ultima_temp = None


def analitza(missatge):
    dades = {}
    cos = missatge[len(PREFIX):]
    for camp in cos.split(";"):
        if ":" not in camp:
            continue
        clau, valor = camp.split(":", 1)
        dades[clau] = valor
    return dades


def mitjana(llista):
    return sum(llista) / len(llista) if llista else 0


def mostra_vista():
    nom = VISTES[vista_actual]
    if nom == "ULTIMA" and ultima_temp is not None:
        display.scroll(str(ultima_temp), delay=80, wait=False)
    elif nom == "MITJANA":
        display.scroll(str(int(mitjana(historic_distancies))), delay=80, wait=False)
    elif nom == "MAXMIN" and temp_maxima is not None:
        display.scroll(str(temp_maxima) + "/" + str(temp_minima), delay=80, wait=False)


while True:
    if button_a.was_pressed():
        # Ampliacio 1: canvia de vista sense esperar cap missatge nou.
        vista_actual = (vista_actual + 1) % len(VISTES)
        mostra_vista()

    if button_b.was_pressed():
        mostra_vista()

    # Ampliacio 3: si fa massa temps que no arriba res, avisa'n.
    ara = running_time()
    if ara - ultim_missatge_rebut > LLINDAR_SENSE_SENYAL_MS:
        display.show(Image.CONFUSED)

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ultim_missatge_rebut = running_time()
        dades = analitza(missatge)

        try:
            distancia = int(dades.get("D", -1))
        except ValueError:
            distancia = -1
        historic_distancies.append(distancia)
        if len(historic_distancies) > MAX_HISTORIC:
            historic_distancies.pop(0)

        try:
            temp = int(dades.get("T", -1))
        except ValueError:
            temp = -1
        ultima_temp = temp

        es_record = False
        if temp != -1:
            if temp_maxima is None or temp > temp_maxima:
                temp_maxima = temp
                es_record = True
            if temp_minima is None or temp < temp_minima:
                temp_minima = temp
                es_record = True

        log.add(dist=dades.get("D", ""), seguidor=dades.get("S", ""),
                 estat=dades.get("E", ""), temp=dades.get("T", ""),
                 humitat=dades.get("H", ""), orientacio=dades.get("O", ""),
                 record="1" if es_record else "0")

        print(missatge, "| mitjana D:", mitjana(historic_distancies),
              "| max/min T:", temp_maxima, temp_minima)
        mostra_vista()

    sleep(50)
