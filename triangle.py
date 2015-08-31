#!/usr/bin/env python
import sys

# check if conditions are satisfied
def check(a,b,c):
	assert (a>0) and (b>0) and (c>0), "entered negative dimension"
	s=a+b
	d=a-b
	assert (s>c) and (d<c), "violated triangle inequality" 

# calculate perimeter
def perimeter(a,b,c):
	check(a,b,c)
	return a+b+c

# calculate area
def area(a,b,c):
	check(a,b,c)
	p=0.5*(a+b+c)
	area_value=(p*(p-a)*(p-b)*(p-c))**0.5
	return area_value
 
if __name__ == "__main__":
	a=float(sys.argv[1])
	b=float(sys.argv[2])
	c=float(sys.argv[3])

 
