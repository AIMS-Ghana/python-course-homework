#!/usr/bin/python3
import sys
import turtle
from shapes import *
from random import *

if __name__ == "__main__":
	try:
		global shape
		global area

		shape = sys.argv[1]
		area = float(sys.argv[2])

	except ValueError:
		print("Invalid area entered")
		quit()

	except IndexError:
		print("no shape and area entered")
		quit()

def draw(shape,area):
	if shape == "CIRCLE":
		screen = turtle.Screen()
		circle = turtle.circle(side_calc(shape,area))
		turtle.exitonclick()
	elif shape != "CIRCLE":
		no_of_sides = {"TRIANGLE":3, "SQUARE":4}
		n = no_of_sides[shape]
		int_angle = ((n-2)*180.0)/n
		turn = 180 - int_angle
		screen = turtle.Screen()
		polygon = turtle.Turtle()
		for i in range(1,n+1):
			polygon.forward(side_calc(shape,area))
			polygon.left(turn)
		turtle.exitonclick()


if __name__ == "__main__":
	draw(shape,area)

    Status API Training Shop Blog About Pricing 


