# SA9 · Plantilla del dossier tècnic

> 🧑‍🎓 **Quan toca omplir-la?** Comença-la a la **Sessió 3** (Provar i millorar) amb el que ja tinguis fet, i **tanca-la a la Sessió 4** (Comunicar), abans de la defensa oral. És el teu lliurable principal: la base de **R4** (documentació) i el guió de la teva defensa.

> **Individual.** El dossier és teu: encara que hagis mirat l'[exemple resolt](SA9_exemple_resolt.md) o parlat el disseny amb companys, el text, el codi i les captures són els del **teu** projecte.

**Nom:** ______________________  **Data:** __________  **Repte triat:** ______________________ (vegeu [`SA9_reptes_proposats.md`](SA9_reptes_proposats.md))

---

## 1 · Objectiu

Descriu, en 3-5 frases, **quin problema real** resol el teu repte i **per a qui** (context/client, com als reptes: "Client: ... · Món real: ..."). Inclou els **requisits mínims** que et vas fixar a la Sessió 1 (Idear).

______________________________________________________________________

______________________________________________________________________

## 2 · Disseny

- **Esbós/croquis** de la solució (dibuix, foto del prototip de paper, o descripció de la disposició física).
- **Decisions de disseny clau** (mínim 2): què vas triar i **per què** ho vas triar així (rúbrica R4·DO, indicador "Decisió tècnica justificada").
- **Alternatives descartades** (opcional, ⭐ per a nota alta): què vas considerar i per què no ho vas fer servir.

______________________________________________________________________

## 3 · Esquema de connexions

Taula de pins del maquinari **nou** que afegeix el teu repte (el maquinari heretat del rover ja és a `00_Fil_conductor_construccions.md` §1b; no el repeteixis, cita'l):

| Component | Pin | Tipus | Notes |
|---|---|---|---|
| | | | |
| | | | |

> ⚠️ Recorda: pins ADC vàlids del Micro:shield: **P0, P1, P2, P3, P4, P10**. Consulta els pins **lliures** al mapa de pins abans de triar-ne un de nou.

## 4 · Codi comentat

Enganxa aquí (o enllaça al teu fitxer `.py`) el codi final del teu projecte, partint de [`plantilla_projecte.py`](codi/plantilla_projecte/plantilla_projecte.py). Comenta-hi, com a tot el curs, **sense accents**, què fa cada bloc (percep/decideix/actua).

```python
# El teu codi final aquí (o referència al fitxer .py entregat)
```

## 5 · Proves i resultats

| Prova | Què esperava | Què ha passat | Predicció encertada? |
|---|---|---|---|
| | | | ☐ Sí ☐ No |
| | | | ☐ Sí ☐ No |
| | | | ☐ Sí ☐ No |

> Fes com a mínim **una prova de límit** (què passa quan el sensor dona un valor extrem, o quan el polsador STOP es prem enmig d'una acció).

## 6 · Dificultats i solucions

Descriu **almenys un error real** que has tingut, seguint la rutina **DEPURA** (Descriu · Examina · Prova una hipòtesi · Ubica · Repara · Apunta):

- **Descriu:** què esperaves vs. què passava.
- **Examina:** com vas investigar (display, REPL, `print()`, mesura).
- **Prova/Ubica/Repara:** la hipòtesi que vas provar i com ho vas resoldre.

______________________________________________________________________

## 7 · Millores futures

Si tinguessis més temps o maquinari, què milloraries del teu projecte? (mínim 2 idees, coherents amb el maquinari de `09c` o amb una ampliació raonable)

1. ______________________________________________________
2. ______________________________________________________

## 8 · Conclusions

Què has après fent aquest projecte que no sabies fer abans de la SA9? Relaciona-ho amb almenys **dos blocs** diferents del curs (programació, electrònica, control, robòtica mòbil, telemetria).

______________________________________________________________________

## 9 · Reflexió ètica i ODS

- Quin **Objectiu de Desenvolupament Sostenible (ODS)** connecta amb el teu repte, i per què.
- Si el teu repte recull dades (sensors, telemetria): quina reflexió de **privadesa, consentiment o finalitat** hi apliques (com a SA8)?
- Si has fet servir un **assistent d'IA** per programar o redactar: declara **on** i **com** l'has fet servir, i explica que ets capaç d'explicar cada línia resultant (integritat acadèmica, `00_IA_a_la_materia.md`).

______________________________________________________________________

---

*Plantilla del dossier tècnic de la SA9. Alineada amb **R4** (documentació, la rúbrica que avalua el dossier) i **R5** (actitud, via el registre del procés). Es lliura tancada a la Sessió 4, abans de la defensa oral. Llicència CC BY-SA 4.0.*
