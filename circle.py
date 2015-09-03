#!/usr/bin/python3
# Calculate the area and perimeter of a circle, given its radius
from math import pi


def perimeter(r):
    check(r)
    return 2*pi*r


def area(r):
    check(r)
    return pi*r*r


def check(r):
    assert (r > 0), "Where do you find circles with negative radii?"
    pass

if __name__ == "__main__":
    import sys
    assert (len(sys.argv) == 2), "I need exactly one radius."
    r = float(sys.argv[1])
    print("area {}".format(area(r)))
    print("perimeter {}".format(perimeter(r)))
