#!/usr/bin/python3
import sys
import math


def integrate(f, *args):
    
    nbins=100
    #nbins=len(args)
    a = args[0][0]
    
    b = args[0][1]
   
    h = float(b - a)/float(nbins)
    assert h > 0
    
   
    sum = 0.0
    x = a + h/2                  # first midpoint
    while (x < b):
        sum += h * f(x)
        x += h

    return sum

if __name__ == "__main__":

    def func(x):
     return x - x**2

    xrange = [0,1]
    print(integrate(func,xrange))
    
