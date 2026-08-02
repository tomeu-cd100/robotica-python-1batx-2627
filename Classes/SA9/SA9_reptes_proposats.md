# SA9 · Banc de reptes proposats

> 🧑‍🎓 **Quan toca triar-ne un?** A la **Sessió 1 (Idear)**. Aquest banc **no és una llista de repte extra** com a la resta de SA: aquí **el repte és el projecte mateix** de la SA9 — el tries un cop, individualment, i el desenvolupes durant les 4 sessions de projecte (S1-S4).

> **Tots són INDIVIDUALS i viables amb 1 rover + els kits d'un sol alumne** (micro:bit V2 + Micro:shield + rover de SA7-SA8 + Kits Keyestudio 1-3). El maquinari de cada repte surt **únicament** de [`09c_Inventari_kits_disponibles.md`](../../Programació%20didàctica/09c_Inventari_kits_disponibles.md); res de compra addicional ni de núvol.

> **Si vols proposar un repte propi** (no d'aquesta llista), parla-ho amb el docent a la Sessió 1: ha de ser individual, viable amb el maquinari de `09c` i integrar almenys dos blocs del curs (programació + electrònica + control + robòtica mòbil + telemetria).

---

## ⭐ Repte 1 · Reg automàtic d'una planta

**Objectiu.** El rover (o una estació fixa muntada amb el Micro:shield) rega una planta automàticament quan el terra està massa sec, sense intervenció humana.

**Maquinari necessari (Kit 2 + Kit 3).** Sensor d'humitat del terra (Kit 2, analògic) + mòdul relé (Kit 3) + bomba d'aigua amb tub (Kit 3).

**Esquema de components.** Sensor d'humitat del terra → pin analògic lliure: en estació fixa, **P0**; al rover (on P0 és del seguidor de línia), **P4**, i llavors cal `display.off()` perquè P3/P4/P10 comparteixen circuit amb el display. Relé → pin digital lliure **no compartit amb el display** (p. ex. **P12**); la bomba es connecta a través del relé, **mai** directament al Micro:shield (el relé commuta l'alimentació externa de la bomba). Alimentació de la bomba: portapiles/font externa, mai des de l'USB.

**Criteris d'èxit.**
- ⭐ Llegeix el sensor d'humitat del terra i mostra la lectura (display o REPL).
- ⭐⭐ Activa el relé (i la bomba) quan la humitat baixa d'un llindar, i l'atura quan el supera; sense oscil·lar contínuament.
- ⭐⭐⭐ Afegeix **histèresi** (dos llindars, com `termostat_histeresi.py` de SA6) i registra amb el mòdul `log` cada cop que s'ha regat (instant + lectura).

**Codi del curs que es reutilitza.** Lectura analògica (`read_analog()`, SA3), relé i sortides digitals (SA2/SA6), FSM amb histèresi (`termostat_histeresi.py`, SA6), registre amb `log` (SA6/SA8).

---

## ⭐⭐ Repte 2 · Rover missatger guiat

**Objectiu.** El rover porta un "missatge" (un objecte lleuger, o simplement una notificació) fins a un punt marcat, guiat per ràdio des d'un comandament (una segona placa), i confirma l'entrega.

**Maquinari necessari (Kit 2).** Rover de SA7-SA8 (motors, seguidor de línia, HC-SR04); brunzidor o LED (Kit 1/3) per confirmar l'entrega; segona micro:bit com a comandament (d'un company, per torns, o del docent, com a SA5/SA8).

> 🎛️ **Dues plaques, treball individual.** Com a SA5/SA8: el codi de les **dues** plaques l'escriu **cada alumne**; la segona placa (comandament) s'obté per **emparellament puntual** amb un company (per torns) o amb el docent — és només un **banc de proves**, mai un producte compartit.

**Esquema de components.** Sense pins nous respecte al rover heretat; el comandament envia ordres per ràdio amb un protocol propi (`"CMD:"`, com a SA5/SA6); el rover confirma l'entrega amb el brunzidor/LED ja cablejat i, opcionalment, envia telemetria de tornada (`"TEL:"`, com a SA8).

**Criteris d'èxit.**
- ⭐ El rover es mou teleoperat per ràdio (endavant/enrere/gir/atura) amb el protocol de SA5.
- ⭐⭐ Detecta que ha arribat al punt d'entrega (per exemple, amb l'HC-SR04 davant d'un obstacle marcat, o un temps/distància recorreguts) i ho confirma (so/llum).
- ⭐⭐⭐ Envia telemetria de confirmació per ràdio al comandament (`"TEL:ENTREGAT"`), amb registre de l'hora d'entrega (`log`).

