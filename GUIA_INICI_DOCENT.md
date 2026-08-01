# Guia d'inici per al docent

Aquest document és el punt d'entrada del curs **Robòtica amb Python** (1r de
Batxillerat, optativa pròpia de centre, 2 h/setmana, curs 2026-2027). No repeteix
el contingut de cada document: t'hi porta, en l'ordre que té sentit llegir-lo.

## 1. Itinerari de lectura (abans de començar)

1. **Aquest document** — visió general, checklist d'arrencada i com fer servir la web.
2. **`README.md`** — què hi ha a cada carpeta, com es genera la web i com es passa el QA.
3. **`CLAUDE.md`** — regles del repositori (tot individual, MicroPython exclusiu, contracte de QA): útil si has d'editar o ampliar material.
4. **`Normativa/01_Normativa_LOMLOE_RoboticaPython_1Batx.md`** — per què aquesta matèria és legal com a optativa pròpia i com s'ancora a Tecnologia i Enginyeria I (necessari només si has de justificar-la a PEC/PGA/inspecció).
5. **`Programació didàctica/00_Index_general.md`** — mapa de tots els documents de programació (objectius, sabers, metodologia, avaluació, seqüenciació, les 9 SA).
6. Per al dia a dia, amb prou feines calen tres documents de `Programació didàctica/`:
   - **`04_Metodologia.md`** — com és una sessió tipus.
   - **`06_Avaluacio_criteris_qualificacio.md`** + **`07_Rubriques.md`** — com es qualifica.
   - **`08_Sequenciacio_temporal_anual.md`** — el calendari del curs, trimestre a trimestre.
7. **`Classes/00_General/00_Fil_conductor_construccions.md`** — els tres robots del curs (mascota → vehicle → rover) i el mapa de pins únic que els travessa. Llegeix-lo abans de la primera sessió de muntatge (SA2·S4): és el document que evita haver de rellegir el cablatge cada trimestre.
8. Per a cada sessió, la **SA corresponent** dins `Classes/SAn/`: comença sempre per la **guia docent**, després la **fitxa d'alumnat**, després **esquemes i codi**, i finalment la **fitxa ampliada i reptes** — és l'ordre de treball fixat a tot el curs.

