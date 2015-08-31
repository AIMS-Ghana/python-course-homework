#!/usr/bin/python

import numpy as np

def integrate(f,rangex):
	accumulator = ((rangex[-1] - rangex[0])/(2.0*len(rangex)))*(f(rangex[0]) + f(rangex[-1]))
	for i in range(1, 98):
		accumulator = accumulator + ((rangex[-1] - rangex[0])/float(len(rangex)))*f(rangex[i])
	return accumulator

if __name__ == "__main__":
	print (integrate(np.exp, np.linspace(0, 10, 100, endpoint=True)))

