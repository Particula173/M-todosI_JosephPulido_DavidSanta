import sympy as sp
import numpy as np
x = sp.symbols('x',real=True)

def GetHermitRecursive(n,x):

    if n==0:
        poly = sp.Number(1)
    elif n==1:
        poly = 2*x
    else:
        poly = (2*x*(GetHermitRecursive(n-1,x)))-(2*(n-1)*(GetHermitRecursive(n-2,x)))
    return sp.expand(poly,x)
print(GetHermitRecursive(7,x))
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
def GetDHermit(n,x):
    Pn = GetHermitRecursive(n,x)
    return sp.diff(Pn,x,1)
def GetAllRootsHermit(n):
    j=np.sqrt(4*n+1)
    xn = np.linspace(-j,j,100)
    
    Hermit = []
    DHermit = []
    
    for i in range(n+1):
        Hermit.append(GetHermitRecursive(i,x))
        DHermit.append(GetDHermit(i,x))
    
    poly = sp.lambdify([x],Hermit[n],'numpy')
    Dpoly = sp.lambdify([x],DHermit[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots
def getHermitWeight (n):
    l_n_1 = sp.lambdify(x,GetHermitRecursive(n+1,x),"numpy")
    x_k = GetAllRootsHermit(n)
    c_k = np.array([])
    for i in x_k:
        W = ((2**(n-1))*(sp.factorial(n))*(np.sqrt(np.pi)))/((n**2)*((GetHermitRecursive((n-1),x))**2))
        if W not in c_k:  
            c_k = np.append(c_k,W)
    return c_k
def GetHermiteWR(n):
    
    R,W = GetAllRootsHermit(n) , getHermitWeight(n)
    
    return (R,W)

def NpolinomiosHermite(n):
    
    for i in range(1,n+1):
        
        wr = GetHermiteWR(i)
        
        print('Polinomio n° ' + str(i))
        print(GetHermitRecursive(i,x))
        print(wr[0])
        print(wr[1])
        
nh = 20

NpolinomiosHermite(nh)


def function(x):
    return x**4

def IntegralHermite(f,n):
    
    res = 0
    
    r,w = GetHermiteWR(n)
    
    for i in range(len(r)+1):
        
        res += w[i]*f(r[i])
    
    return res*(2/np.sqrt(np.pi))

print(IntegralHermite(function,20))