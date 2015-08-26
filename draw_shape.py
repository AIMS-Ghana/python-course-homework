#!/usr/bin/env python3

import sys
from turtle import *
import shape
if __name__=="__main__":
	a=sys.argv[1]
	b=sys.argv[2]
	if a=="square":
		forward(side3(b))
		left(90)
		forward(side3(b))
		left(90)
		forward(side3(b))
		left(90)
		forward(side3(b))
		done()
	elif
		 a=="Equilateral triangle"
			forward(side2(b))
			left(120)
			forward(side2(b))
			left(120)
			forward(side2(b))
	elif
		a=="Circle"
		circle(side1(b))
	else
		print("error, wrong shape")	
	