**Codi del curs que es reutilitza.** Funcions de moviment (SA4/SA7), protocol de ràdio (SA5/SA6), HC-SR04 (SA3/SA7), telemetria (SA8).

---

## ⭐⭐ Repte 3 · Sentinella amb PIR

**Objectiu.** El rover (o una estació fixa) vigila una zona i alerta quan detecta moviment, com un sistema de seguretat domèstic senzill.

**Maquinari necessari (Kit 2 + Kit 3).** Sensor PIR (Kit 2) + LED RGB o brunzidor (Kit 1/3) per a l'alarma; ràdio interna per enviar l'alerta a una segona placa (estació de vigilància, com a SA8).

**Esquema de components.** PIR → pin digital lliure **no compartit amb el display** (p. ex. **P8** si no hi ha DHT11 muntat, o **P12**; evita P3/P4/P10, que són del display); en detectar moviment, activa l'alarma local (LED/so) i envia un missatge de telemetria d'alerta (`"TEL:ALERTA_PIR"`) a l'estació base.

**Criteris d'èxit.**
- ⭐ Detecta moviment amb el PIR i ho mostra al display.
- ⭐⭐ Activa una alarma local (llum/so) durant un temps fix quan detecta moviment, sense repetir l'alarma contínuament mentre hi ha moviment sostingut.
- ⭐⭐⭐ Envia l'alerta per ràdio a una estació base (el teu propi `estacio_base.py`, com a SA8) que en porta un registre amb `log` (instant de cada alerta).

**Codi del curs que es reutilitza.** Entrades digitals (SA3), FSM amb temporització (SA6/SA8), protocol i telemetria per ràdio (SA5/SA8), registre amb `log` (SA6/SA8).

---

## ⭐ Repte 4 · Indicador ambiental amb tira NeoPixel

**Objectiu.** Un indicador lluminós (semàfor ambiental) que combina dues magnituds (per exemple, temperatura i llum) en un codi de colors fàcil d'interpretar d'un cop d'ull.

**Maquinari necessari (Kit 2 + sensors interns).** Tira LED adreçable WS2812B/NeoPixel (Kit 2, reserva SA9); sensor de temperatura i de llum (interns de la micro:bit, o DHT11 del Kit 3).

**Esquema de components.** Tira NeoPixel → pin digital lliure (p. ex. **P8** en estació fixa, o **P12**; els pins 17-18 de l'edge connector són de 3V, no GPIO), mòdul `neopixel` (com preveu `09c`); sensors de temperatura/llum sense cablatge addicional (interns) o DHT11 a P8 si el rover ja el porta muntat (SA6/SA8).

**Criteris d'èxit.**
- ⭐ Llegeix dues magnituds ambientals i les mostra per REPL.
- ⭐⭐ Tradueix la combinació de magnituds a un color de la tira NeoPixel (per exemple, verd = confortable, groc = alerta, vermell = crític), amb almenys 3 nivells.
- ⭐⭐⭐ Afegeix histèresi entre nivells (evita parpelleig) i registra amb `log` cada canvi de nivell.

**Codi del curs que es reutilitza.** Sortides PWM/digitals (SA2), sensors interns/DHT11 (SA3/SA6/SA8), FSM amb histèresi (SA6), registre amb `log` (SA6/SA8).

---

## ⭐⭐⭐ Repte 5 · Classificador de comportaments amb IA

**Objectiu.** El rover distingeix, amb un model d'IA entrenat (Teachable Machine, com a SA8), entre diversos gestos o sons i respon amb un comportament diferent per a cadascun.

**Maquinari necessari (sensors interns + Kit 3).** Acceleròmetre intern (gestos) o sensor de so (Kit 3, micròfon); rover de SA7-SA8 per executar el comportament resultant.

**Esquema de components.** Sense pins nous si es fa servir l'acceleròmetre intern o el **micròfon intern de la V2** (`microphone.sound_level()`, ja usat a T1 — l'opció recomanada per al so); si es fa servir el sensor de so extern del Kit 3, cal un pin **ADC** lliure (només P0-P4 i P10 ho són; en estació fixa, P0).

**Criteris d'èxit.**
- ⭐ Distingeix, amb una regla feta a mà (llindar), almenys dos patrons diferents (com `mpu_orientacio()` de SA8).
- ⭐⭐ Entrena un classificador senzill amb Teachable Machine per als mateixos patrons i compara les decisions amb la regla feta a mà.
- ⭐⭐⭐ El rover respon amb un comportament diferent per a cada patró detectat (per exemple, gest 1 → avança, gest 2 → gira) i documenta la reflexió d'IA i ètica de dades (com a SA8).

