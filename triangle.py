#!/usr/bin/python

def check(a,b,c):
    assert (a>0) & (b>0) & (c>0), "entered negative dimension"
    s = a+b
    d = a-b
    assert (s > c) & (d < c), "violated triangle innequality"


def perimeter(a,b,c):
    check(a,b,c)
    return a+b+c

def area (a,b,c):
    check(a,b,c)
    s= ((a+b+c)/2)
    res = (s*(s-a)*(s-b)*(s-c))**0.5
    return res

import sys
#input command that does not import sys

if __name__ == "__main__":
   a=float(sys.argv[1]) 
   b=float(sys.argv[2]) 
   c=float(sys.argv[3])
   print("area{}, perimeter{}".format(area (a,b,c), perimeter (a,b,c)))




