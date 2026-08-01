# SA5 · Qüestionari de conceptes (ràdio, grup, protocol, esdeveniment)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega.

> **Ús.** Comprovació breu dels conceptes clau de la SA5: mòdul `radio` (`on`, `config`, `send`, `receive`),
> grup de ràdio, protocol de missatges amb prefix, i relació esdeveniment → acció.
> **Repàs formatiu (autocorregible); es fa com a deures en acabar la SA.** No qualifica mai
> (vegeu `../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md` §6.2): 10
> preguntes per autocorregir-te. Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. Què cal cridar **primer**, abans de poder enviar o rebre cap missatge de ràdio?
   - a) `radio.send()`.
   - b) `radio.on()`.
   - c) `radio.receive()`.
   - d) No cal preparar res, la ràdio ja està activa.

2. Per a què serveix `radio.config(group=N)`?
   - a) Per triar el color del LED.
   - b) Perquè només les plaques amb el **mateix** número de grup es puguin "sentir" entre elles.
   - c) Per augmentar la memòria disponible.
   - d) Per canviar la velocitat del processador.

3. **[TRAÇA]** Observa aquest fragment (com el de `comandament.py`):

   ```python
   PREFIX = "CMD:"
   ordre = ""
   if button_a.is_pressed() and button_b.is_pressed():
       ordre = "S"
   elif button_a.was_pressed():
       ordre = "F"
   elif button_b.was_pressed():
       ordre = "B"
   radio.send(PREFIX + ordre)
   ```

   Si en aquell instant **només** està premut el botó **B** (el A no), quin missatge s'envia?
   - a) `"CMD:S"`.
   - b) `"CMD:F"`.
   - c) `"CMD:B"`.
   - d) No s'envia cap missatge.

4. Per què cal cridar `radio.receive()` dins d'un `while True:` i no un sol cop?
   - a) Perquè no funciona bé fora d'un bucle.
   - b) Perquè `receive()` **no espera**: cal repetir la crida a cada volta per no perdre cap missatge que arribi entremig.
   - c) Perquè cada crida canvia de grup automàticament.
   - d) No cal, un sol cop ja n'hi ha prou.

5. Què és un **protocol** de missatges, en el sentit d'aquesta SA?
   - a) Un tipus de cable especial per a la ràdio.
   - b) Un acord tancat sobre com s'escriuen els missatges perquè qui els rep els pugui interpretar sense ambigüitat.
   - c) Un altre nom per a `radio.config()`.
   - d) La velocitat màxima de transmissió.

6. **[COMPLETAR]** A aquest programa hi falta una línia (marcada amb `pass  # <-- que hi va aqui?`):

   ```python
   from microbit import *
   import radio

   GRUP = 3
   radio.on()
   pass  # <-- que hi va aqui?

   while True:
       radio.send("CMD:F")
       sleep(500)
   ```

   Quina línia ha de substituir el `pass` perquè aquesta placa **només** es "senti" amb les plaques del mateix grup 3?
   - a) `radio.config(group=GRUP)`.
   - b) `radio.receive()`.
   - c) `PREFIX = "CMD:"`.
   - d) `display.show(GRUP)`.

7. **[CORREGIR]** Aquest codi té **un error**: el receptor mai reacciona a cap ordre del comandament, encara que tots dos tinguin el mateix `GRUP` i cridin `radio.on()` correctament.

   ```python
   # A la placa COMANDAMENT:
   PREFIX = "CMD:"
   radio.send(PREFIX + "F")

   # A la placa RECEPTORA:
   PREFIX = "cmd:"
   missatge = radio.receive()
   if missatge is not None and missatge.startswith(PREFIX):
       ordre = missatge[len(PREFIX):]
       actua(ordre)
   ```

   On és l'error?
   - a) El `PREFIX` del receptor està en minúscules (`"cmd:"`) i no coincideix **exactament** amb el del comandament (`"CMD:"`), així que `startswith(PREFIX)` mai és cert.
   - b) `radio.send()` no admet concatenar cadenes amb `+`.
   - c) Hauria de ser `PREFIX.startswith(missatge)` en lloc de `missatge.startswith(PREFIX)`.
   - d) Cal cridar `radio.receive()` dues vegades per cada missatge.

8. Quina diferència hi ha entre una **llista** i una **tupla** com les que es fan servir per guardar l'historial de comandes?
   - a) Cap, són exactament el mateix.
   - b) Una llista es pot modificar després de crear-la (`append`, `pop`); una tupla, un cop creada, no.
   - c) Les tuples només poden guardar números.
   - d) Les llistes només poden tenir un element.

9. A `receptor_vehicle.py`, quines funcions de moviment es reutilitzen **tal qual** de la SA4?
   - a) Cap, s'han hagut de reescriure totes per a la ràdio.
   - b) `avancar()`, `retrocedir()`, `girar()` i `aturar()`.
   - c) Només `aturar()`.
   - d) Les funcions de moviment no existien abans de la SA5.

10. Per què el docent assigna els **grups de ràdio per parelles de números de llista** en lloc de deixar que tothom faci servir el mateix grup?
    - a) Perquè si no, totes les plaques de la classe es "sentirien" entre elles i hi hauria interferències.
    - b) Perquè és obligatori per llei tenir un grup diferent cada dia.
    - c) No té cap motiu tècnic, és només organització.
    - d) Perquè cada grup de ràdio necessita un `PREFIX` diferent obligatòriament.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, per què `receptor_vehicle.py` no és "un programa nou de zero" sinó que reutilitza el codi de moviment ja fet a la SA4. Quin avantatge té reutilitzar-lo en lloc de tornar-lo a escriure?

___________________________________________________________________

___________________________________________________________________

---

## Clau de correcció (docent)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | b | c | b | b | a | a | b | b | a |

La pregunta 3 (traça) demana seguir l'execució real d'un `if`/`elif` amb `is_pressed()`/`was_pressed()`: valora que l'alumnat distingeixi que amb només el botó B premut s'entra a la branca `elif button_b.was_pressed()`, no a la del A+B ni a la del A sol.

La pregunta 6 (completar) comprova que l'alumnat identifica **quina crida concreta** falta (`radio.config(group=GRUP)`) per activar el filtre de grup, no només que en sap la definició de memòria.

La pregunta 7 (corregir) es basa en l'error freqüent documentat a la guia docent ("el `PREFIX` no coincideix exactament entre comandament i receptor"): valora que l'alumnat sàpiga localitzar una discrepància concreta de text (majúscules) dins de codi que, a simple vista, sembla correcte.

La pregunta 11 és oberta: valora que expliqui la idea de **reutilització**/modularitat (les funcions `avancar`/`girar`/`aturar` ja estaven provades i funcionaven a la SA4; només cal canviar **l'entrada** que les crida, dels botons a la ràdio) i que reconegui l'avantatge de no haver de tornar a depurar una lògica ja validada.

---

*Qüestionari de conceptes de la SA5. Es recolza en `SA5_fitxa_alumnat.md`, `SA5_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
