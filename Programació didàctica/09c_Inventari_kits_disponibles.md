# 09c · Inventari del maquinari disponible (dotació real del centre)

Aquest document deixa **constància del maquinari que el centre ja té** per a la matèria i **on s'utilitza cada element** dins de les SA. A diferència de `09b_Guia_compra_pressupost.md` (compra i reposició), aquí es documenta la **dotació real disponible** el curs 2026-2027.

## Dotació per alumne

- **1 micro:bit V2 + 1 Micro:shield per alumne** (hi ha tantes unitats com alumnes): plataforma nucli de tot el curs.
- **Kits Keyestudio 1-3 per alumne** (1 de cada per alumne): sensors i actuadors que es connecten al Micro:shield.
- **Fabricació digital compartida a l'aula:** talladora làser **xTool S1** i impressora 3D **Bambu Lab P2S Combo**, gestionades pel docent per fabricar les peces del fil conductor individual (mascota T1 / vehicle T2 / rover T3) de cada alumne.
- **Alimentació i cables al centre:** piles AA + carregador, cables **micro-USB** per als micro:bit.

> ✅ Amb aquesta dotació, **les 9 SA queden cobertes** sense compra addicional de maquinari de control. La compra pendent (§ «Compres del fil conductor») és **només consumible** (DM, PLA, cargols, portapiles) — vegeu `09b_Guia_compra_pressupost.md`.

---

## micro:bit V2 + Micro:shield (1 per alumne)

Plataforma base de **totes** les SA del curs.

**Contingut de la micro:bit V2:**
- Microcontrolador amb **matriu de 25 LED**, **2 botons**, **acceleròmetre**, **brúixola**, **sensor de llum i de temperatura integrats**, **micròfon i altaveu**, **ràdio i Bluetooth**, connector d'expansió edge.

**El Micro:shield** dona accés còmode als pins per connectar sensors/actuadors dels kits Keyestudio (connectors tipus block, alimentació externa per a servos/motors).

**On s'utilitza:**
| SA | Ús del micro:bit V2 + Micro:shield |
|---|---|
| SA1 | Micro:bit sola (matriu LED, botons) — primer programa, lectura de codi. |
| SA2 | Matriu LED, so (altaveu), sortides via Micro:shield (LED externs, PWM). |
| SA3 | Botons, sensors integrats (llum, temperatura, acceleròmetre) i sensors del Micro:shield (entrades). |
| SA4 | Micro:shield + servos/motors del kit (base del moviment del vehicle). |
| SA5 | Ràdio integrada de la micro:bit (comunicació entre plaques). |
| SA6 | Micro:shield + actuadors per a sistemes de control. |
| SA7 | Micro:shield + motors/sensors del rover individual. |
| SA8 | Ràdio + sensors integrats i del kit per a telemetria. |
| SA9 | Tot el conjunt, integrat al repte final. |

---

## Kit Keyestudio 1 (bàsic)

Aporta components passius i sensors/actuadors bàsics de l'alumne.

**Contingut orientatiu:**
- **LED** de diversos colors + **LED RGB**.
- **Polsadors**, **potenciòmetre**.
- **Brunzidor piezo**.
- **Resistències** i **cables dupont**.
- **Sensor de temperatura** bàsic.

**On s'utilitza:**
| SA | Ús del Kit 1 |
|---|---|
| SA2 | LED, LED RGB, brunzidor (sortides digitals i PWM). |
| SA3 | Polsador, potenciòmetre, sensor de temperatura (entrades). |
| SA6 | LED/actuadors per a sistemes de control senzills. |

---

## Kit Keyestudio 2 (sensors de percepció i peces de robot mòbil)

Aporta els **sensors de percepció** i les **peces mecàniques** per a la robòtica mòbil individual.

**Contingut orientatiu:**
- **Motoreductor(s)** + **roda(es)** per al vehicle/rover.
- **Micro servo(s)**.
- **Sensor de llum**, **sensor de temperatura**, **sensor PIR** de moviment.
- **Sensor d'ultrasons HC-SR04**.
- **Seguidor de línia.**
- **Sensor d'humitat.**

