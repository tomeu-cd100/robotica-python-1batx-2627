# -*- coding: utf-8 -*-
"""Dades del quadern tècnic imprimible: una entrada per sessió lectiva.

Font única per a `generar_quadern_tecnic.py`. Cada sessió porta el títol
CANÒNIC de la guia docent (capçalera «## SESSIÓ n (2 h) — …»; SA9 usa les
fases de la taula «Seqüència de sessions») — `tools/qa.py` comprova que no
es desincronitzin. Els camps `avui` i `vocab` estan curats a mà des de les
guies i fitxes, en llenguatge d'alumne.

La darrera sessió de cada trimestre és la prova pràctica (`"prova": True`).

TODO (Tasks 7-15, guies docents de cada SA): aquest fitxer és un ESQUELET
MÍNIM del curs nou (Robòtica amb Python, micro:bit V2 + Micro:shield +
sensors Keyestudio, MicroPython). El contingut curricular detallat del curs
germà (Arduino UNO, Servo.h, pont H L298N...) NO és vàlid aquí i s'ha
substituït per placeholders d'una sola sessió per SA. Quan es creïn les
guies docents reals, cal:
  1. Desglossar cada SA en les seves sessions reals (2 h cadascuna, tantes
     com calguin perquè `n * 2` quadri amb les hores de
     `Programació didàctica/08_Sequenciacio_temporal_anual.md`: SA1=6,
     SA2=8, SA3=8, SA4=8, SA5=6, SA6=8, SA7=8, SA8=6, SA9=10).
  2. Fer que el `titol` de cada sessió coincideixi literalment amb la
     capçalera «## SESSIÓ n (2 h) — …» de la guia docent corresponent
     (ho valida `tools/qa.py:comprova_quadern()`).
  3. Omplir `avui`/`vocab` amb el contingut real de la sessió.
Mentre això no existeixi, `tools/qa.py --nomes-sintaxi` salta els checks
que depenen d'aquest fitxer (5 i 12).
"""

def _s(sa, s, titol, avui, vocab, prova=False):
    return {"sa": sa, "s": s, "titol": titol, "avui": avui, "vocab": vocab,
            "prova": prova}


# Títol de cada SA (ha de coincidir amb SA_TRIMESTRE, més avall).
_TITOL_SA = {
    "SA1": "Hola, robot!",
    "SA2": "Sortides digitals i PWM",
    "SA3": "Entrades i sensors",
    "SA4": "Funcions i moviment",
    "SA5": "Ràdio i comunicació",
    "SA6": "Sistemes de control",
    "SA7": "Robòtica mòbil",
    "SA8": "Autonomia i telemetria",
    "SA9": "Repte final integrador",
}

