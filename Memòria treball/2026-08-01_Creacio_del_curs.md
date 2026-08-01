# Memòria de treball — Creació del curs «Robòtica amb Python» (1r Batxillerat)
### Data: 1 d'agost de 2026

Resum de la creació completa del curs **Robòtica amb Python**, optativa pròpia de
1r de Batxillerat (LOMLOE, Catalunya), des de la infraestructura fins al
tancament i QA global. Aquest repositori és una **adaptació** del curs germà
[«Robòtica» (Arduino + micro:bit)](../../Curs%202627%201%20Batx%20Robotica/):
mateix marc normatiu i estructura de repositori, maquinari i llenguatge diferents.

---

## 1. Decisions clau que van fixar el disseny del curs

| Decisió | Per què |
|---|---|
| **Optativa pròpia de centre**, no "Robòtica" ni "Programació" oficials | El nom, l'anual de 2 h/setmana i el 100 % Python no encaixen amb cap de les dues optatives oficials de 1r Batx; es tracta com a referents no vinculants, ancorada a la Competència específica 5 de Tecnologia i Enginyeria I (bloc Automatització) — vegeu `Normativa/01_Normativa_LOMLOE_RoboticaPython_1Batx.md`. |
| **Tot el treball és individual** (mai en parelles ni en grup) | Amb un únic kit (micro:bit + Micro:shield + Keyestudio) per alumne, cada alumne construeix, cabla i programa el seu propi exemplar dels tres robots del curs; l'ajuda entre iguals es fomenta com a dinàmica d'aula, no com a producte compartit (`04_Metodologia.md` §4.3). Simplifica també l'avaluació: cap rúbrica de coavaluació de grup. |
| **micro:bit V2 + Micro:shield + Keyestudio, MicroPython exclusiu** | Substitueix l'Arduino C/C++ del curs germà. Un sol llenguatge (`.py`) i un sol maquinari de principi a fi: menys càrrega cognitiva de canvi d'entorn, simulador natiu (python.microbit.org) sense instal·lació. |
| **Fil conductor mascota → vehicle → rover** | Un projecte trimestral per trimestre, no despenjat de les SA: **T1 (mascota reactiva)** tanca a final del 1r trimestre amb els reptes de SA2-SA3; **T2 (vehicle teledirigit)** es munta a SA4 i es tanca a final del 2n; **T3 (rover autònom)** **no és un xassís nou** sinó el vehicle de T2 amb dues peces d'ampliació impreses en 3D, muntat a la Sessió 0 del 3r trimestre abans de SA7. Dona sentit acumulatiu al curs: cada trimestre "hereta" i amplia el robot anterior en lloc de començar de zero. |
| **Mapa de pins únic i vinculant** | `Classes/00_General/00_Fil_conductor_construccions.md` §1b és la **font única** del cablatge de tots tres robots: cada guia docent i esquema hi remet en lloc de repetir (i poder desincronitzar) la taula de pins. Evita l'error més probable en un curs amb maquinari reutilitzat trimestre a trimestre (pins que "es mouen" d'un projecte a l'altre). |
| **Model d'avaluació:** R1-R5 + una prova pràctica individual per trimestre integrada a l'última sessió de SA3/SA6/SA9 | No costa hores extra (s'aprofita la sessió que ja hi havia). T1 i T2 són individuals per defecte; el radar previ són els mini-checks (10' sense ajuda, cada SA). Full de qualificació creua criteris CA amb rúbriques; quadern tècnic individual compta el 25 % de R4. |

## 2. Com es va construir (fases)

1. **Infraestructura** (Task 1): estructura de carpetes, `CLAUDE.md` amb les
   regles del repositori, generador web (`web/_generador/generar.py`) i QA
   automàtic (`tools/qa.py`), adaptats del curs germà substituint Arduino per
   micro:bit/MicroPython.
2. **Normativa i programació didàctica** (Tasks 2-6): síntesi legal, objectius,
   sabers, metodologia, atenció a la diversitat, avaluació, rúbriques,
   seqüenciació anual (68 h en 9 SA + marge) i inventari/pressupost de
   materials.
3. **Fil conductor i material d'aula SA1-SA9** (Tasks 7-15): un cicle
   guia docent → fitxa base → esquemes i codi → fitxa ampliada i reptes per
   cada SA, amb el fil mascota/vehicle/rover integrat als projectes
   trimestrals de `Classes/00_General/`.
4. **Avaluació** (Task 16): les tres proves pràctiques trimestrals (enunciat
   per nivells, graella de correcció, solució orientativa) i el full de
   qualificació de competències.
5. **Recursos i simulacions** (Task 17): enllaços de professorat validats,
   plantilles de tall làser, activació de la secció Simulacions (micro:bit
   simulator com a eina principal; Wokwi només per a l'ampliació opcional
   amb Raspberry Pi Pico).
6. **Tancament** (Task 18, aquest document): QA global a zero, web final i
   aquesta memòria.

## 3. Feina de tancament (Task 18)

El QA complet (`py tools/qa.py`, sense `--nomes-sintaxi`) donava **713
problemes** en començar aquest task. Les causes, totes arreglades:

