// roda_boja.scad
// Suport de la roda boja: soste una canica de 16 mm com a tercer punt de
// suport del vehicle (T2) i del rover (T3, reaprofitat sense canvis).
// Es cargola al xassis amb 2 cargols M3, a la zona "RODA BOJA" de
// Recursos/plantilles_laser/xassis_vehicle.svg.
// Material recomanat: PLA. 1 unitat per vehicle.

// --- Parametres (mm) ---
diametre_canica = 16;
marge_copa = 1.5;          // joc perque la canica giri lliure
gruix_paret = 3;
alcada_suport = 12;        // alcada total (aixeca el xassis del terra)
separacio_forats = 16;     // ha de coincidir amb els 2 forats M3 del SVG
forat_m3 = 3.4;
$fn = 48;

diametre_copa = diametre_canica + marge_copa * 2 + gruix_paret * 2;

module copa() {
    difference() {
        cylinder(h = alcada_suport, d = diametre_copa);
        // buit esferic on gira la canica
        translate([0, 0, alcada_suport - diametre_canica / 2 - 1])
            sphere(d = diametre_canica + marge_copa * 2);
        // obertura inferior: la canica sobresurt i toca a terra
        translate([0, 0, -1])
            cylinder(h = alcada_suport / 2, d = diametre_canica - 4);
    }
}

module base_fixacio() {
    translate([0, 0, alcada_suport])
        difference() {
            cylinder(h = gruix_paret, d = diametre_copa + gruix_paret * 4);
            translate([-separacio_forats / 2, 0, -1])
                cylinder(h = gruix_paret + 2, d = forat_m3);
            translate([separacio_forats / 2, 0, -1])
                cylinder(h = gruix_paret + 2, d = forat_m3);
        }
}

union() {
    copa();
    base_fixacio();
}
