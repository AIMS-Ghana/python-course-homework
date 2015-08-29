#!/usr/bin/python3
import sys
import math
def f(x):
	return x**3 + x -1
	
def bisection(a,b,tol):
	c = (a+b)/2.0
	while (b-a)/2.0 > tol:
		if f(c) == 0:
			return c
		elif f(b)*f(c) < 0:
			b = c
		else :
			m = c
		c = (a+b)/2.0
		
	return c
	

