 #!/usr/bin/env python

# check if condition is satisfied
def check(r):
	assert (r>0), "entered negative dimension"

import math
	  
# calculate perimeter
def perimeter(r):
	check(r,)
	return 2*math.pi*r

# calculate area
def area(r):
	check(r,)
	return math.pi*r**2

import sys
 
if __name__ == "__main__":
	r=float(sys.argv[1])
	 
 

