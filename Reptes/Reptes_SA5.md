# Reptes SA5 · Ràdio: robots que parlen

> 🧑‍🎓 **Quan toca fer-ne un?** El repte **⭐ és NUCLI OBLIGATORI — forma part del producte de la SA**: comença'l quan tinguis el **nucli al dia** (el repte «control remot bàsic» de la S3, tancat). Els reptes **⭐⭐/⭐⭐⭐ resten opcionals** (ampliació), per a qui vagi sobrat de temps. Ensenya el ⭐ al docent perquè el validi.

**Fes els reptes en ordre de dificultat: comença per ⭐, i si arribes a ⭐⭐⭐ hauràs passat pels tres.** Tots parteixen dels programes de `Classes/SA5/codi/` i fan servir la ràdio de la micro:bit. Es fan amb **maquinari real** (dues plaques aparellades puntualment): el simulador de python.microbit.org **sí simula la ràdio**, però només entre instàncies del simulador (vegeu [`SA5_esquemes_connexions.md`](../Classes/SA5/SA5_esquemes_connexions.md) §Simulació), útil per revisar la lògica del protocol.

> **Continguts SA5:** mòdul `radio` (`on`, `config(group=...)`, `send`, `receive`), protocol de missatges amb prefix, esdeveniment → acció, llistes i tuples bàsiques. · **Vocabulari/bases:** `Classes/SA0/`.

> **Format "producte real":** cada repte simula un **encàrrec** amb **client**, **lliurable** i **ús al món real**. El requisit tècnic no canvia; el marc ajuda a donar sentit al producte.

> 📻 **Recorda la regla d'individualitat:** el codi i el producte de cada repte són **teus**; l'aparellament amb un company és només per provar l'enviament/recepció.

---

## ⭐ Repte 1 · Xat de classe amb identificació (NUCLI OBLIGATORI)

**Context.** Un club de robòtica vol un petit "walkie-talkie" digital: cada membre s'identifica amb un nom curt en cada missatge, perquè es pugui saber sempre qui ha enviat què.

> *Client: club de robòtica escolar · Lliurable: xat amb identificació de remitent i historial · Món real: aplicacions de missatgeria, ràdios d'equip amb identificador de canal.*

**Què treballa.** `radio.on()`/`config()`/`send()`/`receive()`, llistes, `radio_missatges.py`.

**Requisit mínim.**
- Parteix de `radio_missatges.py`: enviament amb remitent, historial en una llista i `mostra_historic()` (ja fets).
- Escriu una funció **nova** `compta_missatges(remitent)` que recorri `historic` i **retorni** quants missatges són d'aquell remitent (els que comencen per `remitent + ":"`).
- Fes que, en prémer **B**, a més del darrer missatge es mostri el recompte dels teus: `display.scroll(compta_missatges(MEU_NOM))`.
- Codi comentat.

<details markdown="1">
<summary>🧗 Si t'encalles (repte ⭐): pistes esglaonades</summary>

**Nivell 1 — Pista conceptual.** Vols **comptar**, no mostrar: necessites una variable que comenci a 0 i pugi 1 cada cop que un missatge compleixi la condició. La condició és la mateixa idea de protocol que ja coneixes: un missatge «és de» un remitent si **comença per** `remitent + ":"` (`startswith`, com al protocol `CMD:`). I com que la funció **retorna** el resultat (no el mostra), qui la crida decideix què fer-ne.

**Nivell 2 — Pseudocodi.**
```
defineix compta_missatges(remitent):
  comptador comenca a 0
  per a cada missatge de historic:
    si el missatge comenca per remitent + ":":
      suma 1 al comptador
  retorna el comptador
```

