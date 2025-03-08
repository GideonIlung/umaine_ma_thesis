import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
from matplotlib.widgets import Slider
import warnings

# Suppress warnings for invalid operations in sqrt
warnings.filterwarnings('ignore', category=RuntimeWarning)

def compute_hue_plot(theta1, theta2, e=0.6, n=0):
    # Define the range and resolution
    x = np.linspace(-2, 2, 500)
    y = np.linspace(-2, 2, 500)
    X, Y = np.meshgrid(x, y)
    z = X + 1j*Y

    # Compute f(z)
    angle = theta2 - theta1
    f_z = 1j*(angle) + np.log(((z - e)/(z + e)) * (-1j)**(n))

    # Compute magnitude and phase
    magnitude = np.abs(f_z)
    phase = np.angle(f_z)

    # Map phase to hue (0 to 1)
    hue = (phase + np.pi) / (2 * np.pi)
    # Normalize magnitude for brightness (value)
    value = magnitude / np.nanmax(magnitude)
    value = np.clip(value, 0, 1)
    saturation = np.ones_like(hue)

    # Combine to get HSV image
    hsv = np.stack((hue, saturation, value), axis=-1)
    rgb = hsv_to_rgb(hsv)

    return rgb

# Initial values
theta1_init = 0.0
theta2_init = 0.0
e_init = 0.6
n_init = 0

# Compute initial hue plot
rgb = compute_hue_plot(theta1_init, theta2_init, e_init, n_init)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.25, bottom=0.35)

# Display the image
x = np.linspace(-2, 2, 500)
y = np.linspace(-2, 2, 500)
im = ax.imshow(rgb, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower')
ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')
title = ax.set_title(f'Hue plot of f(z) with θ₁={theta1_init:.2f}, θ₂={theta2_init:.2f}, e={e_init:.2f}, n={n_init}')

# Define the axes for the sliders
axcolor = 'lightgoldenrodyellow'
ax_theta1 = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
ax_theta2 = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_n = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

# Create the sliders
theta1_slider = Slider(ax_theta1, 'θ₁', 0, 2*np.pi, valinit=theta1_init)
theta2_slider = Slider(ax_theta2, 'θ₂', 0, 2*np.pi, valinit=theta2_init)
e_slider = Slider(ax_e, 'e', 0, 1, valinit=e_init)
n_slider = Slider(ax_n, 'n', 0, 4, valinit=n_init, valstep=1)

# Update function
def update(val):
    theta1 = theta1_slider.val
    theta2 = theta2_slider.val
    e = e_slider.val
    n = n_slider.val
    n = int(n)  # Ensure n is integer
    rgb = compute_hue_plot(theta1, theta2, e, n)
    im.set_data(rgb)
    title.set_text(f'Hue plot of f(z) with θ₁={theta1:.2f}, θ₂={theta2:.2f}, e={e:.2f}, n={n}')
    fig.canvas.draw_idle()

# Connect the update function to sliders
theta1_slider.on_changed(update)
theta2_slider.on_changed(update)
e_slider.on_changed(update)
n_slider.on_changed(update)

plt.show()
