#!/usr/bin/python
import sys
def root(funcntion, endpoint, tol=0.001, n=100):
    a, b = endpoint
    fa = funcntion(a)
    fb = funcntion(b)

    assert fa*fb < 0 
    h= (a+b)/2
    f_h = funcntion(midpoint)
    if (f_h) < tol or (n== 0):
        return h
    elif fa*f_h < 0:
        return root(funcntion,[a,h])
    else:
        return root(funcntion, [h,b])
