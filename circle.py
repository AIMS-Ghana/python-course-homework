#!/usr/bin/env python
import sys
value="area {0}\nperimeter {1}"
area=""
perimeter=""
import math
from math import pi

if len(sys.argv)==2: 
	# sys.argv[1] represents radius of a circle
	area=pi * float(int(sys.argv[1])) ** 2  
	perimeter=2 * pi * float(int(sys.argv[1]))
	print (value.format(str(area),str(perimeter)))
elif  len(sys.argv) <2:
	value="ERROR! INPUT VALUE!"
	print (value)
else:
	if len(sys.argv) >2:  
		value="wrong input! one value required!"
		print (value)
	 

