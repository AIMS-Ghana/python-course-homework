#!/usr/bin/env python
from numpy.random import uniform, seed

def pick_seed(amount, dim): # pick random seed
	return uniform(size=(amount//dim,dim))

def is_in_circle(x,y): 
	return (x**2+y**2) <= 1 # seed in circle when x**2+y**2 < 1 holds

def is_in_sphere(x,y,z):
	return (x**2+y**2+z**2) < 1 # seed in sphere when x**2+y**2+z**2 < 1 holds

def est_pi(in_circle, out_circle): # function that estimates the value of pi by circle area method
        return float(4*in_circle)/float(out_circle)

def est_pi_sph(is_in_sphere,out_sphere): # function that estimates the value of pi by shere-volume method
	return 6.0*float(is_in_sphere)/float(out_sphere)

if __name__ =="__main__":
	import sys
	assert len(sys.argv) == 3, "missing values"
	seed(int(sys.argv[1]))
	samples = int(sys.argv[2])
	circle_samples = pick_seed(samples,2)
	vol_samples = pick_seed(samples,3)
	in_circle = sum(is_in_circle(circle_samples[:,0],circle_samples[:,1]))
        in_sphere = sum(is_in_sphere(vol_samples[:,0], vol_samples[:,1], vol_samples[:,2]))
	print "points in circle :",in_circle
	print "value Est: pi = ",est_pi(in_circle, samples//2)
	print "points in sphere: ",in_sphere
	print "value Est: pi = ",est_pi_sph(in_sphere,float(samples)/float(3))
