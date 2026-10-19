import numpy as np
def norma(x,p): #ya probado
    res = 0
    i_p = []

    if p == 'inf':
        
        max = 0
        for i in range(len(x)):
            x_abs = abs(x[i])
            if x_abs > max:
                max = x_abs
        res = max

    else:
        for i in range(len(x)):
            x_i = abs(x[i])          
            x_i = x_i**p
            res += x_i
        res = res**(1/p)
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
    m,n = A.shape
    if m != n:
        return False
    A_tras = traspuesta(A)
    m,n = A.shape
    for i in range(m):
        for j in range(n):
            if abs(A[i,j] - A_tras[i,j]) > 1e-03:
                return False
    return True

def prod_exterior(A, B):

    m = len(A)
    n = len(B)
    
    res = np.zeros((m, n))
    
    # Multiplicamos elemento a elemento sin sumar nada
    for i in range(n):
        for j in range(n):
            res[i, j] = A[i] * B[j]
            
    return res

def metpot2k(A, tol=1e-15, K = 1000):
    n = A.shape[0] #A es cuadrada

    v = np.random.rand(n)
    v = v / norma(v,2)
    v_prima = (A@v)/norma(A@v,2)
    error = v_prima@v
    k = 0

    for _ in range(int(K)):
        if abs(abs(error) - 1)  < tol:
            break
        v_k = v_prima
        v_prima = (A@v_k)/norma(A@v_k,2)
        error = v_prima@v_k
        k += 1
    aval = (v_prima@A)@v_prima

    return v_prima, aval, k

def diagRH(A,tol = 1e-15,K = 1000):
    n = A.shape[0]

    if n == 1:
        return None, None

    if not esSimetrica(A):
        return None, None


    avec, aval, _ = metpot2k(A, tol, K)     

    I = np.eye(n)
    e1 = np.zeros(n)
    e1[0] = 1.0

    u = e1 - avec

    H = I - 2 * (prod_exterior(u,u))/(norma((u),2)**2)

    if n == 2:
        S = H
        D = (H@A)@(traspuesta(H))
    else:
        B = (H@A)@(traspuesta(H))
        A_prima = B[1:,1:]
        S_prima, D_prima = diagRH(A_prima,tol,K)

        D = np.zeros((n,n))
        D[0,0] = aval
        D[1:,1:] = D_prima

        aux = np.zeros((n,n))
        aux[0,0] = 1.0
        aux[1:,1:] = S_prima

        S = H@aux
    return S,D






