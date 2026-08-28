import numpy as np


def error(x,y): #ya probado
    x_float64 = np.float64(x)
    y_float64 = np.float64(y)

    res = np.abs(x_float64-y_float64)

    return res


def error_relativo(x,y): #ya probado
  
    res = np.abs(error(x,y)/x)

    return res

def matricesIguales(A,B): #ya probado
    a,b = A.shape
    c,d = B.shape

    if a != c:
        return False
    elif b != d:
        return False
    else:
        res = True
        for i in range(a):
            for j in range(b):
                if error(A[i][j],B[i][j]) > 1e-15:
                    res = False
                    break
    return res


def sonIguales(x,y,atol=1e-08):
    return np.allclose(error(x,y),0,atol=atol)

assert(not sonIguales(1,1.1))
assert(sonIguales(1,1 + np.finfo('float64').eps))
assert(not sonIguales(1,1 + np.finfo('float32').eps))
assert(not sonIguales(np.float16(1),np.float16(1) + np.finfo('float32').eps))
assert(sonIguales(np.float16(1),np.float16(1) + np.finfo('float16').eps,atol=1e-3))

assert(np.allclose(error_relativo(1,1.1),0.1))
assert(np.allclose(error_relativo(2,1),0.5))
assert(np.allclose(error_relativo(-1,-1),0))
assert(np.allclose(error_relativo(1,-1),2))

assert(matricesIguales(np.diag([1,1]),np.eye(2)))
assert(matricesIguales(np.linalg.inv(np.array([[1,2],[3,4]]))@np.array([[1,2],[3,4]]),np.eye(2)))
assert(not matricesIguales(np.array([[1,2],[3,4]]).T,np.array([[1,2],[3,4]])))




