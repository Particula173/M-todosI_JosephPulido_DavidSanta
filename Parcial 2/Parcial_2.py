import numpy as np
import sympy as sp



h = 6.626 *10**(-34)
k = 1.3806 * 10**(-23)
c = 3*10**(8)
t = 5772

def integral_numerador (v_0,v_1):
    g=lambda x : (x**3)/(((np.e)**x)-1)
    r , w = np.polynomial.legendre.leggauss(20)
    integral =(np.sum(w*g((((r*(v_1-v_0))/2)+((v_0+v_1)/2)))))*((v_1-v_0)/2)  
    return integral

def Idenominador():
    r2 , w2 = np.polynomial.laguerre.laggauss(20)
    f2=lambda x: x**3/(1-np.e**(-x))
    I=np.sum(w2*f2(r2))
    return I


landa_0 = 100*10**(-9)
landa_1 = 400*10**(-9)
a = (h*(c / landa_1))/(k*t)
b = (h*(c / landa_0))/(k*t)


num = integral_numerador(a,b)
den = Idenominador()
frac = (num/den)*100
print(frac)

print("la diferencia presentada entre lo medido en bogota f=7.2% y lo generado por el sol f=12%, es debido a la atmosfera")