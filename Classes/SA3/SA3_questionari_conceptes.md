# SA3 · Qüestionari de conceptes (entrades digitals, analògiques i sensors)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega — i com a **repàs directe** abans de la prova pràctica T1 (Sessió 4).

> **Ús.** Comprovació breu dels conceptes clau de la SA3: entrades digitals vs analògiques,
> `read_analog()`, mapatge de rangs, *pull-up*/antirebot, HC-SR04 i PIR.
> Es pot fer servir com a **repàs formatiu** o com a **prova curta qualificable**
> (10 preguntes × 1 punt = **nota 0-10**). Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. **[TRAÇA]** Llegeix aquest codi (sense executar-lo) i respon: què fa?

   ```python
   from microbit import *

   comptador = 0
   pin0.set_pull(pin0.PULL_UP)

   while True:
       if pin0.read_digital() == 0:
           comptador += 1
           display.show(comptador)
       sleep(200)
   ```
   - a) Compta i mostra al display el nombre de vegades que el pin P0 es posa a `1` (nivell alt).
   - b) Compta i mostra al display el nombre de vegades que es prem un polsador connectat a P0 (amb *pull-up*, `0` = premut).
   - c) Llegeix la temperatura ambiental cada 200 ms.
   - d) Fa pampallugar el display cada 200 ms sense comptar res.

2. Una entrada **analògica** (`read_analog()`) es diferencia d'una **digital** (`read_digital()`/`is_pressed()`) perquè…
   - a) Només serveix per als botons.
   - b) Dona un rang de valors (per exemple 0-1023), no només 0/1.
   - c) No es pot fer servir amb sensors.
   - d) Sempre dona el mateix valor.

3. **[COMPLETAR]** A aquesta funció `mapa()` li falta la línia final (marcada `____`). Quina línia cal perquè `n` doni un valor de sortida ben calculat dins el rang 0-5?

   ```python
   from microbit import *

   def mapa(valor, e_min, e_max, s_min, s_max):
       rang_e = e_max - e_min
       rang_s = s_max - s_min
       proporcio = (valor - e_min) / rang_e
       ____

   llum = pin0.read_analog()
   n = mapa(llum, 0, 1023, 0, 5)
   display.show(n)
   ```
   - a) `return s_min + proporcio * rang_s`
   - b) `print(proporcio)`
   - c) `return valor`
   - d) `return rang_e`

4. Per què cal un *pull-up* (`pin.set_pull(pin.PULL_UP)`) en un polsador extern?
   - a) Perquè el LED s'encengui més fort.
   - b) Perquè, sense ell, el pin "flota" i dona lectures indeterminades quan el circuit és obert.
   - c) Perquè és obligatori per a tots els pins ADC.
   - d) No serveix per a res, és opcional sempre.

5. Què és el "rebot" (*bounce*) d'un polsador i per què cal un antirebot per software?
   - a) És un error de programació, no té relació amb el maquinari.
   - b) El contacte mecànic "tremola" en prémer, i sense antirebot una premuda es pot comptar diverses vegades.
   - c) Fa que el LED reboti de color.
   - d) Només passa als botons A/B interns.

6. MicroPython **no** té una funció `map()` integrada com Arduino. Com es resol a la SA3?
   - a) No es pot mapar cap valor.
   - b) Programant una funció pròpia (`mapa()`) amb una regla de tres entre dos rangs.
   - c) Fent servir sempre `write_analog()`.
   - d) Convertint-ho tot a text.

7. L'HC-SR04 (ultrasons) mesura la distància…
   - a) Llegint directament un valor analògic de distància.
   - b) Mesurant el temps que triga un pols de so a anar i tornar (temps de vol).
   - c) Amb un sensor de llum.
   - d) Comptant botons premuts.

8. Per què `machine.time_pulse_us()` és més adequat que `sleep()` per mesurar el pols de l'echo de l'HC-SR04?
   - a) `sleep()` no existeix a MicroPython.
   - b) `time_pulse_us()` mesura microsegons amb precisió; `sleep()` treballa en mil·lisegons i no serveix per mesurar un pols tan curt.
   - c) Són exactament el mateix.
   - d) `time_pulse_us()` només funciona amb LED.

9. **[CORREGIR]** Aquest codi hauria de mostrar una cara de son (`Image.ASLEEP`) quan l'entorn és fosc, però gairebé sempre mostra `Image.HAPPY`, fins i tot a les fosques. On és l'error?

   ```python
   from microbit import *

   LLINDAR_FOSCOR = 50

   while True:
       llum = pin0.read_analog()   # 0-1023, sensor extern
       if llum < LLINDAR_FOSCOR:
           display.show(Image.ASLEEP)
       else:
           display.show(Image.HAPPY)
       sleep(200)
   ```
   - a) `LLINDAR_FOSCOR = 50` és un llindar pensat per a l'escala 0-255 (sensors integrats), però `pin0.read_analog()` dona valors en escala 0-1023: cal un llindar molt més alt (o usar `display.read_light_level()`).
   - b) `Image.ASLEEP` no existeix a MicroPython.
   - c) El bucle `while True:` està mal escrit i no s'executa mai.
   - d) `sleep(200)` fa que el programa vagi massa ràpid per detectar la foscor.

10. A `mascota_reactiva.py`, per què cada branca de `llegeix_sensors()` acaba amb un `return`?
    - a) És obligatori a MicroPython, sense excepcions.
    - b) Perquè només es vol UN estímul (el de més prioritat) per volta, i el `return` evita que se'n processin diversos alhora.
    - c) Perquè `return` apaga la micro:bit.
    - d) No té cap efecte, és estètic.

---

## Pregunta oberta (opcional)

11. Explica, amb les teves paraules, per què cal **mesurar amb el REPL** el valor real d'un sensor abans de fixar un llindar (`if valor > ...`), i posa un exemple concret d'un llindar que hagis calibrat a la teva mascota.

___________________________________________________________________

___________________________________________________________________

---

## Clau de correcció (docent)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | b | a | b | b | b | b | b | a | b |

La pregunta 1 (**TRAÇA**) substitueix una pregunta merament memorística per exigir seguir l'execució d'un codi real (comptador amb *pull-up* i antirebot implícit) i triar què fa, no només reconèixer una instrucció aïllada.

La pregunta 3 (**COMPLETAR**) substitueix la llista memorística de pins ADC per demanar completar la línia que falta a `mapa()`, comprovant que l'alumnat entén per què cal un `return` amb la regla de tres, no només que existeix la funció.

La pregunta 9 (**CORREGIR**) substitueix el fet aïllat del PIR per un error real i freqüent (confondre l'escala 0-255 dels sensors integrats amb la 0-1023 dels pins ADC, documentat a la guia docent), i obliga a diagnosticar-lo sobre codi complet.

La pregunta 11 és oberta: valora que expliqui que un llindar "inventat" pot no funcionar amb les condicions reals de l'aula (llum ambiental, soroll de fons...) i que l'exemple sigui coherent amb un component real de la SA3 (llindar de foscor, de temperatura, de so o de distància).

---

*Qüestionari de conceptes de la SA3. Es recolza en `SA3_fitxa_alumnat.md`, `SA3_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
