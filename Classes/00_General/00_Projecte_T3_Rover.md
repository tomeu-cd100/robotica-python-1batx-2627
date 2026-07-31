# 🚙 Projecte T3 · El rover autònom

> **Per a qui és?** Per a **cada alumne**, individualment, durant el 3r trimestre. És el dossier del tercer robot del curs: peces d'ampliació, muntatge, cablatge, codi mínim i rúbrica. Es munta abans de començar la SA7 i els reptes de SA7, SA8 i SA9 hi van sumant capacitats.

**Durada:** 3r trimestre (Sessió 0 + SA7-SA9) · **Maquinari:** el **mateix xassís, motoreductors, roda boja, micro:bit V2 + Micro:shield i portapiles del vehicle de T2** + seguidor de línia KS0050 (Kit 2), sensor d'ultrasons HC-SR04 (Kit 2), IMU MPU6050 + DHT11 + BMP280 + CCS811 (Kit 3, SA8)

## El robot

> ⚠️ **El rover NO és un xassís nou: és el vehicle de T2 amb sensors afegits.** No hi ha cap plantilla de tall làser pròpia de T3 ni cap sessió de fabricació de xassís: cada alumne reaprofita **el mateix xassís, els mateixos motoreductors i la mateixa roda boja** que ja va muntar a SA4 per al vehicle teledirigit. El que s'afegeix a T3 és **percepció pròpia**, amb dues peces petites impreses en 3D: un **seguidor de línia** sota el xassís i un **suport per al sensor d'ultrasons** al davant, que li permeten decidir sol, sense comandament.

A **Sessió 0** (prèvia a SA7) cada alumne recupera el seu vehicle de T2 i hi munta les dues peces d'ampliació; a **SA7** hi programa comportaments autònoms (seguidor de línia, evita-obstacles); a **SA8** hi afegeix **telemetria per ràdio** cap al seu propi programa d'estació base; a **SA9** l'amplia amb un **repte lliure** individual per al projecte final.

![Xassís del vehicle de T2 reaprofitat amb les dues peces d'ampliació del rover: suport de l'HC-SR04 al davant i seguidor de línia enganxat sota el xassís mirant a terra; motoreductors, roda boja, micro:bit amb Micro:shield i portapiles es mantenen tal com es van muntar a T2](img/rover-xassis.svg)

Què fa: a **SA7** decideix sol amb **cinemàtica diferencial** (heretada de T2) —seguir una línia pintada a terra o evitar un obstacle amb l'HC-SR04—; a **SA8** envia les seves lectures (IMU, temperatura, pressió, CO₂) **per ràdio** cap a una estació base amb el seu propi programa; a **SA9** és la plataforma del **repte final individual** de cada alumne.

## Llista de peces

| Peça | Origen | Quantitat |
|---|---|---|
| **Reaprofitat íntegrament del vehicle T2** (xassís, 2 motoreductors + rodes KS9008, roda boja + canica 16 mm, micro:bit V2 + Micro:shield, portapiles 4×AA) | Muntatge ja fet a SA4 | — |
| Suport frontal HC-SR04 | `suport_hcsr04.scad`, impressió 3D (**peça nova**, petita) | 1 |
| Suport del seguidor de línia | `suport_seguidor_linia.scad`, impressió 3D (**peça nova**, petita) | 1 |
| Seguidor de línia KS0050 | Kit 2 | 1 |
| Sensor d'ultrasons HC-SR04 | Kit 2 | 1 |
| IMU MPU6050, DHT11, BMP280, CCS811 *(SA8)* | Kit 3 | 1 de cada |
| Cargols M3 addicionals (fixació dels dos suports nous) | Material del centre | ~4-6 |

<!-- web:only-github -->
**Cap plantilla de tall làser nova.** Peces impreses en 3D (noves, petites): [`../../Recursos/peces_3d/suport_hcsr04.scad`](../../Recursos/peces_3d/suport_hcsr04.scad),
[`../../Recursos/peces_3d/suport_seguidor_linia.scad`](../../Recursos/peces_3d/suport_seguidor_linia.scad).
<!-- /web:only-github -->

## Fabricació i personalització

No hi ha personalització nova ni cua de làser: el xassís i el seu gravat/nom **ja es van fer a T2**. La **Sessió 0**, prèvia a la SA7 i finançada per la compressió de la SA8 (6→4 h) — vegeu `Programació didàctica/08_Sequenciacio_temporal_anual.md` §«Fil conductor i consum del marge» — és una sessió **lleugera**: cada alumne recupera el seu vehicle ja muntat i hi cargola les dues peces d'ampliació noves (impreses prèviament pel docent, lot molt més petit que el d'un xassís sencer). Calendari de lots: [`00_Fil_conductor_construccions.md`](00_Fil_conductor_construccions.md) §3.

## Muntatge

