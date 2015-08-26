#!/usr/bin/python3
import sys
import math

import triangle
import circle
import rectangle

import shapes

def draw(shape,area):
 import turtle
 import sys
 import math
 
 import triangle
 import circle
 import rectangle

 import shapes

 if shape == "CIRCLE":
  r = shapes.circlerad(area)
  scale = 30.0
  rshow = r*scale
  wn = turtle.Screen()
  turtle.circle(rshow)
  turtle.write("Click Me",font=("Arial", 20, "normal"))
  wn.exitonclick() 
  

 elif shape == "SQUARE":
  L = shapes.squarelength(area)
  scale = 30.0
  Lshow = L*scale
  wn = turtle.Screen()
  turtle.forward(Lshow)
  turtle.left(90)
  turtle.forward(Lshow)
  turtle.left(90)
  turtle.forward(Lshow)
  turtle.left(90)
  turtle.forward(Lshow)
  turtle.write("Click Me",font=("Arial", 20, "normal"))
  wn.exitonclick() 
  
  print("SQUARE",area)

 elif shape == "RECTANGLE":
  L2 = ((2.0*area)/(1+5.0**(1/2.0)))**(1/2.0)
  L1 = ((1+5.0**(1/2.0))*area/2.0)**(1/2.0)
  scale = 30.0
  L1show = L1*scale
  L2show = L2*scale
  wn = turtle.Screen()
  turtle.forward(L1show)
  turtle.left(90)
  turtle.forward(L2show)
  turtle.left(90)
  turtle.forward(L1show)
  turtle.left(90)
  turtle.forward(L2show)
  turtle.write("Click Me",font=("Arial", 20, "normal"))
  wn.exitonclick() 
  
  

 elif shape == "TRIANGLE":
  L = shapes.trianglelength(area)
  scale = 30.0
  Lshow = L*scale
  wn = turtle.Screen()
  turtle.forward(Lshow)
  turtle.left(120)
  turtle.forward(Lshow)
  turtle.left(120)
  turtle.forward(Lshow)
  turtle.write("Click Me",font=("Arial", 20, "normal"))
  wn.exitonclick() 
  

 else:
  print("Cannae draw this, pal")

totalargs = len(sys.argv)

if __name__ == "__main__":  

 shape = sys.argv[1] 
 A = float(sys.argv[2])

 draw(shape,A)
