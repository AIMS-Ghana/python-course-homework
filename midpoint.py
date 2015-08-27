#!/usr/bin/python
 
def f(x):
    return 0.5 + x*x

def midpoint(a, b, f, nbins=10):

    h = float(b-a)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = 0.0
    x = a + h/2
    while (x < b):
         sum += h* f(x)
         x += h

    return sum

     
