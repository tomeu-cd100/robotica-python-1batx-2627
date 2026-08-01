# Simulador oficial de micro:bit (python.microbit.org)

> **Per a qui és?** Docent i alumnat. Detall exacte de **què simula i què
> NO simula** l'editor oficial de MicroPython (<https://python.microbit.org>),
> com fer-lo servir a cada SA i quins són els seus límits. Complementa
> `Classes/00_General/00_Entorns_de_treball.md` §2 (el simulador com a pla
> B), aquí amb la llista exhaustiva.

## 1. Què simula (amb fidelitat suficient per programar-hi)

| Component | Es simula? | Detall |
|---|---|---|
| Matriu de 5×5 LED (`display`) | ✅ Sí | `show()`, `scroll()`, `set_pixel()`/`get_pixel()`, `clear()`: es veuen al canvas del navegador. |
| Botons A i B (`button_a`/`button_b`) | ✅ Sí | Es fa clic amb el ratolí (o es prem la tecla `A`/`B` del teclat en alguns navegadors). |
| Acceleròmetre (`accelerometer`) | ✅ Sí (parcial) | Es pot arrossegar la placa virtual per generar gestos com `"shake"`; els valors bruts (`get_x/y/z`) són aproximats, no una física real. |
| Ràdio (`radio`) | ✅ Sí, entre pestanyes | Dues pestanyes del navegador amb dos programes simulats es poden "parlar" per ràdio (útil per a SA5/SA8 sense dues plaques físiques). |
| REPL / consola | ✅ Sí | Consola interactiva per provar ordres línia a línia i llegir `print()`, igual que amb la placa real connectada. |
| `log` (registre de dades) | ✅ Sí (bàsic) | `log.add()` funciona i es pot inspeccionar, però **no genera el fitxer `MY_DATA.HTM`** real que es descarrega d'una placa física. |
| Sensor de llum intern (`display.read_light_level()`) | ⚠️ Parcial | Retorna un valor, però no hi ha llum ambiental real: cal moure un control simulat, no reflecteix la il·luminació de l'aula. |
| Micròfon intern (`microphone.sound_level()`) | ⚠️ Parcial | Disponible a versions recents de l'editor; no reprodueix el soroll real de l'aula. |
| Temperatura interna (`temperature()`) | ⚠️ Parcial | Retorna un valor fix o ajustable manualment, no la temperatura física del xip. |

## 2. Què NO simula (cal maquinari real per validar-ho)

- **Micro:shield i pins externs:** `pinN.read_digital()/write_digital()/
  read_analog()/write_analog()` **no tenen cap component connectat** al
  simulador. El codi s'executa sense error, però no hi ha cap resposta
  visible ni real.
- **Sensors del Kit 1-3** (polsador extern, LED extern, PIR, sensor de so,
  DHT11, HC-SR04, seguidor de línia KS0050, relé, IMU MPU6050, BMP280,
  CCS811): **cap d'ells es simula**. Es pot escriure i provar la
  **lògica** (llegir → comparar amb llindar → decidir), però els valors
  concrets són inventats pel programador, no mesures reals.
- **Motoreductors i servos:** `pinN.write_analog()` no mou res al
  simulador; no hi ha física de moviment, fricció ni consum de bateria.
- **Alimentació externa (portapiles):** el simulador no distingeix entre
  alimentar per USB o per portapiles; l'avís d'«alimenta els motors des
  del portapiles, mai per USB» només es pot comprovar amb la placa real.
- **Soroll de mesura real:** els llindars que "funcionen" al simulador
  (sons, llum, temperatura) **s'han de recalibrar sempre** amb el
  maquinari físic; el simulador no reprodueix la variabilitat real d'un
  sensor barat.

## 3. Ús recomanat per SA (SA1-SA9)

| SA | Ús principal del simulador | Límit a tenir present |
|---|---|---|
| SA1 | Primer contacte amb l'editor i el simulador; primer programa (`display`, botons). | Cap sensor extern encara: tot el maquinari d'aquesta SA (matriu, botons) **ja es simula bé**. |
| SA2 | Provar animacions de sortides digitals/PWM i melodies abans (o en lloc) de cablejar el LED/brunzidor extern. | El LED/RGB/brunzidor **externs** del Kit 1 no es veuen: cal maquinari real per al repte final de la SA. |
| SA3 | Provar la lògica `if/elif` sobre `button_a.is_pressed()` i sobre valors de sensor **inventats** (variables). | Cap sensor del Kit 2-3 (PIR, so, ultrasons, DHT11) es simula: el disseny de la reacció es prova, no la lectura real. |
| SA4 | Provar una funció pròpia amb paràmetres i diversos valors de crida; esbós de `avancar()/girar()` sense moviment real. | Servo i motoreductor no es mouen al simulador; cal el vehicle muntat per validar-ho físicament. |
| SA5 | **Ús fort:** protocol de ràdio complet, emissor i receptor, entre dues pestanyes del navegador — sense necessitat de dues plaques. | Cap moviment real del vehicle: la ràdio es valida, el moviment no. |
| SA6 | Esbossar i provar la màquina d'estats (RUN/STOP/ALERTA) en codi mínim; provar `log.add()`. | STOP prioritari sobre motors reals no es pot verificar sense maquinari; el `log` no genera el fitxer real. |
| SA7 | Pseudocodi/lògica de trajectòries (quadrat, gir en "L") sense maquinari. | Seguidor de línia i HC-SR04 no es simulen: cap valor de sensor és real. |
| SA8 | Protocol de telemetria (`radio.send`/`receive`) entre estació base i "rover" simulats. | Els sensors I2C (IMU, BMP280, CCS811, DHT11) no es simulen: els valors enviats són inventats pel programador per provar el format. |
| SA9 | Pla B puntual per repassar lògica del repte lliure sense maquinari (vegeu `00_Mode_supervivencia.md`). | El repte final normalment necessita el rover complet: el simulador només ajuda a la fase de disseny/lògica. |

## 4. Com fer-lo servir (recordatori ràpid)

1. Ves a <https://python.microbit.org>, cap instal·lació ni compte.
2. Escriu o enganxa el codi a l'editor; botó **▶ Simula** obre el panell
   amb la placa virtual.
3. Interactua amb els botons/gestos simulats i llegeix la consola/REPL
   per depurar.
4. Quan calgui maquinari real (la majoria de reptes a partir de SA3), passa
   a la placa física seguint `Classes/00_General/00_Entorns_de_treball.md`
   §4 (transferència del programa).

---

⬅️ Torna a [`Index_simulacions.md`](Index_simulacions.md).
