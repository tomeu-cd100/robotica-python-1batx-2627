# SA5 · Checklist docent — Ràdio: robots que parlen

**6 h (3 sessions) · micro:bit V2 (ràdio integrada) · vehicle T2 muntat a SA4 · Criteris CA1.1, CA1.2 · Rúbriques R1 (codi) i R4 (documentació)**

> Eina d'acció d'una cara. Condensa la [`SA5_guia_docent.md`](SA5_guia_docent.md) en punts verificables. Marca `[x]` a mesura que ho tinguis fet. **Quan s'usa:** imprimeix-lo en **preparar la SA** (§1) i tingues-lo **a taula a cada sessió** (§2–§4).

## 🧰 1. Logística prèvia (preparar abans de començar la SA)
- [ ] micro:bit V2 + Micro:shield + cable USB per alumne/a a punt
- [ ] Recordar a l'alumnat que porti el **vehicle T2** muntat a la SA4 (motors i cablatge ja fets, no es toquen)
- [ ] **Taula de grups de ràdio per parelles de números de llista** preparada i compartida abans de la Sessió 1 (vegeu [`SA5_guia_docent.md`](SA5_guia_docent.md#assignacio-de-grups-de-radio))
- [ ] Projector provat amb [`SA5_esquemes_connexions.md`](SA5_esquemes_connexions.md)
- [ ] Programes oberts i provats: `radio_missatges` · `comandament` · `receptor_vehicle`
- [ ] Compartir rúbriques **R1 i R4** amb l'alumnat *abans* del producte (avaluació formativa)
- [ ] Recordar la **regla d'individualitat de la ràdio**: codi i producte sempre propis, emparellament només de banc de proves

## ⏱️ 2. Moments (punts de control per sessió)

**Sessió 1 — Xat per ràdio**
- [ ] Repartir/repassar la taula de grups de ràdio
- [ ] Modelatge de `radio_missatges.py`: `radio.on()`, `radio.config(group=...)`, `send()`/`receive()` dins del bucle
- [ ] Deixar clar que l'aparellament és **puntual** (banc de proves), no producte compartit
- ⚠️ *Error a vigilar:* grups diferents entre parelles (no reben res) o coincidents amb una altra parella (interferències)

**Sessió 2 — Dissenyar un protocol de comandes**
- [ ] Introduir la idea de **protocol** (prefix + ordre curta) abans de mostrar `comandament.py`
- [ ] Modelatge de la connexió recepció → funcions de moviment de la SA4
- [ ] **Mini-check individual** al final de la sessió, amb el tancament (10', [banc SA5](../00_General/00_Mini_checks_individuals.md)) — enviar/rebre un missatge i actuar-hi
- ⚠️ *Error a vigilar:* `PREFIX` que no coincideix exactament entre comandament i receptor

**Sessió 3 — Repte «control remot bàsic» (producte)**
- [ ] PRIMM amb `receptor_vehicle.py` (predicció abans d'executar)
- [ ] Acompanyar el tancament individual del repte, aparellat puntualment amb un company o el docent com a emissor
- [ ] **Repte ⭐** de `Reptes_SA5.md` (nucli obligatori, 25' fila pròpia)
- [ ] **Mini-defensa breu (R4·DO), per MOSTREIG rotatiu:** 5-6 alumnes (protocol + una decisió justificada; registre rotatiu, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md#mostreig-rotatiu-de-la-mini-defensa-repte--sa2-sa8))
- ⚠️ *Mantra:* les funcions de moviment **no canvien** respecte a la SA4; només canvia l'entrada (ràdio en lloc de botons)

## 📊 3. Avaluació i evidències (a recollir)
- [ ] Repte **«control remot bàsic»** (S3) → **R1** (compta, Projectes 45 %)
- [ ] **Repte ⭐** (`Reptes_SA5.md`) fet i validat → **R1** (compta, Projectes 45 %)
- [ ] **Mini-defensa** (S3, R4·DO) → **R4** (fila «Defensa oral»)
- [ ] **Quadern tècnic** → **R4** (Quadern tècnic i pràctiques 25 %)
- [ ] **Observació d'aula** (individualitat de la ràdio, autonomia) → **R5** (Actitud 10 %)
- [ ] Recollir **exit tickets** de la fitxa ampliada
- [ ] Traspassar valoracions al registre (nota **0–10**)

## 🪜 4. Atenció a la diversitat (previst per aquesta SA)
- [ ] **Bastida:** protocol de comandes model (taula comanda → acció) proporcionat · esquelet de `actua()`/`rep_i_actua()` ja escrit
- [ ] **+ Ampliació (només reptes ⭐⭐/⭐⭐⭐, un cop fet el ⭐ obligatori):** comandes de velocitat variable o seqüències · historial de comandes amb llista/tupla mostrat per REPL (vegeu `Reptes_SA5.md`)
- [ ] **Sense segona placa disponible:** el docent fa d'emissor de proves per torns; simulador de python.microbit.org **sí** simula la ràdio entre instàncies del simulador
