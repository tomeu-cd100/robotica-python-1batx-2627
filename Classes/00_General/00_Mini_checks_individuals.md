# 00 · Mini-checks individuals (radar formatiu de cada SA)

> **Per a qui és?** Per al **docent**. Un **micro-repte individual de 10 minuts** per SA (SA1–SA9), a fer **en solitari, sense apunts i sense IA**. **No qualifica**: és un radar formatiu.
> **Quan es passa?** A l'**inici de la sessió que indica cada fitxa** (normalment la Sessió 2; a SA1 i a les SA que tanquen trimestre —SA3, SA6, SA9— es reubica perquè la darrera sessió és la prova pràctica): prou aviat per reaccionar, prou tard perquè hi hagi hagut pràctica.

## El problema que resol

Tot el curs és **individual** (`Programació didàctica/04_Metodologia.md` §4.3): no hi ha parella que «arrossegui» ningú, però sí altres maneres d'arribar a la prova trimestral sense saber-ho fer sol —copiar un esquelet sense entendre'l, demanar-ho a una IA sense passar per DEPURA, o anar acumulant retard sense que ningú se n'adoni fins que és tard. Sense aquest radar, el primer moment en què es detectaria seria la **prova trimestral** — massa tard per reaccionar. El mini-check dona **10 minuts de veritat, sense ajuda de cap tipus**, cada SA.

## Rutina (10 minuts)

1. **Quan:** a l'**inici de la sessió indicada** de cada SA. **Aquell dia el mini-check substitueix la graella d'activació** (`00_Banc_activacio_repas.md`): també és recuperació.
2. **Com:** individual, **sense apunts, sense IA i sense connexió a internet**, en paper o a l'editor amb el projector apagat. 10' clavats.
3. **Correcció:** no es puntua. El docent fa una passada ràpida amb **semàfor**:
   - 🟢 **Ho fa sol** (errors de detall com a molt).
   - 🟡 **Se'n surt amb dubtes** (estructura bé, sintaxi o conceptes coixos).
   - 🟠🔴 **No se'n surt sol** (no distingeix les estructures bàsiques).
4. **Acció amb els 🔴 (el sentit de tot plegat):**
   - Deriva a la secció de `SA0/SA0_guia_programacio.md` indicada a cada check.
   - Reforç individual a la sessió següent (bastida addicional, atenció prioritària a la pràctica guiada).
   - Si es repeteix dues SA seguides, activa mesures addicionals (`Programació didàctica/05_Atencio_a_la_diversitat.md` §5.2).
5. **Registre:** un semàfor per alumne al full de seguiment (`Avaluació/Full_qualificacio_competencies.md`). En acabar el trimestre, la sèrie de semàfors és evidència d'evolució (no de nota).

> ⚖️ **No qualifica, i s'ha de dir explícitament a l'alumnat.** L'objectiu és que escriguin sense por: el mini-check només funciona com a radar si ningú té incentius per dissimular.

---

## SA1 · Mini-check (inici de la Sessió 3)

**Enunciat (projectar):**
> Llegeix aquest programa **sense executar-lo** i explica, línia per línia, què fa:
> ```python
> from microbit import *
> display.scroll("HOLA")
> sleep(1000)
> display.show(Image.HAPPY)
> ```

