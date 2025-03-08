import numpy as np
import matplotlib.pyplot as plt

# PARAMETERS
delta = 0.2
e = np.sqrt(2 * delta + delta**2)
M = -1  # source strength

c1 = -1 - delta
c2 = 1 + delta

# Define the complex function f(z)
def f(z):
    z0 = e / 2
    exp_term = ((z - z0) / e) ** (M / np.pi)
    output = (exp_term + 1) / (exp_term - 1)
    return output

# Set up the grid for the complex plane
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Exclude points inside the circles centered at c1 and c2 with radius 1
mask = (np.abs(Z - c1) > 1) & (np.abs(Z - c2) > 1)

# Compute f(z) on the grid
F = f(Z)

# Apply the mask to U and V
U = np.where(mask, np.real(F), np.nan)
V = np.where(mask, np.imag(F), np.nan)

# Compute magnitude for color coding
magnitude = np.sqrt(U**2 + V**2)

plt.figure(figsize=(10, 10))

plt.quiver(X, Y, U, V, magnitude, pivot='mid', angles='xy', scale_units='xy', scale=1, cmap='viridis', width=0.002)
plt.colorbar(label='Magnitude of f(z)')

# Plotting the circles centered at c1 and c2 with radius 1
theta = np.linspace(0, 2 * np.pi, 200)
circle1_x = np.real(c1) + np.cos(theta)
circle1_y = np.imag(c1) + np.sin(theta)
circle2_x = np.real(c2) + np.cos(theta)
circle2_y = np.imag(c2) + np.sin(theta)

plt.plot(circle1_x, circle1_y, color='red')
plt.plot(circle2_x, circle2_y, color='red')


plt.xlim(x.min(), x.max())
plt.ylim(y.min(), y.max())
plt.gca().set_aspect('equal', adjustable='box')

plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.title('Vector Plot of f(z)')
plt.grid(True)
plt.show()
