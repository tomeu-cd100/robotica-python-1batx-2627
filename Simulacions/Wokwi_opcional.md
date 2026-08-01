# Wokwi — només per a l'opció Pico

> **Per a qui és?** Docent (i alumnat si el centre/grup activa l'opció
> Pico). **Wokwi NO és el simulador del curs**: el maquinari nucli
> (micro:bit V2 + Micro:shield) es simula amb l'editor oficial
> (vegeu [`Simulador_microbit.md`](Simulador_microbit.md)). Wokwi entra en
> joc **només** si s'explora l'ampliació opcional amb **Raspberry Pi Pico**.

## Per què no és el simulador principal

- El maquinari nucli d'aquest curs és **micro:bit V2 + Micro:shield +
  sensors Keyestudio**, en MicroPython (`CLAUDE.md`). L'editor oficial
  (python.microbit.org) ja inclou un simulador prou fidel per a aquest
  maquinari (matriu de LED, botons, ràdio entre pestanyes...).
- Wokwi simula **altres** plaques (Arduino, ESP32, Raspberry Pi Pico) amb
  més fidelitat de circuit (resistències, LED externs, protoboard virtual),
  però **no simula la micro:bit ni el Micro:shield**.
- Introduir Wokwi com a eina general duplicaria innecessàriament l'entorn
  de treball del curs (vegeu `Classes/00_General/00_Entorns_de_treball.md`,
  que només documenta python.microbit.org i Thonny com a eines del curs).

## Quan sí té sentit: l'opció Pico

Si un alumne o grup **amplia** el curs amb una Raspberry Pi Pico (fora del
maquinari nucli, vegeu `Enllacos_i_tutorials.md` §9 «Get Started with
MicroPython on Pico»), **Wokwi és l'eina recomanada** per simular-la:

1. Ves a <https://wokwi.com> i crea un **projecte nou** amb placa
   **Raspberry Pi Pico** (o Pico W).
2. Escriu el codi MicroPython del Pico a l'editor de Wokwi (sintaxi molt
   semblant a la de micro:bit, però **no és el mateix mòdul `microbit`**:
   els pins, `machine.Pin`, ADC, PWM, etc. es defineixen diferent — vegeu
   el PDF de referència enllaçat a `Enllacos_i_tutorials.md`).
3. Munta el circuit virtual (protoboard, LED, sensors bàsics) al canvas de
   Wokwi i executa la simulació des del navegador, sense maquinari.
4. Quan hi hagi una Pico física disponible, transfereix el codi amb Thonny
   (mateix flux que amb la micro:bit, intèrpret diferent).

## Límits de Wokwi per a l'opció Pico

- Els sensors específics del Kit Keyestudio del centre (PIR, HC-SR04,
  seguidor de línia KS0050...) **no tenen sempre un component equivalent**
  a la llibreria de Wokwi: cal aproximar-los amb components genèrics
  (resistència variable, interruptor) o limitar la simulació a la lògica.
- Cap component de Wokwi reprodueix el **Micro:shield**: l'opció Pico
  s'ha de cablejar amb un protoboard extern, no amb els connectors *block*
  del Kit.
- Com amb el simulador de micro:bit, el **soroll de mesura real** dels
  sensors i el comportament físic dels motors **s'han de recalibrar** amb
  el maquinari físic un cop muntat.

---

⬅️ Torna a [`Index_simulacions.md`](Index_simulacions.md).
