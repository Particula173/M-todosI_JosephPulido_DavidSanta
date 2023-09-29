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

landa_0 = 100*10**(-9)
landa_1 = 400*10**(-9)
v_1 = (h*(c / landa_1))/(k*t)
v_0 = (h*(c / landa_0))/(k*t)
g=lambda x : (x**3)/(((np.e)**x)-1)
def integral_numerador (v_0,v_1):
    r , w = np.polynomial.legendre.leggauss(20)
    integral =np.sum(w*g((((r*(v_1-v_0))/2)+((v_0+v_1)/2))))  
    return integral
print(integral_numerador(v_0,v_1))
x = sp.symbols("x")
verificacion = sp.integrate(g(x), x,)