#!/usr/bin/python
import sys

	
def root(rangex, bisectf):
	tol=0.001
	for x in range(0,20):
		c = (rangex[x]+rangex[x+1])/2.0
		b = bisectf(c)
		while (rangex[x+1]-rangex[x]) > tol:
			if b == 0:
				return c
			elif b < 0:
				rangex[x] = c
			elif b > 0:
				rangex[x+1]= c	
			
		return c
	