1. Recupera el teu **vehicle de T2** (xassís, motors, roda boja, micro:bit + Micro:shield, portapiles): no cal desmuntar-lo, només ampliar-lo.
2. Cargola el **suport de l'HC-SR04** (`suport_hcsr04.scad`) al davant, sensor mirant endavant.
3. Enganxa el **suport del seguidor de línia** (`suport_seguidor_linia.scad`) sota el xassís, centrat, amb el KS0050 mirant a terra.
4. Cablatge addicional segons la taula de baix (només els dos sensors nous; M1/M2 i l'alimentació **no es toquen**); comprova-ho abans d'alimentar els motors.

> ⚠️ **GND comú:** el mateix avís que al vehicle (T2) — piles, Micro:shield i sensors han de compartir massa, o les lectures i els motors fallen de manera intermitent.

## Cablatge (pins del Micro:shield)

| Component | Pin / canal | Notes |
|---|---|---|
| Motoreductor esquerre | M1 | **Ja cablejat a T2; no es toca.** |
| Motoreductor dret | M2 | **Ja cablejat a T2; no es toca.** |
| Sensor d'ultrasons HC-SR04, TRIG | P1 | Digital, sortida. *(nou)* |
| Sensor d'ultrasons HC-SR04, ECHO | P2 | Digital, entrada. *(nou)* |
| Seguidor de línia KS0050 | P0 (analògic; ADC vàlid: P0/P1/P2/P3/P4/P10) | Llindar de detecció a calibrar sobre el circuit real. *(nou)* |
| IMU MPU6050 *(SA8)* | P19/P20 (I2C) | Bus I2C compartit amb altres sensors I2C del kit. *(nou, SA8)* |
| DHT11 *(SA8)* | P13 | Bus digital 1-Wire. *(nou, SA8)* |
| BMP280, CCS811 *(SA8)* | P19/P20 (I2C) | Mateix bus I2C que l'IMU. *(nou, SA8)* |
| Ràdio (SA8, telemetria) | — | Ràdio interna de la micro:bit (`radio`); no necessita cablatge. |

> 🔑 **Continuïtat de pins amb el vehicle (T2):** els canals de motor (M1/M2) **no es tornen a tocar** un cop fixats a SA4 — és l'avantatge de reaprofitar el mateix xassís: el bloc de pins de moviment es fixa una sola vegada per a tot el curs, i a T3 només s'hi afegeixen els pins dels dos sensors nous.

## Comportaments autònoms (SA7)

- **Cinemàtica diferencial:** girar variant la velocitat/sentit relatiu de cada roda (les mateixes funcions `avancar()/girar()/aturar()` de T2, sense cap canvi).
- **Seguidor de línia:** llegeix el KS0050 i corregeix la trajectòria cap al costat on es perd la línia.
- **Evita-obstacles:** llegeix la distància amb `mesura_distancia()` (HC-SR04) i atura/gira si detecta un obstacle proper.
- El repte **"tria un comportament autònom"** (seguidor de línia i/o evita-obstacles) pot fer de producte de la SA si el calendari ho requereix (pla de contingència, tercera retallada — vegeu doc. 08).

## Telemetria (SA8)

- **Regla de ràdio i estació base (treball individual):** cada alumne escriu igualment el **seu propi** programa d'estació base (és el que s'avalua); l'executa temporalment a la placa d'un **company** (per torns, grups per números de llista) o del **docent**. La placa és només el banc de proves; el codi i la interpretació de les dades són sempre evidència pròpia. Detall complet: `Programació didàctica/17_SA8_Autonomia_i_telemetria.md`.
- **Mínim dos sensors** del Kit 3 (IMU, DHT11, BMP280 o CCS811) enviats per ràdio i registrats/mostrats amb el programa d'estació base propi (llista de lectures + mitjana simple).

## 🧗 Si t'encalles: l'esquelet del programa (evita-obstacles + telemetria bàsica)

<details markdown="1">
<summary>Desplega l'esquelet (còpia'l a un fitxer nou)</summary>

```python
# Projecte T3 - El rover autonom (ESQUELET per comencar)
#
# Comportament base: evita obstacles (SA7) + telemetria per radio (SA8).
# Omple els # TODO.

from microbit import *
import radio

GRUP_RADIO = 10
LLINDAR_OBSTACLE = 15  # cm

radio.on()
radio.config(group=GRUP_RADIO)


def mesura_distancia():
    pass  # TODO: pols TRIG/ECHO de l'HC-SR04 -> distancia en cm


def avancar(velocitat):
    pass  # TODO: PWM als canals M1/M2 (reaprofita el del vehicle T2, sense canvis)


def girar(costat):
    pass  # TODO


def aturar():
    pass  # TODO


def envia_lectura(etiqueta, valor):
    radio.send(etiqueta + ':' + str(valor))  # EXEMPLE RESOLT: format "T:23.5"


while True:
    # EXEMPLE RESOLT: cicle reactiu - llegir a CADA volta, no un sol cop
    dist = mesura_distancia()
    if dist < LLINDAR_OBSTACLE:
        aturar()
        girar('esquerra')
    else:
        avancar(400)

    # TODO (SA8): llegeix un sensor del Kit 3 (temperature(), accelerometer...)
    #      i envia'l amb envia_lectura() cada 2 segons (usa running_time()).

    sleep(20)
```

