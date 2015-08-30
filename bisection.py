#!/usr/bin/python

import math

def root (f, l):
#l is a list (a, b)
#f is a function
	a = l [0]
	b = l [1]
	while abs (b - a) > 0.0001:
		m = float (b + a) / 2
		image = f (m)
		if (f (a) * image > 0):
			a = m
		if (image * f(b) > 0):
			b = m
	return b	




