#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eliminacion Gausianna
"""
import numpy as np

def calculaLU(A):
    if A is None:
            return None, None, 0 
    
    cant_op = 1
    m=A.shape[0]
    n=A.shape[1]
    Ac = A.copy()
    
    if m!=n:
        return None, None, 0
    else:
        L = np.eye(m)
        for i in range(m):
            if Ac[i][i] == 0:
                return None, None, 0
            for k in range(i+1,m):
                L[k][i] = Ac[k][i]/Ac[i][i]
                cant_op +=1
                for j in range(i,n): 
                    Ac[k][j] = Ac[k][j] - L[k][i]*Ac[i][j]
                    cant_op += 1
        U = Ac
        cant_op += 1   
    return L, U, cant_op


def res_tri(L,b,inferior = True):
    m,n = L.shape
    x = []
    if inferior:
        for i in range(m):
            for j in range(n):
                x_i = 

          
     
    
