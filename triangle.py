#!/usr/bin/python

def chec(a,b,c):
    assert ((a>0) & (b>0) & (c>0)), "entered negative dimension"
    s=a+b
    d=a-b
    assert ((s>c) and (d<c)), "violated triangle inequality"

def perimeter(a,b,c):
    chec(a,b,c)
    return a+b+c

def area(a,b,c):
    chec(a,b,c)
    s=(a+b+c)/2
    res = (s*(s-a)*(s-b)*(s-c))**0.5 
    return res

import sys
if __name__=="__main__":
    a=float(sys.argv[1])
    b=float(sys.argv[2])
    c=float(sys.argv[3])
print("area {} \nperimeter {}".format(area(a,b,c), perimeter(a,b,c)))
