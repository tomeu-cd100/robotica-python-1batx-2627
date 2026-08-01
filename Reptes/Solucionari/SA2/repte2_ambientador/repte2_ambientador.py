# SA2 - Repte 2 (SOLUCIO): ambientador de llum i so per a una habitacio
# Nucli + ampliacions 1-3: dos colors amb boto A, respiracio d'intensitat,
# color sincronitzat amb la melodia.
# Maquinari: LED RGB als pins P8 (vermell), P12 (verd), P16 (blau) i
# brunzidor al pin P2 del Micro:shield (Kit 1).
# Nivell SA2: nomes variables simples (cap color en tupla ni diccionari),
# funcions amb parametres separats i if/elif.

from microbit import *
import music

# Colors en tres variables simples (vermell, verd, blau) per a cada mode.
RELAX_R = 0
RELAX_G = 200
RELAX_B = 600     # blau suau

FESTA_R = 700
FESTA_G = 0
FESTA_B = 700     # magenta viu


def mostra_color(vermell, verd, blau):
    pin8.write_analog(vermell)
    pin12.write_analog(verd)
    pin16.write_analog(blau)


def transicio(r_final, g_final, b_final, passos, espera):
    # Transicio suau des d'apagat fins al color final (nucli).
    for i in range(passos + 1):
        vermell = r_final * i // passos
        verd = g_final * i // passos
        blau = b_final * i // passos
        mostra_color(vermell, verd, blau)
        sleep(espera)


def respira(r, g, b, cicles=1):
    # Ampliacio 2: la intensitat del color "respira" (puja i baixa).
    for c in range(cicles):
        for i in range(0, 21):
            mostra_color(r * i // 20, g * i // 20, b * i // 20)
            sleep(20)
        for i in range(20, -1, -1):
            mostra_color(r * i // 20, g * i // 20, b * i // 20)
            sleep(20)


def toca_nota(freq, durada, r, g, b):
    # Una nota + el seu color associat (greu=blau, agut=vermell).
    mostra_color(r, g, b)
    music.pitch(0, 0)  # evita solapament residual d'una nota anterior
    music.pitch(freq, durada, pin=pin2)


def melodia_sincronitzada():
    # Ampliacio 3: canvia de color a cada nota, en lloc de fer sonar
    # la melodia sencera d'un cop amb music.play(). Quatre crides seguides
    # (una per nota) en lloc de recorrer una llista/diccionari.
    toca_nota(262, 200, 0, 0, 1023)      # C4 - blau
    toca_nota(330, 200, 0, 600, 400)     # E4
    toca_nota(392, 200, 400, 600, 0)     # G4
    toca_nota(523, 400, 1023, 0, 0)      # C5 - vermell


# --- Engegada: transicio suau + melodia de benvinguda (requisit minim) ---
transicio(RELAX_R, RELAX_G, RELAX_B, 20, 30)
melodia_sincronitzada()

mode_festa = False

while True:
    if button_a.is_pressed():
        mode_festa = not mode_festa   # Ampliacio 1: alterna entre dos colors ambient
        sleep(300)

    if mode_festa:
        respira(FESTA_R, FESTA_G, FESTA_B)
    else:
        respira(RELAX_R, RELAX_G, RELAX_B)
