# SA1 · Checklist docent — Hola, robot!

**6 h (3 sessions) · micro:bit V2 sola · Criteris CA1.2, CA5.3 · Rúbriques R4 (documentació) i R5 (actitud)**

> Eina d'acció d'una cara. Condensa la [`SA1_guia_docent.md`](SA1_guia_docent.md) en punts verificables. Marca `[x]` a mesura que ho tinguis fet. **Quan s'usa:** imprimeix-lo en **preparar la SA** (§1) i tingues-lo **a taula a cada sessió** (§2–§4).

## 🧰 1. Logística prèvia (preparar abans de començar la SA)
- [ ] micro:bit V2 + cable USB per alumne/a a punt (o simulador com a pla B si no n'hi ha prou)
- [ ] Ordinadors amb accés a **python.microbit.org** (no cal compte ni instal·lació)
- [ ] Projector provat amb [`SA1_esquemes_connexions.md`](SA1_esquemes_connexions.md)
- [ ] **Imprimir:** [prova diagnòstica](SA1_prova_diagnostica.md) · [full de normes de seguretat](SA1_normes_seguretat.md) (per signar) · [plantilla fitxa-pòster](SA1_poster_robot_plantilla.md)
- [ ] Programes oberts i provats: `hola_mon` · `emocions_botons` · (ampliació `dau_sacseig`)
- [ ] Compartir rúbriques **R4 i R5** amb l'alumnat *abans* del producte (avaluació formativa)

## ⏱️ 2. Moments (punts de control per sessió)

**Sessió 1 — Què és un robot?**
- [ ] Activació: *"Quins robots tens a casa sense saber-ho?"*
- [ ] Model entrada→procés→sortida i anàlisi de 3 sistemes (Act. 1)
- [ ] Passar la **prova diagnòstica** (no qualifica → orienta el ritme)
- [ ] Tancament: presentar mètode de projecte (el quadern tècnic s'obre a la Sessió 2)
- ⚠️ *Error a vigilar:* confondre entrada (sensor) amb sortida (actuador)

**Sessió 2 — Arquitectura i seguretat**
- [ ] micro:bit real a la mà; etiquetar l'esquema de la placa (Act. 2)
- [ ] **Signatura del full de seguretat** (recollir-lo)
- [ ] Tour de l'editor python.microbit.org (simulador + transferència del `.hex`)
- [ ] **Obrir el quadern tècnic** (primera entrada)
- ⚠️ *Mantra:* la matriu de LED és entrada **i** sortida (mostra imatges i llegeix llum) · *Error:* pensar que és només decorativa

**Sessió 3 — El primer programa (PRIMM)**
- [ ] Mini-check individual (10', a l'inici — [banc SA1](../00_General/00_Mini_checks_individuals.md#sa1--mini-check-inici-de-la-sessió-3))
- [ ] Projectar `hola_mon.py` **sense executar-lo** → alumnat prediu (Act. 4)
- [ ] Executar → Investigar → Modificar → **Crea** `emocions_botons`
- [ ] **Repte ⭐** (`Reptes_SA1.md`, 25' fila pròpia) + 🤝 parella de lectura (5', dins)
- [ ] Mini-debat ètic (ODS) + presentar la fitxa-pòster
- ⚠️ *Error:* oblidar `from microbit import *` i no saber interpretar el `NameError`

## 📊 3. Avaluació i evidències (a recollir)
- [ ] **Repte ⭐** (`Reptes_SA1.md`) fet i validat → **R1** (compta, Projectes 45 %)
- [ ] **Fitxa-pòster** d'un robot real → **R4** (compta, Projectes 45 %)
- [ ] **Quadern tècnic** 1a entrada → **R4** (Quadern tècnic i pràctiques 25 %)
- [ ] **Observació d'aula** (autonomia, seguretat, responsabilitat) → **R5** (Actitud 10 %)
- [ ] Recollir **exit tickets** de la fitxa ampliada
- [ ] Traspassar valoracions al registre (nota **0–10**)

## 🪜 4. Atenció a la diversitat (previst per aquesta SA)
- [ ] **Bastida:** esquema de la placa de referència · esquelet «Si t'encalles» a la pàgina de la pràctica d'`emocions_botons` · treball amb el simulador si falta placa
- [ ] **+ Ampliació (⭐⭐/⭐⭐⭐):** `dau_sacseig` (acceleròmetre + aleatorietat) · investigar un robot amb IA/autonomia avançada i preparar una defensa breu
