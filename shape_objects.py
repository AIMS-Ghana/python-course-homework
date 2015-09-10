#!/usr/bin/env python
import math

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

    def draw(self, turt,fill,degree,x_org,y_org):
        pass

class Triangle(Shape):
  
    def kind(self):
        return "Equilateral Triangle"

    def invert_area(self,area):
	return math.sqrt (float(area*4) / float(math.sqrt(3)))

    def dimname(self):
        return "Side"

    def draw(self, turt,fill,degree,x_org,y_org):
        turt.penup()
        turt.setheading(degree)
        turt.setposition(x_org,y_org)
        turt.pendown()
    	turt.color(fill)
    	turt.fill(True)
	turt.begin_fill()
        #turt.left(degree)
	for i in range(3):
                
		turt.forward(self.dim)
		turt.left(120)
	turt.end_fill()
        


class Square(Shape):
      def kind(self):
        return "Square"

      def invert_area(self,area):
	return (float(area)**(0.5))

      def dimname(self):
        return "Side"

      def draw(self,turt,fill,degree,x_org,y_org):
            turt.penup()
            turt.setposition(x_org,y_org)
            turt.pendown()
    	    turt.color(fill)
	    turt.fill(True)
	    turt.begin_fill()
	    turt.left(degree)
	    turt.forward(self.dim)
	    
	    turt.left(90)
	    turt.forward(self.dim)
	   
	    turt.left(90)
	    turt.forward(self.dim)
	    
	    turt.left(90)
	    turt.forward(self.dim)
	   
	    turt.left(90)
	    turt.end_fill()



class Rectangle(Shape):
      def kind(self):
        return "Golden Rectangle"

      def invert_area(self,area):
        length = (float(area)*1.618)**0.5
        breadth = float(length)/1.618
	return [length,breadth]

      def dimname(self):
        return "Sides"

      def draw(self,turt,fill,degree,x_org,y_org):
	    turt.penup()
            turt.setposition(x_org,y_org)
            turt.pendown()
    	    turt.color(fill)
	    turt.fill(True)
	    turt.begin_fill()
	    turt.left(degree)
	    turt.forward(self.dim[0])
	    
	    turt.left(90)
	    turt.forward(self.dim[1])
	   
	    turt.left(90)
	    turt.forward(self.dim[0])
	    
	    turt.left(90)
	    turt.forward(self.dim[1])
	   
	    turt.left(90)
	    turt.end_fill()


from math import pi

class Circle(Shape):
      def kind(self):
        return "Circle"

      def invert_area(self,area):
	return math.sqrt(float(area)/math.pi)

      def dimname(self):
        return "Radius"

      def draw(self, turt,fill,degree,x_org,y_org):
        turt.penup()
        turt.setpos(x_org,y_org)
        turt.pendown()
	turt.color(fill)
        turt.fill(True)
        turt.begin_fill()
	turt.circle(self.dim)
        turt.end_fill()


if __name__ == "__main__":
    import turtle
    circ = Circle(1000)
    square = Square(4000)
    triangle = Triangle(34000)
    print(circ)
    print(square)
    print(triangle)
    '''
    triangle.draw(turtle)
    square.draw(turtle)
    circ.draw(turtle)
    '''