**Temps de preparació estimat.** La lectura inicial (punts 1-7 d'aquest itinerari, un cop) porta unes **3-4 h**. Un cop rodant, preparar cada SA porta **~20 min** amb el `SAn_checklist_docent.md` (§1 «Logística prèvia») com a guió d'una cara. Per preparar **una sessió concreta** (p. ex. abans d'entrar a classe, o per recuperar un alumne que ha faltat) no cal rellegir res: el **`00_Quadern_sessions_docent.pdf`** (`Classes/00_General/pdf/`, generat per `web/_generador/generar_fulls_imprimibles.py`) reuneix, en una pàgina per sessió, la kata del dia, el mini-check i el repte ⭐ (quan toquen) i el checklist docent d'aquella sessió.

## 2. Maquinari

**micro:bit V2 + Micro:shield + sensors Keyestudio.** Tot el codi d'alumnat és
MicroPython (`.py`); no hi ha cap component ni codi Arduino en aquest curs. Es pot
treballar sense maquinari amb el **simulador de python.microbit.org** (l'eina
principal, vegeu `Simulacions/Simulador_microbit.md`); Wokwi és només per a
l'ampliació opcional amb Raspberry Pi Pico.

**Tot el treball de l'alumnat és individual**: cap activitat en parelles ni en grup.

## 3. Com fer servir la web

La web (`web/index.html`, un cop generada) és la manera còmoda de navegar el
material: té **vista alumnat** i **vista docent** (commutador a la capçalera —
la vista docent hi afegeix guies, solucionaris i material que no es reparteix a
classe) i un cercador global. Genera-la o regenera-la sempre que canviïs algun
`.md`:

```bash
py -m pip install -r web/_generador/requirements.txt
py web/_generador/generar.py
```

`web/` (excepte `_generador/`, `assets/css/estil.css`, `assets/js/lloc.js` i el
seu `README.md`) és artefacte generat: **no s'edita a mà**, es torna a generar.

### Abans de publicar a GitHub Pages

`web/_generador/generar.py` calcula els enllaços a GitHub (codi font, PDFs,
"veure a GitHub") a partir de `REPO_SLUG`, que **de moment és una suposició**
(`PENDENT-DOCENT/robotica-python-1batx-2627`): no hi ha encara cap repositori
creat. Abans de publicar:

1. Crea el repositori a GitHub (públic, com el curs germà) amb `gh repo create`.
2. Genera la web amb el repositori real: `REPO_SLUG="usuari/repo" py web/_generador/generar.py` (o edita el valor per defecte a `generar.py`).
3. Fes el push i activa **GitHub Pages** (branca o carpeta `web/`, segons com es publiqui el curs germà).

La publicació externa (pas 4 del pla de tancament del curs) **només es fa amb
confirmació explícita del docent**: no forma part de la feina automatitzada.

## 4. Passar el QA

```bash
py tools/qa.py
```

Comprova cobertura de les 9 SA, enllaços interns del web generat, quadre
d'hores, sintaxi dels `.py` d'alumnat i del solucionari, PII/RGPD, PDFs
versionats, mojibake i coherència dels projectes trimestrals. Ha de donar
**«✅ QA net.»** (0 problemes; els avisos `⚠️` de PDFs pendents de regenerar no
bloquegen). És exactament el que executa el CI (`.github/workflows/qa.yml`) a
cada push i pull request.

## 5. Classroom (fase posterior)

Encara no hi ha Classroom del grup: quan es creï (setembre), les tasques,
qüestionaris autocorrectius i rúbriques s'hi pugen amb la skill
`classroom-sync`, a partir del material ja validat d'aquest repositori
(`Material Classroom/`, pendent de generar-se llavors — no abans, perquè
necessita l'ID real del Classroom).

## 6. Checklist d'arrencada (abans del setembre)

- [ ] **Aprovació PEC/PGA**: la matèria és una **optativa pròpia de centre**
  (no una de les optatives oficials "Robòtica"/"Programació"): ha de constar
  al Projecte Educatiu de Centre i a la Programació General Anual del curs
  2026-2027, amb el nom exacte «Robòtica amb Python» i les 2 h/setmana. Vegeu
  `Normativa/01_Normativa_LOMLOE_RoboticaPython_1Batx.md` per a l'argumentari
  complet si cal justificar-la.
- [ ] **Franja horària**: confirma amb direcció/cap d'estudis la franja de 2 h
  setmanals dins l'estructura d'optatives de 1r de Batxillerat (Decret
  103/2026): cada centre la fixa dins els mínims/màxims normatius.
- [ ] **Compra de consumibles**: revisa `Programació didàctica/09b_Guia_compra_pressupost.md`
  (estimació ~150-270 €/curs per al grup real de 15-20 alumnes) i
  `09c_Inventari_kits_disponibles.md` (què ja hi ha al centre) abans de fer
  la comanda; confirma el nombre real d'alumnes matriculats per ajustar la
  xifra.
- [ ] **Validar drivers amb maquinari real**: el codi dels sensors MPU6050
  (IMU, SA8) i DHT11 (SA6 ampliació, SA8 nucli) s'ha escrit i revisat sense
  placa física davant. Abans de la primera sessió que els fa servir, munta'ls
  i comprova la lectura real (pins, adreça I2C, temps entre lectures del
  DHT11): és l'únic material del curs que no s'ha pogut provar amb maquinari.
- [ ] **Imatges/fotos reals de muntatges**: els esquemes actuals són vectorials
  (SVG); les fotos dels tres robots muntats es faran al setembre amb el
  maquinari davant (fora d'abast d'aquest tancament).
- [ ] **Repositori GitHub**: crea'l i publica la web (§3) quan ho confirmis
  explícitament — no s'ha fet automàticament.

## 7. Estat del material (a la data de tancament)

- ✅ Infraestructura, generador web, QA automàtic complet (`py tools/qa.py`
  net, sense `--nomes-sintaxi`).
- ✅ Programació didàctica completa (00-18), les 9 SA amb guia docent + fitxa
  + esquemes + codi + reptes + solucionari, avaluació (proves T1-T3 + full de
  qualificació) i recursos (enllaços, plantilles de tall làser, simulacions).
- ⏳ Pendent de fase posterior (fora d'aquest tancament): Classroom real,
  fotos de muntatges amb maquinari, publicació del repositori a GitHub
  (només amb confirmació del docent).
