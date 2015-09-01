#!/usr/bin/python
import sys
import random
from random import uniform

def circle (N, Pt):
	random.seed (Pt)
	A = 0
	for i in range (N):
		xT = uniform (0, 1)
		yT = uniform (0, 1)
		if (xT ** 2) + (yT ** 2) <= 1:
			A += 1
	return 4 * float(A) / N


def sphere (N, Pt):
	random.seed (Pt)
	B = 0
	for i in range (N):
		xT = uniform (0, 1)
		yT = uniform (0, 1)
		zT = uniform (0, 1)
		if (xT ** 2) + (yT ** 2) + (zT ** 2) <= 1:
			B += 1
	return 6 * float(B) / N

if __name__ == "__main__":
	pT = int (sys.argv[1])
	rT = int (sys.argv[2])
	print "circle-area pi: {}".format(circle (rT, pT))
	print "sphere-volume pi: {}".format(sphere (rT, pT))

