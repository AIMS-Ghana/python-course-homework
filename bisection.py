#!/usr/bin/python

def root(bisectf, rangex):
	tol=0.001
	for x in range(len(rangex)-1):
		c = (rangex[x]+rangex[x+1])/2.0
		b =	bisectf(c)
		while (rangex[x+1]-rangex[x])> tol:
			if bisectf(c) == 0:
				return c
			elif b < 0:
				rangex[x] = c
			else:
				rangex[x+1] = c
			
		return c
