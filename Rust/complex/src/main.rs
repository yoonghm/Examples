use num::complex::Complex;
use std::f64::consts::PI;

fn main() {
    let z1 = Complex { re: 1.0, im: 2.0 };
    let z2 = Complex::new(3.0, 4.0);

    println!("{}", z1 + z2);

    let polar_form = format!("{:.2} * cis({:.2})", 
        z1.norm(), z1.arg() * 180.0 / PI);
    println!("z in polar form: {}", polar_form);
}
