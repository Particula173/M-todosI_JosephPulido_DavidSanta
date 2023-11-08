# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:46:42 2023

@author: david
"""

import numpy as np 

sigmas=[np.array([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]]),
        np.array([[0,0,0,-1],[0,-1,0,0],[0,0,1,0],[1,0,0,0]]),
        np.array([[0,0,0,-1j],[0,1j,0,0],[0,0,1j,0],[-1j,0,0,0]]),
        np.array([[0,0,-1,0],[0,0,0,1],[1,0,0,0],[0,-1,0,0]])
        ]


AlgClif=2*np.array([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]])*np.identity(4)


def conmutador(i,j):
    A=sigmas[i]
    B=sigmas[j]
    resultado= np.dot(A,B)+np.dot(B,A)
    return resultado


print(conmutador(0, 2))

for i in range (0,4):
    for j in range (0,4):
        if i!=j:
            print(np.all(AlgClif==conmutador(i, j)))