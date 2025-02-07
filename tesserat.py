"""
This module provides a function to draw a Tesseract in 3D.
"""

import matplotlib.pyplot as plt
import numpy as np

def desenhar_tesseract(ax):
    """
    Draw a Tesseract in 3D.

    Parameters:
    - ax: The 3D axis to draw on.
    """
    pontos = np.array([[1, 1, 1],
                       [-1, 1, 1],
                       [-1, -1, 1],
                       [1, -1, 1],
                       [1, 1, -1],
                       [-1, 1, -1],
                       [-1, -1, -1],
                       [1, -1, -1]])

    linhas = [[pontos[i], pontos[j]] for i in range(len(pontos)) for j in range(i+1, len(pontos)) if np.sum(np.abs(pontos[i] - pontos[j])) == 2]

    for linha in linhas:
        ax.plot3D(*zip(*linha), color="b")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

desenhar_tesseract(ax)

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

plt.show()
