#!/usr/bin/env python3

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
        return "Triangle"



    def invert_area(self, area):
       return 2*(area/3**(0.5))**(0.5)





    def dimname(self):
        return "Side"





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





class Square(Shape):
    def kind(self):
        return "Square"





    def invert_area(self, area):
        return area**(0.5)

    def dimname(self):
        return "Side"

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




from math import pi

class Circle(Shape):
	def kind(self):
        	return "Circle"
 	
	
	def invert_area(self, area):
        	return (area/pi)**(0.5)


	def dimname(self):
	        return "Radius"

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
    
if __name__ == "__main__":
    
    import sys
    #a = sys.argv[0]
    #b = sys.argv[1]
    #c = sys.argv[2]





    circ = Circle(10)
    print(circ)
    tria = Triangle(10)
    print(tria)
    squar = Square(10)
    print(squar)
