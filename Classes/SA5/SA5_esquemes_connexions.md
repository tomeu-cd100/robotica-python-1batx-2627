# SA5 · Esquemes i connexions

> 🧑‍🎓 **Quan toca?** Tingues aquesta pàgina oberta durant les **Sessions 1-3**: avui la micro:bit **no estrena cap component nou** — la ràdio és **interna** i no necessita cablatge — però reutilitza tots els pins de moviment fixats a la SA4.

> ⚠️ **Cap cablatge nou.** Aquesta SA no toca cap pin nou. El vehicle T2 arriba **ja muntat** de la SA4: si algun cablatge no funciona, revisa primer que segueixi exactament l'esquema de la SA4, no aquesta pàgina.

---

## 1. Ràdio (Sessions 1-3) — sense cablatge

| Component | Pin | Tipus | Programa(es) | Notes |
|---|---|---|---|---|
| Ràdio integrada de la micro:bit V2 | — | Interna (RF) | `radio_missatges`, `comandament`, `receptor_vehicle` | No necessita cap connexió física. `radio.on()` l'activa; `radio.config(group=N)` fixa amb qui es "sent". |

> 🔑 **Font única de pins:** el mapa de pins de tot el fil conductor és [`00_Fil_conductor_construccions.md` §1b](../00_General/00_Fil_conductor_construccions.md#1b-mapa-de-pins-per-trimestre-font-unica-vinculant), que ja indica «Ràdio (SA5) — Ràdio interna; no necessita cablatge.» a la fila T2. Aquesta pàgina no en repeteix cap de nou.

## 2. Configuració de grup (Sessions 1-3) — el "cablatge lògic" de la ràdio

En lloc de fils, la ràdio es "connecta" amb un número de **grup**: només les plaques amb el mateix `group` es poden sentir entre elles.

| Paràmetre | Valor | Notes |
|---|---|---|
| `group` | Assignat pel docent per parella de números de llista (vegeu [`SA5_guia_docent.md`](SA5_guia_docent.md#assignacio-de-grups-de-radio)) | Evita interferències entre les ~10 parelles simultànies de l'aula. |
| `power` | `6` (valor moderat) | Abast suficient dins de l'aula; no cal tocar-lo. |

> 🔒 **Regla vinculant (fitxa 14):** el `group` és **només** per a proves puntuals de banc de proves; el codi i el producte que s'avaluen són sempre **individuals**.

## 3. Pins del vehicle reutilitzats (Sessió 3 — producte «control remot bàsic»)

El programa [`receptor_vehicle.py`](codi/receptor_vehicle/receptor_vehicle.py) fa servir **exactament** els mateixos pins fixats a la SA4, sense cap canvi:

| Component | Pin | Tipus | Notes |
|---|---|---|---|
| Motoreductor **esquerre** (M1), sentit endavant | **P13** | PWM | Fixat a la SA4, Sessió 2; **no es toca**. |
| Motoreductor **esquerre** (M1), sentit enrere | **P14** | PWM | Fixat a la SA4, Sessió 2; **no es toca**. |
| Motoreductor **dret** (M2), sentit endavant | **P15** | PWM | Fixat a la SA4, Sessió 2; **no es toca**. |
| Motoreductor **dret** (M2), sentit enrere | **P16** | PWM | Fixat a la SA4, Sessió 2; **no es toca**. |
| Alimentació dels motors | Portapiles 4×AA → Micro:shield | — | **Mai** des de l'USB de l'ordinador quan els motors giren. |

> Detall complet del muntatge físic: [`SA4_esquemes_connexions.md`](../SA4/SA4_esquemes_connexions.md) i [`00_Projecte_T2_Vehicle.md`](../00_General/00_Projecte_T2_Vehicle.md).

## 4. Comprovació ràpida (abans de fer proves de ràdio)

- [ ] `radio.on()` cridat a **totes dues** plaques (emissora i receptora).
- [ ] Mateix número de `group` a totes dues plaques (consulta la taula del docent).
- [ ] Mateix `PREFIX` de protocol escrit **literalment igual** a emissor i receptor.
- [ ] Vehicle alimentat des del **portapiles**, mai des de l'USB, si es prova `receptor_vehicle.py`.
- [ ] El programa comença amb `from microbit import *` i `import radio`.

---

## Simulació al navegador

- ▶ [python.microbit.org](https://python.microbit.org) **sí simula la ràdio**, però només **entre instàncies del simulador** obertes alhora (no entre el simulador i una placa física real): obre dues pestanyes/finestres per provar l'enviament i la recepció.
- És una via de pràctica **individual** vàlida a casa per a `radio_missatges.py` i `comandament.py` (protocol, `group`, `send`/`receive`).
- `receptor_vehicle.py` es pot revisar amb el simulador només per a la part de **lògica** (separar prefix i ordre): el moviment real dels motors necessita el vehicle físic, com ja passava a la SA4.

> Detall del procediment de transferència i limitacions generals del simulador: [`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md) §2.
