#!/usr/bin/python

# check for conditions

def check(a,b):
	assert a>0 and b>0 , "entered negative dimension"

	

# calculate the Perimeter
def perimeter(a,b):
	check(a,b)
	p = 2*(a+b)
	return p


# calculate the area
def area(a,b):
	check(a,b)
	f=a*b
	return f

import sys

if __name__ == "__main__":

	if len(sys.argv)==3:
		a = float(sys.argv[1])
		b = float(sys.argv[2])
		print("area {}, perimerter {}".format(area(a,b),perimeter(a,b)))

	elif len(sys.argv)==2:
		a = float(sys.argv[1])
		b = float(sys.argv[1])
		print("area {}, perimerter {}".format(area(a,b),perimeter(a,b)))
	
	
	





	

