# SA7 · Exemple resolt (model «jo ho faig») — Un buscador de llum amb aturada per obstacle

> 🧑‍🎓 **Quan toca mirar-lo?** Després del teu **primer intent** amb `calibratge_motors.py`/`segueix_linia.py` (S1-S2) — mai abans. És un problema **anàleg** per veure *com es pensa*, no una solució per copiar: el repte «tria un comportament autònom» l'has de fer amb el **teu** rover.

> 🔗 **D'on ve i on va.** Aquest exemple és el **bessó comentat** de les pràctiques [`segueix_linia`](codi/segueix_linia/EXPLICACIO.md) i [`evita_obstacles`](codi/evita_obstacles/EXPLICACIO.md): la mateixa idea (llegir un sensor, comparar-lo amb un llindar, corregir) amb un context expressament diferent — un **buscador de llum** amb només la placa micro:bit, sense rover — perquè vegis **com es pensa**, no per copiar-lo. Quan l'hagis entès, torna al teu rover i fes el **teu** repte.

> **Nota docent:** mostra'l **després del primer intent** amb el seguidor de línia. No és la solució del repte «tria un comportament autònom» (que cada alumne/a fa amb el **seu** rover): és un problema **anàleg** resolt pas a pas perquè l'alumnat vegi *com es pensa* un comportament reactiu basat en llindar, no què s'ha de copiar. Comenta en veu alta el pas «🧭 Com ho penso» (per què un llindar no és universal) i el «⚠️ Contraexemple».

---

## 🔑 El repte model

> Vull que un LED (que simula un actuador de gir) s'encengui quan la micro:bit està en una zona **fosca** i quedi apagat quan hi ha prou **llum**: és l'anàleg d'un rover que "corregeix" cap a un costat quan el sensor de línia deixa de veure la línia. A més, si es prem el botó A (simulant l'HC-SR04 detectant un obstacle), el sistema s'atura del tot, sigui quina sigui la lectura de llum.

Fa servir només conceptes de la SA7: **llegir un sensor analògic**, **llindar de detecció** (calibrat, no fix) i **prioritat d'una condició sobre una altra** (l'obstacle sempre guanya). Maquinari: micro:bit V2, un LED extern com a simulació de l'actuador de correcció (pin1) i el sensor de llum **intern** de la placa (`display.read_light_level()`), sense necessitat del rover ni del KS0050.

---

## 🧭 Com ho penso (abans d'escriure res)

