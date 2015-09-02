#!/usr/bin/python

from numpy.random import uniform, seed

def get_samples(how_many, dim):
    return uniform(size=(how_many//dim, dim))

def is_in_circ(x, y):
    return (x**2 + y**2) < 1

def is_in_sph(x, y, z):
    return(x**2 + y**2 + z**2) < 1
    return (4.0*in_circ) / tot

def est_pi(in_circ, tot):
    return(4*0*in_cir) / tot

def est_pi_sphere(in_sph, tot):
    return (6.0*in_sph) / tot
if __name__ == "__main":
    import sys
    seed(int(sys.argv[1]))
    samples = int(sys.argv[2])
    circ_samples = get_samples(samples, 2)
    vol_samples = get_samples(samples, 3)
    in_circ = sum(is_in_circ(circ_samples[:,0], circ_samples[:,1]))
    in_sph = sum(is_in_sph(vol_samples[:,0], vol_samples[:,1], vol_samples[:,2]))
    print(est_pi(in_circ, samples//2))
    print(est_pi_sphere(in_circ, samples//2))

        
