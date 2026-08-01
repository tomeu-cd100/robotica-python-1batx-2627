# SA5 - Repte 3 (SOLUCIO): historial de comandes amb estadistiques
# Nucli + ampliacions 1-3: comanda_mes_frequent(), total de comandes i
# temps mitja entre comandes per REPL, i aturada automatica de seguretat
# si fa mes de 3 segons que no arriba cap comanda.
# Maquinari: vehicle T2 (M1=pin13/pin14, M2=pin15/pin16), com a
# receptor_vehicle.py.

from microbit import *
import radio

GRUP = 1

radio.on()
radio.config(group=GRUP, power=6)

PREFIX = "CMD:"

M1_ENDAVANT = pin13
M1_ENRERE = pin14
M2_ENDAVANT = pin15
M2_ENRERE = pin16

VELOCITAT = 400
TEMPS_MAXIM_SENSE_ORDRE = 3000   # ampliacio 3: 3 segons, en ms

historic_comandes = []
MAX_HISTORIC = 20
ultim_instant_rebut = running_time()


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


def girar(costat):
    velocitat_gir = 300
    if costat == 'esquerra':
        M1_ENRERE.write_analog(velocitat_gir)
        M1_ENDAVANT.write_digital(0)
        M2_ENDAVANT.write_analog(velocitat_gir)
        M2_ENRERE.write_digital(0)
    elif costat == 'dreta':
        M1_ENDAVANT.write_analog(velocitat_gir)
        M1_ENRERE.write_digital(0)
        M2_ENRERE.write_analog(velocitat_gir)
        M2_ENDAVANT.write_digital(0)


def aturar():
    M1_ENDAVANT.write_digital(0)
    M1_ENRERE.write_digital(0)
    M2_ENDAVANT.write_digital(0)
    M2_ENRERE.write_digital(0)


def desa_al_historic(ordre):
    historic_comandes.append((ordre, running_time()))
    if len(historic_comandes) > MAX_HISTORIC:
        historic_comandes.pop(0)


def comanda_mes_frequent():
    # Requisit minim: recorre l'historial i compta quantes vegades apareix
    # cada ordre, sense fer servir diccionaris (encara no vistos al curs).
    ordres_vistes = []
    comptadors = []
    for ordre, instant in historic_comandes:
        if ordre in ordres_vistes:
            index = ordres_vistes.index(ordre)
            comptadors[index] = comptadors[index] + 1
        else:
            ordres_vistes.append(ordre)
            comptadors.append(1)
    if len(ordres_vistes) == 0:
        return None
    index_max = comptadors.index(max(comptadors))
    return ordres_vistes[index_max]


def temps_mitja_entre_comandes():
    # Ampliacio 2: diferencia mitjana entre instants de tuples consecutives.
    if len(historic_comandes) < 2:
        return 0
    suma_diferencies = 0
    for i in range(1, len(historic_comandes)):
        instant_anterior = historic_comandes[i - 1][1]
        instant_actual = historic_comandes[i][1]
        suma_diferencies = suma_diferencies + (instant_actual - instant_anterior)
    return suma_diferencies // (len(historic_comandes) - 1)


def actua(ordre):
    if ordre == "F":
        display.show(Image.ARROW_N)
        avancar(VELOCITAT)
    elif ordre == "B":
        display.show(Image.ARROW_S)
        retrocedir(VELOCITAT)
    elif ordre == "L":
        display.show(Image.ARROW_W)
        girar('esquerra')
    elif ordre == "R":
        display.show(Image.ARROW_E)
        girar('dreta')
    elif ordre == "S":
        display.show(Image.NO)
        aturar()


aturar()
display.show(Image.NO)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        # Ampliacio 1: mostra per REPL el total i la comanda mes frequent.
        print("Total de comandes:", len(historic_comandes))
        print("Comanda mes frequent:", comanda_mes_frequent())
        print("Temps mitja entre comandes (ms):", temps_mitja_entre_comandes())

    missatge = radio.receive()
    if missatge is not None and missatge.startswith(PREFIX):
        ordre = missatge[len(PREFIX):]
        desa_al_historic(ordre)
        ultim_instant_rebut = running_time()
        actua(ordre)

    if running_time() - ultim_instant_rebut > TEMPS_MAXIM_SENSE_ORDRE:
        # Ampliacio 3: aturada automatica de seguretat per inactivitat.
        aturar()
        display.show(Image.SAD)

    sleep(20)
