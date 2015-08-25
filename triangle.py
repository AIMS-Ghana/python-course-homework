#!/usr/bin/python

import sys
from math import sqrt

a = len(sys.argv)
try:
  l1 = int(sys.argv[1])
  l2 = int(sys.argv[2])
  l3 = int(sys.argv[3])

  if int(sys.argv[1]) <= 0 or int(sys.argv[2]) <= 0 or int(sys.argv[3]) <= 0:
     print "invalid side length entered. The length should be non-negative and non-zero"
     pass
  elif a != 4:
      print "The figure is not a triangle. A triangle has 3 sides so check the number of side"
      pass
  else:
      p = l1 + l2 + l3
      a = float(l1 + l2 + l3)
      s = a/2.0
      A1 = float(s*(s-l1)*(s-l2)*(s-l3))
      A = sqrt(A1)
      if A == 0:
         print "invalid lengths entered"
      else:
         print "area ",
         print A
         print "perimeter",
         print p
   
except ValueError:
 print "invalid lengths entered"
except IndexError:
 print "invalid lengths entered"

	    
