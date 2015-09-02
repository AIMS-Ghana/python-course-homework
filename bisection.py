#!/usr/bin/python
import sys
import math

def root(f, x):
	def bisect(a,b,tol):
		tol = 0.001
		c = (a+b)/2.0
#		for n in range(len(b)-1):
#			c = (b[n] + b[n+1])/2.0
#			d = a(c)
		while (b-a)/2.0 > tol:
			if f(c) == 0:
				return c
			elif f(a)*f(c) < 0:
				b = c
			else:
				a = c
		return c

if __name__  =="__main__":

	main(sys.argv[1:])
	print 'The root is: '
	print bisection(int((sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]))
