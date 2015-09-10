#!/usr/bin/python

import sys
import shape
import turtle
import csv

#defining the various shapes
    

def draw_circle(radius,fill=True):
    turtle.color()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    #ends circle function
     

def draw_square(side,fill=True):
    turtle.color()
    turtle.begin_fill()
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)  
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)  
    turtle.end_fill()

def draw_rectangle(side,fill=True):
    turtle.color()
    turtle.begin_fill()
    turtle.forward(side*1.5)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)  
    turtle.forward(side*1.5)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)  
    turtle.end_fill()
	
	
    #ends rectangle function
 

def draw_triangle(side, fill=True):
    turtle.color()
    turtle.begin_fill()
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.end_fill()
    

def draw(name, color, angle, area, x, y):
    # seting the color for drawing the various shapes (uses color)
    turtle.color((color))    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(angle)
    if name == "TRIANGLE":
       draw_triangle(area)
    elif name == "CIRCLE": 
       draw_circle(area)  
    elif name == "SQUARE":
       draw_square(area)
    elif name=="RECTANGLE":
       draw_rectangle(area)         
    else:
        pass
        
if __name__ == "__main__":
	
    try:
        filename=sys.argv[1]
    
       # reading the csv file
        for row in csv.reader(open(filename)):
            draw(row[0],row[1],float(row[2]),float(row[3]),float(row[4]),float(row[5]))	
        ts=turtle.getscreen()
	ts.getcanvas().postscript(file="output.eps")
	turtle.exitonclick()
	
    except IndexError:
	print "ERROR:>>>>Must add a valid csv file that corresponds with the program<<<<<" 
    except ValueError:
        print "Error:..... Wrong csv input......."
    except IOError:
        print ">>>>This is a draw shape program. This program draws rectangles,circles,squares and triangles of various sizes and colors. You must give it a csv file that corresponds with that of the program else it would give you an error <<<<<" 

        

    
