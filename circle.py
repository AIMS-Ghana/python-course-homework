#!/usr/bin/python

def check(r):
	assert r>0, "entered negative dimension"
	
import math
def area(r):
	check(r)
	area=math.pi*r**2
	return area
def perimeter(r):
	check(r)
	perimeter=2*math.pi*r
	return perimeter


import sys 
if __name__ == "__main__":
	r= float(sys.argv[1])
	
	
	print ("area {}, perimeter {}".format (area(r),perimeter(r)))

 













