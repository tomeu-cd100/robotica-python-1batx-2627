# SA2 - Repte 2 (SOLUCIO): ambientador de llum i so per a una habitacio
# Nucli + ampliacions 1-3: dos colors amb boto A, respiracio d'intensitat,
# color sincronitzat amb la melodia.
# Maquinari: LED RGB als pins P8 (vermell), P12 (verd), P16 (blau) i
# brunzidor al pin P2 del Micro:shield (Kit 1).

from microbit import *
import music

COLOR_RELAX = (0, 200, 600)     # blau suau
COLOR_FESTA = (700, 0, 700)     # magenta viu
MELODIA = ['C4:2', 'E4:2', 'G4:2', 'C5:4']

# Ampliacio 3: un color per nota (greu=blau, agut=vermell).
COLORS_PER_NOTA = {
    'C4': (0, 0, 1023),
    'E4': (0, 600, 400),
    'G4': (400, 600, 0),
    'C5': (1023, 0, 0),
}


def mostra_color(vermell, verd, blau):
    pin8.write_analog(vermell)
    pin12.write_analog(verd)
    pin16.write_analog(blau)


def transicio(color_final, passos=20, espera=30):
    # Transicio suau des d'apagat fins al color final (nucli).
    r_final, g_final, b_final = color_final
    for i in range(passos + 1):
        mostra_color(r_final * i // passos, g_final * i // passos, b_final * i // passos)
        sleep(espera)


def respira(color, cicles=1):
    # Ampliacio 2: la intensitat del color "respira" (puja i baixa).
    r, g, b = color
    for c in range(cicles):
        for i in range(0, 21):
            mostra_color(r * i // 20, g * i // 20, b * i // 20)
            sleep(20)
        for i in range(20, -1, -1):
            mostra_color(r * i // 20, g * i // 20, b * i // 20)
            sleep(20)


def melodia_sincronitzada():
    # Ampliacio 3: canvia de color a cada nota, en lloc de fer sonar
    # la melodia sencera d'un cop amb music.play().
    for nota in MELODIA:
        clau = nota.split(':')[0]
        color = COLORS_PER_NOTA.get(clau, (200, 200, 200))
        mostra_color(*color)
        music.pitch(0, 0)  # evita solapament residual d'una nota anterior
        durada_notes = int(nota.split(':')[1]) * 100
        freq = 262 if clau == 'C4' else 330 if clau == 'E4' else 392 if clau == 'G4' else 523
        music.pitch(freq, durada_notes, pin=pin2)


# --- Engegada: transicio suau + melodia de benvinguda (requisit minim) ---
transicio(COLOR_RELAX)
melodia_sincronitzada()

mode_festa = False

while True:
    if button_a.is_pressed():
        mode_festa = not mode_festa   # Ampliacio 1: alterna entre dos colors ambient
        sleep(300)

    if mode_festa:
        respira(COLOR_FESTA)
    else:
        respira(COLOR_RELAX)
