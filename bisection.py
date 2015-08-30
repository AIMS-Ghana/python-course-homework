#!/usr/bin/python

import sys
	 
def f(x):
	return x**3 + x -1     

def root(a,b):
	c = (a+b)/2.0
	if f(c) == 0:
		return c
	elif f(a)*f(c) < 0:
	        b = c
	 else :
	        a = c
	        c = (a+b)/2.0
         
	 return c
