#!/usr/bin/python

import math

def  equilateralTRIANGLE (A):
	from math import sqrt
	x = sqrt((4*A)/sqrt(3))
	return x
	assert (A <=0 ), "verify your number"

	
def SQUARE (A):
	from math import sqrt
	C = sqrt(A)
	return C 
	assert ( A<=0 ), "verify your number"

def CIRCLE (A):
	from math import sqrt
	from math import pi
	R = sqrt(A/pi)
	return R
	assert (A<=0), "verify your number"

import sys

if __name__ == "__main__":
	A= float(sys.argv[1])
	print ("equilateralTRIANGLE {},\n side {}".format(equilateralTRIANGLE(A), side(x))
	print ("SQUARE{},\n side {}".format(SQUARE(A), side(C)))
	print ( " CIRCLE {},\n radium {}".format (CIRCLE(A), radium(r)))
