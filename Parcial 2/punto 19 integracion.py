# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:44:33 2023

@author: david
"""

import numpy as np

roots, wheigts = np.polynomial.legendre.leggauss(50)

f=lambda x,t,delt:np.tanh(np.sqrt(x**2+delt**2)*300/(2*t))/np.sqrt(x**2+delt**2)


def integral(T,deltaT):
    I=1/2*np.sum(wheigts*f(roots,T,deltaT))
    return I

dt=0.0001  
T=np.arange(12.1321,12.134,dt)


i=0
centi=True
tc=0
while centi and i<=len(T):
    I=integral(T[i],0)
    if np.abs(I-1/0.3)<0.00014:
        centi=False
        tc=round(T[i],4)
    else:
        i+=1


print(tc)