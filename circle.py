#!/usr/bin/python3
from Math import pi
import sys
R= float(sys.argv[1])
if R(<=0) :
 print("error")
else :
 print("area", pi*R**2)
 print("perimeter", 2*pi*R)
