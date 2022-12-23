#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Name:      Huber, Dennys
   Email:     dennys.huber@uzh.ch
   Date:      26 October, 2021
   Course:    ESC201
   Semester:  FS21
   Week:      6
   Topic:     oscillator & pendulum
"""

import numpy as np
import matplotlib.pyplot as plt


# Exercise_____________________________________________________________________
"""
Symplectic Integrators: Use the Leap-Frog method to make a phase plot (p vs q) 
of the harmonic oscillator for different total energies. Compare the results 
with what you get using the Forward Euler method and the midpoint Runge-Kutta 
method. Make the same plot for a simple pendulum 
(to submit by 7 November, 2021, 9pm).
"""
# Functions_____________________________________________________________________
def odeSolver(p0, q0, dfFunc, h, nSteps, solverStepFunc):
    qn = q0
    pn = p0
    plist = [p0]
    qlist = [q0]
    for _ in range(nSteps):
        pn1, qn1  = solverStepFunc(pn, qn, h, dfFunc)
        plist.append(pn1)
        qlist.append(qn1)
        pn = pn1
        qn = qn1
    return (np.array(plist), np.array(qlist))

def eulerStep(pn, qn, h, dfdt):
    dp, dq = dfdt(pn, qn)
    pn += h * dp
    qn += h * dq
    return np.array([pn, qn])

def midPointRK2Step(pn, qn, h, dfdt):
    dp, dq = dfdt(pn, qn)
    dp2, _ = dfdt(pn + h/2, qn + h/2 * dp)
    _, dq2 = dfdt(pn + h/2, qn + h/2 * dq)
    pn += h * dp2
    qn += h * dq2
    return np.array([pn, qn])

def leapFrog(p0, q0, h, odeSystem):
    q12 = q0 + 0.5*h*p0         # first drift
    dp, dq = odeSystem(p0, q12)
    p1 = p0 + h*dp              # kick
    q1 = q12 + 0.5*h*p1         # second drift
    return np.array([p1, q1])

def odeHo(p,q):
    dp = -q
    dq = p
    return np.array([dp, dq])

def odePendulum(p,q):
    dp = - eps * np.sin(q)
    dq = p
    return np.array([dp, dq])


# Main__________________________________________________________________________

if __name__ == '__main__':
    fig, ax = plt.subplots(2,3)
    h = 0.1
    nSteps = 100
    eps = 1
    p = 1

    qlist = [1, 2, 3]
    x = []
    y = []

    for q in qlist:
        x, y = odeSolver(p, q, odeHo, h, nSteps, leapFrog)
        ax[0,0].set_title("Leap Frog")
        ax[0,0].plot(x,y)
        ax[0,0].set_xlabel("p")
        ax[0,0].set_ylabel("q")
        x, y = odeSolver(p, q, odeHo, h, nSteps, eulerStep)
        ax[0,1].set_title("Euler")
        ax[0,1].plot(x,y)
        ax[0,1].set_xlabel("p")
        ax[0,1].set_ylabel("q")
        x, y = odeSolver(p, q, odeHo, h, nSteps, midPointRK2Step)
        ax[0,2].set_title("Mid Point RK2")
        ax[0,2].plot(x,y)
        ax[0,2].set_xlabel("p")
        ax[0,2].set_ylabel("q")

    h = 0.0005
    p = 0.0001
    nSteps = 30000
    qlist = np.linspace(-10*np.pi, 10*np.pi, 100)
    for q in qlist:
        x, y = odeSolver(p, q, odePendulum, h, nSteps, leapFrog)
        ax[1,0].set_title("Leap Frog")
        ax[1,0].plot(y,x)
        ax[1,0].set_ylabel("p")
        ax[1,0].set_xlabel("q")
        ax[1,0].set_xlim(-4, 4)

        x, y = odeSolver(p, q, odePendulum, h, nSteps, eulerStep)
        ax[1,1].set_title("Euler")
        ax[1,1].plot(y,x)
        ax[1,1].set_ylabel("p")
        ax[1,1].set_xlabel("q")
        ax[1,1].set_xlim(-4, 4)

        x, y = odeSolver(p, q, odePendulum, h, nSteps, midPointRK2Step)
        ax[1,2].set_title("Mid Point RK2")
        ax[1,2].plot(y,x)
        ax[1,2].set_ylabel("p")
        ax[1,2].set_xlabel("q")
        ax[1,2].set_xlim(-4, 4)

    fig.tight_layout()
    plt.savefig('oscillator_pendulum.png', dpi=400)
    plt.show()


