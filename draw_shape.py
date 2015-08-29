#!/usr/bin/python

import turtle

from shapes import compute

def Circle(radius):
	turtle.circle(radius)

def ngon(n,side):
	turn= 180-(n-2)*180/n
	
    for i in range(n-1):
	turtle.forward(side)
	turtle.right(turn)
	turtle.forward(side)

def triangle(side):
	ngon(3, side)

def square(side)
	ngon(4, side)

figs={
	'CIRCLE':circle,
	'SQUARE':square,
	'TRIANGLE':triangle
}

def draw(shape, area):
	dim=compute(shape,area)
	figs[shape](dim)
	turtle. exitoniclick ()

import sys.

if __name__= "__main__":
	shape = sys.argv[1]
	area = float(sys.argv[1])
	draw(shape,area)
	print


