# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:46:29 2023

@author: david
"""

import numpy as np
Volumen=0
n=10


f=lambda X,Y: X**2+Y**2
R=1
x=np.linspace(-R, R,n+1)
y=np.linspace(-R, R,n+1)
    

    
h=x[1]-x[0]
area=h**2


    
for i in x :
    for j in y:
        summ=0
        s=0
        if f(i,j)<=R:
            summ+=f(i,j)
            s+=1
        if f(i+h,j)<=R:
            summ+=f(i+h,j)
            s+=1
        if f(i,j+h)<=R:
            summ+=f(i,j+h)
            s+=1
        if f(i+h,j+h)<=R:
            summ+=f(i+h,j+h)
            s+=1
        if s!=0:
            Volumen+=summ/s*area

print(Volumen)


            
