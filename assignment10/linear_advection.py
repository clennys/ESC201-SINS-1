#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Name:      Huber, Dennys
   Email:     dennys.huber@uzh.ch
   Date:      12 December, 2021
   Course:    ESC201
   Semester:  FS21
   Week:      11
   Topic:     Solar System orrery
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace


# Exercise_____________________________________________________________________
"""
Hyperbolic PDEs: Solve the linear advection equation by evolving an initial 
waveform in a periodic grid. See how the waveform behaves after passing through
the grid multiple times and compare the results you get when using various
methods introduced in the lecture 
(e.g. the LAX method, upwind scheme, LAX-Wendroff method…) 
(you can get 0.5 bonus points if you implement all three variants provided in
Stefan's Hyperbolic Hints.txt) (to submit by 12 December, 2021, 9pm).
"""
# Functions_____________________________________________________________________

def lax_method(_, rho_jp1, rho_jm1, c):
    return 0.5*(rho_jp1 + rho_jm1) + 0.5*c*(rho_jm1 - rho_jp1) 

def upwind_scheme(rho, _, rho_jm1, c):
    # for a > 0
    return rho - c*(rho - rho_jm1)

def lax_wendroff_method(rho, rho_jp1, rho_jm1, c):
    return 0.5*c*(1 + c)*rho_jm1 + (1 - c**2)*rho - 0.5*c*(1 - c)*rho_jp1

def time_step(rho, method, c):
    rho_jp1 = np.roll(rho, -1)
    rho_jm1 = np.roll(rho, 1)
    rho_new = method(rho, rho_jp1, rho_jm1, c)
    return rho_new


# Main__________________________________________________________________________

if __name__ == '__main__':
    n = 200
    rho = np.zeros(n)
    x = np.arange(n)
    c = 0.5 # clf := 0 <= c < 1

    for j in range(int(n/2)-10, int(n/2)+10):
      rho[j] = 1

    fig, ax = plt.subplots(1, 3)

    t1 = rho
    t2 = rho
    t3 = rho

    for i in range(2*n):
        tnew1 = time_step(t1, lax_method, c)
        tnew2 = time_step(t2, upwind_scheme, c)
        tnew3 = time_step(t3, lax_wendroff_method, c)
        t1 = tnew1
        t2 = tnew2
        t3 = tnew3
        if i%50 == 1:
            ax[0].plot(x, t1)
            ax[1].plot(x, t2)
            ax[2].plot(x, t3)

    ax[0].set_title("LAX")
    ax[1].set_title("Upwind")
    ax[2].set_title("LAX-Wendroff")

    plt.tight_layout()
    plt.savefig('advection.png', dpi=400)
    plt.show()
