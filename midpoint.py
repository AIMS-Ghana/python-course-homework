#!/usr/bin/python
import math
import sys
#calculate the midpoint using the midpoint rule

def integrate(f, rangex):
	m=0.0
	for n in range(len(rangex)-1):
		w=rangex[n+1]-rangex[n]
		mid_point=float(rangex[n+1]+rangex[n]/2)
		height=f(mid_point)
		m=mid_point+w*height
	return m


