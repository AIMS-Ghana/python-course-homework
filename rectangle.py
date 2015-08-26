#!/usr/bin/env python
#area of a rectangle
import math

import sys
input_area="{0}"
input_perimeter="{0}"
def area(x,y):
    	area_value=float(x)*float(y)
    	return area_value
def perimeter(x,y):
    	perimeter_value=2*(float(x)+float(y))
   	return perimeter_value


if __name__ == "__main__":
    if len(sys.argv) ==2:
	print "area",  area(sys.argv[1])
        print "perimeter",  perimeter(sys.argv[1])
    
    elif len(sys.argv) !=3:
        print "wrong inputs"
    
    else:   
        if sys.argv[1].replace('.','',1).isdigit()==True:
            print "area",  area(sys.argv[1],sys.argv[2])
            print "perimeter",  perimeter(sys.argv[1],sys.argv[2])
        else :
		print "have atleast three values"

