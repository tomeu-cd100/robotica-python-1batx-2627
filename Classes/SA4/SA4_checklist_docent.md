# SA4 · Checklist docent — Funcions i moviment

**8 h (4 sessions; S4 = fabricació del vehicle T2) · micro:bit V2 + Micro:shield + Kit 2 · Criteris CA1.1, CA2.1 · Rúbriques R1 (codi), R2 (muntatge) i R4 (documentació)**

> Eina d'acció d'una cara. Condensa la [`SA4_guia_docent.md`](SA4_guia_docent.md) en punts verificables. Marca `[x]` a mesura que ho tinguis fet. **Quan s'usa:** imprimeix-lo en **preparar la SA** (§1) i tingues-lo **a taula a cada sessió** (§2–§4).

## 🧰 1. Logística prèvia (preparar abans de començar la SA)
- [ ] micro:bit V2 + Micro:shield + cable USB per alumne/a a punt
- [ ] Kit Keyestudio 2 (micro servo, 2 motoreductors + rodes) per alumne/a; portapiles 4×AA carregats
- [ ] Peces pretallades del xassís del vehicle T2 a punt per a la Sessió 4 (vegeu `00_Fil_conductor_construccions.md`)
- [ ] Projector provat amb [`SA4_esquemes_connexions.md`](SA4_esquemes_connexions.md)
- [ ] Programes oberts i provats: `funcions_moviments` · `coreografia` · `velocitat_pwm` · `control_per_botons`
- [ ] Compartir rúbriques **R1, R2 i R4** amb l'alumnat *abans* del producte (avaluació formativa)
- [ ] **Sessió 4:** eines de muntatge (destornillador, cargols M3, canica per a la roda boja) a punt

## ⏱️ 2. Moments (punts de control per sessió)

**Sessió 1 — Funcions amb paràmetres i valor de retorn**
- [ ] Repassa un fragment ja conegut (`mapa()` de SA3, `respira()` de SA2) com a "funció que ja fèieu sense el nom"
- [ ] Modelatge de `funcions_moviments.py`: `graus_a_pwm()` (retorn) vs `mou_servo()` (sense retorn)
- ⚠️ *Error a vigilar:* confondre una funció que **calcula** amb una que **fa** alguna cosa

**Sessió 2 — Motoreductor amb funcions de moviment**
- [ ] Introduir els pins **definitius** M1/M2: no es tornaran a tocar en tot el curs
- [ ] Modelatge de `velocitat_pwm.py`: `avancar`/`retrocedir`/`girar`/`aturar`
- [ ] **Mini-check individual** a l'inici (10', [banc SA4](../00_General/00_Mini_checks_individuals.md)) — funció amb paràmetre sense apunts
- ⚠️ *Error a vigilar:* motors alimentats només per USB (no giren); PWM als dos pins d'un motor alhora

**Sessió 3 — Repte «control per botons» (producte)**
- [ ] PRIMM amb `control_per_botons.py` (predicció abans d'executar)
- [ ] Acompanyar la programació individual de la seqüència pròpia
- [ ] **Mini-defensa breu (R4·DO)** de cada alumne/a: seqüència + una decisió justificada
- [ ] **Repte ⭐** de `Reptes_SA4.md` (nucli obligatori, diferent de «control per botons»): dins la S3 o com a deures abans de la S4
- ⚠️ *Mantra:* el botó B **sempre** atura, es processi on es processi (anticipa l'STOP de la SA6)

**Sessió 4 — Muntatge del vehicle T2 (fabricació)**
- [ ] Acompanyar el muntatge pas a pas del [dossier del vehicle](../00_General/00_Projecte_T2_Vehicle.md)
- [ ] Supervisar la **prova de fum** (motors giren en el sentit esperat) abans de tancar el xassís
- [ ] Checklist de muntatge; recordar portar el vehicle a la SA5
- ⚠️ *Mantra:* els pins de motor **no canvien** respecte a la S2-S3; el cablatge és mecànic, no de programació

## 📊 3. Avaluació i evidències (a recollir)
- [ ] Repte **«control per botons»** (S3) → **R1** + **R2** (compta, Projectes 45 %)
- [ ] **Repte ⭐** (`Reptes_SA4.md`) fet i validat → **R1** (compta, Projectes 45 %)
- [ ] **Mini-defensa** (S3, R4·DO) → **R4** (fila «Defensa oral»)
- [ ] **Muntatge del vehicle** (S4) → **R2** (Projectes 45 %)
- [ ] **Quadern tècnic** → **R4** (Quadern tècnic i pràctiques 25 %)
- [ ] **Observació d'aula** (autonomia, seguretat) → **R5** (Actitud 10 %)
- [ ] Recollir **exit tickets** de la fitxa ampliada
- [ ] Traspassar valoracions al registre (nota **0–10**)

## 🪜 4. Atenció a la diversitat (previst per aquesta SA)
- [ ] **Bastida:** plantilla de funció de moviment amb nom i paràmetres ja definits (cos buit) · esquema de connexió del motoreductor ja fet
- [ ] **+ Ampliació:** velocitat variable i acceleració progressiva · seqüència coreografiada · reptes **⭐⭐/⭐⭐⭐** opcionals (vegeu `Reptes_SA4.md`) — el ⭐ ja no hi és: és nucli obligatori (§2, Sessió 3)
- [ ] **Sense maquinari per a tothom:** simulador limitat (ni servo ni motoreductors); torns amb la placa física o substitució per `display.scroll(...)` per validar la lògica
