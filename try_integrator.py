#!/usr/bin/python
from math import exp
import midpoint

def intf(x):
    return(exp(x))
rangex = range(100)
print"...midpoint method, area under e^x on (0,10), 100 points:",midpoint.integrate(intf, rangex)


