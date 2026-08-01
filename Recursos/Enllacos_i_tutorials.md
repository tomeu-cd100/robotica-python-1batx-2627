# Enllaços i tutorials — recursos externs validats

> **Per a qui és?** Docent (i, en 3 casos marcats, també alumnat). Deu
> recursos externs **verificats el juliol de 2026**: què són, quina
> llicència tenen i **quan** usar-los dins la seqüència del curs. Cap
> d'aquests enllaços és obligatori per seguir el curs (tot el material
> propi és autosuficient a `Classes/` i `Reptes/`): són **ampliació,
> referència i pla B**.

> ⚠️ **Els enllaços externs poden canviar.** Verificats el juliol del 2026;
> si algun deixa de funcionar, cerca el títol al motor de cerca del lloc
> d'origen (sol mantenir-se, només canvia la URL exacta).

## Taula resum

| Recurs | URL | Llicència | Ús recomanat |
|---|---|---|---|
| First lessons with Python | <https://microbit.org/teach/lessons/> | © Micro:bit Educational Foundation, ús educatiu gratuït | SA1-SA2, primer contacte amb l'editor i la sintaxi |
| Docs oficials MicroPython micro:bit | <https://microbit-micropython.readthedocs.io/> | MIT (codi) / CC BY-SA (docs) | Referència permanent de l'API (`display`, `music`, `radio`...) |
| Editor + simulador oficial | <https://python.microbit.org/> | © Micro:bit Educational Foundation, ús gratuït | Eina principal del curs (SA1-SA9); vegeu `Simulacions/Simulador_microbit.md` |
| INTEF «Programando la micro:bit con Python» | Aula En Abierto (INTEF) + PDF de projectes | CC BY-NC-SA (INTEF) | Alumnat: exercicis addicionals en castellà (opcional) |
| XTEC Pensament computacional Python batxillerat | <https://projectes.xtec.cat/pensament-computacional/inici/programacio/pagina-inicial-python-25-26/> | © Generalitat de Catalunya, ús educatiu | Referència curricular Catalunya (contrast amb la programació pròpia) |
| Wiki Keyestudio Micro:shield i kits 37-in-1 | <https://wiki.keyestudio.com/> (cerca «Micro:bit Micro:shield Ks0360» i «37 in 1 Sensor kit») | © Keyestudio, documentació pública del fabricant | Esquemes i datasheets dels sensors/mòduls del kit del centre |
| awesome-microbit | <https://github.com/carlosperate/awesome-microbit> | CC0 (domini públic) | Directori de recursos micro:bit per explorar ampliacions |
| Teach Computing KS4 Physical Computing Project | National Centre for Computing Education (Regne Unit), registre gratuït | © NCCE, ús educatiu (registre) | Model de projecte «buggy + rúbrica» com a referència per a T2/T3 i SA9 |
| Get Started with MicroPython on Pico | PDF (Raspberry Pi Foundation), mirall a mclibre.org | CC BY-SA (Raspberry Pi Foundation) | **Només per a l'opció Pico** (ampliació fora del maquinari nucli) |
| Real Python «Arduino With Python» (pyFirmata) | <https://realpython.com/arduino-python/> | © Real Python, alguns continguts d'accés gratuït | **Només per a l'ampliació pyFirmata** (control des de l'ordinador) |

## Detall per recurs

