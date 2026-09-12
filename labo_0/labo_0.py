import numpy as np

def esCuadrada(A): #ya probada
    m, n = A.shape

    return m == n


def triangSup(A): #no esta en modulo
    m,n = A.shape
    res = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i < j:
                res[i,j] = A[i,j]
    return res


def triangInf(A): #no esta en modulo
    m,n = A.shape
    res = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i > j:
                res[i,j] = A[i,j]
    return res


def diagonal(A): #ya probada
    m, n = A.shape

    res = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i == j:
                res[i,j] = A[i,j]
    return res


def traza(A): #ya probada
    res = 0
    m,n = A.shape
    if not esCuadrada(A):
        return 0
    else:
        for i in range(m):
            res += A[i,i]
    return res


def traspuesta(A): #ya probada
    m,n = A.shape
    res = np.zeros((n,m))

    for i in range(m):
        for j in range(n):
            res[j,i] = A[i,j]
    return res 


def esSimetrica(A): #ya probada
    if A is None:
        return False
    A_tras = traspuesta(A)
    res = True
    m,n = A.shape
    for i in range(m):
        for j in range(n):
            if A[i,j] != A_tras[i,j]:
                res = False
                break
    return res

    





        
        
