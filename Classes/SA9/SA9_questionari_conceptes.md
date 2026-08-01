# SA9 · Qüestionari de conceptes (mètode de projecte, integració, documentació, ètica/ODS)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de la defensa oral i del checklist d'entrega.

> **Ús.** Comprovació breu dels conceptes clau de la SA9: mètode de projecte, integració de sistemes, dossier tècnic i defensa, i ètica de dades/ODS aplicats al propi repte. A diferència de les altres SA, aquestes preguntes **no versen sobre un sensor concret**: la SA9 integra tot el que ja saps.
> Es pot fer servir com a **repàs formatiu** o com a **prova curta qualificable**
> (10 preguntes × 1 punt = **nota 0-10**). Durada orientativa: **15-20 min**, individual, sense apunts.

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

5. Per què cada repte del banc de la SA9 té criteris ⭐/⭐⭐/⭐⭐⭐, igual que els reptes de SA1-SA8?
   - a) Perquè només compta l'ampliació ⭐⭐⭐; el nucli ⭐ no puntua.
   - b) **Perquè el nucli ⭐ és assolible per a tothom i les ampliacions permeten diferenciar sense excloure ningú.**
   - c) Els nivells són només decoratius, no tenen relació amb la nota.
   - d) ⭐⭐⭐ vol dir que cal fer els tres reptes diferents.

6. Segons la R4·DO (mini-rúbrica de la defensa oral), quins són els 3 indicadors que s'avaluen a la defensa de la SA9?
   - a) Volum de veu, durada i nombre de diapositives.
   - b) Quantitat de codi escrit, nombre de sensors i preu del maquinari.
   - c) Només la claredat; la resta no compta a la SA9.
   - d) **Claredat (què fa el sistema), decisió tècnica justificada (el per què) i resposta a preguntes.**

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

10. Un repte que combina "temperatura alta" **i** "CO₂ alt" alhora per generar una alerta combinada, integra quins dos blocs del curs com a mínim?
    - a) Cap, és un sol bloc (sensors).
    - b) Només robòtica mòbil.
    - c) **Sensors avançats/telemetria (lectura i protocol) i control (condicionals combinats per decidir l'alerta).**
    - d) Fabricació digital i electrònica bàsica.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, per què es diu que la SA9 és una SA d'**integració** i no d'aprenentatge d'un component nou, com la majoria de les SA anteriors.

___________________________________________________________________

___________________________________________________________________

---

## Clau de correcció (docent)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | a | b | c | b | d | b | a | b | c |

La pregunta 11 és oberta: valora que expliqui que a la SA9 no s'introdueix cap component "nou i obligatori per a tothom" (com el DHT11 a SA6 o l'IMU a SA8), sinó que cada alumne **combina** components i tècniques ja après en SA anteriors (sensors, FSM, motors, ràdio) en una solució pròpia coherent: el saber nou és **com integrar-los**, no un component concret.

---

*Qüestionari de conceptes de la SA9. Es recolza en `SA9_fitxa_alumnat.md`, `SA9_reptes_proposats.md`, `SA9_dossier_plantilla.md`,
`../00_General/00_Guia_defensa_oral.md`, `../00_General/00_IA_a_la_materia.md` i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
