#!/usr/bin/python

import sys

word = ""

if len (sys.argv) == 1:
	world = "World!"
elif len (sys.argv) == 2:
	word = sys.argv [1]
else:
	word = ",".join (sys.argv [1:-1]) + " and " + sys.argv [-1]

print ("hello, {}".format (word))	
		
