#!/usr/bin/python
import sys
r=sys.argv[-1]
s=sys.argv[1]
r=int(r)
s=int(s)
if r<0 or s<0:
	print("error,there is a negative numbers, please retype")
	sys.exit()
else:
	print"area ",r*s
	print"perimeter",2*(r+s)

