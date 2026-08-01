# 🛟 Targetes de rescat

> **Per a l'alumnat.** Quan et quedis encallat en una pràctica, **no esperis el docent ni depenguis d'un company**: agafa la targeta de la teva SA i segueix els tres nivells de pista **en ordre**. Anota al quadern tècnic quin nivell has fet servir (no penalitza: forma part d'aprendre a depurar).

## Com es fa servir

1. **Nivell 1 · Pregunta conceptual.** Rellegeix la pregunta i respon-te-la abans de tocar el codi. Sovint és suficient.
2. **Nivell 2 · Pas concret.** Si segueixes encallat, segueix el pas indicat: què has de mirar o provar exactament.
3. **Nivell 3 · Fragment amb forat.** Última opció: un tros de codi gairebé complet, amb un `___` que has d'omplir tu mateix. Mai còpia-i-enganxa sense entendre què fa la línia.

Si després del nivell 3 encara estàs encallat: crida el docent (senyal de la classe) o consulta el glossari (`00_Glossari_tecnic.md`).

> Has faltat a la sessió i no saps per on començar? Això no és per a tu: vés a [`00_Vaig_faltar.md`](00_Vaig_faltar.md).

---

## SA1 · Introducció a la robòtica

**Nivell 1.** Estàs treballant amb `display`, `button_a`/`button_b` o `accelerometer`? Quin d'aquests tres «sap» el programa que has de fer servir?

**Nivell 2.** Prova el fragment aïllat a la consola REPL del simulador (només aquesta línia) abans de posar-lo dins del programa sencer. Si funciona sol però no dins del programa, l'error és d'indentació o d'ordre, no de la instrucció.

**Nivell 3.**
```python
while True:
    if button_a.is_pressed():
        display.show(Image.___)
    sleep(200)
```

## SA2 · Sortides digitals i PWM

**Nivell 1.** El component fa alguna cosa (encara que no sigui el que esperaves), o no fa res? Si no fa res, és un problema de **cablatge/pin**; si fa una cosa inesperada, és un problema de **codi**.

**Nivell 2.** Comprova el pin exacte al `00_Fil_conductor_construccions.md` (mapa de pins) i que `write_digital` (0/1) no s'hagi confós amb `write_analog` (0-1023, PWM).

**Nivell 3.**
```python
pin0.write_analog(___)   # 0 = apagat, 1023 = màxima intensitat
sleep(1000)
pin0.write_digital(0)
```

## SA3 · Entrades i sensors

**Nivell 1.** Has **llegit el valor real** del sensor (amb `print()` o al display) abans de decidir el llindar, o t'has inventat un número?

**Nivell 2.** Calibra: anota el valor del sensor en repòs i el valor quan «passa la cosa» que vols detectar; el llindar va **entre els dos**, no a l'atzar.

**Nivell 3.**
```python
llindar = ___
while True:
    valor = pin0.read_analog()
    if valor > llindar:
        display.show(Image.YES)
    else:
        display.show(Image.NO)
    sleep(200)
```

## SA4 · Funcions i moviment

**Nivell 1.** La funció està **definida** (`def`) abans d'on la **crides**? Python llegeix de dalt a baix: no pots cridar una funció que encara no existeix.

**Nivell 2.** Prova la funció sola, cridant-la un cop des del `while True:`, sense res més al voltant. Si funciona sola però no combinada amb altres, el problema és l'**ordre de crides**, no la funció.

**Nivell 3.**
```python
def avancar():
    motor_esq.write_analog(___)
    motor_dre.write_analog(___)

def aturar():
    motor_esq.write_analog(0)
    motor_dre.write_analog(0)
```

## SA5 · micro:bit i MicroPython (ràdio)

**Nivell 1.** Les **dues** plaques tenen `radio.on()` i el **mateix `group`**? Sense el mateix grup, no es «senten» encara que estiguin engegades.

**Nivell 2.** Comprova per separat: la que envia mostra al display que ha enviat (`display.show(Image.YES)` després del `send`); la que rep, imprimeix (`print`) tot el que arriba, encara que no sigui el que esperaves.

**Nivell 3.**
```python
import radio
radio.on()
radio.config(group=___)
radio.send("AVANÇAR")
msg = radio.receive()
```

## SA6 · Sistemes de control

**Nivell 1.** Quin és l'**estat actual** del teu sistema en aquest instant (RUN, STOP, ALERTA…)? Si no ho pots dir en una paraula, encara no tens una màquina d'estats, tens un embolic de `if`.

**Nivell 2.** Dibuixa (paper o quadern) els estats possibles i les fletxes de transició abans de tocar més codi; després tradueix **cada fletxa** a un `if`.

**Nivell 3.**
```python
estat = "RUN"
while True:
    if boto_emergencia.is_pressed():
        estat = "STOP"
    if estat == "STOP":
        aturar()
    elif estat == "___":
        avancar()
```

## SA7 · Robòtica mòbil

**Nivell 1.** El robot gira cap al costat **contrari** del que volies? Sovint és que els dos motors estan **invertits** (esquerra↔dreta) al cablatge o al codi, no un error de lògica.

**Nivell 2.** Prova `avancar()`, `girar("esquerra")` i `girar("dreta")` **per separat**, sobre la taula (rodes enlaire), abans de combinar-los amb sensors.

**Nivell 3.**
```python
def girar(costat):
    if costat == "esquerra":
        motor_esq.write_analog(0)
        motor_dre.write_analog(___)
    elif costat == "dreta":
        motor_esq.write_analog(___)
        motor_dre.write_analog(0)
```

## SA8 · IoT i IA (autonomia i telemetria)

**Nivell 1.** El problema és que **no arriba** la dada (ràdio) o que arriba **però és incorrecta** (sensor/format)? Separa-ho: imprimeix la dada abans d'enviar-la i just en rebre-la.

**Nivell 2.** Envia sempre el mateix format de missatge (per exemple `"TEMP:23.5"`) i, a l'estació base, comprova primer que el missatge **no és `None`** abans de processar-lo.

**Nivell 3.**
```python
msg = radio.receive()
if msg is not None:
    if msg.startswith("___"):
        valor = msg.split(":")[1]
        display.scroll(valor)
```

## SA9 · Projecte final integrador

**Nivell 1.** El teu repte final és massa gran per depurar-lo tot de cop? Torna a la versió que **sí que funcionava** (control de versions o còpia de seguretat) i afegeix la funcionalitat nova **una peça cada vegada**.

**Nivell 2.** Fes una llista de les funcions/comportaments que ja tens provats i funcionant per separat; integra'ls d'un en un, provant després de cada integració.

**Nivell 3.** No hi ha fragment: a SA9 el rescat és **metodològic**. Revisa `00_Quadern_tecnic.md` §«🐞 Error del dia» i la rutina DEPURA de `00_Mode_supervivencia.md`.
