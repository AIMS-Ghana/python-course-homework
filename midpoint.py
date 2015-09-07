#!/usr/bin/python
import numpy as np
def integrate (f, l):
#l is a list (a, b)
#f is a function
	integration = 0
	m = abs (l [-1] - l [0]) / 100.0
	p = abs (l [-1] - l [0]) * 10
	for i in l:
		integration += m * f(i + m)

	return integration
	
#####################
# An another method #
#####################

"""
def midpoint(f, a, b, n):
    deltaX = (b-a)/n
    start = a + deltaX/2
    end = b - deltaX/2
    mids = np.linspace(start, end, n)
    fs = f(mids)
    fsum = np.sum(fs)
    return deltaX*fsum
"""
