import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial Parameters
delta_init = 0.2
theta1_init = 0
theta2_init = 0
n_init = 0

# Parameter Ranges
delta_min = 0
delta_max = 2

theta1_min = 0
theta1_max = 2 * np.pi

theta2_min = 0
theta2_max = 2 * np.pi

n_min = 0
n_max = 4
n_step = 1

def mobius(z, e, theta1=0, theta2=0, n=0):
    angle = theta2 - theta1
    f_z = 1j * angle + np.log(((z - e) / (z + e)) * (-1j) ** n)
    return f_z

def circle_map(c, t):
    return c + np.exp(1j * t)

tspan = np.linspace(0, 2 * np.pi, 1000)

# Create the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
plt.subplots_adjust(bottom=0.35)

# Initial Calculations
delta = delta_init
theta1 = theta1_init
theta2 = theta2_init
n = n_init

e = np.sqrt(2 * delta + delta ** 2)
c1 = -1 - delta
c2 = 1 + delta

circle1 = circle_map(c1, tspan)
circle2 = circle_map(c2, tspan)

# Plot Original Circles
line1, = axs[0].plot(circle1.real, circle1.imag, label='Circle 1')
line2, = axs[0].plot(circle2.real, circle2.imag, label='Circle 2')
axs[0].axis('equal')
axs[0].legend()
axs[0].set_title('Original Circles')

# Plot Mapped Circles
mapped_circle1 = mobius(circle1, e, theta1, theta2, n)
mapped_circle2 = mobius(circle2, e, theta1, theta2, n)

line3, = axs[1].plot(mapped_circle1.real, mapped_circle1.imag, label='Mapped Circle 1')
line4, = axs[1].plot(mapped_circle2.real, mapped_circle2.imag, label='Mapped Circle 2')
axs[1].axis('equal')
axs[1].legend()
axs[1].set_title('Mapped Circles (Annulus)')

# Create Sliders
ax_delta = plt.axes([0.15, 0.25, 0.75, 0.03])
ax_theta1 = plt.axes([0.15, 0.20, 0.75, 0.03])
ax_theta2 = plt.axes([0.15, 0.15, 0.75, 0.03])
ax_n = plt.axes([0.15, 0.10, 0.75, 0.03])

slider_delta = Slider(ax_delta, 'delta', delta_min, delta_max, valinit=delta_init)
slider_theta1 = Slider(ax_theta1, 'theta1', theta1_min, theta1_max, valinit=theta1_init)
slider_theta2 = Slider(ax_theta2, 'theta2', theta2_min, theta2_max, valinit=theta2_init)
slider_n = Slider(ax_n, 'n', n_min, n_max, valinit=n_init, valstep=n_step)

# Update Function
def update(val):
    delta = slider_delta.val
    theta1 = slider_theta1.val
    theta2 = slider_theta2.val
    n = int(slider_n.val)

    e = np.sqrt(2 * delta + delta ** 2)
    c1 = -1 - delta
    c2 = 1 + delta

    circle1 = circle_map(c1, tspan)
    circle2 = circle_map(c2, tspan)

    line1.set_xdata(circle1.real)
    line1.set_ydata(circle1.imag)
    line2.set_xdata(circle2.real)
    line2.set_ydata(circle2.imag)

    mapped_circle1 = mobius(circle1, e, theta1, theta2, n)
    mapped_circle2 = mobius(circle2, e, theta1, theta2, n)

    line3.set_xdata(mapped_circle1.real)
    line3.set_ydata(mapped_circle1.imag)
    line4.set_xdata(mapped_circle2.real)
    line4.set_ydata(mapped_circle2.imag)

    # Adjust the axes limits
    for ax in axs:
        ax.relim()
        ax.autoscale_view()

    fig.canvas.draw_idle()

# Connect Sliders to Update Function
slider_delta.on_changed(update)
slider_theta1.on_changed(update)
slider_theta2.on_changed(update)
slider_n.on_changed(update)

plt.show()
