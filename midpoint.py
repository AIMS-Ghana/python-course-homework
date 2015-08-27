#!/usr/bin/python

import math

def integrate (a, b):
#b is a list
#a is an interger
	integration = 0

	for i in b:
		integration = integration + a * math.exp((i / 10) + (float (a) + (float (a) / 2))

	return "midpoint method, area under e^x on (0, 10), 100 points: {}".format (integration)	




