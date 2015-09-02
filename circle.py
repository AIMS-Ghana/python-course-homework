#!/usr/bin/python

def check (a):
	assert a > 0 and b > 0 and c > 0, "negative dimension"

def perimeter (a):
	check (a)
	return 2 * 3.14 * a

def area (a):
	check (a)
	return 3.14 * a * a

if __name__ == "__main__":
	import sys
	a = float (sys.argv [1])
	print "area {}, perimeter {}".format (area (a), perimeter (a))
