# SA0 · Primers passos amb l'editor

> **Per a què serveix aquest document?** És el teu **full de ruta del primer dia**: com obrir l'editor, escriure el primer programa, provar-lo i passar-lo a la placa. Per al detall complet (simulador, Thonny, incidències de maquinari...) tens **[`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md)**: llegeix-lo abans del primer programa de la SA1.

## 1. Obre l'editor: no cal crear cap compte

Tot el curs fa servir l'editor oficial de MicroPython per a micro:bit, a **<https://python.microbit.org>**.

- Funciona directament al navegador: **no cal instal·lar res ni registrar-se**.
- Va bé fins i tot als ordinadors de l'aula amb perfils restringits.
- Té un **simulador** integrat (per provar el programa sense placa) i un editor de text amb resaltat de sintaxi.

## 2. Escriu el teu primer programa

Un programa MicroPython, encara que sigui de dues línies, ja fa les tres coses d'un robot: **percep** (o no, si no té entrades), **decideix** i **actua**. Per començar, prova un que només actua:

```python
from microbit import *

display.scroll("HOLA")
```

Prem el botó de **provar/executar** dins l'editor per veure'l al simulador abans de tocar cap placa.

## 3. Desa una còpia: `.hex` i `.py`

L'editor desa automàticament dins del navegador, però **no t'hi refiïs mai**: un ordinador compartit d'aula pot esborrar-ho tot en netejar-se.

- **Baixa sempre una còpia** al final de cada sessió, a l'espai personal (carpeta pròpia o Drive).
- Dues opcions de fitxer, amb un propòsit diferent cadascuna:
  - **`.hex`**: el programa **empaquetat amb el microprogramari** de la placa. És el que s'arrossega a la micro:bit per transferir-hi el codi.
  - **`.py`**: **només el teu codi font**, sense empaquetar. És el que obriràs a Thonny o guardaràs com a còpia de seguretat llegible.

> Detall complet de com tornar a obrir un `.hex` per continuar-lo editant, i de les alternatives (simulador, Thonny): **[`00_Entorns_de_treball.md`](../00_General/00_Entorns_de_treball.md)**.

## 4. Connecta la placa i transfereix el programa

1. Connecta la micro:bit a l'ordinador amb un cable **micro-USB**: apareixerà com una unitat extraïble anomenada `MICROBIT`.
2. A l'editor, prem **«Baixa»**: es descarrega el fitxer `.hex`.
3. **Arrossega** aquest `.hex` a la unitat `MICROBIT`.
4. El **LED groc del darrere** de la placa parpelleja mentre es grava. Quan s'atura i la placa es reinicia, el programa nou ja s'executa.

> ⚠️ **No desendollis la placa mentre parpelleja el LED groc**: pots corrompre el sistema de fitxers intern. Espera sempre que acabi.

## Resum d'una ullada

| Pas | Acció |
|---|---|
| 1 | Obre <https://python.microbit.org> (sense compte). |
| 2 | Escriu i prova el programa al simulador. |
| 3 | Baixa'n una còpia (`.hex` per a la placa, `.py` com a còpia de seguretat). |
| 4 | Connecta la placa per USB i arrossega-hi el `.hex`. |

A partir d'aquí ja estàs a punt per començar la **SA1**.
