# SA8 · El meu checklist — Autonomia i telemetria

**Nom:** ______________________  **Data:** __________

> 🧑‍🎓 **Quan toca?** Tingues-lo obert **durant tota la SA** (marca a mesura que avances) i repassa'l **sencer abans d'entregar** — és l'últim pas de l'itinerari.

> Marca cada cosa quan la tinguis feta. Serveix per no oblidar-te res i per saber com vas.

## ✅ Abans d'acabar aquesta SA he de…
- [ ] Provar `comportaments.py` sobre el meu rover i entendre els tres estats (`SEGUIR`/`ESQUIVAR`/`RECUPERAR`) (Act. 1)
- [ ] Muntar el **DHT11** (P8) i l'**IMU MPU6050** (I2C, P19/P20) sobre el meu rover
- [ ] Dissenyar el meu **format de missatge** de telemetria (prefix `"TEL:"` + camps)
- [ ] Fer el **mini-check** individual (Sessió 2, no qualifica)
- [ ] Programar `telemetria_radio.py` i el meu propi `estacio_base.py` (Act. 2)
- [ ] Fer la **pràctica guiada d'IA** (classificació de patrons) i escriure la reflexió d'IA i ètica de dades
- [ ] Tancar el **sistema de telemetria del rover** (Act. 3, producte) → *compta amb R1 i R3*
- [ ] Fer el **repte ⭐** de `Reptes/Reptes_SA8.md` (nucli obligatori) i ensenyar-lo al docent → *compta amb R1*
- [ ] Fer la **mini-defensa breu** (una decisió justificada; per mostreig — si no et toca, escriu-ho al quadern) → *compta amb R4*
- [ ] Tenir l'entrada del **quadern tècnic** de la SA8 (què he après · el repte · un error · el meu format de missatge · reflexió d'IA)
- [ ] Recordar que el rover reutilitza els motors/sensors de la SA7 (`avancar/retrocedir/girar/aturar`, HC-SR04, seguidor de línia); a la SA8 s'hi afegeixen només el DHT11, l'IMU i la ràdio de telemetria

## 🚦 Com vaig? (pinta el teu nivell)
| Ja sé… | 🔴 Encara no | 🟡 A mitges | 🟢 Sí |
|---|---|---|---|
| Llegir l'IMU MPU6050 i el DHT11 i interpretar-ne les magnituds | | | |
| Enviar dades de sensors per ràdio amb un protocol propi | | | |
| Registrar i visualitzar dades rebudes (llista, mitjana) | | | |
| Explicar la diferència entre una regla feta a mà i un model d'IA entrenat amb dades | | | |

## 🆘 Si m'encallo
Segueixo **DEPURA**: **D**escriu · **E**xamina · **P**rova una hipòtesi cada cop · **U**bica · **R**epara · **A**punta. Nou aquesta SA: si un missatge de ràdio "no arriba com toca", **comprovo primer** el protocol (mateix `group`? mateix `PREFIX`?), abans de sospitar dels sensors. Si segueixo encallat, demano ajuda explicant **què ja he provat**.

> Tens dos o més 🔴? Repassa el material de la SA i demana ajuda: **no passa res**, per això hi ha temps abans de la SA9.
