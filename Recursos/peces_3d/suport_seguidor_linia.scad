// suport_seguidor_linia.scad
// Suport del seguidor de linia KS0050 per al rover (T3), enganxat/cargolat
// sota el xassis del vehicle ja muntat, amb el sensor mirant a terra
// (Sessio 0, vegeu Classes/00_General/00_Projecte_T3_Rover.md). Peca nova,
// petita: NO hi ha plantilla laser (vegeu
// Recursos/plantilles_laser/README.md).
// Material recomanat: PLA. 1 unitat per rover.

// --- Parametres (mm) ---
// Modul KS0050 (seguidor de linia IR, 1 canal): placa aprox. 32 x 14 mm.
amplada_sensor = 32;
fondaria_sensor = 14;
gruix_placa = 3;
marge = 3;
alcada_potes = 15;             // distancia del sensor al terra (mirant avall)
diametre_ull = 6;              // finestra pel LED/fotodiode emissor+receptor
separacio_forats_sensor = 26;  // distancia entre forats de muntatge del modul
forat_m3 = 3.4;                // forats per fixar el suport al xassis
separacio_forats_xassis = 20;
$fn = 32;

module placa_sensor() {
    difference() {
        cube([amplada_sensor + marge * 2, fondaria_sensor + marge * 2, gruix_placa],
             center = true);
        // finestra de visio del sensor cap a terra
        translate([0, 0, -1])
            cylinder(h = gruix_placa + 2, d = diametre_ull);
        // forats de muntatge del modul KS0050
        translate([-separacio_forats_sensor / 2, 0, -1])
            cylinder(h = gruix_placa + 2, d = 2.2);
        translate([separacio_forats_sensor / 2, 0, -1])
            cylinder(h = gruix_placa + 2, d = 2.2);
    }
}

module pota(x) {
    translate([x, 0, 0])
        difference() {
            cylinder(h = alcada_potes, d = 8);
            translate([0, 0, -1])
                cylinder(h = alcada_potes + 2, d = forat_m3);
        }
}

union() {
    translate([0, 0, alcada_potes])
        placa_sensor();
    pota(-separacio_forats_xassis / 2);
    pota(separacio_forats_xassis / 2);
}
