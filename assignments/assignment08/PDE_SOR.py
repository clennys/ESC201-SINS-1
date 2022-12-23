#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:42:39 2018

@author: florianfurrer
"""

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

toleranz = 0.01
J,L = 50,50 # J = Zeile && L = Spalte
omega= 2/(1+(np.pi/J))

U = np.zeros((J+1,L+1))
R = np.ones_like(U)*(omega/4)
C = np.zeros_like(U)
M = np.zeros_like(U)

def condition(U):
    P = np.zeros_like(U,dtype=bool) # geht in jeder zweiten Spalte jede 2. Zelle markieren
    P[::2,::2] = True
    P[1::2,1::2] = True
    return P

def border(U,R):
    for j in range(0,J+1):
        for l in range(0,L+1):
            if j==0 or j==J:
                U[j,l]=1
                R[j,l]=0
            if l==0 or l==L:
                U[j,l]=1
                R[j,l]=0
            if j==round(J/2) and l>(L/4) and l<(3*L/4):
                U[j,l]=1000 #Bedingung für Mitte
                R[j,l]=0
border(U,R)
P = condition(U)

def correction(U,R,C,M,P):
    W = np.array([[0,1,0],[1,-4,1],[0,1,0]])
    ndimage.convolve(U,W,output=C,mode="constant",cval=0)
    np.multiply(R,C, out=M)
    max1=np.amax(np.absolute(M[P]))
    U[P]=U[P]+M[P]
    ndimage.convolve(U,W,output=C,mode="constant",cval=0) #weil teilweise modifiziertes U
    np.multiply(R,C, out=M)
    max2=np.amax(np.absolute(M[~P]))
    U[~P]=U[~P]+M[~P]
    return U,max(max1,max2)

cor = toleranz+1
#count = 0
while cor>toleranz:
    U,cor = correction(U,R,C,M,P)
#    count +=1

levels = np.arange(0,1000,50)    
plt.contour(U,levels=levels)
plt.show()
