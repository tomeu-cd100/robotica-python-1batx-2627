# SA4 · Exemple resolt (model «jo ho faig») — Encapsulo un semàfor intermitent en funcions pròpies

> 🧑‍🎓 **Quan toca mirar-lo?** Després del teu **primer intent** amb `funcions_moviments.py`/`velocitat_pwm.py` (S1-S2) — mai abans. És un problema **anàleg** per veure *com es pensa*, no una solució per copiar: el repte «control per botons» l'has de fer amb el **teu** disseny.

> 🔗 **D'on ve i on va.** Aquest exemple és el **bessó comentat** de les pràctiques [`funcions_moviments`](codi/funcions_moviments/EXPLICACIO.md) i [`velocitat_pwm`](codi/velocitat_pwm/EXPLICACIO.md): la mateixa idea (repetir un bloc de codi → convertir-lo en funció amb paràmetres) amb un context expressament diferent — un **semàfor intermitent** en lloc d'un servo o un motor — perquè vegis **com es pensa**, no per copiar-lo. Quan l'hagis entès, torna a `control_per_botons` i fes el **teu** repte.

> **Nota docent:** mostra'l **després del primer intent** amb `funcions_moviments.py` i `velocitat_pwm.py`, mai abans. No és la solució del repte «control per botons» (que cada alumne/a fa amb el **seu** disseny): és un problema **anàleg** resolt pas a pas perquè l'alumnat vegi *com es pensa* el pas de codi repetitiu a funcions amb paràmetres, no què s'ha de copiar. Comenta en veu alta el pas «🧭 Com ho penso» (per què encapsular abans d'afegir més casos) i el «⚠️ Contraexemple».

---

## 🔑 El repte model

> Reprodueixo el LED semàfor de la SA2 (`semafor_rele.py`) però amb un comportament nou: en lloc d'un cicle fix, vull poder fer que **qualsevol** LED de la mascota parpellegi un nombre de vegades i a una velocitat que jo decideixi, sense escriure un `for` diferent cada cop.

Fa servir només conceptes de la SA4: **funcions** (`def`) amb **paràmetres**, i el mateix LED extern (P1) que ja coneixes de la SA2. Maquinari: LED extern al Micro:shield (Kit 1), el mateix muntatge de `led_parpelleig.py`.

---

## 🧭 Com ho penso (abans d'escriure res)

1. **Analitzo:** si escric el bucle de parpelleig 3 cops (per a 3, 5 i 10 parpellejos) tindria el mateix codi copiat 3 vegades, amb un únic número diferent cada cop — el senyal clar que necessito una **funció**.
2. **Identifico el paràmetre:** el que canvia entre les tres còpies és el **nombre de parpellejos**; això és exactament el que ha de ser el paràmetre de la meva funció.
3. **Decideixo si necessito un valor de retorn:** no, `parpelleja()` **fa** alguna cosa (encén i apaga el LED), no **calcula** cap número per fer servir després — per això no porta `return`, a diferència de `graus_a_pwm()` a `funcions_moviments.py`.
4. **🔮 PREDIU (fes-ho tu abans de llegir el codi):** si crido `parpelleja(3)` i després `parpelleja(1)`, el LED parpellejarà… ☐ **3 vegades i després 1** ☐ 4 vegades seguides ☐ només 1 vegada en total.

---

## 💡 La solució anotada

```python
# SA4 - exemple_semafor_funcions.py  (EXEMPLE MODEL, no es el producte)
# Encapsula el parpelleig d'un LED en una funcio amb parametre, en lloc de
# repetir el mateix bucle amb un numero diferent cada cop.
# Maquinari: LED extern al pin P1 del Micro:shield (Kit 1), com a
# led_parpelleig.py (SA2).

from microbit import *

PIN_LED = pin1


def parpelleja(vegades):
    # Funcio AMB UN PARAMETRE: substitueix copiar aquest bucle
    # una vegada per cada numero de parpellejos que necessites.
    for i in range(vegades):
        PIN_LED.write_digital(1)
        sleep(200)
        PIN_LED.write_digital(0)
        sleep(200)


# --- Demostracio: la MATEIXA funcio, cridada amb arguments diferents ---
parpelleja(3)
sleep(500)
parpelleja(1)
sleep(500)
parpelleja(10)
```

