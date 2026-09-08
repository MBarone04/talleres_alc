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


assert(np.allclose(norma(np.array([1,1]),2),np.sqrt(2)))
assert(np.allclose(norma(np.array([1]*10),2),np.sqrt(10)))
assert(norma(np.random.rand(10),2)<=np.sqrt(10))
assert(norma(np.random.rand(10),2)>=0)

def normaliza(X,p): #ya probado
    res = []
    for i in range(len(X)):
        vect = X[i]
        norma_vect = norma(vect,p)

        vect_normalizado = vect / norma_vect
        res.append(vect_normalizado)

    return res



for x in normaliza([np.array([1]*k) for k in range(1,11)],2):
    assert(np.allclose(norma(x,2),1))
for x in normaliza([np.array([1]*k) for k in range(2,11)],1):
    not np.allclose(norma(x,2),1) 
for x in normaliza([np.random.rand(k) for k in range(1,11)],'inf'):
    assert( np.allclose(norma(x,'inf'),1) )

def normaMatMC(A, q , p ,Np):
    max_norma = 0
    for _ in range(Np):
        x = np.array(np.random.rand(A.shape[1]))

        den = norma(x,p)
        if den == 0:
            continue
        x_norm = x / den
        Ax = A@x_norm
        num = norma(Ax,q)
        
        norma_Ax = num
        
        if norma_Ax > max_norma:
            max_norma = norma_Ax
            res_x = x_norm
        
    
    return max_norma, res_x


nMC = normaMatMC(A=np.eye(2),q=2,p=1,Np=100000)
assert(np.allclose(nMC[0],1,atol=1e-3))
assert(np.allclose(np.abs(nMC[1][0]),1,atol=1e-3) or np.allclose(np.abs(nMC[1][1]),1,atol=1e-3))
assert(np.allclose(np.abs(nMC[1][0]),0,atol=1e-3) or np.allclose(np.abs(nMC[1][1]),0,atol=1e-3))

nMC = normaMatMC(A=np.eye(2),q=2,p='inf',Np=100000)
assert(np.allclose(nMC[0],np.sqrt(2),atol=1e-3))
assert(np.allclose(np.abs(nMC[1][0]),1,atol=1e-3) and np.allclose(np.abs(nMC[1][1]),1,atol=1e-3))

A = np.array([[1,2],[3,4]])
nMC = normaMatMC(A=A,q='inf',p='inf',Np=1000000)
#assert(np.allclose(nMC[0],normaExacta(A,'inf'),rtol=2e-1)) 


def normaExacta(A, p=1):
    m,n = A.shape
    max_suma_col = 0
    max_suma_fila = 0

    if p == 1:
        for j in range(n):
            suma_col = 0
            for k in range(m):
                suma_col += abs(A[k][j])
            if suma_col > max_suma_col:
                max_suma_col = suma_col
        return max_suma_col
    elif p == 'inf':
        for i in range(m):   
            suma_fila = 0
            for k in range(n):
                suma_fila += abs(A[i][k])
            if suma_fila > max_suma_fila:
                max_suma_fila = suma_fila
        return max_suma_fila
    else:
        return None

assert(np.allclose(normaExacta(np.array([[1,-1],[-1,-1]]),1),2))
assert(np.allclose(normaExacta(np.array([[1,-2],[-3,-4]]),1),6))
assert(np.allclose(normaExacta(np.array([[1,-2],[-3,-4]]),'inf'),7))
assert(normaExacta(np.array([[1,-2],[-3,-4]]),2) is None)
assert(normaExacta(np.random.random((10,10)),1)<=10)
assert(normaExacta(np.random.random((4,4)),'inf')<=4)

def condMC(A,p,Np): #ya probado
    A_inv = np.linalg.inv(A)

    norma_A = normaMatMC(A,p,p,Np)[0]
    norma_A_inv = normaMatMC(A_inv,p,p,Np)[0]

    return norma_A*norma_A_inv

A = np.array([[1,1],[0,1]])
A_ = np.linalg.solve(A,np.eye(A.shape[0]))
normaA = normaMatMC(A,2,2,10000)
normaA_ = normaMatMC(A_,2,2,10000)
condA = condMC(A,2,10000)
assert(np.allclose(normaA[0]*normaA_[0],condA,atol=1e-3))

A = np.array([[3,2],[4,1]])
A_ = np.linalg.solve(A,np.eye(A.shape[0]))
normaA = normaMatMC(A,2,2,10000)
normaA_ = normaMatMC(A_,2,2,10000)
condA = condMC(A,2,10000)
assert(np.allclose(normaA[0]*normaA_[0],condA,atol=1e-3))
print(normaA[0]*normaA_[0],condA)


def condExacta(A,p): #ya probada
    A_inv = np.linalg.inv(A)

    norma_A = normaExacta(A,p)
    norma_A_inv = normaExacta(A_inv,p)

    return norma_A*norma_A_inv

A = np.random.rand(10,10)
A_ = np.linalg.solve(A,np.eye(A.shape[0]))
normaA = normaExacta(A,1)
normaA_ = normaExacta(A_,1)
condA = condExacta(A,1)
assert(np.allclose(normaA*normaA_,condA))

A = np.random.rand(10,10)
A_ = np.linalg.solve(A,np.eye(A.shape[0]))
normaA = normaExacta(A,'inf')
normaA_ = normaExacta(A_,'inf')
condA = condExacta(A,'inf')
assert(np.allclose(normaA*normaA_,condA))



