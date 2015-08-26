#!/usr/bin/env python

import math

pi=3.14
def check(a):
  	assert (a>0)  , "enter positive  number"
	
  	
def perimeter(a):
	check(a)
 	p=2*a*pi #perimeter of circle
  	return p
def area(a):
   	check(a)
   
   	res= a*a*pi # area of circle 
   
   	return res 
import sys 

if __name__== "__main__":
   	a= float(sys.argv[1])
  	print ("area {}, perimeter {}".format(area(a),perimeter(a)))
