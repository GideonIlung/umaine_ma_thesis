import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb  # Import the correct function

# PARAMETERS
delta = 0.2
e = np.sqrt(2 * delta + delta**2)
M = 1  # source strength

c1 = -1 - delta
c2 = 1 + delta

# Define the complex function f(z)
def f(z):
    z0 = e / 2
    exp_term = ((z - z0) / e) ** (M / np.pi)
    output = (exp_term + 1) / (exp_term - 1)
    return output

# Set up the grid for the complex plane
x = np.linspace(-10, 10, 800)  # Real part range
y = np.linspace(-10, 10, 800)  # Imaginary part range
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Exclude points inside the circles centered at c1 and c2 with radius 1
mask = (np.abs(Z - c1) > 1) & (np.abs(Z - c2) > 1)
Z_masked = np.where(mask, Z, np.nan + 1j * np.nan)

# Compute f(z) on the grid
F = f(Z_masked)

# Compute hue (argument/phase) and magnitude
hue = np.angle(F)  # Argument of f(z)
magnitude = np.abs(F)  # Magnitude of f(z)

# Normalize magnitude for better visualization
magnitude = np.log1p(magnitude)

# Create a hue plot using HSV colormap
hsv = np.zeros((*hue.shape, 3))
hsv[..., 0] = (hue + np.pi) / (2 * np.pi)  # Normalize hue to [0, 1]
hsv[..., 1] = 1  # Full saturation
hsv[..., 2] = magnitude / np.nanmax(magnitude)  # Normalize brightness

# Convert HSV to RGB using the correct function
rgb = hsv_to_rgb(hsv)

# Plot the hue plot
plt.figure(figsize=(10, 10))
plt.imshow(rgb, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', zorder=2)

# Function to plot lines excluding the regions inside the circles
def plot_masked_line(xdata, ydata, mask_line, **kwargs):
    xdata = np.asarray(xdata)
    ydata = np.asarray(ydata)
    xdata = xdata[mask_line]
    ydata = ydata[mask_line]
    plt.plot(xdata, ydata, **kwargs)

# Plot the x=0 and y=0 lines excluding the circles
# Horizontal line y=0
mask_x0 = mask[int(len(y)//2), :]
plot_masked_line(x, np.zeros_like(x), mask_x0, color='black', linewidth=0.5, linestyle='--', zorder=1)
# Vertical line x=0
mask_y0 = mask[:, int(len(x)//2)]
plot_masked_line(np.zeros_like(y), y, mask_y0, color='black', linewidth=0.5, linestyle='--', zorder=1)

# Set the grid, excluding regions inside the circles
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5, zorder=0)
plt.title('Hue Plot of f(z)')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.colorbar(plt.cm.ScalarMappable(cmap='hsv'), label='Arg(f(z)) (radians)')
plt.show()
