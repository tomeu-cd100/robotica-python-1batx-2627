# Reptes SA1 · Hola, robot!

> 🧑‍🎓 **Quan toca fer-ne un?** El repte **⭐ és NUCLI OBLIGATORI — forma part del producte de la SA**: comença'l quan tinguis el **nucli al dia** (les activitats de la fitxa). Els reptes **⭐⭐/⭐⭐⭐ resten opcionals** (ampliació), per a qui vagi sobrat de temps. Ensenya el ⭐ al docent perquè el validi.

**Fes els reptes en ordre de dificultat: comença per ⭐, i si arribes a ⭐⭐⭐ hauràs passat pels tres.** Tots parteixen dels programes de `Classes/SA1/codi/` i del model **entrada→procés→sortida**. Es poden fer al simulador de [python.microbit.org](https://python.microbit.org) o a la placa física.

> **Continguts SA1:** robot i sistema embegut, digital vs analògic, `display`, `button_a`/`button_b`, `accelerometer`, `random`. · **Vocabulari/bases:** `Classes/SA0/`.

> **Format "producte real":** cada repte simula un **encàrrec** amb **client**, **lliurable** i **ús al món real**. El requisit tècnic no canvia; el marc ajuda a donar sentit al producte.

---

## ⭐ Repte 1 · Targeta de benvinguda digital (NUCLI OBLIGATORI)

**Context.** L'escola vol una petita "targeta" digital de presentació per al dia de portes obertes: cada alumne/a en fa una amb el seu nom.

> *Client: secretaria del centre · Lliurable: targeta digital de presentació · Món real: senyalització i identificació personal (targetes d'accés, etiquetes intel·ligents).*

**Què treballa.** `display.scroll()`, `display.show()`, `Image`, `sleep()`.

**Requisit mínim.**
- El display mostra el teu **nom** (`scroll`) i, després, una **imatge fixa** que et representi (`show` amb una `Image` predefinida).
- Codi comentat, partint de `hola_mon.py`.

<details markdown="1">
<summary>🧗 Si t'encalles (repte ⭐): pistes esglaonades</summary>

**Nivell 1 — Pista conceptual.** `hola_mon.py` ja et mostra el patró: un text amb `display.scroll()`, una pausa amb `sleep()` i després una imatge fixa amb `display.show()`. Al teu repte només cal canviar **quin** text i **quina** imatge — l'estructura (scroll → sleep → show) es manté igual.

**Nivell 2 — Pseudocodi.**
```
importa microbit
mostra el TEU NOM en desplacament (scroll)
espera una mica perque es vegi sencer
mostra una imatge fixa que et representi (show)
```

**Nivell 3 — Esquelet amb TODO.** Copia'l a un programa nou i completa'l; l'esquelet **no és la solució**, encara has de triar el nom i la imatge.
```python
# SA1 - Repte 1 (BASTIDA / esquelet per a l'alumnat)
#
# QUE JA ESTA FET (no ho toquis):
#   - L'import de microbit ja hi es.
#
# QUE HAS DE FER TU:
#   - Substitueix "NOM" pel teu nom (entre cometes).
#   - Tria una Image predefinida que et representi.
#
# EINES QUE POTS USAR (nomes conceptes de la SA1):
#   - display.scroll(text)    -> mostra text desplacant-se
#   - sleep(ms)                -> pausa en mil.lisegons
#   - display.show(Image....)  -> mostra una imatge fixa

from microbit import *

display.scroll("NOM")     # TODO 1: posa el teu nom
sleep(500)
display.show(Image.___)   # TODO 2: tria una imatge que et representi
```

</details>

**Ampliacions graduades.**
1. *(bàsica)* Afegeix una **segona imatge** (per exemple, alterna dues cares o símbols amb un `sleep()` entre totes dues).
2. *(notable)* Repeteix el cicle nom→imatge **tres vegades seguides** amb un `while` (sense copiar i enganxar el mateix bloc tres cops).
3. *(⭐⭐⭐)* Crea una **imatge pròpia** amb `Image("90009:09090:00900:09090:90009")` (o el patró que tu dissenyis) en lloc d'usar-ne una de predefinida.

    **Fites** (valida-les en ordre):
    1. Saps explicar què vol dir cada dígit del text de la teva `Image` pròpia (0 = apagat, 9 = màxima brillantor).
    2. La teva imatge es veu correctament al simulador (ni buida ni tota encesa).
    3. El programa alterna nom i imatge pròpia en un `while True:` sense bloquejar-se.

---

## ⭐⭐ Repte 2 · Semàfor d'humor amb tres estats (ampliació opcional)

**Context.** Una joguina educativa expressa el seu "humor" segons com la toquis: en repòs, contenta o sorpresa.

> *Client: fabricant de joguines educatives · Lliurable: joguina que expressa 3 estats d'ànim · Món real: interfícies expressives (robots socials, assistents amb "cara").*

**Què treballa.** `while True:`, `if`/`elif`/`else`, `button_a`/`button_b`, comptadors.

**Requisit mínim.**
- Parteix d'`emocions_botons.py`: el botó A mostra una cara, el B una altra, i sense prémer cap dels dos, una tercera (ja fet).
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Afegeix un **tercer estat** quan es premen **A i B alhora** (`button_a.is_pressed() and button_b.is_pressed()`): per exemple, una cara sorpresa.
2. *(notable)* Compta quants cops s'ha premut el botó A amb `button_a.get_presses()` i mostra'l al display quan es toqui el **logo** (`pin_logo.is_touched()`).
3. *(⭐⭐⭐)* Encapsula cada estat en una **funció pròpia** (`cara_contenta()`, `cara_sorpresa()`...) cridada des del `while True:`.

    **Fites** (valida-les en ordre):
    1. El tercer estat (A+B) funciona sense interferir amb els altres dos.
    2. `get_presses()` mostra un comptador que **puja** cada vegada que es prem A (comprova-ho prement-lo diverses vegades seguides).
    3. El `while True:` queda reduït a poques línies llegibles que només criden funcions, sense codi `display.show(...)` repetit.

---

## ⭐⭐⭐ Repte 3 · Dau doble sense repeticions (ampliació opcional)

**Context.** Un joc de taula necessita un "dau electrònic" que llanci dos daus alhora i eviti que surti dues vegades seguides el mateix resultat (per fer el joc més imprevisible).

> *Client: dissenyador de jocs de taula · Lliurable: dau electrònic de dos daus · Món real: generadors de nombres aleatoris en jocs i sorteigs.*

**Què treballa.** `accelerometer.was_gesture()`, `random.randint()`, variables que "recorden" l'estat anterior.

**Requisit mínim.**
- Parteix de `dau_sacseig.py`: en sacsejar la placa, mostra un nombre aleatori d'1 a 6 (ja fet).
- Codi comentat.

**Ampliacions graduades.**
1. *(bàsica)* Fes que cada sacseig mostri **la suma de dos daus** (dos `random.randint(1, 6)` sumats, resultat entre 2 i 12).
2. *(notable)* Guarda l'últim resultat en una **variable** i, si el nou sacseig dona el mateix número, torna a tirar fins que surti un de diferent.
3. *(⭐⭐⭐)* Porta un **comptador de tirades** i mostra'l (per exemple, tocant el logo) sense interrompre el joc principal.

    **Fites** (valida-les en ordre):
    1. La suma de dos daus (2-12) es mostra correctament amb `str(...)` (compte: cal dos dígits per als resultats de 10, 11 i 12; investiga `display.scroll(str(suma))` per a aquests casos).
    2. El programa detecta quan surt el mateix resultat que l'anterior i **el torna a tirar** sense que l'alumnat ho noti com un error.
    3. El comptador de tirades es manté correcte després de 10 sacsejos seguits provats al simulador.

---

## 🎨 Fes-lo teu (tria abans de començar)

> El repte fixa **què** ha de fer el sistema; **el context el poses tu**. Tria i anota-ho al quadern — un producte amb decisions teves sempre s'explica i es defensa millor:
> - **Repte 1:** tria la teva **imatge pròpia** (inicial, símbol, emoji senzill).
> - **Repte 2:** decideix **quines cares** representen cada estat i per què.
> - **Repte 3:** decideix si el "dau" té regles pròpies (per exemple, tornar a tirar si surt un 7 exacte).

## Material necessari (els tres reptes)

- micro:bit V2 sola (o el simulador de [python.microbit.org](https://python.microbit.org), pla B recomanat).

## Per on començar (mètode de projecte + PRIMM)

1. **Analitzar:** què vull que mostri el display i quan?
2. **Dissenyar (Predir):** escriu *abans* quines línies de codi necessitaràs.
3. **Programar/Prototipar:** parteix del programa base de `Classes/SA1/codi/` i modifica'l.
4. **Provar:** executa'l, observa, compara amb la teva predicció.
5. **Millorar:** introdueix variables/funcions i una ampliació.

## Com s'avalua

| Rúbrica | Per què |
|---|---|
| **R1** (codi) | Funcionament, estructura, llegibilitat, depuració. |
| **R4** (documentació) | Quadern tècnic: predicció, solució i millora. |
| **R5** (actitud) | Autonomia, gestió de l'error. |

## Producte / entrega

- Codi `.py` comentat + entrada al **quadern tècnic** (predicció, què he fet, error trobat i millora).

---

## Orientació docent

- **Errors freqüents:** oblidar `from microbit import *`; `sleep()` massa curt (no es veu el canvi); oblidar `str(...)` en mostrar números; indentació incorrecta als `if`.
- **Diferenciació:** el mínim és idèntic per a tothom → tothom assoleix la base; les ampliacions 2-3 introdueixen funcions i variables d'estat per a qui va sobrat.
- **Gestió d'aula:** tots són simulables al 100 % sense maquinari; el repte 3 connecta amb l'ampliació `dau_sacseig.py` de la SA1.
- **Vincle avaluació:** producte coherent amb el de la SA1 (quadern tècnic, R4/R5) i amb la rúbrica R1 de codi.
