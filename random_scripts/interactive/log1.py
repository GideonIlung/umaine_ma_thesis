import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
from matplotlib.widgets import Slider
import warnings

# Suppress warnings for invalid operations in sqrt
warnings.filterwarnings('ignore', category=RuntimeWarning)

def compute_hue_plot(theta1, theta2,n1=0,n2=0):
    # Define the range and resolution
    x = np.linspace(-2, 2, 500)
    y = np.linspace(-2, 2, 500)
    X, Y = np.meshgrid(x, y)
    z = X + 1j*Y

    # Compute f(z)
    #exponent = 1j * 0.5 * (theta1 + theta2)
    #f_z = np.exp(exponent) * np.sqrt(z**2 -1)

    angle = theta2-theta1
    f_z = 1j*(angle) + np.log(((z-1)/(z+1))*(-1j)**(n1-n2))

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

# Initial theta values
theta1_init = 0.0
theta2_init = 0.0

# Compute initial hue plot
rgb = compute_hue_plot(theta1_init, theta2_init)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.25, bottom=0.25)

# Display the image
x = np.linspace(-2, 2, 500)
y = np.linspace(-2, 2, 500)
im = ax.imshow(rgb, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower')
ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')
title = ax.set_title(f'Hue plot of f(z) with θ₁={theta1_init:.2f}, θ₂={theta2_init:.2f}')

# Define the axes for the sliders
axcolor = 'lightgoldenrodyellow'
ax_theta1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_theta2 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

# Create the sliders
theta1_slider = Slider(ax_theta1, 'θ₁', 0, 2*np.pi, valinit=theta1_init)
theta2_slider = Slider(ax_theta2, 'θ₂', 0, 2*np.pi, valinit=theta2_init)

# Update function
def update(val):
    theta1 = theta1_slider.val
    theta2 = theta2_slider.val
    rgb = compute_hue_plot(theta1, theta2)
    im.set_data(rgb)
    title.set_text(f'Hue plot of f(z) with θ₁={theta1:.2f}, θ₂={theta2:.2f}')
    fig.canvas.draw_idle()

# Connect the update function to sliders
theta1_slider.on_changed(update)
theta2_slider.on_changed(update)

plt.show()
