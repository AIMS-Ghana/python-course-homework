#!/usr/bin/env python

import math
def check(a,b,c):
  	assert (a>0) and (b>0) and (c>0), "enter positive  number"
	s=a+b 
  	d=a-b
  	assert (s>c) and (d<c), "violated triangle "
def perimeter(a,b,c):
	check(a,b,c)
 	p=a+b+c
  	return p
def area(a, b,c):
   	check(a,b,c)
   	v=(a+b+c)/2
   	res= math.sqrt(v*(v-a)*(v-b)*(v-c)) # heron's formula
   
   	return res 
import sys 

if __name__== "__main__":
   	a= float(sys.argv[1])
   	b= float(sys.argv[2])
   	c= float(sys.argv[3])
	print 6
  	print ("area {}, perimeter {}".format(area(a,b,c),perimeter(a,b,c)))
