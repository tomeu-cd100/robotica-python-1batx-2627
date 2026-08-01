# Reptes SA7 · Robòtica mòbil: el rover

> 🧑‍🎓 **Quan toca fer-ne un?** El repte **⭐ és NUCLI OBLIGATORI — forma part del producte de la SA**: comença'l quan tinguis el **nucli al dia** (el comportament autònom de la S4, tancat). Els reptes **⭐⭐/⭐⭐⭐ resten opcionals** (ampliació), per a qui vagi sobrat de temps. Ensenya el ⭐ al docent perquè el validi.

**Fes els reptes en ordre de dificultat: comença per ⭐, i si arribes a ⭐⭐⭐ hauràs passat pels tres.** Tots parteixen dels programes de `Classes/SA7/codi/` i fan servir el concepte de cinemàtica diferencial, llindar calibrat i/o mesura de distància per temps de vol. Es fan **sempre amb maquinari real** (el rover): el simulador de python.microbit.org **NO** simula cap component del rover (motors, HC-SR04, seguidor de línia), vegeu [`SA7_esquemes_connexions.md`](../Classes/SA7/SA7_esquemes_connexions.md) §Simulació.

> **Continguts SA7:** cinemàtica diferencial, calibratge de motors, seguidor de línia (llindar), evita-obstacles (time-of-flight), integració en missions. · **Vocabulari/bases:** `Classes/SA0/`.

> **Format "producte real":** cada repte simula un **encàrrec** amb **client**, **lliurable** i **ús al món real**. El requisit tècnic no canvia; el marc ajuda a donar sentit al producte.

> 🎛️ **Recorda:** el codi i el producte de cada repte són **teus**, com a tota la SA7.

---

## ⭐ Repte 1 · Carret de magatzem amb velocitat variable (NUCLI OBLIGATORI)

**Context.** Un petit magatzem escolar (el material de robòtica del centre) vol un carret que segueixi un carril pintat entre les prestatgeries, més ràpid als trams rectes i més lent a les corbes, perquè no caigui res del carret.

> *Client: coordinació de material del centre · Lliurable: seguidor de línia amb velocitat variable segons la qualitat de la lectura · Món real: carrets AGV de magatzem que segueixen carrils pintats o cintes magnètiques.*

**Què treballa.** Llindar calibrat, correcció de rumb, `segueix_linia.py`.

**Requisit mínim.**
- Parteix de `segueix_linia.py`: manté la lectura amb `read_analog()` i el llindar calibrat (ja fet).
- Afegeix una **segona velocitat**, més baixa, que s'utilitzi durant els girs de correcció (quan es perd la línia), i la velocitat normal quan la segueix recte.
- Codi comentat.

<details markdown="1">
<summary>🧗 Si t'encalles (repte ⭐): pistes esglaonades</summary>

**Nivell 1 — Pista conceptual.** `girar()` ja accepta un segon paràmetre `velocitat` (amb un valor per defecte). No necessites cap funció nova: només una **constant nova**, més baixa que `VELOCITAT_AVANCAR`, i passar-la com a argument a `girar()` a la branca on ara es perd la línia.

**Nivell 2 — Pseudocodi.**
```
defineix VELOCITAT_CORRECCIO (mes baixa que VELOCITAT_AVANCAR)
dins del while True:
  si la lectura indica linia:
    avanca a VELOCITAT_AVANCAR
  sino:
    gira cap a un costat a VELOCITAT_CORRECCIO
```

**Nivell 3 — Esquelet amb TODO.** El llindar i el bucle base ja hi són; omple només la velocitat de correcció.
```python
# SA7 - Repte 1 (BASTIDA / esquelet per a l'alumnat)
#
# QUE JA ESTA FET (no ho toquis):
#   - VELOCITAT_AVANCAR i LLINDAR_LINIA ja hi son.
#
# QUE HAS DE FER TU:
#   - Defineix una velocitat de correccio MES BAIXA i fes-la servir
#     nomes quan es perd la linia.
#
# EINES QUE POTS USAR (nomes conceptes de la SA7):
#   - girar(costat, velocitat)   -> ja feta, admet un segon parametre

VELOCITAT_CORRECCIO = ___   # TODO 1: mes baixa que VELOCITAT_AVANCAR

# ... dins del while True:
if lectura < LLINDAR_LINIA:
    avancar(VELOCITAT_AVANCAR)
else:
    girar('esquerra', ___)   # TODO 2: fes servir VELOCITAT_CORRECCIO
```

