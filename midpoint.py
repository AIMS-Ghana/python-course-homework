#!/usr/bin/python

def integMid(a, b, f, nbins=10):
    '''Return the integral from a to b of function f using the midpoint rule

    >>> integMid(0, 1, f, 4)
    0.828125
    '''
    h = float(b-a)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = 0.0
    x = a + h/2                  # first midpoint
    while (x < b):
        sum += h * f(x)
        x += h

    return sum



