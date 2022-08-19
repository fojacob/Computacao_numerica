from numpy.linalg import norm
import numpy as np
from copy import deepcopy

def seidel(A, b, x):

    L = np.tril(A)
    U = A - L
    contador = 0
    #erro = 5*10**(-2)
    
    while True:
        xa = deepcopy(x)
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        contador = contador + 1
        print(x, contador, 'Mx=', (norm(x-xa))/norm(x))
        if contador == 4:
            return x, contador
        #if (norm(x-xa))/norm(x) < erro :
                #return x,contador

A = ([[ 4.0, -1.0, 1.0 ],
      [-1.0, 4.0, -2.0 ],
      [ 1.0,-2.0, 4.0]])

b = ([12.0,-1.0,5.0])

x = ([0.0,0.0,0.0])

print(seidel(A,b,x))
