# Reptes SA3 · Entrades: el robot percep

> 🧑‍🎓 **Quan toca fer-ne un?** És l'**ampliació ⭐** de la SA: comença'l quan tinguis el **nucli al dia** (el repte «mascota reactiva» de la S3, tancat). Ensenya'l al docent perquè el validi.

**Fes els reptes en ordre de dificultat: comença per ⭐, i si arribes a ⭐⭐⭐ hauràs passat pels tres.** Tots parteixen dels programes de `Classes/SA3/codi/` i fan servir el Micro:shield. Es fan amb **maquinari real**: el simulador de python.microbit.org **no** reprodueix cap sensor extern (vegeu [`SA3_esquemes_connexions.md`](../Classes/SA3/SA3_esquemes_connexions.md) §Simulació), tot i que la **lògica** es pot escriure i revisar-hi abans de provar-la a la placa.

> **Continguts SA3:** entrades digitals (`is_pressed()`, `read_digital()`), *pull-up*/antirebot, entrades analògiques (`read_analog()`, 0-1023), sensors interns (0-255/graus C), funció `mapa()`, HC-SR04 (temps de vol), PIR, condicionals encadenats. · **Vocabulari/bases:** `Classes/SA0/`.

> **Format "producte real":** cada repte simula un **encàrrec** amb **client**, **lliurable** i **ús al món real**. El requisit tècnic no canvia; el marc ajuda a donar sentit al producte.

---

## ⭐ Repte 1 · Llum automàtica d'estudi

**Context.** Una marca de làmpades d'escriptori vol un prototip que s'encengui sol quan la taula es queda fosca, sense que calgui prémer cap interruptor.

> *Client: fabricant de làmpades d'escriptori · Lliurable: llum automàtica de dos nivells · Món real: enllumenat automàtic d'exteriors i passadissos.*

**Què treballa.** `read_analog()`/`read_light_level()`, funció `mapa()`, condicionals, LED.

**Requisit mínim.**
- Parteix de `nivell_llum.py`: lectura del sensor de llum (intern o extern) i barres al display (ja fet).
- Afegeix un **LED extern** (pin lliure) que s'encengui quan la llum estigui **per sota** del teu `LLINDAR_FOSCOR`, i s'apagui altrament.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Afegeix un **segon llindar** ("molt fosc") que faci parpellejar el LED en lloc de quedar-se fix.
2. *(notable)* Fes que la **intensitat** del LED (PWM, `write_analog`) sigui proporcional a la foscor (com més fosc, més intensitat), amb la funció `mapa()`.
3. *(⭐⭐⭐)* Afegeix un **temporitzador d'apagada** (`running_time()`): un cop s'encén per foscor, es manté encès un temps mínim encara que torni la llum de sobte (evita parpellejos ràpids si algú passa una ombra pel davant).

    **Fites** (valida-les en ordre):
    1. El LED s'encén/apaga de manera **fiable** i repetible amb el llindar calibrat al REPL.
    2. El "molt fosc" es distingeix clarament del "fosc normal" (parpelleig vs fix).
    3. El temporitzador de l'ampliació 3 evita almenys un parpelleig ràpid provocat expressament.

---

## ⭐⭐ Repte 2 · Aparcament amb sensor de distància

**Context.** Un taller mecànic vol un petit indicador d'aparcament: com més a prop estàs de la paret, més ràpid avisa, com els sensors d'aparcament dels cotxes reals.

> *Client: taller mecànic / instal·lador d'accessoris de garatge · Lliurable: indicador de distància amb avís progressiu · Món real: sensors d'aparcament, robots que eviten obstacles.*

**Què treballa.** HC-SR04 (`machine.time_pulse_us`), càlcul de distància, condicionals encadenats, `music`.

**Requisit mínim.**
- Parteix de `alarma_ultrasons.py`: mesura de distància i alarma sonora simple (ja fet).
- Substitueix l'alarma única per **tres zones** (per exemple, > 30 cm "lluny", 15-30 cm "atenció", < 15 cm "molt a prop"), cadascuna amb un so o ritme diferent.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Mostra la **distància aproximada** (en desenes de cm) al display a cada zona, no només el so.
2. *(notable)* Fes que el **ritme** dels avisos sonors s'acceleri progressivament com més a prop estiguis (no només tres nivells fixos, sinó un `sleep()` entre avisos que depèn de la distància).
3. *(⭐⭐⭐)* Encapsula cada zona en una **funció pròpia** (`zona_lluny()`, `zona_atencio()`, `zona_perill()`) cridada des del `while True:` segons la distància mesurada.

    **Fites** (valida-les en ordre):
    1. Les tres zones es distingeixen clarament pel so (no cal mirar el display per saber en quina zona estàs).
    2. La distància mostrada al display (ampliació 1) és coherent amb la zona activa.
    3. El `while True:` queda reduït a poques línies que criden funcions, sense repetir la lògica de cada zona.

---

## ⭐⭐⭐ Repte 3 · Estació meteorològica de butxaca

