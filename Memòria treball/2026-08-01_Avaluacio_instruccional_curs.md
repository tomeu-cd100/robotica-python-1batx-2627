# Avaluació instruccional del curs — corba d'aprenentatge, exercicis i resultats

> Auditoria pedagògica independent (01/08/2026) amb tres anàlisis paral·leles sobre el
> material real: (1) mapa de conceptes i càrrega cognitiva sessió a sessió, (2) tipologia
> PRIMM i gradient dels exercicis, (3) alineació objectius↔activitats↔avaluació.
> Pregunta guia: **en acabar el curs, l'alumnat sabrà programar en Python/MicroPython?**

## Dictamen global

| Dimensió | Valoració | Síntesi |
|---|---|---|
| Corba d'aprenentatge | 🟡 Bona amb 2 pics i 1 forat | PRIMM ben aplicat a T1; pics de sobrecàrrega a S19 (5 conceptes) i sobretot S28 (6 conceptes); SA7 té 3 sessions planes seguides just abans del pic |
| Exercicis | 🟡 Llegir/modificar excel·lent, escriure insuficient | El «Make» (escriure codi de zero) viu a la capa OPCIONAL (reptes) i a SA9; zero pràctica de fluïdesa (katas/Parsons); cap qüestionari demana codi |
| Objectius i resultats | 🟡 Fins per SA, difusos a nivell de matèria | «Saber programar» només és objectiu explícit 1 cop de 8; a la resta és instrumental al robot |
| Avaluació | 🟠 Risc estructural | Pes efectiu de «programar codi» a la nota final ≈ 30-33 %; la prova T3 només té ~20-25 % de codi nou; els mini-checks (l'instrument més vàlid) no qualifiquen. **Es pot aprovar sense saber escriure un programa sol.** |
| Coherència tècnica | 🟢 Excel·lent | Espiral maquinari/funcions impecable; ponts explícits entre SA; pins/protocols consistents |

**Resposta a la pregunta guia:** l'alumnat que segueixi NOMÉS el nucli obligatori acabarà
sabent llegir, predir, modificar i muntar amb solvència, però la seva escriptura autònoma
de codi no està garantida ni prou avaluada. Qui faci els reptes opcionals i s'impliqui a
SA9 sí que en sortirà programant. El risc és l'alumne del mig.

## Evidència principal (resum; detall als tres informes de sessió)

### Corba
- **Forats de producció**: `return` es declara objectiu a SA4 però la primera escriptura
  real és a un repte de SA6; `global` s'usa des de SA4 i s'exigeix a la prova T2 **sense
  cap explicació en prosa a tot el curs**; `for` mai es formalitza com a estructura
  general (només el cas `range` de `pwm_led_rgb`); `try/except` apareix un únic cop
  (SA8) i es passa de llegir-lo a escriure'l al producte avaluable sense graó.
- **Pics**: S19 (SA6 S1: FSM + diccionari + histèresi + global en 2 h) i S28 (SA8 S2:
  I2C + bits + tupla + for-sobre-llista + dict dinàmic + try/except = 6 conceptes nous).
- **Valls**: S23-S25 (SA7 sencera menys la S4) sense cap concepte nou de programació —
  espai desaprofitat just abans del pic S28.
- **Repàs espaiat**: els ponts contextuals entre SA són bons, però la «graella de repàs
  espaiat» que la metodologia (doc 04) i l'avaluació (doc 06) citen com a peça central
  (`Classes/00_General/00_Banc_activacio_repas.md`) **no existeix al repositori**.
- El patró `percep()/decideix()/actua()` de la plantilla de SA9 no s'usa a cap programa
  anterior: l'alumne l'estrena en producció autònoma.

### Exercicis
- Tots els `Reptes_SAn.md` diuen «comença'l quan tinguis el nucli al dia»: el gruix de
  codi NOU que escriu l'alumne és opcional. SA6 no té cap activitat de Make pur al nucli.
- Únic exercici curt de producció sense bastida de tot el curs: el mini-check de SA4
  («escriu una funció amb paràmetre, sense apunts») — i no qualifica.
- Els 9 qüestionaris de conceptes: 10 preguntes d'opció múltiple cadascun, **cap** demana
  escriure, completar, corregir o traçar codi.
- Temps net d'escriptura de codi per l'alumnat: minoritari (est. 15-40 % del temps de
  pràctica segons SA); sessions senceres sense codi (SA2-S4, SA4-S4, SA7-S0 — fabricació).

### Avaluació
- Validesa de proves com a mesura de programar: T1 ≈ 60 % codi nou (bona), T2 ≈ 70-80 %
  però reproduint patrons ja resolts, **T3 ≈ 20-25 %** (domina calibratge/muntatge i
  reproducció; el propi document diu «no s'avalua contingut nou»).
- Després de SA4, **cap prova torna a exigir escriure una funció nova amb paràmetres i
  return**. CA1.2 (depuració/REPL) no té cap ítem puntuat a cap prova.
- Pes efectiu de «programar codi individualment» a la nota final ≈ **30-33 %** (projectes
  45 % amb R1 diluïda entre 3-4 rúbriques + quadern 25 % dominat per R4 + proves 20 %
  amb T3 fluixa + actitud 10 %). Un alumne fort en muntatge, documentació i actitud pot
  aprovar amb capacitat de programació feble.
- El bucle formatiu (mini-checks amb semàfor i derivació a seccions concretes) és
  específic i ben dissenyat, però tot fora de nota i sense coavaluació estructurada.

## Pla de millora recomanat (prioritzat)

### P1 — Garantir producció de codi obligatòria i freqüent (impacte màxim)
1. **Kata d'obertura (10')** a cada sessió de S4 en endavant: exercici curt d'ESCRIPTURA
   amb progressió Parsons → completar buits → escriure de zero, sobre el concepte de fa
   1-2 setmanes (retrieval espaiat). Materialitza'l creant el fitxer que ja se cita:
   `Classes/00_General/00_Banc_activacio_repas.md` (banc de 30-40 katas, un per sessió,
   amb solució). Cobreix alhora el forat de repàs espaiat i el de fluïdesa.
2. **Promoure el repte ⭐ de cada SA a nucli obligatori** (els ⭐⭐/⭐⭐⭐ resten opcionals).
   És el canvi més barat per garantir que TOTHOM escriu codi nou a cada SA.
3. **Un mini-check d'escriptura per SA** (com el de SA4) en lloc de teòric, i que el
   millor de cada trimestre qualifiqui (p. ex. 5 punts dins la dimensió proves).

### P2 — Tapar els forats de la corba
4. `return`: afegir a SA4 S2 una activitat nucli on l'alumne escrigui una funció que
   RETORNA un valor i l'usa (p. ex. `distancia_en_passos(cm)`).
5. `global`: explicació en prosa (àmbit de variables, per què cal) a l'EXPLICACIO de
   `control_per_botons` (SA4) + 1 kata.
6. `for`: formalitzar-lo a SA2 (fitxa: mecanisme general + exercici de modificar) i
   introduir `for element in col·leccio` a SA5 (llistes de missatges) en lloc
   d'estrenar-lo a SA8.
7. **Descarregar S28** aprofitant les valls de SA7: moure `try/except` (amb kata) i el
   `for` sobre col·lecció a SA7 S2-S3 (context: llegir llistes de missions); a S28
   queden I2C/bits (llegir) + dict dinàmic. De 6 conceptes a 3.
8. Introduir el patró `percep/decideix/actua` refactoritzant `comportaments.py` (SA8 S1)
   perquè l'alumne el VEGI funcionar abans d'escriure'l a SA9.

### P3 — Reforçar la validesa de l'avaluació
9. Prova T2 i T3: **ítem obligatori de 2 punts «escriu una funció nova»** (T2: funció amb
   paràmetre i return; T3: comportament nou del rover no vist a classe, p. ex. «aparca
   quan detecta la línia dues vegades»). A T3, reequilibrar el barem: calibratge màx. 2
   punts (ara 3).
10. Qüestionaris: substituir 3 de les 10 preguntes per «què imprimeix aquest codi?» /
    «completa la línia que falta» / «troba l'error».
11. Rúbrica de producte: subcriteri explícit «codi escrit per l'alumne» amb pes mínim
    del 40 % de R1 dins de cada projecte (garanteix pes real de programar a la nota).
12. Objectius del doc 02: desglossar l'objectiu 2 en 3 resultats observables (escriure
    programes amb estructures de control; definir i usar funcions pròpies; depurar amb
    REPL/simulador) i vincular-los 1:1 amb instruments.

### P4 — Complements
13. Coavaluació lleugera de codi (sense producte compartit): «parella de lectura» de 5'
    amb checklist de 3 ítems (noms de variables, un comentari útil, cap número màgic).
14. Registrar el tipus d'error als mini-checks (sintaxi vs concepte), no només el color.

## Cost estimat d'implantació

P1+P2 ≈ crear 1 banc de katas + retocs a 6-8 documents i 3-4 programes; P3 ≈ retocs a
2 proves, 9 qüestionaris i 2 documents d'avaluació. Tot compatible amb el calendari
actual (les katas caben als 10' d'activació ja previstos a l'estructura de sessió).

*Document d'auditoria interna. Llicència CC BY-SA 4.0.*
