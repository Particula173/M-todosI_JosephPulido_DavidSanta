import numpy as np
import matplotlib.pyplot as plt
x0 = np.array([0.25,0.625,1.])

def Function(x):
    return (np.exp(-x))-x

def x_3 (f,x0):
    h=x0[1]-x0[0]
    a=(f(x0[2])+(f(x0[0])))/(2*h**2)
    b=((f(x0[1])-f(x0[0]))/(h))-(x0[0]+x0[1])*a
    c=(f(x0[0]))-x0[0]*(((f(x0[1])-f(x0[0]))/(h)))+(x0[0]*x0[1]*a)
    if b<0:
        return((-2*c)/(b-np.sqrt(b**2-4*a*c)))
    elif b>=0:
        return((-2*c)/(b+np.sqrt(b**2-4*a*c)))




def algoritmo (f,x0):
    i=0
    x_3f=x_3(f,x0)
    
    while i!=100 and abs(f(x_3f))>=(1*10**(-10)):
        np.delete(x0,2)
        x0=np.insert(x0,0,x_3f)
        x0.sort()
        x_3f=x_3(f,x0)
        i+=1
    return x_3f
print(algoritmo(Function,x0))
        
