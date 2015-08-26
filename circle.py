#!/usr/bin/python

#getting the input from the user

def check(x):
 assert x>0, "Entered a negative number"

def area (x):
 check(x)
 return math.pi*(x**2)

def perimeter (x):
 check(x)
 return 2*math.pi*x  

import sys
import math

if __name__=="__main__":
#getting the input from the user
 x=float(sys.argv[1])

 print"area " " {}, perimeter" " {}".format(area(x),perimeter(x))

