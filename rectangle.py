#!/usr/bin/python
import sys
import math

def perimeter(a,b):
    check(a,b)
    p=(2*a+2*b)
    return p

def area(a,b):
    check(a,b) 
    res=(a*b)
    return res

def check(a,b):
    assert (a>0) & (b>0) , "negative dimension"
    
    
import sys
if __name__ == "__main__":
	try:
   		 a = float(sys.argv[1])
   		 b = float(sys.argv[2])
		 print "area {},\nperimeter{} ".format(area(a,b), perimeter(a,b))
	except:
		a = float(sys.argv[1])
		print "area {},\nperimeter{} ".format(area(a,a), perimeter(a,a))
    
#    print "area {},\nperimeter{} ".format(area(a,b), perimeter(a,b))
