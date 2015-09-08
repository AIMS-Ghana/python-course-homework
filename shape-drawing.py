#!/usr/bin/env python3


# shape objects calculate sides of figures, given the area
import shape_objects
# draw shape gives a single shape on the canvas
import draw_shape
import turtle

# inspect data for invalid row specifications
def check_input(figures):
    pass

# deal with given row
class paint:
    def __init__(self, row):
        self.__area = float(row[3])
        self.__color = row[1]
        self.__kind = row[0]
        self.__angle, self.__x, self.__y = float(row[2]),float(row[4]),float(row[5])


    def position(self, angle, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(angle)
        turtle.pendown()


    def draw(self):
        self.position(self.__angle, self.__x, self.__y)
        draw_shape.draw(self.__kind, self.__area, self.__color, cont = True)



# Program flow begins here
if __name__ == '__main__':
    import csv
    import sys
    with open(sys.argv[1]) as input_file:
        figures = csv.reader(input_file, delimiter = ',')
        check_input(figures)
        for row in figures:
            #Do diagram justice with data on turtle canvas
            thingy_bobby = paint(row)
            thingy_bobby.draw()
        if len(sys.argv) == 3:
            # Produce out file if asked to do so
            # Should fix this later so that turtle does not animate at all
            assert (''.join(sys.argv[-4:]) == '.eps'), 'The format of the output file is not appropiate. Please specify as \'filename.eps\''
            ts = turtle.getscreen()
            ts.getcanvas().postscript( file = sys.argv[2])