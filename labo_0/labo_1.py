import numpy as np

def esCuadrada(A):
    m, n = A.shape

    return m == n


def triangSup(A):
    m,n = A.shape
    res = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i < j:
                res[i,j] = A[i,j]
    return res


def triangInf(A):
    m,n = A.shape
    res = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i > j:
                res[i,j] = A[i,j]
    return res


def diagonal(A):
    m, n = A.shape

    res = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i == j:
                res[i,j] = A[i,j]
    return res


def traza(A):
    res = 0
    m,n = A.shape
    if not esCuadrada(A):
        return 0
    else:
        for i in range(m):
            res += A[i,i]
    return res


def traspuesta(A):
    m,n = A.shape
    res = np.zeros((n,m))

    for i in range(m):
        for j in range(n):
            res[j,i] = A[i,j]
    return res 


def esSimetrica(A):
    A_tras = traspuesta(A)
    res = True
    m,n = A.shape
    for i in range(m):
        for j in range(n):
            if A[i,j] != A_tras[i,j]:
                res = False
                break
    return res

    


a = np.array([[1,2,3],[2,5,6],[3,6,9]])

print(a)



        
        
