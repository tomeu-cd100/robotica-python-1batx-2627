// suport_motor.scad
// Suport d'un motoreductor TT groc estandard (Kit 2) al xassis del vehicle
// (T2, reaprofitat sense canvis al rover T3). Encaixa a la ranura de brida
// del lateral del xassis ("MOTOR ESQUERRE"/"MOTOR DRET" de
// Recursos/plantilles_laser/xassis_vehicle.svg) i abraca el cos rodo del
// motor amb una sella semicircular subjectada amb una brida.
// Material recomanat: PLA. 2 unitats per vehicle (esquerre + dret).

// --- Parametres (mm) ---
diametre_motor = 22;      // diametre del cos rodo del motoreductor TT
gruix_sella = 4;
alcada_sella = 16;        // alcada de la paret que abraca el motor
amplada_sella = 20;       // amplada de la sella (llargada del motor coberta)
tab_amplada = 8;          // ha de coincidir amb la ranura de brida del xassis
tab_fondaria = 10;
gruix_tab = 3;
diametre_forat_brida = 3;  // forat per passar la brida de subjeccio
$fn = 40;

module sella() {
    difference() {
        // paret amb un buit semicircular on reposa el motor
        translate([0, 0, gruix_sella / 2])
            cube([amplada_sella, diametre_motor + gruix_sella * 2, alcada_sella],
                 center = true);
        translate([0, 0, alcada_sella / 2 + gruix_sella / 2 - diametre_motor / 2])
            rotate([90, 0, 0])
                cylinder(h = amplada_sella + 2, d = diametre_motor, center = true);
        // 2 forats per a la brida de subjeccio, per damunt del motor
        translate([-amplada_sella / 2 - 1, 0, alcada_sella - 3])
            rotate([0, 90, 0])
                cylinder(h = amplada_sella + 2, d = diametre_forat_brida);
    }
}

module tab_xassis() {
    // s'insereix a la ranura de brida del xassis (8 x 10 mm)
    translate([0, -(diametre_motor / 2 + gruix_sella + tab_fondaria / 2), 0])
        cube([tab_amplada, tab_fondaria, gruix_tab], center = true);
}

union() {
    sella();
    tab_xassis();
}
