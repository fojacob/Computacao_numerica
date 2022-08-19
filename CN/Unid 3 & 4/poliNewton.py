import numpy as np

def PoliNewton (x, z, b):
    tam = len(z)
    for n in range (1, tam):
        for i in range (0, tam-n):
            z[i][n] = (z[i+1][n-1] - z[i][n-1])/ (x[i+n] - x[i])

    p = z[0][0]
    
    for i in range (1, tam):
        a = z[0][i]
        for j in range (0, i):
            a = a * (b-x[j])
        p = p+a

    print("TABELA DE DELTA")
    print (z)
    print("------------------")
    print("Resultado")
    print (p)



x = [-9, -8, -7, -6]

delta = np.array([[9.9, 0.0, 0.0, 0.0],
                  [11.7, 0.0, 0.0, 0.0],
                  [17.6, 0.0, 0.0, 0.0],
                  [18.2, 0.0, 0.0, 0.0]])

b = -7.5

d = PoliNewton (x, delta, b)
