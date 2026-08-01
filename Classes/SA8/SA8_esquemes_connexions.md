# SA8 · Esquemes i connexions

> 🧑‍🎓 **Quan toca?** Tingues aquesta pàgina oberta durant les **Sessions 1-3**: el rover arriba **ja muntat** de la SA7, però avui hi afegeixes els dos sensors nous del Kit 3 (DHT11 i IMU MPU6050) i actives la ràdio per telemetria.

> ⚠️ **Cablatge nou, però mínim.** El rover no canvia de xassís ni de motors: només s'hi connecten dos components nous (DHT11 i IMU MPU6050) sobre els pins que ja reservava el mapa de pins des de la SA6/SA7.

---

## 1. Pins del rover (font única de pins)

| Component | Pin | Tipus | Notes |
|---|---|---|---|
| Motoreductor **esquerre** (M1), sentit endavant | **P13** | PWM | Heretat de SA4-SA7; **no es toca**. |
| Motoreductor **esquerre** (M1), sentit enrere | **P14** | PWM | Heretat de SA4-SA7; **no es toca**. |
| Motoreductor **dret** (M2), sentit endavant | **P15** | PWM | Heretat de SA4-SA7; **no es toca**. |
| Motoreductor **dret** (M2), sentit enrere | **P16** | PWM | Heretat de SA4-SA7; **no es toca**. |
| Sensor d'ultrasons HC-SR04, **TRIG** | **P1** | Digital, sortida | Heretat de SA7; **no es toca**. |
| Sensor d'ultrasons HC-SR04, **ECHO** | **P2** | Digital, entrada | Heretat de SA7; **no es toca**. |
| Seguidor de línia KS0050 | **P0** | Analògic, ADC vàlid | Heretat de SA7; **no es toca**. |
| **DHT11** (temperatura/humitat, Kit 3) | **P8** | Digital, mesura de polsos (`machine.time_pulse_us`) | *(nou d'aquesta SA)* Heretat del pin de l'ampliació de SA6 (mateix pin, sense canvi). |
| **IMU MPU6050** (Kit 3) | **P19 (SCL)** / **P20 (SDA)** | I2C | *(nou d'aquesta SA)* Bus I2C: `from microbit import *` ja exposa l'objecte `i2c`, cap import addicional. |
| Polsador STOP (`comportaments.py`/`telemetria_radio.py`) | **P12** | Digital, *pull-up* intern (`pin12.set_pull(pin12.PULL_UP)`) | Heretat de SA6-SA7; mateix patró prioritari. |
| Ràdio interna (telemetria) | — | Interna (RF) | No necessita cablatge; `radio.on()` + `radio.config(group=N)`, com a la SA5. |
| Alimentació dels motors | Portapiles 4×AA → Micro:shield | — | **Mai** des de l'USB de l'ordinador quan els motors giren. |

> 🔑 **Font única de pins:** el mapa de pins de tot el fil conductor és [`00_Fil_conductor_construccions.md` §1b](../00_General/00_Fil_conductor_construccions.md#1b-mapa-de-pins-per-trimestre-font-unica-vinculant), que és el document vinculant. Aquesta pàgina no en repeteix cap de nou sense citar-lo.

> ➡️ **Sensors del Kit 3 que NO són al nucli d'aquesta SA.** El BMP280 (pressió) i el CCS811 (CO₂) també es connecten al **mateix bus I2C** (P19/P20), cadascun amb la seva pròpia adreça: no calen pins nous per afegir-ne cap. Formen part dels objectius de lectura de la Sessió 1, però el **producte** avaluable només exigeix "com a mínim dos sensors" (fitxa 17): aquesta SA els tria com a **IMU MPU6050 + DHT11** (nucli programat a `telemetria_radio.py`); BMP280/CCS811 queden com a **+ampliació** (vegeu [`SA8_fitxa_ampliada.md`](SA8_fitxa_ampliada.md)).

## 2. Pins ADC vàlids del Micro:shield

Pins analògics (`read_analog()`) vàlids: **P0, P1, P2, P3, P4, P10**. Com a la SA7, el seguidor de línia fa servir **P0**; **P1** i **P2** continuen ocupats per l'HC-SR04 (digitals). El DHT11 (P8) i l'IMU (P19/P20) **no** són entrades analògiques: no competeixen pels pins ADC.

## 3. Comprovació ràpida (abans de fer proves de telemetria)

- [ ] Rover alimentat des del **portapiles**, mai des de l'USB, sempre que els motors girin.
- [ ] DHT11 connectat a **P8**, amb `set_pull(PULL_UP)` cridat abans de llegir-lo.
- [ ] IMU MPU6050 connectat al bus I2C: **SCL a P19**, **SDA a P20**, i alimentat a 3,3 V (revisa el connector del Micro:shield).
- [ ] `mpu_inicia()` cridat **un únic cop** abans del bucle (desperta el sensor del mode "sleep").
- [ ] Mateix `group` de ràdio i mateix `PREFIX` (`"TEL:"`) a `telemetria_radio.py` **i** a `estacio_base.py`.
- [ ] GND comú entre piles, Micro:shield i tots els sensors (motors, HC-SR04, seguidor de línia, DHT11, IMU): sense això, les lectures fallen de manera intermitent, com a totes les SA anteriors.
- [ ] El programa comença amb `from microbit import *` (i `import radio`, `import machine`, `import utime`, `import math` a `telemetria_radio.py`; `import radio`, `import log` a `estacio_base.py`).

---

## Simulació al navegador

- ▶ [python.microbit.org](https://python.microbit.org) **sí simula la ràdio** (entre dues instàncies del simulador obertes alhora, com a la SA5) i **també simula el mòdul `log`** (com a la SA6, es pot descarregar el CSV/HTML de dades simulades).
- ▶ **NO simula** cap component nou d'aquesta SA: ni els motoreductors, ni l'HC-SR04, ni el seguidor de línia (heretats, ja ho sabies de la SA7), ni el **DHT11**, ni l'**IMU MPU6050**.
- **Via de pràctica vàlida al simulador:** el **format del missatge** de telemetria (protocol `"TEL:..."`, separació de camps amb `analitza()`) i el comportament d'`estacio_base.py` en rebre missatges de prova enviats des d'una segona pestanya amb `radio.send()`.
- **Pla B sense rover o sense Kit 3 a punt:** codi **per parts** amb valors de sensor simulats (per exemple, `distancia = 30` en lloc de `mesura_distancia()`) per assajar la lògica del missatge, exactament com es feia amb els comportaments de la SA7.

> Detall del procediment de transferència i limitacions generals del simulador: [`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md) §2.
