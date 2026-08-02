# SA4 · Qüestionari de conceptes (funcions, paràmetres, servo, PWM del motor)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega.

> **Ús.** Comprovació breu dels conceptes clau de la SA4: funcions (`def`), paràmetres,
> valor de retorn, servomotor amb PWM i motoreductor amb PWM/sentit.
> **Repàs formatiu (autocorregible); es fa com a deures en acabar la SA.** No qualifica mai
> (vegeu `../../Programació%20didàctica/06_Avaluacio_criteris_qualificacio.md` §6.2): 10
> preguntes per autocorregir-te. Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. **[TRAÇA el codi]** Aquest fragment fa servir les funcions de moviment (com a `velocitat_pwm.py`). Quin és l'estat final de `pin13` en acabar d'executar-lo?

   ```python
   from microbit import *

   def avancar(velocitat):
       pin13.write_analog(velocitat)
       pin14.write_digital(0)
       pin15.write_analog(velocitat)
       pin16.write_digital(0)

   def girar(costat):
       if costat == 'dreta':
           pin13.write_analog(300)
           pin14.write_digital(0)
       elif costat == 'esquerra':
           pin14.write_analog(300)
           pin13.write_digital(0)

   avancar(700)
   girar('dreta')
   ```

   - a) `pin13` queda amb PWM 300, perquè `girar('dreta')` torna a escriure-hi després d'`avancar()`.
   - b) `pin13` queda amb PWM 700, el valor que li va donar `avancar()`.
   - c) `pin13` queda a 0, perquè `girar()` sempre reinicia els pins abans de moure's.
   - d) No es pot saber sense executar-ho al maquinari real.

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

7. **[COMPLETA el codi]** A aquest fragment (com a `funcions_moviments.py`, Sessió 1) falta una línia perquè el servo es mogui amb precisió als graus indicats. Quina hi ha d'anar?

   ```python
   from microbit import *

   ____   # <-- que hi va aqui?

   def mou_servo(angle):
       valor = 26 + (angle * (128 - 26)) // 180
       pin0.write_analog(valor)

   mou_servo(90)
   ```

   - a) `pin0.set_analog_period(20)`, per fixar el període de 20 ms que espera el servo abans d'enviar-hi PWM.
   - b) `pin0.write_digital(20)`
   - c) `pin0.read_analog(20)`
   - d) `sleep(20)`

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

10. **[CORREGEIX el codi]** Aquest codi hauria de fer avançar el vehicle en línia recta (com a `velocitat_pwm.py`), però el motor M1 només vibra sense girar. Troba l'error:

    ```python
    def avancar(velocitat):
        pin13.write_analog(velocitat)
        pin14.write_analog(velocitat)
        pin15.write_analog(velocitat)
        pin16.write_digital(0)
    ```

    - a) `pin14` hauria de ser `pin14.write_digital(0)`: els dos pins d'un mateix motor (M1: pin13/pin14) mai poden rebre PWM alhora.
    - b) `pin13` hauria de ser `pin13.write_digital(0)`.
    - c) Falta cridar `aturar()` al principi de la funció.
    - d) `velocitat` hauria de ser un valor negatiu.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, per què encapsular `avancar()`, `retrocedir()`, `girar()` i `aturar()` en funcions fa que el codi de `control_per_botons.py` sigui més fàcil d'entendre que si tot estigués escrit en un únic bloc sense funcions.

___________________________________________________________________

___________________________________________________________________

---

> 🔑 **La correcció.** La clau és **material del docent** (`Classes/Solucionari/Questionaris_conceptes_solucions.md`): així el qüestionari serveix de debò per comprovar què saps. Si el fas amb el **Google Form** del Classroom, la correcció te la dona el formulari mateix en enviar-lo; si el fas en paper, demana-la al docent en acabar.

---

*Qüestionari de conceptes de la SA4. Es recolza en `SA4_fitxa_alumnat.md`, `SA4_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
