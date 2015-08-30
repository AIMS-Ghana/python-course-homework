#!/usr/bin/python
import sys
name = sys.argv
greet = "hello, {0}"

msg = " "
if len(sys.argv) == 1:
    msg =  "world"
elif len(sys.argv) == 2:
    mgs = sys.argv[1] 
else:
    msg = ", ".join(sys.argv[1:-1]) + " and " + sys.argv[-1]
    
print(greet.format(msg))

