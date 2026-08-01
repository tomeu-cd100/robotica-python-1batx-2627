# SA4 · Esquemes i connexions

> 🧑‍🎓 **Quan toca?** Tingues aquesta pàgina oberta durant les **Sessions 1-4**: avui la micro:bit comença a **moure's**. A partir de la Sessió 2 els pins dels motoreductors que fixis aquí ja **no es tornaran a tocar** en tot el curs (es reutilitzen al vehicle T2 i al rover T3).

> ⚠️ **Abans de connectar res:** micro:bit **desendollada** de l'USB. Els servos i els motoreductors necessiten **alimentació externa** (portapiles): el port USB de l'ordinador **no** en subministra prou. No connectis mai l'USB i les piles alhora als motors.

---

## 1. Micro servo de la mascota (Sessió 1) — pin fix des de la SA2

| Component | Pin | Tipus | Kit | Programa(es) | Notes |
|---|---|---|---|---|---|
| Micro servo (orelles/cua de la mascota) | **P0** | PWM | Kit 2 | `funcions_moviments`, `coreografia` | Muntat des de la SA2 (S4); avui es programa per primer cop. `pin0.set_analog_period(20)` + `write_analog(26-128)` per a 0-180°. |
| Brunzidor (mascota) | **P2** | PWM | Kit 1 | `coreografia` | Mateix pin que a SA2/SA3; `music.pitch`/`music.play` amb `pin=pin2` explícit. |

> 🔁 El servo és el **mateix** de la mascota (Projecte T1): no forma part del vehicle T2 (el vehicle gira per diferència de velocitat entre motors, no amb direcció de servo).

## 2. Motoreductors del vehicle (Sessió 2-3) — pins DEFINITIUS de tot el curs

El Kit 2 porta **dos** motoreductors amb roda. Cada motor es connecta al **canal de motor** del Micro:shield mitjançant **dos** pins (un per a cada sentit de gir); el sentit es tria enviant el PWM a un pin o a l'altre, i la velocitat és el valor mateix de `write_analog` (0-1023).

> 🔑 **Font única de pins:** aquesta taula reprodueix la fila «T2 · Vehicle» del [«Mapa de pins per trimestre»](../00_General/00_Fil_conductor_construccions.md#1b-mapa-de-pins-per-trimestre-font-unica-vinculant) de `00_Fil_conductor_construccions.md`. És **aquí, a la Sessió 2-3 de la SA4**, on aquests pins es fixen per **primer** cop; el [dossier del vehicle T2](../00_General/00_Projecte_T2_Vehicle.md) i el [dossier del rover T3](../00_General/00_Projecte_T3_Rover.md) **hi remeten** un cop fixats, no al revés.

| Component | Pin / canal | Tipus | Kit | Programa(es) | Notes |
|---|---|---|---|---|---|
| Motoreductor **esquerre** (M1), sentit endavant | **P13** | PWM | Kit 2 | `velocitat_pwm`, `control_per_botons` | `write_analog(velocitat)` per avançar; `0` per aturar aquest sentit. |
| Motoreductor **esquerre** (M1), sentit enrere | **P14** | PWM | Kit 2 | `velocitat_pwm`, `control_per_botons` | `write_analog(velocitat)` per recular. |
| Motoreductor **dret** (M2), sentit endavant | **P15** | PWM | Kit 2 | `velocitat_pwm`, `control_per_botons` | — |
| Motoreductor **dret** (M2), sentit enrere | **P16** | PWM | Kit 2 | `velocitat_pwm`, `control_per_botons` | — |
| Alimentació dels motors | Portapiles 4×AA → Micro:shield | — | — | Tots | **Mai** des de l'USB de l'ordinador quan els motors giren. |

> 🔒 **Pins que es fixen avui per a tot el curs.** No s'usa **P8** (pin del PIR a la mascota, alliberat a la transició T1→T2): es deixa lliure de motors expressament, i a T2 hi va el DHT11 de l'ampliació de SA6 (vegeu el mapa de pins). Un cop cablejats i provats a la Sessió 2-3, aquest bloc de quatre pins («M1»/«M2») queda fix i **no es torna a tocar** ni al vehicle T2 (SA5-SA6) ni al rover T3 (SA7-SA9).

## 3. Pins del repte «control per botons» (Sessió 3 — producte de la SA)

El programa [`control_per_botons.py`](codi/control_per_botons/control_per_botons.py) fa servir els **mateixos** pins de motor de la taula anterior, més els botons **A** i **B** interns de la micro:bit (`button_a`/`button_b`, sense cablatge).

## 4. Muntatge del vehicle (Sessió 4 — fabricació)

La Sessió 4 és la **fabricació i el muntatge físic** del xassís del vehicle T2 (peces pretallades pel docent): fixa els dos motoreductors amb les rodes, la roda boja, la micro:bit + Micro:shield i el portapiles, i cablega'ls **exactament** amb els pins de la taula §2 (ja provats des de la Sessió 2). Segueix pas a pas el [dossier del vehicle T2](../00_General/00_Projecte_T2_Vehicle.md) §Muntatge i §Cablatge, que és la referència **vinculant** per a aquest muntatge (aquí en teniu el resum de pins).

> ⚠️ **GND comú:** si el portapiles, el Micro:shield i els motors no comparteixen la mateixa massa, els motors fallen de manera intermitent i difícil de diagnosticar (mateix avís que al dossier del vehicle).

## 5. Pins analògics (ADC) del micro:bit V2 — recordatori

Només els pins **P0, P1, P2, P3, P4 i P10** tenen conversor analògic-digital (ADC) per **llegir** senyals analògics. Aquesta SA només **escriu** sortides PWM (`write_analog`) cap al servo i els motors, no en llegeix cap, així que la restricció d'ADC no afecta cap component d'aquesta pàgina.

## 6. Comprovació ràpida (abans de transferir el codi)

- [ ] Micro:bit **desendollada** mentre es cableja.
- [ ] Servo i motoreductors alimentats des del **portapiles**, mai des de l'USB.
- [ ] Els dos pins de cada motor **mai** reben PWM alhora (bloqueja o fa vibrar el motor sense girar).
- [ ] `pin0.set_analog_period(20)` cridat abans de moure el servo.
- [ ] GND comú entre portapiles, Micro:shield i motors.
- [ ] El programa comença amb `from microbit import *`.

---

## Simulació al navegador

- ▶ [python.microbit.org](https://python.microbit.org) simula els **botons A/B** i el **display**, i el **so** si no porta `pin=` (altaveu intern), però **NO simula ni el servo ni els motoreductors externs**: cap component d'aquesta pàgina és visible en moviment al simulador.
- Per a `funcions_moviments.py` i `velocitat_pwm.py`, pots revisar la **lògica** (bucles, paràmetres, `if`) substituint temporalment les crides al servo/motor per `display.scroll(...)`, però cal maquinari real per veure el moviment de veritat.
- `control_per_botons.py` (Sessió 3, producte) es pot provar amb els botons al simulador si substitueixes `avancar()`/`retrocedir()`/`girar()`/`aturar()` per missatges de text; recalibra amb el vehicle real quan en tinguis.

> Detall del procediment de transferència i limitacions generals del simulador: [`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md) §2.
