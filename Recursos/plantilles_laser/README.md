# Plantilles de tall làser dels robots

Plantilles de **DM de 3 mm** per als dos robots del curs que tenen peça
làser pròpia (mascota T1 i vehicle T2). Segueixen el conveni de capes per
color: el **negre** marca les línies de **tall** i el **vermell** marca les
zones de **gravat** (personalització i etiquetes de muntatge). Totes les
mides estan en mil·límetres reals i el `viewBox` de cada SVG és a escala
1:1, de manera que es poden importar directament a la talladora sense
reescalar.

> 🔑 **Font única del contingut d'aquestes plantilles:** els dossiers de
> projecte `Classes/00_General/00_Projecte_T1_Mascota.md` i
> `00_Projecte_T2_Vehicle.md`, i el calendari de fabricació
> `00_Fil_conductor_construccions.md` (peces, mides aproximades i nesting).
> Si hi ha cap discrepància, aquests documents manen.

## Fitxers

| Fitxer | Robot | Peces | Mida generada (1 unitat) |
| --- | --- | --- | --- |
| `mascota.svg` | T1 · Mascota | Base + 4 laterals + tapa + 2 orelles (8 peces) | 158 × 120 mm |
| `xassis_vehicle.svg` | T2 · Vehicle | Xassís amb encaixos de motor integrats (1 peça) | 190 × 140 mm |

**El rover (T3) NO té cap plantilla làser pròpia**: reaprofita íntegrament
el xassís ja tallat per al vehicle (T2) — vegeu
`Classes/00_General/00_Projecte_T3_Rover.md` («El rover NO és un xassís
nou») i `00_Fil_conductor_construccions.md` §3.1 («T3 no consumeix hores de
làser»). Les seves dues peces d'ampliació (suport de l'HC-SR04 i suport del
seguidor de línia) són **impressió 3D** (`Recursos/peces_3d/*.scad`), fora
de l'abast d'aquest script i d'aquesta carpeta.

## Mides i gruix del material

- **Material:** DM (fibra de densitat mitjana) de **3 mm** de gruix.
- **Forats de muntatge:** Ø 3,2 mm (cargol M3), a 8 mm de cada cantonada de
  peça — encaixen amb els escaires impresos en 3D (`escaire_caixa.scad`) que
  uneixen les plaques sense encolar.
- **Finestra de micro servo** (mascota, orelles/cua): 23,5 × 12,5 mm amb 2
  forats de cargol de Ø 2 mm.
- **Ranura de servo/orella** (mascota): 10,4 × 3,4 mm a la tapa; cada orella
  porta una pestanya de 10 mm integrada al contorn de tall que hi encaixa.
  Si un equip redibuixa la seva pròpia orella, ha de **mantenir aquesta
  pestanya de 10 mm**: és l'únic requisit fix.
- **Encaixos de motor** (vehicle): ranures de 8 × 10 mm als dos laterals del
  xassís per a les brides que subjecten cada motoreductor; 2 forats M3 al
  davant per al suport de la roda boja imprès en 3D.

## Nesting per a 20 unitats (grup de 15-20 alumnes)

Segons `00_Fil_conductor_construccions.md` §3.1, amb un tauler de treball de
**600 × 400 mm**:

| Robot | Mida/unitat | Unitats/tauler | Taulers per a 20 alumnes |
| --- | --- | --- | --- |
| Mascota (`mascota.svg`) | 158 × 120 mm | 2 (costat a costat, 316 × 120 mm; hi cabrien 3, però es reserva marge de tall/pinces) | 10 |
| Vehicle (`xassis_vehicle.svg`) | 190 × 140 mm | 2 (costat a costat, 380 × 140 mm) | 10 |
| Rover | — | — | 0 |
| **Total anual** | | | **20 taulers** |

La mida de la mascota (158 × 120 mm) és propera a l'aproximació «~180 ×
140 mm» de `00_Fil_conductor_construccions.md` §3.1 (caixa de sobretaula
petita, pensada per a micro:bit + Micro:shield + sensors del Kit, no per a
un Arduino UNO); qualsevol ajust del generador (mida de la caixa, forma de
les orelles) es reflecteix automàticament aquí en tornar a executar
l'script.

El **nesting** (agrupar les còpies personalitzades de 2 alumnes al mateix
tauler abans de llançar el tall) és el que fa viable tallar fora d'horari
lectiu: vegeu el calendari de lots (setmanes S-2/S-1/S0) a
`00_Fil_conductor_construccions.md` §3.3.

## Com regenerar-les

`mascota.svg` i `xassis_vehicle.svg` **no s'editen a mà**: es generen amb
l'script paramètric `tools/genera_plantilles_laser.py`:

```
py -3.13 tools/genera_plantilles_laser.py
```

Si cal canviar una mida, un forat o una etiqueta, modifica l'script i
torna'l a executar; això sobreescriu els dos fitxers.

## Com importar-les a la talladora làser

1. Importa l'SVG directament (`Fitxer → Importa`, xTool Creative Space o
   programari equivalent).
2. Assigna la potència i la velocitat de **tall** a les línies **negres** i
   la configuració de **gravat** (potència baixa, més passades) a les línies
   **vermelles**, segons el gruix real del DM disponible (referència: 3 mm;
   calibra sempre amb una peça de prova).
3. Comprova a la previsualització que cap peça surt del tauler de treball
   abans de llançar el tall.

## Personalització (còpia de l'alumnat)

Cada alumne fa una **còpia pròpia** de `mascota.svg` (T1) o
`xassis_vehicle.svg` (T2) i **només edita les línies vermelles**: la cara de
la mascota i el contorn de les orelles (mantenint la pestanya de 10 mm), o
el nom gravat al xassís del vehicle. Les línies de tall en negre i els
forats de muntatge **no es toquen** perquè les peces continuïn encaixant amb
els escaires i suports impresos en 3D. El docent valida cada disseny abans
d'agrupar-lo per nesting (vegeu el flux complet a
`00_Projecte_T1_Mascota.md` §«Fabricació i personalització» i
`00_Projecte_T2_Vehicle.md` §«Fabricació i personalització»).

---

⬅️ Torna a [`00_LLEGEIX-ME_Recursos.md`](../00_LLEGEIX-ME_Recursos.md).
