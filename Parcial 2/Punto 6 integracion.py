# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:42:03 2023

@author: david
"""

import numpy as np


a=-0.01
b=0.01
R=0.5
f=lambda x: np.sqrt(0.01**2-x**2)/(R+x)

ValrealI=np.pi*(R-np.sqrt(R**2-a**2))

def Itrap_err (n):
    omega=np.linspace(a,b,n)
    h=(b-a)/n
    summ=0
    for i in omega[1:-1] :
        summ+=f(i)
    I=h/2*(f(a)+f(b))+h*summ
    error=abs(ValrealI-I)/ValrealI*100
    return error

def Isimp_err (n):
    if n%2==0 and n>=2:
        omega=np.linspace(a,b,n+1)
        h=(b-a)/n
        fomega=f(omega)
        summ=fomega[0]+fomega[-1]
        for i in range(len(fomega[1:-1])):
            if i%2==0:
                summ+=4*fomega[i+1]
            else:
                summ+=2*fomega[i+1]
        I=h/3*summ
        error=abs(ValrealI-I)/ValrealI*100
        return error
    else:
        return 100


N=1
errT=100
while errT>5:
    errT=Itrap_err(N)
    N+=1
print("el n necesario para la formula del trapecio compuesto es "+str(N-1))

N=1
errS=100
while errS>5:
    errS=Isimp_err(N)
    N+=1
print("el n necesario para la formula del simpson 1/3 compuesto es "+str(N-1))
