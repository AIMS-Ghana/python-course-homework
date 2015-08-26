#!/usr/bin/python

def perimeter(a,b):
    return 2*(a+b)

def area(a,b):
    res = a*b
    return res

import sys
if __name__=="__main__":
    a=float(sys.argv[1])
    b=float(sys.argv[2])
print(" area {} \n perimeter {}".format(area(a,b), perimeter(a,b)))

