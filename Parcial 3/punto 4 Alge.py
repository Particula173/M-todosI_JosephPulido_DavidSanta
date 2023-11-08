# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:16:22 2023

@author: david
"""
import numpy as np
A=np.array([[1,0,0],[5,1,0],[-2,3,1]])
B=np.array([[4,-2,1],[0,3,7],[0,0,2]])

Creal=np.dot(A,B)
C=np.zeros((3,3))

summ=0
for n in range(np.shape(A)[0]):
    for m in range(np.shape(A)[1]):
        for i in range(3):
            summ+=A[n][i]*B[i][m]
        C[n][m]=summ
        summ=0
    summ=0
        
print(Creal)
    