**Nivell 3 — Esquelet amb TODO.** Cada `# TODO` és una línia sencera que has d'escriure tu.
```python
# SA5 - Repte 1 (BASTIDA / esquelet per a l'alumnat)
#
# QUE JA ESTA FET (no ho toquis):
#   - La llista historic ja es va omplint amb desa_al_historic().
#
# QUE HAS DE FER TU:
#   - Escriu compta_missatges(remitent): retorna quants missatges de
#     historic comencen per remitent + ":".
#
# EINES QUE POTS USAR (nomes conceptes ja vistos):
#   - for element in colleccio:   -> recorre els elements de la llista
#   - text.startswith(prefix)     -> True si el text comenca aixi
#   - return valor                -> torna el resultat a qui ha cridat

def compta_missatges(remitent):
    comptador = 0
    for missatge in historic:
        # TODO: si el missatge comenca per remitent + ":", suma 1
        pass
    # TODO: retorna el comptador
```

</details>

**Ampliacions graduades.**
1. *(bàsica)* Afegeix un comptador `total_rebuts` que sumi 1 cada cop que arriba un missatge nou, i mostra'l amb el botó A+B.
2. *(notable)* Filtra l'historial: una funció `mostra_historial_amb_paraula(paraula)` que només mostri els missatges que continguin una paraula concreta (per exemple, el nom d'un company).
3. *(⭐⭐⭐)* Afegeix una comanda especial `"NETEJA"` que, en rebre-la, buidi l'historial (`historic.clear()` o `historic = []`) de qui la rep.

    **Fites** (valida-les en ordre):
    1. `compta_missatges()` retorna el recompte correcte amb missatges de **dos remitents diferents** a l'historial.
    2. El filtre per paraula (ampliació 2) distingeix correctament els missatges que la contenen.
    3. La comanda `"NETEJA"` (ampliació 3) buida l'historial sense afectar cap altra funcionalitat.

---

## ⭐⭐ Repte 2 · Comandament amb gestos per a un joc (ampliació opcional)

**Context.** Una empresa d'oci vol un comandament sense botons visibles per a una atracció interactiva: els jugadors el controlen només inclinant-lo i sacsejant-lo.

> *Client: empresa d'oci/atraccions · Lliurable: comandament basat només en gestos · Món real: comandaments de consola amb sensors de moviment, controladors de realitat virtual.*

**Què treballa.** `accelerometer.was_gesture()`, protocol amb prefix, `comandament.py`.

**Requisit mínim.**
- Parteix de `comandament.py`: substitueix **tots** els botons per gestos (mínim `"left"`, `"right"`, `"shake"`; pots afegir-ne més, per exemple `"up"`/`"down"`).
- Documenta la teva taula gest → comanda.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Afegeix una comanda de **velocitat** (per exemple, `"CMD:V3"`) activada per un gest diferent (`"face up"`/`"face down"`), i fes que `receptor_vehicle.py` l'interpreti canviant la variable `VELOCITAT`.
2. *(notable)* Evita enviar el mateix gest repetidament de manera descontrolada: afegeix una petita pausa (`sleep`) o una variable d'estat perquè cada gest s'enviï només un cop clar.
3. *(⭐⭐⭐)* Fes que el comandament mostri al seu propi display quina ha estat la **darrera** comanda enviada (confirmació visual local, sense esperar resposta del receptor).

    **Fites** (valida-les en ordre):
    1. Els tres gestos bàsics es distingeixen clarament i mouen el vehicle correctament.
    2. La comanda de velocitat (ampliació 1) canvia visiblement la velocitat del vehicle.
    3. El control de repetició (ampliació 2) evita l'enviament descontrolat sense perdre cap gest real.

---

## ⭐⭐⭐ Repte 3 · Historial de comandes amb estadístiques (ampliació opcional)

**Context.** Un fabricant de robots de magatzem vol poder revisar, després d'una jornada de proves, quines ordres ha rebut més un robot teledirigit, per detectar si algun sensor o comandament falla.

> *Client: fabricant de robots industrials · Lliurable: registre de comandes amb estadístiques bàsiques · Món real: registres (logs) de telemetria, manteniment predictiu.*

**Què treballa.** Llistes i tuples, `receptor_vehicle.py`, recompte amb diccionaris o llistes paral·leles.

