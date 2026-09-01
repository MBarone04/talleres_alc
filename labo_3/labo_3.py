import numpy as np

def norma(x,p):
    res = 0
    i_p = []

    if p == 'inf':
        max = 0
        for i in range(len(x)):
            if abs(x[i]) > max:
                max = abs(x[i])
        res = max

    else:
        for i in range(len(x)):
            x_i = abs(x[i])
            if p == 'inf':
                x_i = max(x)
            else:    
                x_i = pow(x_i,p)
            i_p.append(x_i)

        for i in range(len(i_p)):
            res += i_p[i]
        res = pow(res,1/p)
        return res


assert(np.allclose(norma(np.array([1,1]),2),np.sqrt(2)))
assert(np.allclose(norma(np.array([1]*10),2),np.sqrt(10)))
assert(norma(np.random.rand(10),2)<=np.sqrt(10))
assert(norma(np.random.rand(10),2)>=0)

def normaliza(X,p):
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
#for x in normaliza([np.random.rand(k) for k in range(1,11)],'inf'):
 #   assert( np.allclose(norma(x,'inf'),1) )
print(norma([np.random.rand(k) for k in range(1,11)],'inf'))
