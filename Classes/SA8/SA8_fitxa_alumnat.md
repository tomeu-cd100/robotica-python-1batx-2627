# SA8 · Fitxa base — Autonomia i telemetria

<!-- web:only-github -->

**Nom:** ______________________  **Data:** __________

<!-- /web:only-github -->

> *"Com sap algú, des d'una altra taula, què està 'sentint' el rover en aquest moment?"* El teu rover (T3) ja decideix sol des de la SA7: avui li ensenyes a **explicar-se**, enviant per ràdio el que "sent" (sensors avançats del Kit 3) a un altre programa, escrit també per tu. Tot el treball d'aquesta fitxa és **individual**.

## 🎯 Objectius i avaluació

**En acabar aquesta SA podré:**
1. Llegir sensors avançats del Kit 3 (**IMU MPU6050**, DHT11) i interpretar-ne les magnituds.
2. Enviar dades de sensors per **ràdio** des del rover al meu propi programa d'estació base.
3. Registrar i visualitzar dades rebudes (llista de lectures, mitjana simple).
4. Introduir-me a la **IA aplicada al control**: classificació senzilla de patrons de dades.

| Què lliuro | Rúbrica | On compta |
|---|---|---|
| Sistema de telemetria del rover (producte, S3) | **R1**, **R3** | Projectes (45 %) |
| Repte **⭐** de [Reptes_SA8.md](../../Reptes/Reptes_SA8.md) (nucli obligatori, S3) | **R1** | Projectes (45 %) |
| Mini-defensa breu (S3, R4·DO) | **R4** | Projectes (45 %) |
| Quadern tècnic | **R4** | Quadern tècnic i pràctiques (25 %) |
| Treball a l'aula (autonomia, responsabilitat amb les dades) | **R5** | Actitud (10 %) |
| Mini-check (S2) | — | **No qualifica** (radar formatiu) |

> 🪜 **Versió nucli (ja és assoliment satisfactori):** el rover llegeix **dos** sensors del Kit 3 (IMU MPU6050 + DHT11), els envia per ràdio amb un protocol propi, i el meu `estacio_base.py` els rep i els mostra. **Versió completa:** registre amb `log`, mitjana de lectures, reflexió d'IA i ètica de dades ben argumentada, mini-defensa que explica una decisió pròpia.

