#!/usr/bin/python

# check for conditions
def check(a,b,c):
	assert a>0 and b>0 and c>0, "entered negative dimension"
	s=a+b
	d=a-b
	assert (s>c) and (d<c), "violated triangle inequality"

# calculate the Perimeter
def perimeter(a,b,c):
	check(a,b,c)
	return a+b+c

# calculate the area
def area(a,b,c):
	check(a,b,c)
	t = 0.5*(a+b+c)
	res = (t*(t-a)*(t-b)*(t-b))**0.5
	return res

import sys

if __name__ == "__main__":
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	c = float(sys.argv[3])

print("area {0}, perimerter {1}".format(area(a,b,c,),perimeter(a,b,c)))






