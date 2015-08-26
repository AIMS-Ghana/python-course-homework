#!/usr/bin/env python
import sys
value="area {0}\nperimeter {1}"
area=""
perimeter=""
if len(sys.argv)==3: 
	area=float(int(sys.argv[1]) * int(sys.argv[2]))
	perimeter=2 * float(sys.argv[1]) + 2 * float(sys.argv[2])
	print (value.format(str(area),str(perimeter)))
elif len(sys.argv)==2:
	area=float(int(sys.argv[1])) ** 2
	perimeter=float(int(sys.argv[1])) ** 4
 	print (value.format(str(area),str(perimeter)))
else:
	if len(sys.argv) >3: 
		value="wrong input! only two values required!"
		print (value)
if len(sys.argv)==1:
	value="wrong input! two values required!"
	print (value)
 
      
