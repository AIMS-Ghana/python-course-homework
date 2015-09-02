#!/usr/bin/python

def root(fxn, endpt, tol=0.001, Max=100):
    a, b = endpt
    fa = fxn(a)
    fb = fxn(b)
#check if end points have same sign
    assert fa*fb < 0 
    midp = (a+b)/2
    fmidp = fxn(midp)
    if (fmidp) < tol or (Max== 0):
        return midp
    elif fa*fmidp < 0:
        return root(fxn,[a,midp])
    else:
        return root(fxn, [midp,b])
