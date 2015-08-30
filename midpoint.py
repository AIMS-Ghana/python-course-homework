#!/usr/bin/python3

import numpy as np

def integrate(f,rangex):
	accumulator = 0
	for i in range(1,100,1):
		Ii = (rangex[i] - rangex[i-1])*f((rangex[i-1] + rangex[i])/2.0)
		accumulator = accumulator + Ii
	return accumulator


if __name__ == "__main__":
	print (integrate(np.exp, np.linspace(0, 10, 100, endpoint=True)))
