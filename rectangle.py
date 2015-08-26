#!/usr/bin/env python

import math
def check(a,b):
  	assert (a>0) and (b>0) , "enter positive  number"
	
  	
def perimeter(a,b):
	check(a,b)
 	p=(a+b)*2 #perimeter
  	return p
def area(a, b):
   	check(a,b)
   
   	res= a*b # heron's formula
   
   	return res 
import sys 

if __name__== "__main__":
   	a= float(sys.argv[1])
   	b= float(sys.argv[2])
  	print ("area {}, perimeter {}".format(area(a,b),perimeter(a,b)))
