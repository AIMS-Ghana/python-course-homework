#!/usr/bin/python3
import sys
import math
l=float(sys.argv[1])
b=float(sys.argv[2])
h=float(sys.argv[3])

area =(b*h)/2
perimeter =l+b+h
          
print "area" + str(area)
print "perimeter" + str(perimeter)
if len (sys.argv)==3:           
                  print "area" + str(area)
                  print "perimeter" + str(perimeter)
if sys.argv[1]<=0 or sys.argv[2]<=0 or sys.argv[3]<=0:
                print "check and revise parameters"
elif len (sys.argv)!=3:
             print "check and revise parameters"
else:
     print "revise parameters"


   
   

