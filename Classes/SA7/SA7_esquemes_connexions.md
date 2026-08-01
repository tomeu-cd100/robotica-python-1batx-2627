# SA7 · Esquemes i connexions

> 🧑‍🎓 **Quan toca?** Tingues aquesta pàgina oberta durant les **Sessions 1-4**: el rover arriba **ja muntat** de la Sessió 0, però aquí trobaràs els pins exactes de tots els seus components, motors heretats inclosos.

> ⚠️ **Cap cablatge nou en aquesta SA.** El rover s'acaba de cablejar a la **Sessió 0** (muntatge): si algun cablatge no funciona, revisa primer que segueixi exactament aquesta pàgina i [`00_Projecte_T3_Rover.md`](../00_General/00_Projecte_T3_Rover.md), no un esquema anterior.

---

## 1. Pins del rover (font única de pins)

| Component | Pin | Tipus | Notes |
|---|---|---|---|
| Motoreductor **esquerre** (M1), sentit endavant | **P13** | PWM | Fixat a la SA4; **no es toca**. |
| Motoreductor **esquerre** (M1), sentit enrere | **P14** | PWM | Fixat a la SA4; **no es toca**. |
| Motoreductor **dret** (M2), sentit endavant | **P15** | PWM | Fixat a la SA4; **no es toca**. |
| Motoreductor **dret** (M2), sentit enrere | **P16** | PWM | Fixat a la SA4; **no es toca**. |
| Sensor d'ultrasons HC-SR04, **TRIG** | **P1** | Digital, sortida | *(pin reconvertit, vegeu §Conversió avall)* |
| Sensor d'ultrasons HC-SR04, **ECHO** | **P2** | Digital, entrada | *(pin reconvertit, vegeu §Conversió avall)* |
| Seguidor de línia KS0050 | **P0** | Analògic, ADC vàlid | Llindar de detecció a calibrar sobre el circuit real. |
| Polsador STOP (opcional, `rover_missions.py`) | **P12** | Digital, *pull-up* intern (`pin12.set_pull(pin12.PULL_UP)`, no ve activat per defecte) | LOW (0) = premut; mateix patró que el polsador de `vehicle_seguretat.py` (SA6). |
| Alimentació dels motors | Portapiles 4×AA → Micro:shield | — | **Mai** des de l'USB de l'ordinador quan els motors giren. |

> 🔑 **Font única de pins:** el mapa de pins de tot el fil conductor és [`00_Fil_conductor_construccions.md` §1b](../00_General/00_Fil_conductor_construccions.md#1b-mapa-de-pins-per-trimestre-font-unica-vinculant), que és el document vinculant. Aquesta pàgina no en repeteix cap de nou sense citar-lo.

> ➡️ **Conversió T2 → T3 (frase vinculant).** En convertir el vehicle en rover, el **LED indicador i el relé** de la SA6 es retiren: **P1/P2 passen a l'HC-SR04** (TRIG/ECHO) i el **seguidor de línia va a P0** (ADC). Nota didàctica: a la SA3 l'HC-SR04 es va practicar a **P14/P15** (banc de proves de la mascota, exercici sense continuïtat); al rover **canvia de pins** perquè P14/P15 són ara dels motors (M1 enrere / M2 endavant), fixats des de la SA4.

## 2. Pins ADC vàlids del Micro:shield

Pins analògics (`read_analog()`) vàlids: **P0, P1, P2, P3, P4, P10**. El seguidor de línia d'aquesta SA usa **P0**; **P1** i **P2** estan ocupats aquí per l'HC-SR04 (digitals, no analògics) i no es poden fer servir per a cap altra entrada analògica mentre el rover els tingui connectats.

## 3. Comprovació ràpida (abans de fer proves de comportaments autònoms)

- [ ] Rover alimentat des del **portapiles**, mai des de l'USB, sempre que els motors girin.
- [ ] HC-SR04 alimentat a **5 V** (no 3,3 V): revisa el connector del Micro:shield.
- [ ] Trigger a **P1**, echo a **P2** (no P14/P15, que ara són dels motors).
- [ ] Seguidor de línia a **P0**, orientat cap a terra, a una alçada constant.
- [ ] Si es fa servir el polsador STOP de `rover_missions.py`: `set_pull(PULL_UP)` cridat abans del bucle.
- [ ] GND comú entre piles, Micro:shield i tots els sensors: sense això, les lectures i els motors fallen de manera intermitent (mateix avís que al vehicle T2).
- [ ] El programa comença amb `from microbit import *` (i `import machine`, `import utime` a `evita_obstacles.py`/`rover_missions.py`).

---

## Simulació al navegador

- ▶ [python.microbit.org](https://python.microbit.org) **NO simula cap component d'aquesta SA**: ni els motoreductors, ni l'HC-SR04, ni el seguidor de línia KS0050. A diferència de SA6 (que sí simulava `temperature()` i el mòdul `log`), aquí el simulador **només** és útil per esbossar en pseudocodi l'**estructura** d'una trajectòria (per exemple, la seqüència d'avançar/girar d'una "L"), no per validar cap comportament real.
- **Pla B sense rover a punt:** codi **per parts**, amb el rover **alçat** sobre un suport (rodes lliures de terra) per veure els motors respondre sense que el rover es desplaci; els sensors (HC-SR04, seguidor de línia) es poden provar igualment amb el rover alçat, sense necessitat que es mogui.

> Detall del procediment de transferència i limitacions generals del simulador: [`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md) §2.
