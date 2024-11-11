import numpy as np

R_0 = 1.2  # fm
e = 1.602e-19
epsilon_0 = 8.854e-12

nuclei = {
    "B-11": (11, 5),
    "C-11": (11, 6),
    "O-15": (15, 8),
    "N-15": (15, 7)
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

# DeltaE_c B-11 and C-11
delta_E_B_C = abs(coulomb_energies["B-11"] - coulomb_energies["C-11"])
# DeltaE_c O-15 and N-15
delta_E_O_N = abs(coulomb_energies["O-15"] - coulomb_energies["N-15"])

print("Coulomb energies (in MeV):")
for nucleus, energy in coulomb_energies.items():
    print(f"{nucleus}: {energy:.2f} MeV")

print(f"\nDifference in Coulomb energy (ΔE_C) between B-11 and C-11: {delta_E_B_C:.2f} MeV")
print(f"Difference in Coulomb energy (ΔE_C) between O-15 and N-15: {delta_E_O_N:.2f} MeV")
