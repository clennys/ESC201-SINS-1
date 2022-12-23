# -*- coding: utf-8 -*-
"""
1D diffusion equation
"""
#%% Load modules
import numpy as np
from scipy.ndimage import convolve
import matplotlib.pyplot as plt

#%% Initial & boundary conditions
Nmax = 1000

DiffCoeff = 1.0

t = 0
# Stable case
dt = 4.9*1e-5
# Instable case
#dt = 5.1*1e-5

x = 0
L = 1.0
dx = 0.01

xGrid = np.linspace(x,L,int(L/dx))

# Option 1: Delta peak
#u = np.zeros_like(xGrid)
#u[0] = 1.0

# Option 2: Sinusoidal temperature distribution
#u = np.sin(2*np.pi*xGrid)

# Option 3: Compact support distribution
lamda=0.1
u = 1-(xGrid-0.5)**2/lamda**2
mask = (abs(xGrid-0.5)>lamda)
u[mask]=0.0

alpha = DiffCoeff*dt/dx**2

#%% Solving the diffusion equation

#Explicit method:

LaplaceKernel1D = np.array([1,-2,1])

uList = [u]
n = 0
while n<Nmax:
    u=u+alpha*convolve(u,LaplaceKernel1D)
    uList.append(u)
    n += 1
    
uArr = np.array(uList)



#%% Plot the result

Fig1, ax1= plt.subplots()
for i in range(len(uList)):
    if i%50==0:
        ax1.plot(xGrid, uArr[i,:])
ax1.set_xlabel("L")
ax1.set_ylabel("u")
plt.show()