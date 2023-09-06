import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

def cargar_datos (a):
    D = pd.read_csv(a,sep=',')
    x=D['X']
    y=D['Y']
    return (x,y)

def lagrange (datos,n):
    datos=datos[0]
    x=sp.symbols('x')
    resultado = 1
    for k in range(len(datos)):
        if k != n:
            resultado *= (x-(datos[k]))/((datos[n])-datos[k])
    return resultado

def todo (f,datos):
    L=[]
    r=0
    for i in range(len(datos[0])):
        r+=(f(datos,i))*datos[1][i]
        L.append(r)
        r=0
    return sum(L)

def coeficientes (pol):
   x=(sp.poly_from_expr(pol))[0]
   x=x.all_coeffs()
   return(x[0],x[1])

def valores (Val):
    g=9.8
    ang=sp.atan(Val[1])
    V=np.sqrt(g/(2*(-1*float(Val[0]))*(np.cos(float(ang)))**2))
    print((ang*180)/np.pi)
    return ((round(V,1)),((ang*180)/np.pi))
"""View"""
def imprimir ():
    Datos = cargar_datos("Parabolico.csv")
    polinomio_movimiento = todo(lagrange,Datos)
    coeficientes_polinomio = coeficientes(polinomio_movimiento)
    Resultado = valores(coeficientes_polinomio)
    print("El polinomio que se obtuvo de la interpolacion usando el metodo de lgrange es:", (sp.poly_from_expr(polinomio_movimiento))[0],"\nLa rapidez inicialmente es", Resultado[0],"\nEl angulo con que sale es: ", round(Resultado[1],1))
print(imprimir())
    