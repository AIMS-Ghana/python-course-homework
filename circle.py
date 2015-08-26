#!/usr/bin/python

def check(a):
	assert (a>0), "entered negative dimension"

def area(a):
	check(a)
	return 3.14*(a**2)

def perimeter(a):
	check(a)
	return 2*3.14*a

import sys

if __name__ == "__main__":
	a = float (sys.argv[1])
	print("Area {}, Perimeter {}".format(area(a), perimeter(a)))
