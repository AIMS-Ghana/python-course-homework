#!/usr/bin/env python

import math
pi=3.14
def check(area):
  	assert (area>0) , "enter positive  number"
	
  	
def  shape(area):
	check(area)
	if  a == "TRIANGLE":
 		side= math.sqrt((area*4)/math.sqrt(3))
		return side
	elif a== "SQUARE":
		side= math.sqrt(area)
		return side

	elif  a== "CIRCLE" :		
		radius = math.sqrt(area/pi)
			
			
  		return radius

import sys 

if __name__== "__main__":
   	a= str (sys.argv[1])
	area= float(sys.argv[2])
	if a=="TRIANGLE" or a== "SQUARE":
  	 	print "size:",shape(area)
	elif a== "CIRCLE":
 		print "raduis:",shape(area)


