#!/usr/bin/python3
import math
import sys
def check (a,b,c):
	assert (a>0) & (b>0) & (c>0), "input positive numbers"
	s=a+b
	d=a-b
	assert (s>c) & (d<c), "input valid arguments"
def area(a,b,c):
	check (a,b,c)
	m= (a+b+c)/2
	area=(m*(m-a)*(m-b)*(m-c))**0.5 
	return (area)
def perimeter(a,b,c):
	check (a,b,c)
	return (a+b+c)
if __name__ == "__main__":
	a=float(sys.argv[1])
	b=float(sys.argv[2])
	c=float(sys.argv[3])
print ("area {}, perimeter {} ".format(area(a,b,c), perimeter(a,b,c)) )
