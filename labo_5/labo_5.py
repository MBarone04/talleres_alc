### Funciones L05-QR
import numpy as np
def esCuadrada(A): #ya probada
    m, n = A.shape

    return m == n

def mult_vectorial(a,b):

    if len(a) != len(b):
        return 0
    res = 0
    for i in range(len(a)):
        res += a[i]*b[i]
    return res

def traspuesta(A): #ya probada
    m,n = A.shape
    res = np.zeros((n,m))

    for i in range(m):
        for j in range(n):
            res[j,i] = A[i,j]
    return res 

def mult_matricial(A,B):
    a,b = A.shape
    c,d = B.shape

    res = np.zeros((a,d))

    for i in range(a):
        for j in range(d):
            num = 0
            for k in range(b):
                num += A[i,k]*B[k,j]
            res[i,j] = num

    return res

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

def QR_con_GS(A,tol=1e-12,retorna_nops=False):

    if not esCuadrada(A):
        if retorna_nops:
            return None, None, 0
        else: 
            return None, None
    m,_ = A.shape
    Q = np.zeros((m,m))
    num_ops = 0

    for i in range(m):
        v_i = A[:,i].copy()
        u_i = Q[:,i]
        for j in range(i): 
            u_j = Q[:,j]
            v_i -= (mult_vectorial(v_i,u_j)/mult_vectorial(u_j,u_j))*u_j
            num_ops += 1
        v_i = v_i/norma(v_i,2)
        for elem in range(len(v_i)):
            if abs(v_i[elem]) < tol:
                v_i[elem] = 0
        Q[:,i] = v_i

    Q_t = traspuesta(Q)
    R = mult_matricial(Q_t,A)

    if retorna_nops:
        return Q, R, 0
    else:
        return Q, R


    """
    A una matriz de n x n 
    tol la tolerancia con la que se filtran elementos nulos en R
    retorna_nops permite (opcionalmente) retornar el numero de operaciones realizado
    retorna matrices Q y R calculadas con Gram Schmidt (y como tercer argumento opcional, el numero de operaciones).
    Si la matriz A no es de n x n, debe retornar None
    """

def QR_con_HH(A,tol=1e-12,extras=False):
    m,n = A.shape

    if m < n:
        return None, None

    Q = A.copy()
    R_matrices = {}
    Q_matrices = {}
    for i in range(m):
        u_i = A[i :,i].copy()
        id = np.eye(m)
        u_t = traspuesta(u_i)
        H = id - (2*mult_matricial(u_i,u_t)/mult_matricial(u_t,u_i))
        Q = mult_matricial(H,A)
    



    """
    A una matriz de m x n (m>=n)
    tol la tolerancia con la que se filtran elementos nulos en R
    retorna matrices Q y R calculadas con reflexiones de Householder
    Si la matriz A no cumple m>=n, debe retornar None
    extras : bool, opcional
        Si es True, devuelve informacion extra sobre el proceso de factorizacion.
        Por defecto es False. Esto lo hacemos para poder graficar el proceso.
    Devuelve la factorizacion QR de A usando reflectores de Householder.
    Devuelve: 
        Q, R, extra_info (si extras es True)
        Q, R (si extras es False)
    extra_info es un diccionario con la clave:
        'R_matrices': lista de las matrices R en cada paso
        'Q_matrices': lista de las matrices Q en cada paso


    """
def calculaQR(A,metodo='RH',tol=1e-12):
    """
    A una matriz de n x n 
    tol la tolerancia con la que se filtran elementos nulos en R    
    metodo = ['RH','GS'] usa reflectores de Householder (RH) o Gram Schmidt (GS) para realizar la factorizacion
    retorna matrices Q y R calculadas con Gram Schmidt (y como tercer argumento opcional, el numero de operaciones)
    Si el metodo no esta entre las opciones, retorna None
    """




A2 = np.array([[1., 2.],
               [3., 4.]])

A3 = np.array([[1., 0., 1.],
               [0., 1., 1.],
               [1., 1., 0.]])

A4 = np.array([[2., 0., 1., 3.],
               [0., 1., 4., 1.],
               [1., 0., 2., 0.],
               [3., 1., 0., 2.]])

Q,R = QR_con_GS(A2,tol=1e-12,retorna_nops=False)
print(Q@R)



