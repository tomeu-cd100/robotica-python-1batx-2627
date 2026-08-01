# Reptes SA8 · Autonomia i telemetria

> 🧑‍🎓 **Quan toca fer-ne un?** És l'**ampliació ⭐** de la SA: comença'l quan tinguis el **nucli al dia** (el sistema de telemetria de la S3, tancat). Ensenya'l al docent perquè el validi.

**Fes els reptes en ordre de dificultat: comença per ⭐, i si arribes a ⭐⭐⭐ hauràs passat pels tres.** Tots parteixen dels programes de `Classes/SA8/codi/` i fan servir el concepte de protocol de telemetria amb prefix propi, sensors del Kit 3 (IMU MPU6050, DHT11) i registre amb llista/mitjana o amb `log`. Es fan **sempre amb maquinari real** (el rover i una segona placa): el simulador de python.microbit.org **sí** simula la ràdio i el mòdul `log` (entre dues instàncies obertes alhora), però **cap** sensor del Kit 3, vegeu [`SA8_esquemes_connexions.md`](../Classes/SA8/SA8_esquemes_connexions.md) §Simulació.

> **Continguts SA8:** IMU MPU6050 (I2C), DHT11 (time-of-flight amb `machine.time_pulse_us`), protocol de telemetria amb prefix, arquitectura de prioritats (FSM), registre amb llista/mitjana i amb `log`. · **Vocabulari/bases:** `Classes/SA0/`.

> **Format "producte real":** cada repte simula un **encàrrec** amb **client**, **lliurable** i **ús al món real**. El requisit tècnic no canvia; el marc ajuda a donar sentit al producte.

> 🎛️ **Recorda:** el codi i el producte de cada repte són **teus**, com a tota la SA8. Si el repte necessita una segona placa (estació base), l'escrius **tu** encara que corri temporalment en una altra micro:bit.

---

## ⭐ Repte 1 · Estació meteorològica escolar amb alertes

**Context.** La coordinació de manteniment d'un institut vol un petit sensor mòbil que avisi quan la temperatura d'una aula o d'un magatzem surt d'un rang segur, sense haver de mirar constantment cap pantalla.

> *Client: coordinació de manteniment del centre · Lliurable: telemetria amb alerta de temperatura per ràdio · Món real: sensors IoT de sales de servidors o magatzems que avisen quan la temperatura surt de rang.*

**Què treballa.** Protocol de telemetria amb prefix, DHT11, llindar de temperatura, `telemetria_radio.py`.

**Requisit mínim.**
- Parteix de `telemetria_radio.py`: manté la lectura del DHT11 i de l'IMU MPU6050 (ja fetes).
- Afegeix un **llindar de temperatura** (`LLINDAR_TEMP_ALTA`) i un nou camp al missatge de telemetria (`"AL:1"` si se supera, `"AL:0"` si no).
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Mostra al display, amb `display.show()`, una icona diferent quan hi ha alerta activa i quan no n'hi ha.
2. *(notable)* Compta amb una variable quantes vegades s'ha activat l'alerta des que es va engegar la placa, i mostra-ho per REPL amb `print()` en prémer A+B.
3. *(⭐⭐⭐)* Afegeix **histèresi** a l'alerta (dos llindars, com `termostat_histeresi.py` de la SA6) perquè no "parpellegi" quan la temperatura balla just al voltant del llindar.

    **Fites** (valida-les en ordre):
    1. El nucli de telemetria (IMU+DHT11+ràdio) funciona igual que abans si no es toca res més.
    2. El camp `"AL:"` (requisit mínim) apareix correctament al missatge i canvia quan la temperatura creua el llindar.
    3. La histèresi (ampliació 3) evita que l'alerta canviï d'estat més d'un cop quan la temperatura es manté estable a prop del llindar.

---

## ⭐⭐ Repte 2 · Estació base multisensor amb registre avançat

**Context.** Un projecte de ciència ciutadana d'un institut vol una petita estació receptora que no només mostri l'última lectura rebuda, sinó també els valors màxim i mínim registrats durant tota la sessió, per detectar variacions extremes.

> *Client: projecte de ciència ciutadana del centre · Lliurable: estació base amb estadístiques (mitjana, màxim, mínim) i navegació de camps amb botons · Món real: panells de control de xarxes de sensors ambientals.*

**Què treballa.** Anàlisi de missatges (`analitza()`), llista + mitjana, estadístiques bàsiques, `estacio_base.py`.

**Requisit mínim.**
- Parteix de `estacio_base.py`: manté `analitza()` i el registre amb `log` (ja fets).
- Afegeix el seguiment del valor **màxim** i **mínim** de temperatura rebuts (dues variables noves, actualitzades a cada missatge vàlid).
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Amb els botons A/B, permet a qui mira l'estació base **navegar** entre "última lectura", "mitjana" i "màxim/mínim" al display (`display.scroll()`).
2. *(notable)* Registra amb `log.add()` un camp addicional que indiqui si la lectura ha establert un nou rècord (màxim o mínim), a més dels camps ja existents.
3. *(⭐⭐⭐)* Detecta quan fa **més de N segons** que no arriba cap missatge nou (amb `running_time()`) i mostra una icona d'"estació sense senyal", per distingir un rover aturat d'un problema de ràdio.

    **Fites** (valida-les en ordre):
    1. El registre amb `log` (herència d'`estacio_base.py`) segueix funcionant exactament igual, sense cap regressió.
    2. El màxim i el mínim (requisit mínim) són correctes després de rebre almenys 5 lectures de prova.
    3. La detecció de "sense senyal" (ampliació 3) només s'activa quan realment ha passat el temps configurat, no just després d'un missatge rebut.

---

## ⭐⭐⭐ Repte 3 · Missió telemetrada amb alerta d'emergència per gest

**Context.** Una empresa de logística interna vol un rover de repartiment que, a més d'informar contínuament del seu estat, permeti a l'operari aturar-lo d'emergència amb una simple sacsejada del comandament (sense necessitat d'un polsador físic al rover), i que quedi constància de cada aturada d'emergència al registre.

