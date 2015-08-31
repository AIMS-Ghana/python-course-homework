#!/usr/bin/python

def root(funct, endpt, TOL=0.001, MAX=100):
    a, b = endpt
    fa = funct(a)
    fb = funct(b)

#check if end points have same sign
    assert fa*fb < 0 
    midpt = (a+b)/2
    fmidpt = funct(midpt)
    if (fmidpt) < TOL or (MAX == 0):
        return midpt
    elif fa*fmidpt < 0:
        return root(funct,[a,midpt])
    else:
        return root(funct, [midpt,b])
