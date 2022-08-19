import numpy as np

def LUdecomp(a): #Transforma a matriz a em uma matriz formada por L & U
    global count
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
           if a[i,k] != 0.0:
               lam = a [i,k]/a[k,k]
               a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n] 
               a[i,k] = lam
               count += 1
    return a

def LUsolve(a,b):
    global count
    n = len(a)
    for k in range(1,n): #Substituições sucessivas de L para encontrar Y
        b[k] = b[k] - np.dot(a[k,0:k],b[0:k])
        count += 1
    b[n-1] = b[n-1]/a[n-1,n-1]

    for k in range(n-2,-1,-1): #Substituições retroativas de U para encontrar X
       b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
       count += 1
    return b

count = 0
z = np.array([[3.50, 2.77, -0.76, 1.80],
             [-1.80, 2.68, 3.44, -0.09],
             [0.27, 5.07, 6.90, 1.61],
              [1.71, 5.45, 2.68, 1.71]])

k = np.array([[7.31, 4.23, 13.85, 11.55]])

z = LUdecomp(z)
x = LUsolve(z,k[0])

print('x = \n', x)

print(count)
