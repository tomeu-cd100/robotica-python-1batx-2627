# SA1 · Qüestionari de conceptes (què és un robot i la placa micro:bit)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega — i torna-hi com a **repàs** abans de la prova del 1r trimestre (a la sessió de tancament de la SA3).

> **Ús.** Comprovació breu dels conceptes clau de la SA1: robot, sistema embegut,
> model entrada-procés-sortida, anatomia de la micro:bit V2 i mètode de projecte.
> **Repàs formatiu (autocorregible); es fa com a deures en acabar la SA.** No qualifica mai
> (vegeu `../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md` §6.2): 10
> preguntes per autocorregir-te. Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. Observa aquest programa de micro:bit i respon: **què mostra?**

   ```python
   from microbit import *

   while True:
       if button_a.is_pressed():
           display.show(Image.HAPPY)
       else:
           display.show(Image.SAD)
       sleep(200)
   ```
   - a) Sempre mostra la cara SAD; no reacciona mai als botons.
   - b) Mentre es prem el botó A mostra la cara HAPPY; si no es prem, mostra la cara SAD, i ho repeteix contínuament.
   - c) Mostra la cara HAPPY una sola vegada i després el programa s'atura.
   - d) Alterna HAPPY i SAD cada 200 ms sense tenir en compte el botó.

2. En el model **entrada → procés → sortida**, un **sensor** correspon a…
   - a) La sortida (la placa actua).
   - b) El procés (la placa decideix).
   - c) L'entrada (la placa percep l'entorn).
   - d) L'alimentació de la placa.

3. Aquest programa hauria de mostrar el nom **"ALEX"** desplaçant-se i, en acabar, deixar fixa una cara contenta a la pantalla. Falta una línia:

   ```python
   from microbit import *

   display.scroll("ALEX")
   # <-- que hi va aqui?
   ```
   Quina línia cal afegir on diu el comentari?
   - a) `display.show(Image.HAPPY)`
   - b) `sleep(1000)`
   - c) `display.scroll(Image.HAPPY)`
   - d) `button_a.is_pressed()`

4. Quin d'aquests elements és un **actuador** (sortida)?
   - a) Un sensor de temperatura.
   - b) La matriu de LED d'una micro:bit, quan mostra una imatge.
   - c) Un botó polsador.
   - d) Un sensor de llum.

5. Dins la placa micro:bit, quina part fa de **"cervell"** i executa el programa (el procés)?
   - a) El microcontrolador.
   - b) El connector USB.
   - c) La pila.
   - d) El botó de reinici.

6. Quina és la diferència entre un senyal **digital** i un d'**analògic**?
   - a) El digital és més car que l'analògic.
   - b) L'analògic només val per als motors.
   - c) El digital té dos estats (per exemple, un botó premut o no); l'analògic pren molts valors intermedis.
   - d) No hi ha cap diferència.

7. La instrucció que **sempre** cal a la primera línia d'un programa de micro:bit és…
   - a) `while True:`
   - b) `from microbit import *`
   - c) `display.show()`
   - d) `import random`

8. La matriu de **25 LED** de la micro:bit pot funcionar, a més de com a sortida, com a…
   - a) Entrada: sensor de llum.
   - b) Font d'alimentació.
   - c) Connector USB.
   - d) Res més, només és sortida.

9. Què fa `sleep(1000)` en un programa de micro:bit?
   - a) Apaga la placa.
   - b) Espera 1000 mil·lisegons (1 segon) abans de continuar.
   - c) Esborra el display.
   - d) Reinicia el programa.

10. Aquest programa hauria de comprovar **contínuament** el botó A i canviar la cara en conseqüència, però a la placa real només ho fa un instant en arrencar i es queda així. Quin és l'error?

    ```python
    from microbit import *

    if button_a.is_pressed():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
    ```
    - a) Falta `from microbit import *` a la primera línia.
    - b) Falta envoltar el codi amb un `while True:` que ho repeteixi contínuament.
    - c) `button_a.is_pressed()` hauria de ser `button_a.was_pressed()`.
    - d) Falta un `sleep()` abans de l'`if`.

---

## Pregunta oberta (opcional)

11. Tria un aparell que tinguis a casa (rentadora, robot aspirador, ascensor, caixer…) i
    analitza'l amb el model **entrada → procés → sortida**: digues quin **sensor** (entrada)
    fa servir, què **decideix** (procés) i quin **actuador** (sortida) mou.

___________________________________________________________________

___________________________________________________________________

---

## Clau de correcció (docent)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | c | a | b | a | c | b | a | b | b |

La pregunta 1 (traça) es corregeix perquè cal llegir el codi sencer (bucle, condicional i `sleep`) i deduir el comportament real, no recordar una definició de "robot".

La pregunta 3 (completar) es corregeix perquè demana identificar quina instrucció (`display.show`) produeix l'efecte descrit —una imatge fixa després del text—, en lloc de repetir de memòria la definició de "sistema embegut".

La pregunta 10 (corregir) es corregeix perquè reprodueix l'error freqüent real d'aquesta SA (falta el `while True:`, vegeu `SA1_guia_docent.md`, taula «Errors freqüents») i obliga a raonar sobre l'execució del codi, no a recitar les fases del mètode de projecte.

La pregunta 11 és oberta: valora que aparegui **un** sensor, **una** decisió i **un** actuador coherents amb l'aparell triat.

---

*Qüestionari de conceptes de la SA1. Es recolza en `SA1_fitxa_alumnat.md`, `SA1_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
