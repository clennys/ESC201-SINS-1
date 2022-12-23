#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Name:      Huber, Dennys
   Email:     dennys.huber@uzh.ch
   Date:      03 October, 2021
   Course:    ESC201
   Semester:  FS21
   Week:      3
   Topic:     Feigenbaum
"""

import numpy as np
import matplotlib.pyplot as plt


# Exercise_____________________________________________________________________
"""
Plot (and/or animate) the elliptical orbit of a planet around the sun by 
repeatedly solving Kepler's equation with Newton's method 
(or the bisection method), 
as explained in the lecture! (to submit by 10 October 2021, 9pm)
"""
# Functions_____________________________________________________________________
def LogEq(a, x):
	return a * x * (1 - x)


# Main__________________________________________________________________________

if __name__ == '__main__':

    fig, ax = plt.subplots()
    len = 10000
    xList = 1e-5 * np.ones(len)
    aList = np.linspace(2.5, 4.0, len)
    print = 900

    for i in range(1000):
        xList = LogEq(aList, xList)
        if i >= (print):
                ax.plot(aList, xList, ',k')
        ax.set_xlim(2.5, 4)
    ax.set_title("Feigenbaum diagram")
    plt.show()


