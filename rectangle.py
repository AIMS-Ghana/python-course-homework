#!/usr/bin/env python
#area of a triangle
import math



def check(a,b):
	assert a>0 and b>0, "enter positive numbers"

def area(a,b):
	check(a,b)
	result=a*b
	return result
def perimeter(a,b):
	check(a,b)
	value=2*(a+b)
	return value
import sys
if __name__=="__main__":
	a=float (sys.argv[1])	
	b=float (sys.argv[2])
	print("area{}, perimeter{}".format(area(a,b), perimeter(a,b)))



        if sys.argv[1].replace('.','',1).isdigit()==True:
            print "area",  area(sys.argv[1],sys.argv[2])
            print "perimeter",  perimeter(sys.argv[1],sys.argv[2])
        else :
		print "have atleast three values"

