#!/usr/bin/python

import math
def check(r):
  assert (r>0), "entered negative dimension"
def area(r):
    check(r)
    a=r**2*math.pi
    return a

def perimeter(r):
   check(r)
   t=2*r*math.pi
   return t

import sys 
if  __name__ =="__main__":
  r = float(sys.argv[1])

print("area {},\nperimeter {}".format(area(r), perimeter(r)))
 
     
    


























