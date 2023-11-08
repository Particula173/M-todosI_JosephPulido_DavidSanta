# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:34:49 2023

@author: david
"""

import numpy as np
import sympy as sym

x=sym.Symbol("x",real=True)
y=sym.Symbol("y",real=True)

F=np.array([sym.log(x**2+y**2)-sym.sin(x*y)-sym.log(2)-sym.log(sym.pi),
sym.exp(x-y)+sym.cos(x*y)])

Fnp= np.array([sym.lambdify([x,y],F[0],'numpy'),
               sym.lambdify([x,y],F[1],'numpy')])

def GetF(G,r):
    
    n = r.shape[0]
    
    v = np.zeros_like(r)
    
    for i in range(n):
        v[i] = G[i](r[0],r[1])
    return v



dim=F.shape[0]
J = sym.zeros(dim)


for i in range(dim):
    for j in range(dim):
        if j==0:
            J[i,j] = sym.diff(F[i],x,1)
        else:
            J[i,j] = sym.diff(F[i],y,1)
InvJsym = J.inv(method='LU')
InvJ = sym.lambdify([x,y],InvJsym,'numpy')

def NewtonRaphson(G,r,J,itmax=1000,error=1e-9):
    
    it = 0
    d = 1.
    dvector = []
    
    while d > error and it < itmax:
        
        rc = r
        F = GetF(G,rc)
        
            
        Jeval=J(rc[0],rc[1])
        
        r = rc - np.dot(Jeval,F)
        
        diff = r - rc
        
        d = np.max( np.abs(diff) )
        
        it += 1
        
    return r,dvector


r,d=NewtonRaphson(Fnp, np.array([2.,2.]),InvJ)

print(r )