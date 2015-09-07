#!/usr/bin/python

def integrate (f, l):
#l is a list (a, b)
#f is a function
	a = l [0]
	b = l [-1]
	integration = 0
	m = abs (b - a) / 100
	p = abs (b - a) * 10
	for i in l:
		integration += m * f((i / 100) + m)

	return integration	

#####################
# An another method #
#####################

"""
def trapezoid(f, a, b, n):
    deltaX = (b-a)/n
    points = np.linspace(a, b, n+1)
    fpoints = f(points)
    res = fpoints[0]+fpoints[-1]+2*np.sum(fpoints[1:-1])
    return res * deltaX/2
"""

