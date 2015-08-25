#!/usr/bin/python

import sys
import math

#getting the input from the user

x=float(sys.argv[1])
y=float(sys.argv[2])
z=float(sys.argv[3])

#calculating the semi-perimeter(s)

if(x>0 and y>0 and z>0 and (x+y)>z and (x+z)>y and (y+z)>x):
 s=(x+y+z)/2
#"a" is the area
 a=((s*(s-x)*(s-y)*(s-z))**0.5)
 p=x+y+z   #"p" is the perimeter
 print"area ",a
 print"perimeter",p
else:
 print"Error!"
 print"Either a negative number(s) is entered or the Triangular Inequality is violated."

