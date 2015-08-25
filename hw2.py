#!/usr/bin/python
import sys
greeting="hello,{0}!"
word= ""
if len (sys.argv) ==1
word="word"
elif len(sys.argv)==2:

word=sys.argv[1]
else:
world= ", ".join(sys.arg[1:-1]) + " and" + sys.argv[-1]
print(greeting.format(world))

