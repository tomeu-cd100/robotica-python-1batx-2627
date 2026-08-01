# El vehicle s'atura SEMPRE que cal: STOP prioritari (Sessió 2-3 — producte)

**Quan es fa:** Sessions 2-3 · **Fitxer:** `vehicle_seguretat.py` · **Maquinari:** vehicle T2 (motoreductors **M1**=P13/P14, **M2**=P15/P16), LED indicador **P1**, polsador STOP **P12** ([esquemes](../../SA6_esquemes_connexions.md)); es prova aparellat puntualment amb la placa d'un company que porti `comandament.py` (SA5)

> 🎯 **Producte del Projecte T2.** Aquest programa és el que **tanca el vehicle teledirigit** a la **Sessió 3**: s'avalua amb **R1**, **R3** (criteri "Autonomia/control") i **R4**.

## 🎯 Per què fem aquesta pràctica

A la SA5 el vehicle obeïa **ordres puntuals**: cada missatge de ràdio disparava un moviment. Aquí el vehicle passa a ser un **sistema de control amb màquina d'estats**: en tot moment és en un estat (**RUN** en marxa, **STOP** aturat), i l'**STOP** és **prioritari sobre qualsevol altra cosa**: es dispara amb el **polsador físic** (P12) o amb la **comanda de ràdio dedicada `"X"`**, i interromp el moviment **a l'instant**, sigui quin sigui l'estat previ.

## 🔮 Abans d'executar: prediu

Si el vehicle està avançant (`estat == RUN`) i just en aquell moment arriba per ràdio la comanda `"X"`, però mig segon abans havia arribat `"F"` sense processar-se encara: quin dels dos "guanya"? Per què el codi comprova el polsador **abans** de mirar el missatge de ràdio a cada volta del bucle?

## 🧠 El codi, per blocs

### Bloc 0 — El pull-up del polsador es configura ABANS del bucle

```python
POLSADOR_STOP = pin12
POLSADOR_STOP.set_pull(POLSADOR_STOP.PULL_UP)
```

Sense aquesta línia, la lectura del pin **flota** (no té repòs definit) i pot donar falsos STOP o, pitjor, no detectar-ne un de real. Amb `PULL_UP`, el pin llegeix `1` en repòs i `0` quan es prem el polsador (per això el bloc 1 fa `if not ...`).

### Bloc 1 — El polsador es mira SEMPRE primer

```python
if not POLSADOR_STOP.read_digital():
    actualitza_estat(STOP)
```

Aquesta línia és la **primera** cosa que fa el bucle, abans de mirar cap missatge de ràdio. Si es mirés després (o només "de tant en tant"), hi hauria una finestra de temps en què el polsador estaria premut i el vehicle encara seguiria movent-se.

### Bloc 2 — Un únic lloc que canvia l'estat

```python
def actualitza_estat(nou):
    global estat
    if nou == STOP:
        aturar()
        display.show(Image.NO)
    estat = nou
    actualitza_led()
```

Igual que a `maquina_estats_semafor.py`, **tot** el que ha de passar en entrar a STOP (aturar motors, mostrar la cara, actualitzar el LED) viu en un sol lloc. Cap altra part del programa pot "oblidar-se" de cridar `aturar()`: sempre que `estat` val `STOP`, els motors ja estan a 0.

### Bloc 3 — La comanda "X": STOP també per ràdio

```python
if ordre == "X":
    actualitza_estat(STOP)
```

`"X"` és una comanda **nova** d'aquesta SA, amb la mateixa prioritat que el polsador físic: qualsevol missatge `"CMD:X"` atura el vehicle sense excepcions, encara que en aquell moment s'estigués processant una altra ordre.

### Bloc 4 — Sortir de STOP només amb una ordre explícita

```python
elif estat == STOP and ordre in ("F", "B", "L", "R"):
    actualitza_estat(RUN)
```

El vehicle **no** torna a RUN tot sol: cal una ordre de moviment explícita per ràdio. Això evita que el vehicle "arrenqui sol" per un missatge perdut o repetit després d'una emergència.

## ⚠️ Errors que veuràs segur

| Símptoma | Causa probable |
|---|---|
| L'STOP no interromp el moviment | El polsador es comprova només en algun punt del bucle, no a **cada** volta (revisa que sigui el primer `if`) |
| El vehicle no torna a moure's mai després d'un STOP | Falta la transició `STOP -> RUN` amb una ordre de moviment nova |
| El LED no s'apaga en STOP | `actualitza_led()` no s'ha cridat des de `actualitza_estat()` |
| El vehicle es mou sol sense cap comandament proper | Un altre grup de la classe fa servir el mateix `GRUP`: canvia'l |

## 🔗 On ho aplicaràs

- **Ara mateix:** tanca el **Projecte T2** (vehicle teledirigit amb aturada d'emergència), avaluat amb R1/R3/R4 a la Sessió 3.
- **+ Ampliació:** l'estat **ALERTA** (reservat però no usat al nucli) es pot activar amb un sensor d'ultrasons o de temperatura, sense canviar l'estructura de la màquina d'estats — vegeu [`SA6_fitxa_ampliada.md`](../../SA6_fitxa_ampliada.md).
- **Simulador:** python.microbit.org **no** simula motors ni el relé; només es pot revisar la **lògica** de la màquina d'estats i del protocol de ràdio.

> ⭐⭐/⭐⭐⭐ **Has acabat abans?** El repte ⭐ ja és nucli obligatori (vegeu la fitxa base). Si vols anar més enllà, tria un repte ⭐⭐/⭐⭐⭐ a **[Reptes de la SA6](../../../../Reptes/Reptes_SA6.md)**.
