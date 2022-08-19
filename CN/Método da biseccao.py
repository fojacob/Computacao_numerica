import math
def f(x):
    return math.cos(x)- x
def falsePosition(a,b,accuracy):
    i = 1
    count = 0
    booleano = True
    while booleano:
        x = (a+b)/2
        print('ITERACAO %d' %i)
        print('a = %0.5f, f(a) = %0.5f' % (a, f(a)))
        print('b = %0.5f, f(b) = %0.5f' % (b, f(b)))
        print('x = %0.5f, f(x) = %0.5f' % (x, f(x)))

        print('----------------------------')
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

        i = i + 1
        count = count + 1
        booleano = count != 4
        #booleano = abs(f(x)) > accuracy

    print('\nA raiz final eh: %0.4f' % x)

falsePosition(0,3,0.00001)
