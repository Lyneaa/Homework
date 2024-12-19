import numpy as np
import matplotlib.pyplot as plt

# Data for material and setup
material_thickness = 0.1  # Thickness 
beam_intensity_initial = 1.0  # Initial intensity 
linear_attenuation_coefficient = 50  # Linear attenuation coefficient  
distance_steps = np.linspace(0, material_thickness, 500) 

# Calculate radiation intensity 
# I(x) = I_0 * exp(-mu * x)
radiation_intensity = beam_intensity_initial * np.exp(-linear_attenuation_coefficient * distance_steps)

plt.figure(figsize=(8, 6))
plt.plot(distance_steps, radiation_intensity, label="Radiation Intensity")
plt.xlabel("Depth in Material (m)")
plt.ylabel("Radiation Intensity (arbitrary units)")
plt.title("Radiation Attenuation through Material")
plt.grid()
plt.legend()
plt.show()

print("--- Radiation Attenuation Properties ---")
print(f"Initial Radiation Intensity: {beam_intensity_initial}")
print(f"Material Thickness: {material_thickness} m")
print(f"Linear Attenuation Coefficient: {linear_attenuation_coefficient} 1/m")
print(f"Final Radiation Intensity after {material_thickness} m: {radiation_intensity[-1]:.4f}")
