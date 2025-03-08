import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1         # Strength of the source
e = 1         # Distance between vertical lines
x0 = e / 2    # x-coordinate of the source
y0 = 0        # y-coordinate of the source

# Grid definition
x = np.linspace(0, e, 300)
y = np.linspace(-2*e, 2*e, 600)
X, Y = np.meshgrid(x, y)

# Compute theta and eta
theta = np.pi * (X - x0) / e
eta = np.pi * (Y - y0) / e

# Compute the sine of the complex argument
sin_theta_eta = np.sin(theta + 1j * eta)

# Compute Phi and Psi
Phi = (m / np.pi) * np.log(np.abs(sin_theta_eta))
Psi = (m / np.pi) * np.angle(sin_theta_eta)

# Plot streamlines (Psi = constant)
plt.figure(figsize=(10, 8))
contour_levels = np.linspace(np.min(Psi), np.max(Psi), 50)
contours = plt.contour(X, Y, Psi, levels=contour_levels, colors='blue')
plt.clabel(contours, inline=True, fontsize=8, fmt='%.2f')

# Plot equipotential lines (Phi = constant)
equipotential_levels = np.linspace(np.min(Phi), np.max(Phi), 50)
contours2 = plt.contour(X, Y, Phi, levels=equipotential_levels, colors='red', linestyles='dashed')
plt.clabel(contours2, inline=True, fontsize=8, fmt='%.2f')

# Plot boundaries
plt.axvline(x=0, color='black', linestyle='-', linewidth=2)
plt.axvline(x=e, color='black', linestyle='-', linewidth=2)

# Mark the source
plt.plot(x0, y0, 'ko', markersize=8, label='Source')

# Labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Streamlines and Equipotential Lines for a Source Between Two Vertical Lines')
plt.legend()
plt.grid(True)
plt.xlim(-10, 10)
plt.ylim(-2*e, 2*e)
plt.show()
