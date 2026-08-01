# SA6 · El meu checklist — Control: el robot decideix

**Nom:** ______________________  **Data:** __________

> 🧑‍🎓 **Quan toca?** Tingues-lo obert **durant tota la SA** (marca a mesura que avances) i repassa'l **sencer abans d'entregar** — és l'últim pas de l'itinerari, abans de la prova pràctica T2.

> Marca cada cosa quan la tinguis feta. Serveix per no oblidar-te res i per saber com vas.

## ✅ Abans d'acabar aquesta SA he de…
- [ ] Distingir **llaç obert** de **llaç tancat** amb un exemple propi del vehicle
- [ ] Dissenyar el meu **diagrama d'estats** (RUN/STOP/ALERTA) i provar `maquina_estats_semafor.py` (Act. 1)
- [ ] Entendre i provar la **histèresi** amb `termostat_histeresi.py` (dos llindars, sense oscil·lació) (Act. 1)
- [ ] Fer el **mini-check** individual (Sessió 2, no qualifica)
- [ ] Programar l'estat **STOP prioritari** (polsador + comanda de ràdio `"X"`) sobre `vehicle_seguretat.py` (Act. 2)
- [ ] Provar `registre_dades.py` i llegir `MY_DATA.HTM` per USB (Act. 2)
- [ ] Tancar el repte **«vehicle amb aturada d'emergència»** amb el meu protocol complet (Act. 3) → *compta amb R1 i R3*
- [ ] Fer la **mini-defensa breu** (una decisió justificada) → *compta amb R4*
- [ ] Tenir l'entrada del **quadern tècnic** de la SA6 (què he après · el repte · un error · el meu diagrama d'estats)
- [ ] Recordar que aquest repte **tanca el Projecte T2**: la Sessió 4 és la prova pràctica T2, individual

## 🚦 Com vaig? (pinta el teu nivell)
| Ja sé… | 🔴 Encara no | 🟡 A mitges | 🟢 Sí |
|---|---|---|---|
| Distingir llaç obert de llaç tancat | | | |
| Programar una màquina d'estats amb condicionals | | | |
| Fer que l'STOP interrompi qualsevol moviment, sigui quin sigui l'origen | | | |
| Integrar un sensor amb histèresi (sense oscil·lació) | | | |

## 🆘 Si m'encallo
Segueixo **DEPURA**: **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara · **A**punta. Nou aquesta SA: si l'STOP "de vegades" no funciona, **comprovo on** dins del bucle es fa la comprovació del polsador (ha de ser el **primer** `if`, abans de mirar cap altra entrada). Si segueixo encallat, demano ajuda explicant **què ja he provat**.

> Tens dos o més 🔴? Repassa el material de la SA i demana ajuda: **no passa res**, per això hi ha temps abans de la prova pràctica T2.
