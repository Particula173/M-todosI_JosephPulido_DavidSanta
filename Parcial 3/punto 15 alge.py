# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:44:52 2023

@author: david
"""

import numpy as np 

sigmas=[np.array([[0,1],[1,0]]),
        np.array([[0,-1j],[1j,0]]),
        np.array([[1,0],[0,-1]])
        ]

def func(i,j):
    lista=[1,2,3]
    lista.remove(i)
    lista.remove(j)
    k=lista[0]
    return [i,j,k]

def simboLC(lis):
    val=0
    if lis==[1, 2, 3] or lis==[2, 3, 1] or lis==[3, 1, 2]:
        val=1
    elif lis==[3, 2, 1] or lis==[2, 1, 3] or lis==[1, 3, 2]:
        val=-1
    return val

def AlgLie(i,j):
    lista=func(i, j)
    simbolo=simboLC(lista)
    k=lista[2]
    sigmak=sigmas[k-1]
    resultado=2*1j*simbolo*sigmak
    return(resultado)

def conmutador(i,j):
    A=sigmas[i-1]
    B=sigmas[j-1]
    resultado= np.dot(A,B)-np.dot(B,A)
    return resultado


for i in range (1,4):
    for j in range (1,4):
        if i!=j:
            print(np.all(AlgLie(i, j)==conmutador(i, j)))