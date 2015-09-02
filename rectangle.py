#!/usr/bin/python

def check (a, b):
	assert a > 0 and b > 0, "negative dimension"

def perimeter (a, b):
	check (a, b)
	return a + b

def area (a, b):
	check (a, b)
	return a * b

if __name__ == "__main__":
	import sys
	a = float (sys.argv [1])
	b = float (sys.argv [2])
	print "area {}, perimeter {}".format (area (a, b), perimeter (a, b))
