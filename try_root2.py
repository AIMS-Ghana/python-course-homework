#!/usr/bin/python
import math
import sys
#secant method
def root(f, interval, tol=1e-5, steps=100)
	b0,b1=interval
	d=b1-b0
	f0(b0)
	f1=f(b1)
	if (f1<=tol)or (steps==0):
		return b1
	else:
	m=f1-f0
	bn=b1-f1*d/m
		
	
