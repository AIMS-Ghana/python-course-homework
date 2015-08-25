#!/usr/bin/python
import sys
a=float (sys.argv[1])
b=float (sys.argv[2])
c=float (sys.argv[3])
s=(float(a)+float(b)+float(c))*0.5
p= (a)+(b)+(c)
area=(p*0.5*(p-a)*(p-b)*(p-c))**0.5

print "area " + str(area)
print "perimeter " ,p
