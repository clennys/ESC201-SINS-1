#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Name:      Huber, Dennys
   Email:     dennys.huber@uzh.ch
   Date:      03 October, 2021
   Course:    ESC201
   Semester:  FS21
   Week:      2
   Topic:     Kepler's equation
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Exercise_____________________________________________________________________
"""
Plot (and/or animate) the elliptical orbit of a planet around the sun by repeatedly solving Kepler's equation with Newton's method (or the bisection method), as explained in the lecture! (to submit by 10 October 2021, 9pm)
"""
# Functions_____________________________________________________________________
def newtons_method(f, f_prime, M, e, start):
    E = start
    Enew = E + 1
    tol = 0.00001
    while np.abs(E - Enew) > tol:
        dx = -f(E, M, e)/f_prime(E, e) 
        Enew = E + dx
        E = Enew
    return E

def kepler(E, M, e):
    return E - e*np.sin(E) - M

def kepler_prime(E, e):
    return 1 - e*np.cos(E)

def init():
    ax.set_xlim(-2*a, a+10)
    ax.set_ylim(-a-10, a+10)
    ax.set_title("Kepler's Equation with Newton's method")
    plt.plot([0], [0], 'yo', ms=15)
    ax.text(-1.75*a, 0.75*a, "a = %d \ne = %.2f" % (a, e))
    ax.grid()
    return ln,


def update(frame):
    global xdata, ydata
    M = frame
    E = newtons_method(kepler, kepler_prime, M, e, M)
    x = a*np.cos(E) - a*e
    y = a*np.sqrt(1-e**2)*np.sin(E)
    xdata.append(x)
    ydata.append(y)
    ln.set_data(xdata, ydata)
    return ln,


# Main__________________________________________________________________________

if __name__ == '__main__':

    # Input a and e
    a=int(input("Semi-major axis of ellipse (int >0):"))
    e=float(input("Eccentricity of ellipse (float [0-1]):"))
    f=int(input("Frames (int ex. 64, 128, etc):"))

    # Plot Animation
    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'k.', animated=True,)
    ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, f),
                        init_func=init, blit=True, interval=20)
    # Save as mp4
    ani.save("kepler%d_%.2f_fps%d.mp4" % (a,e,f), writer="ffmpeg", dpi=250 , fps=2*np.pi)

    # Show Plot
    plt.show()
