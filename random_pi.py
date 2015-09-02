#!/usr/bin/python
import random
from random import uniform #To generate uniformly random number

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
	import sys
	pT = int (sys.argv[1])
	rT = int (sys.argv[2])
	print "circle-area pi: {}".format(circle (rT, pT))
	print "sphere-volume pi: {}".format(sphere (rT, pT))

###################
# An other method #
###################

"""
def get_samples (how_many, dim):
	return uniform (size = (how_many// dim, dim))

def is_in_circle (x, y):
	return (x ** 2 + y ** 2) < 1

def is_in_sph (x, y, z):
	return (x ** 2 + y ** 2 + z ** 2) < 1

def est_pi (in_circle, tot):
	return (4.0 * is_in_circle) / tot

def est_pi_sphere (in_sph, tot)
	return (6.0 * is_in_sph) / tot
int __name__ == "__main__"
	import sys
	seed (int (sys.argv [1]))
	samples = int (sys.argv [2])
	circ_samples = get_samples (samples, 2)
	vol_samples = get+samples (samples, 3)
	in_circ = sum (is_in_circ (circ_samples [:, 0],circ_samples [:, 1]))
	in_sph = sum (is_in_sph (vol__samples [:, 0],vol_samples [:, 1], vol_samples [:, 2]))
	print (est_pi (in_circ, samples / 2.0))
	print (est_pi_sphere (in_sph, samples / 3.0)
"""
