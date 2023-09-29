import numpy as np
import sympy as sp

x=sp.Symbol("x")

def GetLaguerreRecursive(n,x):

    if n==0:
        poly = sp.Number(1)
    elif n==1:
        poly = 1-x
    else:
        poly =((((2*(n-1))+1-x)*GetLaguerreRecursive(n-1,x))-((n-1)*GetLaguerreRecursive(n-2,x)))/n
    return sp.expand(poly,x)
poly = GetLaguerreRecursive(2,x)
print(poly)