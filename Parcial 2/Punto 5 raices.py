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
print(GetLaguerreRecursive(20,x))
def GetNewton(f,df,xn,itmax=10000,precision=1e-9):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
    
def GetDLaguerre(n,x):
    Pn = GetLaguerreRecursive(n,x)
    return sp.diff(Pn,x,1)
    
def GetRoots(f,df,x,tolerancia = 5):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots
def GetAllRootsGLeg(n):
    j=n+((n-1)*np.sqrt(n))
    xn = np.linspace(0,j,round(50+((j**2)/2)))
    
    Legendre = np.array([])
    DLegendre = np.array([])
    
    for i in range(n+1):
        Legendre =np.append(Legendre,GetLaguerreRecursive(i,x))
        DLegendre =np.append(DLegendre,GetDLaguerre(i,x))
    
    poly = sp.lambdify([x],Legendre[n],'numpy')
    Dpoly = sp.lambdify([x],DLegendre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

print(GetAllRootsGLeg(20))

def GetWeightsGLag(n):
    l_n_1 = sp.lambdify(x,GetLaguerreRecursive(n+1,x),"numpy")
    x_k = GetAllRootsGLeg(n)
    c_k = np.array([])
    for i in x_k:
        W = (i)/(((n+1)**2)*((l_n_1(i))**2))
        if W not in c_k:  
            c_k = np.append(c_k,W)
    return c_k
print(GetWeightsGLag(20))