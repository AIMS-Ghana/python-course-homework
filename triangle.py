#!/usr/bin/python

import sys

import math

a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
s=(a+b+c)/2

perimeter = a+b+c

area = (s*(s-a)*(s-b)*(s-c))**0.5

if len(sys.argv)!= 4:
     print"error!"
 
elif len(sys.argv)==4:
      if float(sys.argv[1])<0 or float(sys.arg[2])<0 or float
(sys.argv[3])<0:
         print"error!"
      else:
         print"area "+str(area)
         print"perimeter "+str(perimeter)

