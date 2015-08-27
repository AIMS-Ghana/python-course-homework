#!/usr/bin/python
from math import *
import sys
def integrate(a,b):
	l=0.0
	for n in range(len(b)-1):
		width=b[n+1]-b[n]
		midpoint= float(b[n+1]+b[n]/2)
		height= a(midpoint)
		r=l+(width*height)
	return r
 	
		
	
