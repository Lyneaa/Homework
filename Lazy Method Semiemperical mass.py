import numpy as np

#constants in MeV
a_v = 15.5
a_s = 16.8
a_c = 0.72
a_sym = 23
a_p = 34

# atom values
A = 128 # atomic mass
#Z = 1 # number of protons
#n = A - Z # number of neutrons

# mass values in u
m_n = 1.00866 
m_h = 1.00728

top = (m_n - m_h) + a_c * A ** (-1/3) + 4 * a_sym
bot = 2 * a_c * A ** (-1/3) + 8 * a_sym * A ** (-1)

Z_min = top / bot
expected_Z_min = A / 2

print(Z_min, expected_Z_min)
