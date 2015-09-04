#!/usr/bin/python
import math


def root(f, rangex,tol=0.001):
	a=rangex[0]
	b=rangex[1]
	while (b-a)>tol:
	    c = (a+b)/2.0
	    if f(c) == 0:
	       return c
	    elif f(a)*f(c)<0:
	       return c
	    elif f(b)*f(c)<0:
	       return c
	    else :
	        pass

