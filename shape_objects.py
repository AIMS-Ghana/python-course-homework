#!/usr/bin/env python

class Shape:
    def kind(self):
        return "Shape"

    def invert_area(self, area):
        return area

    def dimname(self):
        return "HUH?"

    def __init__(self, area):
        self.__area = area
        self.__dim = self.invert_area(area)

    strformat = "{}, area: {}, {}: {}"

    def __str__(self):
        return Shape.strformat.format(
          self.kind(),
          self.__area,
          self.dimname(),
          self.__dim
        )

    def draw(turt):
        pass

class Triangle(Shape):
    def kind(self):
        return "TRIANGLE"
    def dimname(self):
        return "side"
    def invert_area(self, area):
        return (2*(float( area))**0.5)/3**0.25
    def draw(self,turt):
            turtle.color("yellow")
            turtle.begin_fill()
            turtle.forward(self.dim)
            turtle.left(120)
            turtle.forward(self.dim)
            turtle.left(120)
            turtle.forward(self.dim)
            turtle.end_fill()


class Square(Shape):
    def kind(self):
        return "SQUARE"
    def dimname(self):
        return "side"
    def invert_area(self, area):
        return (float (area))**.5
    def draw(self,turt):
        turtle.color("green")
        turtle.begin_fill()
        turtle.forward(self.dim)
        turtle.left(90)
        turtle.forward(self.dim)
        turtle.left(90)  
        turtle.forward(self.dim)
        turtle.left(90)
        turtle.forward(self.dim)
        turtle.left(90) 
        turtle.end_fill()

from math import pi

class Circle(Shape):
    def kind(self):
        return "CIRCLE"
    def dimname(self):
        return "radius"
    def invert_area(self, area):
        return (area/pi)**.5
    def draw(self,turt):
        turtle.color("red")
        turtle.begin_fill()
        turtle.circle(self.dim)
        turtle.end_fill()
         

if __name__ == "__main__":
    circ = Circle(1000)
    triang = Triangle(1000)
    sqr = Square(10)
    print(circ)
    print(triang)
    print(sqr)
    circ.draw(turtle)
    tri.draw(turtle)
    sqr.draw(turtle)
