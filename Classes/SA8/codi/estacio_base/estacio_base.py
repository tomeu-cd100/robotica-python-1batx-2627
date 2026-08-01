# SA8 - estacio_base.py  (segona placa: PRODUCTE de la SA, Sessions 2-3)
# Programa que ESCRIU CADA ALUMNE (regla d'estacio base, fitxa 17): rep la
# telemetria de telemetria_radio.py, la mostra i la registra. S'executa
# TEMPORALMENT a la placa d'un company (per torns) o del docent: la placa
# nomes es el banc de proves, el codi i la interpretacio de les dades son
# sempre l'evidencia propia de qui l'ha escrit.
# Protocol: missatges amb prefix "TEL:" i camps "clau:valor" separats per
# ";" (mateixa idea de PREFIX que comandament.py/receptor_vehicle.py, SA5,
# nomes que aqui el prefix es DIFERENT perque no es una ordre).
# Registre: llista amb les ultimes lectures + mitjana simple (fitxa 17,
# objectiu 3) I registre persistent amb el modul "log" natiu de la V2
# (res de nuvol: es llegeix per USB, mateix mecanisme que registre_dades.py
# de la SA6).
# Maquinari: cap component nou, nomes la radio interna i el display.
# Simulador: la radio SI es simula (2 instancies obertes alhora); el modul
# log tambe es simula (es pot descarregar el CSV/HTML del simulador).

from microbit import *
import radio
import log

GRUP = 1   # ha de coincidir amb el GRUP de telemetria_radio.py de la parella

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "TEL:"

log.set_labels('dist', 'seguidor', 'estat', 'temp', 'humitat', 'orientacio')

MAX_HISTORIC = 10
historic_distancies = []   # llista de lectures (objectiu 3 de la fitxa 17)


def analitza(missatge):
    # Separa "TEL:D:23;S:412;E:SEGUIR;T:24;H:55;O:PLA" en un diccionari
    # {"D": "23", "S": "412", ...}: mateixa idea que el split(";") de
    # 02_telemetria_receptor.py, generalitzada a qualsevol nombre de camps.
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


def mostra_estat(dades):
    estat = dades.get("E", "")
    if estat == "ESQUIVAR":
        display.show(Image.NO)
    elif estat == "RECUPERAR":
        display.show(Image.TARGET)
    elif estat == "SEGUIR":
        display.show(Image.YES)
    else:
        display.show(Image.CONFUSED)   # missatge inesperat (protocol trencat)


while True:
    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        dades = analitza(missatge)

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

        print(missatge, "| mitjana distancia:", mitjana(historic_distancies))
        mostra_estat(dades)

    sleep(50)
