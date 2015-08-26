#!/usr/bin/python
import math

def check (a, b):
	assert (a > 0) and (b > 0), "Negative dimension" 

def perimeter (a, b):
	check (a, b)
	return 2*a + 2*b

def area (a, b):
	check (a, b)
	return a * b


	
import sys

if __name__ == "__main__":
    a = float (sys.argv [1])
    b = float (sys.argv [2])
    print "area {}, perimeter {}".format (area (a, b), perimeter (a, b))
