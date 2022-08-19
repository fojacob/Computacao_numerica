import numpy as np

def gaussElimin(a, b):
    n = len(b)
  # Elimination Phase
    for k in range(0, n-1):
        for i in range(k+1, n):
          if a[i, k] != 0.0:
              lam = a[i, k]/a[k, k]
              a[i, k] = 0
              a[i, k+1:n] = a[i, k+1:n] - lam*a[k, k+1:n]
              b[i] = b[i] - lam*b[k]
    #arredondamento
    
    print("MATRIZ TRIANGULAR")
    print(a)
    print("--------------------------------")
    print("MATRIZ INDEPENDENTE")
    print(b)
    print("--------------------------------")
    print("MATRIZ COEFICIENTES")
    # Back substitution
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k+1:n], b[k+1:n]))/a[k, k]

    return b

x = [0.15,2.30,3.15,4.85,6.25,7.95]

z = np.array([[x[0]**5, x[0]**4, x[0]**3, x[0]**2, x[0]**1, 1],
              [x[1]**5, x[1]**4, x[1]**3, x[1]**2, x[1]**1, 1],
              [x[2]**5, x[2]**4, x[2]**3, x[2]**2, x[2]**1, 1],
              [x[3]**5, x[3]**4, x[3]**3, x[3]**2, x[3]**1, 1],
              [x[4]**5, x[4]**4, x[4]**3, x[4]**2, x[4]**1, 1],
              [x[5]**5, x[5]**4, x[5]**3, x[5]**2, x[5]**1, 1]])

y = np.array([[4.79867, 4.49013, 4.2243, 3.47313, 2.66674, 1.51909]])

d = gaussElimin(z, y[0])

print('x = \n', d)

