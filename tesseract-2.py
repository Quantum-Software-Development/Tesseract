import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters for the torus
R = 1  # Major radius
r = 0.4  # Minor radius

# Create a mesh grid for the angles
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Parametric equations for the torus
X = (R + r * np.cos(theta)) * np.cos(phi)
Y = (R + r * np.cos(theta)) * np.sin(phi)
Z = r * np.sin(theta)

# Create the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with color mapping
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap='coolwarm', edgecolor='none')

# Set the limits of the plot
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Set the viewpoint
ax.view_init(elev=20, azim=30)

# Show the plot
plt.show()
