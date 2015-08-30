#!/usr/bin/python

import math

def integrate (f, l):
#l is a list (a, b)
#f is a function
	a = l [0]
	b = l [-1]
	integration = 0
	longueur = abs (b - a)
	m = longueur / 100
	p = longueur * 10
	for i in l:
		integration += m * f(i + m)

	return integration	




