# SA6 · Qüestionari de conceptes (llaç obert/tancat, FSM, histèresi, STOP prioritari)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega.

> **Ús.** Comprovació breu dels conceptes clau de la SA6: llaç obert vs llaç tancat, màquina d'estats finits (variable d'estat + transicions), histèresi, i aturada d'emergència prioritària.
> **Repàs formatiu (autocorregible); es fa com a deures en acabar la SA.** No qualifica mai
> (vegeu `../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md` §6.2): 10
> preguntes per autocorregir-te. Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. Quina diferència hi ha entre un sistema de **llaç obert** i un de **llaç tancat**?
   - a) Cap, són exactament el mateix.
   - b) El de llaç tancat llegeix un sensor (realimentació) i ajusta l'acció; el de llaç obert executa una acció fixa sense comprovar res.
   - c) El de llaç obert sempre és més ràpid.
   - d) El de llaç tancat no necessita cap actuador.

2. En una **màquina d'estats finits (FSM)**, quantes coses pot valer alhora la variable d'estat?
   - a) Tantes com calgui, poden combinar-se.
   - b) Sempre dues, com a mínim.
   - c) Una sola, en cada instant.
   - d) Cap: la FSM no fa servir cap variable.

3. Per què un termòstat amb un **sol llindar** (per exemple, `if temp < 25`) pot fer "clic-clic" sense parar?
   - a) Perquè el relé està espatllat de fàbrica.
   - b) Perquè una lectura real balla uns dècims al voltant del llindar i el sistema canvia d'estat cada vegada que hi passa per sobre o per sota.
   - c) Perquè `temperature()` no funciona bé a la micro:bit.
   - d) No té cap motiu tècnic, és un error del programador sempre.

4. Què és la **histèresi**, tal com s'ha vist en aquesta SA?
   - a) Un altre nom per al control proporcional.
   - b) Fer servir dos llindars (baix i alt) perquè l'estat només canviï quan la lectura els travessa de veritat, no quan hi ronda a prop.
   - c) Una manera de fer el programa més lent expressament.
   - d) Una funció pròpia del mòdul `radio`.

5. A `vehicle_seguretat.py`, per què el **polsador** es comprova al **principi** de cada volta del bucle, abans de mirar la ràdio?
   - a) Perquè `read_digital()` només funciona a l'inici del programa.
   - b) Perquè si es comprovés després, hi hauria una finestra de temps en què el vehicle podria "ignorar" el polsador i seguir movent-se.
   - c) No hi ha cap motiu, es podria posar en qualsevol ordre.
   - d) Perquè la ràdio és més lenta que el polsador.

6. Quina prioritat té la comanda de ràdio `"X"` respecte a qualsevol altra ordre (F/B/L/R/S)?
   - a) Cap, es processa igual que les altres.
   - b) Prioritat màxima: interromp qualsevol moviment en curs, igual que el polsador físic.
   - c) Només funciona si el vehicle està aturat.
   - d) `"X"` no existeix al protocol d'aquesta SA.

7. Per què `actualitza_estat()` és **l'únic** lloc del programa que canvia la variable `estat`?
   - a) Perquè MicroPython ho exigeix per llei del llenguatge.
   - b) Perquè així es garanteix que tot el que ha de passar en canviar d'estat (aturar motors, mostrar-ho, actualitzar el LED) es fa sempre, sense que cap altra part del codi ho pugui "oblidar".
   - c) No hi ha cap motiu especial, és només estil.
   - d) Perquè `estat` és una constant, no es pot canviar enlloc més.

8. **[TRAÇA]** Quin és el valor de `estat` que imprimeix aquest codi?
   ```python
   estat = "FRED"
   temp = 23

   if estat == "FRED" and temp > 26:
       estat = "CALENT"
   elif estat == "CALENT" and temp < 24:
       estat = "FRED"

   print(estat)
   ```
   - a) `CALENT`
   - b) `FRED`
   - c) Dona error perquè `estat` no és una variable global.
   - d) No imprimeix res perquè manca un `else`.

9. **[COMPLETAR]** Aquesta funció ha de canviar la variable `estat` "de debò" (que el canvi es vegi també fora de la funció). Tal com està escrit ara (sense la línia que falta), el `print(estat)` final mostra `STOP`, no `RUN`. Quina línia falta on diu el comentari?
   ```python
   estat = "STOP"

   def actualitza_estat(nou):
       # <-- quina linia falta aqui?
       estat = nou

   actualitza_estat("RUN")
   print(estat)
   ```
   - a) `global estat`
   - b) `estat = "STOP"`
   - c) `return estat`
   - d) `import estat`

10. **[CORREGIR]** Aquest fragment de `vehicle_seguretat.py` no respecta la convenció de seguretat de la SA per a la comanda STOP. Quin és el problema?
    ```python
    while True:
        missatge = radio.receive()
        if missatge is not None and missatge.startswith(PREFIX):
            ordre = missatge[len(PREFIX):]
            if ordre == "S":
                actualitza_estat(STOP)

        if not POLSADOR_STOP.read_digital():
            actualitza_estat(STOP)

        sleep(20)
    ```
    - a) El polsador es comprova DESPRÉS de processar la ràdio, no al principi del bucle: encara que amb aquest codi concret el polsador es llegeix igualment a cada volta, no seguir la convenció de "STOP sempre primer" és una mala pràctica de seguretat que deixa el disseny fràgil davant de futurs canvis al bloc de la ràdio.
    - b) Falta un `import radio` al principi del programa.
    - c) `sleep(20)` fa que el programa vagi massa ràpid.
    - d) `read_digital()` no es pot fer servir amb un polsador, només amb un sensor.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, per què l'STOP d'aquesta SA es diu "prioritari" i no simplement "una comanda més" del protocol de ràdio. Quin problema de seguretat evita aquest disseny?

___________________________________________________________________

___________________________________________________________________

---

> 🔑 **La correcció.** La clau és **material del docent** (`Classes/Solucionari/Questionaris_conceptes_solucions.md`): així el qüestionari serveix de debò per comprovar què saps. Si el fas amb el **Google Form** del Classroom, la correcció te la dona el formulari mateix en enviar-lo; si el fas en paper, demana-la al docent en acabar.

---

*Qüestionari de conceptes de la SA6. Es recolza en `SA6_fitxa_alumnat.md`, `SA6_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
