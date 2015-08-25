#!/usr/bin/python
import sys
greeting="Area={O} and perimeter={1}"
x=float(sys.argv[1])
y=float(sys.argv[2])
area=x*y
perimeter=2*(x+y)

print "area ", area
print "perimeter", perimeter
