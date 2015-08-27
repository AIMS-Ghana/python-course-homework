#!/usr/bin/python
import math
import sys
	 
def f(a):
	return  math.exp(a)   

def bisection(x,y):
	z = (x+y)/2.0
	if f(z) == 0:
		return z
	elif f(a)*f(z) < 0:
	        y = z
	 else :
	        x = z
	        z = (x+y)/2.0
         
	 return z
