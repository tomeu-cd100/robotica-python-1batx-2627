# 09b · Guia de compra i pressupost del maquinari

Llista de compra orientativa per a la matèria, derivada de l'inventari de `09_Materials_recursos_per_unitat.md`. Pensada per al **grup real de 15-20 alumnes** (xifres calculades amb 20, l'extrem superior, com a `Classes/00_General/00_Fil_conductor_construccions.md`), cadascun amb el seu propi micro:bit V2 + Micro:shield + kit Keyestudio (dotació ja existent al centre — vegeu `09c_Inventari_kits_disponibles.md`).

> ⚠️ **Els preus són orientatius (mercat 2026, IVA inclòs) i varien molt** segons proveïdor i quantitat. Demana sempre pressupost a diversos proveïdors educatius. La majoria de pràctiques es poden fer **sense maquinari** amb el simulador (python.microbit.org) si un component falla o el pressupost és nul en un moment donat.

> 📦 **Ja tens material?** Aquesta guia és per a la **compra pendent i la reposició**, no per engegar des de zero. Segons `09c_Inventari_kits_disponibles.md`, el centre **ja disposa** de micro:bit V2, Micro:shield i els 3 kits Keyestudio per a cada alumne; l'única compra necessària és el material **consumible del fil conductor individual**.

---

## 1. Estratègia de compra (llegeix-ho abans)

- **El maquinari de control ja està cobert:** cap alumne necessita comprar res per programar (micro:bit V2 + Micro:shield + Keyestudio, 1 de tot per persona). El pressupost es concentra en els **consumibles de fabricació** del fil conductor individual (mascota T1 / vehicle T2 / rover T3) i en el **material de reserva** per a avaries.
- **Compra per alumne + material comú:** cada alumne rep les peces del seu fil conductor (pretallades pel docent); una reserva comuna de consumibles (cargols, cables, portapiles) es reposa centralment.
- **Reserva de maquinari:** com que el maquinari és individual, una avaria bloqueja un sol alumne però l'atura del tot; cal tenir **unitats de reserva** de micro:bit i Micro:shield.

---

## 2. Consumibles del fil conductor individual (mascota/vehicle/rover)

> ⚠️ **El rover (T3) NO té xassís propi**: reaprofita el de vehicle (T2) i només hi afegeix dues peces petites impreses en 3D (suport HC-SR04 i suport del seguidor de línia). Per això el DM 3 mm i les caniques/roda boja **només es consumeixen a T1 i T2** — vegeu el detall calculat a `Classes/00_General/00_Fil_conductor_construccions.md` §3.

| Component | Quant. orientativa (curs, 20 alumnes) | Cost orientatiu/u | SA |
|---|---|---|---|
| Tauler **DM 3 mm** (talladora làser) | **20 taulers/curs** (10 mascota + 10 vehicle; **0 pel rover**) | 3-5 €/tauler | SA2 (mascota), SA4 (vehicle) |
| Filament **PLA** (impressora 3D) | **3-4 bobines/curs** (peces de T3 molt més lleugeres que un xassís) | 20-25 €/bobina | SA2, SA4, SA7 (peces auxiliars: escaires, difusors, rodes, suports) |
| **Cargols M3 + separadors** | segons muntatge, ~20 jocs | 0,5-1 €/joc | SA2, SA4, SA7 (SA7 només els dels 2 suports nous) |
| **Portapiles** (4×AA, individual) | ×20 | 1-2 €/u | SA4 (alimentació del vehicle; **reaprofitat pel rover a T3**) |
| Cable **micro-USB** de reserva | ~10 | 2-4 €/u | Totes (programació) |
| Canica de 16 mm (roda boja) | ×20 | 0,20 €/u | SA4 (vehicle; **reaprofitada pel rover a T3**, cap unitat nova) |

> **Estimació total dels consumibles del fil conductor: ~150-270 €/curs** (per a 20 alumnes). És més baixa que en un disseny amb xassís propi per a cada trimestre perquè **T3 no fabrica cap peça làser** i el grup real (15-20 alumnes) és més petit que l'estimació inicial de 30; és la partida recurrent principal, ja que es consumeix cada any (a diferència del maquinari de control, que es reutilitza curs rere curs).

---

## 3. Reserva de maquinari de control (per a avaries)

| Component | Quant. | Cost orientatiu/u |
|---|---|---|
| micro:bit V2 de reserva | 2-3 | 18-25 € |
| Micro:shield de reserva | 2-3 | 5-10 € |
| Peces sensors/actuadors Keyestudio de reserva | segons avaries habituals | 1-5 €/u |

> **Estimació:** 60-100 €/curs. No és una compra anual obligatòria si l'estoc de reserva de l'any anterior encara cobreix la demanda.

---

## 4. Opcional i no bloquejant

Elements que **no calen per a cap SA del curs actual** però que es documenten per si en algun moment es vol ampliar el programa (p. ex. un projecte d'ampliació individual, §5.4 de `05_Atencio_a_la_diversitat.md`):

| Component | Ús potencial | Cost orientatiu/u | Quantitat si mai s'activa |
|---|---|---|---|
| **Raspberry Pi Pico** (o Pico W) | Ampliació avançada d'IoT/control per a alumnat d'altes capacitats | 5-8 €/u | 1 per alumne interessat (no tot el grup) |

> ⚠️ **No bloquejant:** cap SA del curs 2026-2027 requereix la Pico. És una opció a valorar **només** si sorgeix un projecte d'ampliació individual concret; no s'ha de comprar per endavant.

---

## 5. Resum de pressupost orientatiu

| Bloc | Estimació anual (20 alumnes) |
|---|---|
| Consumibles del fil conductor individual (mascota/vehicle + ampliació del rover) | 150-270 € |
| Reserva de maquinari de control (micro:bit/Micro:shield/sensors) | 60-100 € |
| **TOTAL orientatiu (curs)** | **≈ 210-370 €** |

> **Versió mínima** (sense fabricació digital, amb peces reutilitzades d'anys anteriors o cartró en lloc de DM): **~100-150 €** (només reserva de maquinari).

---

## 6. On comprar (orientatiu, sense afiliació)

- **micro:bit i Micro:shield:** [microbit.org/buy](https://microbit.org/buy) i distribuïdors educatius (Farnell, RS…).
- **Kits Keyestudio:** botigues d'electrònica educativa i distribuïdors del fabricant.
- **DM, PLA i consumibles de fabricació digital:** proveïdors locals de material de taller/maker.

> Per a centres públics, consulta el **procediment de compra/licitació** del teu centre i demana **factura amb dades del centre**.

---

*Guia orientativa sota llicència CC BY-SA 4.0. Preus a revisar abans de cada compra. Complementa `09_Materials_recursos_per_unitat.md` i `09c_Inventari_kits_disponibles.md`.*
