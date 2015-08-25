#!/usr/bin/python

import sys

area = 0.5*float(sys.argv[1])*float(sys.argv[2])*float(sys.argv[3])
perimeter = float(sys.argv[1])+float(sys.argv[2])+float(sys.argv[3])


print 'Area ' + str(area)
print 'Perimeter '  + str(perimeter)
