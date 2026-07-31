# 📖 Glossari tècnic català ↔ anglès

> **Per a l'alumnat.** La documentació real de la professió —*datasheets*, fòrums, la referència oficial de MicroPython i de micro:bit— és **en anglès**. Aquest glossari és el pont: el terme en català (com en diem a classe), el terme en anglès (com el trobaràs quan busquis) i què vol dir en una línia.
>
> **Hàbit del quadern:** a cada SA, apunta-hi **3 termes nous** amb les teves paraules, amb l'anglès inclòs (vegeu `Programació didàctica/04_Metodologia.md` §4.5). A final de curs tindràs el teu diccionari d'enginyer/a.

## ⚡ Electrònica

| Català | Anglès | Què és | On surt |
|---|---|---|---|
| pin / connector | *pin* | Punt de connexió del Micro:shield on s'endolla un sensor o actuador | SA1+ |
| polaritat | *polarity* | Sentit correcte de connexió (+/−) d'un component | SA2 |
| massa (GND) | *ground* | Punt de referència de 0 V del circuit | SA1+ |
| massa comuna | *common ground* | Unir els GND de totes les fonts (piles, Micro:shield, sensors) perquè «parlin» amb la mateixa referència | SA4, SA7 |
| tensió | *voltage* | «Pressió» elèctrica entre dos punts (V) | SA2 |
| corrent | *current* | Flux de càrrega que travessa el circuit (A) | SA2 |
| curtcircuit | *short circuit* | Camí directe entre + i − sense càrrega: perill | SA1 |
| resistència de pull-up | *pull-up resistor* | Manté un pin a HIGH quan no hi ha res connectat (la micro:bit en porta d'internes en llegir amb `pull=microbit.PULL_UP`) | SA3 |
| full de característiques | *datasheet* | Document oficial d'un component: límits, pins, corbes | SA2+ |
| controlador de motors | *motor driver* | Circuit del Micro:shield que permet fer girar un motoreductor en tots dos sentits amb prou corrent | SA4 |
| relé | *relay* | Interruptor comandat elèctricament per a càrregues grans | SA2, SA6 |
| brunzidor | *buzzer* | Actuador que fa so | SA2 |
| font d'alimentació | *power supply* | D'on surt l'energia del circuit (USB, portapiles) | SA4 |

## 💻 Programació (MicroPython)

| Català | Anglès | Què és | On surt |
|---|---|---|---|
| variable / constant | *variable / constant* | Nom que guarda un valor que canvia / que no canvia mai | SA2 |
| bucle | *loop* | Repetició d'un bloc de codi (`while`, `for`) | SA2 |
| condicional | *conditional / if statement* | Decidir entre camins segons una condició (`if`/`elif`/`else`) | SA3 |
| funció | *function* | Bloc de codi amb nom (`def`) que fa una feina concreta | SA4 |
| paràmetre / argument | *parameter / argument* | Valor que li passes a una funció perquè el faci servir | SA4 |
| retornar | *return* | El valor que una funció «lliura» a qui la crida (`return`) | SA4 |
| mòdul / biblioteca | *module / library* | Codi ja escrit que importes per no reinventar la roda (`import radio`) | SA1+ |
| REPL | *REPL (Read-Eval-Print Loop)* | Consola interactiva on proves ordres línia a línia i llegeixes el resultat a l'instant | SA1+ |
| flashejar / carregar | *flash / upload* | Enviar el `.hex` amb el teu programa a la placa micro:bit | SA1 |
| depurar | *debug* | Trobar i arreglar errors de manera sistemàtica (DEPURA!) | SA1+ |
| error de sintaxi | *syntax error* | El codi no compleix les regles del llenguatge: no s'executa | SA2 |
| indentació | *indentation* | Espais a l'inici de línia; en Python **delimiten els blocs** (no hi ha claus `{}`) | SA1 |
| pseudocodi | *pseudocode* | El programa escrit en paraules teves, abans del codi | SA3+ |
| diagrama de flux | *flowchart* | El programa dibuixat amb caixes i fletxes | SA3+ |
| antirebot | *debounce* | Filtrar les lectures múltiples d'una sola premuda de botó | SA3 |
| microprogramari | *firmware* | El programa base (MicroPython) que viu dins de la placa, empaquetat amb el teu codi dins del `.hex` | SA1 |
| estructura de dades | *data structure* | Manera d'organitzar diversos valors junts (llista, tupla) | SA5-SA6 |

## 🎛️ Senyals i control

| Català | Anglès | Què és | On surt |
|---|---|---|---|
| senyal digital | *digital signal* | Dos estats: HIGH/LOW | SA1 |
| senyal analògic | *analog signal* | Molts valors possibles dins d'un rang (0–1023 en llegir amb `read_analog()`) | SA3 |
| PWM | *pulse-width modulation* | «Simular» valors intermedis encenent i apagant molt de pressa | SA2 |
| llindar | *threshold* | Valor frontera a partir del qual es pren una decisió | SA3 |
| calibratge | *calibration* | Mesurar valors reals per ajustar llindars i paràmetres | SA3, SA7 |
| consigna | *setpoint* | El valor que el sistema de control vol assolir | SA6 |
| realimentació | *feedback* | El sensor informa el controlador del resultat de les seves accions | SA6 |
| llaç obert / tancat | *open / closed loop* | Control sense sensor / amb sensor que corregeix | SA6 |
| histèresi | *hysteresis* | Dos llindars separats per evitar el clic-clic constant | SA6 |
| màquina d'estats | *state machine* | Sistema organitzat en estats (p. ex. RUN/STOP/ALERTA) i transicions | SA6 |
| soroll (de mesura) | *noise* | Variacions aleatòries que embruten una lectura de sensor | SA3, SA6 |

## 🤖 Robòtica i moviment

| Català | Anglès | Què és | On surt |
|---|---|---|---|
| sensor / actuador | *sensor / actuator* | El que percep / el que actua sobre el món | SA1 |
| servomotor | *servo* | Motor que controla la **posició** (angle) | SA1 (mascota) |
| motoreductor | *geared DC motor* | Motor de gir continu amb reductora; velocitat amb PWM | SA4 |
| sensor d'ultrasons | *ultrasonic sensor* | Mesura distància pel temps de l'eco (HC-SR04) | SA3, SA7 |
| seguidor de línia | *line follower* | Sensor(s) IR que detecten una línia pintada a terra | SA7 |
| cinemàtica diferencial | *differential drive* | Girar variant la velocitat de cada roda (sense volant) | SA7 |
| autònom | *autonomous* | Que decideix sol, sense comandament humà | SA7 |
| gest | *gesture* | Moviment detectat per l'acceleròmetre (`was_gesture()`), p. ex. sacsejar o girar | SA1 (mascota), SA8 |

## 📡 Comunicacions i dades

| Català | Anglès | Què és | On surt |
|---|---|---|---|
| ràdio | *radio* | Comunicació sense fils entre plaques micro:bit (`import radio`) | SA5, SA8 |
| grup / canal | *group* | Número que fa que dues plaques «es puguin sentir» (`radio.config(group=...)`) | SA5, SA8 |
| protocol de comandes | *command protocol* | Conjunt de missatges curts acordats i el seu significat (p. ex. `"F"` = endavant) | SA5 |
| estació base | *base station* | Placa (pròpia, temporalment executada a la d'un company o del docent) que rep la telemetria | SA8 |
| telemetria | *telemetry* | Enviar mesures a distància per llegir-les des d'un altre lloc | SA8 |
| aprenentatge automàtic | *machine learning (ML)* | El sistema aprèn patrons a partir d'exemples, no de regles escrites | SA8 |
| entrenar / etiqueta | *train / label* | Donar exemples al model / el nom de la classe de cada exemple | SA8 |
| classificador | *classifier* | Model que assigna una categoria a cada entrada | SA8 |
| biaix | *bias* | Error sistemàtic (sovint heretat de dades poc variades) | SA8 |
| dades personals | *personal data* | Informació que identifica algú: exigeix consentiment | SA8 |

---

*Consell de cerca: si busques un error o un component, **busca'l en anglès** («micro:bit radio group», «HC-SR04 timeout»): trobaràs 100 vegades més respostes. No trobes un terme aquí? Busca'l al vocabulari essencial de la [SA0](../SA0/README.md), organitzat SA per SA i amb analogies del dia a dia. Llicència CC BY-SA 4.0.*