**Context.** Una empresa d'articles escolars vol un prototip d'estació meteorològica senzilla: llegeix llum i temperatura reals i mostra un "resum del dia" combinant totes dues lectures, com faria una icona de previsió del temps.

> *Client: empresa d'articles escolars / educatius · Lliurable: mini estació meteorològica de butxaca · Món real: estacions meteorològiques domèstiques, apps de previsió del temps.*

**Què treballa.** Múltiples entrades analògiques (llum i temperatura), condicionals encadenats amb diverses condicions, funcions, memòria de l'estat anterior.

**Requisit mínim.**
- Parteix de `nivell_llum.py` i `termometre.py`: lectura de llum i temperatura (ja fet).
- Combina totes dues lectures en **almenys 3 "resums"** diferents (per exemple: "sol" = clar i calent, "ennuvolat" = fosc i temperat, "fred" = temperatura baixa independentment de la llum), cadascun amb la seva icona pròpia al display.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Afegeix un **cinquè "resum"** propi (amb el teu propi criteri de llum+temperatura) i justifica'l al quadern.
2. *(notable)* Fes que el resum **només canviï** quan l'estat és estable durant almenys 2 segons seguits (evita "parpellejar" d'un resum a un altre per una lectura puntual estranya).
3. *(⭐⭐⭐)* Afegeix el **PIR** com a "sensor de vent simulat": si detecta moviment sobtat, mostra un avís curt de "ràfega" per sobre del resum normal, i després torna al resum que tocava.

    **Fites** (valida-les en ordre):
    1. Els 3 resums mínims es distingeixen clarament amb icones diferents i reaccionen a canvis reals de llum/temperatura.
    2. L'estabilitat de l'ampliació 2 es pot demostrar tapant/destapant el sensor ràpidament sense que "parpellegi" el resum.
    3. L'avís de "ràfega" (ampliació 3) no substitueix permanentment el resum: torna a l'estat normal en acabar.

---

## 🎨 Fes-lo teu (tria abans de començar)

> El repte fixa **què** ha de fer el sistema; **el context el poses tu**. Tria i anota-ho al quadern — un producte amb decisions teves sempre s'explica i es defensa millor:
> - **Repte 1:** decideix els teus **llindars** de foscor i "molt fosc" i per què.
> - **Repte 2:** tria les teves **tres distàncies** de zona i el to de cada avís.
> - **Repte 3:** tria els teus **criteris** de "resum" (què vol dir "sol", "ennuvolat"... per a tu) i les icones.

## Material necessari (els tres reptes)

- micro:bit V2 + Micro:shield + cable micro-USB.
- Kit Keyestudio 1 (polsador) i Kit 2 (sensor de llum, sensor de temperatura, HC-SR04, PIR), muntats segons [`SA3_esquemes_connexions.md`](../Classes/SA3/SA3_esquemes_connexions.md).
- El simulador de python.microbit.org **només** serveix per revisar la lògica (condicionals, temps): els sensors externs cal provar-los amb maquinari real.

## Per on començar (mètode de projecte + PRIMM)

1. **Analitzar:** quins sensors necessito i quina és la seva escala (0-255, 0-1023, graus C, temps de vol)?
2. **Dissenyar (Predir):** escriu *abans* quins llindars creus que necessitaràs, i mesura'ls després amb el REPL.
3. **Programar/Prototipar:** parteix del programa base de `Classes/SA3/codi/` i modifica'l.
4. **Provar:** executa'l amb el maquinari real, observa, compara amb la teva predicció.
5. **Millorar:** introdueix funcions i una ampliació.

## Com s'avalua

| Rúbrica | Per què |
|---|---|
| **R1** (codi) | Funcionament, estructura, llegibilitat, depuració. |
| **R2** (circuit) | Muntatge correcte i segur dels sensors. |
| **R4** (documentació) | Quadern tècnic: predicció, solució i millora. |
| **R5** (actitud) | Autonomia, gestió de l'error. |

## Producte / entrega

- Codi `.py` comentat + entrada al **quadern tècnic** (predicció, què he fet, error trobat i millora).

---

## Orientació docent

- **Errors freqüents:** confondre l'escala 0-255 (sensors interns) amb la 0-1023 (pins ADC); triar llindars sense mesurar-los al REPL; oblidar l'antirebot al polsador; connectar un component analògic a un pin sense ADC.
- **Diferenciació:** el mínim és idèntic per a tothom → tothom assoleix la base; les ampliacions 2-3 introdueixen funcions, temporitzadors i memòria de l'estat anterior per a qui va sobrat.
- **Gestió d'aula:** tots requereixen maquinari real per a la part de sensors externs (el simulador només valida la lògica); el repte 2 reaprofita el muntatge de `alarma_ultrasons` de la S3.
- **Vincle avaluació:** producte coherent amb el de la SA3 (quadern tècnic, R4/R5) i amb les rúbriques R1/R2/R3 del repte «mascota reactiva».
