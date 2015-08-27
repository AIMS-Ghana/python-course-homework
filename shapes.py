#!/usr/bin/env python

import math #import mathematics package
pi=3.14
def check(area):
  	assert (area>0) , "enter positive  number"
	
  	
def  shape(area):
	check(area)
	if  a == "TRIANGLE": 
 		side= math.sqrt((area*4)/math.sqrt(3)) # side of equileteral triangle when I know area
		return side
	elif a== "SQUARE":
		side= math.sqrt(area) # side of square when I know area
		return side

	elif  a== "CIRCLE" :		
		radius = math.sqrt(area/pi) # radius of circle when I know area
			
			
  		return radius

import sys #import systeme 

if __name__== "__main__":
   	a= str (sys.argv[1])
	area= float(sys.argv[2])
	if a=="TRIANGLE"  :
  	 	print "the equilateral triangle of area: ",area , "size: " ,shape(area)
	elif  a== "SQUARE":
		print "the Square of area: ",area , "size: " ,shape(area)

	elif a== "CIRCLE":
 		print "the circle  of area: ",area , "radius: " ,shape(area)
	else :
		print "invalid error try again "

