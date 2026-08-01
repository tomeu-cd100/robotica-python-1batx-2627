# 00 · Mini-checks individuals (radar formatiu de cada SA)

> **Per a qui és?** Per al **docent**. Un **micro-repte individual de 10 minuts** per SA (SA1–SA9), sempre d'**escriptura de codi curt (5-10 línies)**, a fer **en solitari, sense apunts i sense IA**. **Cap mini-check individual no es puntua en el moment de fer-lo** (és un radar formatiu i cal dir-ho explícitament a l'alumnat), però **el millor mini-check del trimestre sí que compta** un 5 % dins la dimensió «Proves pràctiques» — vegeu §«El millor mini-check qualifica» més avall i `Programació didàctica/06_Avaluacio_criteris_qualificacio.md` §6.3.
> **Quan es passa?** **On digui la guia de cada SA** (normalment la Sessió 2, però no sempre a l'**inici**: a SA4 i SA5 la pròpia guia el situa al **final** de la Sessió 2, combinat amb el tancament, i les capçaleres de cada bloc més avall ho reflecteixen). A SA6, SA7, SA8 i SA9 el mini-check **substitueix la graella d'activació** aquell dia (no hi ha fila d'Activació/kata pròpia a la sessió); a la resta de SA **conviu amb la kata** (totes dues fases hi apareixen, per separat, a la taula de la sessió). A SA1 i a les SA que tanquen trimestre —SA3, SA6, SA9— es reubica, a més, perquè la darrera sessió és la prova pràctica: prou aviat per reaccionar, prou tard perquè hi hagi hagut pràctica.

## El problema que resol

Tot el curs és **individual** (`Programació didàctica/04_Metodologia.md` §4.3): no hi ha parella que «arrossegui» ningú, però sí altres maneres d'arribar a la prova trimestral sense saber-ho fer sol —copiar un esquelet sense entendre'l, demanar-ho a una IA sense passar per DEPURA, o anar acumulant retard sense que ningú se n'adoni fins que és tard. Sense aquest radar, el primer moment en què es detectaria seria la **prova trimestral** — massa tard per reaccionar. El mini-check dona **10 minuts de veritat, escrivint codi de zero i sense ajuda de cap tipus**, cada SA.

## Rutina (10 minuts)

1. **Quan:** a l'**inici de la sessió indicada** de cada SA. **Aquell dia el mini-check substitueix la graella d'activació** (`00_Banc_activacio_repas.md`): també és recuperació.
2. **Com:** individual, **sense apunts, sense IA i sense connexió a internet**, en paper o a l'editor amb el projector apagat. 10' clavats. Es demana sempre **escriure** un programa curt (5-10 línies) de zero, mai només llegir-lo o triar una opció.
3. **Correcció:** no es puntua individualment (excepte l'ús retrospectiu del §«El millor mini-check qualifica»). El docent fa una passada ràpida amb **semàfor**:
   - 🟢 **Ho fa sol** (errors de detall com a molt).
   - 🟡 **Se'n surt amb dubtes** (estructura bé, sintaxi o conceptes coixos).
   - 🟠🔴 **No se'n surt sol** (no distingeix les estructures bàsiques).
4. **Registre del tipus d'error (junt amb el semàfor).** Quan el resultat no és 🟢, el docent anota també **quin tipus d'error predomina**, amb una lletra enganxada al semàfor (p. ex. `🟡-C`):
   - **S · Sintaxi** — indentació, falten `:` o parèntesis, noms mal escrits, `=` per `==`: **sap què ha de fer però no ho escriu bé**.
   - **C · Concepte** — no sap quina estructura cal (bucle, condició, paràmetre, `return`...) o la fa servir amb el sentit canviat: **no té clar què ha de fer**.
   - **D · Descuit** — la solució és correcta en l'essencial però hi falta un detall menor (un `import`, una `sleep()`, un cas límit): **ho sap fer, s'ha distret**.
   - Aquesta lletra és la que orienta el reforç: **S** → practicar dictats/Parsons de sintaxi; **C** → tornar a la secció indicada de `SA0/SA0_guia_programacio.md`; **D** → revisió pausada abans d'entregar (autocorrecció), no repàs de contingut.
5. **Acció amb els 🟠/🔴 (el sentit de tot plegat):**
   - Deriva a la secció de `SA0/SA0_guia_programacio.md` indicada a cada check.
   - Reforç individual a la sessió següent (bastida addicional, atenció prioritària a la pràctica guiada).
   - Si es repeteix dues SA seguides, activa mesures addicionals (`Programació didàctica/05_Atencio_a_la_diversitat.md` §5.2).
6. **Registre:** un semàfor **+ tipus d'error** per alumne al full de seguiment (`Avaluació/Full_seguiment_grup.md`, columna «Mini-check SA__») i al full de qualificació (`Avaluació/Full_qualificacio_competencies.md`). En acabar el trimestre, la sèrie de semàfors és evidència d'evolució **i** la base per triar el millor mini-check qualificable.

> ⚖️ **Cap mini-check individual no qualifica el dia que es fa, i s'ha de dir explícitament a l'alumnat.** L'objectiu és que escriguin sense por: el mini-check només funciona com a radar si ningú té incentius per dissimular. Que el **millor** del trimestre compti a posteriori (§ següent) no ho canvia: com no se sap per endavant quin serà el millor, cal seguir fent-los tots amb honestedat.

## El millor mini-check del trimestre qualifica (5 %)

- **Es guarden totes les evidències** de cada mini-check del trimestre (paper arxivat o captura de l'editor), amb el semàfor i el tipus d'error anotats.
- **En tancar el trimestre**, el docent selecciona, per a cada alumne/a, el **mini-check amb millor resultat** d'entre els fets aquell trimestre i li assigna una nota **1-10** amb l'escala:

  | Semàfor | Nota orientativa | Matís del docent |
  |---|---|---|
  | 🟢 | 9-10 | 10 si és net a la primera; 9 si hi ha algun detall menor. |
  | 🟡 | 6-8 | Més amunt (8) com més a prop de 🟢; més avall (6) com més a prop de 🟠. |
  | 🟠 | 4-5 | 5 si hi ha intent estructurat encara que incomplet; 4 si és molt parcial. |
  | 🔴 | 1-3 | 3 si hi ha almenys una línia correcta; 1 si és en blanc o incoherent. |

- Aquesta nota s'incorpora a la dimensió **«Proves pràctiques» (20 %)** com el seu tram de **5 %** (l'altre 15 % és la prova trimestral T1/T2/T3): vegeu `Programació didàctica/06_Avaluacio_criteris_qualificacio.md` §6.3.
- **No es fa mitjana** dels mini-checks del trimestre: qualifica el **millor**, no el conjunt — així ningú perd per un dia fluix, i la funció de radar (detectar dificultats sense por) es manté intacta a la resta.

---

## SA1 · Mini-check (inici de la Sessió 3)

**Enunciat (projectar):**
> Sense mirar `hola_mon.py`, **escriu de zero** un programa curt que: **(1)** mostri el teu nom lletra a lletra, **(2)** esperi mig segon, i **(3)** mostri fixa una imatge `Image.HAPPY` durant 2 segons.

**Què mires:** primera línia `from microbit import *` present · `display.scroll("...")` per al nom · `sleep(500)` entremig · `display.show(Image.HAPPY)` · `sleep(2000)` final.
**🟢** les 5 línies completes i en l'ordre correcte · **🟡** l'estructura hi és però falta l'`import` o confon `scroll`/`show` · **🔴** no sap escriure cap de les dues instruccions de display.
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

## SA4 · Mini-check (final de la Sessió 2, combinat amb el tancament)

**Enunciat (projectar):**
> Escriu una funció `avancar(velocitat)` que faci moure el motor esquerre (canal M1) a la velocitat rebuda com a paràmetre. **(b)** En una frase: per què el motoreductor **no** es pot alimentar només amb el corrent del port USB?

**Què mires:** `def avancar(velocitat):` amb el paràmetre ben col·locat · ús del paràmetre dins la funció (no un valor fix) · (b) consum de corrent superior al que dona l'USB → cal alimentació externa (portapiles).
**🟢** tot · **🟡** funció correcta però (b) confosa · **🔴** no recorda la sintaxi de `def`/paràmetre.
**Reforç 🔴:** `SA0_guia_programacio.md` A7 (funcions i paràmetres).

## SA5 · Mini-check (final de la Sessió 2, combinat amb el tancament)

**Enunciat (projectar):**
> **Escriu de zero** el bucle receptor: configura la ràdio en el canal (`group`) **10**, activa-la, i a cada volta comprova si ha arribat el missatge exacte `'F'`; si és així, crida `avancar(400)`.

**Què mires:** `import radio` · `radio.config(group=10)` · `radio.on()` obligatori (abans del bucle) · dins el `while True:`, `missatge = radio.receive()` i `if missatge == 'F':` amb `==` (no `=`).
**🟢** les 6-7 línies completes, `on()` fora del bucle i la comparació ben feta · **🟡** l'estructura hi és però oblida `radio.on()` o el `group` · **🔴** no distingeix `receive()` d'una simple lectura de botó.
**Reforç 🔴:** repassar el bloc de ràdio de `SA0_guia_programacio.md` Part B.

## SA6 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> Un termòstat activa el relé quan `temp < 25` i el desactiva quan `temp >= 25`. A la pràctica, el relé fa **clic-clic sense parar** al voltant de 25 °C. **(a)** Per què passa? **(b)** Reescriu les condicions perquè no passi (pista: dos llindars).

**Què mires:** (a) la lectura balla al voltant de la consigna → commutació contínua · (b) histèresi: `if temp < 24: activa()` / `if temp > 26: desactiva()` (valors raonables).
**🟢** explica i escriu els dos llindars · **🟡** intueix el problema però només mou un llindar · **🔴** no veu el problema.
**Reforç 🔴:** repassar l'exemple de termòstat amb histèresi de la fitxa SA6.

## SA7 · Mini-check (inici de la Sessió 2)

> Deliberadament **no** demana res del seguidor de línia (tema de la Sessió 2, que encara no s'ha explicat quan es passa el mini-check): repassa el cicle **llegir → decidir → actuar** amb un sensor analògic genèric (patró ja après a la SA3) aplicat al rover ja calibrat a la Sessió 1.

**Enunciat (projectar):**
> El teu rover ja avança recte gràcies al calibratge de M1/M2 (Sessió 1). Imagina un sensor analògic qualsevol muntat al davant, llegit amb `SENSOR.read_analog()` (0-1023), amb un llindar ja calibrat `LLINDAR = 500`. Les funcions de moviment (`avancar()`, `aturar()`) ja estan fetes. Escriu el **bucle complet**: si la lectura és per sota del llindar, avança (`avancar(400)`); si és per sobre, atura't (`aturar()`).

**Què mires:** `while True:` · `if SENSOR.read_analog() < LLINDAR: avancar(400)` / `else: aturar()` · que la lectura es faci **a cada volta** del bucle (llaç tancat: llegeix → decideix → actua), no un sol cop abans d'entrar-hi.
**🟢** estructura reactiva completa i correcta, lectura dins del bucle · **🟡** lògica bé però llegeix el sensor un sol cop fora del bucle, o inverteix el sentit de la comparació · **🔴** no lliga sensor→decisió→acció.
**Reforç 🔴:** repassar el cicle «llegir → decidir → actuar» amb `nivell_llum.py`/`termometre.py` (SA3); el seguidor de línia concret (`SEGUIDOR_LINIA`, `LLINDAR_LINIA`) i l'evita-obstacles amb `mesura_distancia()` arriben aquesta mateixa Sessió 2 i la Sessió 3.

## SA8 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> **Escriu de zero** un emissor de telemetria: configura la ràdio en el canal **10**, activa-la, i cada **2 segons** envia la temperatura llegida amb `temperature()`, en forma de text que comenci per `'T:'`.

**Què mires:** `import radio` · `radio.config(group=10)` · `radio.on()` · dins `while True:`, `radio.send('T:' + str(temperature()))` (cal `str(...)` perquè `send` envia text) · `sleep(2000)` marca la cadència.
**🟢** les 6 línies completes amb el `str(...)` ben col·locat · **🟡** l'estructura hi és però oblida `str(...)` o el `sleep` · **🔴** no sap muntar l'emissor (falta `config`/`on`/`send`).
**Reforç 🔴:** repassar l'esquelet de telemetria de `00_Projecte_T3_Rover.md`.

## SA9 · Mini-check (inici de la Sessió 2)

**Enunciat (projectar):**
> Escriu una funció `comprova_i_envia()` que **integri** el que ja saps: llegeix un sensor (per exemple `accelerometer.get_x()`), i si el valor supera un llindar que tu decideixis, envia un missatge per ràdio amb `radio.send()`.

**Què mires:** capacitat d'**integrar sense bastida** dos blocs ja apresos per separat (llegir sensor + condicional + ràdio) en una sola funció pròpia; que el llindar sigui una constant raonada, no un número a l'atzar.
**🟢** integra els tres blocs sense ajuda · **🟡** els tres blocs hi són però amb estructura confusa (p. ex. `radio.on()` oblidat) · **🔴** no sap combinar sensor i ràdio en una sola funció.
**Reforç 🔴:** repassar per separat SA3 (sensors), SA5/SA8 (ràdio) i tornar-ho a intentar abans del repte lliure.

---

> Tots els mini-checks alimenten el **full de seguiment** de l'alumnat i són la font de l'indicador trimestral «distribució de semàfors dels mini-checks» de `Programació didàctica/06b_Avaluacio_programacio_i_practica_docent.md` §1 (llindar d'alerta: ≥ ⅓ de 🟡/🔴 en un check → repesca col·lectiva de 10').
