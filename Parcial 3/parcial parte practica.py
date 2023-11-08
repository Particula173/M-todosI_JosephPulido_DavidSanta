import numpy as np

M = np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b = np.array([1,2,3,4,5])
def conjugado (A,b,x_k,e=0.01):
    r_k = np.dot(A,x_k)-b
    p_k = -r_k
    k = 0
    while np.max(np.abs(r_k)) > e :
        al_k = -((np.dot(r_k.T,p_k))/(np.dot(p_k.T,np.dot(A,p_k))))
        x_k = x_k + np.dot(al_k,p_k)
        r_k = np.dot(A,x_k)-b
        beta_k = np.dot(r_k.T,np.dot(A,p_k)) / np.dot(p_k.T,np.dot(A,p_k))
        p_k = -r_k+np.dot(beta_k,p_k)
        k += 1
    print(k)
    return x_k
print(conjugado(M,b,np.array([1,1,1,1,1])))

print(np.linalg.solve(M,b))