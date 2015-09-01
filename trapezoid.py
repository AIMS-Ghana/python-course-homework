#!/usr/bin/env python
import math
import sys
import numpy as np

a=rangex[0]
b=rangex[1]
def integrate(f,rangex) :
	h=(b-a)/float(n)
	z=0.5*(f(a)+f(b))     
	for i in range(1,n) :
		z=z+f(a+i*h)
	return h*z
