# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:53:30 2023

@author: david
"""

import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

x=sym.Symbol("x",real=True)
y=sym.Symbol("y",real=True)
z=x+sym.I*y

f=z**3+1
F=[sym.re(f),sym.im(f)]

J = sym.zeros(2,2)

for i in range(2):
    for j in range(2):
        if j==0:
            J[i,j] = sym.diff(F[i],x,1)
        else:
            J[i,j] = sym.diff(F[i],y,1)
            
InvJ = J.inv(method='LU')

Funcn = sym.lambdify([x,y],F,'numpy')
jacobIn = sym.lambdify([x,y],InvJ,'numpy')

def NewtonRaphson(z,Fn,Jn,itmax=100,precision=1e-7):
    
    error = 1
    it = 0
    
    while error > precision and it < itmax:
        
        IFn = Fn(z[0],z[1])
        IJn = Jn(z[0],z[1])
        
        z1 = z - np.dot(IJn,IFn)
        
        error = np.max( np.abs(z1-z) )
        
        z = z1
        it +=1
    return z

N=300
x=np.linspace(-1,1,N)
y=np.linspace(-1,1,N+1)
Fractal=np.zeros((N,N),np.int64)

z0=np.array([0.5,np.sqrt(3)/2])
z1=np.array([0.5,-np.sqrt(3)/2])
z2=np.array([-1,0])

for i in range(N):
    for j in range(N):
        z=np.array([x[i],y[j]])
        if not np.array_equal(z,np.array([0,0])):
            sol = NewtonRaphson(z,Funcn,jacobIn)
            if np.all(np.round(sol,5)==np.round(z0,5)):
                Fractal[i][j]=20
            elif np.all(np.round(sol,5)==np.round(z1,5)):
                Fractal[i][j]=100
            elif np.all(np.round(sol,5)==np.round(z2,5)):
                Fractal[i][j]=255
                
plt.imshow(Fractal, cmap='coolwarm' ,extent=[-1,1,-1,1])