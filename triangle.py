#!/usr/bin/env python

#check for negative numbers and triangle inequality

def check(x,y,z):
	s= x+y
	d=x-y
	assert x>0 and y>0 and z>0 , "Please input non negative numbers"
	assert (s>z) and (d<z), "invalid input - triangle inequality"
# calculate area
def area(x,y,z):
	check(x,y,z)
	sum_value=(x+y+z)/2
    	area_value=math.sqrt(sum_value*(sum_value-x)*(sum_value-y)*(sum_value-z))
    	return area_value
#calculate perimeter
def perimeter(x,y,z):
	check (x,y,z)
    	perimeter_value=x+y+z
   	return perimeter_value
import sys
import math
if __name__ == "__main__":
	x=float(sys.argv[1])
	y=float(sys.argv[2])
	z=float(sys.argv[3])
	#print values
	print ("area is {}, perimeter is {}".format(area(x,y,z), perimeter(x,y,z)))


