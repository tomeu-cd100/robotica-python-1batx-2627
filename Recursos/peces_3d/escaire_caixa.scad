// escaire_caixa.scad
// Escaire d'angle per unir, sense encolar, dues plaques de DM de 3 mm en
// angle recte (caixa de la mascota T1: base + 4 laterals + tapa). Cada ala
// te un forat M3 que coincideix amb els forats de cantonada de
// Recursos/plantilles_laser/mascota.svg (a 8 mm del caire, funcio
// "_forats_escaire" del generador).
// Material recomanat: PLA. 8 unitats per mascota (6 caixa + 2 tapa).

// --- Parametres (mm) ---
llargada_ala = 18;    // llargada de cada ala: cobreix el forat a 8 mm del caire
amplada_ala = 10;     // amplada de l'escaire
gruix_peca = 4;       // gruix del material imprès
forat_m3 = 3.4;       // diametre del forat (M3 amb marge d'impressio)
vora_forat = 8;        // distancia del centre del forat al caire (com el SVG)
$fn = 32;

module ala_plana() {
    cube([llargada_ala, amplada_ala, gruix_peca]);
}

module ala_vertical() {
    cube([gruix_peca, amplada_ala, llargada_ala]);
}

module forat_vertical(x) {
    translate([x, amplada_ala / 2, -1])
        cylinder(h = gruix_peca + 2, d = forat_m3);
}

module forat_horitzontal(z) {
    translate([-1, amplada_ala / 2, z])
        rotate([0, 90, 0])
            cylinder(h = gruix_peca + 2, d = forat_m3);
}

module escaire_caixa() {
    difference() {
        union() {
            ala_plana();      // reposa sobre la base/lateral 1 (pla XY)
            ala_vertical();   // s'apuja contra el lateral 2 (pla YZ)
        }
        forat_vertical(vora_forat);
        forat_horitzontal(vora_forat);
    }
}

escaire_caixa();
