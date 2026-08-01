# SA6 · Checklist docent — Control: el robot decideix

**8 h (4 sessions; S4 = Prova pràctica T2) · micro:bit V2 + Micro:shield + Kit 1/2/3 · vehicle T2 muntat a SA4-SA5 · Criteris CA1.1, CA2.1, CA3.1 · Rúbriques R1, R3 (codi/autonomia) i R4 (documentació)**

> Eina d'acció d'una cara. Condensa la [`SA6_guia_docent.md`](SA6_guia_docent.md) en punts verificables. Marca `[x]` a mesura que ho tinguis fet. **Quan s'usa:** imprimeix-lo en **preparar la SA** (§1) i tingues-lo **a taula a cada sessió** (§2–§4).

## 🧰 1. Logística prèvia (preparar abans de començar la SA)
- [ ] micro:bit V2 + Micro:shield + cable USB per alumne/a a punt
- [ ] Recordar a l'alumnat que porti el **vehicle T2** amb el protocol de ràdio de la SA5 (motors i ràdio ja fets, no es toquen)
- [ ] Kit 3 (relé, DHT11) disponible per a qui ampliï a la S3; **no imprescindible** per al nucli
- [ ] Projector provat amb [`SA6_esquemes_connexions.md`](SA6_esquemes_connexions.md)
- [ ] Programes oberts i provats: `maquina_estats_semafor` · `termostat_histeresi` · `registre_dades` · `vehicle_seguretat`
- [ ] Compartir rúbriques **R1, R3 i R4** amb l'alumnat *abans* del producte (avaluació formativa)
- [ ] Reservar/confirmar l'enunciat de la **Prova pràctica T2** (S4): [`Avaluació/Prova_practica_T2.md`](../../Avaluació/Prova_practica_T2.md)

## ⏱️ 2. Moments (punts de control per sessió)

**Sessió 1 — Llaç obert i llaç tancat: la màquina d'estats**
- [ ] Diferenciar llaç obert/tancat amb exemples propis del vehicle (SA4-SA5) abans del codi
- [ ] Acompanyar el disseny del **diagrama RUN/STOP/ALERTA** al paper abans d'escriure res
- [ ] Modelatge de `maquina_estats_semafor.py` i `termostat_histeresi.py` (histèresi: per què dos llindars)
- ⚠️ *Error a vigilar:* un sol llindar al termòstat (provoca "clic-clic" a l'observació en directe)

**Sessió 2 — Aturada d'emergència prioritària**
- [ ] **Mini-check individual** a l'inici (10', [banc SA6](../00_General/00_Mini_checks_individuals.md#sa6--mini-check-inici-de-la-sessió-2)) — histèresi, sense apunts
- [ ] Modelatge de `actualitza_estat()`: STOP com a únic lloc que atura motors, mostra LED i display
- [ ] Comprovar que el polsador es mira **abans** que qualsevol altra entrada a cada volta del bucle
- [ ] Introducció breu de `registre_dades.py` (mòdul `log`, lectura per USB)
- ⚠️ *Error a vigilar:* comprovar el polsador només "de tant en tant" en lloc de cada iteració

**Sessió 3 — Repte «vehicle amb aturada d'emergència» (producte, tanca el Projecte T2)**
- [ ] PRIMM amb `vehicle_seguretat.py` (predicció abans d'executar): què fa `"X"` si arriba en ple moviment
- [ ] Acompanyar el tancament individual: protocol complet F/B/L/R/S/X + STOP prioritari
- [ ] **Repte ⭐** de `Reptes_SA6.md` (nucli obligatori, 25' fila pròpia, termòstat de dues zones)
- [ ] **Mini-defensa breu (R4·DO), per MOSTREIG rotatiu:** 5-6 alumnes (FSM + una decisió justificada; registre rotatiu, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md#mostreig-rotatiu-de-la-mini-defensa-repte--sa1-sa8))
- [ ] Ampliació opcional: sensor de temperatura/DHT11 com a tercer estat ALERTA (**no nucli**)
- ⚠️ *Mantra:* les funcions de moviment i el protocol **no canvien** respecte a SA4/SA5; només s'hi afegeix la màquina d'estats amb STOP prioritari

**Sessió 4 — Prova pràctica T2 (individual, sessió sencera)**
- [ ] Repartir l'enunciat i el material individual necessari
- [ ] Supervisar en silenci; només aclarir dubtes d'enunciat, no de solució
- [ ] Recollir el material i les entregues al tancament

## 📊 3. Avaluació i evidències (a recollir)
- [ ] Repte **«vehicle amb aturada d'emergència»** (S3) → **R1**, **R3** (compta, Projectes 45 %)
- [ ] **Repte ⭐** (`Reptes_SA6.md`) fet i validat → **R1** (compta, Projectes 45 %)
- [ ] **Mini-defensa** (S3, R4·DO) → **R4** (fila «Defensa oral»)
- [ ] **Quadern tècnic** → **R4** (Quadern tècnic i pràctiques 25 %)
- [ ] **Observació d'aula** (seguretat amb el relé, autonomia) → **R5** (Actitud 10 %)
- [ ] **Prova pràctica T2** (S4) → R1, R3, R4 (Prova pràctica 20 %)
- [ ] Recollir **exit tickets** de la fitxa ampliada
- [ ] Traspassar valoracions al registre (nota **0–10**)

## 🪜 4. Atenció a la diversitat (previst per aquesta SA)
- [ ] **Bastida:** diagrama d'estats model (RUN/STOP/ALERTA) amb transicions ja indicades · esquelet de `actualitza_estat()` ja escrit (vegeu l'esquelet de [`00_Projecte_T2_Vehicle.md`](../00_General/00_Projecte_T2_Vehicle.md))
- [ ] **+ Ampliació (només reptes ⭐⭐/⭐⭐⭐, un cop fet el ⭐ obligatori):** semàfor amb botó prioritari · vehicle amb alerta de temperatura i registre de bord (vegeu `Reptes_SA6.md`)
- [ ] **Sense vehicle a punt:** la lògica de FSM/histèresi es treballa al simulador (`maquina_estats_semafor.py`, `termostat_histeresi.py`); `vehicle_seguretat.py` necessita el vehicle físic per als motors i el relé
