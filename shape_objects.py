#!/usr/bin/env python3
import math
import turtle

class Shape:
    def kind(self):
        return "Shape"

    def invert_area(self, area):
       return area

    def dimname(self):
        return "HUH?"

    def __init__(self, area):
        self.area = area
        self.dim = self.invert_area(area)

    strformat = "{}, area: {}, {}: {}"

    def __str__(self):
        return Shape.strformat.format(
          self.kind(),
          self.area,
          self.dimname(),
          self.dim
        )

    def draw(self):
        pass


class Triangle(Shape):
   def kind(self):
        return "triangle"

   def invert_area(self, area):
       return math.sqrt(float((area)*4)/math.sqrt(3))

   def dimname(self):
        return "side"

   def draw(self):
       turtle.penup()
       turtle.setx(20)
       turtle.sety(100)
       turtle.pendown()
       turtle.color('blue')
       turtle.begin_fill()
       for i in range(0,3):
           turtle.forward(self.dim)
           turtle.left(120)
       turtle.end_fill()
       #turtle.end_fill()
            

class Square(Shape):
    def kind(self):
        return "square"
    def dimname(self):
        return "side"
    def invert_area(self, area):
       return area**0.5

    def draw(self):
        turtle.penup()   
        turtle.setx(-100)
        turtle.sety(20)	       
        turtle.pendown()
        turtle.color('red')
        turtle.begin_fill()
        for i in range(0,4):           
             turtle.forward(self.dim)
             turtle.left(90)
        turtle.end_fill()
             
	
from math import pi

class Circle(Shape):
    def kind(self):
        return "circle"
    def dimname(self):
        return "radius"
    def invert_area(self, area):
       return float(math.sqrt(area/math.pi)) 

    def draw(self):
       turtle.penup()
       turtle.setx(-100)
       turtle.sety(-50)
       turtle.pendown()
       turtle.begin_fill()
       turtle.color('red')
       turtle.circle(self.dim)
       turtle.end_fill()
   
if __name__ == "__main__":
    import turtle
    window = turtle.Screen()
    turtle.ht()
    circ = Circle(5000)
    sq=Square(4000)
    tri=Triangle(5000)
    print(circ)
    print(sq)
    print(tri)
    circ.draw()
    sq.draw()
    tri.draw()
    #turtle.write(sq)
    window.exitonclick()