> *Client: servei de logística interna d'un campus · Lliurable: rover telemetrat amb alerta d'emergència per gest, registrada amb `log` · Món real: robots de repartiment i drons amb aturada d'emergència remota i registre d'incidències.*

**Què treballa.** Integració FSM + telemetria + gest (`accelerometer.was_gesture`), protocol bidireccional, `telemetria_radio.py` + `estacio_base.py`.

**Requisit mínim.**
- Parteix de `telemetria_radio.py`: manté el polsador STOP físic, la FSM i la telemetria (ja fets).
- Afegeix la detecció d'una **sacsejada** (`accelerometer.was_gesture("shake")`) sobre la **pròpia** IMU del rover que, en detectar-se, aturi el rover immediatament (mateixa prioritat que el polsador STOP) i enviï un missatge especial (`"TEL:ALERTA_STOP"`).
- A `estacio_base.py`, mostra una icona diferent i clarament identificable quan arriba aquest missatge d'alerta.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Registra amb `log.add()` cada alerta d'emergència, amb l'instant (`running_time()`) en què s'ha disparat.
2. *(notable)* Mostra per REPL (`print()`), a `estacio_base.py`, quantes alertes d'emergència s'han rebut des que es va engegar la placa.
3. *(⭐⭐⭐)* Fes el protocol **bidireccional**: `estacio_base.py` envia un missatge `"CMD:S"` (mateix prefix que la SA5/SA6) quan es prem el botó A, i `telemetria_radio.py` l'escolta a més dels seus propis sensors, aturant el rover a distància sense necessitat de sacsejada ni polsador físic.

    **Fites** (valida-les en ordre):
    1. El polsador STOP físic (herència de `telemetria_radio.py`) segueix funcionant exactament igual, sense cap regressió.
    2. La sacsejada (requisit mínim) atura el rover i envia l'alerta, que `estacio_base.py` mostra de manera inequívoca.
    3. El protocol bidireccional (ampliació 3) atura el rover des de l'estació base sense interferir mai amb els missatges `"TEL:"` normals.

---

## 🎨 Fes-lo teu (tria abans de començar)

> El repte fixa **què** ha de fer el sistema; **el context el poses tu**. Tria i anota-ho al quadern — un producte amb decisions teves sempre s'explica i es defensa millor:
> - **Repte 1:** tria tu el llindar de temperatura i com el distingeixes visualment.
> - **Repte 2:** decideix com organitzes la navegació entre camps al display.
> - **Repte 3:** decideix el disseny del teu protocol bidireccional (quins missatges, amb quina prioritat).

## Material necessari (els tres reptes)

- micro:bit V2 + Micro:shield + cable micro-USB, individual.
- El **rover T3** amb DHT11 i IMU MPU6050 muntats, per als reptes 1 i 3.
- Una segona micro:bit (d'un company, per torns, o del docent) per fer d'estació base, per als tres reptes.
- El simulador de python.microbit.org **sí** simula la ràdio i el mòdul `log` (2 instàncies obertes alhora): útil per assajar el protocol; **no** simula cap sensor del Kit 3.

## Per on començar (mètode de projecte + PRIMM)

1. **Analitzar:** quina part del programa base ja tinc feta i puc reutilitzar (protocol, FSM, registre), i quina lògica nova necessito?
2. **Dissenyar (Predir):** dibuixa o descriu el nou camp/comportament *abans* d'escriure el codi.
3. **Programar/Prototipar:** parteix del programa base de `Classes/SA8/codi/` i modifica'l.
4. **Provar:** executa'l amb el rover i l'estació base reals, observa, compara amb el teu disseny.
5. **Millorar:** afegeix una ampliació i documenta-la.

## Com s'avalua

| Rúbrica | Per què |
|---|---|
| **R1** (codi) | Funcionament, disseny del protocol, depuració. |
| **R3** (criteri "Integració") | Sensors i ràdio ben integrats, protocol coherent entre emissor i receptor. |
| **R4** (documentació) | Quadern tècnic: format de missatge, predicció, solució i millora. |

## Producte / entrega

- Codi `.py` comentat (emissor i, si cal, receptor) + entrada al **quadern tècnic** (format de missatge, predicció, què he fet, error trobat i millora).

---

## Orientació docent

- **Errors freqüents:** `group`/`PREFIX` diferents entre emissor i receptor; enviar telemetria a cada volta del bucle en lloc de cada `INTERVAL_TELEMETRIA_MS`; oblidar comprovar la llista buida abans de calcular una mitjana.
- **Diferenciació:** el mínim és idèntic per a tothom → tothom assoleix la base; les ampliacions 2-3 introdueixen estadístiques, registre avançat i protocol bidireccional.
- **Gestió d'aula:** el repte 1 només necessita el rover; el repte 2 se centra en la placa receptora; el repte 3 reaprofita el sistema complet i necessita coordinació de parelles (torns d'estació base).
- **Vincle avaluació:** producte coherent amb el de la SA8 (quadern tècnic, R4/R5) i amb les rúbriques R1/R3 del sistema de telemetria.
