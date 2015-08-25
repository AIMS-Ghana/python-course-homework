#!/usr/bin/python
import sys
area=" "
perimeter=" "
greeting="area=[0]\n perimeter=[1]"
l=float(sys.argv[1])
w=float(sys.argv[2])
area =l*w
perimeter=2*(l + w)
#area=(sys.argv[0])
#perimeter =(sys.argv[1]) 
print "area" + str (area)
print "perimeter" + str(perimeter)


