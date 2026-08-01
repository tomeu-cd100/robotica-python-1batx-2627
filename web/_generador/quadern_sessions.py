# -*- coding: utf-8 -*-
"""Dades del quadern tècnic imprimible: una entrada per sessió lectiva.

Font única per a `generar_quadern_tecnic.py`. Cada sessió porta el títol
CANÒNIC de la guia docent (capçalera «## SESSIÓ n (2 h) — …»; SA9 usa les
fases de la taula «Seqüència de sessions») — `tools/qa.py` comprova que no
es desincronitzin. Els camps `avui` i `vocab` estan curats a mà des de les
guies i fitxes, en llenguatge d'alumne.

La darrera sessió de cada trimestre és la prova pràctica (`"prova": True`).

Tasks 7-15 (guies docents de SA1-SA9) completades: totes les sessions
reflecteixen ja el contingut curricular real del curs nou (Robòtica amb
Python, micro:bit V2 + Micro:shield + sensors Keyestudio, MicroPython;
SA1=6 h, SA2=8 h, SA3=8 h, SA4=8 h, SA5=6 h, SA6=8 h, SA7=8 h, SA8=6 h,
SA9=10 h, quadrant amb `Programació didàctica/08_Sequenciacio_temporal_
anual.md`). El `titol` de cada sessió coincideix literalment amb la
capçalera «## SESSIÓ n (2 h) — …» de la guia docent corresponent (SA1-SA8;
SA9 usa les fases de la seva taula «Seqüència de sessions» i queda
exempta d'aquesta comparació literal, vegeu `tools/qa.py:comprova_
quadern()`). `PROVES` (T1-T3) reflecteix el títol real de cada
`Avaluació/Prova_practica_Tn.md` (Task 16 completada).
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
    "SA5": "Ràdio: robots que parlen",
    "SA6": "Sistemes de control",
    "SA7": "Robòtica mòbil",
    "SA8": "Autonomia i telemetria",
    "SA9": "Repte final integrador",
}

# Una entrada per sessió lectiva real de cada SA. La darrera SA de cada
# trimestre porta, a més, una sessió de prova pràctica.
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
        _s("SA5", 1, "Xat per ràdio: enviar i rebre missatges",
           "Avui he activat la radio de la meva placa (radio.on, "
           "radio.config amb un grup) i he enviat i rebut missatges de "
           "text amb un company, guardant els ultims a una llista.",
           "radio, group, radio.send, radio.receive, llista"),
        _s("SA5", 2, "Dissenyar un protocol de comandes",
           "Avui he dissenyat el meu propi protocol de comandes (prefix "
           "CMD: + una ordre curta) i l'he enviat amb botons i gestos. He "
           "fet el mini-check individual (no qualifica).",
           "protocol, prefix, accelerometer, gest, esdeveniment"),
        _s("SA5", 3, "Repte «control remot bàsic» (producte de la SA)",
           "Avui he tancat el repte control remot basic: el vehicle rep "
           "les meves ordres per radio i les converteix en moviment amb "
           "les funcions de la SA4. He guardat l'historic en tuples.",
           "esdeveniment, accio, tupla, historic de comandes"),
        _s("SA6", 1, "Llaç obert i llaç tancat: la màquina d'estats",
           "Avui he distingit llac obert de llac tancat amb exemples del "
           "vehicle, he dissenyat el meu diagrama d'estats RUN/STOP/ALERTA "
           "i he provat una FSM de semafor i un termostat amb histeresi.",
           "llac obert, llac tancat, maquina d'estats, transicio, histeresi"),
        _s("SA6", 2, "Aturada d'emergència prioritària",
           "Avui he programat l'estat STOP com a prioritari: es dispara amb "
           "el polsador o amb una comanda de radio dedicada i interromp "
           "qualsevol moviment. He fet el mini-check individual (no "
           "qualifica) i he provat el registre de dades amb el modul log.",
           "STOP prioritari, polsador, actualitza_estat, log, MY_DATA.HTM"),
        _s("SA6", 3, "Repte «vehicle amb aturada d'emergència» (producte de la SA — es tanca el Projecte T2)",
           "Avui he tancat el repte vehicle amb aturada d'emergencia: "
           "protocol de radio complet (F/B/L/R/S/X) i maquina d'estats amb "
           "STOP prioritari. He tancat el Projecte T2 amb una mini-defensa breu.",
           "protocol CMD, comanda X, maquina d'estats, mini-defensa, Projecte T2"),
        _s("SA6", 4, "PROVA PRÀCTICA T2 (individual)",
           "Avui he fet la prova pràctica individual del 2n trimestre "
           "(SA4-SA6): funcions de moviment, radio i sistemes de control "
           "amb maquina d'estats.",
           "prova practica, avaluacio individual", prova=True),
    ],
    3: [
        _s("SA7", 1, "Cinemàtica diferencial: el rover gira",
           "Avui he revisat el meu rover muntat i he calibrat "
           "FACTOR_M1/FACTOR_M2 perque vagi recte, reutilitzant les funcions "
           "de moviment de la SA4. He provat una trajectoria en quadrat amb "
           "girs i avancos temporitzats.",
           "cinematica diferencial, calibratge, motoreductor, trajectoria"),
        _s("SA7", 2, "Seguidor de línia",
           "Avui he programat el seguidor de linia del rover: lectura amb "
           "read_analog() i un llindar calibrat sobre el meu circuit real, "
           "amb correccio de rumb cap al costat on es perd la linia. He fet "
           "el mini-check individual (no qualifica).",
           "seguidor de linia, read_analog, llindar, ADC, correccio de rumb"),
        _s("SA7", 3, "Evita-obstacles amb ultrasons",
           "Avui he programat l'evita-obstacles amb l'HC-SR04 "
           "(mesura_distancia amb machine.time_pulse_us, mateix metode que "
           "la SA3, pins nous). He triat el meu comportament autonom "
           "(linia i/o obstacles) pel repte d'aquesta sessio.",
           "HC-SR04, time_pulse_us, temps de vol, evita-obstacles"),
        _s("SA7", 4, "Integració: missions del rover (producte de la SA)",
           "Avui he integrat el meu comportament autonom en una estructura "
           "de missions (rover_missions.py) amb un polsador STOP prioritari, "
           "amb millores de velocitat i marge de seguretat. He fet la "
           "mini-defensa breu d'una decisio de disseny.",
           "missio, integracio, polsador STOP, mini-defensa"),
        _s("SA8", 1, "Sensors avançats: llegir el Kit 3",
           "Avui he conegut els sensors avancats del Kit 3 (IMU MPU6050, "
           "DHT11, BMP280, CCS811), he programat comportaments.py (FSM de "
           "prioritats SEGUIR/ESQUIVAR/RECUPERAR) i he dissenyat el meu "
           "format de missatge de telemetria.",
           "IMU, I2C, DHT11, FSM de prioritats, protocol de telemetria"),
        _s("SA8", 2, "Telemetria per ràdio: enviar i registrar",
           "Avui he programat telemetria_radio.py (sensors del Kit 3 + "
           "radio amb prefix TEL:) i el meu propi estacio_base.py (rebre, "
           "mostrar i registrar amb log). He fet el mini-check individual "
           "(no qualifica).",
           "radio.send, prefix TEL, log, llista, mitjana simple"),
        _s("SA8", 3, "IA aplicada al control i producte: sistema de telemetria",
           "Avui he fet una practica guiada de classificacio de patrons "
           "(Teachable Machine) i he tancat el producte: sistema de "
           "telemetria del rover amb com a minim dos sensors, radio i "
           "registre. He fet la mini-defensa breu i la reflexio d'IA i "
           "etica de dades.",
           "IA aplicada al control, biaix, etica de dades, mini-defensa"),
        _s("SA9", 1, "Idear",
           "Avui he triat el meu repte lliure al banc de reptes de la SA9, "
           "he definit els requisits minims i he fet un esbos de la solucio, "
           "amb la planificacio de les properes sessions.",
           "repte lliure, requisits minims, esbos, planificacio"),
        _s("SA9", 2, "Prototipar",
           "Avui he muntat el component nou del meu repte i he programat "
           "un prototip minim viable a partir de plantilla_projecte.py "
           "(percep/decideix/actua), integrant almenys un element nou.",
           "prototip minim viable, percep, decideix, actua"),
        _s("SA9", 3, "Provar i millorar",
           "Avui he provat el meu sistema (DEPURA), he fet una prova de "
           "limit i una primera iteracio de millora, i he avancat el meu "
           "dossier tecnic (objectiu, disseny, esquema de connexions).",
           "prova de limit, iteracio, dossier tecnic, DEPURA"),
        _s("SA9", 4, "Comunicar",
           "Avui he tancat el meu dossier tecnic complet i he fet la meva "
           "defensa oral individual (5' + preguntes) amb demostracio del "
           "meu rover ampliat. Producte de la SA9.",
           "dossier tecnic, defensa oral individual, R4-DO, demostracio"),
        _s("SA9", 5, "Prova pràctica T3 (individual)",
           "Avui he fet la prova pràctica individual del 3r trimestre "
           "(SA7-SA8), per estacions rotatives (taula + pista): no reavalua "
           "el meu projecte de la SA9.",
           "prova practica, avaluacio individual, estacions rotatives", prova=True),
    ],
}

# Prova pràctica de cada trimestre (Avaluació/Prova_practica_Tn.md). El
# títol coincideix literalment amb l'«## » de la 2a línia de cada document.
PROVES = {
    1: {"titol": "Estació personal d'alertes",
        "material": "micro:bit V2 · Micro:shield · sensors Keyestudio",
        "reflexio_final": False},
    2: {"titol": "Vehicle amb màquina d'estats + control amb histèresi",
        "material": "micro:bit V2 · Micro:shield · sensors Keyestudio",
        "reflexio_final": False},
    3: {"titol": "Rover autònom + telemetria",
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
