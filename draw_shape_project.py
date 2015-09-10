#!/usr/bin/env python

import sys
import shapes
import turtle
import csv
import argparse

#filename='data.csv'
#for row in csv.reader(open(filename)):
    #fill=row
    

def draw_circle(radius,fill=True):
    turtle.color()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    #turtle.exitonclick()
     

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
	
	
    #turtle.exitonclick()
 

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
    # seting color for drawing (uses color)
    turtle.color((color))
    #goto the location to draw (uses x, y)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    # rotate pen (rotation)
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
    if len(sys.argv)>1:
	    if str(sys.argv[1]) =='-h' or str(sys.argv[1]) =='-g':
		parser = argparse.ArgumentParser(description='Drawing Shapes Code.')
		parser.add_argument('-g', type=str, dest='inp',
				   help='input csv file required')
		args = parser.parse_args()
		print("\n", args, args.inp)

	    try:
		filename=sys.argv[1]
	    
	       # reading the csv file
		for row in csv.reader(open(filename)):
		    draw(row[0],row[1],float(row[2]),float(row[3]),float(row[4]),float(row[5]))	
		
	    except IndexError:
		pass
		#print "Useful info about usage" 
	    except ValueError:
		print "Error indicating wrong csv input"
	    except IOError:
		print "wrong csv file entered" 
	    try:

		    t = turtle.getscreen()
		    t.getcanvas().postscript(file= sys.argv[2], colormode ="color")   
		    turtle.exitonclick() 
	    except IndexError:
		pass       

    else:
        pass
    
