# SA2 - semafor_rele.py  (REPTE / PRODUCTE de la SA2)
# Semafor complet: LED verd, ambre i vermell amb temporitzacions, un avis
# sonor a l'ambre i un rele que commuta un llum extern quan esta en vermell
# (per exemple, l'enllumenat d'un pas de vianants).
#
# Maquinari (Micro:shield): LED verd P1, LED ambre P8, LED vermell P12,
# brunzidor P2, rele P13. Veure SA2_esquemes_connexions.md pel cablatge
# complet i les normes de seguretat del rele.

from microbit import *
import music

# Temps de cada fase, en ms: en variables perque nomes calgui canviar UN lloc.
TEMPS_VERD = 3000
TEMPS_AMBRE = 1000
TEMPS_VERMELL = 3000


def tot_apagat():
    pin1.write_digital(0)
    pin8.write_digital(0)
    pin12.write_digital(0)


while True:
    # --- Fase verda ---
    tot_apagat()
    pin1.write_digital(1)
    sleep(TEMPS_VERD)

    # --- Fase ambre: avisa amb un to curt ---
    tot_apagat()
    pin8.write_digital(1)
    music.pitch(440, 200, pin=pin2)
    sleep(TEMPS_AMBRE)

    # --- Fase vermella: encen el LED i commuta el rele (llum extern) ---
    tot_apagat()
    pin12.write_digital(1)
    pin13.write_digital(1)   # el rele tanca el circuit extern
    sleep(TEMPS_VERMELL)
    pin13.write_digital(0)   # el rele torna a obrir el circuit extern