> Escala de nota 0-10, rúbriques i tot el sistema: **[Com s'avalua la matèria](../00_General/00_Avaluacio_per_alumnat.md)**.

---

## El que has de fer

### 1 · Sensors avançats i comportaments amb prioritats (Sessió 1)

Coneix els sensors avançats del **Kit 3**: **IMU MPU6050** (orientació, per I2C a P19/P20) i **DHT11** (temperatura/humitat, a P8). Prova [`comportaments.py`](codi/comportaments/comportaments.py): una arquitectura de prioritats amb tres estats (`SEGUIR`/`ESQUIVAR`/`RECUPERAR`) que generalitza el que ja fèieu a la SA7.

**Prediu abans d'executar:** si el rover està seguint la línia i l'HC-SR04 detecta un obstacle molt a prop, quin dels tres estats es dispara? ______________________

**Dissenya el teu format de missatge de telemetria** (quins camps hi vols, amb quin prefix, per exemple `"TEL:D:23;T:24"`): ______________________

### 2 · Telemetria per ràdio (Sessió 2)

Programa [`telemetria_radio.py`](codi/telemetria_radio/telemetria_radio.py): reutilitza la FSM de `comportaments.py` i hi afegeix l'enviament per ràdio de l'estat i dels sensors, amb el prefix **`"TEL:"`** (diferent del `"CMD:"` de la SA5/SA6, perquè no és una ordre). Escriu el teu propi [`estacio_base.py`](codi/estacio_base/estacio_base.py): rep els missatges, els mostra i en guarda un registre (llista + mitjana simple).

> 🎯 **Mini-check individual (10', a l'inici d'aquesta sessió; no qualifica).** Enviar un valor de sensor per ràdio, sense apunts. Banc: [`00_Mini_checks_individuals.md`](../00_General/00_Mini_checks_individuals.md).

### 3 · IA aplicada al control i producte (Sessió 3)

Practica una **classificació de patrons** amb dades de sensors (p. ex. Teachable Machine, a nivell de demostració/pràctica guiada). **Tanca el producte: sistema de telemetria del rover** (com a mínim dos sensors del Kit 3, ràdio, registre amb el teu propi `estacio_base.py`).

**Mini-defensa (breu, davant el docent):** explica **una decisió** de disseny (per exemple, per què has triat aquest format de missatge, o com decideixes si el rover està "inclinat" a `mpu_orientacio()`).

**Reflexió d'IA i ètica de dades:** si volguessis que un model d'IA "aprengués" a decidir en lloc del teu llindar fet a mà, quines dades li caldrien i per què cal tenir cura amb la privadesa d'aquestes dades? ______________________

### 4 · Repte ⭐ (nucli obligatori, mateixa Sessió 3)

Amb el temps de pràctica de la Sessió 3 (el que abans es dedicava opcionalment als reptes), fes el **repte ⭐ · Estació meteorològica escolar amb alertes** de [Reptes_SA8.md](../../Reptes/Reptes_SA8.md): ara és **NUCLI OBLIGATORI**, no una ampliació — no s'hi afegeixen hores noves. **Ensenya'l al docent perquè el validi.**

## Producte · Sistema de telemetria del rover

Es tanca i s'avalua a la **Sessió 3** amb les rúbriques **R1** (codi, funcionament) i **R3** (criteri "Integració"). La mini-defensa hi suma **R4**.

## Si t'encalles (DEPURA)
> **D**escriu (què esperaves vs què passa) · **E**xamina (LED, display, lectura del sensor, missatge rebut) · **P**rova una hipòtesi cada cop · **U**bica el problema · **R**epara i torna a provar · **A**punta-ho al quadern. Nou aquesta SA: si un missatge de ràdio "no arriba com toca", comprova **primer** si el problema és de **protocol** (mateix `group`? mateix `PREFIX`?), abans de sospitar dels sensors.

<!-- web:only-github -->

## M'autoavaluo (Insuficient · Suficient/Bé · Notable · Excel·lent — la nota és 0-10)
| Criteri | Insuficient | Suficient/Bé | Notable | Excel·lent |
|---|---|---|---|---|
| Llegeixo l'IMU MPU6050 i el DHT11 i n'interpreto les magnituds | ☐ | ☐ | ☐ | ☐ |
| Envio dades de sensors per ràdio amb un protocol propi | ☐ | ☐ | ☐ | ☐ |
| Registro i visualitzo dades rebudes (llista, mitjana) | ☐ | ☐ | ☐ | ☐ |
| Explico la diferència entre una regla feta a mà i un model d'IA entrenat amb dades | ☐ | ☐ | ☐ | ☐ |

## Quadern tècnic

> 📓 Escriu-ho a la teva entrada del **[quadern tècnic](../00_General/00_Quadern_tecnic.md)** (guia + plantilla; compta el 25 %).
- **Què he après:** ___________________________________________________
- **El repte i com l'he resolt** (què havia de fer, què vaig predir, com): ___________________________________________________
- **Un error i com l'he resolt:** _____________________________________
- **El meu format de missatge de telemetria** i per què l'he triat així.
- **Reflexió d'IA i ètica de dades:** una decisió que hauria de prendre abans de recollir dades (privadesa, consentiment, finalitat).

<!-- /web:only-github -->

> 📌 **Vols més?** Ampliació, [reptes ⭐⭐/⭐⭐⭐](../../Reptes/Reptes_SA8.md), pensament computacional, exit ticket i ODS → **[SA8_fitxa_ampliada.md](SA8_fitxa_ampliada.md)**