</details>

## Què hi aporta cada fase

| Fase | Sessions | Què s'hi construeix | Repte relacionat |
|---|---|---|---|
| Sessió 0 | 1 sessió, prèvia a SA7 | Ampliació del vehicle de T2 amb les dues peces d'ampliació (HC-SR04, seguidor de línia); **cap fabricació de xassís**. | Checklist de muntatge (R2, formativa) |
| SA7 | S1-S4 | Cinemàtica diferencial (heretada), seguidor de línia i/o evita-obstacles: el rover **és** la plataforma de la SA. | `Reptes_SA7.md` |
| SA8 | S1-S3 | Telemetria per ràdio (IMU, DHT11, BMP280, CCS811) cap al propi programa d'estació base; introducció a la IA aplicada al control. | `Reptes_SA8.md` |
| SA9 | S1-S5 (S5 = Prova T3) | Repte lliure individual + dossier tècnic + defensa oral, amb el mateix rover ampliat. | [`README de la SA9`](../SA9/README.md) |

**Producte final (SA9-S4):** el rover ampliat amb el repte lliure de cada alumne, funcional, més el **dossier tècnic** i la **defensa oral individual**. Es tanca a la S4; la S5 és la prova pràctica **T3**, individual i per estacions rotatives.

## Rúbrica del robot (avaluada dins el producte de SA9, dimensió «Projectes i productes»)

| Criteri | Insuficient (0-4) | Suficient/Bé (5-6) | Notable (7-8) | Excel·lent (9-10) |
|---|---|---|---|---|
| **R2 · Muntatge i robustesa** | El rover no aguanta el repte final (es desmunta o deixa de respondre). | Aguanta amb algun retoc d'última hora. | Aguanta sense retocs, cablatge endreçat. | Aguanta sense retocs, cablatge endreçat i etiquetat, res solt. |
| **R3 · Comportaments autònoms** | No segueix línia ni evita obstacles de manera fiable. | Segueix línia **o** evita obstacles, amb errors freqüents. | Segueix línia **i** evita obstacles, amb algun error puntual. | Comportaments fiables i fluids, més el repte lliure de SA9 integrat. |
| **R1 · Telemetria** | No arriben dades per ràdio a l'estació base. | Arriben dades bàsiques, de manera intermitent. | Arriben dades de manera fiable i es registren. | Telemetria fiable, ben etiquetada i útil per seguir l'estat del rover en directe. |
| **R4 · Documentació tècnica i defensa** | Sense esquema ni codi comentat. | Esquema o codi comentat, no els dos. | Dossier complet (esquema, codi comentat, proves) i defensa clara. | Dossier exhaustiu amb diari de calibratge i defensa que respon preguntes amb criteri. |

## Problemes freqüents

| Símptoma | Causa probable | Solució |
|---|---|---|
| Un motor gira al revés | Sentit del canal M1/M2 invertit (arrossegat del muntatge del vehicle). | Inverteix el signe de la velocitat del motor afectat al codi; **no** recablis M1/M2. |
| El rover no avança recte | PWM desigual entre M1 i M2 (ja hi era al vehicle de T2). | Calibra els valors de cada motor per compensar la diferència. |
| Lectures d'ultrasons erràtiques | GND no comú, o cable massa llarg fins al TRIG/ECHO. | Uneix totes les masses i escurça el cablatge del sensor. |
| No arriba telemetria a l'estació base | Grup de ràdio diferent entre rover i estació base, o `radio.on()` no cridat als dos costats. | Comprova el `group=` i que la ràdio estigui activada a les dues plaques. |
| El seguidor de línia no detecta la línia | Llindar mal calibrat per a la il·luminació real de l'aula. | Recalibra el llindar amb el REPL sobre el circuit de proves real. |

> **Pla B:** si el vehicle d'un alumne no arriba a la Sessió 0 en condicions (avaria acumulada des de T2), es reparen només els components afectats (motor, roda, connexió): **mai cal refer el xassís**, ja que no se'n fabrica cap de nou. Si algun dels dos suports nous no arriba imprès a temps, es pot fixar temporalment el sensor amb cinta/brides i substituir-lo per la peça definitiva més endavant, sense aturar la programació (vegeu `00_Fil_conductor_construccions.md` §4).

---

⬅️ Torna a: [SA7 (itinerari per sessions)](../SA7/README.md) · [Reptes de la SA7](../../Reptes/Reptes_SA7.md) · [Reptes de la SA8](../../Reptes/Reptes_SA8.md) · [El fil conductor de les tres construccions](00_Fil_conductor_construccions.md)
