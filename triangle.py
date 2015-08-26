#!/usr/bin/env python
import math

import sys
input_area="{0}"
input_perimeter="{0}"
def area(x,y,z):
	sum_value=(float(x)+float(y)+float(z))/2
    	area_value=(sum_value*(sum_value-float(x))*(sum_value-float(y))*(sum_value-float(z)))**0.5
    	return area_value
def perimeter(x,y,z):
    	perimeter_value=float(x)+float(y)+float(z)
   	return perimeter_value


if __name__ == "__main__":

    if len(sys.argv) !=4:
        print "wrong inputs"

    else:   
        if sys.argv[1].replace('.','',1).isdigit()==True:
            print "area",  area(sys.argv[1],sys.argv[2],sys.argv[3])
            print "perimeter",  perimeter(sys.argv[1],sys.argv[2], sys.argv[3])
        else :
		print "have atleast three values"
