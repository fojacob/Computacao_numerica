from numpy.linalg import norm
from numpy import array, zeros, diag, diagflat, dot
from copy import deepcopy
def jacobi(A,b,x):
                                                                                                                                               
    # Criar o vetor da diagonal dos elementos de A
    # Subtraí-los de A                                                                                                                                                                     
    D = diag(A)
    R = A - diagflat(D)
    erro = 10**(-2)
    contador = 0
    # Iterando...                                                                                                                                                                        
    while True :
        xa = deepcopy(x)
        x = (b - dot(R,x)) / D
        contador = contador + 1
        print('Iteracao',contador)
        print('Valor do x:',x)
        print('\n')
        if (norm(x-xa))/norm(x) < erro :
                return x,contador

E4 = array([[ 5.0, 1.0, 1.0 ],
            [3.0, 4.0, 1.0 ],
            [ 3.0,3.0, 6.0]])

e4 = array([5.0,6.0,0.0])

ap4 = array([0.0,0.0,0.0])

print(jacobi(E4,e4,ap4))
