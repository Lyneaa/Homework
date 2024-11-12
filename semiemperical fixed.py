def semi_empirical_mass(A, Z):
    # Constants
    a_v = 15.5  # MeV
    a_s = 16.8   # MeV
    a_c = 0.72  # MeV
    a_a = 23   # MeV
    a_p = 34  # MeV

    # amu (u)
    m_n = 1.00866  # mass of neutron
    m_h = 1.00728  # mass of hydrogen
    N = A - Z
    
    # pairing term
    if A % 2 == 1:
        delta = 0  # odd A
    elif Z % 2 == 0:
        delta = +a_p / (A ** 0.5)  # even Z and even N
    else:
        delta = -a_p / (A ** 0.5)  # odd Z and odd N
    
    # Binding energy
    binding_energy = (
        a_v * A
        - a_s * A ** (2 / 3)
        - a_c * Z * (Z - 1) / A ** (1 / 3)
        - a_a * ((A - 2 * Z) ** 2) / A
        + delta
    )
    
    # Mass 
    mass = Z * m_h + N * m_n - binding_energy / 931.502  # amu (u)
    
    return binding_energy, mass

Z_A3 = 2   # Z values
Z_A90 = 42 # Same change Z values

# For A = 3
binding_energy_3, mass_3 = semi_empirical_mass(3, Z_A3)
print(f"A = 3, Z = {Z_A3}: Binding Energy = {binding_energy_3:.2f} MeV, Mass = {mass_3:.5f} u")

# For A = 90
binding_energy_90, mass_90 = semi_empirical_mass(90, Z_A90)
print(f"A = 90, Z = {Z_A90}: Binding Energy = {binding_energy_90:.2f} MeV, Mass = {mass_90:.5f} u")