**Per què està escrit així (🌟):**
- **Un sol bloc de codi, molts usos:** `parpelleja()` és **una** definició; es crida amb l'argument que calgui (`3`, `1`, `10`) sense reescriure mai el `for`.
- **Sense valor de retorn perquè no calia:** la funció **actua** sobre el LED (efecte directe), no calcula cap número per reutilitzar després — el mateix criteri que distingeix `mou_servo()` (sense `return`) de `graus_a_pwm()` (amb `return`) a `funcions_moviments.py`.
- **Nom que explica la intenció:** `parpelleja(vegades)` es llegeix quasi com una frase; és el mateix principi que `avancar(velocitat)` a `velocitat_pwm.py`.

---

## 🔬 Provo i mesuro

- **Predicció ✔:** `parpelleja(3)` fa 3 parpellejos i, en acabar, `parpelleja(1)` en fa 1 més — són dues crides **independents**, no s'acumulen.
- **Provo la funció sola al REPL:** abans d'escriure el programa sencer, crido `parpelleja(1)` directament al REPL per comprovar que fa exactament un parpelleig, no dos ni zero.
- **Sense maquinari:** la **lògica** (bucle, paràmetre) es pot revisar llegint el codi, però el parpelleig real només es veu amb el LED connectat.

---

## ⚠️ Contraexemple (errors típics i com es detecten)

- **Escric el bucle tres vegades enlloc d'una funció:** el programa "funciona" però qualsevol canvi (per exemple, la velocitat del parpelleig) s'ha de fer **tres cops**, i és fàcil oblidar-ne un. **Pista:** si copies i enganxes el mateix bloc més d'un cop canviant només un número, aquest número hauria de ser un paràmetre.
- **Poso un `return` a `parpelleja()` sense necessitar-lo:** MicroPython no dona error, però el valor retornat (`None`, per defecte) no serveix per a res i confon qui llegeix el codi. **Pista:** si la funció només **fa** alguna cosa (no calcula cap dada per reutilitzar), no cal `return`.
- **Crido `parpelleja` sense parèntesis:** el programa no dona error visible però tampoc parpelleja mai el LED (estàs referint-te a la funció, no cridant-la). **Pista:** `nom_funcio` és el valor de la funció; `nom_funcio()` l'executa.
- **El LED no parpelleja mai:** component al pin equivocat o polaritat invertida (pota llarga cap al senyal). **Pista:** repassa l'[esquema](SA4_esquemes_connexions.md) i el de la SA2.

---

## 📔 Diari de bord (entrada model, 1a persona)

> **Sessions 1-2:** He après a **encapsular** codi repetitiu en una funció amb paràmetre. He analitzat un semàfor intermitent: en lloc d'escriure el bucle de parpelleig un cop per cada nombre de parpellejos que volia, l'he convertit en `parpelleja(vegades)` i l'he cridat amb arguments diferents. Vaig **predir** que dues crides seguides (`parpelleja(3)` i `parpelleja(1)`) donarien 3 i després 1 parpelleig, i es va complir. Al principi no sabia si calia un `return`: l'error va ser no adonar-me que `parpelleja()` **fa** alguna cosa (no calcula cap valor per fer servir després), així que no en necessitava cap. **Evidència:** codi comentat + prova al REPL cridant la funció amb un valor conegut.

**Per què és una bona entrada:** usa el **vocabulari clau** (funció, paràmetre, valor de retorn), explica *el com* (per què no calia `return`), i és **honesta amb el dubte** (si calia o no un `return`) i com es va resoldre.

---

*Exemple resolt de la SA4. Model de treball per a l'alumnat (alliberament gradual: es mostra després del primer intent). Es recolza en `codi/funcions_moviments` i `codi/velocitat_pwm`. El repte «control per botons» real l'has de fer amb el **teu** disseny, no amb aquest. Llicència CC BY-SA 4.0.*
