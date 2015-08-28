#!/usr/bin/env python

#calculate bisection 

def f(midp):
	return x**3 + x -1
	
def bisection(rangex[0], rangex[1],tol):
	a=rangex[0], 
	b=rangex[1]
	c = (a+b)/2.0
	while (b-a)/2.0 > tol:
		if f(c) == 0:
			return c
		elif f(a)*f(c) < 0:
			b = c
		else :
			a = c
		c = (a+b)/2.0
		
	return c

