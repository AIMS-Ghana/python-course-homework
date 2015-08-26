#!/usr/bin/env python
import sys

value_area = "area = {0}"
value_perimeter = "perimeter = {0}!"


def area(x,y):
	area_value = float(x) * float(y)
	return area_value
	

def perimeter(x,y):
	perimeter_value = 2*float(x) + 2*float(y)
	return perimeter_value
	
if __name__ == "__main__":

	if len(sys.argv)== 2:
		#check if  int or not'3.14'.replace('.','',1).isdigit()
		if sys.argv[1].replace('.','',1).isdigit() ==True: 
			print'area = ',area(sys.argv[1],sys.argv[1])
			print'perimeter = ',perimeter(sys.argv[1],sys.argv[1])
			#print(value.format(area_value,perimeter_value)) 
		
		else:
			print "Wrong input!! enter a positive number!!"

	elif len(sys.argv)== 3:
		#check if  int or not'3.14'.replace('.','',1).isdigit()
		if sys.argv[1].replace('.','',1).isdigit() ==True and sys.argv[2].replace('.','',1).isdigit()==True: 
			print'area = ',area(sys.argv[1],sys.argv[2])
			print'perimeter = ',perimeter(sys.argv[1],sys.argv[2])
			#print(value.format(area_value,perimeter_value)) 
		
		else:
			print "Wrong input!! enter a positive number!!"

	else:
		print "Wrong input!! provide two values"
