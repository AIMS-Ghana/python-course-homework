#!/usr/bin/python
# A program that prints the area and the perimeter of a triangle.
import sys
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

area = 0.5*float(a)*float(b)
perimeter = (float(a) + float(b) + float(c))

if sys.argv[1:-1] <= 0:
    print 'Error in the number of inputs'
elif len(sys.argv) == 1:
    print 'Error in the number of inputs'
elif len(sys.argv) == 2:
    print 'Error in the number of inputs'
elif len(sys.argv) == 3:
    print 'Error in the number of inputs'
elif len(sys.argv) == str:
    print 'Error in type'
elif len(sys.argv) == 4:
    print "area " + str(area)
    print "perimeter " + str(perimeter)
elif len(sys.argv) > 4:
    print 'Error in the size of input'
else:
    pass






