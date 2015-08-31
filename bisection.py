#!/usr/bin/env python
import sys
import math
#from math import error

def g(x):
	h = x**2+2*x-5
	return h

def root(h,rangex,tol = 1.0e-9): # find the root of a function using bisection method
	a=rangex[0] 
	b=rangex[1]
	m = (a+b)*0.5
	ha = h(a)
	hb = h(b)
	 
	while (rangex[1] - rangex[0])*0.5 > tol:
		if ha == 0.0:
			return m
		if hb == 0.0:
			return b
		if ha*hb > 0.0:
			print ('....root is not bracketed....')
		if ha*h(m) < 0:
			return m
		if g(m) < 0:
			a = m 
		elif g(m) > 0:
			b = m
		elif g(m) == 0:
			return m
		else:
			pass
			
