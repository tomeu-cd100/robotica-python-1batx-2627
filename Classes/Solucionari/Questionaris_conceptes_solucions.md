# Solucionari dels qüestionaris de conceptes (SA1-SA9)

> **Material del docent.** Claus de correcció dels 9 qüestionaris de conceptes (`Classes/SAn/SAn_questionari_conceptes.md`), amb les notes de per què està triada cada pregunta de traça, de completar codi o de corregir codi. Viuen aquí i no als fitxers d'alumnat perquè aquells es publiquen a la vista alumnat del web.

> Els qüestionaris són **formatius: no qualifiquen mai** (`Programació didàctica/06_Avaluacio_criteris_qualificacio.md` §6.2). Es fan com a deures en acabar cada SA i es tornen a fer com a repàs abans de la prova del trimestre. Al Google Classroom hi ha una versió **Google Form autocorrectiva** de cada un: allà l'alumnat rep la correcció automàticament en enviar-lo.

---

## SA1 · Qüestionari de conceptes (què és un robot i la placa micro:bit)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | c | a | b | a | c | b | a | b | b |

La pregunta 1 (traça) es corregeix perquè cal llegir el codi sencer (bucle, condicional i `sleep`) i deduir el comportament real, no recordar una definició de "robot".

La pregunta 3 (completar) es corregeix perquè demana identificar quina instrucció (`display.show`) produeix l'efecte descrit —una imatge fixa després del text—, en lloc de repetir de memòria la definició de "sistema embegut".

La pregunta 10 (corregir) es corregeix perquè reprodueix l'error freqüent real d'aquesta SA (falta el `while True:`, vegeu `SA1_guia_docent.md`, taula «Errors freqüents») i obliga a raonar sobre l'execució del codi, no a recitar les fases del mètode de projecte.

La pregunta 11 és oberta: valora que aparegui **un** sensor, **una** decisió i **un** actuador coherents amb l'aparell triat.

---

## SA2 · Qüestionari de conceptes (sortides digitals, PWM i actuadors)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | c | c | b | b | a | b | a | b | b |

La pregunta 1 (TRAÇA) substitueix una pregunta de pur record de la instrucció; ara cal llegir un bucle real amb `write_digital` i un acumulador i predir què mostra, no només recordar el nom de la funció.

La pregunta 6 (CORREGIR) substitueix la definició memorística d'"acumulador" per l'error freqüent documentat a la guia docent ("el comptador no avança perquè s'inicialitza dins del bucle"): l'alumnat ha de localitzar-lo en codi, no repetir-ne la definició.

La pregunta 8 (COMPLETAR) substitueix la definició memorística de "relé" per la necessitat de completar la línia que el torna a obrir (`write_digital(0)`), aplicant directament el patró tanca/obre del repte «semàfor o llum d'ambient».

La pregunta 11 és oberta: valora que la diferència digital/PWM sigui correcta (dos estats vs valors intermedis) i que els dos exemples siguin coherents amb components reals de la SA2 (per exemple, LED verd/ambre/vermell = digital; respiració o intensitat = PWM).

---

## SA3 · Qüestionari de conceptes (entrades digitals, analògiques i sensors)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | b | a | b | b | b | b | b | a | b |

La pregunta 1 (**TRAÇA**) substitueix una pregunta merament memorística per exigir seguir l'execució d'un codi real (comptador amb *pull-up*) i triar què fa, no només reconèixer una instrucció aïllada. Nota per al docent: aquest fragment **no** té antirebot (a diferència de `mascota_reactiva.py`), així que en una premuda llarga pot incrementar `comptador` diverses vegades; és exactament el problema de sobrecomptatge per rebot que la SA ensenya a resoldre amb `running_time()`, i es pot aprofitar la pregunta per obrir aquest debat a classe encara que no formi part de les opcions de resposta.

La pregunta 3 (**COMPLETAR**) substitueix la llista memorística de pins ADC per demanar completar la línia que falta a `mapa()`, comprovant que l'alumnat entén per què cal un `return` amb la regla de tres, no només que existeix la funció.

