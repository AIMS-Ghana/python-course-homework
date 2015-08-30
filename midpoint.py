#!/usr/bin/python
import math
import sys
#calculate the midpoint using the midpoint rule

def integrate(f, nbins):
	m=0.0
	for n in range(len(nbins)-1):
		w=nbins[n+1]-nbins[n]
		mid_point=float(nbins[n+1]+nbins[n]/2)
		height=f(mid_point)
		d=m+w*height
	return d
