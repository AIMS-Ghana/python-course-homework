#!/usr/bin/python

import math


def circle(a):
    	return (a/math.pi)**0.5

def square(a):
	return a**0.5

def triangle(a):
	return 2*(a/(3**0.5))**0.5

Shaper = {

       	'CIRCLE': circle,
       	'TRIANGLE': triangle,
	'SQUARE': square
}

output_mods = {

	'TRIANGLE':'equilateral'
}

dim_name = {
	'CIRCLE':'radius'
}


def compute(shape,a):
     	assert shape in Shaper,"shape " "+shape+" is not parseable
	return Shaper[shape](a)



import sys


if __name__== "__main__":
	assert len(sys.argv)==3
	shape = (sys.argv[1])
	area = float(sys.argv[2])
	compute(shape,area)
        out = "{}, area {}, {}:{}"
	
	print(out.format(shape,area,"side",compute(shape,area)))




