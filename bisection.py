#!/usr/bin/python

import math

def root (f, l):
#l is a list (a, b)
#f is a function
	solution = 0
	while (l [1] - l [0]) > 0.1:
		m = float (l [0] + l [1]) / 2
		image = f (m)
		if (f (l [0]) * image > 0):
			a = m
		if (image * f(l [1]) > 0):
			b = m
	return "[{}, {}]".format (a, b)	




