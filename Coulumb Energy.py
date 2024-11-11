import numpy as np

R_0 = 1.2  # fm
e = 1.602e-19
epsilon_0 = 8.854e-12

nuclei = {
    "C-12": (12, 6),
    "Na-23": (23, 11),
    "Al-27": (27, 13),
    "Ca-48": (48, 20),
    "Nd-148": (148, 60),
    "Au-197": (197, 79),
    "Pb-208": (208, 82)
}

def calculate_radii(nuclei):
    radii = {}
    for name, (A, _) in nuclei.items():
        R = R_0 * A**(1/3)
        radii[name] = R
    return radii

radii = calculate_radii(nuclei)
for name, R in radii.items():
    print(f"{name}: Radius R = {R:.2f} fm")

def calculate_coulomb_energy(nuclei, radii):
    coulomb_energies = {}
    for name, (A, Z) in nuclei.items():
        R = radii[name] * 1e-15  # Convert radius from fm to meters
        E_C = (3 / 5) * (Z**2 * e**2) / (4 * np.pi * epsilon_0 * R)  # Coulomb energy in Joules
        E_C_MeV = E_C / (1.602e-13)  # Convert Joules to MeV
        coulomb_energies[name] = E_C_MeV
    return coulomb_energies

radii = calculate_radii(nuclei)
coulomb_energies = calculate_coulomb_energy(nuclei, radii)

for name in nuclei:
    print(f"{name}:")
    print(f"  Radius R = {radii[name]:.2f} fm")
    print(f"  Coulomb Energy E_C = {coulomb_energies[name]:.2f} MeV")
