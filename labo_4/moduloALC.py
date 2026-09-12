#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eliminacion Gausianna
"""
import numpy as np

def traspuesta(A): #ya probada
    m,n = A.shape
    res = np.zeros((n,m))

    for i in range(m):
        for j in range(n):
            res[j,i] = A[i,j]
    return res 

def diagonal(A): #ya probada
    m, n = A.shape

    res = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i == j:
                res[i,j] = A[i,j]
    return res

def esSimetrica(A): #ya probada
    if A is None:
        return False
    A_tras = traspuesta(A)
    m,n = A.shape
    for i in range(m):
        for j in range(n):
            if abs(A[i,j] - A_tras[i,j]) > 1e-03:
                return False
    return True

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

    x = [0.0]* L.shape[0]

    if inferior:
        for i in range(L.shape[0]):
            suma = 0.0
            for j in range(i):
                suma += x[j]*L[i][j]
            x[i] = (b[i] - suma)/L[i][i]
    else:
        for i in range(L.shape[0]-1,-1,-1):
            suma = 0.0
            for j in range(i+1,L.shape[0]):
                suma += x[j]*L[i][j]
            x[i] = (b[i] - suma)/L[i][i]
    return x

def inversa(A): #YA PROBADO
    L, U, _ = calculaLU(A)   

    if L is None:
        return None
    n = L.shape[0]
    id = np.eye(n)
    A_inv = np.zeros((n,n))

    for i in range(n):
        y = res_tri(L,id[i],inferior = True)
        A_inv[i] = res_tri(U,y,inferior = False)
    A_inv = traspuesta(A_inv)

    return A_inv

def calculaLDV(A): #YA PROBADA
    L,U, _ = calculaLU(A)

    if L is None:
        return None, None, None
    
    U_tras = traspuesta(U)
    V_t,D, _  = calculaLU(U_tras)
    if V_t is None:
        return None, None, None
    V = traspuesta(V_t)

    return L, D, V

def esSDP(A,atol=1e-10):
    if A is None:
        return False

    if not esSimetrica(A):
        return False  
    _,D,_ = calculaLDV(A)

    if D is None:
        return False

    for i in range(D.shape[0]):
        if D[i][i] < atol:
            return False
    return True


    
    
        

                
          
    
    

          
     
    
