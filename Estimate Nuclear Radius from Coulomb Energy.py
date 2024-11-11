import numpy as np

R_0 = 1.2  # fm
e = 1.602e-19
epsilon_0 = 8.854e-12

nuclei = {
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

# Function to calculate radius from Coulomb energy
def calculate_radius_from_energy(Z, E_C):
    E_C_Joules = E_C * 1.602e-13 # Joules to MeV
    R = (3 / 5) * (Z**2 * e**2) / (4 * np.pi * epsilon_0 * E_C_Joules)
    R_fm = R * 1e15 # meters to femtometers (fm)
    return R_fm

# radius from Coulomb energy
R_O_from_energy = calculate_radius_from_energy(8, coulomb_energies["O-15"])
R_N_from_energy = calculate_radius_from_energy(7, coulomb_energies["N-15"])

print(f"\nCalculated radius for O-15 from Coulomb energy: {R_O_from_energy:.2f} fm")
print(f"Calculated radius for N-15 from Coulomb energy: {R_N_from_energy:.2f} fm")
