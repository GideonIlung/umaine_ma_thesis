import numpy as np
import matplotlib.pyplot as plt

# Parameter
e = 1  # set your value of e here

# Define the computational domain: x from -e to e
x_min, x_max = -e, e
y_min, y_max = -2*e, 2*e
num_points = 300

x = np.linspace(x_min, x_max, num_points)
y = np.linspace(y_min, y_max, num_points)
X, Y = np.meshgrid(x, y)
Z = X + 1j*Y

# Compute f(z) = (pi/e)*cot((pi*z)/e)
factor = (np.pi / e)
f = factor * (np.cos(factor * Z) / np.sin(factor * Z))

# Real part: Phi, Imag part: Psi
Phi = np.real(f)
Psi = np.imag(f)

plt.figure(figsize=(10, 8))

# Plot streamlines (Psi = constant)
contour_levels_psi = np.linspace(np.min(Psi), np.max(Psi), 50)
contours_psi = plt.contour(X, Y, Psi, levels=contour_levels_psi, colors='blue')
plt.clabel(contours_psi, inline=True, fontsize=8, fmt='%.2f')

# Plot equipotential lines (Phi = constant)
contour_levels_phi = np.linspace(np.min(Phi), np.max(Phi), 50)
contours_phi = plt.contour(X, Y, Phi, levels=contour_levels_phi, colors='red', linestyles='dashed')
plt.clabel(contours_phi, inline=True, fontsize=8, fmt='%.2f')

# Plot boundaries at x = -e and x = e
plt.axvline(x=-e, color='black', linestyle='-', linewidth=2)
plt.axvline(x=e, color='black', linestyle='-', linewidth=2)

plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Streamlines and Equipotential Lines for $f(z)=\frac{\pi}{e}\cot\left(\frac{\pi z}{e}\right)$')
plt.grid(True)
plt.show()
