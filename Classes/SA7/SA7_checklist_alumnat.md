# SA7 · El meu checklist — Robòtica mòbil: el rover

**Nom:** ______________________  **Data:** __________

> 🧑‍🎓 **Quan toca?** Tingues-lo obert **durant tota la SA** (marca a mesura que avances) i repassa'l **sencer abans d'entregar** — és l'últim pas de l'itinerari.

> Marca cada cosa quan la tinguis feta. Serveix per no oblidar-te res i per saber com vas.

## ✅ Abans d'acabar aquesta SA he de…
- [ ] Tenir el rover **muntat** (Sessió 0) amb la checklist de muntatge feta (R2, formativa)
- [ ] Calibrar el meu rover perquè vagi **recte** (`FACTOR_M1`/`FACTOR_M2`) i provar una trajectòria en quadrat amb `calibratge_motors.py` (Act. 1)
- [ ] Fer el **mini-check** individual (Sessió 2, no qualifica)
- [ ] Calibrar el **llindar del seguidor de línia** i provar `segueix_linia.py` sobre el meu circuit (Act. 2)
- [ ] Programar l'**evita-obstacles** amb `evita_obstacles.py` i triar el meu comportament autònom (Act. 3)
- [ ] Integrar el comportament triat amb `rover_missions.py` i alguna millora (Act. 4) → *compta amb R1 i R3*
- [ ] Fer la **mini-defensa breu** (una decisió justificada) → *compta amb R4*
- [ ] Tenir l'entrada del **quadern tècnic** de la SA7 (què he après · el repte · un error · els meus llindars i factors)
- [ ] Recordar que el rover reutilitza les funcions de moviment de la SA4 (`avancar/retrocedir/girar/aturar`); a la SA7 `girar()` guanya un segon paràmetre opcional de velocitat per als girs suaus del seguidor de línia

## 🚦 Com vaig? (pinta el teu nivell)
| Ja sé… | 🔴 Encara no | 🟡 A mitges | 🟢 Sí |
|---|---|---|---|
| Relacionar el gir del rover amb la velocitat/sentit de cada motor | | | |
| Programar un seguidor de línia amb llindar calibrat | | | |
| Programar un evita-obstacles amb l'HC-SR04 | | | |
| Modelitzar una trajectòria combinant girs i avanços | | | |

## 🆘 Si m'encallo
Segueixo **DEPURA**: **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara · **A**punta. Nou aquesta SA: si un sensor "no reacciona com toca", **comprovo primer** el valor que llegeix al REPL, abans de sospitar de l'algorisme o dels motors. Si segueixo encallat, demano ajuda explicant **què ja he provat**.

> Tens dos o més 🔴? Repassa el material de la SA i demana ajuda: **no passa res**, per això hi ha temps abans de la SA8.
