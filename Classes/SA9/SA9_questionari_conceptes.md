# SA9 · Qüestionari de conceptes (mètode de projecte, integració, documentació, ètica/ODS)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de la defensa oral i del checklist d'entrega.

> **Ús.** Comprovació breu dels conceptes clau de la SA9: mètode de projecte, integració de sistemes, dossier tècnic i defensa, i ètica de dades/ODS aplicats al propi repte. A diferència de les altres SA, aquestes preguntes **no versen sobre un sensor concret**: la SA9 integra tot el que ja saps.
> **Repàs formatiu (autocorregible); es fa com a deures en acabar la SA.** No qualifica mai
> (vegeu `../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md` §6.2): 10
> preguntes per autocorregir-te. Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. Segons el mètode de projecte del curs, quin és l'ordre correcte de les fases?
   - a) Provar → Idear → Prototipar → Millorar.
   - b) **Idear (analitzar/dissenyar) → Prototipar → Provar i millorar → Comunicar.**
   - c) Comunicar → Idear → Provar → Prototipar.
   - d) No hi ha un ordre: es pot començar per qualsevol fase.

2. Per què `plantilla_projecte.py` separa `percep()`, `decideix()` i `actua()` en tres funcions diferents?
   - a) **Perquè facilita la depuració: si el sistema falla, es pot aïllar si el problema és de lectura, de decisió o d'acció.**
   - b) Perquè MicroPython obliga a separar-les.
   - c) No hi ha cap motiu, és només estil.
   - d) Perquè `while True` no pot contenir més de dues crides a funcions.

3. Quina diferència hi ha entre provar el "cas normal" i fer una "prova de límit"?
   - a) Són el mateix, no hi ha diferència real.
   - b) **La prova de límit comprova què passa en condicions extremes o inesperades (sensor desconnectat, valor fora de rang), no només si el sistema funciona quan tot va bé.**
   - c) La prova de límit només serveix per a sistemes amb ràdio.
   - d) Una prova de límit sempre fa petar el programa a propòsit sense solució.

4. Per què el repte de reg automàtic connecta la bomba d'aigua a través d'un **relé**, i no directament al Micro:shield?
   - a) No cal el relé, és opcional per estètica.
   - b) Perquè el relé fa que la bomba vagi més ràpida.
   - c) **Perquè el relé commuta l'alimentació externa de la bomba de manera segura; el Micro:shield no pot alimentar-la directament.**
   - d) Perquè el relé substitueix el sensor d'humitat.

5. Observa aquest fragment del bucle principal d'un projecte de la SA9 (variant **no recomanada** de `plantilla_projecte.py`):
   ```python
   while True:
       if polsador_premut():
           display.show(Image.NO)
           continue
       humitat = HUMITAT.read_analog()
       if humitat < LLINDAR_SEC:
           RELE_BOMBA.write_digital(1)
       else:
           RELE_BOMBA.write_digital(0)
       sleep(20)
   ```
   Quin és el problema principal d'aquest codi, segons l'arquitectura del curs?
   - a) No hi ha cap problema real: separar-ho en `percep()`/`decideix()`/`actua()` és només estètica.
   - b) **Barreja lectura del sensor, decisió i acció sobre el relé, totes dins del `while True`, sense separar `percep()`/`decideix()`/`actua()`; si el sistema falla, costa més saber si el problema és de lectura, decisió o acció.**
   - c) El problema és que `humitat` s'hauria de llegir amb `read_digital()` en lloc de `read_analog()`.
   - d) El problema és que falta un `sleep(20)` al final del bucle.

6. Aquest fragment és la `decideix()` d'un repte de reg automàtic (Kit 3: sensor d'humitat + bomba amb relé). Quina línia falta perquè el sistema comenci a regar quan el terra estigui sec?
   ```python
   def decideix(dades):
       global estat
       if estat == ESPERA:
           if dades["humitat"] < LLINDAR_SEC:
               ____  # <-- que hi va aqui?
       elif estat == REGANT:
           if dades["humitat"] >= LLINDAR_SEC:
               actualitza_estat(ESPERA)
   ```
   - a) **`actualitza_estat(REGANT)`**
   - b) `RELE_BOMBA.write_digital(1)`
   - c) `estat = ESPERA`
   - d) `return REGANT`