La pregunta 9 (**CORREGIR**) substitueix el fet aïllat del PIR per un error real i freqüent (confondre l'escala 0-255 dels sensors integrats amb la 0-1023 dels pins ADC, documentat a la guia docent), i obliga a diagnosticar-lo sobre codi complet.

La pregunta 11 és oberta: valora que expliqui que un llindar "inventat" pot no funcionar amb les condicions reals de l'aula (llum ambiental, soroll de fons...) i que l'exemple sigui coherent amb un component real de la SA3 (llindar de foscor, de temperatura, de so o de distància).

---

## SA4 · Qüestionari de conceptes (funcions, paràmetres, servo, PWM del motor)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| a | b | b | b | b | a | a | a | c | a |

La pregunta 1 (traça de codi) substitueix una pregunta merament memorística per una de lectura activa: valora que l'alumnat entengui que una crida posterior (`girar('dreta')`) **sobreescriu** l'estat que havia deixat una crida anterior (`avancar()`) sobre el mateix pin, no que els valors "se sumin" ni que quedin fixats per sempre.

La pregunta 7 (completar codi) comprova que l'alumnat sap identificar quina instrucció **falta** perquè un fragment funcioni com cal, no només reconèixer-la quan ja hi és: `set_analog_period(20)` és el pas que sovint s'oblida abans d'un `write_analog` sobre un servo.

La pregunta 10 (corregir codi) es basa en un error freqüent real (guia docent, Sessió 2): enviar PWM als **dos** pins del mateix motor alhora. Valora que l'alumnat sàpiga localitzar l'error concret, no només recitar la norma general.

La pregunta 11 és oberta: valora que expliqui la idea d'**abstracció** (un nom que expressa la intenció, "avançar", amaga el detall de pins i PWM) i que el codi principal (`seguent_moviment()`) es pugui llegir com una seqüència d'ordres senzilles en lloc d'un bloc llarg de `write_analog`/`write_digital`.

---

## SA5 · Qüestionari de conceptes (ràdio, grup, protocol, esdeveniment)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | b | c | b | b | a | a | b | b | a |

La pregunta 3 (traça) demana seguir l'execució real d'un `if`/`elif` amb `is_pressed()`/`was_pressed()`: valora que l'alumnat distingeixi que amb només el botó B premut s'entra a la branca `elif button_b.was_pressed()`, no a la del A+B ni a la del A sol.

La pregunta 6 (completar) comprova que l'alumnat identifica **quina crida concreta** falta (`radio.config(group=GRUP)`) per activar el filtre de grup, no només que en sap la definició de memòria.

La pregunta 7 (corregir) es basa en l'error freqüent documentat a la guia docent ("el `PREFIX` no coincideix exactament entre comandament i receptor"): valora que l'alumnat sàpiga localitzar una discrepància concreta de text (majúscules) dins de codi que, a simple vista, sembla correcte.

La pregunta 11 és oberta: valora que expliqui la idea de **reutilització**/modularitat (les funcions `avancar`/`girar`/`aturar` ja estaven provades i funcionaven a la SA4; només cal canviar **l'entrada** que les crida, dels botons a la ràdio) i que reconegui l'avantatge de no haver de tornar a depurar una lògica ja validada.

---

## SA6 · Qüestionari de conceptes (llaç obert/tancat, FSM, histèresi, STOP prioritari)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | c | b | b | b | b | b | b | a | a |

La pregunta 8 és de **traça de codi**: valora que sàpiga seguir pas a pas una transició d'estat condicionada (el mateix patró que `termostat_histeresi.py`), sense executar-lo, no només recordar-ne la definició de memòria.

La pregunta 9 és de **completar codi**: valora que identifiqui que sense `global estat` la funció crea una variable local pròpia i el canvi no es propaga a la variable de fora, tal com passa a `actualitza_estat()` de `vehicle_seguretat.py`.

La pregunta 10 és de **corregir codi**: en aquest fragment concret el bucle és seqüencial (sense `return`/`continue`) i el polsador SÍ es llegeix a cada volta, així que no hi ha cap finestra real en què quedi "ignorat". El que cal reconèixer és una mala pràctica de **prioritat**: la convenció de seguretat d'aquesta SA és comprovar sempre l'aturada d'emergència **primer**, abans de processar qualsevol altra comanda (vegeu "Errors freqüents i solució" de la guia docent), perquè un canvi futur al bloc de la ràdio (per exemple, afegir-hi un `continue` o un `return` anticipat en alguna branca) no acabi deixant el polsador sense comprovar-se. No és un bug demostrable amb aquest codi tal com està escrit, sinó un disseny fràgil que trenca la convenció de seguretat del curs.

La pregunta 11 és oberta: valora que expliqui que l'STOP s'ha de comprovar **abans que res** a cada volta del bucle i que **totes** les vies (polsador i ràdio) criden la mateixa funció, de manera que mai hi ha un moment en què el vehicle pugui "ignorar" una ordre d'aturada perquè estava processant-ne una altra.

---

## SA7 · Qüestionari de conceptes (cinemàtica diferencial, llindars, time-of-flight, missions)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | b | b | c | b | c | b | d | b | a |

La pregunta 1 (traça de codi) avalua que l'alumnat sàpiga llegir un fragment real de `missio_quadrat()` i predir el comportament resultant (una trajectòria en quadrat), en lloc de limitar-se a recitar la definició de cinemàtica diferencial.

La pregunta 4 (completar codi) avalua que l'alumnat entengui la seqüència exacta del pols de trigger de l'HC-SR04 (0 → 1 → 0) prou bé com per identificar quina línia hi falta, no només que en sàpiga la definició de manual.

La pregunta 10 (corregir codi) avalua que l'alumnat reconegui un error real i freqüent (un `except:` massa genèric que amaga bugs de programació, en lloc de capturar només el timeout amb `except OSError:`), tal com es descriu a la guia docent de la S3.

La pregunta 11 és oberta: valora que expliqui que el mètode de mesura (pols de trigger + `machine.time_pulse_us` a l'echo + càlcul distància = temps × velocitat del so / 2) és **idèntic** als dos programes; només canvien els pins concrets (P14/P15 a la SA3, P1/P2 al rover), perquè al rover aquests dos pins vells ja estan ocupats pels motoreductors.

---

## SA8 · Qüestionari de conceptes (I2C, telemetria, protocol, IA aplicada al control)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| a | b | a | b | a | b | b | b | b | b |

La pregunta 1 (COMPLETAR) substitueix el record memorístic de "com es connecta l'IMU per I2C" per la necessitat de completar la línia que el desperta (`i2c.write(MPU_ADR, bytes([MPU_REG_PWR, 0x00]))`), aplicant directament el patró d'inicialització de `mpu_inicia()`.

La pregunta 3 (CORREGIR) substitueix la definició memorística del mecanisme de lectura del DHT11 per l'error freqüent documentat a la guia docent ("el DHT11 retorna sempre `None` perquè es llegeix massa sovint"): l'alumnat ha de localitzar-lo en codi, no repetir-ne la definició.

La pregunta 6 (TRAÇA) substitueix la pregunta de pur record ("quants estats alhora") per haver de llegir un fragment real de la FSM i predir quin és l'estat final, reforçant que `estat` és una variable de decisió pròpia (no una lectura de sensor) i que només en pren un valor cada volta.

La pregunta 11 és oberta: valora que expliqui que totes dues funcions fan servir `machine.time_pulse_us` per mesurar **quant de temps** dura un senyal digital (un pols) i que, a partir d'aquesta durada, en dedueixen una magnitud (distància o bit de dades): el mecanisme de mesura és el mateix, encara que el que se'n dedueix i el nombre de polsos mesurats (1 a l'HC-SR04, 40 al DHT11) sigui diferent.

---

## SA9 · Qüestionari de conceptes (mètode de projecte, integració, documentació, ètica/ODS)

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| b | a | b | c | b | a | b | a | b | b |

La pregunta 11 és oberta: valora que expliqui que a la SA9 no s'introdueix cap component "nou i obligatori per a tothom" (com el DHT11 a SA6 o l'IMU a SA8), sinó que cada alumne **combina** components i tècniques ja après en SA anteriors (sensors, FSM, motors, ràdio) en una solució pròpia coherent: el saber nou és **com integrar-los**, no un component concret.

La pregunta 5 (CORREGIR) substitueix l'antiga pregunta sobre els nivells ⭐/⭐⭐/⭐⭐⭐ (record purament memorístic) per un error real recollit a la guia docent (Sessió 2: "el prototip barreja tota la lògica dins del `while True`, sense `percep()`/`decideix()`/`actua()`"): cal que l'alumnat sàpiga identificar-lo llegint codi, no només recitar-ne el motiu.

La pregunta 6 (COMPLETAR) substitueix l'antiga pregunta sobre els indicadors de la R4·DO (fet aïllat, sense codi) per una traça de la FSM del repte de reg: cal saber que `decideix()` només canvia d'estat i mai actua directament sobre el relé (aquest matís és el que distingeix la resposta correcta de la distractora b).

La pregunta 10 (TRAÇA) manté el tema original (integrar temperatura i CO₂ en una alerta combinada) però ara amb codi real: cal distingir una condició `and` d'una `or` llegint `decideix()`, en lloc de triar entre frases abstractes sobre "quins blocs s'integren".

---

*Solucionari dels qüestionaris de conceptes. Es manté sincronitzat amb els `SAn_questionari_conceptes.md` de cada SA: si canvia una pregunta, canvia la clau. Llicència CC BY-SA 4.0.*
