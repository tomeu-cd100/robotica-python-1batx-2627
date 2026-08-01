# SA8 · Checklist docent — Autonomia i telemetria

**6 h (3 sessions, comprimible a 4 h) · micro:bit V2 + Micro:shield + Kit 3 · rover T3 de la SA7 · Criteris CA1.1, CA3.1, CA4.2 · Rúbriques R1, R3 (Integració) i R4 (documentació)**

> Eina d'acció d'una cara. Condensa la [`SA8_guia_docent.md`](SA8_guia_docent.md) en punts verificables. Marca `[x]` a mesura que ho tinguis fet. **Quan s'usa:** imprimeix-lo en **preparar la SA** (§1) i tingues-lo **a taula a cada sessió** (§2–§4).

## 🧰 1. Logística prèvia (preparar abans de començar la SA)
- [ ] micro:bit V2 + Micro:shield + cable USB per alumne/a a punt
- [ ] Rover T3 de la SA7 a punt (motors, HC-SR04, seguidor de línia funcionant)
- [ ] DHT11 i IMU MPU6050 del Kit 3 disponibles per alumne/a (BMP280/CCS811 per a qui vulgui l'ampliació)
- [ ] Segona micro:bit disponible per parella (torns entre companys) o la del docent, per fer d'estació base
- [ ] Ordinadors amb accés a python.microbit.org i a Teachable Machine provats abans de la S3
- [ ] Projector provat amb [`SA8_esquemes_connexions.md`](SA8_esquemes_connexions.md)
- [ ] Programes oberts i provats: `comportaments` · `telemetria_radio` · `estacio_base`
- [ ] Compartir rúbriques **R1, R3 i R4** amb l'alumnat *abans* del producte (avaluació formativa)
- [ ] **Decidit el mode (6 h o comprimit a 4 h)** segons el pla de contingència (doc. 08) — si comprimit, fusiona S1+S2

## ⏱️ 2. Moments (punts de control per sessió)

**Sessió 1 — Sensors avançats: llegir el Kit 3**
- [ ] Presentar els 4 sensors del Kit 3 i explicar per què el nucli programa només IMU+DHT11 (I2C i time-of-flight, ja coneguts)
- [ ] Modelatge de `comportaments.py`: repàs de la FSM SEGUIR/ESQUIVAR/RECUPERAR
- [ ] Acompanyar el muntatge del DHT11 (P8) i l'IMU (I2C, P19/P20) i el disseny del format de missatge
- ⚠️ *Error a vigilar:* confondre "estat de la FSM" (decisió pròpia) amb "valor d'un sensor" (dada externa)

**Sessió 2 — Telemetria per ràdio: enviar i registrar**
- [ ] Modelatge de `telemetria_radio.py`: FSM + sensors + `radio.send()` amb prefix `"TEL:"`
- [ ] Modelatge d'`estacio_base.py`: cada alumne l'escriu, encara que s'executi temporalment en una altra placa
- [ ] **Mini-check individual** a l'inici (10', [banc SA8](../00_General/00_Mini_checks_individuals.md)) — enviar un valor de sensor per ràdio
- [ ] Acompanyar el muntatge i les proves per parelles (torns de placa d'estació base)
- ⚠️ *Error a vigilar:* `group` o `PREFIX` diferents entre les dues plaques d'una mateixa parella

**Sessió 3 — IA aplicada al control i producte**
- [ ] Demostració/pràctica guiada de classificació de patrons (Teachable Machine), amb pla B sense internet
- [ ] Bloc «Ètica de dades i IA» (RGPD, biaix, consentiment) aplicat a la telemetria del rover
- [ ] Acompanyar el tancament del producte (mínim dos sensors, ràdio, registre)
- [ ] **Repte ⭐** de `Reptes_SA8.md` (nucli obligatori, 25' fila pròpia, estació meteorològica amb alertes)
- [ ] **Mini-defensa breu (R4·DO), per MOSTREIG rotatiu:** 5-6 alumnes (una decisió justificada; registre rotatiu, vegeu [`00_Guia_defensa_oral.md`](../00_General/00_Guia_defensa_oral.md#mostreig-rotatiu-de-la-mini-defensa-repte--sa1-sa8))
- ⚠️ *Error a vigilar:* que la reflexió d'IA es quedi en generalitats sense connectar-la amb `mpu_orientacio()`

## 📊 3. Avaluació i evidències (a recollir)
- [ ] **Sistema de telemetria del rover** (S3) → **R1**, **R3** (Integració) (compta, Projectes 45 %)
- [ ] **Repte ⭐** (`Reptes_SA8.md`) fet i validat → **R1** (compta, Projectes 45 %)
- [ ] **Mini-defensa** (S3, R4·DO) → **R4** (fila «Defensa oral»)
- [ ] **Quadern tècnic** (format de missatge, reflexió d'IA i ètica de dades) → **R4** (Quadern tècnic i pràctiques 25 %)
- [ ] **Observació d'aula** (autonomia i responsabilitat amb sensors i dades) → **R5** (Actitud 10 %)
- [ ] Recollir **exit tickets** de la fitxa ampliada
- [ ] Traspassar valoracions al registre (nota **0–10**)

## 🪜 4. Atenció a la diversitat (previst per aquesta SA)
- [ ] **Bastida:** format de missatge de telemetria model ja donat (p. ex. `"TEL:T:23.5"`); esquelet de `envia_lectura()`/`analitza()` ja escrit
- [ ] **+ Ampliació:** BMP280/CCS811 al mateix bus I2C, protocol propi més ric, comparació classificació manual vs IA (vegeu els reptes **⭐⭐/⭐⭐⭐** de `Reptes_SA8.md`; el ⭐ ja és nucli obligatori, no ampliació)
- [ ] **Sense rover/Kit 3 a punt:** lògica del protocol al simulador (ràdio i `log` sí es simulen) amb valors de sensor simulats en variables
