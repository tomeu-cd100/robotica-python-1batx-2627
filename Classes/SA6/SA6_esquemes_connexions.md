# SA6 · Esquemes i connexions

> 🧑‍🎓 **Quan toca?** Tingues aquesta pàgina oberta durant les **Sessions 1-3**: el nucli d'aquesta SA (FSM + STOP prioritari) **no estrena cap component nou** — reutilitza tots els pins de moviment/ràdio fixats a la SA4-SA5 —, però l'**ampliació** de la S3 (sensor de temperatura/relé) sí que hi afegeix el relé i el DHT11 del Kit 3.

> ⚠️ **Cap cablatge nou al nucli.** El vehicle T2 arriba **ja muntat i controlat per ràdio** de la SA4-SA5: si algun cablatge de motors/LED/polsador no funciona, revisa primer que segueixi exactament l'esquema de la SA4, no aquesta pàgina.

---

## 1. Pins del vehicle reutilitzats (Sessions 2-3 — `vehicle_seguretat.py`)

| Component | Pin | Tipus | Notes |
|---|---|---|---|
| Motoreductor **esquerre** (M1), sentit endavant | **P13** | PWM | Fixat a la SA4; **no es toca**. |
| Motoreductor **esquerre** (M1), sentit enrere | **P14** | PWM | Fixat a la SA4; **no es toca**. |
| Motoreductor **dret** (M2), sentit endavant | **P15** | PWM | Fixat a la SA4; **no es toca**. |
| Motoreductor **dret** (M2), sentit enrere | **P16** | PWM | Fixat a la SA4; **no es toca**. |
| LED indicador d'estat | **P1** | Digital | Encès fix = RUN, apagat = STOP, intermitent = ALERTA (si s'amplia). Reaprofita el pin del LED de la mascota, ja alliberat. |
| Polsador STOP manual | **P12** | Digital, *pull-up* intern (cal configurar-lo al codi amb `pin12.set_pull(pin12.PULL_UP)`, no ve activat per defecte) | LOW (0) = premut; **prioritat màxima**, es comprova el primer a cada volta del bucle. |
| Ràdio (SA5) | — | Interna (RF) | `radio.on()` + `radio.config(group=...)`; mateix `GRUP` i mateix `PREFIX` ("CMD:") que a la SA5. |
| Alimentació dels motors | Portapiles 4×AA → Micro:shield | — | **Mai** des de l'USB de l'ordinador quan els motors giren. |

> 🔑 **Font única de pins:** el mapa de pins de tot el fil conductor és [`00_Fil_conductor_construccions.md` §1b](../00_General/00_Fil_conductor_construccions.md#1b-mapa-de-pins-per-trimestre-font-unica-vinculant), que és el document vinculant. Aquesta pàgina no en repeteix cap de nou sense citar-lo.

## 2. Sensor de temperatura intern (Sessió 1 — `termostat_histeresi.py`)

| Component | Pin | Tipus | Notes |
|---|---|---|---|
| Sensor de temperatura **intern** | — | (graus C directes) | `temperature()`, sense cablatge; no cal el sensor extern del Kit 2 per al nucli. |
| Relé (Kit 3) | **P2** | Digital | Reaprofita el pin del brunzidor de la mascota, ja alliberat. Substitut segur si no tens relé a mà: **LED al P1** (mateixa lògica, canvia només l'actuador). |

## 3. Ampliació — sensor de temperatura extern i DHT11 (Sessió 3, +ampliació)

| Component | Pin | Tipus | Notes |
|---|---|---|---|
| DHT11 (temperatura/humitat, Kit 3) | **P8** | Digital 1-Wire | Reaprofita el pin del PIR de la mascota; **no** P13, ocupat pel motor M1. |
| Sensor de temperatura extern (Kit 2, si es vol comparar amb l'intern) | **P10** *(o el pin ADC vàlid que indiqui el docent)* | Analògic (0-1023), ADC | Mateix pin que a la pràctica `termometre.py` de la SA3; **només** per a qui amplia. |

> Pins ADC vàlids del Micro:shield: **P0, P1, P2, P3, P4, P10**. Si el LED indicador (P1) ja està ocupat al vehicle, no reutilitzis aquest pin per a cap entrada analògica del sensor extern.

## 4. Comprovació ràpida (abans de fer proves de la màquina d'estats)

- [ ] `radio.on()` cridat i mateix `group` que el comandament de la SA5.
- [ ] El polsador (P12) es comprova amb `read_digital()` **al principi** de cada volta del bucle.
- [ ] El LED (P1) reflecteix l'estat: fix en RUN, apagat en STOP.
- [ ] El relé (P2) o el LED substitut estan connectats abans de provar `termostat_histeresi.py`.
- [ ] Vehicle alimentat des del **portapiles**, mai des de l'USB, si es prova `vehicle_seguretat.py` amb els motors.
- [ ] El programa comença amb `from microbit import *` (i `import radio` a `vehicle_seguretat.py`, `import log` a `registre_dades.py`).

---

## Simulació al navegador

- ▶ [python.microbit.org](https://python.microbit.org) **sí simula**: `temperature()`, els botons A/B, l'acceleròmetre i el mòdul **`log`** (es pot descarregar el registre simulat des del propi simulador).
- ▶ **NO simula**: el relé/actuador extern (`termostat_histeresi.py`, part física), els motors (`vehicle_seguretat.py`, part física) ni el DHT11/sensor extern de l'ampliació.
- Amb dues instàncies del simulador obertes, la **lògica** de ràdio de `vehicle_seguretat.py` (separar prefix i ordre, processar `"X"` com a prioritari) es pot revisar igual que a la SA5; el moviment real dels motors i l'efecte del relé necessiten el vehicle físic.

> Detall del procediment de transferència i limitacions generals del simulador: [`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md) §2.
