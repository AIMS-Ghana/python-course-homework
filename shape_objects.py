#!/usr/bin/env python3

class Shape:

    

    def kind(self):
        return "Shape"

    def invert_area(self, area):
        return area

    def dimname(self):
        return "HUH?"

    def __init__(self, area):
        self._area = area
        self._dim = self.invert_area(area)

    
    strformat = "{}, area: {}, {}: {}"

    def __str__(self):
        return Shape.strformat.format(
          self.kind(),
          self._area,
          self.dimname(),
          self._dim
        )

    def draw(self,turt):
        pass
#####################################################################################

class Triangle(Shape):
     def kind(self):
        return "Triangle"
     
     def invert_area(self, area):
        return (4*area/3**(1/2.0))**(1/2.0)
    
     def dimname(self):
        return "L"
     
     def draw(self,turt):
        import turtle
        wn = turtle.Screen()
        L= self._dim
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

class Square(Shape):
     def kind(self):
        return "Square"
     
     def invert_area(self, area):
        return area**(1/2.0)

     def dimname(self):
        return "L"
     
     def draw(self,turt): 
       import turtle
       wn = turtle.Screen() 
       L = self._dim
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
       

from math import pi

class Circle(Shape):
     def kind(self):
        return "Circle"
     
     def invert_area(self, area):
        return (area/pi)**(1/2.0)

     def dimname(self):
        return "r"
     
     def draw(self,turt): 
       import turtle
       wn = turtle.Screen() 
       scale = 30.0
       r = self._dim
       rshow = r*scale
       wn = turtle.Screen()
       turtle.circle(rshow)
       turtle.write("Click Me",font=("Arial", 20, "normal"))
       wn.exitonclick()   
       
      

#############################################################

if __name__ == "__main__":
    circle = Circle(10)
    triangle = Triangle(4)
    square = Square(4)

    print(circle)
    print(triangle)
    print(square)

    circle.draw(circle)
    triangle.draw(triangle)
    square.draw(square)
