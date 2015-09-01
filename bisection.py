#!/usr/bin/python

def root(bisectf, rangex):
	tol=0.001
	for x in range(len(rangex)-1):
		c = (rangex[x]+rangex[x+1])/2.0
		b =	bisectf(c)
		while (rangex[x]-rangex[x+1])/2.0 > tol:
			if f(c) == 0:
				return c
			elif bisectf(rangex[x])*b < 0:
				rangex[x+1] = c
			else :
				rangex[x] = c
		
		return c
	

