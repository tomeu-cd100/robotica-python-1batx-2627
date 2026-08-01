# SA6 · Qüestionari de conceptes (llaç obert/tancat, FSM, histèresi, STOP prioritari)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega.

> **Ús.** Comprovació breu dels conceptes clau de la SA6: llaç obert vs llaç tancat, màquina d'estats finits (variable d'estat + transicions), histèresi, i aturada d'emergència prioritària.
> Es pot fer servir com a **repàs formatiu** o com a **prova curta qualificable**
> (10 preguntes × 1 punt = **nota 0-10**). Durada orientativa: **15-20 min**, individual, sense apunts.

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

8. On desa les dades el mòdul `log` de la micro:bit V2?
   - a) A un servidor al núvol.
   - b) A la memòria flash interna de la pròpia placa; es llegeixen després per USB.
   - c) Només a la RAM, es perden en apagar la placa.
   - d) En un fitxer al núvol de Microsoft.

9. Quin fitxer apareix a la unitat MICROBIT quan connectes per USB una placa que ha registrat dades amb `log.add()`?
   - a) `LOG.TXT`.
   - b) `DATA.CSV`.
   - c) `MY_DATA.HTM`.
   - d) Cap, cal un programa extra per veure les dades.

10. Per què el simulador de python.microbit.org **no** és suficient per validar del tot `vehicle_seguretat.py`?
    - a) Perquè no simula `temperature()`.
    - b) Perquè no simula els motors ni el relé, encara que sí simuli la lògica de la màquina d'estats i de la ràdio.
    - c) Perquè no permet escriure codi amb `radio`.
    - d) És suficient del tot, no cal cap vehicle físic.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, per què l'STOP d'aquesta SA es diu "prioritari" i no simplement "una comanda més" del protocol de ràdio. Quin problema de seguretat evita aquest disseny?

___________________________________________________________________

___________________________________________________________________

---

## Clau de correcció (docent)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | c | b | b | b | b | b | b | c | b |

La pregunta 11 és oberta: valora que expliqui que l'STOP s'ha de comprovar **abans que res** a cada volta del bucle i que **totes** les vies (polsador i ràdio) criden la mateixa funció, de manera que mai hi ha un moment en què el vehicle pugui "ignorar" una ordre d'aturada perquè estava processant-ne una altra.

---

*Qüestionari de conceptes de la SA6. Es recolza en `SA6_fitxa_alumnat.md`, `SA6_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
