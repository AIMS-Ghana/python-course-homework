#!/usr/bin/env python

#Bisection method 
def root(f, endpt, tol=0.001, N_max=100):
    a, b = endpt
    fa = f(a)
    fb = f(b)
#check if end points have same sign
    assert fa*fb < 0 
    midp = (a+b)/2
    fmidp = f(midp)
    if (f(midp)) < tol or (N_max== 0):
    	return midp
    elif fa*fmidp < 0:
    	return root(f,[a, midp])
    else:
   	return root(f,[midp,b])



