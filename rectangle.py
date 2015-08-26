#!/usr/bin/env python
<<<<<<< HEAD
=======
#area of a rectangle
>>>>>>> 39fbc03850c97e5fc0a027c1f8272510677bd083
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

<<<<<<< HEAD

=======
>>>>>>> 39fbc03850c97e5fc0a027c1f8272510677bd083

