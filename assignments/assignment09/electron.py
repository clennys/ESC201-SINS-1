#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Name:      Huber, Dennys
   Email:     dennys.huber@uzh.ch
   Kurs:      ESC201
   Semester:  HS21
   Week:      8
   Thema:     Interpolation
"""

# Imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage


# Exercise_____________________________________________________________________
"""
Interpolation, Part 1:
Trace the movement of electrons in an electromagnetic potential
(e.g. the one from the last exercise) with Leapfrog or Runge-Kutta.
Use bilinear or bicubic interpolation for the potential.

Interpolation, Part 2 (WIN A PRIZE):
Design an optimal electron detector (specifics in lecture materials)

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
                grid[i, j] = 0
                gridR[i, j] = 0
            if j == 0 or j == y - 1: # horizontal boundries
                grid[i, j] = 0
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

def placePlate(p1, p2, R, U, potential, ax):
    x1, y1 = p1
    x2, y2 = p2
    if x2 < x1:
        t = x2
        x2 = x1
        x1 = t
        t = y2
        y2 = y1
        y1 = t
    a = (y2 - y1) / (x2 - x1)
    j1 = int(x1 / deltaX)
    j2 = int(x2 / deltaX)
    l1 = int(y1 / deltaY)
    l2 = int(y2 / deltaY)

    n = max(j2-j1+1, l2-l1+1)
    for i in range(n+1):
        x = x1 + i*(x2 - x1)/n
        y = y1 + a*(x - x1)
        j = int(x / deltaX)
        l = int(y / deltaY)
        R[l, j] = 0
        U[l, j] = potential
    ax.plot([x1, x2], [y1, y2])

def generateElectrons(n):
    y = np.linspace(0.6*boxH, 0.9*boxH, n)
    x = np.zeros_like(y)
    # Take a random angle phi in the range -pi/2 to pi/2,
    # either uniform or normal distributed
    # vx = 1e6 * cos(phi)
    # vy = 1e6 * sin(phi)
    vx = 1e6*np.ones_like(x)
    vy = np.zeros_like(y)
    return np.array([x, y, vx, vy])

def coordToIndex(x, y):
    j = np.array(x / deltaX, dtype='int')
    l = np.array(y / deltaY, dtype='int')
    return (j, l)

def leapFrog(p, a, h):

    p12x = p[0] + h/2 * p[2]
    p12y = p[1] + h/2 * p[3]

    v1x =  p[2] + h * a[0]
    v1y =  p[3] + h * a[1]

    p1x = p12x + h/2 * v1x
    p1y = p12y + h/2 * v1y

    return np.array([p1x, p1y, v1x, v1y])


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

    boxH = 1
    deltaX = .001
    deltaY = .001
    e = 1.6e-19
    me = 9.11e-31
    ne = 10
    h = 0.0000000001
    steps = 50


    p0 = generateElectrons(ne)

    res = [p0]
    p = p0

    for _ in range(steps):
        j, l = coordToIndex(p[0], p[1]) # Coordinates of electorns (x,y)

        L, J = grid.shape # 101 x 101
        j = np.maximum(j, np.zeros_like(j))
        j = np.minimum(j, (J-2)*np.ones_like(j))
        l = np.maximum(l, np.zeros_like(l))
        l = np.minimum(l, (L-2)*np.ones_like(l))

        t = (p[0] - j*deltaX) / deltaX
        u = (p[1] - l*deltaY) / deltaY

        U1 = grid[l,j]
        U2 = grid[l,j+1]
        U3 = grid[l+1,j+1]
        U4 = grid[l+1,j]

        ax = -(e/me)/deltaX*((1-u)*(U2-U1) + u*(U4-U3))
        print("ax", ax)
        print("e", -(e/me)/deltaX)
        ay = -(e/me)/deltaY*((1-t)*(U3-U1) + t*(U4-U2))

        a = np.array([ax, ay])

        pnew = leapFrog(p, a, h)

        res.append(pnew)
        p = pnew

    res = np.array(res)
    print(res[:,0])

    fig, ax = plt.subplots()
    ax.plot(res[:,0], res[:,1])
    plt.show()


