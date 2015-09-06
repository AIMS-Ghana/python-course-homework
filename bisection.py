#!/usr/bin/python

import sys

	
def root(f,rangex, tol=0.005):
	a=rangex[0]
	b=rangex[1]
	c = (a+b)*0.5
	assert (b-a)*0.5 > tol
	if f(c) == 0:
		return c
	elif f(a)*f(c) < 0:
		b = c
	else :
		a = c
	return c
