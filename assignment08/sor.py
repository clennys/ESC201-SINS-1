#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      Huber, Dennys
   Email:     dennys.huber@uzh.ch
   Kurs:      ESC201
   Semester:  HS21
   Week:      8
   Thema:     Poisson Gleichung
"""

# Imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage


# Exercise_____________________________________________________________________
"""
Elliptical partial differential equations: Solve the Poisson equation for the 
electromagnetic potential using the SOR method described in the lecture, with 
boundary conditions given by a 1000 Volt stick in the center of a 0 Volt box 
(as depicted in the lecture notes). Plot the contours of the resulting potential
(to submit by 21 November, 2021, 9pm).

"""
# Functions_____________________________________________________________________

def cond(grid):
    condGrid = np.zeros_like(grid, dtype=bool) 
    condGrid[1::2,1::2] = True
    condGrid[::2,::2] = True
    return condGrid

def bound(grid, gridR, x, y):
    for i in range(x):
        for j in range(y):
            if i == round(x/2) and (y/4 < j < 3*y/4): # stick boundries
                grid[i, j] = 1000
                gridR[i, j] = 0
            if i == 0 or i == x - 1: # vertical boundries
                grid[i, j] = 1
                gridR[i, j] = 0
            if j == 0 or j == y - 1: # horizontal boundries
                grid[i, j] = 1
                gridR[i, j] = 0
    return grid, gridR

def update(grid, gridOmega, gridCond):
    filter = np.array([[0, 1, 0], [1, -4, 1], [0,1,0]])
    gridHelp = np.zeros_like(grid)

    ndimage.convolve(grid, filter, output=gridHelp, mode="constant", cval=0)
    gridHelp *= gridOmega
    max1 = np.max(abs(gridHelp[gridCond]))
    grid[gridCond] += gridHelp[gridCond]

    ndimage.convolve(grid, filter, output=gridHelp, mode="constant", cval=0)
    gridHelp *= gridOmega
    max2 = np.max(abs(gridHelp[~gridCond]))
    grid[~gridCond] += gridHelp[~gridCond]

    return grid, max(max1, max2)


# Main__________________________________________________________________________

if __name__== "__main__":
    x, y = 101, 101
    omega = 2/(1+np.pi/(x-1))

    end = 0.001
    diff = 1 + end

    grid = np.zeros((x,y))
    gridOmega = np.ones_like(grid) * omega/4
    grid, gridOmega = bound(grid, gridOmega, x, y)
    gridCond = cond(grid)

    while diff > end:
        grid, diff = update(grid, gridOmega, gridCond)

    contours = np.arange(0, 1000, 60)
    fig, ax = plt.subplots()
    ax.set_title("Electrostatic Potential 1000V Stick")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.contourf(grid, levels=contours, cmap=plt.get_cmap('hot'))
    plt.contour(grid, levels=contours)
    plt.show()
