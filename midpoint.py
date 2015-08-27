#!/usr/bin/python

import math
import sys
def integrate(a,b):
	m=0.0
	for n in range(len(b)-1):
		w=b[n+1]-b[n]
		midpoint=float(b[n+1]+b[n]/2)
		h=a(midpoint)
		t=m + w*h
	return t
