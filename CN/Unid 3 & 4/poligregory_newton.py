import numpy as np
import math
def PoliGregoryNewton (x, z, b):
    tam = len(z)
    u = (b-x[0])/(x[1]-x[0])
    for n in range (1, tam):
        for i in range (0, tam-n):
            z[i][n] = (z[i+1][n-1] - z[i][n-1])

    p = z[0][0]
    
    for i in range (1, tam):
        a = z[0][i]/math.factorial(i)
        for j in range (0, i):
            a = a * (u-j)
        p = p+a

    print("TABELA DE DELTA")
    print (z)
    print("------------------")
    print("Resultado")
    print (p)



x = [110, 120, 130]

delta = np.array([[2.041, 0.0, 0.0],
                  [2.079, 0.0, 0.0],
                  [2.114, 0.0, 0.0]])

b = 115

d = PoliGregoryNewton (x, delta, b)

