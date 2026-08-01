# SA2 · Qüestionari de conceptes (sortides digitals, PWM i actuadors)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega — i torna-hi com a **repàs** abans de la prova del 1r trimestre (a la sessió de tancament de la SA3).

> **Ús.** Comprovació breu dels conceptes clau de la SA2: sortides digitals vs PWM,
> LED/LED RGB, so amb `music`, relé i seguretat elèctrica bàsica.
> **Repàs formatiu (autocorregible); es fa com a deures en acabar la SA.** No qualifica mai
> (vegeu `../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md` §6.2): 10
> preguntes per autocorregir-te. Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. **[TRAÇA]** Quina és la sortida d'aquest programa?

   ```python
   from microbit import *

   comptador = 0

   while True:
       pin1.write_digital(1)
       sleep(300)
       pin1.write_digital(0)
       sleep(300)
       comptador = comptador + 1
       if comptador % 5 == 0:
           display.scroll(str(comptador))
   ```

   - a) Puja i baixa la intensitat del LED de P1 amb PWM (efecte de respiració).
   - b) Fa parpellejar el LED de P1 (300 ms encès, 300 ms apagat) i mostra el comptador de parpellejos al display cada 5 vegades.
   - c) Reprodueix una melodia pel brunzidor connectat a P1.
   - d) Encén el LED de P1 de manera fixa i no l'apaga mai.

2. Una sortida **PWM** (`write_analog`) es diferencia d'una **digital** (`write_digital`) perquè…
   - a) Fa servir més corrent.
   - b) Només serveix per al so.
   - c) Permet valors intermedis (0-1023), no només encès/apagat.
   - d) No es pot fer servir amb LED.

3. Quin és el rang de valors vàlids per a `pinN.write_analog(...)`?
   - a) 0 a 1
   - b) 0 a 255
   - c) 0 a 1023
   - d) -1023 a 1023

4. Per barrejar colors amb un **LED RGB** (tres pins independents), cal…
   - a) Escriure només al pin vermell.
   - b) Escriure `write_analog` als tres canals (R, G, B) amb intensitats diferents.
   - c) Fer servir només `write_digital`.
   - d) Connectar els tres pins junts a un de sol.

5. Què fa `music.play(['C4:4', 'E4:4'], pin=pin2)`?
   - a) Encén el LED del pin 2.
   - b) Reprodueix una melodia de dues notes pel brunzidor connectat a P2.
   - c) Llegeix el volum del micròfon.
   - d) Fa parpellejar la matriu de LED.

6. **[CORREGIR]** Aquest programa hauria de comptar parpellejos i mostrar-ne el total cada volta, però sempre mostra `1`. On és l'error?

   ```python
   from microbit import *

   while True:
       comptador = 0
       pin1.write_digital(1)
       sleep(500)
       pin1.write_digital(0)
       sleep(500)
       comptador = comptador + 1
       display.scroll(str(comptador))
   ```

   - a) `comptador = 0` hauria d'anar **abans** del `while True:`, no dins.
   - b) Falta un `pin1.write_digital(0)` per apagar el LED.
   - c) `sleep(500)` hauria de ser `sleep(0.5)`.
   - d) `display.scroll()` no pot mostrar nombres, cal `display.show()`.

7. Per què s'inicialitza un acumulador **abans** del `while True:` i no a dins?
   - a) És igual, no importa on.
   - b) Perquè dins del bucle es tornaria a posar a zero cada volta i mai avançaria.
   - c) Perquè Python no ho permet dins d'un bucle.
   - d) Perquè els acumuladors només funcionen amb `for`.

8. **[COMPLETAR]** Aquest fragment ha de commutar el relé del pin P13 per encendre un llum extern quan es prem el botó A, i tornar-lo a apagar 3 segons després. Quina línia falta?

   ```python
   from microbit import *

   while True:
       if button_a.is_pressed():
           pin13.write_digital(1)   # tanca el rele: engega el llum extern
           sleep(3000)
           ____                     # <-- quina linia hi va aqui?
       sleep(100)
   ```

   - a) `pin13.write_digital(0)`
   - b) `pin13.write_analog(0)`
   - c) `pin13.write_digital(1)`
   - d) `sleep(0)`

9. Per seguretat, el costat del **circuit extern** d'un relé…
   - a) Es pot connectar directament a un pin de la micro:bit.
   - b) Mai s'ha de tocar mentre hi ha tensió, i no es connecta mai directament a la placa.
   - c) No cal cap precaució especial.
   - d) Ha d'anar sempre connectat a l'USB.

10. Per què és millor posar els temps (`TEMPS_VERD`, `TEMPS_AMBRE`...) del semàfor en **variables al principi** del programa?
    - a) No hi ha cap diferència amb escriure'ls directament a cada `sleep()`.
    - b) Per canviar la durada d'una fase només cal canviar **un** número, en un sol lloc.
    - c) Perquè `sleep()` no admet nombres.
    - d) Per fer el programa més llarg.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, la diferència entre una sortida **digital** i una **PWM**, i
    posa un exemple d'ús de cadascuna en el teu repte «semàfor o llum d'ambient».

___________________________________________________________________

___________________________________________________________________

---

## Clau de correcció (docent)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | c | c | b | b | a | b | a | b | b |

La pregunta 1 (TRAÇA) substitueix una pregunta de pur record de la instrucció; ara cal llegir un bucle real amb `write_digital` i un acumulador i predir què mostra, no només recordar el nom de la funció.

La pregunta 6 (CORREGIR) substitueix la definició memorística d'"acumulador" per l'error freqüent documentat a la guia docent ("el comptador no avança perquè s'inicialitza dins del bucle"): l'alumnat ha de localitzar-lo en codi, no repetir-ne la definició.

La pregunta 8 (COMPLETAR) substitueix la definició memorística de "relé" per la necessitat de completar la línia que el torna a obrir (`write_digital(0)`), aplicant directament el patró tanca/obre del repte «semàfor o llum d'ambient».

La pregunta 11 és oberta: valora que la diferència digital/PWM sigui correcta (dos estats vs valors intermedis) i que els dos exemples siguin coherents amb components reals de la SA2 (per exemple, LED verd/ambre/vermell = digital; respiració o intensitat = PWM).

---

*Qüestionari de conceptes de la SA2. Es recolza en `SA2_fitxa_alumnat.md`, `SA2_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
