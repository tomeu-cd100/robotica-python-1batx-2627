# SA0 · Vocabulari de robòtica

> **Per a què serveix aquest document?** És el teu **diccionari de butxaca** de tot el curs. Aquí hi trobaràs els termes bàsics que faràs servir des del primer dia, sempre amb un exemple de la **micro:bit**. Quan a classe surti una paraula que no recordis, busca-la aquí. No cal estudiar-lo de memòria: és per **consultar**.

**Com llegir cada entrada:** **Terme** → definició curta → *exemple amb la micro:bit*.

## Els cinc termes clau

| Terme | Què vol dir | Exemple amb la micro:bit |
|---|---|---|
| **Robot** | Màquina que **percep** l'entorn, **decideix** què fer i **actua** de manera automàtica. | Una micro:bit que, quan detecta poca llum (percep), decideix engegar un LED (actua). |
| **Sensor** | Component que **mesura** una magnitud de l'entorn i la converteix en una dada que el programa pot llegir. | El sensor de llum i el termòmetre **integrats** a la micro:bit; també el sensor d'ultrasons que connectarem al Micro:shield més endavant. |
| **Actuador** | Component que **fa una acció** física: es mou, s'encén, sona. | La matriu de 5×5 LEDs (mostra imatges), l'altaveu (fa sons), un servomotor connectat al Micro:shield (gira). |
| **Microcontrolador** | El petit "cervell" dins la placa que executa el programa, línia a línia. | El xip que hi ha sota la matriu de LEDs de la micro:bit. |
| **Programa** | El conjunt ordenat d'instruccions que li diem a la placa que faci. | El fitxer `.py` que escrius a l'editor i que la micro:bit executa quan l'engegues. |

## Com funciona un robot: entrada → procés → sortida

Tot robot segueix el mateix esquema, encara que sigui molt senzill:

| Fase | Pregunta | Exemple amb la micro:bit |
|---|---|---|
| **Entrada** | Què percep? | El botó A es prem, o l'acceleròmetre detecta un sacseig. |
| **Procés** | Què decideix el programa? | «Si s'ha premut el botó A, aleshores...» |
| **Sortida** | Què fa? | Mostra una cara al display, o fa sonar un so. |

## Programa, bucle i entrada/sortida

| Terme | Què vol dir | Exemple amb la micro:bit |
|---|---|---|
| **Bucle (`while True:`)** | Un tros de codi que es **repeteix sense parar** mentre la placa estigui engegada. | Gairebé tots els programes de micro:bit tenen un `while True:` que va comprovant botons i sensors contínuament. |
| **Entrada** | Una dada que **entra** al programa des del món exterior (un sensor, un botó). | `button_a.is_pressed()`, `accelerometer.get_x()`. |
| **Sortida** | Una acció que el programa **envia** cap al món exterior (un actuador). | `display.show(Image.HAPPY)`, `music.play(...)`. |
| **Variable** | Un "calaix" amb nom on el programa desa un valor que pot canviar. | `nombre = randint(1, 6)` desa un nombre a l'espera de mostrar-lo. |

## MicroPython vs Python

| | Python (a l'ordinador) | MicroPython (a la micro:bit) |
|---|---|---|
| **On s'executa** | A l'ordinador, dins d'un intèrpret complet. | Dins del microcontrolador de la placa, amb molta menys memòria. |
| **Llibreries** | Milers de llibreries generals (matemàtiques, webs, dades...). | Un subconjunt reduït + llibreries pròpies de la placa: `microbit`, `music`, `radio`. |
| **Com es prova** | S'executa directament amb l'intèrpret de Python. | Es **transfereix** a la placa (`.hex`) i s'hi executa sol, sense ordinador connectat. |
| **Per què serveix per aprendre** | És el llenguatge de referència: la sintaxi (variables, `if`, bucles, funcions) és **la mateixa**. | El que aprens aquí (sintaxi de Python) et serveix per a qualsevol altre programa Python. |

> El curs fa servir **MicroPython**, un "Python de butxaca" pensat per a microcontroladors com el de la micro:bit. La sintaxi (com s'escriu una condició, un bucle, una funció) és la mateixa que la de Python; el que canvia és quines llibreries hi ha disponibles.

## El mètode del curs

A totes les SA treballem amb el mateix cicle:

| Fase | Pregunta clau |
|---|---|
| **1. Analitzar** | Quin problema tinc? Què necessito? |
| **2. Dissenyar** | Com el penso resoldre **abans** de fer-ho? |
| **3. Programar/Prototipar** | Escric i provo una primera versió. |
| **4. Provar** | Funciona? On falla? |
| **5. Millorar** | Com ho faig millor? |

> Per aprendre com i on s'escriu, es prova i es transfereix el codi a la placa, ves a **[`SA0_primers_passos_editor.md`](SA0_primers_passos_editor.md)**.