- **Secció «Reptes» sense pàgina d'entrada**: `Reptes/` no tenia `README.md`
  (a diferència de `Simulacions/`, activada al Task 17), de manera que
  `reptes/index.html` no es generava i **710 de les 713** referències
  trencades hi apuntaven. Creat `Reptes/README.md` seguint el mateix patró.
- **3 portades de projecte trimestral inexistents**: `generar.PROJECTES`
  referenciava `00_Projecte_T{1,2,3}_portada.md` a `Classes/00_General/`,
  mai creades. Escrites: una portada breu per projecte (què és el robot,
  maquinari, enllaç al dossier complet).
- **Material imprimible mai creat**: `alumnat.html` i les fitxes de SA1-SA2
  enllaçaven `impresos/Blocs_Programacio_Offline.html` i
  `impresos/Blocs_Diagrames_Flux.html` (48 blocs de codi retallables i peces
  de diagrama de flux), però `Classes/00_General/impresos/` no existia.
  Creats els dos fulls HTML autocontinguts (imprimibles a PDF via Chrome
  headless, com la resta de material imprimible del curs).
- **`00_Targetes_rescat.md` inexistent**: enllaçat des de
  `05_Atencio_a_la_diversitat.md` però mai escrit. Creat: pistes en 3 nivells
  (pregunta conceptual → pas concret → fragment amb `___`) per SA1-SA9.
- **Enllaç trencat al solucionari del dossier de la mascota** (apuntava a un
  `Solucionari_T1_SA1-SA3.md` que mai va existir) i **README desactualitzat**
  de `Reptes/Solucionari/` (deia «SA2-SA8 pendents» quan ja hi eren): tots
  dos corregits per apuntar als solucionaris reals per SA.
- **Href hardcoded desincronitzat**: la portada docent enllaçava
  `classes/00-general/00-fil-conductor-robots.html`, un nom de fitxer que
  havia canviat a `00-fil-conductor-construccions.html`; substituït per
  `find_out()` (com la resta d'enllaços de la portada) perquè no es pugui
  tornar a desincronitzar en un rename futur.
- **Bug latent de `comprova_quadern()`**: llegia la guia docent de cada
  sessió sense comprovar-ne l'existència (`FileNotFoundError` si en faltava
  una). Ja no petava (totes hi són), però s'ha blindat amb una comprovació
  explícita i un missatge d'error net, per si una guia futura es mou o
  s'esborra per error.
- **CI en mode `--nomes-sintaxi`**: `.github/workflows/qa.yml` saltava els
  checks de cobertura/contingut amb un TODO pendent del material complet.
  Tret el flag: el CI executa ara el QA complet.
- **Placeholder «~30 alumnes»**: a `08_Sequenciacio_temporal_anual.md`,
  corregit a la forquilla real (15-20 alumnes), coherent amb
  `09b_Guia_compra_pressupost.md`.
- **`REPO_SLUG` suposat**: marcat explícitament com a placeholder pendent
  (`PENDENT-DOCENT/robotica-python-1batx-2627`) amb instrucció a
  `GUIA_INICI_DOCENT.md` de substituir-lo pel repositori real abans de
  publicar.
- **Frase confusa a la guia de SA8** («mateix criteri que SA6 amb DHT11»,
  quan el nucli de SA6 usa `temperature()` intern i el DHT11 hi és només
  ampliació): reformulada per no donar a entendre que el nucli de SA6
  programava el DHT11.
- **`PROVES` del quadern tècnic amb títol «TODO»**: `quadern_sessions.py`
  tenia el títol de les tres proves trimestrals pendent des d'abans del
  Task 16; substituïts pels títols reals dels documents de
  `Avaluació/Prova_practica_Tn.md».

Amb tots els punts anteriors corregits, es van regenerar tots els PDF
versionats pendents (fulls imprimibles i quaderns tècnics de cada trimestre,
via Chrome headless) i es va tornar a executar el QA complet.

## 4. Estat final del QA

```
py tools/qa.py
```

→ **`✅ QA net.`** (0 problemes, exit code 0). Únics avisos residuals (`⚠️`,
no bloquegen, exit code 0 igualment): dues línies de `[pii]` al fitxer de
tests del generador (`web/_generador/tests/test_generar_nucli.py`), que
contenen el correu del docent com a dada de prova intencionada del test de
classificació de PII — no és una fuita de dades real.

`py -3.13 -m pytest web/_generador/tests -q` → **55 passed**.

## 5. Fora d'abast d'aquest tancament (fase posterior)

- Publicació del repositori a GitHub i activació de Pages: preparada
  (`gh repo create`, push, Pages) però **no executada**; requereix
  confirmació explícita del docent i actualitzar `REPO_SLUG` amb el
  repositori real abans de generar la web definitiva.
- `Material Classroom/`: scripts data-driven per crear tasques, qüestionaris
  i rúbriques al Google Classroom del grup — quan el Classroom existeixi
  (setembre), amb la skill `classroom-sync`.
- Fotos reals de muntatges: els esquemes actuals són vectorials (SVG); les
  fotos dels tres robots muntats es faran al setembre amb el maquinari
  davant.
- Validació dels drivers MPU6050/DHT11 amb maquinari real (escrits i
  revisats sense placa física davant).
- Opció Raspberry Pi Pico (Wokwi): només si s'aprova la compra.
