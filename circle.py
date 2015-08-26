#!/usr/local/bin/python
import sys 

def check(R):
	assert (R<=0) ,"negative dimension"

from math import pi

def perimeter(R):
	check(R)
	P = 2*pi*R
	return P

def area(R):
	check(R)
	A = 2*pi*R**2
	return A

if __name__ =="__main__":
	R = float(sys.argv[1])
	print ("perimeter is {}, /n area is {}".format(perimeter(R), area(R)))








