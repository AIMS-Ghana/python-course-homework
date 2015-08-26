#!/usr/bin/python

def check(a,b):
	assert (a>0) & (b>0), "entered negative dimension"

def area(a,b):
	check(a,b)
	return a*b

def perimeter(a,b):
	check(a,b)
	res = ((2*a)+(2*b))
	return res

import sys

if __name__ == "__main__":

	if len(sys.argv) == 3:
		a = float (sys.argv[1])
		b = float (sys.argv[2])
		print("Area {}, Perimeter {}".format(area(a,b), perimeter (a,b))) 
	
 
   	elif len(sys.argv) == 2:
		a = float (sys.argv[1])
		b = float (sys.argv[1])
 
		print("Area {}, Perimeter {}".format(area(a,b), perimeter (a,b))) 
	
