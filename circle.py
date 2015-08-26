#!/usr/bin/python

def check(r):
	assert r>0, "entered negative dimension"

import math

# calculate the Perimeter
def perimeter(r):
	check(r)
	cir =2*math.pi*r
	return cir

 

# calculate the area
def area(r):
	check(r)
	res =math.pi*r**2 
	return res

import sys

if __name__ == "__main__":
	r = float(sys.argv[1])
	

print("area {}, perimerter {}".format(area(r),perimeter(r)))



