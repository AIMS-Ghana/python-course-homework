#!/usr/bin/python

import math

def integrate (f, l):
#l is a list (a, b)
#f is a function
	integration = 0
	longueur = l [1] - l[0]
	m = longueur / 100
	for i in range (longueur * 10):
		integration += m * f((i / 100) + m)

	return "{}".format (integration)	