# TODO: placeholder d'UNA sessió per SA (vegeu el TODO de dalt). La darrera
# SA de cada trimestre porta, a més, una sessió de prova pràctica.
SESSIONS = {
    1: [
        _s("SA1", 1, "Què és un robot?",
           "Avui he apres el model entrada-proces-sortida i que es un sistema "
           "embegut. He analitzat 3 sistemes quotidians (rentadora, dron, "
           "semafor) i he fet la prova diagnostica (no qualifica).",
           "robot, sistema embegut, entrada, proces, sortida"),
        _s("SA1", 2, "Arquitectura de la micro:bit i seguretat",
           "Avui he conegut les parts de la micro:bit (display, botons, "
           "sensors interns) i he llegit i signat les normes de seguretat "
           "del laboratori.",
           "microcontrolador, sensor, actuador, placa, digital, analogic"),
        _s("SA1", 3, "El primer programa MicroPython",
           "Avui he llegit, provat i modificat el meu primer programa "
           "MicroPython (from microbit import *, display.scroll, display.show, "
           "sleep) i he comencat la fitxa-poster.",
           "MicroPython, display, bucle, while True"),
        _s("SA2", 1, "Sortides digitals amb bucles",
           "Avui he encaixat el Micro:shield i he controlat un LED extern amb "
           "sortides digitals (write_digital), bucles i un acumulador que "
           "compta els parpellejos.",
           "sortida digital, write_digital, bucle for, acumulador"),
        _s("SA2", 2, "Sortides PWM i so",
           "Avui he controlat sortides PWM (write_analog, 0-1023): intensitat "
           "d'un LED i colors combinats d'un LED RGB, i he fet sonar melodies "
           "i tons amb el modul music.",
           "PWM, write_analog, LED RGB, music, to, melodia"),
        _s("SA2", 3, "Repte «semàfor o llum d'ambient» (producte de la SA)",
           "Avui he muntat i programat el meu repte «semafor o llum "
           "d'ambient»: LED, LED RGB, brunzidor i rele amb bucles, PWM i "
           "temps en variables. He fet la mini-defensa oral d'una decisio.",
           "rele, variables de temps, funcions, mini-defensa"),
        _s("SA2", 4, "Fabricació i muntatge de la mascota",
           "Avui he muntat fisicament la carcassa de la meva mascota: he "
           "fixat la micro:bit i el Micro:shield, he muntat el servo i he "
           "cablejat el LED/RGB i el brunzidor per validar-los amb el codi "
           "ja fet.",
           "fabricacio, muntatge, cablatge, mascota"),
        _s("SA3", 1, "Entrades digitals i condicionals",
           "Avui he llegit entrades digitals (button_a/button_b, polsador amb "
           "pull-up) amb if/elif/else i he fet un comptador de premudes al "
           "REPL, amb antirebot per software.",
           "entrada digital, pull-up, antirebot, read_digital, REPL"),
        _s("SA3", 2, "Entrades analògiques: llum i temperatura",
           "Avui he llegit entrades analogiques (read_analog, 0-1023) i "
           "sensors interns (llum 0-255, temperatura en graus C), i he "
           "programat una funcio mapa() per convertir rangs. He fet el "
           "mini-check individual (no qualifica).",
           "entrada analogica, read_analog, mapa, llindar, ADC"),
        _s("SA3", 3, "Repte «mascota reactiva» (producte de la SA — es tanca la mascota T1)",
           "Avui he cablejat la mascota amb el cablatge exacte del dossier i "
           "he programat almenys 2 reaccions sensor-resposta (so, llum, PIR, "
           "polsador, sacsejada). He tancat el Projecte T1 amb una "
           "mini-defensa breu.",
           "PIR, HC-SR04, temps de vol, condicionals encadenats, mascota"),
        _s("SA3", 4, "PROVA PRÀCTICA T1 (individual)",
           "Avui he fet la prova pràctica individual del 1r trimestre "
           "(SA1-SA3): entrades i sortides, condicionals, bucles i el "
           "mètode de projecte.",
           "prova practica, avaluacio individual", prova=True),
    ],
    2: [
        _s("SA4", 1, "Definir funcions amb paràmetres i valor de retorn",
           "Avui he posat nom al concepte de funcio (def, parametre, valor "
           "de retorn) i l'he fet servir per programar per primer cop el "
           "servo de la mascota (graus_a_pwm, mou_servo, saluda, escombra).",
           "funcio, def, parametre, valor de retorn, servo, set_analog_period"),
        _s("SA4", 2, "Controlar un motoreductor amb funcions de moviment",
           "Avui he muntat els dos motoreductors del vehicle i he programat "
           "les funcions avancar, retrocedir, girar i aturar amb PWM i "
           "sentit de gir. He fet el mini-check individual (no qualifica).",
           "motoreductor, PWM, sentit de gir, canal M1/M2, write_analog"),
        _s("SA4", 3, "Repte «control per botons» (producte de la SA)",
           "Avui he programat la meva propia sequencia de moviments "
           "(avancar/girar/retrocedir/aturar) activada amb els botons A/B. "
           "He fet la mini-defensa breu d'una decisio de disseny.",
           "sequencia, estat, boto A/B, funcions de moviment"),
        _s("SA4", 4, "Muntatge físic del vehicle",
           "Avui he muntat fisicament el xassis del vehicle T2: motoreductors "
           "i roda boja, micro:bit i Micro:shield, portapiles, i he fet la "
           "prova d'encesa amb les funcions de moviment ja programades.",
           "fabricacio, muntatge, xassis, vehicle, prova d'encesa"),
        _s("SA5", 1, _TITOL_SA["SA5"],
           "TODO: pendent de la guia docent de SA5 (radio.on/config/send/receive).",
           "TODO"),
        _s("SA6", 1, _TITOL_SA["SA6"],
           "TODO: pendent de la guia docent de SA6 (llaç obert/tancat, histèresi).",
           "TODO"),
        _s("SA6", 2, "PROVA PRÀCTICA T2 (individual)",
           "TODO: pendent de definir l'enunciat de la prova del 2n trimestre.",
           "TODO", prova=True),
    ],
    3: [
        _s("SA7", 1, _TITOL_SA["SA7"],
           "TODO: pendent de la guia docent de SA7 (robot mòbil, cinemàtica diferencial).",
           "TODO"),
        _s("SA8", 1, _TITOL_SA["SA8"],
           "TODO: pendent de la guia docent de SA8 (telemetria per ràdio, autonomia).",
           "TODO"),
        _s("SA9", 1, _TITOL_SA["SA9"],
           "TODO: pendent de la guia docent de SA9 (projecte/repte final).",
           "TODO"),
        _s("SA9", 2, "PROVA PRÀCTICA T3 (individual)",
           "TODO: pendent de definir l'enunciat de la prova del 3r trimestre.",
           "TODO", prova=True),
    ],
}

# Prova pràctica de cada trimestre (Avaluació/Prova_practica_Tn.md).
# TODO: enunciat i títol pendents; el maquinari ja reflecteix el curs nou.
PROVES = {
    1: {"titol": "TODO",
        "material": "micro:bit V2 · Micro:shield · sensors Keyestudio",
        "reflexio_final": False},
    2: {"titol": "TODO",
        "material": "micro:bit V2 · Micro:shield · sensors Keyestudio",
        "reflexio_final": False},
    3: {"titol": "TODO",
        "material": "micro:bit V2 · Micro:shield · sensors Keyestudio · robot mòbil",
        "reflexio_final": True},
}

# Situacions d'aprenentatge de cada trimestre (per a portada i índex).
SA_TRIMESTRE = {
    1: [("SA1", _TITOL_SA["SA1"]), ("SA2", _TITOL_SA["SA2"]),
        ("SA3", _TITOL_SA["SA3"])],
    2: [("SA4", _TITOL_SA["SA4"]), ("SA5", _TITOL_SA["SA5"]),
        ("SA6", _TITOL_SA["SA6"])],
    3: [("SA7", _TITOL_SA["SA7"]), ("SA8", _TITOL_SA["SA8"]),
        ("SA9", _TITOL_SA["SA9"])],
}