</details>

**Ampliacions graduades.**
1. *(bàsica)* Mostra al display, amb `display.show()`, una icona diferent quan el rover va a velocitat normal i quan va a velocitat de correcció.
2. *(notable)* Compta amb una variable quantes vegades ha hagut de corregir el rumb durant una volta completa del circuit, i mostra-ho per REPL amb `print()` en acabar.
3. *(⭐⭐⭐)* Afegeix un **llindar intermedi**: si la lectura és "quasi al límit" (zona propera al llindar, ni clarament línia ni clarament fons), redueix encara més la velocitat en lloc de decidir de cop, com a aproximació bàsica a un control més suau.

    **Fites** (valida-les en ordre):
    1. El seguidor de línia bàsic funciona igual que al nucli si no es toca res més.
    2. La velocitat de correcció (requisit mínim) és clarament més baixa que la normal, i el rover no es descontrola.
    3. El llindar intermedi (ampliació 3) redueix la velocitat de manera progressiva, no amb un salt brusc.

---

## ⭐⭐ Repte 2 · Vehicle d'inspecció amb marge de seguretat variable (ampliació opcional)

**Context.** Una empresa de manteniment d'instal·lacions vol un petit robot d'inspecció que no s'aturi de cop davant de qualsevol obstacle, sinó que vagi frenant progressivament a mesura que s'hi acosta, per no fer moviments bruscos amb l'equip de mesura que porta a sobre.

> *Client: empresa de manteniment industrial · Lliurable: evita-obstacles amb marge de seguretat variable (frenada progressiva) · Món real: robots d'inspecció de tuberies, drons d'interior amb frenada per proximitat.*

**Què treballa.** Mesura de distància per temps de vol, decisió amb més de dos nivells, `evita_obstacles.py`.

**Requisit mínim.**
- Parteix de `evita_obstacles.py`: manté `mesura_distancia()` intacta (ja feta).
- Afegeix **dos llindars** en lloc d'un: per sobre del llindar alt (per exemple, 40 cm) avança a velocitat normal; entre els dos llindars (per exemple, 15-40 cm) avança més lent; per sota del llindar baix (15 cm) s'atura i gira.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Mostra al display una xifra o icona diferent segons la zona de distància en què es troba el rover (lluny / a prop / massa a prop).
2. *(notable)* Registra amb una llista les 5 últimes distàncies mesurades i mostra'n la mitjana per REPL amb `print()` en prémer A+B.
3. *(⭐⭐⭐)* Afegeix un **tercer llindar** encara més baix (per exemple, 5 cm) que faci retrocedir el rover una mica abans de girar, per als casos en què l'obstacle és massa a prop per girar amb seguretat.

    **Fites** (valida-les en ordre):
    1. Els dos llindars (requisit mínim) fan que la velocitat baixi de manera clara i progressiva, no de cop.
    2. El registre de distàncies (ampliació 2) és correcte i la mitjana té sentit.
    3. El retrocés d'emergència (ampliació 3) només s'activa quan l'obstacle és realment molt a prop, mai en la zona intermèdia.

---

## ⭐⭐⭐ Repte 3 · Rover de repartiment amb missió completa i registre de bord (ampliació opcional)

**Context.** Una empresa de repartiment intern d'un campus vol un rover que faci una ruta completa (sortir, seguir un carril fins a una zona de lliurament marcada amb un obstacle, aturar-se i tornar), i que quedi un registre de cada viatge per revisar-ne l'eficiència.

> *Client: servei de missatgeria interna d'un campus · Lliurable: rover amb missió completa (línia + obstacle + retorn) i registre de viatges amb `log` · Món real: robots de repartiment autònom d'interiors, robots de magatzem amb rutes fixes.*

**Què treballa.** Integració de comportaments, màquina de missions, mòdul `log` (SA6), `rover_missions.py`.

