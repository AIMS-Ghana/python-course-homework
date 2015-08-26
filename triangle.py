#!/usr/bin/python3
import math
def check(a,b,c):
	assert (a>0) & (b>0) & (c>0), "entered negative dimension"
	s= a+b
	d= a-b
	assert (s>c) & (d<c),"violetd triangle inequality"
def area(a,b,c):
	check(a,b,c)
        k=(a+b+c)/2
        res = math.sqrt(k*(k-a)*(k-b)*(k-c))
        return res
def perimeter(a,b,c):
    check(a,b,c)
    return a+b+c 
import sys
if __name__ == "__main__":
    a= float(sys.argv[1])
    b= float(sys.argv[2])
    c= float(sys.argv[3])
    print("area{}, parimeter{} ".format(area(a,b,c),perimeter(a,b,c)))




