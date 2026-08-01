# SA8 · Qüestionari de conceptes (I2C, telemetria, protocol, IA aplicada al control)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega.

> **Ús.** Comprovació breu dels conceptes clau de la SA8: sensors avançats per I2C, protocol de telemetria per ràdio, registre de dades i marc conceptual mínim de la IA aplicada al control.
> Es pot fer servir com a **repàs formatiu** o com a **prova curta qualificable**
> (10 preguntes × 1 punt = **nota 0-10**). Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. Aquest codi ha de llegir l'acceleració de l'IMU MPU6050 per I2C, però el sensor no respon (segueix "adormit") fins que no s'hi afegeix una línia abans del bucle. Quina línia falta? (COMPLETAR)

   ```python
   from microbit import *

   MPU_ADR = 0x68
   MPU_REG_PWR = 0x6B
   MPU_REG_ACCEL = 0x3B

   ____                     # <-- quina linia hi va aqui?

   while True:
       i2c.write(MPU_ADR, bytes([MPU_REG_ACCEL]), repeat=True)
       dades = i2c.read(MPU_ADR, 6)
       sleep(100)
   ```

   - a) `i2c.write(MPU_ADR, bytes([MPU_REG_PWR, 0x00]))`
   - b) `i2c.read(MPU_ADR, 1)`
   - c) `radio.on()`
   - d) `display.show(Image.YES)`

2. Per què `telemetria_radio.py` fa servir el prefix `"TEL:"` i no el `"CMD:"` de la SA5/SA6?
   - a) Perquè `"CMD:"` ja no funciona a la micro:bit V2.
   - b) Perquè la telemetria és una **dada** informativa, no una **ordre**: un prefix diferent evita que la placa receptora confongui les dues coses.
   - c) No hi ha cap motiu, és arbitrari.
   - d) Perquè el mòdul `radio` obliga a canviar de prefix a cada SA.

3. Aquest codi hauria de mostrar la temperatura del DHT11 a cada volta, però `lectura` és gairebé sempre `None`. On és l'error? (CORREGIR)

   ```python
   from microbit import *

   while True:
       lectura = llegeix_dht11()
       if lectura is not None:
           temperatura = lectura[0]
           display.scroll(str(temperatura))
       sleep(20)
   ```

   - a) `sleep(20)` és massa curt: el DHT11 necessita 1-2 s entre lectures, si no, sovint torna `None`.
   - b) `lectura[0]` hauria de ser `lectura[1]`.
   - c) Falta cridar `radio.on()` abans del bucle.
   - d) `display.scroll()` no pot mostrar nombres.

4. Per què `telemetria_radio.py` envia un missatge nou només cada `INTERVAL_TELEMETRIA_MS` (500 ms) i no a cada volta del bucle principal (~20 ms)?
   - a) Perquè la ràdio de la micro:bit només pot enviar un missatge cada mitja hora.
   - b) Perquè enviar-ho tot a cada volta saturaria la ràdio i la pantalla de qui rep, amb missatges repetits sense informació nova.
   - c) Perquè `radio.send()` només es pot cridar un cop per programa.
   - d) No hi ha cap motiu tècnic.

5. Per què el codi i el producte de `estacio_base.py` són sempre **individuals**, encara que s'executi temporalment a la placa d'un company?
   - a) Perquè cada alumne el programa i l'interpreta ell mateix; la placa és només el banc de proves, no forma part de l'avaluació.
   - b) No ho són: si dos alumnes fan servir la mateixa placa, comparteixen la nota.
   - c) Perquè la ràdio només funciona amb un únic programa a tot el curs.
   - d) Perquè `estacio_base.py` és opcional i no s'avalua.

6. Quin és el resultat d'executar aquest codi (mateixa FSM que `comportaments.py`, amb `distancia = 10`)? (TRAÇA)

   ```python
   SEGUIR, ESQUIVAR, RECUPERAR = range(3)
   NOMS_ESTAT = {SEGUIR: "SEGUIR", ESQUIVAR: "ESQUIVAR", RECUPERAR: "RECUPERAR"}
   estat = SEGUIR

   distancia = 10
   LLINDAR_OBSTACLE_CM = 15

   if estat == SEGUIR:
       if distancia is not None and distancia < LLINDAR_OBSTACLE_CM:
           estat = ESQUIVAR

   print(NOMS_ESTAT[estat])
   ```

   - a) `SEGUIR`
   - b) `ESQUIVAR`
   - c) `RECUPERAR`
   - d) Error, perquè `estat` no es pot reassignar.

