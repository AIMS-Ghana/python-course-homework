#!/usr/bin/python

def check (l):
	for i in l:
		assert i >0, "negative dimension"

def perimeter (l):
	check (l)
	per = 0
	for i in l :
		per = per + i
	return per

def area (l):
	check (l)
	ar = 1
	for i in l:
		ar *= i
	return ar

if __name__ == "__main__":
	import sys
	if len (sys.argv) == 3:
		a = float (sys.argv [1])
		b = float (sys.argv [2])	
		print "area {}, perimeter {}".format (area ([a,b]), perimeter ([a,b]))
	elif len (sys.argv) == 2:
		a = float (sys.argv [1])
		print "area {}, perimeter {}".format (area ([a]), perimeter ([a]))
