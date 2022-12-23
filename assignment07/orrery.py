#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Name:      Huber, Dennys
   Email:     dennys.huber@uzh.ch
   Date:      26 October, 2021
   Course:    ESC201
   Semester:  FS21
   Week:      6
   Topic:     Solar System orrery
"""

import numpy as np
import matplotlib.pyplot as plt


# Exercise_____________________________________________________________________
"""
Make a solar system orrery following the steps outlined in the lecture 
(to submit by 14 November, 2021, 9pm)!
"""
# Functions_____________________________________________________________________

# Loading text files with NumPy
def readPlanetsNp(filename):
    data = np.loadtxt(filename, delimiter=',', unpack=False,
        dtype={'names': ('planet', 'mass', 'x', 'y', 'z', 'vx', 'vy', 'vz'),
               'formats': ('S10', float, float, float, float,
                           float, float, float)})

    # print(data)
    name = np.array([d[0] for d in data])
    m = np.array([d[1] for d in data])
    r = np.array([[d[2], d[3], d[4]] for d in data])
    v = np.array([[d[5], d[6], d[7]] for d in data])
    return (name, r, v, m)

def magnitude(vec):
    res = 0
    for i in vec:
        res += i*i
    return res

def leapFrog(n, r, m, v, h):
    r12 = np.zeros_like(r)
    v1 = np.zeros_like(r)
    r1 = np.zeros_like(r)
    for i in range(n.size):
        r12[i] = r[i] + 0.5*v[i] # half drift
    a = acceleration(n, r12, m)
    for i in range(n.size):
        v1[i] = v[i] + h * a[i] # full kick
        r1[i] = r12[i] + 0.5 * v1[i] # half drift
    return r1, v1

def acceleration(n, r, m):
    a = np.zeros_like(r)
    k =  0.01720209895
    for i in range(n.size):
        for j in range(i + 1, n.size):
            delta_r = r[j] - r[i]
            r2 = magnitude(delta_r)
            ir = 1/np.sqrt(r2)
            ir3 = ir**3
            # NOTE: Add k2 even though isn't part of psudo code (lecture)
            mir3 = k**2 * m[i] * m[j] * ir3 
            force = mir3 * delta_r
            a[i] += force * 1/m[i]
            a[j] -= force * 1/m[j]
    return a

def orbits(n, r0, v0, m, h, d, e):
    res = [r0] # [planet[xyz]]
    r = r0
    v = v0
    while d <= e:
        rnew, vnew = leapFrog(n, r, m, v, h)
        d += h
        res.append(rnew)
        r = rnew
        v = vnew
    return np.array(res)


# Main__________________________________________________________________________

if __name__ == '__main__':
    h = 1
    day = 0
    end = h * 1000
    name, r0, v0, m = readPlanetsNp("SolSystData.dat")
    res = orbits(name, r0, v0, m, h, day, end)

    end = h * 365 * 165
    resOutter = orbits(name, r0, v0, m, h, day, end)


    fig, ax = plt.subplots(2,2)
    for object in range(9):
        if object < 5:
            ax[0,0].plot(res[:,object,0], res[:,object,1], label=str(name[object], 'utf-8')[1:-1])
            ax[1,0].plot(res[:,object,0], res[:,object,2], label=str(name[object], 'utf-8')[1:-1])
        else:
            ax[0,1].plot(resOutter[:,object,0], resOutter[:,object,1], label=str(name[object], 'utf-8')[1:-1])
            ax[1,1].plot(resOutter[:,object,0], resOutter[:,object,2], label=str(name[object], 'utf-8')[1:-1])

    ax[0,1].plot(resOutter[:,0,0], resOutter[:,0,1], label='Sun')
    ax[1,1].plot(resOutter[:,3,0], resOutter[:,3,2], label='Earth')
    
    ax[0,0].set_title("Orbits")
    ax[0,0].legend(prop={'size': 4})
    ax[0,0].set_xlabel("x")
    ax[0,0].set_ylabel("y")

    ax[1,0].set_title("Orbital Inclinations")
    ax[1,0].legend(prop={'size': 4})
    ax[1,0].set_xlabel("x")
    ax[1,0].set_ylabel("z")

    ax[0,1].set_title("Orbits")
    ax[0,1].legend(prop={'size': 4})
    ax[0,1].set_xlabel("x")
    ax[0,1].set_ylabel("y")

    ax[1,1].set_title("Orbital Inclinations")
    ax[1,1].legend(prop={'size': 4})
    ax[1,1].set_xlabel("x")
    ax[1,1].set_ylabel("z")

    fig.tight_layout()
    plt.savefig('orrery.png', dpi=400)
    plt.show()
