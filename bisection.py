#!/usr/bin/python

import sys
import math

'''def f(x):
	return x**3 + x -1
'''	
def root(f, V, tol=0.0000001, max_n=100):
	a = V [0]
	b = V [1]
	#if f(c) == 0.0:
		#return c
	while abs (b-a) > tol:
		c = float (a+b) / 2
		if f(a)*f(c) < 0:
			b = c
		if f(b)*f(c) < 0:
			a = c
	return a
	
def main(argv):
	if (len(sys.argv) != 4):
		sys.exit('Usage: bisection.py <a> <b> <tol>')
	
	print 'The root is: ',
	print root(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]))

if __name__ == "__main__":
	main(sys.argv[1:])





