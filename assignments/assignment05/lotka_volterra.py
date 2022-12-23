#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Name:      Huber, Dennys
   Email:     dennys.huber@uzh.ch
   Date:      26 October, 2021
   Course:    ESC201
   Semester:  FS21
   Week:      5
   Topic:     Lotka-Volterra Equation
"""

import numpy as np
import matplotlib.pyplot as plt


# Exercise_____________________________________________________________________
"""
Ordinary Differential Equations: Solve the Lotka-Volterra equation using 
the Euler method and the midpoint Runge-Kutta method (optional:
4th order Runge Kutta method) and compare the results. Make two plots:
the time dependence of both populations (mice and foxes),
and the phase diagram using different initial conditions 
(to submit by 31 October, 2021, 9pm).
"""
# Functions_____________________________________________________________________
def odeSolver(t0, y0, dfFunc, h, nSteps, solverStepFunc):
    yn = y0
    tn = t0
    tlist = [t0]
    ylist = [y0]
    for _ in range(nSteps):
        yn1 = solverStepFunc(tn, yn, h, dfFunc)
        tn1 = tn + h
        tlist.append(tn1)
        ylist.append(yn1)
        tn = tn1
        yn = yn1
    return (np.array(tlist), np.array(ylist))

def eulerStep(tn, yn, h, dfdt):
    return yn + h * dfdt(tn, yn)

def MidPointRK2Step(tn, yn, h, dfdt):
    print(dfdt(tn, yn), type(tn), type(yn))
    return yn + h * dfdt(tn + h/2, yn + h/2 * dfdt(tn, yn))

def RK4Step(tn, yn, h, dfdt):
    k1 = h * dfdt(tn, yn)
    k2 = h * dfdt(tn + h/2, yn + k1/2)
    k3 = h * dfdt(tn + h/2, yn + k2/2)
    k4 = h * dfdt(tn + h, yn + k3)
    return yn + (k1/6 + k2/3 + k3/3 + k4/6)

def LotkaVolterra(t, y):
    dmdt = km * y[0] - kmf * y[0] * y[1]
    dfoxdt = -kf * y[1] + kfm * y[1] * y[0]
    return np.array([dmdt, dfoxdt])

# Main__________________________________________________________________________

if __name__ == '__main__':
    fig, ax = plt.subplots(2,3)
    km = 2
    kmf = 0.02
    kfm = 0.01
    kf = 1.06
    h = 0.01
    nSteps = 1000
    t0 = 0

    y0 = np.array([100,15])
    # time vs population
    t, y = odeSolver(t0, y0, LotkaVolterra, h, nSteps, eulerStep)
    l1 = ax[0,0].plot(t,y)

    t, y = odeSolver(t0, y0, LotkaVolterra, h, nSteps, MidPointRK2Step)
    l2 = ax[0,1].plot(t,y)

    t, y = odeSolver(t0, y0, LotkaVolterra, h, nSteps, RK4Step)
    l3 = ax[0,2].plot(t,y)

    # foxes vs mice (phase)
    initArray  = np.linspace(0.0, 1.0, 10)
    for v in initArray:
        y0 = np.array([kf/kfm, km/kfm])
        y1 = v * y0

        t, y = odeSolver(t0, y1, LotkaVolterra, h, nSteps, eulerStep)
        mices = [i[0] for i in y]
        foxes = [i[1] for i in y]
        ax[1,0].plot(mices, foxes)

        t, y = odeSolver(t0, y1, LotkaVolterra, h, nSteps, MidPointRK2Step)
        mices = [i[0] for i in y]
        foxes = [i[1] for i in y]
        ax[1,1].plot(mices, foxes)

        t, y = odeSolver(t0, y1, LotkaVolterra, h, nSteps, RK4Step)
        mices = [i[0] for i in y]
        foxes = [i[1] for i in y]
        ax[1,2].plot(mices, foxes)

    # plt.legend()
    ax[0,0].set_title("Forward Euler")
    ax[0,0].grid()
    ax[0,0].set_xlabel("time")
    ax[0,0].set_ylabel("population")

    ax[1,0].set_title("Forward Euler Phase")
    ax[1,0].grid()
    ax[1,0].set_xlabel("mice")
    ax[1,0].set_ylabel("foxes")

    ax[0,1].set_title("Mid Point RK 2")
    ax[0,1].grid()
    ax[0,1].set_xlabel("time")
    ax[0,1].set_ylabel("population")

    ax[1,1].set_title("Mid Point RK 2 Phase")
    ax[1,1].grid()
    ax[1,1].set_xlabel("mice")
    ax[1,1].set_ylabel("foxes")

    ax[0,2].set_title("RK 4")
    ax[0,2].grid()
    ax[0,2].set_xlabel("time")
    ax[0,2].set_ylabel("population")

    ax[1,2].set_title("RK 4 Phase")
    ax[1,2].grid()
    ax[1,2].set_xlabel("mice")
    ax[1,2].set_ylabel("foxes")

    labels=["mice", "foxes"]
    fig.legend([l1, l2],
           labels=labels,
           loc="upper left",
           prop={'size': 5}
    )

    fig.tight_layout()
    plt.savefig('lotka_volterra.png', dpi=400)
    plt.show()


