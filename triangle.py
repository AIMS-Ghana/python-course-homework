#!/usr/bin/env python
import sys
import math
input_area="{0}"
input_perimeter="{0}"
def area(x,y):
	sum_value=float((x+y+z)/2)
	area_value=float(sum_value)*(sum_value-x)*(sum_value-y)*(sum_value-z)
	return area_value
def perimeter(x,y):
	perimeter_value=2*(float(x)+float(y))
	return perimeter_value


if __name__ == "__main__":

	if len(sys.argv) !=3:
		print "wrong inputs"
	else:	
		if sys.argv[1].replace('.','',1).isdigit()==True:
			print area(sys.argv[1],sys.argv[2])
			print perimeter(sys.argv[1],sys.argv[2])
		else "have atleast two values"
