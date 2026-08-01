# SA2 · Qüestionari de conceptes (sortides digitals, PWM i actuadors)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega — i torna-hi com a **repàs** abans de la prova del 1r trimestre (a la sessió de tancament de la SA3).

> **Ús.** Comprovació breu dels conceptes clau de la SA2: sortides digitals vs PWM,
> LED/LED RGB, so amb `music`, relé i seguretat elèctrica bàsica.
> Es pot fer servir com a **repàs formatiu** o com a **prova curta qualificable**
> (10 preguntes × 1 punt = **nota 0-10**). Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. Quina instrucció fa parpellejar un LED extern connectat al pin P1?
   - a) `pin1.read_digital()`
   - b) `pin1.write_digital(1)` i `pin1.write_digital(0)` alternats
   - c) `display.show(Image.HEART)`
   - d) `music.play(['C4:4'])`

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

6. Un **acumulador** en programació (com `comptador = comptador + 1`) serveix per…
   - a) Esborrar una variable.
   - b) Anar sumant/actualitzant un valor a partir del seu valor anterior, cada volta d'un bucle.
   - c) Definir una funció.
   - d) Llegir un sensor.

7. Per què s'inicialitza un acumulador **abans** del `while True:` i no a dins?
   - a) És igual, no importa on.
   - b) Perquè dins del bucle es tornaria a posar a zero cada volta i mai avançaria.
   - c) Perquè Python no ho permet dins d'un bucle.
   - d) Perquè els acumuladors només funcionen amb `for`.

8. Un **relé** connectat a la micro:bit serveix per…
   - a) Amplificar el so de l'altaveu.
   - b) Llegir un senyal analògic.
   - c) Commutar (obrir/tancar), amb un senyal de baixa tensió, un circuit extern que porta la seva pròpia alimentació.
   - d) Carregar la bateria de la placa.

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
| b | c | c | b | b | b | b | c | b | b |

La pregunta 11 és oberta: valora que la diferència digital/PWM sigui correcta (dos estats vs valors intermedis) i que els dos exemples siguin coherents amb components reals de la SA2 (per exemple, LED verd/ambre/vermell = digital; respiració o intensitat = PWM).

---

*Qüestionari de conceptes de la SA2. Es recolza en `SA2_fitxa_alumnat.md`, `SA2_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
