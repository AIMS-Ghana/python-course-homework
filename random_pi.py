#!/usr/bin/puyhon
import sys
import numpy.random as npr
from numpy import reshape

seed = int(sys.argv[1])
npr.seed(seed)
n = int(sys.argv[2])
samples = npr.random_sample(n)
circ = reshape(samples, ())
