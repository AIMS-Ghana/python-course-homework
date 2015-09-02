#!/usr/bin/python

import math

def root (f, l):
#l is a list (a, b)
#f is a function
	a = l [0]
	b = l [1]
	while abs (b - a) > 0.0001:
		m = b + a / 2.0
		if (f (a) * f (m) > 0):
			a = m
		if (f (m) * f(b) > 0):
			b = m
	return b	




