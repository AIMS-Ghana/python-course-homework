#!/usr/bin/python

def integrate (f, l):
#l is a list (a, b)
#f is a function
	a = l [0]
	b = l [-1]
	integration = 0
	m = abs (b - a) / 100,0
	p = abs (b - a) * 10
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


