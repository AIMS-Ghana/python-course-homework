#!/usr/bin/python

import sys
import math

#getting the input from the user

x=float(sys.argv[1])

if x>0:
 A=math.pi*(x**2)
 P=2*math.pi*x 
 print"area ",A
 print"perimeter ",P
else:
 print"Error!"
 print"Either a negative number."
