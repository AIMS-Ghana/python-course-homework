#!/usr/local/bin/python3
import sys
L=float(sys.argv[0])
l=float(sys.argv[2])
if(L>0 and l>0):
print("the area is=",L*l)
print("The perimeter is:",(L+l)*2)
else:
print("impossible")
