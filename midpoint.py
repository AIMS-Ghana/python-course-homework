#!/use/bin/env python

def import(m, l, n, nbins=10):
    h = float(l-m)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = 0.0
    x = m + h/2                  # first midpoint
    while (x < l):
        sum += h * f(x)
        x += h

    return sum

