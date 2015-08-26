#!/usr/bin/python
import sys
PI = 3.14159

def area_of_Circle(radius):
    area = PI * radius **2
    return area 

def perimeter_of_Circle(radius):
    perimeter = 2 * PI * radius
    return perimeter

radius = float(sys.argv[1])

area = area_of_Circle(radius)
print 'Area', area 

perimeter =perimeter_of_Circle(radius)
print 'perimeter', perimeter