7. Segons el marc conceptual mínim d'aquesta SA, què distingeix una **regla feta a mà** (com `mpu_orientacio()`) d'un model d'**aprenentatge automàtic**?
   - a) No hi ha cap diferència real, són el mateix concepte amb noms diferents.
   - b) La regla la decideix la persona que programa (un llindar fix); el model **s'entrena** amb exemples (dades) i en dedueix ell mateix la decisió.
   - c) Un model d'IA mai fa servir dades, només regles.
   - d) La regla feta a mà sempre és més precisa que qualsevol model d'IA.

8. Què vol dir que un classificador entrenat amb dades **parcials** té **biaix**?
   - a) Que el codi té un error de sintaxi.
   - b) Que les seves decisions seran esbiaixades cap a les condicions de les dades amb què es va entrenar, i pot fallar amb condicions diferents.
   - c) Que el model és més lent que una regla feta a mà.
   - d) Que el model no es pot fer servir mai més.

9. Per què cal tenir cura amb la **privadesa** en recollir telemetria, encara que sembli "només dades d'un robot"?
   - a) No cal, la telemetria d'un robot mai té a veure amb persones.
   - b) Perquè la telemetria pot incloure dades associades a una persona concreta (per exemple, on i quan s'ha fet una prova), i cal privadesa, consentiment i finalitat clara en recollir-la.
   - c) Perquè el mòdul `log` esborra les dades automàticament si detecta un problema de privadesa.
   - d) Perquè la ràdio de la micro:bit xifra sempre les dades.

10. Per què el simulador de python.microbit.org **sí** és útil per a la part de protocol d'aquesta SA, però **no** per als sensors del Kit 3?
    - a) Perquè no simula res en absolut d'aquesta SA.
    - b) Perquè simula la ràdio i el mòdul `log` (es poden assajar dos "instàncies" del simulador enviant-se missatges), però no simula el DHT11 ni l'IMU MPU6050, que necessiten maquinari real.
    - c) Perquè el simulador només funciona amb el mòdul `radio`, mai amb `log`.
    - d) Perquè cal comprar una llicència per simular sensors.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, per què `llegeix_dht11()` d'aquesta SA i `mesura_distancia()` de la SA7 es consideren "el mateix mecanisme" pel que fa a la manera de mesurar, encara que llegeixin sensors diferents.

___________________________________________________________________

___________________________________________________________________

---

## Clau de correcció (docent)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| a | b | a | b | a | b | b | b | b | b |

La pregunta 1 (COMPLETAR) substitueix el record memorístic de "com es connecta l'IMU per I2C" per la necessitat de completar la línia que el desperta (`i2c.write(MPU_ADR, bytes([MPU_REG_PWR, 0x00]))`), aplicant directament el patró d'inicialització de `mpu_inicia()`.

La pregunta 3 (CORREGIR) substitueix la definició memorística del mecanisme de lectura del DHT11 per l'error freqüent documentat a la guia docent ("el DHT11 retorna sempre `None` perquè es llegeix massa sovint"): l'alumnat ha de localitzar-lo en codi, no repetir-ne la definició.

La pregunta 6 (TRAÇA) substitueix la pregunta de pur record ("quants estats alhora") per haver de llegir un fragment real de la FSM i predir quin és l'estat final, reforçant que `estat` és una variable de decisió pròpia (no una lectura de sensor) i que només en pren un valor cada volta.

La pregunta 11 és oberta: valora que expliqui que totes dues funcions fan servir `machine.time_pulse_us` per mesurar **quant de temps** dura un senyal digital (un pols) i que, a partir d'aquesta durada, en dedueixen una magnitud (distància o bit de dades): el mecanisme de mesura és el mateix, encara que el que se'n dedueix i el nombre de polsos mesurats (1 a l'HC-SR04, 40 al DHT11) sigui diferent.

---

*Qüestionari de conceptes de la SA8. Es recolza en `SA8_fitxa_alumnat.md`, `SA8_esquemes_connexions.md`,
`00_IA_a_la_materia.md` i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