**Què mires:** identifica l'`import` com a requisit · sap que `scroll` mostra text lletra a lletra i `show` una imatge fixa · entén `sleep()` com una pausa en mil·lisegons.
**🟢** explica les 4 línies amb precisió · **🟡** explica el que fa però no per què cal l'`import` · **🔴** no distingeix `scroll` de `show`.
**Reforç 🔴:** `SA0_guia_programacio.md` A1-A2 (primer programa, estructura d'un fitxer `.py`).

## SA2 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> Escriu **de memòria** un programa que faci parpellejar el LED del pin **P1**: mig segon encès, mig segon apagat, per sempre.

**Què mires:** `while True:` · `pin1.write_digital(1)` / `pin1.write_digital(0)` · `sleep(500)` a cada estat · indentació correcta.
**🟢** estructura completa i correcta · **🟡** estructura bé, errors de sintaxi o d'indentació · **🔴** no sap on va cada instrucció.
**Reforç 🔴:** `SA0_guia_programacio.md` A3-A4 (bucles, sortides digitals).

## SA3 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> Tens `llum = display.read_light_level()` (0-255) al bucle principal. **(a)** Escriu l'`if/else` perquè el LED de P1 s'encengui quan `llum` sigui **més petit que 50** i s'apagui altrament. **(b)** Entre quins valors es mou `llum`?

**Què mires:** condició amb `<` ben escrita · les dues branques actuen sobre el LED · resposta (b): 0-255.
**🟢** tot correcte · **🟡** if bé però rang confós amb 0-1023 · **🔴** no sap escriure la condició.
**Reforç 🔴:** `SA0_guia_programacio.md` A5 (`if/elif/else`) i A6 (entrades analògiques).

## SA4 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> Escriu una funció `avancar(velocitat)` que faci moure el motor esquerre (canal M1) a la velocitat rebuda com a paràmetre. **(b)** En una frase: per què el motoreductor **no** es pot alimentar només amb el corrent del port USB?

**Què mires:** `def avancar(velocitat):` amb el paràmetre ben col·locat · ús del paràmetre dins la funció (no un valor fix) · (b) consum de corrent superior al que dona l'USB → cal alimentació externa (portapiles).
**🟢** tot · **🟡** funció correcta però (b) confosa · **🔴** no recorda la sintaxi de `def`/paràmetre.
**Reforç 🔴:** `SA0_guia_programacio.md` A7 (funcions i paràmetres).

## SA5 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> Anota què fa **cada línia** d'aquest programa:
> ```python
> import radio
> radio.config(group=10)
> radio.on()
> missatge = radio.receive()
> if missatge == 'F':
>     avancar(400)
> ```

**Què mires:** `group` = canal compartit (l'altra placa ha de tenir el mateix) · `radio.on()` obligatori · `receive()` pot retornar `None` si no ha arribat res · comparació de text amb `==`.
**🟢** explica `group` i el possible `None` · **🟡** descriu línies però no el paper del `group` · **🔴** no distingeix emissor de receptor.
**Reforç 🔴:** repassar el bloc de ràdio de `SA0_guia_programacio.md` Part B.

## SA6 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> Un termòstat activa el relé quan `temp < 25` i el desactiva quan `temp >= 25`. A la pràctica, el relé fa **clic-clic sense parar** al voltant de 25 °C. **(a)** Per què passa? **(b)** Reescriu les condicions perquè no passi (pista: dos llindars).

**Què mires:** (a) la lectura balla al voltant de la consigna → commutació contínua · (b) histèresi: `if temp < 24: activa()` / `if temp > 26: desactiva()` (valors raonables).
**🟢** explica i escriu els dos llindars · **🟡** intueix el problema però només mou un llindar · **🔴** no veu el problema.
**Reforç 🔴:** repassar l'exemple de termòstat amb histèresi de la fitxa SA6.

## SA7 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> El rover té les funcions fetes: `mesura_distancia()` (cm), `avancar()`, `aturar()` i `girar()`. Escriu el **bucle complet** del comportament *evita-obstacles*: si hi ha res a menys de 15 cm, atura't i gira; si no, avança.

**Què mires:** `if mesura_distancia() < 15: aturar(); girar()` / `else: avancar()` (amb pauses opcionals) · que la lectura es faci **a cada volta** del bucle.
**🟢** estructura reactiva correcta · **🟡** lògica bé però llegeix el sensor un sol cop fora del bucle · **🔴** no lliga sensor→decisió→acció.
**Reforç 🔴:** repassar el cicle «llegir → decidir → actuar» de la fitxa SA7.

## SA8 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> Anota què fa **cada línia** d'aquest emissor de telemetria:
> ```python
> import radio
> radio.config(group=10)
> radio.on()
> while True:
>     radio.send('T:' + str(temperature()))
>     sleep(2000)
> ```

**Què mires:** `group` = canal compartit amb l'estació base · `radio.on()` obligatori · `send()` envia text (per això cal `str(...)`) · `sleep` marca la cadència de mostreig.
**🟢** explica `group` i la conversió a text · **🟡** descriu línies però no per què cal `str()` · **🔴** no distingeix rover d'estació base.
**Reforç 🔴:** repassar l'esquelet de telemetria de `00_Projecte_T3_Rover.md`.

## SA9 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> Escriu una funció `comprova_i_envia()` que **integri** el que ja saps: llegeix un sensor (per exemple `accelerometer.get_x()`), i si el valor supera un llindar que tu decideixis, envia un missatge per ràdio amb `radio.send()`.

**Què mires:** capacitat d'**integrar sense bastida** dos blocs ja apresos per separat (llegir sensor + condicional + ràdio) en una sola funció pròpia; que el llindar sigui una constant raonada, no un número a l'atzar.
**🟢** integra els tres blocs sense ajuda · **🟡** els tres blocs hi són però amb estructura confusa (p. ex. `radio.on()` oblidat) · **🔴** no sap combinar sensor i ràdio en una sola funció.
**Reforç 🔴:** repassar per separat SA3 (sensors), SA5/SA8 (ràdio) i tornar-ho a intentar abans del repte lliure.

---

> Tots els mini-checks alimenten el **full de seguiment** de l'alumnat i són la font de l'indicador trimestral «distribució de semàfors dels mini-checks» de `Programació didàctica/06b_Avaluacio_programacio_i_practica_docent.md` §1 (llindar d'alerta: ≥ ⅓ de 🟡/🔴 en un check → repesca col·lectiva de 10').
