import numpy as np
import matplotlib.pyplot as plt
x0 = np.array([0.25,0.625,1])

def Function(x):
    return (np.exp(-x))-x

def x_3 (f,x0):
    h=x0[1]-x0[0]
    a=(f(X0[2])+(f(x0[0])))/(2*h**2)
    b=((f(x0[1])-f(x0[0]))/(h))-(x0[0]+x0[1])*a
    c=(f(x0[0]))-x0[0]*(((f(x0[1])-f(x0[0]))/(h)))+(x0[0]*x0[1]*a)
    print(a,b,c)
prin