#!/usr/bin/python
import sys 
import math

def check(R):
	assert (R>0) ,"negative dimension"

def perimeter(R):
	check(R)
	return 2*R*3.14

def area(R):
	check(R)
	return 2*3.14*R**2

if __name__ == "__main__":
	R = float(sys.argv[1])
	print ("perimeter is {0}, area is {1}".format(perimeter(R) , area(R)))







