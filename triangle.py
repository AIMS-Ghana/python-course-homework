#!/usr/bin/env python
import sys
import math


value = "area = {0}!\nperimeter = {1}!"

if len(sys.argv)!=4:
	print "Wrong input!! provide three values"

else:
	#check if int or not
	if sys.argv[1].replace('.','',1).isdigit() ==True and sys.argv[2].replace('.','',1).isdigit()==True and sys.argv[3].replace('.','',1).isdigit()==True: 
		#check triangular rule
		sum_  = float(sys.argv[1]) + float(sys.argv[2])
		diff_ = float(sys.argv[1]) - float(sys.argv[2])
		
		#checking
		if sum_>float(sys.argv[3]) and diff_ < float(sys.argv[3]):
			
			sum_main = float((float(sys.argv[1]) + float(sys.argv[2]) +float(sys.argv[3]))/2)
			
			pre_area = sum_main * (sum_main-float(sys.argv[1])) * (sum_main-float(sys.argv[2])) * (sum_main-float(sys.argv[3]))       
		
			area_value = math.sqrt(pre_area)

			perimeter_value = float(sys.argv[1]) + float(sys.argv[2]) +float(sys.argv[3])
			print(value.format(area_value,perimeter_value)) 
		else:
			print "Values provided can't be the sides of a triangle"

	else:
		print "Wrong input!! Enter a number!!"
	
