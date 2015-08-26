#!/usr/bin/python
import math

def area(r):


	area=(math.pi*(r**2))
	return area
def perimeter(r):

	perimeter=(2*(math.pi)*(r))
	return perimeter
def check (r):
	assert (r>0),"entered negative dimension"
	

import sys 
if __name__ == "__main__":
	if len(sys.argv) == 2:
    		r= float(sys.argv[1])
	
	elif len(sys.argv) == 2:
    		a= float(sys.argv[1])
    		b= float(sys.argv[1])
print ("area {0}, perimeter {1}".format (area(r),perimeter(r)))

 













