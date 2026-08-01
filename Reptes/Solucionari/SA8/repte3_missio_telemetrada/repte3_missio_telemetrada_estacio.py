# SA8 - Repte 3 (SOLUCIO): missio telemetrada amb alerta d'emergencia per
# gest (ESTACIO BASE, receptor). Nucli (rebre, mostrar, registrar) +
# ampliacio 2 (comptador d'alertes per REPL) + ampliacio 3 (boto A envia
# "CMD:S" per aturar el rover a distancia, protocol bidireccional).
# Maquinari: identic a estacio_base.py (nomes radio interna + display).

from microbit import *
import radio
import log

GRUP = 1
radio.on()
radio.config(group=GRUP, power=6)

PREFIX_TEL = "TEL:"
PREFIX_CMD = "CMD:"

log.set_labels('dist', 'seguidor', 'estat', 'temp', 'humitat', 'orientacio')

MAX_HISTORIC = 10
historic_distancies = []
comptador_alertes = 0   # ampliacio 2


def analitza(missatge, prefix):
    dades = {}
    cos = missatge[len(prefix):]
    for camp in cos.split(";"):
        if ":" not in camp:
            continue
        clau, valor = camp.split(":", 1)
        dades[clau] = valor
    return dades


def mitjana(llista):
    return sum(llista) / len(llista) if llista else 0


while True:
    if button_a.was_pressed():
        # Ampliacio 3: protocol bidireccional, atura el rover a distancia.
        radio.send(PREFIX_CMD + "S")
        display.show(Image.NO)
        sleep(150)

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX_TEL):
        cos = missatge[len(PREFIX_TEL):]

        if cos == "ALERTA_STOP":
            comptador_alertes += 1
            print("ALERTA D'EMERGENCIA rebuda. Total:", comptador_alertes)
            display.show(Image.SKULL)
            sleep(300)
            continue

        dades = analitza(missatge, PREFIX_TEL)
        try:
            distancia = int(dades.get("D", -1))
        except ValueError:
            distancia = -1
        historic_distancies.append(distancia)
        if len(historic_distancies) > MAX_HISTORIC:
            historic_distancies.pop(0)

        log.add(dist=dades.get("D", ""), seguidor=dades.get("S", ""),
                 estat=dades.get("E", ""), temp=dades.get("T", ""),
                 humitat=dades.get("H", ""), orientacio=dades.get("O", ""))

        print(missatge, "| mitjana D:", mitjana(historic_distancies))
        display.show(Image.YES)

    sleep(50)
