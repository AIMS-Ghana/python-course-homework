#!/usr/bin/env python
import sys
# calculate the area of the rectangle
def area(a,b):
	return a*b

if __name__ == "__main__":

 	a=float(sys.argv[1])
	b=float(sys.argv[2])
	
elif len(sys.argv) == 2:

	a=float(sys.argv[1])
	b=float(sys.argv[1])
	print a*b

else:
	print "wrong input"

