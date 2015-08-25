#!/usr/bin/python
# A program that prints the area and the perimeter of a triangle.
import sys
a = sys.argv[1]
b = sys.argv[2]

area = float(a)*float(b)
perimeter = 2*(float(a) + float(b))



if len(sys.argv) == 1:
    print 'Error in the number of inputs'
elif sys.argv == str:
    print 'Error in type'
elif len(sys.argv) == 2:
    print "area " + sys.argv**2
    print "perimeter " + 4*sys.argv
elif len(sys.argv) == 4:
    print "Over the limit"
elif len(sys.argv) > 4:
    print 'Error in the size of input'

else:
    print "area " + str(area)
    print "perimeter " + str(perimeter)






