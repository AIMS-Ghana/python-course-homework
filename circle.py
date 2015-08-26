#!/usr/bin/python3

import math

def check(r):
   assert (r>0), "Negative number entered"

def area(r):
   check(r)

   A = math.pi*r**2
    	
   return A

def perimeter(r):
   check(r)
   p = 2*math.pi*r
   return p



import sys

if __name__ == "__main__":
	r = float(sys.argv[1])
	
	print ("area {}, \nperimeter {}".format(area(r), perimeter(r)))


