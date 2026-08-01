# SA3 · Checklist docent — Entrades: el robot percep

**8 h (4 sessions; S4 = Prova pràctica T1) · micro:bit V2 + Micro:shield + Kit 1 + Kit 2 + Kit 3 · Criteris CA1.1, CA2.1, CA2.2 · Rúbriques R1 (codi), R2 (muntatge), R3 (compliment del repte) i R4 (documentació)**

> Eina d'acció d'una cara. Condensa la [`SA3_guia_docent.md`](SA3_guia_docent.md) en punts verificables. Marca `[x]` a mesura que ho tinguis fet. **Quan s'usa:** imprimeix-lo en **preparar la SA** (§1) i tingues-lo **a taula a cada sessió** (§2–§4).

## 🧰 1. Logística prèvia (preparar abans de començar la SA)
- [ ] micro:bit V2 + Micro:shield + cable USB per alumne/a a punt
- [ ] Kit Keyestudio 1 (polsador, potenciòmetre, sensor de temperatura), Kit 2 (sensor de llum, sensor de temperatura, HC-SR04, PIR) i Kit 3 (sensor de so) per alumne/a
- [ ] Accés al **REPL/consola** provat als ordinadors (webREPL o terminal sèrie)
- [ ] Projector provat amb [`SA3_esquemes_connexions.md`](SA3_esquemes_connexions.md)
- [ ] Programes oberts i provats: `nivell_llum` · `termometre` · `alarma_ultrasons` · `mascota_reactiva`
- [ ] **Sessió 3:** mascotes de la SA2 (S4) a punt, caixa **oberta i accessible** per cablejar
- [ ] Compartir rúbriques **R1, R2, R3 i R4** amb l'alumnat *abans* del producte (avaluació formativa)
- [ ] **Sessió 4:** confirmar que l'enunciat de la prova pràctica T1 (`Avaluació/Prova_practica_T1.md`) està a punt

## ⏱️ 2. Moments (punts de control per sessió)

**Sessió 1 — Entrades digitals i condicionals**
- [ ] Modelatge en directe al REPL: `is_pressed()`/`read_digital()`, *pull-up*, comptador de premudes
- [ ] Introduir el concepte d'**antirebot** (*debounce*) abans que aparegui com a "error"
- ⚠️ *Error a vigilar:* llegir el polsador sense *pull-up* (valors erràtics)

**Sessió 2 — Entrades analògiques: llum i temperatura**
- [ ] **Mini-check individual** a l'inici (10', [banc SA3](../00_General/00_Mini_checks_individuals.md#sa3--mini-check-inici-de-la-sessió-2)) — `if/else` sobre `read_light_level()`
- [ ] Modelatge de `nivell_llum.py` (barres, funció `mapa()`) i `termometre.py` (condicionals)
- [ ] Recordar els **pins ADC vàlids** (P0, P1, P2, P3, P4, P10) i que P3/P4/P10 no es poden llegir amb el display actiu (usar P0/P1/P2 a les pràctiques d'avui)
- ⚠️ *Error a vigilar:* confondre l'escala 0-255 (sensors interns) amb la 0-1023 (pins ADC)

**Sessió 3 — Repte «mascota reactiva» (producte — tanca T1)**
- [ ] Modelatge de `alarma_ultrasons.py`: trigger/echo, `machine.time_pulse_us`, seguretat 5 V
- [ ] Introduir el PIR: temps d'estabilització (30-60 s)
- [ ] Acompanyar el cablatge **EXACTE** de la mascota (P1, P2, P8, P12) i la programació individual
- [ ] **Mini-defensa breu (R4·DO)** de cada alumne/a: reaccions + una decisió justificada
- [ ] **Repte ⭐** de `Reptes_SA3.md` (nucli obligatori, en acabar la mascota): dins la S3 o com a deures abans de la S4
- [ ] Checklist de **tancament del Projecte T1**
- ⚠️ *Mantra:* el cablatge de la mascota és **vinculant**: cap component nou fora de la taula del dossier

**Sessió 4 — Prova pràctica T1 (individual, sessió sencera)**
- [ ] Repartir l'enunciat de [`Avaluació/Prova_practica_T1.md`](../../Avaluació/Prova_practica_T1.md)
- [ ] Condicions de la prova: individual, sense apunts/ajuda, temps tancat
- [ ] Recollir les entregues i el material

## 📊 3. Avaluació i evidències (a recollir)
- [ ] Repte **«mascota reactiva»** (S3) → **R1** + **R2** + **R3** (compta, Projectes 45 %)
- [ ] **Repte ⭐** (`Reptes_SA3.md`) fet i validat → **R1** (compta, Projectes 45 %)
- [ ] **Mini-defensa** (S3, R4·DO) → **R4** (fila «Defensa oral»)
- [ ] **Quadern tècnic** → **R4** (Quadern tècnic i pràctiques 25 %)
- [ ] **Observació d'aula** (autonomia, seguretat) → **R5** (Actitud 10 %)
- [ ] **Prova pràctica T1** (S4) → R1, R2, R4 (segons `06_Avaluacio_criteris_qualificacio.md`)
- [ ] Recollir **exit tickets** de la fitxa ampliada
- [ ] Traspassar valoracions al registre (nota **0–10**)

## 🪜 4. Atenció a la diversitat (previst per aquesta SA)
- [ ] **Bastida:** esquelet «Si t'encalles» del [dossier de la mascota](../00_General/00_Projecte_T1_Mascota.md#-si-tencalles-lesquelet-del-programa) · funció `mapa()` ja proposada a la fitxa
- [ ] **+ Ampliació:** calibratge fi de llindars · combinar 3+ sensors a la mascota · reptes **⭐⭐/⭐⭐⭐** opcionals (vegeu `Reptes_SA3.md`) — el ⭐ ja no hi és: és nucli obligatori (§3)
- [ ] **Sense maquinari per a tothom:** simulador limitat (només llum/temperatura/so interns, acceleròmetre, botons); torns amb la placa física per als sensors externs
