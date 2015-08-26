#!/usr/bin/env python
import sys
import math



value_area = "area = {0}"
value_perimeter = "perimeter = {0}!"

def check(x,y,z):
	if x.replace('.','',1).isdigit() ==True and y.replace('.','',1).isdigit()==True and z.replace('.','',1).isdigit()==True: 
			#check triangular rule
			sum_  = float(x) + float(y)
			diff_ = float(x) - float(y)
		
			#checking
                        assert sum_>float(z) and diff_< float(z),'error'
			 
	
	else:
			print "Wrong input!! Enter a number!!"
	


def area(x,y,z):
	check(x,y,z)
	sum_main = float((float(x) + float(y) +float(z))/2)
	pre_area = sum_main * (sum_main-float(x)) * (sum_main-float(y)) * (sum_main-float(z))       
	area_value = math.sqrt(pre_area)
	return area_value
	
	

def perimeter(x,y,z):
	check(x,y,z)
	perimeter_value = 2*float(x) + 2*float(y)
	return perimeter_value
	
if __name__ == "__main__":
	if len(sys.argv)!=4:
		print "Wrong input!! provide three values"

	else:
		print'area = ',area(sys.argv[1], sys.argv[2],sys.argv[3])
		print'perimeter = ', perimeter(sys.argv[1],sys.argv[2],sys.argv[3])
		
'''

		#check if int or not
		if sys.argv[1].replace('.','',1).isdigit() ==True and sys.argv[2].replace('.','',1).isdigit()==True and sys.argv[3].replace('.','',1).isdigit()==True: 
			#check triangular rule
			sum_  = float(sys.argv[1]) + float(sys.argv[2])
			diff_ = float(sys.argv[1]) - float(sys.argv[2])
		
			#checking
			if sum_>float(sys.argv[3]) and diff_ < float(sys.argv[3]):
				print'area = ',area(sys.argv[1], sys.argv[2],sys.argv[3])
				print'perimeter = ', perimeter(sys.argv[1],sys.argv[2],sys.argv[3])
			else:
				print "Values provided can't be the sides of a triangle"

		else:
			print "Wrong input!! Enter a number!!"
'''
	
