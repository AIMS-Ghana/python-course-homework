#!/usr/bin/python

import sys
import math
def f(x):
	return x**3 + x -1
	
def bisection(a,b,tol):
	d = (a+b)/2.0
	while (b-a)/2.0 > tol:
		if f(d) == 0:
			return d
		elif f(b)*f(d) < 0:
			b = d
		else :
			m = d
		d = (a+b)/2.0
		
	return d
	
