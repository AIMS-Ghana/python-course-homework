#!/usr/bin/env python

# check if conditions are satisfied
def check(a,b):
	assert (a>0) and (b>0), "entered negative dimension"
	  
# calculate perimeter
def perimeter(a,b):
	check(a,b)
	return (a+b)*2

# calculate area
def area(a,b):
	check(a,b)
	return a*b

import sys
 
if __name__ == "__main__":

	if len(sys.argv) == 3:
 
		a=float(sys.argv[1])
		b=float(sys.argv[2])

	elif len(sys.argv) == 2:

		a=float(sys.argv[1])
		b=float(sys.argv[1])

print ("area {0}\nperimeter {1}".format(area(a,b),perimeter(a,b)))

if len(sys.argv) >3: 
	print ("wrong input! only two values required!")

elif len(sys.argv) == 1:
	print ("wrong input! two values required!")
 
      
