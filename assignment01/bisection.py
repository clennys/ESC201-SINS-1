#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Name:      Huber, Dennys
   Email:     dennys.huber@uzh.ch
   Date:      22 September, 2021
   Course:    ESC201
   Semester:  FS21
   Week:      1
   Topic:     bisection root finding method
"""

import numpy as np

# Functions_____________________________________________________________________

def func0(x):
    return x**3 + 5*x**2 - 8*x - 2

def func1(x):
    return x**x - 100

def bisection(f, a, b, e):

    # Check the signs
    if np.sign(f(a)) == np.sign(f(b)):
        raise Warning("Invalid Input!")

    # Swap a and b if f(a) is positive and f(b) is negative
    if(f(a) > 0 and f(b) < 0):
        tmp = b
        b = a
        a = tmp

    m = b

    # Loop while |a-b| is bigger than the absolut error
    while np.abs(a - b) > e:
        m = (a + b)/2
        if f(m) > 0:
            b = m
        else:
            a = m

    return m

def print_root(f, x):
    y = f(x)
    print("root: (%f,%f)" % (x, y))


# Main__________________________________________________________________________

if __name__ == '__main__':

    #func0
    print_root(func0, bisection(func0, 0, -2, 0.00001))
    print_root(func0, bisection(func0, 2, 0, 0.00001))
    print_root(func0, bisection(func0, -2, -8, 0.00001))

    #func1
    print_root(func1, bisection(func1, 0, 4, 0.00001))
