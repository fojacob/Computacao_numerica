import numpy as np

def lagrange(x, y, a):
  n = len(x)
  S = 0

  for i in range(0,n):
    print(y[i], end='')
    for j in range(0,n):
      if(i!=j):
        y[i] = y[i] * ((a-x[j]) / (x[i] - x[j]))
        print(" * (%.1f - %.1f)/(%.1f - %.1f)"%(a,x[j],x[i],x[j]), end='')
    S = S + y[i]
    print("")
  return S

x = [0, 2, 3]
y = [7, 11,28]
a = 1


print (lagrange(x, y, a))
