import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Sigmoid.csv")

data = df.to_numpy()

x = data[:,0]
y = data[:,1]


def M(x,t):
    return t[0]/(t[1] + np.exp(-t[2]*x))

#función costo
def Fun_cost(x,y,t,n):
    valor = 0
    for i in range(n):
        valor += (y[i] - M(x[i],t))**2
    return valor

def grad_Fun_cost(x,y,theta,n=10000):

    gradiente= np.zeros(3)

    da, db, dc = 0.,0.,0.
    for i in range(n):

        da += -2*((y[i] - M(x[i],theta))*(1/(theta[1] + np.exp(-theta[2]*x[i]))))
        db += -2*((y[i] - M(x[i],theta))(-1*theta[0]/((theta[1] + np.exp(-theta[2]*x[i]))*2)))
        dc += -2*((y[i] - M(x[i],theta))(theta[0]*np.exp(-theta[2]*x[i])*x[i]/((theta[1] + np.exp(-theta[2]*x[i]))*2)))

    gradiente[0]= da
    gradiente[1]= db
    gradiente[2] =dc

    return gradiente

N = len(x)
theta= np.array([0,0,0])
e = 0.01
num_e = 10000
gamma = 5e-4
values = np.zeros((num_e,3))

for i in range(num_e):
    g = grad_Fun_cost(x,y,theta,N)
    theta =theta - gamma*g/(np.sum(g*2)*(1/2))
    values[i] = theta
    
param = values[-1]
print(param)


plt.plot(values)
plt.show()



plt.scatter(x,y)

x0 = np.linspace(-10,10,100)
plt.plot(x0,M(x0,param),color="red")
plt.show()