### 1. First lessons with Python (micro:bit Educational Foundation)
- **URL:** <https://microbit.org/teach/lessons/>
- **Llicència:** contingut de la Micro:bit Educational Foundation, d'ús
  educatiu gratuït (consulta les condicions d'ús de cada lliçó al lloc).
- **Ús recomanat:** lliçons introductòries oficials, pensades per a un
  primer contacte amb Python a la micro:bit. Útils com a **suport per a
  SA1-SA2** (vocabulari i primeres sortides digitals/PWM) si algun alumne
  necessita repassar fora de classe amb un material diferent del propi.

### 2. Documentació oficial de MicroPython per a micro:bit
- **URL:** <https://microbit-micropython.readthedocs.io/>
- **Llicència:** codi font MIT; documentació generalment CC BY-SA (vegeu
  peu de pàgina del lloc per a la versió vigent).
- **Ús recomanat:** **referència d'API permanent** per al docent i per a
  l'alumnat avançat: la font primària de `display`, `Image`, `button_a`/
  `button_b`, `pin0`-`pin20`, `music`, `radio`, `accelerometer`,
  `microphone`, `log`, `speech`, etc. La xuleta pròpia del curs
  (`Referencia_MicroPython_microbit.md`) és un resum **només de l'API
  usada al curs**; per a qualsevol altra funció, aquesta és la font.

### 3. Editor i simulador oficial — python.microbit.org
- **URL:** <https://python.microbit.org/>
- **Llicència:** © Micro:bit Educational Foundation, ús gratuït al
  navegador, sense compte ni instal·lació.
- **Ús recomanat:** és **l'eina principal de tot el curs**
  (`Classes/00_General/00_Entorns_de_treball.md` §1). Simula la matriu de
  LED, els botons A/B, alguns sensors interns i la ràdio (entre dues
  pestanyes); **no simula maquinari extern** (Micro:shield, sensors del
  Kit, motors). Detall exacte del que simula i no simula, i el seu ús per
  SA, a [`../Simulacions/Simulador_microbit.md`](../Simulacions/Simulador_microbit.md).

### 4. INTEF — «Programando la micro:bit con Python» (Aula En Abierto)
- **URL:** cerca del curs a Aula En Abierto (INTEF); PDF de projectes:
  <https://intef.es/wp-content/uploads/2021/11/Microbit-1.pdf>
- **Llicència:** materials de l'INTEF, generalment **CC BY-NC-SA**
  (comprova la llicència concreta indicada a cada document).
- **Ús recomanat:** material **en castellà**, pensat per a **alumnat** que
  vulgui exercicis addicionals amb un altre enfocament didàctic. No
  substitueix cap material propi (que és en català); es recomana com a
  **ampliació opcional**, especialment el PDF de projectes per a idees de
  repte lliure a SA9.

### 5. XTEC — Pensament computacional, Python a batxillerat
- **URL:** <https://projectes.xtec.cat/pensament-computacional/inici/programacio/pagina-inicial-python-25-26/>
- **Llicència:** © Generalitat de Catalunya (Departament d'Educació), ús
  educatiu.
- **Ús recomanat:** **referència curricular** per contrastar la
  seqüenciació i els sabers de Python de 1r de Batxillerat a Catalunya amb
  la programació pròpia del curs (`Programació didàctica/`). Útil per al
  docent en la justificació curricular davant de coordinació o inspecció.

### 6. Wiki Keyestudio — Micro:shield Ks0360 i kits 37-in-1
- **URL:** <https://wiki.keyestudio.com/> (cerca «Ks0360», el Micro:shield,
  i «37 in 1 Sensor kit for Beginner»/kit equivalent del centre).
- **Llicència:** documentació pública del fabricant (© Keyestudio), lliure
  consulta.
- **Ús recomanat:** **esquemes i datasheets** del maquinari real del
  centre: distribució de pins del Micro:shield, especificacions dels
  sensors/actuadors dels Kits 1-3. Font de contrast quan un esquema propi
  (`SAx_esquemes_connexions.md`) necessita verificar-se contra el
  fabricant.

### 7. awesome-microbit
- **URL:** <https://github.com/carlosperate/awesome-microbit>
- **Llicència:** **CC0** (domini públic / sense restriccions).
- **Ús recomanat:** directori curat d'eines, biblioteques, projectes i
  tutorials de micro:bit. Punt de partida per al docent quan vol explorar
  ampliacions fora del temari (per exemple, idees per al repte lliure
  individual de SA9) sense haver de cercar des de zero.

### 8. Teach Computing — KS4 Physical Computing Project
- **Origen:** National Centre for Computing Education (NCCE, Regne Unit),
  **registre gratuït** necessari per accedir al material complet.
- **Llicència:** © NCCE, ús educatiu amb registre.
- **Ús recomanat:** **model de projecte** (un «buggy» robòtic amb rúbrica
  d'avaluació) estructuralment semblant al fil conductor T2-T3 d'aquest
  curs. Útil com a referència de disseny de rúbrica i de seqüenciació d'un
  projecte de robòtica mòbil, no com a material a traduir directament (el
  maquinari i el llenguatge hi difereixen).

### 9. Get Started with MicroPython on Pico (Raspberry Pi Foundation)
- **Format:** PDF, amb mirall a mclibre.org.
- **Llicència:** **CC BY-SA** (Raspberry Pi Foundation).
- **Ús recomanat:** **només per a l'opció Pico**, és a dir, si algun grup o
  alumne treballa amb Raspberry Pi Pico enlloc de (o a més de) la
  micro:bit. No forma part del maquinari nucli del curs
  (`CLAUDE.md`: «Maquinari nucli: micro:bit V2 + Micro:shield»). Vegeu
  també [`../Simulacions/Wokwi_opcional.md`](../Simulacions/Wokwi_opcional.md)
  per a la simulació d'aquesta opció.

### 10. Real Python — «Arduino With Python» (pyFirmata)
- **URL:** <https://realpython.com/arduino-python/>
- **Llicència:** © Real Python; part del contingut és d'accés lliure, part
  requereix subscripció.
- **Ús recomanat:** **només per a l'ampliació pyFirmata**, és a dir, si
  s'explora el control d'una placa des de Python executat a l'ordinador
  (enlloc del codi MicroPython embegut a la placa). És una ampliació
  optativa i puntual, no forma part de la seqüència obligatòria de cap SA.

---

⬅️ Torna a [`00_LLEGEIX-ME_Recursos.md`](00_LLEGEIX-ME_Recursos.md).
