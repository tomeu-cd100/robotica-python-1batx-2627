# SA7 · Checklist docent — Robòtica mòbil: el rover

**8 h (4 sessions) + Sessió 0 prèvia (muntatge, no compta a les hores) · micro:bit V2 + Micro:shield + Kit 2 · rover T3 muntat a la Sessió 0 · Criteris CA1.1, CA3.1, CA4.1 · Rúbriques R1, R3 (codi/autonomia) i R4 (documentació)**

> Eina d'acció d'una cara. Condensa la [`SA7_guia_docent.md`](SA7_guia_docent.md) en punts verificables. Marca `[x]` a mesura que ho tinguis fet. **Quan s'usa:** imprimeix-lo en **preparar la SA** (§1) i tingues-lo **a taula a cada sessió** (§2–§4).

## 🧰 1. Logística prèvia (preparar abans de començar la SA)
- [ ] micro:bit V2 + Micro:shield + cable USB per alumne/a a punt
- [ ] **Sessió 0 feta:** rover T3 muntat (peces d'ampliació HC-SR04 i seguidor de línia impreses i cargolades), amb checklist de muntatge R2 passada
- [ ] Circuit de línia a terra (cinta negra/full imprès) per taula per a la S2
- [ ] Espai lliure d'obstacles petits per a la S3-S4
- [ ] Projector provat amb [`SA7_esquemes_connexions.md`](SA7_esquemes_connexions.md)
- [ ] Programes oberts i provats: `calibratge_motors` · `segueix_linia` · `evita_obstacles` · `rover_missions`
- [ ] Compartir rúbriques **R1, R3 i R4** amb l'alumnat *abans* del producte (avaluació formativa)

## ⏱️ 2. Moments (punts de control per sessió)

**Sessió 0 (prèvia) — Muntatge del rover**
- [ ] Repartir el joc de les dues peces noves (ja impreses pel docent) a cada alumne/a
- [ ] Acompanyar el muntatge: suport HC-SR04 al davant, suport seguidor de línia sota el xassís
- [ ] Passar la **checklist de muntatge (R2, formativa)**: GND comú, sensors ben orientats, motors intactes
- ⚠️ *Pla B:* peça endarrerida → fixar temporalment amb cinta/brides i seguir programant

**Sessió 1 — Cinemàtica diferencial**
- [ ] Revisar el rover muntat; recordar que `avancar/retrocedir/girar/aturar` són les mateixes de la SA4, sense pins nous
- [ ] Modelatge de `calibratge_motors.py`: per què cal compensar M1/M2
- [ ] Acompanyar el calibratge individual i les primeres proves de trajectòria (quadrat)
- ⚠️ *Error a vigilar:* atribuir la desviació del rover a "un error de codi" en lloc del desequilibri real dels motors

**Sessió 2 — Seguidor de línia**
- [ ] **Mini-check individual** a l'inici (10', [banc SA7](../00_General/00_Mini_checks_individuals.md#sa7--mini-check-inici-de-la-sessió-2)) — cicle llegir→decidir→actuar
- [ ] Modelatge de `segueix_linia.py`: `read_analog()` i llindar de detecció calibrat sobre el circuit real
- [ ] Acompanyar la calibració del llindar taula per taula (la llum de cada punt de l'aula varia)
- ⚠️ *Error a vigilar:* assumir un llindar universal vàlid per a tota la classe

**Sessió 3 — Evita-obstacles (repte «tria un comportament autònom»)**
- [ ] PRIMM amb `evita_obstacles.py` (predicció abans d'executar)
- [ ] Modelatge de `mesura_distancia()`: mateix patró que `alarma_ultrasons.py` (SA3), pins nous (trigger P1, echo P2)
- [ ] Acompanyar el repte «tria un comportament autònom» (línia i/o obstacles, segons material de taula)
- ⚠️ *Mantra:* el mètode del sensor **no** canvia respecte a la SA3; només canvien els pins

**Sessió 4 — Missions del rover (producte)**
- [ ] Modelatge de `rover_missions.py`: selecció de missions amb botons + polsador STOP prioritari (mateix patró que `vehicle_seguretat.py`, SA6)
- [ ] Acompanyar la integració individual amb millores (velocitat variable, marge de seguretat)
- [ ] **Mini-defensa breu (R4·DO)** de cada alumne/a: una decisió justificada
- ⚠️ *Error a vigilar:* el polsador STOP no comprovat dins del bucle intern de cada missió

## 📊 3. Avaluació i evidències (a recollir)
- [ ] Checklist de **muntatge** (Sessió 0) → **R2** (formativa, no compta a les hores de SA7)
- [ ] **Comportament autònom del rover** (S4) → **R1**, **R3** (compta, Projectes 45 %)
- [ ] **Repte ⭐** (`Reptes_SA7.md`) fet i validat → **R1** (compta, Projectes 45 %)
- [ ] **Mini-defensa** (S4, R4·DO) → **R4** (fila «Defensa oral»)
- [ ] **Quadern tècnic** → **R4** (Quadern tècnic i pràctiques 25 %)
- [ ] **Observació d'aula** (autonomia, seguretat amb el rover) → **R5** (Actitud 10 %)
- [ ] Recollir **exit tickets** de la fitxa ampliada
- [ ] Traspassar valoracions al registre (nota **0–10**)

## 🪜 4. Atenció a la diversitat (previst per aquesta SA)
- [ ] **Bastida:** llindars de partida indicats (`LLINDAR_LINIA = 500`, `LLINDAR_OBSTACLE_CM = 15`) per calibrar-los, no per trobar-los de zero · esquelet de `mesura_distancia()` ja escrit (vegeu l'esquelet de [`00_Projecte_T3_Rover.md`](../00_General/00_Projecte_T3_Rover.md))
- [ ] **+ Ampliació:** combinar línia I obstacles amb prioritats · control proporcional bàsic (vegeu els reptes **⭐⭐/⭐⭐⭐** de `Reptes_SA7.md`; el ⭐ ja és nucli obligatori, no ampliació)
- [ ] **Sense rover a punt:** lògica al simulador (sense cap component real) o codi per parts amb el rover **alçat** sobre un suport, rodes lliures
