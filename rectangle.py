#!/usr/bin/env python

import sys
import math

a=float(sys.argv[1])
b=float(sys.argv[2])
if (a<0 and b<0):
 print "Please enter a non negative number"
else:

area=a*b
perimeter=2*(a+b)

print "area", area
print "perimeter", perimeter
