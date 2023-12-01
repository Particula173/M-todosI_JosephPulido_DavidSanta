import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def f(x,y):
    func = np.array([[2*x - y - 2],[x + 2*y - 1],[x + y - 4]])
    rta = np.linalg.norm(func)
    return rta

h = 0.01
x = np.linspace(-5,5,1000)
y = np.linspace(-5,5,1000)

distancia = []
x_l = []
y_l = []
dmin = 10000

for i in range(len(x)):
    for j in range(len(y)):

        d = np.linalg.norm(f(x[i],y[j]))
        x_l.append(x[i])
        y_l.append(y[j])
        distancia.append(d)
        if d <= dmin:
            dmin = d
            xmin = x[i]
            ymin = y[j]


print(dmin)
print(xmin)
print(ymin)


def f(x, y):
    return np.array([[2*x - y - 2], [x + 2*y - 1], [x + y - 4]])


x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x, y)
Z = np.zeros([len(x), len(y)])
for i in range(len(x)):
    for j in range(len(y)):
        Z[i, j] = np.linalg.norm(f(x[i], y[j]))

axg = plt.figure(figsize=(6, 6)).add_subplot(projection='3d')
axg.plot_surface(X, Y, Z, cmap='coolwarm')
axg.view_init(azim=60, elev=30)

plt.show()