**Requisit mínim.**
- Parteix de `rover_missions.py`: manté el polsador STOP prioritari i l'estructura de missions (ja fets).
- Amplia (o crea de nou) una missió que **segueixi una línia** fins detectar un **obstacle** amb l'HC-SR04 (marca la "zona de lliurament"), s'aturi 2 segons (simulant l'entrega) i després **torni** enrere fins al punt de sortida (per exemple, amb un temporitzador o repetint els passos a l'inrevés).
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Registra amb `log.add()` cada vegada que el rover completa una missió, amb la durada total (usa `running_time()`).
2. *(notable)* Mostra per REPL (`print()`) quantes missions ha completat des que es va engegar la placa, llegint un comptador propi (a més del `log`).
3. *(⭐⭐⭐)* Fes que una segona missió es pugui encadenar automàticament a la primera (per exemple, "anar i tornar" dues vegades seguides) sense haver de tornar a prémer el botó B entremig.

    **Fites** (valida-les en ordre):
    1. El polsador STOP prioritari (herència de `rover_missions.py`) segueix funcionant exactament igual que al nucli, sense cap regressió.
    2. La missió completa (anar + aturar-se a l'obstacle + tornar) s'executa sencera sense intervenció manual entremig.
    3. El registre amb `log` (ampliació 1) queda llegible per USB amb almenys 2 entrades de missions completades.

---

## 🎨 Fes-lo teu (tria abans de començar)

> El repte fixa **què** ha de fer el sistema; **el context el poses tu**. Tria i anota-ho al quadern — un producte amb decisions teves sempre s'explica i es defensa millor:
> - **Repte 1:** decideix tu la velocitat de correcció i com la distingeixes visualment.
> - **Repte 2:** tria els teus tres llindars de distància i com els documentes.
> - **Repte 3:** decideix el disseny de la teva pista de proves (recorregut, on hi ha la "zona de lliurament").

## Material necessari (els tres reptes)

- micro:bit V2 + Micro:shield + cable micro-USB, individual.
- El **rover T3** muntat (Sessió 0), amb HC-SR04 i seguidor de línia funcionant, per als tres reptes.
- Un circuit de línia i un espai amb obstacles petits per provar-los.
- El simulador de python.microbit.org **no** simula cap component del rover: útil només per esbossar pseudocodi de l'estructura, no per validar-la.

## Per on començar (mètode de projecte + PRIMM)

1. **Analitzar:** quina part del programa base ja tinc feta i puc reutilitzar (calibratge, llindar, mesura de distància), i quina lògica nova necessito?
2. **Dissenyar (Predir):** dibuixa o descriu la missió/comportament *abans* d'escriure el codi.
3. **Programar/Prototipar:** parteix del programa base de `Classes/SA7/codi/` i modifica'l.
4. **Provar:** executa'l amb el rover real, observa, compara amb el teu disseny.
5. **Millorar:** afegeix una ampliació i documenta-la.

## Com s'avalua

| Rúbrica | Per què |
|---|---|
| **R1** (codi) | Funcionament, disseny del comportament, depuració. |
| **R3** (autonomia/control) | Llindars i marges ben calibrats, integració correcta dels sensors. |
| **R4** (documentació) | Quadern tècnic: llindars/factors, predicció, solució i millora. |

## Producte / entrega

- Codi `.py` comentat + entrada al **quadern tècnic** (llindars/factors, predicció, què he fet, error trobat i millora).

---

## Orientació docent

- **Errors freqüents:** llindars fixos sense calibrar-los sobre el circuit/espai real; oblidar comprovar el polsador STOP dins del bucle intern d'una missió llarga; barrejar la lògica de dues decisions en un sol `if` confús.
- **Diferenciació:** el mínim és idèntic per a tothom → tothom assoleix la base; les ampliacions 2-3 introdueixen registre de dades, missions encadenades i marges progressius.
- **Gestió d'aula:** el repte 1 només necessita el circuit de línia; el repte 2 només necessita espai amb obstacles; el repte 3 reaprofita el rover complet i necessita més espai/temps de pista.
- **Vincle avaluació:** producte coherent amb el de la SA7 (quadern tècnic, R4/R5) i amb les rúbriques R1/R3 del comportament autònom del rover.
