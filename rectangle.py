#!/usr/bin/python3

import sys
import math

def check(L,l):
	assert (L>0) & (l>0),"entered negative dimension"

def area (L,l):
	#check(L,l)
	return L*l

def perimeter (L,l):
	check(L,l)
	return (L+l)*2
	
import sys
if __name__ == "__main__":
	L = float (sys.argv[1])
	l = float(sys.argv[2])
  
	print ("The area is {},\n The perimeter is {}".format(area(L,l), perimeter(L,l)))


