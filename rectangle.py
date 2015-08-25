#!/usr/bin/python
import sys
from math import *

try:
 if len(sys.agrv) == 2:
  print "area " + int(sys.argv[1])*int(sys.argv[1])
  print "perimeter " + 2*int(sys.argv[1])
 elif len(sys.argv) == 3:
  print "area " + int(sys.argv[1])*int(sys.argv[2])
  print "perimeter " + int(sys.argv[1])+int(sys.argv[2])
#except:
# print "invalid sides entered"
