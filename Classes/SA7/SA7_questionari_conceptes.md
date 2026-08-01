# SA7 · Qüestionari de conceptes (cinemàtica diferencial, llindars, time-of-flight, missions)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega.

> **Ús.** Comprovació breu dels conceptes clau de la SA7: cinemàtica diferencial, calibratge de motors, llindar de detecció, mesura de distància per temps de vol, i integració de comportaments en missions.
> Es pot fer servir com a **repàs formatiu** o com a **prova curta qualificable**
> (10 preguntes × 1 punt = **nota 0-10**). Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. **[TRAÇA]** Fixa't en aquest fragment, adaptat de `missio_quadrat()` (`rover_missions.py`):

   ```python
   for _ in range(4):
       avancar(400)
       sleep(900)
       girar('dreta')
       sleep(430)
   aturar()
   ```

   Què fa aquest fragment de codi?
   - a) El rover gira sobre si mateix indefinidament, sense avançar mai.
   - b) El rover recorre una trajectòria aproximadament en quadrat: repeteix 4 vegades avançar una estona i girar uns 430 ms (aprox. 90°).
   - c) El rover segueix una línia negra combinant els dos sensors del rover.
   - d) El rover mesura la distància a un obstacle abans de cada gir.

2. Per què cal **calibrar** els motors (`FACTOR_M1`/`FACTOR_M2`) encara que els dos motoreductors siguin del mateix model?
   - a) Perquè MicroPython ho exigeix per llei del llenguatge.
   - b) Perquè cap parell de motoreductors surt idèntic de fàbrica: petites diferències fan que el rover es desviï si reben exactament la mateixa consigna de PWM.
   - c) No cal mai calibrar-los si el codi és correcte.
   - d) Perquè els dos motors comparteixen el mateix pin.

3. El seguidor de línia KS0050 es llegeix amb `read_analog()`. Per què el `LLINDAR_LINIA` **no** és el mateix a tota la classe?
   - a) Perquè cada micro:bit té un `read_analog()` diferent.
   - b) Perquè el valor llegit depèn de la il·luminació real de cada punt de l'aula i de cada circuit concret: cal calibrar-lo sobre el propi circuit.
   - c) Perquè el KS0050 és analògic i mai dona el mateix valor dues vegades.
   - d) No hi ha cap motiu, es podria fixar un únic valor vàlid per a tothom.

4. **[COMPLETAR]** Aquest fragment és una versió incompleta de `mesura_distancia()` (d'`evita_obstacles.py`). Hi falta **una línia** (marcada amb `____`):

   ```python
   def mesura_distancia():
       TRIGGER.write_digital(0)
       utime.sleep_us(2)
       TRIGGER.write_digital(1)
       utime.sleep_us(10)
       ____  # <-- que hi va aqui?
       try:
           durada_us = machine.time_pulse_us(ECHO, 1, 30000)
       except OSError:
           return None
       if durada_us < 0:
           return None
       return (durada_us * VELOCITAT_SO_CM_US) / 2
   ```

   Quina línia cal perquè el pols de trigger duri només 10 microsegons i després es talli, tal com demana l'HC-SR04?
   - a) `ECHO.write_digital(0)`
   - b) `sleep(10)`
   - c) `TRIGGER.write_digital(0)`
   - d) `TRIGGER.write_digital(1)`

5. A `evita_obstacles.py`, per què `TRIGGER = pin1` i `ECHO = pin2`, i no `pin14`/`pin15` com a la pràctica `alarma_ultrasons.py` de la SA3?
   - a) Perquè el mètode de mesura ha canviat completament respecte a la SA3.
   - b) Perquè al rover, P14/P15 ja estan ocupats pels motoreductors (fixats des de la SA4); el mètode de mesura és exactament el mateix, només canvien els pins.
   - c) Perquè P1/P2 són els únics pins digitals de la placa.
   - d) No hi ha cap motiu tècnic, és arbitrari.

6. Quantes coses pot valer, alhora, la variable de missió a `rover_missions.py`?
   - a) Tantes com calgui, es poden combinar diverses missions a la vegada.
   - b) Sempre dues, com a mínim.
   - c) Una sola, en cada instant (igual que la variable d'estat d'una FSM, vist a la SA6).
   - d) Cap: `rover_missions.py` no fa servir cap variable de missió.

