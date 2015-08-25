#!/usr/bin/python
# A program that prints the area and the perimeter of a triangle.
import sys
r = sys.argv[1]
pi = float(3.14)

area = 3.14*float(r)*float(r)
perimeter = 2*pi*float(r)

if sys.argv <= 0:
    print 'Error in the number of inputs'
elif len(sys.argv) == 1:
    print 'Error in the number of inputs'
elif len(sys.argv) == 3:
    print 'Error in the number of inputs'
elif len(sys.argv) == str:
    print 'Error in type'
elif len(sys.argv) == 2:
    print "area " + str(area)
    print "perimeter " + str(perimeter)

else:
    pass




