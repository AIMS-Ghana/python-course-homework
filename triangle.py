#!/usr/bin/python
import math
def area(a,b,c):
	p=(a+b+c)/2
	area=math.sqrt(p*(p-a)*(p-b)*(p-c))
	return area
def perimeter(a,b,c):
	perimeter=a+b+c
	return perimeter
def check (a,b,c):
	assert (a>0) & (b>0) & (c>0),"entered negative dimension"
	s=a+b
	d=a-b
	assert (s>c) & (d<c), "violated triangle inequality"
import sys 
if __name__ == "__main__":
    a= float(sys.argv[1])
    b= float(sys.argv[2])
    c= float(sys.argv[3])
print ("area {0}, perimeter {1}".format (area(a,b,c),perimeter(a,b,c)))

