#!/usr/bin/python
import sys
greet = ""
if len(sys.argv) == 1:
    print"hello, world"
elif len(sys.argv) == 2:
   print("hello, {}".format())
msg = ", ".join(sys.argv[1:-1]) + " and " + sys.argv[-1]
print()
