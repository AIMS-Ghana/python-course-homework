#!/usr/bin/python
import math
import numpy as np
import midpoint
import time


def root(a, b):
	tol=0.001
	for n in range(len(b)-1):
		c = (b[n]+b[n+1])/2.0
		d =	a(c)
		while (b[n]-b[n+1])/2.0 > tol:
			if f(c) == 0:
				return c
			elif a(b[n])*d < 0:
				b[n+1] = c
			else :
				b[n] = c
		
		return c
	

