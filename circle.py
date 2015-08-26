#!/usr/bin/env python
import sys
import math

value_area = "area = {0}"
value_perimeter = "perimeter = {0}!"



def area(x):
	area_value = math.pi * float(x) * float(x)
	return area_value

def perimeter(x):
	perimeter_value = 2*math.pi*float(x)
	return perimeter_value
	
if __name__ == "__main__":	
	if len(sys.argv)!=2:
		print "Wrong input!! provide just one value"

	else:
		#check if  int or not
		if sys.argv[1].replace('.','',1).isdigit() ==True:
			print(value_area.format(area(sys.argv[1])))
			print(value_perimeter.format(perimeter(sys.argv[1])))
			
		else:
			print "Wrong input!! enter a positive number!!"
	

