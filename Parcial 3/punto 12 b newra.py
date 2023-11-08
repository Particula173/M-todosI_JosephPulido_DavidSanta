# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 11:06:35 2023

@author: david
"""

import numpy as np
import sympy as sym

x=sym.Symbol("x",real=True)
y=sym.Symbol("y",real=True)
z=sym.Symbol("z",real=True)

F=np.array([6*x-2*sym.cos(y*z)-1,
            9*y+sym.sqrt(x**2+sym.sin(z)+1.06)+0.9,
            60*z +3*sym.exp(-x*y)+10*sym.pi-3])

Fnp= np.array([sym.lambdify([x,y,z],F[0],'numpy'),
               sym.lambdify([x,y,z],F[1],'numpy'),
               sym.lambdify([x,y,z],F[2],'numpy')])

def GetF(G,r):
    
    n = r.shape[0]
    
    v = np.zeros_like(r)
    
    for i in range(n):
        v[i] = G[i](r[0],r[1],r[2])
    return v



dim=F.shape[0]
J = sym.zeros(dim)


for i in range(dim):
    for j in range(dim):
        if j==0:
            J[i,j] = sym.diff(F[i],x,1)
        elif j==1:
            J[i,j] = sym.diff(F[i],y,1)
        else:
            J[i,j] = sym.diff(F[i],z,1)
InvJsym = J.inv(method='LU')
InvJ = sym.lambdify([x,y,z],InvJsym,'numpy')

def NewtonRaphson(G,r,J,itmax=1000,error=1e-9):
    
    it = 0
    d = 1.
    dvector = []
    
    while d > error and it < itmax:
        
        rc = r
        F = GetF(G,rc)
        
            
        Jeval=J(rc[0],rc[1],rc[2])
        
        r = rc - np.dot(Jeval,F)
        
        diff = r - rc
        
        d = np.max( np.abs(diff) )
        
        it += 1
        
    return r,dvector


r,d=NewtonRaphson(Fnp, np.array([0.,0.,0.]),InvJ)

print(r )