#!/usr/bin/python

import sys
PI = 3.14159

def area_of_circle(r):
    area = PI * r **2
    return area

def perimeter_of_circle(r):
    perimeter = 2* PI * r
    return perimeter

r= float(sys.argv[1])
area= area_of_circle(r)
print ' Area ', area

perimeter=perimeter_of_circle(r)
print'perimeter', perimeter
