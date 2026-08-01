# Índex de Simulacions

> **Per a qui és?** Docent i alumnat. Punt d'entrada a tot el material de
> simulació del curs: quina eina fer servir, quan i amb quins límits.

## Contingut

| Document | Què hi trobaràs |
|---|---|
| [`Simulador_microbit.md`](Simulador_microbit.md) | **L'eina principal del curs**: què simula exactament l'editor oficial de MicroPython (python.microbit.org) i què no, taula d'ús recomanat per a cada SA (SA1-SA9) i els seus límits. |
| [`Wokwi_opcional.md`](Wokwi_opcional.md) | Wokwi, **només per a qui exploni l'ampliació opcional amb Raspberry Pi Pico** (no forma part del maquinari nucli del curs). |

## Quina eina fer servir?

```
Maquinari nucli del curs (micro:bit V2 + Micro:shield + Kit Keyestudio)?
  → Simulador_microbit.md (python.microbit.org)

Ampliació opcional amb Raspberry Pi Pico?
  → Wokwi_opcional.md (wokwi.com)
```

Per a **tota la seqüència obligatòria del curs (SA1-SA9)**, l'únic
simulador necessari és l'editor oficial de MicroPython. Wokwi és
exclusivament per a l'ampliació Pico, opcional i fora del maquinari nucli.

## Relació amb la resta del curs

- El simulador és el **pla B sense maquinari** (vegeu
  `Classes/00_General/00_Mode_supervivencia.md` i
  `00_Entorns_de_treball.md` §2): quan un component falla o no hi ha prou
  plaques per a tothom, o per fer els deures de cada SA.
- També és l'eina de la rutina **PRIMM** (predir abans d'executar,
  `Programació didàctica/04_Metodologia.md` §4.2): el docent hi projecta
  codi nou sense executar-lo.
- **Cap dels dos simuladors substitueix la validació amb maquinari real**:
  els llindars de sensors calibrats al simulador **sempre** s'han de
  recalibrar amb la placa física (registrar-ho al quadern tècnic com a
  «mesura simulada»).

---

⬅️ Torna a l'arrel del repositori ([`README.md`](../README.md)).
