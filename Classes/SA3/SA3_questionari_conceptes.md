# SA3 · Qüestionari de conceptes (entrades digitals, analògiques i sensors)

> 🧑‍🎓 **Quan toca fer-lo?** En acabar les activitats de la SA, com a **consolidació** abans de repassar el checklist d'entrega — i com a **repàs directe** abans de la prova pràctica T1 (Sessió 4).

> **Ús.** Comprovació breu dels conceptes clau de la SA3: entrades digitals vs analògiques,
> `read_analog()`, mapatge de rangs, *pull-up*/antirebot, HC-SR04 i PIR.
> Es pot fer servir com a **repàs formatiu** o com a **prova curta qualificable**
> (10 preguntes × 1 punt = **nota 0-10**). Durada orientativa: **15-20 min**, individual, sense apunts.

**Nom:** ______________________  **Data:** __________

---

## Preguntes (tria una resposta)

1. Quina instrucció llegeix si el botó A de la micro:bit està premut?
   - a) `button_a.write_digital(1)`
   - b) `button_a.is_pressed()`
   - c) `pin_a.read_analog()`
   - d) `display.show(Image.YES)`

2. Una entrada **analògica** (`read_analog()`) es diferencia d'una **digital** (`read_digital()`/`is_pressed()`) perquè…
   - a) Només serveix per als botons.
   - b) Dona un rang de valors (per exemple 0-1023), no només 0/1.
   - c) No es pot fer servir amb sensors.
   - d) Sempre dona el mateix valor.

3. Quins pins de la micro:bit V2 tenen conversor analògic-digital (ADC) per llegir senyals analògics?
   - a) Tots els pins.
   - b) Només P0 i P1.
   - c) P0, P1, P2, P3, P4 i P10.
   - d) Només els pins connectats al Micro:shield.

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

9. Per què el sensor **PIR** necessita 30-60 segons d'estabilització abans d'usar-lo?
   - a) No en necessita, funciona a l'instant.
   - b) Perquè si no s'espera, sol donar falsos positius mentre el mòdul s'ajusta a l'entorn.
   - c) Perquè necessita carregar-se com una bateria.
   - d) Perquè és més lent que un botó.

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
| b | b | c | b | b | b | b | b | b | b |

La pregunta 11 és oberta: valora que expliqui que un llindar "inventat" pot no funcionar amb les condicions reals de l'aula (llum ambiental, soroll de fons...) i que l'exemple sigui coherent amb un component real de la SA3 (llindar de foscor, de temperatura, de so o de distància).

---

*Qüestionari de conceptes de la SA3. Es recolza en `SA3_fitxa_alumnat.md`, `SA3_esquemes_connexions.md`
i el vocabulari de [`../SA0/SA0_vocabulari_robotica.md`](../SA0/SA0_vocabulari_robotica.md). Llicència CC BY-SA 4.0.*
