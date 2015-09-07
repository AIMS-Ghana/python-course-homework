#!/usr/bin/python
import math

def check (a, b, c):
	assert a > 0 and b > 0 and c > 0, "negative dimension"
	s = a + b
	d = a - b
	assert s > c and d < c, "not a triangle"

def perimeter (a, b, c):
	check (a, b, c)
	return a + b + c

def area (a, b, c):
	check (a, b, c)
	res = (a + b + c) / 2
	return math.sqrt (res * (res - a) * (res - b) * (res - c))


if __name__ == "__main__":
	import sys
	a = float (sys.argv [1])
	b = float (sys.argv [2])
	c = float (sys.argv [3])
	print "area {}, perimeter {}".format (area (a, b, c), perimeter (a, b, c))
