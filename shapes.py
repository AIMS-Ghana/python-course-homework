#!/usr/bin/python

import math
import sys   
#functions to find side lengths for square, circle and triangle
def square(area):
    value=math.sqrt(float(area))
    return value

def circle(area):
    radius=math.sqrt(float(area)/math.pi)
    return radius

def triangle(area):
    side=math.sqrt((float(area)*4)/math.sqrt(3))
    return side

def check():
    a=sys.argv[1]
    area=sys.argv[2]
    
    if a=="SQUARE":
        print 'area: ',area,'side:',square(area)
    elif a=="CIRCLE":
        print 'area: ',area,'side:',circle(area)
    elif a=="TRIANGLE":
        print 'equilateral triangle, area: ',area,'side: ',triangle(area)
    else:
	 print " error indicating no input"	
   
#checking for errors in the input    	
if __name__=="__main__":
	
	if len(sys.argv)==1:
		print " error indicating no input"
	else:
	        check()		

