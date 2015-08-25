#!/usr/bin/python
# A program that prints the area and the perimeter of a triangle.
import sys
a = sys.argv[1]
b = sys.argv[2]

area = float(a)*float(b)
perimeter = 2*(float(a) + float(b))
print "area " + str(area)
print "perimeter " + str(perimeter)





