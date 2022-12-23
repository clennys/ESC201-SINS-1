# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

x = np.linspace(-1.5, 1.0, 300)
y = np.linspace(-1.5, 1.5, 300)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y
Z = np.copy(C)
rmax = np.maximum(abs(C), 2*np.ones_like(C))
iterations = np.zeros_like(C, dtype=int)

maxiter = 100
n = 0
while n <= maxiter:
    cond = abs(Z) < rmax
    Z[cond] = Z[cond]**2 + C[cond]
    iterations[cond] += 1
    n += 1

plt.scatter(C.real, C.imag, s=1, c=iterations, cmap='rainbow')

# iterations = iterations / np.max(iterations)
# cmap = cm.get_cmap(name='rainbow')
# color = iterations
# plt.scatter(C.real, C.imag, s=1, c=color, cmap=cmap)

plt.show()
