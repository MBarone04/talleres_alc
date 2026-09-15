### Funciones L05-QR
import numpy as np
def esCuadrada(A): #ya probada
    m, n = A.shape

    return m == n

def mult_vectorial(a,b):
    if a == [] or b == []:
        return 0
    elif len(a) != len(b):
        return 0
    res = 0
    for i in range(len(a)):
        res += a[i]*b[i]
    return res

def norma(x,p): #ya probado
    res = 0
    
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

def normaliza(X,p): #ya probado
    res = []
    for i in range(len(X)):
        vect = X[i]
        norma_vect = norma(vect,p)

        vect_normalizado = vect / norma_vect
        res.append(vect_normalizado)

    return res



def QR_con_GS(A,tol=1e-12,retorna_nops=False):

    if not esCuadrada(A):
        if retorna_nops:
            return None, None, 0
        else: 
            return None, None
    m,n = A.shape
    Q = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            a_i = A[:,i]
            a_i = normaliza(a_i,2)
            q = Q[:,i]
            q_i = a_i - (mult_vectorial(a_i,q)*q)
        Q[:,i] = q_i
    if retorna_nops:
        return None, None, 0
    else:
        return None, None


    """
    A una matriz de n x n 
    tol la tolerancia con la que se filtran elementos nulos en R
    retorna_nops permite (opcionalmente) retornar el numero de operaciones realizado
    retorna matrices Q y R calculadas con Gram Schmidt (y como tercer argumento opcional, el numero de operaciones).
    Si la matriz A no es de n x n, debe retornar None
    """

def QR_con_HH(A,tol=1e-12,extras=False):
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

# Tests L05-QR:

import numpy as np

# --- Matrices de prueba ---
A2 = np.array([[1., 2.],
               [3., 4.]])

A3 = np.array([[1., 0., 1.],
               [0., 1., 1.],
               [1., 1., 0.]])

A4 = np.array([[2., 0., 1., 3.],
               [0., 1., 4., 1.],
               [1., 0., 2., 0.],
               [3., 1., 0., 2.]])

# --- Funciones auxiliares para los tests ---
def check_QR(Q,R,A,tol=1e-10):
    # Comprueba ortogonalidad y reconstrucción
    assert np.allclose(Q.T @ Q, np.eye(Q.shape[1]), atol=tol)
    assert np.allclose(Q @ R, A, atol=tol)

# --- TESTS PARA QR_by_GS2 ---
Q2,R2 = QR_con_GS(A2)
check_QR(Q2,R2,A2)

Q3,R3 = QR_con_GS(A3)
check_QR(Q3,R3,A3)

Q4,R4 = QR_con_GS(A4)
check_QR(Q4,R4,A4)

# --- TESTS PARA QR_by_HH ---
Q2h,R2h = QR_con_GS(A2)
check_QR(Q2h,R2h,A2)

Q3h,R3h = QR_con_HH(A3)
check_QR(Q3h,R3h,A3)

Q4h,R4h = QR_con_HH(A4)
check_QR(Q4h,R4h,A4)

# --- TESTS PARA calculaQR ---
Q2c,R2c = calculaQR(A2,metodo='RH')
check_QR(Q2c,R2c,A2)

Q3c,R3c = calculaQR(A3,metodo='GS')
check_QR(Q3c,R3c,A3)

Q4c,R4c = calculaQR(A4,metodo='RH')
check_QR(Q4c,R4c,A4)