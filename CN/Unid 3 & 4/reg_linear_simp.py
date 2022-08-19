def regressaoLinearSimples(vetor_x,vetor_y):
  n = len(vetor_x)
  sx = sum(vetor_x)
  sy = sum(vetor_y)
  xy = 0
  for i in range(0,n):
    xy = xy + (vetor_x[i] * vetor_y[i])

  sQuadradoX = 0
  for i in range(0,n):
    sQuadradoX = sQuadradoX + vetor_x[i]**2

  print('sx: %.4f' %sx)
  print('sy: %.4f' %sy)
  print('xy: %.4f' %xy)
  print('sQuadradoX: %.4f' %sQuadradoX)

  print("--------------------")
  
  print("sx*sy: %.4f" %(sx*sy))
  print("(sx*sy)/n): %.4f" %((sx*sy)/n))
  print(" xy - ((sx*sy)/n): %.4f" %( xy - ((sx*sy)/n)))

  print("--------------------")

  print("(sx**2): %.4f" %((sx**2)))
  print("(sx**2)/n): %.4f" %((sx**2)/n))
  print("sQuadradoX - ((sx**2)/n): %.4f" %(sQuadradoX - ((sx**2)/n)) ) 


  #b = ( xy - ((sx*sy)/n) )  / (sQuadradoX - ((sx**2)/n))
  b = ( (sx*sy)- (n*xy) )  / ((sx**2) - (n*sQuadradoX))
  print('b: %.4f' %b)

  a = (sy - (b * sx))/n 

  print("--------------------")
  print("y = %.4f + (%.4f)x" %(a,b))


x = [0, 1, 2, 2.5, 3]
y = [2.9, 3.7, 4.1, 4.4, 5]

regressaoLinearSimples(x,y)