**Requisit mínim.**
- Parteix de `receptor_vehicle.py`: l'historial en tuples `(ordre, instant)` ja fet.
- Afegeix una funció `comanda_mes_frequent()` que recorri `historic_comandes` i digui quina ordre ha aparegut més vegades.
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Mostra per REPL (amb `print()`) el nombre total de comandes rebudes i quina ha estat la més freqüent en acabar una sessió de proves (per exemple, en prémer A+B a la placa receptora).
2. *(notable)* Calcula el temps mitjà entre dues comandes consecutives (diferència entre instants de tuples seguides).
3. *(⭐⭐⭐)* Detecta si el vehicle porta més de 3 segons **sense** rebre cap comanda nova i, en aquest cas, atura'l automàticament per seguretat (avança la idea de "llaç de control" de la SA6).

    **Fites** (valida-les en ordre):
    1. `comanda_mes_frequent()` retorna un resultat correcte amb, com a mínim, 4 comandes diferents provades.
    2. El temps mitjà entre comandes (ampliació 2) es calcula correctament amb els instants de `running_time()`.
    3. L'aturada de seguretat per inactivitat (ampliació 3) s'activa de manera fiable quan es deixa de rebre ràdio.

---

## 🎨 Fes-lo teu (tria abans de començar)

> El repte fixa **què** ha de fer el sistema; **el context el poses tu**. Tria i anota-ho al quadern — un producte amb decisions teves sempre s'explica i es defensa millor:
> - **Repte 1:** decideix què vols comptar i filtrar de l'historial (remitents, paraules…).
> - **Repte 2:** tria els teus **gestos** i la seva correspondència amb comandes.
> - **Repte 3:** decideix quines estadístiques et semblen més útils per detectar problemes.

## Material necessari (els tres reptes)

- micro:bit V2 + Micro:shield + cable micro-USB, per parella (banc de proves puntual).
- El vehicle T2 muntat a la SA4, per als reptes 2 i 3.
- El simulador de python.microbit.org **sí** simula la ràdio entre instàncies obertes del simulador, útil per revisar la lògica del protocol abans de provar-la amb maquinari real.

## Per on començar (mètode de projecte + PRIMM)

1. **Analitzar:** quin protocol ja tinc fet que puc reutilitzar, i quina comanda o estructura nova necessito?
2. **Dissenyar (Predir):** escriu *abans* què esperes que passi amb el protocol que triïs.
3. **Programar/Prototipar:** parteix del programa base de `Classes/SA5/codi/` i modifica'l.
4. **Provar:** executa'l aparellat amb un company, observa, compara amb la teva predicció.
5. **Millorar:** afegeix una ampliació i documenta-la.

## Com s'avalua

| Rúbrica | Per què |
|---|---|
| **R1** (codi) | Funcionament, protocol ben dissenyat, depuració. |
| **R4** (documentació) | Quadern tècnic: predicció, solució i millora. |
| **R5** (actitud) | Autonomia, respecte de la regla d'individualitat de la ràdio. |

## Producte / entrega

- Codi `.py` comentat + entrada al **quadern tècnic** (predicció, què he fet, error trobat i millora).

---

## Orientació docent

- **Errors freqüents:** `PREFIX`/`group` que no coincideixen exactament entre emissor i receptor; oblidar `radio.on()`; confondre `startswith()` amb `==` per comprovar el protocol.
- **Diferenciació:** el mínim és idèntic per a tothom → tothom assoleix la base; les ampliacions 2-3 introdueixen filtres, gestos combinats i estadístiques per a qui va sobrat.
- **Gestió d'aula:** tots requereixen aparellament puntual de dues plaques (banc de proves); el repte 2-3 reaprofita el vehicle muntat a la SA4.
- **Vincle avaluació:** producte coherent amb el de la SA5 (quadern tècnic, R4/R5) i amb la rúbrica R1 del repte «control remot bàsic».
