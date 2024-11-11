import matplotlib.pyplot as plt
import numpy as np

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
        R = R_0 * A **(1/3)
        radii[name] = R
    return radii

radii = calculate_radii(nuclei)
for name, R in radii.items():
    print(f"{name}: Radius R = {R:.2f} fm")

# Need to make list for plotting
A = np.array(list(nuclei.values()))
R = np.array(list(radii.values()))

x = A ** (1/3)
y = R * np.sqrt(3/5)

plt.plot(x, y, 'bo-', label = r'$\sqrt{\langle r^2 \rangle}$')
plt.xlabel(r'$A^{1/3}$')
plt.ylabel(r'$\sqrt{\langle r^2 \rangle}$ (fm)')
plt.title(r'Root Mean Square Radius $\sqrt{\langle r^2 \rangle}$ vs $A^{1/3}$')
plt.grid(True)
for (name, A), x, y in zip(nuclei.items(), x, y):
    plt.text(x, y, name, fontsize=9, ha='right', va='bottom')
plt.show()