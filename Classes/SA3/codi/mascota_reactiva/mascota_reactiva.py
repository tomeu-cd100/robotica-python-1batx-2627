# SA3 - mascota_reactiva.py  (INTEGRADOR / PRODUCTE de la SA3)
# La mascota reacciona a l'entorn: soroll, foscor, presencia (PIR), carinyo
# (polsador) i sacsejada (accelerometre), amb cara (display) i so.
# Cablatge EXACTE del Projecte T1 (00_Projecte_T1_Mascota.md):
#   P0 servo (orelles/cua, NOMES muntat; es programa a la SA4, no aqui)
#   P1 LED/RGB (indicador d'humor) · P2 brunzidor
#   P8 PIR (digital) · P12 polsador (digital, pull-up + antirebot)
#   Microfon: microphone.sound_level() intern (alternativa valida al
#   sensor de so extern del Kit 3, que aniria al pin P4 analogic).
# Veure SA3_esquemes_connexions.md i el dossier de la mascota.

from microbit import *
import music

LLINDAR_SOROLL = 150     # nivell de so (0-255) per sobre = espant
LLINDAR_FOSCOR = 50      # nivell de llum (0-255) per sota = son
TEMPS_CALMA = 8000       # ms sense estimuls per tornar a l'estat de calma
ANTIREBOT_MS = 200       # antirebot per software del polsador

CONTENT, ESPANTAT, ADORMIT, CURIOS, CONTENT_CARICIA = range(5)
emocio = CONTENT
t_ultim_estimul = running_time()
t_ultim_polsador = running_time()

pin12.set_pull(pin12.PULL_UP)   # polsador: repos = 1, premut = 0


def canvia_emocio(nova):
    global emocio, t_ultim_estimul
    if nova == emocio:
        return   # si ja hi es, no repeteix cara ni so
    emocio = nova
    t_ultim_estimul = running_time()
    if emocio == CONTENT:
        display.show(Image.HAPPY)
        music.play(['C4:2', 'E4:2', 'G4:2'], wait=False)
    elif emocio == ESPANTAT:
        display.show(Image.SURPRISED)
        music.pitch(880, 200, pin=pin2, wait=False)
    elif emocio == ADORMIT:
        display.show(Image.ASLEEP)
        music.play(['C4:8'], pin=pin2, wait=False)
    elif emocio == CURIOS:
        display.show(Image.CONFUSED)
        music.play(['E4:2', 'C4:2'], pin=pin2, wait=False)
    elif emocio == CONTENT_CARICIA:
        display.show(Image.HEART)
        music.play(['E4:2', 'G4:2', 'C5:4'], pin=pin2, wait=False)


def llegeix_sensors():
    global t_ultim_polsador

    soroll = microphone.sound_level()   # 0-255, microfon integrat V2
    llum = display.read_light_level()   # 0-255, sensor de llum integrat

    # Reaccio 1: soroll fort -> ESPANTAT (la primera que salta mana).
    if soroll > LLINDAR_SOROLL:
        canvia_emocio(ESPANTAT)
        return

    # Reaccio 2: es fa fosc -> ADORMIT.
    if llum < LLINDAR_FOSCOR:
        canvia_emocio(ADORMIT)
        return

    # Reaccio 3: el PIR detecta algu -> saluda amb curiositat.
    if pin8.read_digital() == 1:
        canvia_emocio(CURIOS)
        return

    # Reaccio 4: caricia al polsador (amb antirebot per software) -> calma-la.
    if pin12.read_digital() == 0:
        ara = running_time()
        if ara - t_ultim_polsador > ANTIREBOT_MS:
            t_ultim_polsador = ara
            canvia_emocio(CONTENT_CARICIA)
        return

    # Reaccio 5: sacsejada -> tambe respon amb curiositat.
    if accelerometer.was_gesture('shake'):
        canvia_emocio(CURIOS)
        return


while True:
    llegeix_sensors()
    if emocio != ADORMIT and running_time() - t_ultim_estimul > TEMPS_CALMA:
        canvia_emocio(CONTENT)
    sleep(50)
