#!/usr/bin/python

import math
import random
from numpy.random import uniform, seed

def get_samples(how_many, dim):
    return uniform(size=(how_many/dim, dim))

def is_in_circ(x, y):
    return (x**2 + y**2)
def is_in_sph(x, y, z):
    return (x**2 + y**2 + z**2) < 1

def est_pi(in_circ, tot):
    return float(4.0*in_circ)/float(tot)

def est_pi_sphere(in_sph, tot):
    return float(6.0*in_sph)/float(tot)

if __name__ =="__main___":
    import sys
    seed = int(sys.argv[1])
    samples = int(sys.argv[2])
    circ_samples = get_samples(samples, 2)
    vol_samples = get_samples(samples, 3)
    in_circ = sum(is_in_circ(circ_samples[1,0], circ_samples[1,1]))
    in_sph = sum(is_in_sph(vol_samples[1,0], vol_samples[1,1], vol_samples[1,2]))
    
    print(est_pi(in_circ, samples/2))
    print(est_pi_sphere(in_sph, samples/3))