7. Per què la Sessió 5 (prova pràctica T3) **no reavalua** el projecte de la SA9?
   - a) Perquè la S5 no compta per a la nota final.
   - b) **Perquè és un instrument separat que avalua destreses individuals de SA7-SA8; cap evidència no pot comptar dues vegades.**
   - c) Perquè el projecte ja s'ha oblidat a la S5.
   - d) Perquè la S5 només és per a qui no ha acabat el projecte.

8. Quina és la diferència entre una "decisió tècnica justificada" de nivell notable i una d'excel·lent, segons la R4·DO?
   - a) **El nivell notable justifica una decisió amb argument tècnic; l'excel·lent, a més, explica alternatives descartades.**
   - b) No hi ha diferència, els dos nivells són idèntics.
   - c) L'excel·lent només cal per a qui fa el repte ⭐⭐⭐.
   - d) La diferència és només la durada de l'explicació.

9. Per què cal declarar l'ús d'un assistent d'IA (per exemple, per redactar el dossier) en lloc d'amagar-ho?
   - a) Perquè fer servir IA sempre resta punts, es declari o no.
   - b) **Perquè declarar-ho no baixa la nota, però amagar-ho o no saber explicar el resultat sí (principi d'integritat acadèmica del curs).**
   - c) Perquè la IA no es pot fer servir mai en aquest curs.
   - d) Perquè declarar-ho és obligatori només si el docent ho demana explícitament.

10. Un repte d'estació ambiental combina "temperatura alta" i "CO₂ alt" per generar una alerta. Observa aquest fragment de `decideix()`:
    ```python
    def decideix(dades):
        global estat
        if estat == NORMAL:
            if dades["temp"] > LLINDAR_TEMP and dades["co2"] > LLINDAR_CO2:
                actualitza_estat(ALERTA)
        elif estat == ALERTA:
            if dades["temp"] <= LLINDAR_TEMP and dades["co2"] <= LLINDAR_CO2:
                actualitza_estat(NORMAL)
    ```
    Què fa exactament aquest fragment?
    - a) Canvia a ALERTA si la temperatura és alta, encara que el CO₂ sigui normal.
    - b) **Canvia a ALERTA només quan la temperatura I el CO₂ superen alhora els seus llindars, i torna a NORMAL només quan totes dues magnituds han baixat alhora.**
    - c) Canvia a ALERTA si la temperatura és alta O el CO₂ és alt (n'hi ha prou amb una de les dues condicions).
    - d) Actua directament sobre els motors segons la temperatura, sense passar per cap estat.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, per què es diu que la SA9 és una SA d'**integració** i no d'aprenentatge d'un component nou, com la majoria de les SA anteriors.

___________________________________________________________________

___________________________________________________________________

---

## Clau de correcció (docent)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | a | b | c | b | a | b | a | b | b |

La pregunta 11 és oberta: valora que expliqui que a la SA9 no s'introdueix cap component "nou i obligatori per a tothom" (com el DHT11 a SA6 o l'IMU a SA8), sinó que cada alumne **combina** components i tècniques ja après en SA anteriors (sensors, FSM, motors, ràdio) en una solució pròpia coherent: el saber nou és **com integrar-los**, no un component concret.

La pregunta 5 (CORREGIR) substitueix l'antiga pregunta sobre els nivells ⭐/⭐⭐/⭐⭐⭐ (record purament memorístic) per un error real recollit a la guia docent (Sessió 2: "el prototip barreja tota la lògica dins del `while True`, sense `percep()`/`decideix()`/`actua()`"): cal que l'alumnat sàpiga identificar-lo llegint codi, no només recitar-ne el motiu.

La pregunta 6 (COMPLETAR) substitueix l'antiga pregunta sobre els indicadors de la R4·DO (fet aïllat, sense codi) per una traça de la FSM del repte de reg: cal saber que `decideix()` només canvia d'estat i mai actua directament sobre el relé (aquest matís és el que distingeix la resposta correcta de la distractora b).

La pregunta 10 (TRAÇA) manté el tema original (integrar temperatura i CO₂ en una alerta combinada) però ara amb codi real: cal distingir una condició `and` d'una `or` llegint `decideix()`, en lloc de triar entre frases abstractes sobre "quins blocs s'integren".

---

*Qüestionari de conceptes de la SA9. Es recolza en `SA9_fitxa_alumnat.md`, `SA9_reptes_proposats.md`, `SA9_dossier_plantilla.md`,
`../00_General/00_Guia_defensa_oral.md`, `../00_General/00_IA_a_la_materia.md` i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
