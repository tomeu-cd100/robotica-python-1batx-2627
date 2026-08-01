# SA2 · Esquemes i connexions

> 🧑‍🎓 **Quan toca?** Tingues aquesta pàgina oberta durant les **Sessions 1-3**, cada cop que munts un component nou al Micro:shield. A partir d'avui la micro:bit **s'encaixa al Micro:shield**: aquí comença la sèrie de taules de connexió pin a pin que t'acompanyarà fins a la SA8.

> ⚠️ **Abans de connectar res:** micro:bit **desendollada** de l'USB. Comprova la **polaritat** dels LED (pota llarga = ànode, cap al senyal) i que el relé no es toca mai pel costat del circuit extern mentre hi ha tensió.

---

## 1. Encaixar el Micro:shield

1. Amb la micro:bit **desendollada**, encaixa'l a l'edge connector del Micro:shield (la matriu de LED i els botons queden accessibles per la part de dalt).
2. El Micro:shield dona accés als pins amb connectors tipus **block** (3 fils: senyal, 3V, GND) i, per a alguns pins, amb pins solts d'header.
3. Torna a connectar l'USB **només quan tots els components estiguin cablejats**.

## 2. Taula de connexions d'aquesta SA

| Component | Pin | Kit | Programa(es) | Notes |
|---|---|---|---|---|
| **LED extern** (parpelleig) | **P1** | Kit 1 | `led_parpelleig`, `pwm_led_rgb` (respiració) | Sortida digital (S1) i PWM (S2). Pota llarga (ànode) cap al pin de senyal. |
| **LED RGB** (colors combinats) | **P8** (R) · **P12** (G) · **P16** (B) | Kit 1 | `pwm_led_rgb` | Un canal PWM per color; `(0,0,0)` = apagat, `(1023,1023,1023)` = blanc. |
| **Brunzidor** (piezo extern) | **P2** | Kit 1 | `musica_altaveu`, `semafor_rele` | Alternativa vàlida: l'altaveu **integrat** de la V2 (sense indicar `pin=` a `music`). |
| **LED semàfor: verd** | **P1** | Kit 1 | `semafor_rele` | Reaprofita el mateix pin que S1 (circuit desmuntat i tornat a muntar). |
| **LED semàfor: ambre** | **P8** | Kit 1 | `semafor_rele` | — |
| **LED semàfor: vermell** | **P12** | Kit 1 | `semafor_rele` | — |
| **Relé** | **P13** (bobina/control) | Kit 3 | `semafor_rele` | Contactes **NO** (normalment obert) al costat del circuit extern; **mai** connectis el costat extern directament a un pin de la placa. |

> 🔁 **Pins reaprofitats a propòsit:** P1, P8 i P12 canvien de component entre exercicis (un LED solt a la S1, un canal del semàfor a la S3): és normal muntar i desmuntar circuits diferents dins de la mateixa SA. Cap muntatge d'aquesta pàgina es queda fix fins a la S4: la mascota **torna a triar** els seus propis pins (taula següent).

## 3. Pins que farà servir la mascota (Sessió 4)

El [dossier del Projecte T1 · La mascota](../00_General/00_Projecte_T1_Mascota.md) defineix el seu propi cablatge definitiu, **diferent** del d'aquesta pàgina perquè inclou components de SA2 **i** de SA3 alhora:

| Component de la mascota | Pin | Es programa a… |
|---|---|---|
| Micro servo (orelles/cua) | P0 | **SA4** (es munta a la S4, no es programa fins llavors). |
| LED / LED RGB (indicador d'humor) | P1 | **SA2** (aquesta SA). |
| Brunzidor | P2 | **SA2** (aquesta SA). |
| Sensor PIR, polsador, sensor de so... | P8, P12, P4... | **SA3** (properament). |

> Per això la prova d'encesa de la S4 només **valida** el LED/RGB i el so amb el codi ja fet d'aquesta SA: la resta arribarà a la SA3.

## 4. Pins analògics (ADC) del micro:bit V2

Recorda: només els pins **P0, P1, P2, P3, P4 i P10** tenen conversor analògic-digital (ADC) per **llegir** senyals analògics. Aquesta SA només **escriu** sortides (`write_digital`/`write_analog`), no en llegeix, així que la restricció no afecta cap dels components d'aquesta pàgina — sí que caldrà tenir-la en compte a la SA3 (entrades).

## 5. Pins ocupats pel display

Els pins **3, 4, 6, 7, 9 i 10** els fa servir en part la matriu de LED per darrere (multiplexat): evita'ls per a components nous si vols que el display i el component extern convisquin sense parpelleigs estranys. Cap component d'aquesta SA hi va connectat.

---

## 6. Comprovació ràpida (abans de transferir el codi)

- [ ] Micro:bit **desendollada** mentre es cableja.
- [ ] Polaritat dels LED correcta (pota llarga cap al senyal).
- [ ] El costat del circuit extern del relé **no** toca cap pin de la micro:bit.
- [ ] El programa comença amb `from microbit import *` (i `import music` si en fa servir).

---

## Simulació al navegador

- ▶ [python.microbit.org](https://python.microbit.org) reprodueix la **matriu de LED**, els **botons** i l'**altaveu integrat** (sense `pin=`), però **NO simula components externs**: ni el LED al Micro:shield, ni el LED RGB, ni el brunzidor extern, ni el relé. Per a aquesta SA, el simulador només serveix per validar la **lògica** dels programes (bucles, `if`, temps) abans de provar-los amb el maquinari real.
- **Alternativa per treballar la part de display/so sense placa:** el mateix simulador, limitant-se als exemples que només fan servir `display` i `music.play()` sense `pin=` (per exemple, una primera versió de `musica_altaveu.py` sense el paràmetre `pin=pin2`).

> Detall del procediment de transferència i limitacions generals del simulador: [`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md) §2.
