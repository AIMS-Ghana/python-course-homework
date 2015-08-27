#!/usr/bin/python3
import sys
import math
def integrate(a,b):
	sum= 0.0
	for n in range(len(b)-1):
		midpoint= float(b[n+1]+[n]/2)
		width= b[n+1]-b[n]
		height= a(midpoint)
		k= sum + height*width
	return k
