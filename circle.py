#!/usr/bin/python3
from math import pi
def area(r):
	check (r)
	
	area=pi*(r**2)
	return area
def perimeter(r):
    	check (r)
	perimeter=2*pi*r
	return perimeter
def check (r):
	assert (r>0) , "input positive numbers"
       
	
import sys
if __name__ == "__main__":
        r=float(sys.argv[1])
  	
print ("area {}, perimeter {} ".format(area(r), perimeter(r)) )
