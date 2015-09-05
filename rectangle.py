#!/usr/bin/python
import math
def area(a,b):
	check (a,b)
	area=(a*b)
	return area
def perimeter(a,b):
    	check (a,b)
	perimeter=2*(a+b)
	return perimeter
def check (a,b):
	assert (a>0) & (b>0), "input positive numbers"
import sys
if __name__ == "__main__":
        a=float(sys.argv[1])
  	b=float(sys.argv[2])
print ("area {}, perimeter {} ".format(area(a,b), perimeter(a,b)) )
