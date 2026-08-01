# SA2 - musica_altaveu.py
# So amb el modul music: una melodia curta i un to que canvia segons el
# boto premut. Maquinari: brunzidor extern al pin P2 del Micro:shield
# (o l'altaveu integrat de la V2 si no hi ha brunzidor connectat).

from microbit import *
import music

MELODIA = ['C4:4', 'E4:4', 'G4:4', 'C5:8']   # nota:duracio

while True:
    if button_a.is_pressed():
        music.pitch(262, 300, pin=pin2)   # to greu (nota Do, 262 Hz) 300 ms
    elif button_b.is_pressed():
        music.pitch(523, 300, pin=pin2)   # to agut (nota Do una octava mes amunt)
    elif pin_logo.is_touched():
        music.play(MELODIA, pin=pin2)     # melodia completa al tocar el logo
    sleep(100)
