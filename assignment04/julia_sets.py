#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Name:      Huber, Dennys
   Email:     dennys.huber@uzh.ch
   Date:      03 October, 2021
   Course:    ESC201
   Semester:  FS21
   Week:      4
   Topic:     Julia sets
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# Exercise_____________________________________________________________________
"""
Fractals: Draw some Julia sets with various constants c 
(you can start with the Mandelbrot set as it was explained in the 
lecture and the exercise class)! (to submit by 24 October, 2021, 9pm)
"""
# Functions_____________________________________________________________________
def yes_or_no(question):
    reply = str(input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Please enter ")


# Main__________________________________________________________________________

if __name__ == '__main__':

    mandelbrot = yes_or_no("Output mandelbrot fractal")
    real = 0
    imag = 0
    if mandelbrot == False:
        print("Enter complex constant number c for complex iterator.\n")
        real=float(input("Real part of constant c:"))
        imag=float(input("Imaginary part of constant c:"))


    x = np.linspace(-1.5, 1.0, 300) # Returns evenly spaced numbers over a specified interval.
    y = np.linspace(-1.5, 1.5, 300) # Returns evenly spaced numbers over a specified interval.
    X, Y = np.meshgrid(x, y) # Returns coordinate matrices from coordinate vectors.
    C = X + 1j * Y # Complex coordinate Matrix
    Z = np.copy(C) # Return an array copy of the given object.
    rmax = np.maximum(abs(C), 2*np.ones_like(C)) # max of the distances of C and 2
    iterations = np.zeros_like(C, dtype=int) #integer of 0s

    maxiter = 100
    n = 0
    while n <= maxiter:
        cond = abs(Z) < rmax
        if mandelbrot == True:
            Z[cond] = Z[cond]**2 + C[cond]
        else:
            Z[cond] = Z[cond]**2 + real + imag * 1j
        iterations[cond] += 1
        n += 1

# iterations = iterations / np.max(iterations)
# cmap = cm.get_cmap(name='rainbow')
# color = iterations
    plt.scatter(C.real, C.imag, s=1, c=iterations, cmap='jet')

    if mandelbrot == True:
        name = "mandelbrot"
        c = "c"
    else:
        name = "julia"
        c = str(real) + '+' + str(imag) + 'i'

    plt.savefig('%s_%s.png' % (name, c), dpi=400)

    plt.show()