**Codi del curs que es reutilitza.** Gestos/acceleròmetre (SA1/SA8), sensor de so (SA3), FSM (SA6/SA8), IA aplicada al control i ètica de dades (SA8).

---

## ⭐⭐⭐ Repte 6 · Estació de telemetria ambiental amb alertes combinades

**Objectiu.** Una estació de telemetria que combina diversos sensors avançats del Kit 3 i genera una alerta quan es superen llindars combinats (per exemple, temperatura alta **i** CO₂ alt alhora), enviant-ho per ràdio i registrant-ho.

**Maquinari necessari (Kit 3).** DHT11, BMP280 i/o CCS811 (Kit 3, bus I2C, com a SA8); ràdio interna; segona placa com a estació base.

**Esquema de components.** Sense pins nous respecte a SA8 (DHT11 a P8, bus I2C a P19/P20); l'alerta combinada és lògica de programa, no cablatge nou.

**Criteris d'èxit.**
- ⭐ Llegeix com a mínim dos sensors del Kit 3 i els envia per ràdio amb un protocol propi (com `telemetria_radio.py`).
- ⭐⭐ Genera una alerta quan **dues** condicions es compleixen alhora (per exemple, temperatura > llindar **i** CO₂ > llindar), no per separat.
- ⭐⭐⭐ L'estació base (el teu `estacio_base.py`) distingeix visualment els tres nivells (normal/alerta simple/alerta combinada) i en porta un registre amb `log`.

**Codi del curs que es reutilitza.** Sensors avançats i I2C (SA8), protocol de telemetria (SA8), condicionals combinats (SA3/SA6), registre amb `log` (SA6/SA8).

---

## 🎨 Fes-lo teu (tria abans de començar)

> El repte fixa **què** ha de resoldre el sistema; **el context, els llindars i el disseny concret els poses tu**. Anota-ho al quadern i al dossier — un producte amb decisions pròpies sempre s'explica i es defensa millor.

## Material necessari (comú als sis reptes)

- micro:bit V2 + Micro:shield + cable micro-USB, individual.
- El teu **rover T3** (SA7-SA8), amb els components que ja hi tens muntats.
- Els kits Keyestudio 1-3 propis, segons el repte triat (vegeu cada fitxa).
- El simulador de [python.microbit.org](https://python.microbit.org) **sí** simula la ràdio i el mòdul `log`; **cap** sensor del Kit 2/3 ni els motors s'hi simulen (com a SA7-SA8).

## Com s'avalua

| Rúbrica | Per què |
|---|---|
| **R1** (codi) | Funcionament, estructura, llegibilitat, depuració. |
| **R2** (circuit) | Muntatge del maquinari nou, esquema, seguretat. |
| **R3** (projecte i robot) | Compliment del repte, disseny i iteració, integració, autonomia/control. |
| **R4** (documentació i defensa) | Dossier tècnic + defensa oral individual, nivell alt. |
| **R5** (actitud) | Implicació, gestió de l'error, autonomia, responsabilitat, al llarg del projecte. |

## Producte / entrega

- Rover ampliat amb el repte, funcional + [dossier tècnic](SA9_dossier_plantilla.md) complet + defensa oral individual (S4).

---

## Orientació docent

- **Diferenciació:** els sis reptes tenen el mateix format ⭐/⭐⭐/⭐⭐⭐ (nucli assolible per a tothom, ampliacions per a qui va sobrat); recomana el repte 1 o 4 a qui necessiti bastida (llindar únic, sense protocol de ràdio) i el 5 o 6 a qui vagi sobrat.
- **Gestió d'aula:** els reptes 1, 3 i 4 necessiten muntatge nou (relé+bomba, PIR, NeoPixel): reserva'n temps a la S2. Els reptes 2 i 6 reutilitzen quasi tot el cablatge de SA7-SA8: es poden centrar més en programació.
- **Vincle amb `09c`:** el repte 1 és l'únic que fa servir la bomba d'aigua; assegura't d'haver-la validada (estanquitat del tub, relé) abans de la S1 perquè l'alumnat que la triï no perdi temps de muntatge.
- **Errors freqüents:** connectar la bomba directament al Micro:shield (sense relé); oblidar la histèresi als llindars (parpelleig); no distingir entre "decisió pròpia" (estat) i "dada externa" (sensor).
