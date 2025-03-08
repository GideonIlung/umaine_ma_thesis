import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_riemann_surface(branch_cut_angle=0, n_branches=5):
    # Configuration
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    theta = np.linspace(0, 2 * np.pi, 100)
    r = np.linspace(0.1, 1, 50)
    theta, r = np.meshgrid(theta, r)
    x, y = r * np.cos(theta), r * np.sin(theta)

    # Colors
    colors = [plt.cm.viridis((i / n_branches)) for i in range(n_branches)]

    for k in range(n_branches):
        z = np.log(np.abs(r)) + 1j * (theta + 2 * np.pi * k)
        z_real = np.real(z)

        if k == 0:
            # Principal branch in full color
            color_array = np.tile(colors[k], (x.shape[0], x.shape[1], 1))
        else:
            # Grey out other branches
            color_array = np.full((x.shape[0], x.shape[1], 4), (0.5, 0.5, 0.5, 0.5))  # RGBA for grey

        ax.plot_surface(x, y, z_real, facecolors=color_array, rstride=1, cstride=1, alpha=0.9)

    # Branch cut
    ax.plot(np.cos(branch_cut_angle) * r.flatten(),
            np.sin(branch_cut_angle) * r.flatten(),
            np.log(r.flatten()), color='red', linewidth=2)

    # Labels and title
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_zlabel('Log modulus')
    ax.set_title('Riemann Surface of the Complex Logarithm with a Branch Cut')

    plt.show()

# Example usage
plot_riemann_surface(branch_cut_angle=np.pi / 2)  # Branch cut along the positive imaginary axis
