#!/usr/bin/env python
import sys
import math
#from math import error

def f(x):
	return x**3+3*x-5

def root(f,rangex,tol = 1.0e-9): # find the root of a function using bisection method
	a=rangex[0] 
	b=rangex[1]
	m = (a+b)*0.5
	fa = f(a)
	fb = f(b)
	if fa == 0.0:
		return m
	if fb == 0.0:
		return b
	if fa*fb > 0.0:
		print ('....root is not bracketed....')
	while (rangex[1] - rangex[0]) < tol:
		if f(m) < 0:
			a = m 
		elif f(m) > 0:
			b = m
		elif f(m) == 0:
			return m
		else:
			pass
			
