import numpy as np
x0 = np.linspace(-2,1,100)
def Function(x):
    return 3*(x**5)+5*(x**4)-(x**3)
def Derivative(f,x,h=1e-6):
    return 15*(x**4)+20*(x**3)-3*(x**2)
def GetNewtonMethod(f,df,xn,itmax=1000,precision=1e-5):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
    
    return xn

def GetAllRoots(x, tolerancia=4):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewtonMethod(Function,Derivative,i)
        
        if root != False:
            
            croot = np.round(root, tolerancia)
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots

print("Las raices de la expresion son: ",GetAllRoots(x0))
