# 00 · Entorns de treball (editor, simulador, Thonny i transferència)

> **Per a qui és?** Docent i alumnat. Explica **on s'escriu i com s'executa** el codi MicroPython del curs: l'editor oficial, el simulador (pla B sense maquinari), Thonny (alternativa d'escriptori) i com passar el programa de l'ordinador a la placa. Llegeix-lo **a la SA1**, abans del primer programa, i torna-hi cada vegada que canviïs d'ordinador o de placa.

## 1. L'eina principal: python.microbit.org

Tot el curs fa servir l'**editor oficial de MicroPython per a micro:bit**: <https://python.microbit.org>.

- **No cal instal·lar res ni crear cap compte**: funciona al navegador, també als ordinadors de l'aula amb perfils restringits.
- Editor de text amb **resaltat de sintaxi**, autocompletar bàsic i botó **«Baixa»** (genera el fitxer `.hex` que s'arrossega a la placa).
- Inclou un **simulador** integrat (matriu de LED, botons A/B, i des de fa temps també alguns sensors) i un **REPL** (consola interactiva) per provar ordres línia a línia i llegir `print()`/`Serial`-style de depuració.
- Els programes es desen com a **projectes** al navegador (`localStorage`) o es baixen com a fitxer `.py`: **recomanació del curs**: baixa sempre una còpia `.py` al final de cada sessió (carpeta personal / Drive), perquè `localStorage` es pot esborrar en netejar el navegador de l'aula.

> ⚠️ **Un ordinador d'aula compartit pot esborrar el teu projecte.** No confiïs mai només en «desar al navegador»: baixa el `.py` o el `.hex` al teu espai personal a cada tancament de sessió.

## 2. El simulador com a pla B

El simulador de python.microbit.org (i, per a comportaments concrets, Wokwi si cal) permet **provar la lògica del programa sense maquinari**:

- Quan un component falla o no hi ha prou plaques per a tothom en un moment donat (vegeu [`00_Mode_supervivencia.md`](00_Mode_supervivencia.md)).
- Per fer els **deures** de cada SA («Deures / simulador» a la seqüència de sessions de cada guia docent).
- Per **predir abans d'executar** (rutina PRIMM, `Programació didàctica/04_Metodologia.md` §4.2): el docent hi projecta codi nou sense executar-lo.

**Limitacions a tenir presents:** el simulador no reprodueix fidelment el **soroll de mesura real** dels sensors analògics (llum, temperatura, so) ni el comportament físic dels motors; els llindars que funcionen bé al simulador **s'han de recalibrar** amb la placa física. Fes-ho constar al quadern tècnic com a «mesura simulada» (vegeu la nota de `Programació didàctica/07_Rubriques.md`, R2 · Mesura/diagnòstic).

## 3. Thonny (alternativa d'escriptori)

**Thonny** (<https://thonny.org>) és un IDE de Python gratuït amb suport nadiu per a micro:bit (menú *Executa → Configura l'intèrpret → MicroPython (BBC micro:bit)*). Útil quan:

- Es vol treballar **sense connexió** a internet (a diferència de l'editor web).
- Es necessita el **REPL persistent** per depurar pas a pas amb més comoditat que al navegador.
- L'alumnat vol continuar practicant a casa amb el seu propi ordinador i una placa pròpia.

No és obligatori: l'editor web n'hi ha prou per a tot el curs. Es presenta com a **alternativa equivalent**, mai com a requisit.

## 4. Transferir el programa a la placa (`.hex` / `.py`)

1. Connecta la micro:bit a l'ordinador amb un cable **micro-USB** (apareix com una unitat extraïble anomenada `MICROBIT`).
2. Des de python.microbit.org: botó **«Baixa»** → es descarrega un fitxer `.hex` (el programa MicroPython empaquetat amb el microprogramari) → arrossega'l a la unitat `MICROBIT`.
3. Des de Thonny: amb l'intèrpret de micro:bit seleccionat, **Fitxer → Desa a → MicroPython** i tria `main.py` (el nom que la placa executa a l'engegar).
4. El **LED groc del darrere parpelleja** mentre es grava; quan s'atura i la placa es reinicia, el programa nou ja s'executa.

> ⚠️ **No desendollis la placa mentre parpelleja el LED groc**: pots corrompre el sistema de fitxers intern. Espera sempre que acabi.

**Diferència `.hex` vs `.py`:** el `.hex` conté el microprogramari MicroPython **i** el teu codi junts (és el que s'arrossega des de l'editor web); el `.py` és **només el teu codi font** (el que s'obre/edita/es desa a Thonny o com a còpia de seguretat personal). Per tornar a editar un `.hex` a l'editor web: **«Obre» → arrossega el `.hex`** — l'editor en recupera el codi font automàticament.

## 5. Micro:shield i alimentació

El **Micro:shield** s'encaixa sobre la micro:bit i dona accés als pins amb connectors tipus *block* (sense necessitat de soldar). Per a servos i motoreductors, connecta l'alimentació externa (portapiles) al Micro:shield **abans** de provar el moviment: el port USB de l'ordinador **no** subministra prou corrent per a motors.

## 6. Registre d'incidències de maquinari

Si una placa, un Micro:shield o un sensor deixa de funcionar, registra-ho a l'espai d'incidències de l'aula (full del docent) i passa temporalment al **pla B del simulador** (`00_Mode_supervivencia.md`) mentre es reposa o es repara. Una avaria de maquinari individual **no penalitza**: el que es qualifica és el codi i la comprensió, no la placa concreta.

---

⬅️ Torna a [`00_LLEGEIX-ME_Classes.md`](00_LLEGEIX-ME_Classes.md).