7. Per què el polsador STOP de `rover_missions.py` es comprova dins del bucle **intern** de cada missió, i no només al bucle principal?
   - a) Perquè `read_digital()` només funciona un cop per programa.
   - b) Perquè si una missió té el seu propi bucle llarg (per exemple, `missio_paret`), i el STOP només es comprovés al bucle principal, hi hauria una finestra de temps en què el rover "ignoraria" l'aturada mentre executa la missió.
   - c) No hi ha cap motiu, es podria comprovar en qualsevol lloc.
   - d) Perquè el polsador només funciona dins de funcions, no al bucle principal.

8. Quina funció de moviment de la SA4 **NO** reutilitza el rover d'aquesta SA?
   - a) `avancar()`.
   - b) `girar()`.
   - c) `aturar()`.
   - d) Totes es reutilitzen: cap funció de moviment és nova a la SA7.

9. En un seguidor de línia amb **un únic** sensor, com decideix el rover cap a quin costat corregir quan perd la línia?
   - a) No pot decidir-ho mai amb un sol sensor, cal sempre HC-SR04 addicional.
   - b) Amb una estratègia de cerca fixa (per exemple, girar sempre cap a l'esquerra), perquè un sol sensor no permet saber cap a quin costat s'ha desviat de veritat.
   - c) Llegint directament el valor de `girar()`.
   - d) El rover s'atura sempre que perd la línia, mai gira.

10. **[CORREGIR]** Aquest fragment (adaptat de `mesura_distancia()` d'`evita_obstacles.py`) té **un error**. Troba'l:

    ```python
    def mesura_distancia():
        TRIGGER.write_digital(0)
        utime.sleep_us(2)
        TRIGGER.write_digital(1)
        utime.sleep_us(10)
        TRIGGER.write_digital(0)
        try:
            durada_us = machine.time_pulse_us(ECHO, 1, 30000)
        except:
            return None
        if durada_us < 0:
            return None
        return (durada_us * VELOCITAT_SO_CM_US) / 2
    ```

    - a) El `except:` sense especificar `OSError` atraparia qualsevol error (fins i tot un error real de programació), en lloc de només el timeout del sensor.
    - b) Falta el `try` abans del `except`.
    - c) `machine.time_pulse_us` no accepta tres arguments.
    - d) `TRIGGER.write_digital(0)` no es pot cridar dues vegades al mateix programa.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, per què `mesura_distancia()` d'aquesta SA i `distancia_cm()` de `alarma_ultrasons.py` (SA3) es consideren "el mateix codi" pel que fa al mètode, encara que estiguin en programes diferents amb pins diferents.

___________________________________________________________________

___________________________________________________________________

---

## Clau de correcció (docent)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | b | b | c | b | c | b | d | b | a |

La pregunta 1 (traça de codi) avalua que l'alumnat sàpiga llegir un fragment real de `missio_quadrat()` i predir el comportament resultant (una trajectòria en quadrat), en lloc de limitar-se a recitar la definició de cinemàtica diferencial.

La pregunta 4 (completar codi) avalua que l'alumnat entengui la seqüència exacta del pols de trigger de l'HC-SR04 (0 → 1 → 0) prou bé com per identificar quina línia hi falta, no només que en sàpiga la definició de manual.

La pregunta 10 (corregir codi) avalua que l'alumnat reconegui un error real i freqüent (un `except:` massa genèric que amaga bugs de programació, en lloc de capturar només el timeout amb `except OSError:`), tal com es descriu a la guia docent de la S3.

La pregunta 11 és oberta: valora que expliqui que el mètode de mesura (pols de trigger + `machine.time_pulse_us` a l'echo + càlcul distància = temps × velocitat del so / 2) és **idèntic** als dos programes; només canvien els pins concrets (P14/P15 a la SA3, P1/P2 al rover), perquè al rover aquests dos pins vells ja estan ocupats pels motoreductors.

---

*Qüestionari de conceptes de la SA7. Es recolza en `SA7_fitxa_alumnat.md`, `SA7_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
