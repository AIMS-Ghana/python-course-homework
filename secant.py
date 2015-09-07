#!/usr/bin/python

import math

def root (f, l):
#l is a list (a, b)
#f is a function
	a = l [0]
	b = l [1]
	while abs (b - a) > 0.00001:
		c =b - ( float (b - a) / (f (b) - f (a))) * (f (b))
		image = f (c)
		if (f (a) * image > 0):
			a = c
		if (image * f(b) > 0):
			b = c
	return b	




