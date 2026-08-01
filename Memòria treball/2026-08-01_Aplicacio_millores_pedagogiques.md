# Memòria de treball — Aplicació de les millores pedagògiques (P1-P4)
### Data: 1 d'agost de 2026

Registre de l'aplicació del pla de millora sorgit de l'auditoria pedagògica
(`2026-08-01_Avaluacio_instruccional_curs.md`): 6 tasks que despleguen les
prioritats **P1-P4** de l'informe. Aquest document tanca el cicle de millora.

---

## 1. Què s'ha aplicat (P1-P4 → tasks 1-6)

| Prioritat de l'auditoria | Task | Què s'ha creat/modificat | Commits |
|---|---|---|---|
| **P1.1** Repàs espaiat i fluïdesa d'escriptura | Task 1 | Banc de 21 katas d'activació (`Classes/00_General/00_Banc_activacio_repas.md`), mapades sessió a sessió S4-S33, amb progressió Parsons → completar buits → escriure de zero. | `5598104`..`0d457af` |
| **P2.4-2.8** Forats de la corba (`return`, `global`, `for`, `try/except`, `percep/decideix/actua`) | Task 2 | Activitats nucli afegides a SA4 (return), SA4 (global en prosa), SA2/SA5 (for), SA7 (try/except desplaçat des de SA8 per descarregar S28), SA8 (patró percep/decideix/actua abans de SA9). | `4c0a2d1`..`926acaf` |
| **P1.2-1.3** Repte ⭐ nucli obligatori i mini-checks qualificables | Task 3 | El repte ⭐ de cada SA (SA2-SA8) passa de la capa opcional al nucli obligatori (mateix temps de pràctica). Mini-checks d'escriptura individuals: el **millor del trimestre qualifica un 5 %** dins «Proves pràctiques» (`06_Avaluacio_criteris_qualificacio.md` §6.3). | `8f52561`..`7262762` |
| **P3.10** Validesa dels qüestionaris | Task 4 | 27 preguntes noves de traça/completar/corregir codi repartides als 9 qüestionaris de conceptes (abans, 100 % opció múltiple sense codi). | `2791ac7`..`cb4aff2` |
| **P3.9, P3.11, P3.12** Validesa de proves i rúbriques | Task 5 | Ítem obligatori «escriu una funció nova» (2 punts) a T2 i T3; calibratge de T3 retallat de 3 a 2 punts; subcriteri «codi escrit per l'alumne» ≥ 40 % de R1 amb mini-entrevista de defensa; objectiu 2 desglossat en 2a/2b/2c amb instruments propis. | `cb4aff2`..`5625b8c` |
| **P4.13** Coavaluació de lectura lleugera | Task 6 (aquest) | `Classes/00_General/00_Parella_de_lectura.md`: protocol de 5', checklist de 3 ítems, sense producte compartit, no qualifica. Referenciat des de les 7 guies docents SA2-SA8. `04_Metodologia.md` actualitzat perquè el discurs reculli katas, repte ⭐ nucli i parella de lectura, i matisi la frase sobre coavaluació («no hi ha coavaluació de **grup** amb nota; sí parella de lectura formativa individual»). | *(vegeu §3)* |

**P4.14** (registrar el tipus d'error als mini-checks) ja es va cobrir de retruc als
Tasks 3 i 5: el mini-check anota sintaxi/concepte/descuit i alimenta l'indicador
de semàfors de `06b_Avaluacio_programacio_i_practica_docent.md`.

## 2. Què queda per validar a l'aula (no es pot verificar des del repositori)

- **Temps reals de les katas d'activació (10')**: el banc assumeix que cada kata
  cap en 10' incloent correcció ràpida a mà alçada; cal cronometrar les primeres
  sessions de cada trimestre i ajustar la progressió Parsons/buits/zero si es
  desborda sistemàticament.
- **Temps reals de la parella de lectura (5')**: el guió assumeix 30" d'aparellar
  + 2' de lectura silenciosa per banda + 30" de comentari; amb grups nombrosos o
  poc entrenats en donar feedback concret, les primeres sessions poden allargar-se
  — val la pena observar-ho a SA2-SA3 i, si cal, reduir la checklist a 2 ítems
  temporalment.
- **Mini-entrevista de R1** (introduïda al Task 5 dins el subcriteri «codi escrit
  per l'alumne» ≥ 40 %): cal comprovar a la pràctica que 1-2 minuts per alumne són
  suficients per discriminar autoria real sense allargar excessivament les
  defenses, i que el criteri és aplicable de manera consistent entre sessions.
- **Recepció del canvi «repte ⭐ ara nucli obligatori»**: cal observar si el temps
  de pràctica previst n'és prou per a tothom o si cal retocar el marge de
  contingència d'alguna SA concreta (SA6/SA8 són les més carregades).

## 3. Indicador a vigilar el primer trimestre

**Distribució de semàfors dels mini-checks** (🟢🟡🟠🔴), ja definida com a
indicador a `06b_Avaluacio_programacio_i_practica_docent.md`: si ≥ ⅓ d'un
mini-check surt 🟡/🔴, toca repesca col·lectiva de 10' **i** marcar aquella
pràctica com a candidata a revisió de bastida. Amb els mini-checks ara alimentant
també una nota (el millor del trimestre, 5 %), aquesta distribució és doblement
rellevant al 1r trimestre: confirma si el canvi de P1.3 està consolidant fluïdesa
d'escriptura real (l'objectiu de tot el pla) o si només trasllada l'ansietat de
l'avaluació al mini-check. Es revisa a la primera reunió de departament després
de tancar el 1r trimestre, creuant-la amb el % de repte ⭐ validat a temps a
SA2-SA3.

---

*Document de tancament del pla de millores pedagògiques (Tasks 1-6). Llicència
CC BY-SA 4.0, com la resta del material del curs.*
