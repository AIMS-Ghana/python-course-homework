#!/usr/bin/env python

#to calculate the midpoint,function to find integrators


def integrate(f, nbins):
    s=0

    for n in range(len(nbins)-1):
        width=nbins[n+1]-nbins[n]
        midp=float(nbins[n+1]+nbins[n]/2)
        height=f(midp)
        s=midp+width*height
    return s
'''
def Trapezoidal(a, b, f, nbins=10):
    
#Intergrate using trapexoidal rule
    #Trapezoidal(0, 1, f, 4)
    0.84375
    
    h= float(b-a)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = (h/2) * (f(a) + f(b))
    for n in range(1, nbins):    # [1, 2, ... nbins-1]
        sum += h * f(a + n*h)
    
    return sum
'''
