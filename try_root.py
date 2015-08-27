#!/usr/bin/python

import bisection

def bisectf(x):
    return((x-1)*(x+10)**2)

rangex = [0,10]
(u,v)=bisection.root(bisectf, rangex)
print"...bisection method, root of y=(x-1)(x+10)^2 on (0.10) result: ",v
