import sympy as sp
x=sp.symbols("x")
y=sp.symbols("y")
f=2*(x+2*y)/3

comprobation = sp.integrate(sp.integrate(f,(x,0,1)),(y,0,1))

g_m = sp.integrate(f,(y,0,1))
h_m = sp.integrate(f,(x,0,1))

Val_x=sp.integrate(x*g_m,(x,0,1))
Val_y=sp.integrate(y*h_m,(y,0,1))

Cova=sp.integrate(sp.integrate(x*y*f,(x,0,1)),(y,0,1))
Cova = Cova-Val_x*Val_y

sig =sp.integrate(sp.integrate((x-Val_x)*(y-Val_y)*f,(x,0,1)),(y,0,1))
 
print (f"Si integramos la funcion en el dominio y como resultado da 1 significa que esta normalizada lo que implica que es una funcion de probabilidad. El valor de la integra es : {comprobation} por lo tanto decimos que si se trata de una funcion de probabilidad.")
print(f"Las funciones de probabilidad marginales son {g_m} y {h_m}.")
print(f"El valor esperado x es: {Val_x}. El valor esperado de y es : {Val_y}.")
print(f"Si con los valores esperados calculamos una covarianza el resultado es : {Cova}")
print(f"La covarianza calculada segun la definición es: {sig}. Dado que el valor de la covariacia teorica es diferente de cero, no se presenta una dependencia entre X y Y")