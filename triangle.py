#!/usr/bin/env python
import math



def check(a,b,c):
	assert a>0 and b>0 and c>0, "enter positive numbers"
	s=a+b
	d=a-b
	assert (s>c) and (c>d), "violated the triangle equilateral rule"
def perimeter(a,b,c):
	check(a,b,c)
	value=a+b+c
	return value
def area(a,b,c):
	#heros formula
	check(a,b,c)
	value=(a+b+c)/2
	result= math.sqrt(value*(value-a)*(value-b)*(value-c))
	return result

import sys
if __name__=="__main__":
	a=float (sys.argv[1])	
	b=float (sys.argv[2])
	c=float (sys.argv[3])
	print("area{}, perimeter{}".format(area(a,b,c), perimeter(a,b,c)))
