#!/usr/bin/python
import sys
import random
from random import uniform

def sphere (N, n):
    random.seed (n)
    sphereArea = 0
    for i in range (N):
        x = uniform (0, 1)
        y = uniform (0, 1)
        z = uniform (0, 1)
        if (x**2) + (y**2) + (z**2) <= 1:
            sphereArea += 1
    return 6 * float(sphereArea) / N


def circle (N, n):
    random.seed (n)
    circleArea = 0
    for i in range (N):
        x = uniform (0, 1)
        y = uniform (0, 1)
        if (x**2) + (y**2) <= 1:
            circleArea += 1
    return 4 * float(circleArea) / N

if __name__ == "__main__":
    seed1 = int (sys.argv[1])
    seed2 = int (sys.argv[2])
    print "circle-area pi: {}".format(circle (seed2, seed1))
    print "sphere-volume pi: {}".format(sphere (seed2, seed1))

"""
