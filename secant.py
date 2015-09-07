#!/usr/bin/python
from math import fabs
#recursive function 
#This method is just the Newton method but with a little changes.
def secante(xm, xn,f):
    if(fabs(xm-xn)<=10e-10):
        return xn
    else:
        return secante(xn, xn - (xn - xm)/(f(xn) - f(xm))*f(xn) , f)
