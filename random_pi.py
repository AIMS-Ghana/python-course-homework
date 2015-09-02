#!/usr/bin/python


import random
import sys
import numpy as np

n = int(sys.argv[2])
seed = int(sys.argv[1])


def circle_area(seed, n):
	random_points = []
        random.seed(seed)
	for i in np.arange(0, n+1):
		x = random.random()
		y = random.random()
		a = (x,y)
		random_points.append(a)

	#print random_points
	count = 0.0
	for j in random_points:
		if (j[0])**2 + (j[-1])**2 <= 1:
			count = count + 1
		else:
			pass
	print count
	pi = (count/n)*4
	print "circle area pi :", pi


def sphere_volume(seed, n):
	random_points = []
        random.seed(seed)
	for i in np.arange(0, n+1):
		x = random.random()
		y = random.random()
		z = random.random()
		a = (x,y,z)
		random_points.append(a)

	#print random_points
	count = 0.0
	for j in random_points:
		if (j[0])**2 + (j[1])**2 + (j[-1])**2 <= 1:
			count = count + 1
		else:
			pass
	print count
	pi = (count/n)*6
	print "sphere volume pi :", pi

circle_area(seed, n)
sphere_volume(seed, n)
