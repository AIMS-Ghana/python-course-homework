#!/usr/bin/python
# A program that prints the area and the perimeter of a triangle.
import math
import sys
r = float(sys.argv[1])
pi = float(3.14)

def check(r):
    assert (r > 0) & (len(sys.argv) == 2), "Entered negative dimension"
    pass

check(r)

area = 3.14*r**2
perimeter = 2*pi*r

# if len(sys.argv) == 2:
print "area " + str(area)
print "perimeter " + str(perimeter)






