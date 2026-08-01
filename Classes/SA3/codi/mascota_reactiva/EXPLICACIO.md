# Mascota reactiva (producte de la SA3)

**Quan es fa:** Sessió 3 (repte, producte de la SA — es tanca aquí) · **Fitxer:** `mascota_reactiva.py` · **Maquinari:** [esquemes de connexions](../../SA3_esquemes_connexions.md) i [dossier de la mascota](../../../00_General/00_Projecte_T1_Mascota.md) — LED **P1**, brunzidor **P2**, PIR **P8**, polsador **P12** (cablatge EXACTE de la mascota)

> ✋ **Aquesta pàgina mostra la SOLUCIÓ del producte "mascota reactiva".** És el **producte de la SA3** (i tanca la mascota T1): intenta-ho pel teu compte a l'Activitat 3 de la [fitxa](../../SA3_fitxa_alumnat.md) abans de mirar-la sencera. Si t'encalles, l'[esquelet del dossier de la mascota](../../../00_General/00_Projecte_T1_Mascota.md#-si-tencalles-lesquelet-del-programa) et dona l'estructura amb `# TODO`.

## 🎯 Per què fem aquesta pràctica

Aquesta és la **integració**: cada sensor de la mascota (so, llum, PIR, polsador, acceleròmetre) llegit per separat i comparat amb un llindar decideix **una emoció**, i cada emoció té la seva cara i el seu so. És exactament el mètode de `nivell_llum`/`termometre` (llegir → comparar amb un llindar → decidir) però amb **cinc** sensors alhora i una prioritat entre ells.

## 🔮 Abans d'executar: prediu

Si fas un soroll fort **i** al mateix moment el PIR detecta moviment, quina emoció guanyarà? Mira l'ordre de `llegeix_sensors()` abans de respondre.

## 🧠 El codi, per blocs

### Bloc 1 — Una funció per estat: `canvia_emocio()`

```python
def canvia_emocio(nova):
    global emocio, t_ultim_estimul
    if nova == emocio:
        return
    emocio = nova
    t_ultim_estimul = running_time()
    if emocio == CONTENT:
        display.show(Image.HAPPY)
        music.play(['C4:2', 'E4:2', 'G4:2'], pin=pin2, wait=False)
    ...
```

Igual que `tot_apagat()` + una fase a `semafor_rele.py` (SA2), cada emoció és un bloc `elif` amb **la seva** cara i **el seu** so. El `if nova == emocio: return` evita repetir la cara/el so si ja hi som (sense això, la mascota "parpellejaria" la mateixa expressió sense parar).

> 🔑 **Què fa `global`:** sense aquesta línia, `emocio = nova` dins de la funció crearia una variable **nova i local** que desapareixeria en sortir de `canvia_emocio()`, sense tocar la `emocio` de fora. `global emocio, t_ultim_estimul` diu explícitament que aquestes dues variables **no** són noves: són les de fora de la funció, i la funció les vol modificar de debò. Es fa servir aquí perquè `emocio` i `t_ultim_estimul` s'han de recordar entre voltes del `while True:`.

### Bloc 2 — Un estímul per volta: `return` després de decidir

```python
if soroll > LLINDAR_SOROLL:
    canvia_emocio(ESPANTAT)
    return

if llum < LLINDAR_FOSCOR:
    canvia_emocio(ADORMIT)
    return
```

`llegeix_sensors()` comprova els estímuls **en ordre de prioritat** i surt (`return`) en el primer que es compleix: el soroll fort mana per sobre de la foscor, la foscor per sobre del PIR, etc. És una decisió de disseny (que tu pots reordenar al teu repte) no una regla fixa.

### Bloc 3 — Antirebot per software al polsador

```python
if pin12.read_digital() == 0:
    ara = running_time()
    if ara - t_ultim_polsador > ANTIREBOT_MS:
        t_ultim_polsador = ara
        canvia_emocio(CONTENT_CARICIA)
    return
```

El polsador té *pull-up* (`pin12.set_pull(pin12.PULL_UP)`): en repòs llegeix `1`, i `0` quan es prem. Sense l'antirebot, un sol "clic" físic es podria detectar com moltes premudes seguides (rebot mecànic del contacte); comparant amb `t_ultim_polsador` només acceptem una detecció cada `ANTIREBOT_MS`.

### Bloc 4 — Tornar a la calma sola

```python
if emocio != ADORMIT and running_time() - t_ultim_estimul > TEMPS_CALMA:
    canvia_emocio(CONTENT)
```

Si fa `TEMPS_CALMA` mil·lisegons que no passa res, la mascota torna sola a l'estat `CONTENT` (excepte si està `ADORMIT`: la foscor l'ha de despertar, no un temporitzador).

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| La cara no canvia mai | `llegeix_sensors()` no s'executa a cada volta del `while True:`, o falta el `return` després de cada `canvia_emocio()` |
| El PIR dispara sempre (fals positiu) | Encara en temps d'estabilització (30-60 s) o sensibilitat massa alta al potenciòmetre del mòdul |
| El polsador detecta moltes premudes d'un sol clic | Falta l'antirebot (`ANTIREBOT_MS`), o el llindar és massa curt |
| Un estímul "no arriba mai" | Un estímul anterior de més prioritat el tapa sempre: revisa l'ordre dels `if` a `llegeix_sensors()` |

## 🔗 On ho aplicaràs

- **Ara mateix:** és el **producte de la SA3** i **tanca la mascota T1** (mini-defensa breu, R1/R2/R3).
- **Simulador:** python.microbit.org simula l'acceleròmetre, els botons i la llum/so **interns**, però **no** el PIR ni el polsador externs (Kit 2/Kit 1): substitueix-los temporalment per `button_a.is_pressed()` per validar la lògica, i recalibra amb el maquinari real.
- **SA4:** el servo (P0) ja és a la mascota però **no** es programa fins llavors.

> ⭐ **Has acabat abans?** Tria un repte a **[Reptes de la SA3](../../../../Reptes/Reptes_SA3.md)**.
