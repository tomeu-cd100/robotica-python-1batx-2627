# Peces impreses en 3D dels robots

Sis peces d'**OpenSCAD** paramètriques (`.scad`), geometries senzilles
(plaques/sabates amb forats M3), enllaçades des dels dossiers de projecte
(`Classes/00_General/00_Projecte_T1_Mascota.md`,
`00_Projecte_T2_Vehicle.md`, `00_Projecte_T3_Rover.md`).

## Fitxers

| Fitxer | Robot | Peça | Quantitat |
|---|---|---|---|
| `escaire_caixa.scad` | T1 · Mascota | Escaire d'angle per unir les plaques de DM sense encolar | 8 per mascota |
| `roda_boja.scad` | T2 · Vehicle (reaprofitat a T3) | Suport de la roda boja (canica de 16 mm) | 1 per vehicle |
| `suport_motor.scad` | T2 · Vehicle (reaprofitat a T3) | Sella per al motoreductor TT groc estàndard, encaixada a la ranura de brida del xassís | 2 per vehicle (esquerre + dret) |
| `suport_electronica.scad` | T2 · Vehicle (reaprofitat a T3) | Safata que aixeca la micro:bit + Micro:shield sobre el xassís, amb pas de cables per sota | 1 per vehicle |
| `suport_hcsr04.scad` | T3 · Rover | Suport frontal del sensor d'ultrasons HC-SR04 (peça nova, petita) | 1 per rover |
| `suport_seguidor_linia.scad` | T3 · Rover | Suport del seguidor de línia KS0050, sota el xassís (peça nova, petita) | 1 per rover |

Cap d'aquestes peces té plantilla de tall làser: totes són **impressió 3D**
(vegeu `Recursos/plantilles_laser/README.md` per a les dues úniques peces
làser del curs, mascota i xassís del vehicle). `suport_motor.scad` i
`suport_electronica.scad` tenen les seves mides de forats sincronitzades amb
`Recursos/plantilles_laser/xassis_vehicle.svg` (ranures de brida de 8×10 mm
als laterals; forats centrals M3 a 40×30 mm de separació).

## Com obrir-les i editar-les

1. Instal·la **OpenSCAD** (gratuït, <https://openscad.org/>).
2. Obre el fitxer `.scad` directament: al capdamunt hi ha una secció
   **«--- Parametres (mm) ---»** amb totes les mides editables (diàmetres
   de forat, gruixos, separacions...).
3. Canvia el paràmetre que calgui i prem **F5** (previsualitza) o **F6**
   (renderitza) per veure el resultat.
4. Exporta a STL (**Fitxer → Exporta → Exporta com a STL...**) per laminar
   i imprimir.

## Material i impressió

- **Material recomanat:** PLA (rigidesa suficient, fàcil d'imprimir, sense
  necessitat de cambra tancada).
- **Reblert:** 15-20 % és suficient per a totes sis peces (no són
  estructurals sota gran càrrega).
- **Suports:** `roda_boja.scad` necessita suports per a la cavitat
  esfèrica interior (o orientar-la amb l'obertura cap amunt durant el
  laminat); la resta s'imprimeixen sense suports si es col·loquen amb la
  cara plana a la base.
- **Temps orientatiu d'impressió** (Bambu Lab P2S Combo o equivalent,
  vegeu `Classes/00_General/00_Fil_conductor_construccions.md` §3.2):

| Peça | Temps orientatiu (1 unitat) |
|---|---|
| `escaire_caixa.scad` | ~5 min |
| `roda_boja.scad` | ~15 min |
| `suport_motor.scad` | ~10 min |
| `suport_electronica.scad` | ~12 min |
| `suport_hcsr04.scad` | ~10 min |
| `suport_seguidor_linia.scad` | ~10 min |

La impressora imprimeix **en lot** (diverses còpies alhora a la mateixa
placa): per a 20 alumnes, vegeu el càlcul complet de lots i temps a
`00_Fil_conductor_construccions.md` §3.2-3.3.

## Cargols i forats

Totes les peces usen **forats M3** (Ø 3,4 mm, amb marge per al cargol,
excepte els forats de muntatge dels mòduls sensor, que segueixen
l'estàndard del fabricant: Ø 2,2 mm). Els cargols M3 són material comú del
centre (vegeu la llista de peces de cada dossier de projecte).

---

⬅️ Torna a [`00_LLEGEIX-ME_Recursos.md`](../00_LLEGEIX-ME_Recursos.md).
