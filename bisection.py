#!/usr/bin/python

def root(func, endpoint, tol=0.001, peak=100):
    a, b = endpoint
    fa = func(a)
    fb = func(b)

    assert fa*fb < 0 
    midpt = (a+b)/2
    f_midpt = func(midpt)
    if (f_midpt) < tol or (peak== 0):
        return midpt
    elif fa*f_midpt < 0:
        return root(func,[a,midpt])
    else:
        return root(func, [midpt,b])
