#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:42:39 2018

https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.convolve.html

@author: Stefan
"""

import numpy as np
from scipy import ndimage


def ex1():
    U = np.ones((5,5))
    W = np.array([[0,0,0],[0,2,0],[0,0,0]])
    Out = np.zeros_like(U)
    ndimage.convolve(U, W, output=Out, mode="constant", cval=0)
    print(U)
    print(W)
    print(Out)


def ex1a():
    U = np.ones((5,5))
    W = np.array([[0,0,0],[0,0,0],[0,0,2]])
    Out = np.zeros_like(U)
    ndimage.convolve(U, W, output=Out, mode="constant", cval=0)
    print(U)
    print(W)
    print(Out)


def ex2():
    U = np.ones((5,5))
    W = np.array([[0,0,0],[1,1,1],[0,0,0]])
    Out = np.zeros_like(U)
    ndimage.convolve(U, W, output=Out, mode="constant", cval=0)
    print(U)
    print(W)
    print(Out)


def ex3():
    U = np.ones((5,5))
    W = np.array([[0,1,0],[0,1,0],[0,1,0]])
    Out = np.zeros_like(U)
    ndimage.convolve(U, W, output=Out, mode="constant", cval=0)
    print(U)
    print(W)
    print(Out)
    

def ex4():
    U = np.ones((5,5))
    W = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    Out = np.zeros_like(U)
    ndimage.convolve(U, W, output=Out, mode="constant", cval=0)
    print(U)
    print(W)
    print(Out)


def ex5():
    C = np.zeros((5, 5), dtype=bool)
    print(C, "\n")
    C[::2, ::2] = True
    print(C, "\n")
    C[1::2, 1::2] = True
    print(C)
    