// suport_electronica.scad
// Safata/suport central que aixeca la micro:bit + Micro:shield sobre el
// xassis del vehicle (T2, reaprofitat sense canvis al rover T3), deixant
// pas de cables per sota. Els 4 forats coincideixen amb els 4 forats M3
// centrals ("MICRO:BIT + MICRO:SHIELD") del xassis de 190x140 mm de
// Recursos/plantilles_laser/xassis_vehicle.svg (separacio 40 x 30 mm).
// Material recomanat: PLA. 1 unitat per vehicle.

// --- Parametres (mm) ---
amplada_safata = 56;        // cobreix la micro:bit + Micro:shield (43 x 52 mm) amb marge
fondaria_safata = 46;
gruix_safata = 3;
alcada_potes = 6;           // aixeca la placa per deixar pas de cables per sota
diametre_pota = 8;
separacio_forats_x = 40;    // ha de coincidir amb el xassis
separacio_forats_y = 30;    // ha de coincidir amb el xassis
forat_m3 = 3.4;
$fn = 32;

module safata() {
    difference() {
        cube([amplada_safata, fondaria_safata, gruix_safata], center = true);
        for (x = [-separacio_forats_x / 2, separacio_forats_x / 2])
            for (y = [-separacio_forats_y / 2, separacio_forats_y / 2])
                translate([x, y, -1])
                    cylinder(h = gruix_safata + 2, d = forat_m3);
    }
}

module pota(x, y) {
    translate([x, y, -alcada_potes])
        difference() {
            cylinder(h = alcada_potes, d = diametre_pota);
            translate([0, 0, -1])
                cylinder(h = alcada_potes + 2, d = forat_m3);
        }
}

union() {
    safata();
    for (x = [-separacio_forats_x / 2, separacio_forats_x / 2])
        for (y = [-separacio_forats_y / 2, separacio_forats_y / 2])
            pota(x, y);
}
