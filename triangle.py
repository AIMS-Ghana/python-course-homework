#!/usr/bin/python
import sys
area=" "
perimeter=" "
greeting="area=[0]\n perimeter=[1]"
b=float(sys.argv[1])
h=float(sys.argv[2])
w=float(sys.argv[3])
area=1/2*b*h
perimeter=b + h + w
#area=(sys.argv[0])
#perimeter=(sys.argv[1])
print"area" + str(area)
print"perimeter" + str(perimeter)


