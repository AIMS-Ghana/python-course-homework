#!/usr/bin/env python

def integrate(f,rangex):
	summ=0.0
	# calculate the integral from a to b of function f using the midpoint rule
	for t in range (len(rangex)-1):
		b=float(rangex[t+1]-rangex[t])
		h=(rangex[t+1] + rangex[t]/2)
		assert h > 0
		summ=summ+b*h
		return summ
