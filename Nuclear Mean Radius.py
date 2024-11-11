R_0 = 1.2  # fm

nuclei = {
    "C-12": 12,
    "Na-23": 23,
    "Al-27": 27,
    "Ca-48": 48,
    "Nd-148": 148,
    "Au-197": 197,
    "Pb-208": 208
}

def calculate_radii(nuclei):
    radii = {}
    for name, A in nuclei.items():
        R = R_0 * A**(1/3)
        radii[name] = R
    return radii

radii = calculate_radii(nuclei)
for name, R in radii.items():
    print(f"{name}: Radius R = {R:.2f} fm")