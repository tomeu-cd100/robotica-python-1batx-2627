// suport_hcsr04.scad
// Suport frontal del sensor d'ultrasons HC-SR04 per al rover (T3), cargolat
// al davant del xassis del vehicle ja muntat (Sessio 0, vegeu
// Classes/00_General/00_Projecte_T3_Rover.md). Peca nova, petita: NO hi ha
// plantilla laser (vegeu Recursos/plantilles_laser/README.md).
// Material recomanat: PLA. 1 unitat per rover.

// --- Parametres (mm) ---
// Placa del sensor HC-SR04: 45 x 20 mm (mida real del modul).
amplada_sensor = 45;
alcada_sensor = 20;
gruix_placa = 3;
marge = 3;                     // vora al voltant del sensor
separacio_forats_sensor = 41;  // distancia entre els 2 forats de muntatge del modul (estandard HC-SR04)
diametre_ulls = 16.5;          // diametre de cada "ull" (transductor) del sensor
separacio_ulls = 26;           // distancia entre centres dels 2 ulls
forat_m3 = 3.4;                // forats per cargolar el suport al xassis
separacio_forats_xassis = 30;  // coincideix amb els forats "SUPORT HC-SR04" previstos al xassis
$fn = 32;

module placa_suport() {
    difference() {
        cube([amplada_sensor + marge * 2, alcada_sensor + marge * 2, gruix_placa],
             center = true);
        // finestra pels 2 ulls del sensor
        translate([-separacio_ulls / 2, 0, -1])
            cylinder(h = gruix_placa + 2, d = diametre_ulls);
        translate([separacio_ulls / 2, 0, -1])
            cylinder(h = gruix_placa + 2, d = diametre_ulls);
        // forats de muntatge del modul HC-SR04
        translate([-separacio_forats_sensor / 2, alcada_sensor / 2 - 2, -1])
            cylinder(h = gruix_placa + 2, d = 2.2);
        translate([separacio_forats_sensor / 2, alcada_sensor / 2 - 2, -1])
            cylinder(h = gruix_placa + 2, d = 2.2);
        // forats M3 per fixar el suport al xassis
        translate([-separacio_forats_xassis / 2, -(alcada_sensor / 2 + marge - 3), -1])
            cylinder(h = gruix_placa + 2, d = forat_m3);
        translate([separacio_forats_xassis / 2, -(alcada_sensor / 2 + marge - 3), -1])
            cylinder(h = gruix_placa + 2, d = forat_m3);
    }
}

placa_suport();
