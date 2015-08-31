#!/usr/bin/python

import sys
greeting = "hello, {0}!"
name = "world "

if len (sys.argv) == 2:
   name = sys.argv[1]
else:
  name = ", " .join (sys.argv[1:-1]) + "and " + sys.argv[-1]
print (greeting.format(name))