1. **Analitzo:** el sensor de llum intern dona un valor **0-255**. Si poso un llindar fix (per exemple, 100) sense comprovar-lo a la meva aula concreta, potser mai s'activa (si l'aula és molt lluminosa) o sempre està activat (si l'aula és fosca). Cal **calibrar-lo**, exactament com el `LLINDAR_LINIA` del seguidor de línia real.
2. **Decideixo l'estructura:** una funció que llegeix el sensor i decideix; una altra condició, comprovada **abans**, que si es compleix (botó A premut) guanya sempre.
3. **Decideixo l'ordre del bucle:** l'obstacle simulat (botó A) es comprova **primer**, exactament com el polsador STOP de `rover_missions.py` es comprova abans que qualsevol missió.
4. **🔮 PREDIU (fes-ho tu abans de llegir el codi):** si la zona és fosca (LED hauria d'estar encès) però en aquell moment es prem el botó A, què hauria de passar amb el LED? ☐ Es queda encès igualment ☐ S'apaga, perquè l'"obstacle" té prioritat.

---

## 💡 La solució anotada

```python
# SA7 - exemple_buscador_llum.py  (EXEMPLE MODEL, no es el producte)
# Llegeix un sensor analogic (llum interna) i corregeix un LED segons un
# llindar CALIBRAT, amb una condicio d'obstacle (boto A) amb prioritat
# maxima, igual que fa el rover real amb el seguidor de linia i l'HC-SR04.
# Maquinari: LED extern al pin1 (simula l'actuador de correccio), sensor de
# llum intern de la placa (sense cablatge nou).

from microbit import *

LED_CORRECCIO = pin1

# Llindar CALIBRAT sobre l'aula real (0-255): per sota, es considera "fosc"
# i cal corregir. Aixi es com es calibra LLINDAR_LINIA al rover real.
LLINDAR_LLUM = 100


def hi_ha_obstacle():
    # Simulacio de l'HC-SR04: el boto A fa de sensor d'obstacle. Prioritat
    # maxima, es comprova SEMPRE abans que la resta de la logica.
    return button_a.is_pressed()


while True:
    if hi_ha_obstacle():
        # L'obstacle guanya SEMPRE, sigui quina sigui la lectura de llum.
        LED_CORRECCIO.write_digital(0)
        display.show(Image.NO)
    else:
        llum = display.read_light_level()
        if llum < LLINDAR_LLUM:
            LED_CORRECCIO.write_digital(1)   # "corregeix": zona fosca
            display.show(Image.ARROW_W)
        else:
            LED_CORRECCIO.write_digital(0)   # "segueix recte": prou llum
            display.show(Image.ARROW_N)

    sleep(100)
```

**Per què està escrit així (🌟):**
- **`LLINDAR_LLUM` és un valor per calibrar, no un dogma:** el codi comença amb un valor raonable (100), però l'alumnat ha de comprovar-lo amb `print(display.read_light_level())` a la seva aula concreta abans de confiar-hi, exactament com el `LLINDAR_LINIA` real.
- **`hi_ha_obstacle()` es comprova primer, sense excepcions:** és la garantia que la condició de prioritat màxima (l'obstacle) mai queda "amagada" darrere d'una altra decisió.
- **Un únic bloc `if/else` decideix, no dos de separats:** evita que la lectura de llum i la decisió d'obstacle es contradiguin (per exemple, que el LED s'encengui per llum just després d'apagar-se per obstacle, en la mateixa volta del bucle).

---

## 🔬 Provo i mesuro

- **Predicció ✔:** si la zona és fosca i es prem el botó A alhora, el LED **s'apaga** igualment: l'obstacle simulat guanya sempre, exactament com passaria amb `missio_linia()` de `rover_missions.py`, on l'HC-SR04 atura el rover encara que el seguidor de línia digués "segueix avançant".
- **Provo cada extrem per separat:** primer verifico el llindar de llum sol (tapant i destapant el sensor amb la mà, sense tocar el botó A), i després que el botó A atura el LED **des de qualsevol estat** de llum.
- **Calibratge real:** anoto amb `print()` el valor de `display.read_light_level()` en 2-3 punts diferents de l'aula abans de fixar `LLINDAR_LLUM` definitivament.

---

## ⚠️ Contraexemple (errors típics i com es detecten)

- **Fixar el llindar sense calibrar-lo a l'aula real:** el programa no dona cap error, però el LED mai s'encén (o mai s'apaga). **Pista:** llegeix el valor real amb `print()` abans de triar el llindar, com fas amb `LLINDAR_LINIA` sobre el teu circuit.
- **Comprovar l'obstacle DESPRÉS de la lògica de llum:** hi ha un instant en què la correcció de llum "guanya" a l'obstacle. **Pista:** la condició de prioritat màxima ha de ser el **primer** `if` del bucle, sempre.
- **Separar la decisió en dos blocs `if` independents en lloc d'un `if/else`:** pot fer que el LED rebi dues ordres contradictòries a la mateixa volta. **Pista:** una sola estructura de decisió, com fa `evita_obstacles.py` amb `if distancia < LLINDAR... else ...`.
- **Oblidar que un únic sensor no diu "cap a quin costat":** aquest exemple només decideix "corregeix / no corregeix", no cap a quin costat, exactament com el `segueix_linia.py` real necessita una estratègia de cerca fixa amb un sol sensor.

---

## 📔 Diari de bord (entrada model, 1a persona)

> **Sessió 1-2:** He après que un **llindar** no és mai un valor fix "de manual": cal **calibrar-lo** sobre les condicions reals (llum de l'aula, circuit concret). Vaig **predir** que l'obstacle simulat (botó A) hauria de guanyar sempre a la lectura de llum, i en provar-ho vaig veure que, efectivament, si comprovava el botó A **després** de la lògica de llum, hi havia un instant en què el LED "no reaccionava" correctament a l'obstacle. Ho vaig resoldre posant la comprovació de l'obstacle com la **primera** del bucle. **Evidència:** codi comentat + taula amb 3 lectures de llum reals de l'aula i el llindar triat, amb una nota al quadern explicant per què l'ordre de les comprovacions importa.

**Per què és una bona entrada:** usa el **vocabulari clau** (llindar, calibratge, prioritat), explica *el com* (per què l'ordre de les comprovacions és crític) i és **honesta amb el dubte** (el llindar mal calibrat al primer intent) i com es va resoldre.

---

*Exemple resolt de la SA7. Model de treball per a l'alumnat (alliberament gradual: es mostra després del primer intent). Es recolza en `codi/segueix_linia` i `codi/evita_obstacles`. El repte «tria un comportament autònom» real l'has de fer amb el **teu** rover, no amb aquest. Llicència CC BY-SA 4.0.*
