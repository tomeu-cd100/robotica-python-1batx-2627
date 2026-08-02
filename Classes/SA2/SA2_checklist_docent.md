# SA2 · Checklist docent — Sortides: el robot actua

**8 h (4 sessions) · micro:bit V2 + Micro:shield + Kit 1 + Kit 3 · Criteris CA1.1, CA2.1, CA2.2 · Rúbriques R1 (codi), R2 (muntatge) i R4 (documentació)**

> Eina d'acció d'una cara. Condensa la [`SA2_guia_docent.md`](SA2_guia_docent.md) en punts verificables. Marca `[x]` a mesura que ho tinguis fet. **Quan s'usa:** imprimeix-lo en **preparar la SA** (§1) i tingues-lo **a taula a cada sessió** (§2–§4).

## 🧰 1. Logística prèvia (preparar abans de començar la SA)
- [ ] micro:bit V2 + Micro:shield + cable USB per alumne/a a punt
- [ ] Kit Keyestudio 1 (LED, LED RGB, brunzidor) i Kit 3 (relé, LEDs) per alumne/a
- [ ] Projector provat amb [`SA2_esquemes_connexions.md`](SA2_esquemes_connexions.md)
- [ ] Programes oberts i provats: `led_parpelleig` · `pwm_led_rgb` · `musica_altaveu` · `semafor_rele`
- [ ] **Sessió 4:** peces de la mascota **pretallades i personalitzades** (encarregar-les amb prou marge, vegeu `00_Fil_conductor_construccions.md`); escaires impresos; cargoleria
- [ ] Compartir rúbriques **R1, R2 i R4** amb l'alumnat *abans* del producte (avaluació formativa)

## ⏱️ 2. Moments (punts de control per sessió)

**Sessió 1 — Sortides digitals amb bucles**
- [ ] Encaixar el Micro:shield; muntar el LED extern a P1
- [ ] Modelatge de `led_parpelleig.py`: bucle + acumulador de comptador
- ⚠️ *Error a vigilar:* inicialitzar el comptador dins del bucle (torna a zero cada volta)

**Sessió 2 — Sortides PWM i so**
- [ ] **Mini-check individual** a l'inici (10', [banc SA2](../00_General/00_Mini_checks_individuals.md#sa2--mini-check-inici-de-la-sessió-2)) — sortida digital, no PWM
- [ ] Modelatge de `pwm_led_rgb.py` (respiració + colors) i `musica_altaveu.py` (melodia + to)
- ⚠️ *Error a vigilar:* confondre l'escala 0-1023 de `write_analog` amb 0-255

**Sessió 3 — Repte «semàfor o llum d'ambient» (producte)**
- [ ] Introduir el relé: seguretat (costat extern mai en contacte amb la placa)
- [ ] Acompanyar el muntatge i la programació individual del repte
- [ ] **Repte ⭐** (25', fila pròpia — [`Reptes_SA2.md`](../../Reptes/Reptes_SA2.md)) + 🤝 parella de lectura (5', dins)
- [ ] **Mini-defensa oral (1', R4·DO), per MOSTREIG rotatiu:** 5-6 alumnes (registre rotatiu, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md#mostreig-rotatiu-de-la-mini-defensa-repte--sa2-sa8))
- ⚠️ *Retallada del pla de contingència:* si cal recuperar temps, aquest repte **fa de producte final** i la S4 s'allibera sencera

**Sessió 4 — Fabricació i muntatge de la mascota**
- [ ] Repartir peces pretallades i personalitzades
- [ ] Acompanyar el muntatge (dossier [`00_Projecte_T1_Mascota.md`](../00_General/00_Projecte_T1_Mascota.md))
- [ ] Prova d'encesa: `led_parpelleig.py` (LED a P1) i `musica_altaveu.py` (so) funcionant; servo **muntat però no programat** (arriba a SA4)
- [ ] Checklist de muntatge i **retorn ordenat del material** sobrant
- ⚠️ *Mantra:* el relé **commuta**, no alimenta, el circuit extern

## 📊 3. Avaluació i evidències (a recollir)
- [ ] Repte **«semàfor o llum d'ambient»** (S3) → **R1** + **R2** (compta, Projectes 45 %)
- [ ] **Mini-defensa** (S3, R4·DO) → **R4** (fila «Defensa oral»)
- [ ] **Muntatge de la mascota** (S4) → **R2** (compta, Projectes 45 %)
- [ ] **Repte ⭐** (`Reptes_SA2.md`) fet i validat → **R1** (compta, Projectes 45 %)
- [ ] **Quadern tècnic** → **R4** (Quadern tècnic i pràctiques 25 %)
- [ ] **Observació d'aula** (autonomia, seguretat) → **R5** (Actitud 10 %)
- [ ] Recollir **exit tickets** de la fitxa ampliada
- [ ] Traspassar valoracions al registre (nota **0–10**)

## 🪜 4. Atenció a la diversitat (previst per aquesta SA)
- [ ] **Bastida:** esquelet «Si t'encalles» a la pàgina de la pràctica de `semafor_rele` · temps de `sleep()` ja proposats a la fitxa
- [ ] **+ Ampliació (⭐⭐/⭐⭐⭐):** llums sincronitzades amb el so · relé + LED RGB en un patró propi (vegeu `Reptes_SA2.md`)
- [ ] **Sense maquinari per a tothom:** simulador limitat (només matriu/botons/so integrat); torns amb la placa física per als components externs
