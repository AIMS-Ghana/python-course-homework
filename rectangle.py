#!/usr/bin/python
import math
def area(a,b,):
	p=(2*(a)+2*(b))
	area=(a*b)
	return area
def perimeter(a,b,):
	perimeter=(2*(a)+2*(b))
	return perimeter
def check (a,b):
	assert (a>0) & (b>0),"entered negative dimension"
	s=a
	d=a-b
	assert (s>c) & (d<c), "violated triangle inequality"
import sys 
if __name__ == "__main__":
	if len(sys.argv) == 3:
    		a= float(sys.argv[1])
		b= float(sys.argv[2])
	elif len(sys.argv) == 2:
    		a= float(sys.argv[1])
    		b= float(sys.argv[1])
print ("area {0}, perimeter {1}".format (area(a,b),perimeter(a,b)))

 




