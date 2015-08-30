#!/usr/bin/python

import math

def check(radius):
    assert (radius > 0),"entered negative radius"

def area(radius):
    check(radius)
    res = (radius**2) * math.Pi
    return res

def perimeter(radius):
    check(radius)
    t = 2 * math.Pi * radius
    return t

import sys

if __name__=="__main__":

    radius = float(sys.argv[1])

print(" area {} \n perimeter {}".format(area(radius),perimeter(radius)))

