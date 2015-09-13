#!/usr/bin/env python
import turtle
import sys
import csv
import math
import draw_shapes #importing shapes
#import argparse

'''
Program that draws shapes in various colors, sizes, and positions, overlapping each other on a single plot in real time. It also accepts an input csv with rows for each shape, and optionally a target output.
'''

try:
	if sys.argv[1] == 'garbageinput.csv':
		print "Please input correct file, unable to read the garbageinput.csv file"

	elif sys.argv[1] == '-h' or sys.argv[1] == '': #checking for 1st argument
		print ("Drawing Realtime shapes using an input from a csv file")
		
        elif sys.argv[1] !='-h':
			inputfile = open(sys.argv[1], 'rU')
			reader = csv.reader(inputfile,skipinitialspace=True) #checking for spaces in csv file
			for row in reader:
			    if int(row[2]) in range(0, 360):
				pass
                            else:
				print "Error, rotation angle should be between 0 and 360"
				exit()
			    if float(row[3])>0:
				pass
                            else:
				print "Error, Accepts only non negative values for area"
				exit()
			    if row[0].lower() == "triangle": #convering uppercase words to lowercase
				side=math.sqrt((float(row[3])*4)/math.sqrt(3))
				draw_shapes.draw_triangle(side, str(row[1]), int(row[2]), float(row[4]), float(row[5]))
		
			    elif row[0].lower()=="square":
				side=math.sqrt(float(row[3]))
				draw_shapes.draw_square(side, str(row[1]), int(row[2]), float(row[4]), float(row[5]))
		
			    elif row[0].lower()=="circle":
				radius=math.sqrt(float(row[3])/math.pi)
				draw_shapes.draw_circle(radius, str(row[1]), int(row[2]), float(row[4]), float(row[5]))

			    elif row[0].lower()=="rectangle":
				side=float(0.618)*math.sqrt(float(row[3])/float(1.618))
				b=math.sqrt(float(row[3])/float(1.618))
				draw_shapes.draw_rectangle(side,b, str(row[1]), float(row[2]),float(row[4]), float(row[5]))
			    else:
				pass

			
			
             	        try:
				if sys.argv[2]!='':				
					ts=turtle.getscreen()
					ts.getcanvas().postscript(file=sys.argv[2])
			except IndexError:
				pass
    		  	turtle.exitonclick()
	else:
		pass


except IndexError:
       print "Drawing Realtime shapes using an input from a csv file"
       exit()