**On s'utilitza:**
| SA | Ús del Kit 2 |
|---|---|
| SA3 | Sensor de llum, temperatura, ultrasons, PIR, humitat (entrades). |
| SA4 | Micro servo(s) i motoreductor (moviment del vehicle). |
| SA6 | Sensor de temperatura + actuador per a control (llaç tancat). |
| SA7 | Motoreductors, rodes, seguidor de línia i ultrasò per al rover individual. |

---

## Kit Keyestudio 3 (comunicació, actuadors i sensors avançats)

Aporta **comunicació, actuadors i sensors avançats** per a control, telemetria i introducció a la IA.

**Contingut orientatiu:**
- **Mòdul relé.**
- **LED RGB** addicional i **LEDs individuals**.
- **Sensor de so / micròfon.**
- **IMU (giroscopi + acceleròmetre)**, si el kit el porta, com a complement del de la micro:bit.
- **Sensor de temperatura i humitat DHT11.**
- **Sensor de pressió baromètrica** o **CO₂**, segons el kit concret.

**On s'utilitza:**
| SA | Ús del Kit 3 |
|---|---|
| SA2 | Relé, LED RGB, LEDs (sortides i commutació). |
| SA3 | Sensor de so, DHT11 (entrades). |
| SA6 | Relé + DHT11 per a control (termòstat, commutació d'actuadors). |
| SA8 | Sensors avançats (DHT11, pressió/CO₂ si disponibles) per a telemetria. |
| SA9 | Qualsevol sensor del kit per al repte lliure. |

---

## Fabricació digital (compartida, gestionada pel docent)

| Element | Ús |
|---|---|
| **Talladora làser xTool S1** | Tall de les peces base (DM 3 mm) del fil conductor individual: mascota (T1), vehicle (T2), rover (T3). El docent pretalla fora d'horari lectiu (vegeu `08_Sequenciacio_temporal_anual.md`, mitigació del pla de contingència). |
| **Impressora 3D Bambu Lab P2S Combo** | Peces auxiliars impreses (rodes boges, suports, escaires) dels tres artefactes individuals. |

---

## Matriu resum: SA → material principal

| SA | Material principal | Procedència | Estat |
|---|---|---|---|
| **SA1** Hola, robot! | micro:bit V2 (matriu LED, botons) | micro:bit | ✅ |
| **SA2** Sortides: el robot actua | matriu LED, LED/RGB, brunzidor, relé | micro:bit + Kit 1 + 3 | ✅ |
| **SA3** Entrades: el robot percep | botons, sensors integrats, potenciòmetre, llum, temperatura, ultrasons, so, PIR | micro:bit + Kit 1 + 2 + 3 | ✅ (ric) |
| **SA4** Funcions i moviment | micro servos, motoreductor | Micro:shield + Kit 2 | ✅ |
| **SA5** Ràdio: robots que parlen | ràdio integrada micro:bit | micro:bit | ✅ |
| **SA6** Control: el robot decideix | sensor temperatura + relé/actuador | Kit 1 + 2 + 3 | ✅ |
| **SA7** Robòtica mòbil: el rover | rover individual (motoreductors, seguidor de línia, ultrasò) | Fil conductor + Kit 2 | ✅ |
| **SA8** Autonomia i telemetria | ràdio + sensors avançats | micro:bit + Kit 3 | ✅ |
| **SA9** Repte final integrador | tot el material | Tots | ✅ |

---

## Compres del fil conductor individual

La fabricació dels tres artefactes del fil conductor (mascota/vehicle/rover, un per alumne) consumeix consumibles propis, no coberts pels kits:

| Material | Quantitat orientativa (curs, ~30 alumnes) |
|---|---|
| DM 3 mm | ~20-25 taulers/curs |
| Filament PLA | 4-6 bobines/curs |
| Cargols M3 + separadors | ~30 jocs |
| Portapiles 4×AA (individual) | ×30 |
| Caniques/roda boja (rover) | ×30 |

**Total orientatiu: ~250-350 €** (detall complet a `09b_Guia_compra_pressupost.md`).

> ℹ️ El maquinari de control (micro:bit V2, Micro:shield, kits Keyestudio) surt de la **dotació d'aula existent** i es **retorna al juny**; només els consumibles de fabricació digital són compra recurrent.

---

*Document de constància de la dotació real. Complementa `09_Materials_recursos_per_unitat.md` (mapatge per unitat) i `09b_Guia_compra_pressupost.md` (compra i reposició). Llicència CC BY-SA 4.0.*
