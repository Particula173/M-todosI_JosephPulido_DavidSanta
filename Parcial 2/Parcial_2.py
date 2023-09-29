import numpy as np
import sympy as sp
r , w = np.polynomial.legendre.leggauss(20)

h = 6.626 *10**(-34)
k = 1.3806 * 10**(-23)
c = 3*10**(8)
t = 5772



def Idenominador():
    r2 , w2 = np.polynomial.legendre.leggauss(20)
    f2=lambda x: x**3/(1-np.e**(-x))
    I=np.sum(w2*f(r2))
    return I

