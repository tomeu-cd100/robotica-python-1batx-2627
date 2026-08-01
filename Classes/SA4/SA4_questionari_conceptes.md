# SA4 · Qüestionari de conceptes (funcions, paràmetres, servo, PWM del motor)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega.

> **Ús.** Comprovació breu dels conceptes clau de la SA4: funcions (`def`), paràmetres,
> valor de retorn, servomotor amb PWM i motoreductor amb PWM/sentit.
> Es pot fer servir com a **repàs formatiu** o com a **prova curta qualificable**
> (10 preguntes × 1 punt = **nota 0-10**). Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. Què és una **funció** en programació?
   - a) Una variable que no canvia mai.
   - b) Un bloc de codi amb nom que es pot cridar tantes vegades com calgui.
   - c) Un tipus de bucle especial.
   - d) Un component del Micro:shield.

2. A `def mou_servo(angle):`, què és `angle`?
   - a) Un valor de retorn.
   - b) Un **paràmetre**: una dada que la funció rep quan es crida.
   - c) El nom de la funció.
   - d) Un error de sintaxi.

3. Quina diferència hi ha entre `graus_a_pwm(angle)` (amb `return`) i `mou_servo(angle)` (sense `return`)?
   - a) Cap, són intercanviables sempre.
   - b) `graus_a_pwm()` calcula i **retorna** un valor; `mou_servo()` **fa** alguna cosa (mou el servo) sense retornar-ne cap.
   - c) `mou_servo()` sempre és més ràpida.
   - d) `return` és obligatori a totes les funcions.

4. Per què `saluda(vegades)` evita haver de copiar i enganxar el mateix codi diverses vegades?
   - a) No ho evita, cal copiar-lo igualment.
   - b) Perquè el codi és **un de sol**, i es crida amb l'argument (`vegades`) que calgui cada cop.
   - c) Perquè les funcions s'executen soles sense cridar-les.
   - d) Perquè MicroPython ho fa automàticament sense `def`.

5. Per moure un servomotor a un angle concret amb `write_analog`, quin pas cal fer primer?
   - a) Res, `write_analog` ja funciona directament amb graus.
   - b) Fixar el període del pols amb `set_analog_period(20)` i convertir l'angle a un valor de PWM (aproximadament 26-128).
   - c) Connectar el servo a un pin ADC.
   - d) Fer servir `read_analog()`.

6. Per què un motoreductor necessita **dos** pins (un per sentit) en lloc d'un de sol?
   - a) Perquè `write_analog` només admet valors positius (0-1023); el sentit es tria enviant el PWM a un pin o a l'altre.
   - b) Perquè els motors sempre necessiten el doble de corrent.
   - c) És un caprici del fabricant, no té cap motiu tècnic.
   - d) Perquè cada pin controla un color diferent.

7. Per què no es pot alimentar un motoreductor només des del port USB de l'ordinador?
   - a) L'USB no subministra prou corrent per moure els motors amb fiabilitat.
   - b) Els motors no necessiten alimentació externa.
   - c) L'USB només serveix per carregar programes, mai per alimentar res.
   - d) No hi ha cap problema a fer-ho.

8. A `control_per_botons.py`, per què el botó B **sempre** atura el vehicle, encara que estigui girant?
   - a) Perquè el codi del botó B es comprova a **cada volta** del bucle `while True:`, no només en punts concrets.
   - b) Perquè `girar()` s'atura automàticament després d'un segon.
   - c) No és cert, el botó B només funciona si el vehicle està aturat.
   - d) Perquè els botons tenen prioritat màxima per hardware.

9. Quina és la funció **sense** cap paràmetre de `velocitat_pwm.py`?
   - a) `avancar()`.
   - b) `girar()`.
   - c) `aturar()`, perquè sempre fa el mateix (velocitat 0 als quatre pins).
   - d) Totes en tenen almenys un.

10. Per què els pins dels motoreductors (M1/M2) fixats a la SA4 **no es tornen a tocar** a la resta del curs?
    - a) Perquè el vehicle de T2 i el rover de T3 reaprofiten el mateix xassís i el mateix cablatge de moviment.
    - b) Perquè és impossible canviar-los un cop programats.
    - c) Perquè no té cap importància quins pins s'usin.
    - d) Perquè la ràdio de la SA5 els necessita lliures.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, per què encapsular `avancar()`, `retrocedir()`, `girar()` i `aturar()` en funcions fa que el codi de `control_per_botons.py` sigui més fàcil d'entendre que si tot estigués escrit en un únic bloc sense funcions.

___________________________________________________________________

___________________________________________________________________

---

## Clau de correcció (docent)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | b | b | b | b | a | a | a | c | a |

La pregunta 11 és oberta: valora que expliqui la idea d'**abstracció** (un nom que expressa la intenció, "avançar", amaga el detall de pins i PWM) i que el codi principal (`seguent_moviment()`) es pugui llegir com una seqüència d'ordres senzilles en lloc d'un bloc llarg de `write_analog`/`write_digital`.

---

*Qüestionari de conceptes de la SA4. Es recolza en `SA4_fitxa_alumnat.md`, `SA4_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
