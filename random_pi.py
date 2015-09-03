#!/usr/bin/python
import sys
import random
from random import uniform

def circle_method(N, pts):
    random.seed (pts)
    count = 0
    for k in range (N):
        x = uniform (0, 1)
        y = uniform (0, 1)
        if (x ** 2) + (y ** 2) <= 1:
            count += 1
    return 4 * float(count) / N


def sphere_method(N, pts):
    random.seed (pts)
    counts = 0
    for k in range (N):
        x = uniform (0, 1)
        y = uniform (0, 1)
        z = uniform (0, 1)
        if (x ** 2) + (y ** 2) + (z ** 2) <= 1:
            counts += 1
    return 6 * float(counts) / N

if __name__ == "__main__":
    seed = int (sys.argv[1])
    samples = int (sys.argv[2])
    print "circle-area pi: {}".format(circle_method (samples, seed))
    print "sphere-volume pi: {}".format(sphere_method (samples, seed))
