# SA9 · Checklist docent — Repte final integrador

**10 h (5 sessions; S5 = Prova pràctica T3) · tot el maquinari del curs · Criteris CA1.1-CA5.3 (tots) · Rúbriques R1-R5 (totes)**

> Eina d'acció d'una cara. Condensa la [`SA9_guia_docent.md`](SA9_guia_docent.md) en punts verificables. Marca `[x]` a mesura que ho tinguis fet. **Quan s'usa:** imprimeix-lo en **preparar la SA** (§1) i tingues-lo **a taula a cada sessió** (§2-§5).

## 🧰 1. Logística prèvia (preparar abans de començar la SA)
- [ ] micro:bit V2 + Micro:shield + cable USB per alumne/a a punt
- [ ] Rover de SA7-SA8 de cada alumne a punt (motors, sensors bàsics funcionant)
- [ ] Kits Keyestudio 1-3 complets disponibles; comprovar especialment **bomba d'aigua + relé + sensor d'humitat del terra** (repte de reg) i **PIR**/**NeoPixel** (repte 3/4) abans de la S1
- [ ] [Banc de reptes](SA9_reptes_proposats.md) imprès o projectable per a la S1
- [ ] [Plantilla de projecte](codi/plantilla_projecte/plantilla_projecte.py) i [plantilla del dossier](SA9_dossier_plantilla.md) accessibles a l'alumnat
- [ ] Pistes de la S5 (línia + obstacles) muntades i provades, en nombre suficient per als torns (vegeu §Organització de la S5 de la guia)
- [ ] Compartir **totes** les rúbriques (R1-R5) amb l'alumnat des de la **Sessió 1** (avaluació formativa)
- [ ] Tenir l'enunciat de [`Avaluació/Prova_practica_T3.md`](../../Avaluació/Prova_practica_T3.md) preparat abans de la S5

## ⏱️ 2. Moments (punts de control per sessió)

**Sessió 1 — Idear**
- [ ] Presentar el banc de reptes i el maquinari de reserva
- [ ] Acompanyar la tria individual del repte + requisits mínims + esbós
- [ ] Comprovar que ningú s'ha quedat sense repte viable amb el seu maquinari
- ⚠️ *Error a vigilar:* repte massa ambiciós per al temps disponible

**Sessió 2 — Prototipar**
- [ ] Mini-check individual (10', a l'inici — [banc SA9](../00_General/00_Mini_checks_individuals.md#sa9--mini-check-inici-de-la-sessió-2))
- [ ] Modelatge de `plantilla_projecte.py` (percep/decideix/actua)
- [ ] Ronda de muntatge del component nou de cada repte (atenció especial: relé+bomba, PIR, NeoPixel)
- [ ] Acompanyar la primera integració de codi (prototip mínim viable)
- ⚠️ *Error a vigilar:* bomba connectada directament al Micro:shield, sense relé

**Sessió 3 — Provar i millorar**
- [ ] Acompanyar proves sistemàtiques (DEPURA) i una 1a iteració de millora
- [ ] Reservar 20-30' finals per a **defenses esglaonades** de qui ja estigui llest
- [ ] Avançar el dossier tècnic (§1-§3)
- ⚠️ *Error a vigilar:* només es prova el "cas feliç", sense cap prova de límit

**Sessió 4 — Comunicar**
- [ ] Acompanyar el tancament del dossier tècnic (§4-§9)
- [ ] Dirigir les **defenses orals individuals** (5' + preguntes), moderant el torn de manera equilibrada
- [ ] Recollir dossiers i repartir el repàs exprés (deures per a la T3)
- ⚠️ *Error a vigilar:* dossier incomplet arribat a la defensa per manca de control en sessions anteriors

**Sessió 5 — Prova pràctica T3 (NO és sessió de projecte)**
- [ ] Organitzar estacions rotatives (taula + pista), torns de 8-10'
- [ ] Recordar: no reavalua el projecte; és destreses individuals de SA7-SA8

## 📊 3. Avaluació i evidències (a recollir)
- [ ] **Producte «rover ampliat»** (S4) → **R1, R2, R3** (compta, Projectes 45 %)
- [ ] **Dossier tècnic complet** (S4) → **R4** (Quadern tècnic i pràctiques 25 %)
- [ ] **Defensa oral individual** (S4, R4·DO nivell alt) → **R4** (fila «Defensa oral», Projectes 45 %)
- [ ] **Observació del procés** (S1-S4) → **R5** (Actitud 10 %)
- [ ] **Prova pràctica T3** (S5) → Proves pràctiques (20 %), **separada**, no reavalua el projecte
- [ ] Recollir **coavaluacions** (2 estrelles i un desig) de les defenses
- [ ] Traspassar valoracions al registre (nota **0-10**)

## 🪜 4. Atenció a la diversitat (previst per aquesta SA)
- [ ] **Bastida:** reptes ⭐ amb nucli acotat; plantilla de projecte i de dossier ja donades; fites per sessió
- [ ] **+ Ampliació:** ampliacions ⭐⭐/⭐⭐⭐; combinar dos reptes; vincle a competició o TR (vegeu `SA9_reptes_proposats.md`)
- [ ] **Sense rover/kit a punt:** lògica al simulador (ràdio i `log` sí es simulen), valors de sensor simulats en variables

## 🎤 5. Defenses i S5 (organització)
- [ ] Defenses esglaonades des de la S3 si el grup és nombrós (>15-18 alumnes)
- [ ] Mai ajornar cap defensa a la S5 (és un instrument separat)
- [ ] S5: nombre de pistes ↔ mida dels grups de torn ja calculat abans de començar
