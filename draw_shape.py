#!/usr/bin/python

import math

from math import pi

radius=(areaC*pi*radius)**0.5
sidea=(2/3)*((3)**(3/4))*((areaA)**0.5)
sideb=(areaB)**0.5


import sys
 
if __name__ =="__triangle__":
      areaA=float(sys.argv[1])

elif __name__ =="__rectangle__":
        areaB=float(sys.argv[1])

elif __name__ =="__triangle__":
       areaC=float(sys.argv[1])

else:
      print"error! "

def draw()

import turtle

wn=turtle.turtle()
triangle=turtle.turtle()
square=turtle.turtle()
circle=turtle.turtle()

triangle.forward(sidea)
triangle.left(120)
triangle.forward(sidea)
triangle.left(120)
triangle.forward(sidea)
triangle.left(120)

square.forward(sideb)
square.left(90)
square.forward(sideb)
square.left(90)
square.forward(sideb)
square.left(90)
square.forward(sideb)
square.left(90)

turtle.circle(radius)
turtle.position(0.00,0.00)
turtle.heading(0)

wn.exitonclick()
