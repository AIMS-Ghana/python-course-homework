#!/usr/bin/python

def checkdim(r):
        assert r >= 0, "Passed negative radius"
       	pass
 
from math import pi
 
def area(r):
	checkdim(r)
	return pi*(r**2)
 
def perimeter(r):
	checkdim(r)
        return 2*pi*r
 
import sys
if __name__ == "__main__":
	r = float(sys.argv[1])
	print("area {} \nperimeter {}".format(area(r),perimeter(r)))

